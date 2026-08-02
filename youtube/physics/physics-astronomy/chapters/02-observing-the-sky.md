# Chapter 2 — Observing the Sky

*A stick, a shadow, a well in Egypt, and a 47,500-kilometer planet — plus everything we had to invent before we could explain anything at all.*

---

There is a question so obvious it almost embarrasses you to ask it: how do you figure out the size of the Earth if you can't leave it?

You can't pace off the circumference. You can't fly overhead and look down. You have a stick, you have the Sun, and you have the willingness to wait for the right day. Around 240 BCE, a man named Eratosthenes — librarian at Alexandria, the largest collection of knowledge in the ancient world — did exactly this. He measured the circumference of the planet to within about 15 percent of the modern satellite value. With a stick.

Here is the trick, and it is beautiful: he had read a traveler's report from Syene, a city roughly 800 kilometers south on the Nile. The report noted that at noon on the summer solstice, the Sun stood directly overhead. A vertical pole cast no shadow. A deep well lit up all the way to the bottom — a column of light, straight down.

Eratosthenes waited for the same solstice in Alexandria. He planted a stick. He measured the shadow. It fell at about 7.2° from vertical.

Now here is the physical assumption that makes everything work: the Sun is so far away that its rays, for purposes of this measurement, arrive parallel. They do not fan out in any way you can measure. This is correct — the Sun is about 24,000 Earth-radii away, so the rays are parallel to better than one part in ten thousand. Under that assumption, if two vertical sticks at the same moment cast different shadow angles, there is only one explanation: the ground between them is curved. The Earth is round, and the shadow angle measures how round.

A vertical stick in Syene points directly at the Sun. A vertical stick in Alexandria points slightly away. The angle between those two "vertical" directions — 7.2° — is exactly the angle subtended at Earth's center by the arc of surface between the two cities. And 7.2° is 7.2/360 of a full circle — one fiftieth.

