# Chapter 24 — Black Holes and Curved Spacetime

*What a dying mathematician found in Einstein's equations while the war was ending around him.*

---

In 1916, a German mathematician named Karl Schwarzschild was dying in a military hospital on the Russian front, sick with a disease contracted during World War I. In the weeks before he died, he solved Einstein's field equations for a perfectly spherical, non-rotating mass — the cleanest possible case — and found something that disturbed him.

His solution said: if you compress enough mass into a small enough volume, a boundary forms. Cross that boundary and you cannot get out. Not because you're too slow. Not because something is blocking you. But because the geometry of space itself makes escape impossible. Light — the fastest thing in the universe — cannot cross it going outward.

Schwarzschild sent the paper to Einstein from the front, and Einstein presented it to the Prussian Academy of Sciences. Then, for decades, physicists quietly agreed to ignore the troubling part. The boundary — the singularity — was surely a mathematical artifact. The universe probably didn't do this.

Schwarzschild did not live to see any of it. The disease was pemphigus, an autoimmune condition that blisters the skin; it killed him in May 1916, a few months after he mailed the solution that now bears his name.

The universe, it turns out, does what his equations predicted, constantly. The galaxy is full of the remnants of dead massive stars that have collapsed exactly as Schwarzschild's equations predicted. We've found dozens of them in binary star systems, watched stars orbiting an invisible object of about 4.3 million solar masses at the center of our own Galaxy, detected the ripples in spacetime from two black holes colliding a billion years ago and a billion light-years away, and photographed the shadow of a six-and-a-half-billion-solar-mass black hole at the center of galaxy M87.

This chapter explains three things. First, what gravity actually is according to Einstein — not a force, but the curvature of spacetime. Second, what the event horizon is and why it forms. Third, how we detect objects that, by definition, emit no light.

![From mathematical curiosity to confirmed observation in one century. Each milestone closed a gap between theory and evidence.](images/24-black-holes-and-curved-spacetime-fig-01.png)
*Figure 24.1 — Timeline of black hole confirmation *

---

## Gravity Is Not a Force

Here is a puzzle that Einstein found beautiful. You are in an elevator when the cable snaps. For the brief moment of free fall, you float. If you held a ball at arm's length and let go, it would hang beside you — not falling to the floor, because it is falling at exactly the same rate you are. A scale under your feet would read zero.

This is obvious, and yet it is strange. What does it mean that gravity has disappeared?

Einstein's answer was this: gravity didn't disappear. There was never any gravity. Or more precisely — there is no distinction between free-falling in a gravitational field and floating in deep space with no gravity at all. If you were sealed in a windowless box and could perform any experiment you liked, no experiment would tell you whether you were falling toward Earth or drifting in empty space. These two situations are physically identical. Einstein called this the equivalence principle.

From this one observation — that free fall and weightlessness are indistinguishable — he made one of the greatest conceptual leaps in the history of physics. If the two situations are identical, then gravity cannot be a force. A force would cause something measurable. Falling freely, you measure nothing. Therefore, gravity is not a force.

What is it, then?

It is geometry. It is the curvature of spacetime.

Newton gave us a picture of gravity as a force: masses attract each other across empty space, instantly, following the inverse-square law. This picture is enormously useful. You can build bridges with it, send spacecraft to Saturn with it, calculate where Jupiter will be a thousand years from now with it. For most purposes, Newton is right.

But Newton's picture fails near compact, massive objects. It cannot explain what happens at the event horizon of a black hole, or why the perihelion of Mercury's orbit precesses slightly faster than Newton predicts, or why clocks run slower in stronger gravitational fields. For these things, you need Einstein.

Einstein's picture: space and time are not a fixed, passive backdrop against which events occur. Space and time are themselves a physical fabric — four-dimensional, elastic, shaped by the matter and energy within it. A massive object warps this fabric, the way a bowling ball warps a stretched rubber sheet. Other objects moving through the warped fabric follow paths that curve — not because a force is pulling them, but because they are following the straightest available path through a curved geometry. Mathematicians call the straightest path through a curved space a geodesic.

In flat spacetime (far from any mass), geodesics are straight lines. Light travels in straight lines. Objects with no forces on them travel in straight lines. This is Newton's first law, recovered as a special case.

