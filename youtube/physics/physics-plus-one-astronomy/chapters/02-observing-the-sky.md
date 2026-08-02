# Chapter 2 — Observing the Sky

*A stick, a shadow, a well in Egypt, and a 47,500-kilometer planet — plus everything we had to invent before we could explain anything at all.*

---

## Suggested titles

1. Observing the Sky
2. The Sky as Instrument: Coordinates Before Mechanism
3. From a Shadow in Alexandria to Right Ascension

## TL;DR

The naked-eye sky forced humans to invent a coordinate system before they had any correct theory of what was moving. The coordinate system survived; the theory got replaced four times — Ptolemy to Copernicus to Kepler to Newton — over eighteen centuries that started with Eratosthenes measuring the whole planet using a stick.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define celestial sphere, celestial pole, ecliptic, obliquity, zodiac, solstice, equinox, parallax, right ascension, and declination in plain language and in the geometry of Earth's rotation and orbit.
2. **(Apply)** Reproduce Eratosthenes' measurement of Earth's circumference from a shadow angle and a north-south distance, and state the physical assumption that makes the calculation work.
3. **(Apply)** Use Kepler's third law (*T*² = *a*³, with *T* in years and *a* in AU) to predict the orbital period of any solar-system body from its average distance.
4. **(Analyze)** Distinguish daily motion (Earth's rotation) from annual motion (Earth's orbit), and explain seasons from axial tilt rather than orbital distance.
5. **(Apply)** Build an interactive D3 celestial-sphere simulation that responds to a latitude slider.

**Prerequisites.** Chapter 1 (powers of ten, AU, theory-as-prediction). Basic trigonometry — degrees, ratios, the small-angle approximation. No calculus.

---

## Opening case: a stick in Alexandria, ~240 BCE

Around 240 BCE, Eratosthenes — chief librarian at Alexandria — had read a traveler's report from Syene, a city about 800 kilometers south on the Nile: at noon on the summer solstice, the Sun stood directly overhead. A vertical stick cast no shadow. A column of light reached the bottom of a deep well.

Eratosthenes did one thing the traveler had not done. He waited for the same solstice in Alexandria, planted a stick, and measured the angle of its shadow — about 7.2° from vertical. From a stick in one city and a memory of a well in another, he calculated the circumference of the planet to within about 15% of the modern satellite value.

The calculation is in the worked example below. The move that lets it exist at all is this: Eratosthenes assumed the Sun is far enough away that its rays arrive parallel. With that assumption, the only way two vertical sticks at the same instant can cast different shadow angles is if the ground beneath them is curved. The shadow angle measures the curvature directly.

One observation, two cities, one physical assumption. The product: a planet's size, 1,900 years before the first satellite, with no instrument more complicated than a pole.

This chapter is what people did with the sky between Eratosthenes and Newton — and, more importantly, it introduces the coordinate system astronomers actually use, the one the next twelve chapters will assume.

---

## Core concept

### The celestial sphere — a useful fiction

Step outside on a dark night. Stars rise in the east, arc across the south (in the northern hemisphere), and set in the west. They keep their positions relative to each other. The arrangement rotates as a single rigid pattern, once around in roughly twenty-four hours, as if you were inside a slowly turning bowl.

That is what the sky *looks like*. It is not what is happening — Earth is turning, not the sky — but the description is exact, and the description is what astronomy starts from.