![Cross-section of Earth at summer solstice. At Syene the Sun is overhead; in Alexandria it casts a shadow at 7.2° from vertical. With parallel rays from the Sun, that angle equals the central angle subtended at Earth's...](../images/02-observing-the-sky-fig-01.png)
*Figure 2.1 — Eratosthenes' Measurement of Earth's Circumference*

So:

$$C = 50 \times 925 \text{ km} = 46{,}250 \text{ km}$$

Modern satellite value: 40,075 km. About 15% high. With a stick, a shadow, and a story about a well.

<!-- → [INFOGRAPHIC: Two vertical sticks at Alexandria and Syene with parallel sun rays, showing the 7.2° shadow angle and the equivalent 7.2° arc at Earth's center — annotate the logical chain: parallel rays → shadow difference → Earth curvature → circumference] -->

I want to pause on the honest accounting of that 15% error, because it matters. Eratosthenes didn't report in kilometers — he worked in stadia, and several different "stadium" lengths were in use in the Greek world. Historians still argue about which one he used. Pick the right conversion and his answer is within a percent of correct. Pick a different reasonable one and it's 20% high. The apparent precision of his result is partly a function of which conversion we choose today. What is not ambiguous is the *method*. The method is perfect. The errors are in the inputs — the distance between cities, the shadow angle, the fact that Alexandria and Syene aren't quite on the same north-south line — and every one of those errors is nameable and shrinkable with better measurement. That's what good science looks like: a method that shows you clearly where to improve.

---

## What the sky actually looks like

Now I want to describe something you've seen your whole life but probably haven't sat down and thought about carefully.

Step outside on a clear night, away from city lights, and let your eyes adjust. What you see is this: a vast dark bowl overhead, scattered with points of light. They keep their positions relative to each other with exquisite fidelity — the pattern you see tonight is the same pattern ancient Egyptian astronomers saw. But the whole arrangement moves. Over the course of a night, stars rise in the east, arc across the sky, and set in the west, as if the bowl is slowly rotating.

Except it isn't the bowl rotating. It's you. Earth turns on its axis once every 23 hours 56 minutes 4 seconds — the **sidereal day**, the rotation period measured against the stars. (The ordinary 24-hour day is slightly longer because Earth has also moved along its orbit, and the Sun takes a bit of extra time to "catch up." We'll come back to that distinction.) Every star traces a circle around a fixed point in the sky — the **celestial pole**, where Earth's rotation axis, extended outward, intersects the imaginary sphere of the sky.

<!-- → [DIAGRAM: Earth's rotation axis extended to celestial north and south poles, with latitude lines projected out to form the celestial equator — show a star at mid-declination tracing a circle around the pole over 24 hours] -->

That imaginary sphere has a name: the **celestial sphere**. It is a fiction, but a tremendously useful one. Stars are not actually arranged on a sphere — Sirius is 8.6 light-years away while Betelgeuse is roughly 550 light-years, and Andromeda is 2.5 million. But your eye sees only *directions*, not distances. Project everything onto a unit sphere centered on you and you have a complete two-dimensional map of every direction in the sky. The celestial sphere makes no claim about what is moving or how far anything is. It just records directions. That is its strength.

Coordinates on the celestial sphere are direct analogs of latitude and longitude on Earth's surface:

- **Declination (Dec)** is celestial latitude. The celestial equator — the projection of Earth's equator onto the sky — sits at Dec = 0°. The north celestial pole is Dec = +90°. Polaris, the current North Star, sits at about Dec = +89.3°, close enough to the pole that it barely moves all night.
- **Right ascension (RA)** is celestial longitude, measured eastward from a fixed zero point — the vernal equinox — in hours, minutes, and seconds. The full circle is 24 hours, so 1 hour of RA equals 15°.

![Earth at center, with the celestial sphere drawn around it. Marked: the two celestial poles, the celestial equator, the ecliptic (tilted 23.44°), the vernal equinox, and a sample star located by right ascension and de...](../images/02-observing-the-sky-fig-02.png)
*Figure 2.2 — Celestial Sphere with RA/Dec Coordinates*

<!-- → [TABLE: Celestial sphere coordinate analogies — two columns: Earth surface / Celestial sphere — rows: latitude/declination, longitude/right ascension, equator/celestial equator, north pole/north celestial pole, prime meridian/vernal equinox — helps student map familiar geography onto unfamiliar coordinate system] -->

A pair (RA, Dec) is the address of every star, galaxy, and pulsar in every catalog you will ever read in this course. Hipparchus introduced a version of this scheme around 130 BCE. The geometry has not changed since. It survived the complete replacement of the theory underneath it — and that is the story I want to tell.

---

## Two different motions

Here is something easy to miss: the sky does two distinct things, and they have two completely different causes.

The first is the nightly rotation — every star rises and sets as the Earth turns. The second is something slower: the *same star* at the *same time of night* is not in the same position on different nights of the year. The constellations shift. Orion, dominant in winter evenings, is gone by summer. The Big Dipper's handle points different directions at midnight depending on the season. If you watch patiently, the sky appears to creep eastward by about one degree per night — a full circle in one year.

The cause: Earth is orbiting the Sun, and as it moves, our line of sight to the stars shifts. Against the backdrop of the fixed stars, the Sun appears to trace a complete circuit through the sky over one year. That path is called the **ecliptic** — the Sun's apparent annual road through the constellations. The twelve constellations it passes through are the zodiac.

<!-- → [DIAGRAM: Earth at four orbital positions (equinoxes, solstices), with a line from Earth through the Sun projected to the distant star background — showing how the Sun's apparent position against the stars changes through the year, tracing the ecliptic] -->

The ecliptic is tilted relative to the celestial equator by 23.44°. This tilt is not a detail — it is the entire explanation of seasons.

I know what most people think about seasons. They think Earth gets closer to the Sun in summer and farther in winter. It is natural. It is wrong.

Earth's orbit is very nearly circular. The eccentricity is 0.0167, meaning closest approach (perihelion) and farthest point (aphelion) differ by only 3.3%. And here is the clincher: perihelion falls around January 3. If seasons came from distance, northern-hemisphere winter would be *warmer* than summer, not colder. Distance is the wrong variable.

The right variable is the 23.44° tilt of Earth's rotation axis. When the northern hemisphere is tilted toward the Sun — around June 21 — two things happen simultaneously. First, sunlight hits at a steeper angle: the same beam covers less ground, concentrating its energy. Second, the day is longer, so the ground accumulates heat for more hours. Both effects point the same direction: it's warmer. Six months later, tilted away: shallower sunlight, shorter days, winter.

Here is the clean test. The southern hemisphere has summer while the northern hemisphere has winter. Both hemispheres are the same distance from the Sun at any given moment — distance is identical for both. But one is tilted toward the Sun and one is tilted away. Tilt produces opposite-hemisphere behavior. Distance cannot.

![June and December solstices. The same axial tilt produces opposite seasons in opposite hemispheres at the same Earth-Sun distance. Distance cannot explain what depends on hemisphere; tilt can.](../images/02-observing-the-sky-fig-03.png)
*Figure 2.3 — Seasons from Tilt: The Definitive Argument*

<!-- → [INFOGRAPHIC: Earth at June and December solstice positions — for each, show the 23.44° axial tilt, the steeper/shallower sunlight angles in each hemisphere, and the longer/shorter daylight arc; sidebar: perihelion date (Jan 3) labeled to underscore that closest approach coincides with northern winter, not summer] -->

---

## What everyone got wrong for thirteen centuries, and why they weren't stupid

Ancient astronomers had a problem. The planets — Mercury, Venus, Mars, Jupiter, Saturn — don't move the way stars do. Against the fixed star background, they usually drift eastward night by night. But occasionally they slow down, stop, reverse direction for weeks or months (moving westward), then stop again and resume eastward motion. The reversal is called **retrograde motion**. To the naked eye, with no telescope, no theory of gravity, no knowledge of distances — just careful positions recorded over decades — this is genuinely puzzling.

Around 150 CE, Claudius Ptolemy assembled the authoritative synthesis in a work we call the *Almagest*. His model: Earth at the center, everything orbiting it. To reproduce retrograde motion, he needed each planet to move on a small circle — an **epicycle** — whose center rode a larger circle called a **deferent**. The epicycle's revolution carried the planet in a little loop, producing the temporary reversal. He also needed a correction called the **equant** — an offset point around which angular speed was constant — to match the observed irregularities.

<!-- → [DIAGRAM: Ptolemaic epicycle and deferent for one planet — show the planet tracing the loop of retrograde motion as seen from Earth at center, with the epicycle center moving along the deferent] -->

It worked. For thirteen centuries — through the Islamic Golden Age, through the European Middle Ages, into the early modern period — Ptolemy's model was what educated people used to calculate where planets would be. It was accurate enough for calendar-making and navigation. A model can be structurally wrong and quantitatively useful at the same time. That is not a contradiction. It is just the nature of fitting curves to data.

In 1543, Copernicus moved the Sun to the center. The immediate payoff: retrograde motion falls out automatically. When Earth, on an inner orbit, overtakes Mars on an outer orbit, Mars appears to slide backward against the stars — the same illusion you get when a slower car appears to move backward as you pass it on the highway. No epicycles needed for that. Copernicus's model was not dramatically more accurate in its numerical predictions — he kept circular orbits, which are wrong, and still needed minor epicycles to match observations. But it was *more honest*: it eliminated the largest class of artificial patches by changing one assumption about what sits at the center.

![Top-down view of the Sun, Earth's inner orbit, and Mars's outer orbit. As Earth overtakes Mars, sightlines from Earth project Mars onto the background stars and trace a backward loop. The retrograde motion is geometri...](../images/02-observing-the-sky-fig-05.png)
*Figure 2.5 — Retrograde Motion: Why Mars Loops Backward*

The objection to Copernicus was not stupidity. It was parallax.

If Earth orbits the Sun, then over the course of a year, nearby stars should appear to shift against more distant background stars — the same way a nearby fence post slides against a distant hillside when you move your head. **Stellar parallax** is a real and measurable effect. The question is: how big is it?

No ancient or Renaissance astronomer could detect it. The conclusion was: either heliocentrism is wrong, or the stars are unimaginably far away. The second option seemed excessive. (It is correct. The nearest star system, Alpha Centauri, is about 4.24 light-years away. Its parallax is 0.747 arcseconds — about 1/5000 of the angular diameter of the full Moon. The first successful parallax measurement was made in 1838, by Friedrich Bessel, using instruments a hundred times more precise than anything Copernicus had. Aristarchus, who proposed heliocentrism in roughly 270 BCE, faced the same objection — and had no way to answer it except to say the stars must be very far away. He was right, but he was making an extraordinary claim with no direct evidence.)

<!-- → [DIAGRAM: Stellar parallax geometry — Earth at two positions six months apart on its orbit, lines of sight to a nearby star against a distant background, parallax angle p labeled at the star; inset showing how p = 0.747″ for Alpha Centauri is far below naked-eye resolution of ~60″] -->

---

## Kepler's 8 arcminutes

Tycho Brahe spent twenty years building the most precise pre-telescope observatory in history, on the island of Hven off the Danish coast, measuring planetary positions accurate to about 1 arcminute. He was not a Copernican — he proposed a hybrid model where the planets orbit the Sun and the Sun orbits the Earth — but he was a meticulous measurer. When he died in 1601, his data passed to a young German assistant named Johannes Kepler.

Kepler believed in the Copernican system and set out to refine it using Brahe's observations. He focused on Mars, the most problematic planet for any circular-orbit model. He tried every circle he could construct. None fit. The model positions disagreed with Brahe's observations by a residual of about 8 arcminutes — about one-seventh of the Moon's apparent diameter. That sounds tiny. But it was within Brahe's measuring precision, which meant the error was real, not instrumental noise.

Kepler could have accepted 8 arcminutes and moved on. He didn't. "Since God's goodness provided us with an observer as careful as Tycho," he wrote, "it is appropriate that we accept God's gift with a thankful mind." He tried every curve he knew. Eventually he tried an ellipse.

The ellipse fit perfectly.

<!-- → [DIAGRAM: Elliptical orbit with Sun at one focus — label semi-major axis a, show the swept areas for Kepler's second law being equal in equal time intervals] -->

![Three panels. Law 1: ellipses with the Sun at one focus. Law 2: equal areas swept in equal times. Law 3: T² ∝ a³ — the period-distance relation that holds across the solar system.](../images/02-observing-the-sky-fig-06.png)
*Figure 2.6 — Kepler's Three Laws: One-Panel Reference*

From this, Kepler published three laws — empirical regularities extracted from data, not derived from any theory of what causes them:

**First law.** Every planet moves on an ellipse with the Sun at one focus.

**Second law.** The line from the Sun to the planet sweeps out equal areas in equal times. (The planet speeds up near the Sun and slows down when far away.)

**Third law.** The square of the orbital period equals the cube of the average distance from the Sun:

$$T^2 = a^3$$

where $T$ is in years and $a$ is in astronomical units (AU, the Earth-Sun distance).

Check it:

<!-- → [TABLE: Kepler's third law verification — columns: Planet, a (AU), a³, T (years), T² — rows for Earth, Mars, Jupiter showing a³ ≈ T² to three significant figures] -->

| Planet  | $a$ (AU) | $a^3$  | $T$ (yr) | $T^2$  |
|---------|----------|--------|----------|--------|
| Earth   | 1.000    | 1.000  | 1.000    | 1.000  |
| Mars    | 1.524    | 3.540  | 1.881    | 3.538  |
| Jupiter | 5.203    | 140.85 | 11.862   | 140.71 |

$a^3$ and $T^2$ agree to three significant figures. No fitting parameter. An asteroid at $a$ = 2.7 AU will have $T^2$ = 19.68, giving $T$ ≈ 4.43 years — match any catalog.

Kepler didn't know *why*. He had found the pattern. It would take Newton to explain it.

---

## The observation that decided everything

In 1609 and 1610, Galileo built a refractor of about 20× magnification and pointed it at things no one had looked at carefully before. On January 7, 1610, he noted three small "stars" in a line near Jupiter, two to the east and one to the west. On January 10 they had moved. By month's end he had tracked four of them — objects clearly orbiting Jupiter.

The geocentric objection to heliocentrism included this: if Earth moved, the Moon would be left behind. Galileo had now found a planet in motion carrying *four* moons with it. The objection was empirically dead.

But the observation that killed geocentrism cleanly — the one that left no philosophical escape — was Venus.

In Ptolemy's model, Venus orbits between Earth and the Sun, its epicycle carrying it back and forth across our line of sight to the Sun. This geometry has a hard prediction: from Earth, Venus should always appear as a crescent or thin arc. It should never show more than a half-phase, because its lit side can never face fully toward us — the Sun is always behind Earth relative to Venus.

![In Ptolemy's geocentric system, Venus always sits between Earth and Sun and could only show crescent phases. In the heliocentric system, Venus shows a full cycle from new through full. Galileo, 1610: full cycle observed.](../images/02-observing-the-sky-fig-07.png)
*Figure 2.7 — Phases of Venus: The Empirical Kill of Ptolemy*

In the heliocentric model, Venus orbits the Sun closer than Earth does. When Venus is on the far side of the Sun from Earth, it appears fully lit but tiny. When it swings around to our side, it appears large but crescent. We should see the full range of phases, with apparent size inversely correlated with phase fullness.

![Looking down on the Moon's orbit. The Sun is offscreen to the right; the Moon's lit half always faces the Sun. What changes with phase is how much of the lit half faces Earth.](../images/02-observing-the-sky-fig-04.png)
*Figure 2.4 — Moon Phases as Pure Geometry*

Galileo watched Venus through the winter of 1610–1611. He saw a full phase cycle — crescent, half, gibbous, full — with angular size behaving exactly as heliocentrism required. He saw a full Venus. In Ptolemy's model, a full Venus is geometrically impossible.

<!-- → [DIAGRAM: Side-by-side comparison — left: Ptolemaic Venus orbit between Earth and Sun, showing that Venus can only ever appear as crescent from Earth's perspective; right: heliocentric Venus orbit interior to Earth's, showing the full phase cycle with apparent size correlated to distance — student should see the two models make incompatible predictions] -->

This is not a philosophical argument or a matter of elegance or parsimony. It is a specific, unambiguous prediction of Ptolemy's model that was false. The geocentric model was not just less convenient — it was *wrong*. Galileo had the observation.

---

## Newton ties it together

The coordinate system survived Ptolemy's mechanics. It survived Copernicus's circles. It survived Kepler's ellipses. Then in 1687, Isaac Newton published the *Principia Mathematica* and derived Kepler's three empirical laws from one assumption:

$$F = \frac{GMm}{r^2}$$

The force between two masses falls off as the square of the distance between them. Everything in orbit obeys this. The Moon stays in orbit by the same rule that pulls an apple downward. Kepler's cube-square law ($T^2 = a^3$) is not a coincidence — it falls out of the inverse-square law as an algebraic consequence. The equal-area rule (second law) is conservation of angular momentum. Every planet moves on an ellipse because the inverse-square force produces conic sections.

Newton unified terrestrial mechanics with celestial mechanics. The same physics, everywhere, in one formula.

The coordinate system still hasn't changed.

---

## What you should be able to do now

You should be able to reproduce Eratosthenes' measurement from first principles — given a shadow angle and a north-south distance, recover Earth's circumference. The only input you need is the assumption of parallel solar rays.

You should be able to apply Kepler's third law: $T^2 = a^3$. Give me an average orbital distance in AU and I should be able to hand you a period in years, or vice versa.

You should be able to explain why seasons come from axial tilt and not from orbital distance — and give me the clean test that distinguishes the two hypotheses.

You should be able to explain why the absence of observed stellar parallax was a *legitimate scientific objection* to heliocentrism, not simple closed-mindedness — and why it wasn't resolved for 2,100 years after Aristarchus.

And you should understand that (RA, Dec) — the coordinate system on the celestial sphere — makes no theoretical assumptions. It survived four complete replacements of the underlying physical theory because it records only *directions*, not causes. The next twelve chapters will use it without ceremony. Now you know why it works.

---

---

## Exercises

**Warm-up** *(Tests: Eratosthenes' method; celestial sphere geometry)*

1. At noon on the summer solstice, a 1-meter vertical stick in a city at latitude 30° N casts a shadow. Without doing any calculation, explain *why* it casts a shadow at all — what does Eratosthenes' logic say must be true about the geometry?

2. State in one sentence what each coordinate measures: (a) right ascension; (b) declination. Then give the RA and Dec of the north celestial pole.

3. The sidereal day is 23h 56m 4s. The solar day is 24h 0m 0s. Why are they different? Which one does your clock track, and why?

**Application** *(Tests: Eratosthenes calculation; Kepler's third law; season reasoning)*

4. A vertical stick in City A casts no shadow at noon on the summer solstice. A vertical stick in City B, 1,200 km due north, casts a shadow at 9.6° from vertical at the same instant. Calculate Earth's circumference from these numbers. Then identify which assumption in Eratosthenes' method is doing the most work — and what would happen to your answer if that assumption were slightly wrong.

5. Use Kepler's third law ($T^2 = a^3$) to find the orbital period of: (a) an asteroid with semi-major axis 3.2 AU; (b) a hypothetical planet at 0.4 AU. Check whether your answers are consistent with the pattern in the Earth-Mars-Jupiter table.

6. A friend argues: "It's summer in Australia in December because that's when Earth is closest to the Sun." Construct a two-part response: first, explain what the actual perihelion date implies for this claim; second, give the clean test from axial tilt that cannot be explained by distance alone.

**Synthesis** *(Tests: connecting coordinate system, historical models, and observational evidence)*

7. Retrograde motion was explained by Ptolemy using epicycles and by Copernicus using relative orbital speeds. Both explanations fit the observations. What kind of evidence *could not* distinguish between the two models on the basis of retrograde motion alone — and what specific observation *did* decide between them? Name the observation and explain why it was decisive rather than merely preferential.

8. Kepler's third law was derived empirically from Brahe's data. Newton later derived the same law from $F = GMm/r^2$. What does the fact that an empirical regularity *falls out* of a physical law tell you about the relationship between Kepler's and Newton's work? Could Kepler's law have been wrong while Newton's was right, or vice versa?

**Challenge** *(Tests: parallax as scientific argument; limits of the coordinate system)*

9. Aristarchus proposed heliocentrism around 270 BCE. The first stellar parallax was measured in 1838 — 2,100 years later. (a) Express the parallax angle of Alpha Centauri (4.24 light-years) in arcseconds. (b) The naked eye resolves angles down to roughly 1 arcminute (60 arcseconds) under ideal conditions. By how many orders of magnitude does Alpha Centauri's parallax fall below naked-eye resolution? (c) Given your answer, was the failure to detect parallax a *reasonable scientific objection* to heliocentrism, or an *irrational resistance* to a correct idea? Defend your answer.

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