In curved spacetime (near a massive object), geodesics are curves. Even light — which has no mass and experiences no gravitational force in Newton's picture — follows the curved geodesics of spacetime. It has to. There's nowhere else to go. Spacetime is all there is, and everything moves through it.

![Gravity is not pulling the light. The geometry of space has changed, and the light follows the only available path.](images/24-black-holes-and-curved-spacetime-fig-02.png)
*Figure 24.2 — Two panels *

This prediction was tested first during the total solar eclipse of 1919. Einstein had calculated that starlight passing close to the Sun's limb should be deflected by 1.75 arcseconds — not because gravity pulls on photons, but because spacetime near the Sun is curved. Arthur Eddington's expedition photographed stars near the Sun during totality and measured the apparent displacement of their positions. The result matched Einstein's prediction. The Sun was bending space, and light was following.

Three other tests confirm the theory with increasing precision. Mercury's perihelion advances by 43 arcseconds per century more than Newton predicts — general relativity accounts for every arcsecond. Clocks at higher elevations run faster than clocks at lower elevations — confirming that time itself runs slower in stronger gravitational fields, an effect so important that GPS satellites must correct for it or accumulate positional errors of kilometers per day. And gravitational waves — ripples in spacetime — travel at exactly the speed of light, as the theory predicts.

The price of this picture is that it is harder to visualize than a force. But it is more accurate, more complete, and in a deep sense more honest about what gravity actually is.

| Test | Newton predicts | Einstein predicts | What was observed |
| --- | --- | --- | --- |
| Mercury's perihelion | No extra precession | +43 arcseconds/century | Matches Einstein exactly |
| Starlight at the Sun's limb | 0.87 arcsecond (mass on light only) | 1.75 arcseconds (curved spacetime) | 1.75 arcseconds (Eddington, 1919) |
| Clocks in gravity (GPS) | No effect | Lower clocks run slower | GPS corrects ~38 µs/day or drifts ~10 km/day |
| Speed of gravitational waves | Not predicted | Exactly the speed of light | Confirmed (GW170817, 2017) |

---

## The Event Horizon

Newton's escape velocity gives you the speed an object must reach to escape a gravitational field. From Earth's surface, it's 11 km/s. From the Sun's surface, 618 km/s. As you compress an object — keeping its mass constant while shrinking its radius — the surface gets closer to all that mass, and the escape velocity climbs.

Carry this thought to its logical end. Keep compressing the Sun. When its radius shrinks to about 3 kilometers, the escape velocity at its surface equals the speed of light. Press further, and the escape velocity exceeds the speed of light. Nothing can escape — not because we lack a fast enough rocket, but because the speed of light is the universal speed limit, and even that is not enough.

In Newton's picture, this is a mathematical curiosity. In Einstein's picture, it is a statement about geometry. When mass is compressed to the Schwarzschild radius, the curvature of spacetime becomes so extreme that every available path — including the path of light — curves back inward. There are no outward-pointing geodesics. Escape is not merely difficult; it is geometrically impossible. This is the event horizon.

The Schwarzschild radius is:

$$R_S = \frac{2GM}{c^2}$$

where $G$ is Newton's gravitational constant, $M$ is the mass, and $c$ is the speed of light.

For the Sun ($M = 2 \times 10^{30}$ kg), this gives $R_S \approx 3$ km. For Earth ($M = 6 \times 10^{24}$ kg), $R_S \approx 9$ mm — smaller than a marble. For a pickup truck, $R_S \approx 10^{-24}$ m, smaller than a proton.

The formula depends only on mass. Nothing else. Not what the object is made of, not its temperature, not its history. Only mass determines the critical radius.

![The Schwarzschild radius spans 28 orders of magnitude in size across the mass range of known black holes.](images/24-black-holes-and-curved-spacetime-fig-03.png)
*Figure 24.3 — Schwarzschild radius comparison across scales *

The event horizon is not a physical surface. There is no shell, no wall, no detectable barrier. If you fell through it, you would not feel it. You would not see it. To a freely falling observer, the event horizon is locally indistinguishable from ordinary space. This is the equivalence principle again: locally, free fall looks like the absence of gravity. The horizon is a global feature of the geometry, not a local one.

