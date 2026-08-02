# Chapter 17 — Analyzing Starlight

*How a prism turned a point of light into a complete biography.*

---

Sirius looks simple. It is the brightest star in the night sky, burning white in Canis Major, and at first glance the interesting facts about it seem exhausted by that brightness. A point. A white point.

But that white point has traveled 8.6 light-years to reach your eye, and it carries, encoded in the pattern of its wavelengths, a message. The message says: I am 10,000 Kelvin at my surface. I am mostly hydrogen, with traces of calcium and iron. I am moving toward you at 5.5 kilometers per second. I rotate with a period of about 12.5 hours, fast enough that my equator bulges. I am a main-sequence star, not a giant — you can read that in the width of my spectral lines.

A spectrograph — a prism that spreads light into its component wavelengths — reveals the message. What you see is a continuous band of color, crossed by thin dark lines. Those lines are not in the starlight itself. They are absences. Atoms in the star's outer atmosphere have plucked specific wavelengths out of the beam. Every element leaves its mark at precise positions. Read the pattern, and you can reconstruct what the star is made of, how hot it burns, whether it is moving toward you or away, how fast it spins, whether it is a dwarf or a giant.

I want to explain how that reading works — not just the names and categories, but why it works. Why temperature determines which lines appear. Why line width tells you about pressure. Why a slight shift in wavelength measures velocity. The machinery is not complicated, but it is not obvious, and I think it is one of the most elegant chains of reasoning in all of observational science.

---

## Brightness and Distance

Start with a problem that took centuries to resolve: stars look brighter or dimmer, but observed brightness conflates two completely different things — how much energy the star actually produces, and how far away it is.

Astronomers distinguish these with two words. **Luminosity** is the total power output of the star — watts, radiated equally in all directions. **Apparent brightness** is the fraction of that power that arrives at Earth.

The geometry is straightforward. A star radiates equally in all directions. Draw a sphere of radius $r$ around it. The star's luminosity is distributed over the surface of that sphere, which has area $4\pi r^2$. Double the distance, and the sphere has four times the area. The same luminosity is spread over four times as much surface. Any detector — your eye, a telescope mirror — catches one quarter as much light. This is the inverse square law:

$$b = \frac{L}{4\pi r^2}$$

The consequence is frustrating. Measure the apparent brightness of a star, and you know the left side of this equation. But there are two unknowns on the right — luminosity and distance. Without independent information about one of them, you cannot solve for the other. A bright star might be intrinsically luminous or simply close. A faint star might be intrinsically dim or simply far. This haunted astronomy for centuries.

The system used to quantify apparent brightness is a historical artifact worth knowing. In about 150 BCE, Hipparchus sorted the visible stars into six classes by eye — the brightest called first-magnitude, the faintest visible to the naked eye called sixth-magnitude. When 19th-century astronomers finally had precise photometers, they measured the actual brightness ratio between first and sixth magnitude and found it was roughly 100 to 1. By convention that ratio was locked in: five magnitudes equals a factor of exactly 100 in brightness. One magnitude step therefore corresponds to the fifth root of 100, which is about 2.51.

Two properties of this system catch people constantly. First, it runs backward: larger numbers mean fainter objects. Sirius is magnitude $-1.5$. Venus at its brightest is $-4.4$. The Sun is $-26.8$. The faintest galaxies detected by modern telescopes are around magnitude 30. Second, magnitudes are logarithmic — they do not add. A difference of 5 magnitudes corresponds to a brightness ratio of exactly 100. The system persists because it was established early and standardized: every astronomer in every country knows exactly what "magnitude 6" means.

---

## Why Color Is a Thermometer

Every object radiates electromagnetic energy. The hotter the object, the more it radiates, and the shorter the wavelengths at which it radiates most intensely. Wien's displacement law quantifies this:

$$\lambda_{\text{peak}} = \frac{b}{T}$$

where $b \approx 2.9 \times 10^{-3}$ m·K and $T$ is the surface temperature in Kelvin. A star at 30,000 K peaks in the ultraviolet — its visible emission is blue. A star at 3,000 K peaks in the infrared — its visible emission is red. At 5,800 K, the peak sits in the green, which is why sunlight looks yellowish-white.

This is why the colors of stars in the night sky form a sequence. The colors are thermometers.

In practice, astronomers measure temperature through **color indices**. Observe the star through a blue filter and record its apparent magnitude, $B$. Observe through a visual (yellow-green) filter and record $V$. The color index is $B - V$.

