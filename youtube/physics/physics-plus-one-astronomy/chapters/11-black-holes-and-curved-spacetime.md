# Chapter 11 — Black Holes and Curved Spacetime

*A dying mathematician on the Russian front in 1916, two laser arms in Louisiana stretching by a thousandth the width of a proton, and the first photograph of an object that emits no light.*

---

## Suggested titles

1. Black Holes and Curved Spacetime
2. The Shape of Gravity
3. What Geometry Does to Light

## TL;DR

Gravity is not a force pulling on things; it is the curvature of spacetime, and at sufficient density that curvature can close on itself into a one-way surface called an event horizon, which is real, photographable, and rings like a bell when two of them collide. The Schwarzschild radius $R_S = 2GM/c^2$ is the entire mechanism — a length scale set by mass alone, where the geometry runs out of outward-pointing futures.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the equivalence principle in plain language and explain why it implies gravity is geometry rather than a force.
2. **(Apply)** Use the Schwarzschild formula $R_S = 2GM/c^2$ to compute the event-horizon radius of any non-rotating mass, from a pebble to a supermassive black hole.
3. **(Apply)** Compute gravitational time dilation for an observer hovering near the event horizon using $t_\infty / t_r = 1/\sqrt{1 - R_S/r}$, and interpret what an infinite redshift means physically.
4. **(Analyze)** Read a black-hole observation — an X-ray binary spectrum, a LIGO chirp, an EHT image — and identify what is being measured, what is being inferred, and what is being assumed.
5. **(Apply)** Build an interactive D3 simulation of curved spacetime that shows geodesic paths, gravitational redshift, and the event horizon as a limit surface.

**Prerequisites.** Chapter 3 (light, the Doppler relation, photons). Chapter 9 (the death of massive stars, neutron-star mass limits). Algebra and an honest willingness to take one fact from special relativity — that nothing carrying information moves faster than $c$ — as a stated rule.

---

## Opening case: Karl Schwarzschild, Russian front, late 1915