What makes it remarkable is what happens to the paths available to you once you've crossed it. Outside the event horizon, you can send signals outward or inward. You have options. Inside the event horizon, every available path — even the path of light moving directly away from the center — eventually curves back toward the singularity. You have no options. The future has only one direction.

This is the feature that physicists mean when they say the event horizon is a one-way membrane. Not that something stops you at the boundary, but that on the other side, the structure of spacetime itself has changed.

![The event horizon is not a wall. It is the boundary where the future changes direction.](images/24-black-holes-and-curved-spacetime-fig-04.png)
*Figure 24.4 — Light cone diagram showing the event horizon *

Let me compute a real example. Astronomers have tracked stars at the center of the Milky Way for thirty years, measuring their positions and velocities with infrared telescopes. The stars trace elliptical orbits around an invisible point. Applying Kepler's third law — the same relationship between orbital period and radius that Kepler found for planets around the Sun — gives the mass of the central object: about 4.3 million solar masses, confined to a volume less than the orbit of Mercury.

The Schwarzschild radius of a black hole of that mass:

$$R_S = \frac{2 \times (6.67 \times 10^{-11}) \times (4.3 \times 10^6) \times (1.99 \times 10^{30})}{(3 \times 10^8)^2} \approx 1.3 \times 10^{10} \text{ m}$$

About 13 million kilometers — roughly one-fifth the radius of Mercury's orbit. This object, Sagittarius A*, is invisible at optical wavelengths, not because it is dark in the sense of reflecting no light, but because it is a black hole, and the geometry of its spacetime permits no light to escape from within that 12-million-kilometer boundary.