This number is independent of distance. A red star looks red whether it is ten light-years away or ten thousand, because the ratio of its blue-to-yellow output depends on temperature, not location. By convention, the color index of the star Vega (about 10,000 K) is defined to be zero. Hotter stars emit proportionally more blue light, so they have negative $B - V$. Cooler stars have positive $B - V$. The Sun has $B - V \approx +0.65$.

From a single number obtained by pointing a telescope through two filters, you have the surface temperature of a star that may be hundreds of light-years away.

---

## The Deep Puzzle: Why the Lines Reveal Temperature, Not Composition

Here is the thing that confused the first stellar spectroscopists, and the correction that followed is one of the most important in the history of astrophysics.

When you spread starlight through a prism, you see a rainbow crossed by thin dark lines. Different stars have strikingly different patterns of lines. The first people to study these patterns thought the differences meant differences in composition — that some stars were rich in hydrogen, others in calcium, others in iron. This was wrong.

Almost all stars have the same composition: roughly 73% hydrogen by mass, 25% helium, and about 2% everything else combined. The differences in spectral lines are not about what elements are present. They are about temperature.

Understanding why requires a detour into atomic physics.

An atom absorbs light when one of its electrons jumps from a lower energy level to a higher one, absorbing a photon with exactly the right energy. The specific photon energies an atom can absorb depend on the gaps between its allowed energy levels — and those gaps are fixed by the structure of the atom. Hydrogen absorbs at specific wavelengths, calcium at different wavelengths, sodium at others. This is the fingerprinting mechanism.

But the atom can only absorb if it has electrons in the right place to begin with.

Consider hydrogen in a very hot star — say, 40,000 K. At this temperature, the thermal energy is high enough to strip electrons away from hydrogen nuclei entirely. Ionized hydrogen has no electrons. No electrons means no absorption transitions. Hydrogen is abundant but completely invisible in the spectrum.

Now consider hydrogen in a very cool star — say, 3,000 K. Here, hydrogen atoms are neutral and their electrons sit mostly in the ground state ($n = 1$). To absorb visible light, an electron needs to be in the second energy level ($n = 2$), from which it can jump to higher levels and absorb photons in the visible Balmer series. But in a cool star, almost no electrons are thermally excited to $n = 2$. They are all in the lowest state. Almost no visible hydrogen absorption.

The sweet spot is around 10,000 K. At this temperature, roughly 1 in 100 million hydrogen atoms has its electron in the $n = 2$ level — enough to produce very strong absorption lines without the bulk of the hydrogen being ionized. This is why the strongest hydrogen lines appear in white A-type stars: not because those stars have the most hydrogen, but because their temperature puts hydrogen's electrons exactly where they need to be.

The same logic applies to every element and every ionization state. Calcium ionized once ($\text{Ca}^+$) produces its strongest visible lines around 6,000 K — which is why those lines dominate in G and K stars, even though there is far less calcium than hydrogen. Titanium oxide molecules form only below about 3,500 K — which is why molecular bands appear only in the coolest M stars.

A common misconception is worth addressing directly: the absence of hydrogen lines does not mean the absence of hydrogen. It means the temperature is wrong for hydrogen to absorb visible light. O stars, which are more than 70% hydrogen by mass, show essentially no hydrogen lines in visible wavelengths. Every star in the sequence is mostly hydrogen. The lines tell you about temperature first.

In the 1890s, Annie Jump Cannon at Harvard organized this understanding into the classification system still in use. She kept seven letters from an earlier alphabetical attempt — O, B, A, F, G, K, M — ordered by decreasing temperature, subdivided into decimal subtypes 0 through 9. She classified roughly 500,000 stars by eye, looking at photographic plates through a microscope, at a rate of up to three stars per minute. The Sun is G2.

The sequence, with its temperatures and characteristic features:

**O** (above 30,000 K): ionized helium, weak hydrogen. Blue.

**B** (10,000–30,000 K): neutral helium, strong hydrogen. Blue-white.

**A** (7,500–10,000 K): strongest hydrogen lines, weak ionized metals. White. (Sirius, Vega.)

**F** (6,000–7,500 K): strong hydrogen, strong ionized calcium. Yellow-white.

**G** (5,200–6,000 K): weak hydrogen, strong ionized calcium, sodium. Yellow. (The Sun.)

**K** (3,700–5,200 K): weak hydrogen, strong neutral metals. Orange. (Arcturus.)