Extend Earth's rotation axis straight outward until it intersects an imaginary sphere centered on you. The two intersection points are the **celestial poles** — the points the sky appears to rotate around. The projection of Earth's equator onto the same sphere is the **celestial equator**. The **celestial sphere** is the imaginary surface on which every astronomical object appears to lie. Stars are at wildly different distances — Sirius 8.6 light-years, Betelgeuse roughly 550, Andromeda 2.5 million ([NASA NED](https://ned.ipac.caltech.edu/)) — but the eye reads only direction. Project everything onto a unit sphere centered on the observer and you have a two-dimensional map of every direction the eye can look.

The coordinates are direct analogs of latitude and longitude:

- **Declination (Dec)** — celestial latitude. +90° at the north celestial pole, 0° on the celestial equator, −90° at the south celestial pole. Polaris sits at Dec ≈ +89.3°.
- **Right ascension (RA)** — celestial longitude. Measured eastward around the celestial equator from a fixed zero (the vernal equinox), in hours, minutes, seconds. 24h = 360°, so 1h of RA = 15°.

(RA, Dec) is the modern address of every star, galaxy, quasar, and pulsar in every catalog you will read. Hipparchus introduced a version of this ~130 BCE. The geometry has not changed since. The coordinate system makes no claim about what is moving. That is its strength.

### Two motions, two causes

The sky does two distinct things, with two distinct causes.

**Daily motion.** Every star rises and sets once a day, tracing a circle around the celestial pole in 23h 56m 4s — the **sidereal day**, the time Earth takes to rotate once relative to the stars. (The 24-hour solar day is slightly longer because Earth has also moved along its orbit, and the Sun has to "catch up.") Cause: Earth's rotation.

**Annual motion.** The same star at the same clock time does not appear in the same place across a year. Constellations visible in January (Orion, Taurus) are absent in July. The Sun, against the background of the fixed stars, traces a complete circuit in one year. That circuit defines the **ecliptic** — the great circle the Sun traces as Earth orbits it. The twelve constellations the ecliptic passes through are the **zodiac**. Cause: Earth's orbit.

The ecliptic does not coincide with the celestial equator. It tilts. The angle between them is the **obliquity** of the ecliptic — currently 23.44°. The intersections are the **equinoxes** (vernal ~March 20, autumnal ~Sept 22). The extreme points are the **solstices** (summer ~June 21, Sun at Dec ≈ +23.44°; winter ~Dec 21, Sun at Dec ≈ −23.44°). That 23.44° tilt is the entire explanation of seasons.

### Why seasons come from tilt, not distance

Almost every adult I have asked thinks seasons happen because Earth gets closer to the Sun in summer. Simple, and wrong.

Earth's **eccentricity** is 0.0167 ([NASA Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)). Perihelion (closest approach) is around January 3 — northern-hemisphere winter. Perihelion and aphelion differ by 3.3%, producing ~6.7% difference in solar energy at the top of the atmosphere. Real but small, and the wrong sign for the distance story.

The cause is the 23.44° axial tilt. When the northern hemisphere is tilted toward the Sun (June solstice), two things happen at once: sunlight strikes at a steeper angle (more energy per square meter), and the day is longer (more accumulated energy). Together: summer. Six months later, tilted away: shallower light, fewer hours, winter. The southern hemisphere runs in reverse.

Clean test: the hemispheres have opposite seasons but the same distance from the Sun at any instant. Distance cannot explain a phenomenon that depends on which hemisphere you are in. Tilt can.

### The Moon and the eclipses

The Moon orbits Earth every 27.3 days (relative to the stars) and runs through phases every 29.5 days (relative to the Sun). Phases are pure geometry — the Moon is always half-illuminated; what changes is how much of the lit side faces Earth. New moon: lit side away. Full moon: lit side toward us. Crescent, quarter, gibbous: in-between angles.

**Eclipses** happen when Sun, Earth, and Moon line up. **Solar eclipse:** Moon's shadow on Earth. **Lunar eclipse:** Earth's shadow on the Moon. They do not happen every new and full moon because the lunar orbit is tilted ~5° to the ecliptic. The August 21, 2017 total solar eclipse path across the U.S. was published to the second and kilometer years in advance ([NASA GSFC Eclipse Bulletin](https://eclipse.gsfc.nasa.gov/SEpubs/20170821/RP-eclipse-bulletin-2017.html)). That is celestial mechanics tuned for three centuries on top of Newton.

### The historical arc, compressed

The mechanism of the sky was not available to ancient astronomers. They had only what the naked eye could record.

**Babylonian astronomers (~2000–500 BCE)** kept the longest continuous astronomical record in human history on clay tablets — synodic periods of every visible planet, lunar eclipses predicted with the **saros cycle** (an 18-year, 11-day pattern), the zodiac as twelve equal ecliptic segments. No model of *why* — only patterns and prediction. The cycles still work.

**Aristarchus of Samos (~270 BCE)** proposed heliocentrism nineteen centuries early. He was almost universally ignored, for a reason that was not foolish: if Earth orbited the Sun, nearby stars should appear to shift against more distant ones over the year — **parallax**, the same effect that makes a fence post slide against a hillside when you move your head. No parallax was observed. Either heliocentrism was wrong, or the stars were unimaginably far away. The second option seemed extravagant. (It was correct. First stellar parallax was measured in 1838 — the nearest stars are about 4 light-years out, parallax below 1 arcsecond.)

**Eratosthenes (~240 BCE)** measured Earth's circumference (worked example below). **Hipparchus (~130 BCE)** cataloged 850 stars, attempted parallax (failed for the right reason), and invented the apparent **magnitude scale** still in use today.

**Claudius Ptolemy (~150 CE)** wrote the *Almagest*. To match planetary positions geocentrically, he needed **epicycles** (small circles whose centers ride larger circles called **deferents**) plus a correction called the **equant**. Baroque, but functional — the standard astronomy text for thirteen centuries.

**Copernicus (1543)** moved the Sun to the center. **Retrograde motion** — the apparent backward looping of Mars, Jupiter, and Saturn — falls out automatically from Earth overtaking outer planets, without custom epicycles. Copernicus kept circular orbits (wrong) and still needed minor epicycles. His model was not dramatically more accurate than Ptolemy's. It was *more honest*: it eliminated the largest class of patches by changing one assumption.

**Tycho Brahe (1546–1601)** built the most precise pre-telescope observatory in the world, positions accurate to about 1 arcminute. He bequeathed twenty years of these to a young German assistant.

**Kepler (1571–1630)** spent eight years trying to fit Mars's orbit to a circle. The fit always failed by 8 arcminutes — within Brahe's precision, so the residual was real. Kepler abandoned circles, tried ellipses, and the fit was exact. Three laws ([*Astronomia Nova* 1609, *Harmonices Mundi* 1619](https://archive.org/details/AstronomiaNova)):

1. Every planet moves on an ellipse with the Sun at one focus.
2. The line from Sun to planet sweeps out equal areas in equal times.
3. *T*² = *a*³ — period squared equals average distance cubed (years, AU).

Empirical regularities. Kepler did not know *why* they held.

**Galileo (1610)** pointed a ~20× refractor at Jupiter on January 7 and noticed three "stars" in a line. By January 10 they had moved; by month's end a fourth had appeared — four objects orbiting Jupiter, the **Galilean moons** (Io, Europa, Ganymede, Callisto). The geocentric objection — *if Earth moved, the Moon would be left behind* — was now obviously wrong. Jupiter moved and carried four moons with it.

In the same months, Galileo watched Venus go through a full phase cycle — crescent, half, gibbous, full — with apparent size correlating with phase exactly as a heliocentric model required and Ptolemy's model forbade. In Ptolemy, Venus orbits between Earth and Sun and can never show more than a thin crescent. Galileo saw a full Venus. The phases of Venus *falsified* geocentrism. Not a stylistic argument — an empirical kill ([*Sidereus Nuncius*, 1610](https://archive.org/details/SidereusNuncius)).

**Newton (1687)** derived Kepler's three laws from one physical assumption in the *Principia*: *F* = *GMm/r*². The same law that pulls an apple down keeps the Moon in orbit. Newton unified terrestrial and celestial mechanics.

The coordinate system survived the whole journey. Ptolemy's mechanism did not. Copernicus's orbits did not. Kepler's empirical fit did, but had to wait for Newton to explain *why*.

---

## Worked example: how Eratosthenes measured a planet

Two facts:

**Fact 1.** At noon on the summer solstice, the Sun is directly overhead in Syene (modern Aswan, 24.09° N — close enough to the obliquity that the Sun passes nearly overhead on June solstice).

**Fact 2.** At the same instant in Alexandria — about 925 km north — a vertical stick casts a shadow at 7.2° from vertical.

**Geometry.** Assume the Sun is far enough that its rays are parallel. (Correct to better than one part in ten thousand — the Sun is about 24,000 Earth-radii away.) The only way two vertical sticks at the same instant can cast different shadow angles is if the verticals point in different directions, meaning the ground between them is curved. The angle between the two verticals equals the angle subtended at Earth's center by the arc between the cities. So 7.2° of shadow at Alexandria means the arc from Alexandria to Syene subtends 7.2° at Earth's center.

**Arithmetic.** The Alexandria-Syene arc is

$$\frac{7.2°}{360°} = \frac{1}{50}$$

of the full circumference. So:

$$C = 50 \times 925 \text{ km} = 46{,}250 \text{ km}$$

Modern satellite value: 40,075 km ([NASA Earth Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html)). Eratosthenes' answer is about 15% high. With a stick and a story about a well.

**Honest limit.** Eratosthenes reported in stadia, and the Greek stadium had several regional values; which one he used is disputed [verify — Greek stadium conversion historiography]. Different reasonable choices give answers from very close to the true value up to about 20% high. The apparent precision is partly an artifact of which conversion we pick. The *method* is exact. The error sits in inputs — distance, shadow angle, the assumption the cities lie on the same meridian (they do not, exactly), and parallel rays. Each error source is namable. None hide inside the geometry.

### Quick check on Kepler's third law

Run *T*² = *a*³ on three planets:

| Planet  | *a* (AU) | *a*³    | *T* (yr) | *T*²    |
|---------|----------|---------|----------|---------|
| Earth   | 1.000    | 1.000   | 1.000    | 1.000   |
| Mars    | 1.524    | 3.540   | 1.881    | 3.538   |
| Jupiter | 5.203    | 140.85  | 11.862   | 140.71  |

*a*³ and *T*² agree to three significant figures with no fitting parameter. An asteroid at *a* = 2.7 AU has *T*² = 19.68, so *T* ≈ 4.43 years — within a percent of any catalog value. Apply the law to a moon around Jupiter and the units change (period in Jupiter days, distance in Jupiter radii) but the cube-square scaling stays. The shape is geometry plus inverse-square. The constant is the mass.

---

## Common misconceptions

**"Seasons happen because Earth is closer to the Sun in summer."** No. Earth's eccentricity is 0.0167; closest and farthest distances differ by 3.3%, and Earth is closest in early January — northern winter. Seasons are entirely from the 23.44° axial tilt. Clean test: hemispheres have opposite seasons but the same distance from the Sun at any moment. Tilt can produce opposite-hemisphere effects; distance cannot.

**"Constellations are physical groupings of stars."** They are not. A constellation is a pattern formed by stars in nearly the same *direction* from Earth, regardless of *distance*. The stars of Orion's belt are at roughly 700, 1,200, and 700 light-years ([Hipparcos catalog](https://www.cosmos.esa.int/web/hipparcos)) — the row is a line-of-sight accident. Move 100 light-years sideways and Orion's belt disappears.

**"Stars appear to move at night because we are moving through space."** True in the long run — the solar system orbits the galactic center at 220 km/s — but that is not the nightly motion. Daily rotation of the sky is Earth spinning on its axis. Annual motion of the constellations is Earth's orbit at 30 km/s. Galactic motion shows up only over thousands of years as **proper motion**, first reported by Halley in 1718.

**"Ptolemy was wrong because he was unscientific."** He was not. He constructed a model that fit the data under the constraint of an assumption (Earth at center) that turned out to be incorrect. His geometry was sophisticated and his predictions were accurate enough for thirteen centuries of calendar-making and navigation. A model can be quantitatively useful and structurally incorrect at the same time.

---

## Exercises

**Warm-up (Understand).** For each, identify the cause: (a) the daily motion of stars; (b) the changing constellations visible at midnight across the year; (c) the seasons; (d) the phases of the Moon; (e) the slow drift of the celestial pole over millennia (precession).

**Apply.** A vertical stick in Quito, Ecuador (latitude ≈ 0°) casts no shadow at noon on which days of the year? At noon on the solstices, the Sun is at Dec ±23.44°. What angle does the shadow make in Quito at noon on (a) June solstice, (b) December solstice, (c) spring equinox?

**Apply.** Use Kepler's third law to estimate Neptune's orbital period (*a* = 30.07 AU). Check against a reference. What does the residual tell you about (a) the precision of *a* and (b) the validity of the inverse-square approximation inside the solar system?

**Challenge (Analyze).** Aristarchus proposed heliocentrism ~270 BCE; the first stellar parallax (Bessel, 61 Cygni) was measured in 1838 — about 2,100 years later. (a) Why was the absence of observed parallax a genuine, not just philosophical, objection? (b) Estimate the maximum parallax angle for a star 4.24 light-years away. (c) What is the smallest angle a careful naked-eye observer could plausibly resolve, and how many orders of magnitude does that exceed the parallax of the nearest star? (d) What does your answer say about the burden of proof Aristarchus actually faced?

---

## LLM Exercises

### Build the celestial-sphere simulator (`02-celestial-sphere.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** The celestial sphere as seen from Earth — celestial equator, ecliptic, celestial poles, and ~30 bright stars at their correct RA and Dec. A latitude slider (−90° to +90°) sets observer location; a time-of-year slider rotates the visible sky. The portion below the local horizon is dimmed.
>
> **Say.** Build an interactive D3 v7 visualization using stereographic projection centered on the local zenith. Draw the celestial equator and ecliptic as labeled great circles. Plot 30 bright stars from a static stars.json {name, RA hours, Dec degrees, apparent magnitude}, derived from a public Hipparcos extract. Star size scales inversely with magnitude. Latitude slider tilts the sphere relative to the horizon plane; time-of-year slider rotates about the polar axis.
>
> **Constrain.** D3 v7 only plus stars.json. Mark Polaris, Sirius, and Vega explicitly. Display latitude and date numerically. Filename: `02-celestial-sphere.html`.
>
> **Verify.** (a) At latitude +90° N, the celestial equator should sit along the horizon and Polaris at the zenith. (b) At latitude 0°, both celestial poles should sit on the horizon and the celestial equator should pass through the zenith. (c) At latitude +42°, Polaris should sit 42° above the northern horizon. Confirm numerically.

### Exploration

- From latitude +50° N, what fraction of the celestial sphere is *circumpolar* (never sets)? What fraction is permanently invisible? Do those add to anything you can predict from geometry alone?
- Animate 24 sidereal hours. From what latitude do star trails become straight lines instead of circles?
- Place the Sun on the ecliptic at the time-of-year slider position. Watch the June solstice from latitude +66.5° N. Then from +90° N.

### Bridge to Chapter 3

> **Show.** I have the geometry of the sky. Now I need to know *what light is* — every astronomical observation in this book is an interpretation of electromagnetic radiation arriving from far away.
>
> **Say.** Modify the simulator so stars are colored by spectral class (O blue, B blue-white, A white, F yellow-white, G yellow, K orange, M red). Click a star to show apparent magnitude and distance in parsecs.
>
> **Verify.** Sirius (A1) appears white-blue. Betelgeuse (M1) appears red. The Sun, at its current ecliptic position, appears yellow (G2).

Save as `02b-stellar-colors-preview.html`. Lead-in to Chapter 3 — *Radiation and Spectra*.

---

## What would change my mind

The central claims of this chapter have survived every test attempted for three centuries. A reproducible measurement of a Kepler's-third-law deviation inside the solar system, once general-relativistic corrections are removed, would force a serious rewriting. The most famous deviation — Mercury's anomalous perihelion precession of 43 arcseconds per century — turned out to be a *correction* to Newtonian gravity (general relativity), not a refutation of Kepler. A deviation today, after that correction is applied, would be evidence of physics beyond general relativity.

## Still puzzling

- *Why exactly 23.44°?* The obliquity is set by collisional history during planet formation — most likely the giant impact that formed the Moon ~4.5 billion years ago. It oscillates between ~22.1° and ~24.5° on a 41,000-year period. There is no first-principles reason this epoch sits where it does. The question is historical, not physical.
- *Why does the celestial sphere work at all?* Because the sky is effectively at infinity — every astronomical object is so far away that its direction from any point on Earth is the same. That no near-field objects exist in the solar neighborhood is a fact about star-formation geometry we did not put in by hand.
- *What broke Ptolemy was data, not philosophy.* One good observation (phases of Venus) decided between two systems that decades of philosophical argument could not. We do not know how many current astronomical disputes are awaiting their telescope.

---

**Tags:** celestial sphere, right ascension, declination, ecliptic, Eratosthenes, Kepler's laws, heliocentrism, Galileo, observational astronomy, history of science