![Stars orbit the Galactic center as if something with about 4.3 million solar masses sits there. The object is invisible. Kepler's law identifies it.](images/24-black-holes-and-curved-spacetime-fig-05.png)
*Figure 24.5 — Stellar orbits around Sagittarius A* *

One important correction to a persistent misconception: black holes are not cosmic vacuum cleaners. They do not suck. A black hole's gravitational field at large distances is identical to that of the ordinary star that formed it. If the Sun magically became a black hole — it can't, it's too low mass, but suppose — Earth's orbit would be unchanged. We would continue orbiting the same as now, in permanent darkness, at the same distance, experiencing the same gravitational acceleration. The black hole's effect differs from the original star only when you get very close — within a few Schwarzschild radii.

---

## Seeing the Invisible

A black hole emits no light. So how do we know they exist?

We look for what they do to things around them.

**X-ray binaries.** About half of all stars are in binary systems. If one star in a binary is massive enough to die as a black hole, and if its companion later expands into a red giant, the outer layers of the red giant can be drawn toward the black hole. The gas doesn't fall straight in — orbital motion causes it to spiral, forming a flattened accretion disk. In the inner regions of this disk, gas orbits at nearly the speed of light. Friction heats it to 100 million Kelvin. At that temperature, the dominant emission is X-rays.

The X-rays are detectable from Earth. The source flickers on timescales of seconds to milliseconds — the orbital period near the event horizon. And the companion star's spectral lines show Doppler shifts, oscillating as the star orbits the invisible object.

By measuring the orbital period and the companion star's velocity, Kepler's law gives the mass of the invisible companion. In Cygnus X-1, the first confirmed black hole binary, the invisible companion has a mass of about 21 solar masses. White dwarfs can't exceed about 1.4 solar masses before collapsing further. Neutron stars can't exceed about 3 solar masses. An invisible object with 21 solar masses in a binary system has only one possible identity.

This is not a direct detection. It is an inference from orbital mechanics and X-ray emission. But the inference is tight. We now know of more than a dozen stellar-mass black holes in binary systems, with masses ranging from 5 to 21 solar masses.

![The black hole is invisible. The X-rays from the disk and the companion star's orbital motion together make its presence unmistakable.](images/24-black-holes-and-curved-spacetime-fig-06.png)
*Figure 24.6 — X-ray binary schematic *

**Gravitational waves.** In September 2015, the LIGO detectors — two instruments in Louisiana and Washington, each consisting of two perpendicular laser-beam arms four kilometers long — measured something that shook the infrastructure of physics. Both instruments registered a signal lasting about 0.2 seconds, rising in frequency from 35 to 150 Hz. It was the chirp of two black holes spiraling together.

The LIGO instrument measures gravitational waves — ripples in spacetime itself. Einstein had predicted them in 1916, as a direct consequence of his equations. An accelerating mass should create disturbances in the spacetime fabric that propagate outward at the speed of light, alternately stretching and squeezing space as they pass. The effect is almost incomprehensibly small — a gravitational wave from a black hole merger a billion light-years away stretches LIGO's four-kilometer arm by less than one ten-thousandth the diameter of a proton.

What LIGO detected on September 14, 2015, was two black holes — one about 36 solar masses, one about 29 solar masses — that had been spiraling together for billions of years. In their final fraction of a second, they merged, converting roughly three solar masses of mass directly into gravitational wave energy. For that instant, the power output exceeded the combined luminosity of all visible stars in the observable universe.

The signal arrived at the Louisiana detector 7 milliseconds before the Washington detector — consistent with a wave traveling at the speed of light from a source in the southern sky. Both detectors registered the same characteristic shape: a rapid increase in frequency (the chirp) as the black holes spiraled faster, then a ringdown as the merged object vibrated and settled.

This was not an inference. This was spacetime itself vibrating against our instruments. The result won the Nobel Prize in Physics in 2017, and since then, LIGO and its partner detectors — Virgo in Italy and KAGRA in Japan — have turned a single event into a catalogue. By the close of the fourth observing run in late 2025, the confirmed count of gravitational-wave events since 2015 had passed three hundred: black holes colliding with black holes, neutron stars colliding with black holes, neutron stars colliding with each other.

![Two detectors, separated by 3,000 km, registered the same signal 7 milliseconds apart. Spacetime had vibrated.](images/24-black-holes-and-curved-spacetime-fig-07.png)
*Figure 24.7 — LIGO schematic and GW150914 signal *

**The shadow of the event horizon.** In 2019, the Event Horizon Telescope Collaboration announced the first image of a black hole's shadow. The target was M87, a giant elliptical galaxy 55 million light-years away, whose central black hole has a mass of about 6.5 billion solar masses.

The Event Horizon Telescope is not a single instrument. It is a collection of radio telescopes scattered across Earth — from Hawaii to Chile to the South Pole — coordinated with atomic-clock precision and combined into an effective aperture as large as Earth itself. The method, called very-long-baseline interferometry, achieves the angular resolution needed to image the event horizon of supermassive black holes.

The image shows a ring of bright emission — gas heated by the black hole, swirling in an accretion disk — surrounding a dark central region. That dark region is the shadow: the silhouette cast by the event horizon against the bright background. The size and shape of the shadow are determined entirely by the black hole's mass and the geometry of general relativity. The observed shadow matched Einstein's prediction precisely. On 12 May 2022, the team released its image of Sagittarius A* at the center of our own Galaxy — the supermassive black hole Schwarzschild's equations had described a century before, now photographed in silhouette — and again, the geometry matched.

This is as close as you can get to a photograph of curved spacetime. The dark region is not a material object. It is the absence of light — light that entered the event horizon and will never return — surrounded by light that narrowly avoided that fate.

![The dark region is not the black hole. It is the shadow cast by the event horizon. Its size and shape are determined entirely by general relativity — and they match.](images/24-black-holes-and-curved-spacetime-fig-08.png)
*Figure 24.8 — Event Horizon Telescope image of M87 black hole*

---

## What General Relativity Actually Predicts

General relativity makes a prediction that physicists find uncomfortable: inside the event horizon, all the matter that fell in continues to collapse. The quantum pressure that holds up a neutron star (the mutual repulsion of densely packed neutrons) is overwhelmed by gravity. The collapse continues until the density becomes formally infinite and volume becomes zero — a singularity. At the singularity, the mathematics of general relativity breaks down entirely.

This probably means general relativity is incomplete, not that an actual infinite-density point exists. The theory works brilliantly at human scales and at the scales of stars and galaxies. But at densities approaching the Planck scale — $10^{97}$ kg/m³ — quantum effects must become important, and we don't yet have a theory of quantum gravity that tells us what actually happens there.

The event horizon is real and the theory is confirmed. The singularity is a signal that the theory reaches its edge.

Physicists have a useful way to describe what is knowable about a black hole from the outside. A black hole is completely characterized by just three numbers: its mass, its rotation (angular momentum), and its electric charge. That's it. Whatever went into making it — hydrogen, iron, neutron star material, previous black holes — leaves no trace that can be detected from outside the event horizon. The information about what formed the black hole is hidden behind a boundary from which it can never escape. Physicists say "black holes have no hair," meaning no additional details stick out.

This raises a genuine puzzle: Stephen Hawking showed in 1974 that black holes should emit a faint thermal radiation from quantum effects near the event horizon — now called Hawking radiation — which would eventually cause them to evaporate. If this is right, then as the black hole evaporates, what happens to all the information about everything that fell in? Does it escape? Is it destroyed? This is called the black hole information paradox, and it remains genuinely unsolved.

---

## The Scale of It

Three masses. Three sizes. Three contexts in which black holes appear.

Stellar-mass black holes — 5 to 100 solar masses — form from the collapse of massive stars. They have Schwarzschild radii of 15 to 300 kilometers. They exist scattered through the Galaxy as the remnants of stars that died. In binary systems, their accretion disks glow in X-rays. Alone, they are invisible.

Intermediate-mass black holes — thousands to hundreds of thousands of solar masses — may form in dense star clusters. Their existence is still being confirmed. They are the least well-studied of the three classes.

Supermassive black holes — millions to tens of billions of solar masses — sit at the centers of nearly all large galaxies. The Milky Way's is about 4.3 million solar masses. M87's is 6.5 billion. Their Schwarzschild radii range from millions to tens of billions of kilometers. They are, paradoxically, less dense on average than stellar-mass black holes: a four-million-solar-mass black hole has an average density inside its event horizon roughly comparable to air. The geometry is extreme, but the matter is not compressed into anything like the density you might imagine. The volume scales as the cube of the radius, and the radius scales with mass, so average density scales inversely with the square of the mass.

All three classes are described by the same equations. The Schwarzschild radius formula is scale-free. The equivalence principle holds everywhere. A physicist doing calculations near a stellar-mass black hole uses the same mathematics as one doing calculations near Sagittarius A*. The universe is, in this sense, economical.

| Class | Mass | Schwarzschild radius | How it forms | How we find it |
| --- | --- | --- | --- | --- |
| Stellar-mass | 5–100 M☉ | 15–300 km | Collapse of a massive star | X-rays from accretion; gravitational waves |
| Intermediate-mass | 10³–10⁵ M☉ | thousands of km | Possibly in dense star clusters | Still being confirmed |
| Supermassive | 10⁶–10¹⁰ M☉ | millions to billions of km | Galaxy-center growth over cosmic time | Stellar orbits; EHT imaging |

The density column hides a surprise: a four-million-solar-mass black hole has an average interior density lower than water, because the volume grows as the cube of the radius while the radius grows only in step with mass.

Two frontiers remain open. The first is whether any information can ever cross back out of an event horizon; a single confirmed instance would overturn the classical picture of the horizon as a strictly one-way membrane and force quantum effects into the geometry. The second is the singularity itself, where general relativity predicts infinite density and zero volume. Physicists are confident this signals the theory reaching its edge rather than a physical truth — a quantum theory of gravity would presumably smooth the infinity into something finite. We do not yet have that theory. The singularity is the place where our best current description of nature goes quiet.

---

## Sources

This chapter follows OpenStax *Astronomy* for the equivalence principle, the geometry of curved spacetime, the Schwarzschild radius, and the three classes of black hole. Karl Schwarzschild's 1916 solution, his service on the Eastern Front, and his death from pemphigus in May 1916 are historical record. The 1919 Eddington eclipse, Mercury's perihelion, and GPS time dilation are the classic tests of general relativity. GW150914 (detected 14 September 2015, announced 11 February 2016) earned the 2017 Nobel Prize; the LIGO-Virgo-KAGRA fourth observing run pushed confirmed detections past three hundred by late 2025. The Event Horizon Telescope imaged M87* in 2019 and Sagittarius A* on 12 May 2022. Cygnus X-1's ~21-solar-mass black hole reflects the 2021 Miller-Jones distance revision.