**M** (2,400–3,700 K): titanium oxide molecules, neutral metals. Red. (Betelgeuse.)

This is a thermometer, not a taxonomy. What changes along it is not the composition but the atomic physics of which electrons are in which states at each temperature.

---

## What the Lines' Shapes and Positions Reveal

Temperature is the dominant story in a stellar spectrum, but not the only one. Once you know the temperature from the pattern of which lines appear, you can ask more subtle questions by looking at the shapes and positions of the lines themselves.

**Pressure tells you whether the star is a dwarf or a giant**

In a dense gas, atoms collide frequently. Each collision slightly perturbs the energy of the transition, smearing the line over a range of wavelengths. More collisions mean broader lines. Fewer collisions mean sharper, narrower lines.

A giant star has an extended, low-density atmosphere spread over a large volume. Few collisions. Narrow lines. A dwarf star is compact and dense. More collisions. Broad lines. Two stars with identical surface temperatures will have the same line positions but different line widths. Reading the widths distinguishes a giant from a dwarf without knowing the distance.

**Doppler shifts measure velocity**

A source of waves moving toward you emits waves that arrive more compressed — shorter wavelength, higher frequency. Moving away, the waves are stretched. The magnitude of this shift depends on the velocity:

$$\frac{\Delta \lambda}{\lambda} = \frac{v}{c}$$

where $\Delta\lambda$ is the shift in wavelength, $\lambda$ is the rest wavelength, $v$ is the radial velocity, and $c$ is the speed of light.

In 1868, William Huggins observed the spectrum of Sirius and saw its hydrogen lines slightly shifted — the first measurement of a stellar radial velocity. A shift of 0.1 nm in a line normally at 656 nm corresponds to a velocity of about 46 km/s. The technique is now precise enough that astronomers routinely detect the wobble of a star caused by an orbiting planet — velocity amplitudes of a few meters per second, measured over months from light that has traveled light-years.

**Rotational broadening measures spin**

Imagine a star rotating. The edge rotating toward you is Doppler-shifted to shorter wavelengths. The edge rotating away is shifted to longer wavelengths. The center of the disk contributes at the rest wavelength. The observed spectral line is the sum of all contributions from different parts of the surface — a smeared, broadened line with a characteristic rounded profile.

Vega rotates once every 12.5 hours — fast enough that it is roughly 23% wider at the equator than at the poles. Its spectral lines are measurably broadened. The Sun rotates once per month; its lines are narrow by comparison. Young stars tend to rotate fast; magnetic braking bleeds angular momentum as they age, and they slow.

**Line strength measures abundance**

Given two stars with the same temperature and pressure, if a particular spectral line is stronger in one than the other, that star contains more of the corresponding element. This is how we know that some stars are metal-rich — two or three times the solar abundance of heavy elements — while others, old stars formed early in the galaxy's history, have heavy-element abundances a hundred times below solar. The word "metals" in this context means all elements heavier than helium; the usage is a legacy of early spectroscopy.

---

## The Chemical Biography of the Galaxy

These measurements, accumulated across hundreds of thousands of stars, tell a story.

Almost all stars are almost entirely hydrogen and helium. These two elements were created in the Big Bang, three minutes after the universe began. Everything else — carbon, oxygen, silicon, iron, calcium, the elements that make planets and people — was made later, in stellar cores, through nuclear fusion. A massive star spends its life fusing hydrogen into helium, helium into carbon, carbon into oxygen and neon and magnesium, up toward iron. When the star exhausts its fuel and collapses, the outer layers are expelled in a supernova, scattering those elements into the surrounding gas. The next generation of stars forms from this enriched material.

The consequence is that the heavy-element abundance of a star tells you roughly when it was born. Old stars, formed when the galaxy was young and few previous stellar generations had yet enriched the gas, have very low metal abundances. Young stars, formed from gas enriched by billions of years of stellar processing, have metal abundances at or above solar.

The Sun, at about 0.2% metals by mass, sits in the middle of this distribution. The fact that Earth exists — with its iron core, its silicate mantle, its carbon-based life — exists because earlier generations of massive stars lived and died, enriching the molecular cloud from which the solar system condensed.

When you measure the spectrum of a faint, metal-poor star in the outer halo of the galaxy, you are reading the chemistry of the early universe, preserved in an ancient object. When you measure the spectrum of a young star in a star-forming region, thick with metals, you are reading the output of billions of years of nucleosynthesis.