In November 1915 Einstein presented the final form of his field equations to the Prussian Academy ([Einstein 1915](https://einsteinpapers.press.princeton.edu/vol6-trans/129)) — ten coupled nonlinear partial differential equations relating spacetime geometry to matter and energy. Einstein had only approximate solutions and did not expect exact ones for years.

Six weeks later a manuscript arrived from the Eastern Front. Karl Schwarzschild, a forty-two-year-old astronomer serving as a lieutenant in the German artillery, had solved the equations exactly for the cleanest case: empty space outside a single non-rotating spherical mass. He was already ill with pemphigus, contracted in the trenches. Einstein read the paper, replied that he "had not expected that the exact solution of the problem could be formulated so simply," and presented it on Schwarzschild's behalf in January 1916 ([Schwarzschild 1916](https://link.springer.com/article/10.1007/s00016-008-0411-5)). Schwarzschild died four months later.

The solution contained a length, $R_S = 2GM/c^2$. For the Sun, about three kilometers. For the Earth, about nine millimeters. Inside this radius, Schwarzschild's equations did something the people reading them did not know how to interpret: certain terms went to zero, others to infinity. Light directed straight out from this surface hung in place.

For half a century physicists treated this as a mathematical pathology — a flaw in the coordinates, surely. The universe does it constantly. We have now heard two of these objects collide, watched stars orbiting one at our Galaxy's center, and photographed the silhouette of another. This chapter is what Schwarzschild's three kilometers turned out to mean.

---

## Core concept

### Spacetime curvature: gravity as geometry

Start with the puzzle Einstein returned to in lectures. You are in an elevator. The cable snaps. For the few seconds before impact, you are weightless. Take a pen from your pocket and let go: it floats beside you. A scale under your feet reads zero. Inside the elevator, no experiment will tell you whether you are falling toward Earth or drifting in deep space.

Newton's account says a force pulls you down at $9.8\text{ m/s}^2$. Where did it go? Einstein's answer, worked out in 1907, was that the force was never there. Free-fall and inertial drift are physically identical. He called this the **equivalence principle** and spent the next eight years working out its consequences. If free-fall is indistinguishable from drift, a force cannot be doing the work — a force would produce measurable acceleration, and free-fall measures zero. Something else is. Einstein's answer: the geometry of spacetime itself.

Space and time are a single four-dimensional fabric, and mass-energy bends it. Objects with no forces on them follow the straightest available paths through that fabric — **geodesics**. In flat regions, the geodesic is a straight line (Newton's first law). Near a massive object, the geodesic is a curve. A planet orbits the Sun not because the Sun pulls on it, but because spacetime around the Sun is shaped like a bowl, and the planet is rolling along the straightest path available.

The standard analogy is a bowling ball on a rubber sheet — the ball depresses the sheet, marbles rolling past curve toward it. I use it because it is the only halfway-visualizable picture we have, and I want to name where it breaks. *It is two-dimensional* (spacetime is four-dimensional; nobody can picture it). *It uses gravity to explain gravity* — marbles roll downhill on the sheet because of Earth's gravity; the analogy smuggles in what it tries to explain. *It misses time*, where most of the curvature near Earth actually lives — a clock at the bottom of a building runs slightly slower than one at the top, and that difference, integrated along a falling object's path, is most of what we call gravity. *It suggests black holes are deep wells things fall into.* They are not wells; they are regions where time and space have rearranged so that what was the "out" direction in space has become the "past" direction in time. Take what intuition the sheet offers — mass changes geometry, unforced motion follows it — and discard the rest.

Einstein's theory makes quantitative predictions Newton's does not. Mercury's perihelion advances by 43 arcseconds per century more than Newton predicts; GR supplies exactly 43. Starlight passing the Sun is deflected by 1.75 arcseconds, twice the Newtonian value; Eddington's 1919 eclipse expedition confirmed it ([Dyson, Eddington & Davidson 1920](https://royalsocietypublishing.org/doi/10.1098/rsta.1920.0009)). GPS-satellite clocks run 38 microseconds per day faster than ground clocks ([Ashby 2003](https://link.springer.com/article/10.12942/lrr-2003-1)). Gravitational waves travel at $c$, confirmed to within $10^{-15}$ by GW170817 ([Abbott et al. 2017](https://iopscience.iop.org/article/10.3847/2041-8213/aa91c9)). Every test has confirmed the theory.

### The Schwarzschild radius and the event horizon

This is the deep-dive. Derive the event horizon two ways and watch them agree.

**The Newtonian estimate.** Escape velocity from a body of mass $M$ and radius $r$ comes from equating kinetic and gravitational potential energy: $v_{\text{esc}} = \sqrt{2GM/r}$. For Earth, 11.2 km/s. For the Sun's surface, 618 km/s. Compress a mass while keeping it intact: $v_{\text{esc}}$ climbs. At what radius does $v_{\text{esc}} = c$? Set them equal: $r = 2GM/c^2$. John Michell did this in two lines in 1783 ([Michell 1784](https://www.jstor.org/stable/106576)), Laplace independently in 1796. The Newtonian derivation is wrong about almost everything — it treats light as a massive ballistic particle, ignores time dilation — and gives exactly the right answer. Physics is occasionally generous.

**The general-relativistic mechanism.** Schwarzschild's exact solution gives two pieces of geometry that matter here. The first is the relation between time at radius $r$ and time at infinity:

$$\frac{dt_\infty}{dt_r} = \frac{1}{\sqrt{1 - R_S/r}}$$

A clock at radius $r$ ticks $\sqrt{1 - R_S/r}$ times slower than one far away. At $r = 2 R_S$, the ratio is $1/\sqrt{0.5} \approx 1.41$. At $r = 1.01 R_S$, the ratio is $\approx 10$. At $r = R_S$ exactly, the denominator is zero and the ratio diverges. Time, as seen from outside, stops.

The second piece: light emitted from radius $r$ and received far away has its wavelength stretched by the same factor.

$$\frac{\lambda_\infty}{\lambda_r} = \frac{1}{\sqrt{1 - R_S/r}}$$

This is **gravitational redshift**. As $r \to R_S$, the wavelength goes to infinity. A photon emitted from the event horizon is redshifted to zero frequency before it reaches us. We see nothing.

The event horizon is the surface of infinite redshift. It is also the surface beyond which all light cones tilt inward — at $r < R_S$ the radial coordinate becomes timelike, so *decreasing $r$* is a future direction, the way *increasing $t$* is for us. There is no path that stays at constant $r$ inside, just as there is no path for us that stays at constant $t$. The future points inward.

Run the formula: $R_S(M_\odot) \approx 2{,}954$ m. The formula scales linearly with mass: $R_S = 2.95 \text{ km} \times (M/M_\odot)$. A ten-solar-mass remnant has $R_S \approx 30$ km. Sagittarius A* (four million solar masses) has $R_S \approx 1.2 \times 10^7$ km, about a fifth of Mercury's orbital radius. M87* (six-and-a-half billion solar masses) has $R_S \approx 2 \times 10^{10}$ km — larger than the entire solar system.

The formula contains only mass. Not composition, not temperature, not history. A stationary black hole is characterized entirely by mass, angular momentum, and (in principle) electric charge — three numbers, all an outside observer can ever measure ([Israel 1967](https://journals.aps.org/pr/abstract/10.1103/PhysRev.164.1776); [Carter 1971](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.26.331)). Whatever fell in is erased from the outside view.

The event horizon is not a physical surface in the way a planet's is. No shell, no wall, no detectable barrier. A freely falling observer crossing it experiences nothing locally — the equivalence principle still holds; locally the geometry is flat. The horizon is a global property, visible only by comparing what is happening here with what is happening at infinity. It is the surface from which no future-directed path leads outward.

### Observational evidence: gravitational waves and the EHT image

The theory is beautiful. The question is whether nature actually does it.

**Stars orbiting Sgr A\*.** Reinhard Genzel's group at MPE and Andrea Ghez's at UCLA spent two decades tracking individual stars at the Galactic center ([Ghez et al. 2008](https://iopscience.iop.org/article/10.1086/592738); [Gillessen et al. 2009](https://iopscience.iop.org/article/10.1088/0004-637X/692/2/1075)). One star, S2, has a sixteen-year orbital period; both teams watched it complete a full orbit. Kepler's third law gives the mass of the invisible object S2 orbits: $4.1 \times 10^6\, M_\odot$, packed inside a volume smaller than 17 light-hours across. Nothing known to physics does that except a black hole. Genzel and Ghez shared the 2020 Nobel Prize ([Nobel scientific background, 2020](https://www.nobelprize.org/uploads/2020/10/advanced-physicsprize2020.pdf)).

**LIGO and the chirp.** On September 14, 2015, the two LIGO detectors — Hanford, Washington and Livingston, Louisiana, each two perpendicular four-kilometer laser arms — registered a 0.2-second signal in which the arms stretched and squeezed by about $10^{-18}$ m, less than a thousandth the diameter of a proton ([Abbott et al. 2016](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102)). The waveform rose from 35 Hz to 150 Hz — a *chirp* — then rang down. Matching it against general-relativistic templates gave the source: two black holes, 36 and 29 solar masses, spiraling together 1.3 billion light-years away. In the final fraction of a second they merged into a 62-solar-mass remnant, radiating the missing three solar masses as gravitational-wave energy. For that instant, the gravitational-wave luminosity exceeded the combined electromagnetic output of every star in the observable universe.

The signal arrived at Livingston 6.9 ms before Hanford, consistent with a wave at the speed of light from the southern sky. No terrestrial noise source produces matched waveforms in two detectors 3,000 km apart with the right delay. The 2017 Nobel Prize went to Weiss, Barish, and Thorne; LIGO and Virgo have now catalogued more than ninety mergers.

**The Event Horizon Telescope image.** On April 10, 2019, the EHT Collaboration released a photograph of M87*, the six-and-a-half-billion-solar-mass black hole at the center of M87, 55 million light-years away ([Akiyama et al. 2019](https://iopscience.iop.org/article/10.3847/2041-8213/ab0ec7)). The image shows an asymmetric ring of light — hot plasma in the accretion flow — around a dark central region about 40 microarcseconds across. The dark region is the **shadow**: photons whose trajectories took them too close to the horizon and were captured. General relativity predicts a shadow diameter of about $5.2 R_S$; observed and predicted agreed within a few percent. The EHT is eight radio observatories synchronized by hydrogen-maser clocks, operating as one Earth-sized interferometer. In 2022 the collaboration published Sgr A*'s image ([Akiyama et al. 2022](https://iopscience.iop.org/article/10.3847/2041-8213/ac6674)), and again the ring matched the GR prediction.

Three independent measurements — Newtonian dynamics of an orbiting star, geometric optics of a hot accretion flow, and spacetime strain — agree on the same theory.

---

## Worked example: Schwarzschild radii for the Sun, Earth, and Sgr A\*

Run the formula three times.

**The Sun.** $M = 1.989 \times 10^{30}$ kg.

$$R_S = \frac{2(6.674 \times 10^{-11})(1.989 \times 10^{30})}{(2.998 \times 10^8)^2} \approx 2{,}953 \text{ m}$$

About three kilometers. The Sun's actual radius is $6.96 \times 10^8$ m — roughly $2 \times 10^5$ times larger. The Sun will never become a black hole; its mass is well below the threshold for core collapse.

**The Earth.** $M = 5.972 \times 10^{24}$ kg gives $R_S \approx 8.87 \times 10^{-3}$ m, less than a centimeter. Earth's actual radius is $6.4 \times 10^6$ m; the ratio is about $7 \times 10^8$. No astrophysical process compresses planet masses to that density.

**Sagittarius A\*.** $M = 4.1 \times 10^6 \, M_\odot$ gives $R_S \approx 1.21 \times 10^7$ km using linear scaling. Mercury's orbital distance from the Sun is $5.8 \times 10^{10}$ m. Sgr A*'s event horizon is about a fifth of Mercury's orbital radius — smaller than the inner solar system, larger than the Sun itself.

**Time dilation at $r = 1.01\, R_S$.** $dt_\infty/dt_r = 1/\sqrt{1 - 1/1.01} \approx 10$. A clock hovering one percent above the horizon ticks ten times slower than one on Earth. At $r = 1.0001\, R_S$, the ratio is 100. The redshift is unbounded as $r \to R_S^+$. The infalling observer's own clock ticks normally — proper time is finite all the way across.

---

## Common misconceptions

- **"Black holes suck things in."** They do not have extra gravity. The gravitational field at large distances is identical to that of any other mass with the same $M$. If the Sun were replaced this instant by a one-solar-mass black hole, Earth would continue its orbit unchanged. The sky would go dark, but nothing would be "pulled in." Black holes differ from ordinary masses only within a few Schwarzschild radii.
- **"At the event horizon you'd be ripped apart by tidal forces."** Tidal force per unit length scales as $GM/r^3$. At the horizon, $r = R_S = 2GM/c^2$, so the horizon-tidal force scales as $1/M^2$ — it *falls* with mass. For a ten-solar-mass hole, horizon tides shred a human well before crossing. For a billion-solar-mass hole, horizon tides are gentler than a staircase. You cross M87*'s horizon without sensation. Whether the horizon kills you depends on mass.
- **"The rubber-sheet analogy is what's really happening."** It is not. It uses Earth's gravity to explain gravity, shows two of four dimensions, hides the time component where most everyday gravity lives, and makes black holes look like spatial wells. Take one intuition from it — mass changes geometry — and drop the rest.
- **"Inside the event horizon, you can still see out."** You can. Light from outside still reaches you. What you cannot do is send anything back, because every future-directed path now leads to the singularity. The horizon is one-way in the future direction, not opaque.

---

## Exercises

**Warm-up (Understand).** State the equivalence principle in one sentence. (a) Name one prediction of general relativity that follows from it. (b) Explain why "free fall is indistinguishable from drift" implies gravity is not a force.

**Application (Apply).** A neutron star has mass $1.4\, M_\odot$ and radius about 12 km. (a) Compute its Schwarzschild radius. (b) Compute the ratio of physical radius to $R_S$. (c) State why a small upward push in mass would tip this object into a black hole.

**Synthesis (Analyze).** GW150914 recorded merging black holes of 36 and 29 solar masses producing a 62-solar-mass remnant. (a) Compute the mass-energy radiated as gravitational waves using $E = \Delta M c^2$. (b) Compare to the Sun's total lifetime electromagnetic output (~$10^{44}$ J). (c) State one observational property of the chirp that no noise source local to a single detector could produce.

**Challenge (Analyze).** A hovering observer at $r = 1.5\, R_S$ emits a photon at 500 nm radially outward. (a) Compute the wavelength received at infinity. (b) At what $r$ would 500 nm redshift to 1 cm? (c) Explain why the result is about clocks at different radii, not photons "losing energy to climb out."

---

## LLM Exercises

### Build the spacetime-curvature simulator (`11-spacetime-curvature.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A two-panel D3 visualization. Left: a 2D deformed grid around a central mass, with a slider for $M$ from $0.1\, M_\odot$ to $10^9 \, M_\odot$. Draw a handful of geodesic paths — light rays and free-fall trajectories — that curve more sharply when $M$ is larger. Mark the Schwarzschild radius as a red circle, labeled with its numerical value. Right: a plot of gravitational redshift $\lambda_\infty / \lambda_r = 1/\sqrt{1 - R_S/r}$ vs. $r/R_S$ on a log $y$-axis, with a vertical cursor at the selected radius.
>
> **Say.** D3 v7. Compute $R_S = 2GM/c^2$ as the slider moves. Geodesic paths can be approximated — the visual cue is that they bend more sharply near the horizon. Add small-text disclaimer under the left panel: "Rubber-sheet visualization. Spacetime is 4D; this is 2D; the picture omits the time component where most everyday gravity lives."
>
> **Constrain.** D3 v7 only. No external relativity libraries. Filename: `11-spacetime-curvature.html`.
>
> **Verify.** (a) Slider at $1\, M_\odot$: horizon label ≈ 3 km. (b) Slider at $4 \times 10^6 \, M_\odot$: ≈ $1.2 \times 10^7$ km. (c) Cursor at $r = 1.01\, R_S$: redshift factor ≈ 10.

### Exploration

- Drive the mass slider from $1$ to $10^9 \, M_\odot$; the horizon radius scales linearly with mass.
- Read the redshift at $r/R_S = 2$. It should equal $\sqrt{2} \approx 1.414$ — half the redshift coefficient already accumulated by $2R_S$.
- Compare tidal stretching at a 1-solar-mass and $10^9$-solar-mass horizon. The larger hole's horizon tides are $\sim 10^{18}$ times weaker — why supermassive horizons are survivable in principle and stellar-mass ones are not.

### Bridge to Chapter 12

> **Show.** Sgr A* sits at the Milky Way's center at four million solar masses; M87* at M87's center at six billion. Every large galaxy we have looked at hard enough has one. What does the rest of a galaxy look like around the hole at its center?
>
> **Say.** Add a third panel showing the Milky Way's mass distribution — Sgr A*, bulge, disk, dark-matter halo — with the rotation curve overlaid. Mark Sgr A*'s radius of influence (~2 pc).
>
> **Verify.** Sgr A* dominates dynamics out to ~2 pc. Beyond, the bulge and disk take over; the rotation curve stays approximately flat to tens of kpc — the dark-matter signature Chapter 12 has to explain.

Save as `11b-galaxy-context-preview.html`. Lead-in to Chapter 12 — *The Milky Way and Galaxies*.

---

## What would change my mind

The chapter rests on one claim: that the objects we call black holes are genuine event horizons, not exotic compact objects that mimic the predictions while lacking a true horizon. A clean detection of light emerging from inside what should be the horizon — a thermal afterglow at the Hawking temperature, or a ringdown deviation consistent with a hard surface at $r$ slightly greater than $R_S$ — would force the question of whether what we have imaged are really horizons. Current LIGO ringdown measurements and EHT shadow imaging are consistent with GR horizons to within a few percent ([Abbott et al. 2021](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.122002)). A confirmed deviation, with every known systematic ruled out, would require rewriting most of this chapter.

## Still puzzling

- *The information paradox.* Hawking showed in 1974 ([Hawking 1974](https://www.nature.com/articles/248030a0); [Hawking 1975](https://link.springer.com/article/10.1007/BF02345020)) that black holes emit faint thermal radiation and eventually evaporate. If that radiation is purely thermal, the information about everything that fell in is destroyed — but quantum unitarity forbids information loss. Fifty years of theoretical work have not produced consensus on how the information escapes or whether the question is well-posed.
- *The firewall paradox.* [Almheiri, Marolf, Polchinski & Sully (2013)](https://link.springer.com/article/10.1007/JHEP02(2013)062) argued that resolving the information paradox requires the equivalence principle to fail at the horizon — an infalling observer would hit a "firewall" of high-energy radiation, contradicting Einstein's assumption that horizons are locally unremarkable. Proposed resolutions (ER = EPR, soft hair, replica wormholes) have not settled it.
- *Quantum gravity.* Inside the horizon, general relativity predicts collapse to a singularity of infinite density. This is almost certainly not what nature does — it is what an incomplete theory does when extrapolated past its regime. The event horizon is real and confirmed. The singularity is a placeholder for the theory that will replace it.

---

**Tags:** general relativity, Schwarzschild radius, event horizon, gravitational waves, LIGO, Event Horizon Telescope, Sgr A*, M87, equivalence principle, gravitational redshift, Hawking radiation