And all of it comes from looking at the pattern of dark lines crossing a rainbow of color. Temperature determines which lines dominate. Line widths tell you the pressure and the stellar size. Doppler shifts measure motion. Broadening measures rotation. Line strengths measure abundance. Point a spectrograph at a point of light, and in the pattern of dark lines you can read temperature, size, motion, rotation, and composition — a complete physical description of an object you will never visit, using light that left it years or centuries ago.

That is what it means to decode starlight. Not to gaze at it, but to read it.

---

## LLM Exercises

**Exercise 1.** Stellar spectra are classified into types O, B, A, F, G, K, M (with subdivisions 0-9), in order of decreasing surface temperature. Prompt an LLM: "What does this spectral type tell us about a star? Walk through the relationship between temperature, color, and dominant absorption lines: hot O stars (~30,000 K) show ionized helium lines; cool M stars (~3,000 K) show molecular bands. Why do specific elements dominate the spectrum at specific temperatures?" Evaluate whether the response correctly identifies that the dominant lines reflect what energy levels are populated at that temperature — too hot, atoms are ionized and don't show neutral lines; too cool, atoms don't have enough thermal energy to populate excited states.

**Exercise 2.** The Doppler effect shifts spectral lines according to a star's radial velocity. Prompt an LLM: "Calculate: a star's hydrogen alpha line (lab wavelength 656.28 nm) is observed at 656.43 nm. What is the star's radial velocity, and is it moving toward or away from us?" Use the formula $\Delta\lambda/\lambda = v/c$ for non-relativistic speeds, where $c = 3 \times 10^5$ km/s. Then ask the LLM: "How is this measurement used to discover exoplanets — specifically, the radial-velocity method?" Evaluate whether the response correctly calculates ~70 km/s recession velocity and correctly identifies that an orbiting planet causes the host star to wobble, producing periodic Doppler shifts.

**Exercise 3.** A spectral line's width tells us about the star's rotation, turbulence, and pressure. Prompt an LLM: "Why does a rapidly rotating star show wider spectral lines than a slowly rotating one? Walk through the Doppler broadening: light from one limb of the star is blueshifted (rotating toward us) while light from the other limb is redshifted (rotating away), broadening the line." Then ask: "How is this used to measure stellar rotation rates? Why is this method most useful for moderately rotating stars?" Evaluate whether the response correctly identifies that the line broadening reveals the projected rotational velocity ($v \sin i$), and that very slow or very fast rotation become difficult to measure (slow gets lost in other broadening mechanisms; fast becomes ambiguous with other broadening sources).

**Exercise 4.** The Hertzsprung-Russell diagram plots stellar luminosity against temperature. Prompt an LLM: "Why does the H-R diagram show stars concentrated in specific regions (main sequence, red giant branch, white dwarf region) rather than randomly distributed? What does the position of a star on the diagram tell us about its evolutionary stage?" Evaluate whether the response correctly identifies that stars spend most of their lives on the main sequence (hydrogen burning in core), then briefly traverse the post-main-sequence regions during late evolution, producing the observed clustering. Where you find a star on the H-R diagram tells you its current life stage.

**Exercise 5 (challenge).** A spectral line's Doppler shift can also reveal whether two stars in a binary system are gravitationally bound and orbiting each other — through periodic alternating blueshift and redshift. Prompt an LLM: "For a spectroscopic binary with an orbital period of 15 days and a maximum velocity amplitude of 100 km/s, calculate the orbital separation and the mass function. What is the mass function, and why is it less than the total mass of the system?" Evaluate whether the response correctly applies Kepler's third law to relate the period to the orbital separation, and identifies that the mass function depends on the orbital inclination (which is generally unknown for spectroscopic binaries unless eclipses or other geometric clues are available).

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Antonia Maury** was a member of the Harvard Computers who refined Annie Jump Cannon's spectral classification by adding a second dimension — sharp vs. fuzzy spectral lines — that turned out to encode stellar luminosity. Hertzsprung built on her insight to create the diagram that bears his name and Russell's.

**Run this:**

```
Who was Antonia Maury, and how does her two-dimensional spectral classification connect to the analysis of starlight we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about her career or ideas.
```

Search **"Antonia Maury"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain in plain language why "sharp" vs. "fuzzy" spectral lines reveal stellar luminosity.
- Ask it to compare how Maury's contribution is usually credited next to Cannon's.

What changes? What gets better? What gets worse?
