# Chapter 17 — Analyzing Starlight

*How a prism turned a point of light into a complete biography.*

---

Sirius looks simple. It is the brightest star in the night sky, burning white in Canis Major, and at first glance the interesting facts about it seem exhausted by that brightness. A point. A white point.

But that white point has traveled 8.6 light-years to reach your eye, and it carries, encoded in the pattern of its wavelengths, a message. The message says: I am 10,000 Kelvin at my surface. I am mostly hydrogen, with traces of calcium and iron. I am moving toward you at 5.5 kilometers per second. I rotate with a period of about 12.5 hours, fast enough that my equator bulges. I am a main-sequence star, not a giant — you can read that in the width of my spectral lines.

A spectrograph — a prism that spreads the light into its component wavelengths — reveals the message. What you see is a continuous band of color, crossed by thin dark lines. Those lines are not in the starlight itself. They are absences. Atoms in the star's outer atmosphere have plucked specific wavelengths out of the beam. Every element leaves its mark at precise positions. Read the pattern of marks, and you can reconstruct what the star is made of, how hot it burns, whether it is moving toward you or away, how fast it spins, whether it is a dwarf or a giant.

I want to explain how that reading works — not just the names and categories, but why it works. Why temperature determines which lines appear. Why line width tells you about pressure. Why a slight shift in wavelength measures velocity. The machinery is not complicated, but it is not obvious either, and I think it is one of the most elegant chains of reasoning in all of observational science.

---

## Brightness, Distance, and the Magnitude Scale

Start with a problem that took centuries to fully resolve: stars look brighter or dimmer, but brightness as you observe it from Earth conflates two completely different things — how much energy the star actually produces, and how far away it is.

Astronomers distinguish these with two words. **Luminosity** is the total power output of the star — watts, radiated equally in all directions. **Apparent brightness** is the fraction of that power that arrives at Earth.

The geometry is straightforward. A star radiates equally in all directions. Draw a sphere of radius $r$ around it. The star's luminosity is distributed over the surface of that sphere, which has area $4\pi r^2$. Double the distance, and the sphere has four times the area. The same luminosity is spread over four times as much surface. Any detector — your eye, a telescope mirror — catches one quarter as much light. This is the inverse square law:

$$b = \frac{L}{4\pi r^2}$$

<!-- → [DIAGRAM: a point-source star at center, three concentric spheres at distances r, 2r, and 3r; a single unit patch on the innermost sphere projected outward onto the middle and outer spheres, showing it covers 4 and 9 patches respectively; annotate the intensity ratios 1, 1/4, 1/9 beneath each sphere; label the total luminosity L as constant across all three surfaces] -->

The consequence is a frustrating one. Measure the apparent brightness of a star, and you know the left side of this equation. But there are two unknowns on the right side — luminosity and distance. Without independent information about one of them, you cannot solve for the other. This haunted astronomy for centuries. A bright star might be intrinsically luminous or simply close. A faint star might be intrinsically dim or simply far.

The system used to quantify apparent brightness is a historical artifact, and I mention it here because you will encounter it everywhere. In about 150 BCE, Hipparchus sorted the visible stars into six classes by eye — the brightest called first-magnitude, the faintest visible to the naked eye called sixth-magnitude. When 19th-century astronomers finally had precise photometers, they measured the actual brightness ratio between first and sixth magnitude stars and found it was roughly 100 to 1. By convention, that ratio was locked in: five magnitudes equals a factor of exactly 100 in brightness. One magnitude step therefore corresponds to the fifth root of 100, which is about 2.51.

The system has two unintuitive properties that catch people constantly. First, it runs backward — larger magnitude numbers mean fainter objects. Sirius is magnitude $-1.5$. Venus at its brightest is $-4.4$. The Sun is $-26.8$. The faintest galaxies detected by modern telescopes are around magnitude 30. Second, magnitudes do not add — they are logarithmic. A difference of 4.5 magnitudes corresponds to a brightness ratio of $2.51^{4.5} \approx 100$.

<!-- → [CHART: a horizontal magnitude scale from −30 to +30, marked as a number line; place labeled points for the Sun (−26.8), full Moon (−12.7), Venus (−4.4), Sirius (−1.5), naked-eye limit (+6), binocular limit (+10), Hubble deep field limit (+30); use a log-scale brightness axis below showing the actual energy flux ratios; the goal is to make the backward-running, logarithmic nature of the scale visually clear in one glance] -->

The magnitude scale persists because it was established early and the astronomical community has used it continuously for two thousand years. Standardization has real value: every astronomer in every country knows exactly what "magnitude 6" means.

---

## Why Color Tells You Temperature

Every object radiates electromagnetic energy. The hotter the object, the more it radiates, and the shorter the wavelengths at which it radiates most intensely. Wien's displacement law quantifies this:

$$\lambda_{\text{peak}} = \frac{b}{T}$$

where $b \approx 2.9 \times 10^{-3}$ m·K and $T$ is the surface temperature in Kelvin. A star with a surface temperature of 30,000 K peaks in the ultraviolet — most of its visible emission is blue. A star at 3,000 K peaks in the infrared — most of its visible emission is red. At 5,800 K, the peak sits in the green part of the visible spectrum, which is why sunlight looks yellowish-white.

This is why the colors of stars in the night sky form a sequence, not a random scatter. The colors are thermometers.

In practice, astronomers measure this temperature through **color indices**. You observe the star through a blue filter and record its apparent magnitude in blue light, $B$. You observe through a visual (yellow-green) filter and record $V$. The color index is $B - V$.

This number is independent of distance. A red star looks red whether it is ten light-years away or ten thousand, because the ratio of its blue-to-yellow output is a property of its temperature, not its location. By convention, the color index of the star Vega (about 10,000 K) is defined to be zero. Hotter stars emit more blue light relative to visual light, so they have negative $B - V$. Cooler stars have positive $B - V$. The Sun, at 5,800 K, has $B - V \approx +0.65$.

A star with $B - V = -0.2$ is hotter than the Sun — probably around 10,000 to 15,000 K. A star with $B - V = +1.5$ is much cooler — below 4,000 K. From a single number obtained by pointing a telescope through two filters, you have the surface temperature of a star that may be hundreds of light-years away.

<!-- → [CHART: scatter plot of B−V color index (x-axis, −0.4 to +2.0) versus surface temperature in Kelvin (y-axis, log scale, 2,000 to 50,000 K); plot representative stars as labeled points: Rigel (B−V ≈ −0.03, 12,000 K), Sirius (B−V ≈ 0.00, 10,000 K), Sun (B−V ≈ +0.65, 5,800 K), Arcturus (B−V ≈ +1.23, 4,300 K), Betelgeuse (B−V ≈ +1.85, 3,500 K); color-code the points from blue to red; draw the smooth calibration curve through them] -->

---

## The Spectral Sequence and Why Temperature Dominates the Lines

Here is the deep puzzle that confused the first stellar spectroscopists.

When you spread starlight through a prism, you see a rainbow crossed by thin dark lines. Different stars have different patterns of lines. The first people to study these patterns thought the differences in lines meant differences in composition — that some stars were rich in hydrogen, others in calcium, others in iron. This turned out to be wrong, in one of the most important corrections in the history of astrophysics.

Almost all stars have the same composition: roughly 73% hydrogen by mass, 25% helium, and about 2% everything else combined. The differences in spectral lines are not about what elements are present. They are about temperature.

Understanding why requires a short detour into atomic physics.

An atom absorbs light when one of its electrons jumps from a lower energy level to a higher one, absorbing a photon with exactly the right energy. The specific photon energies that an atom can absorb depend on the gaps between its allowed energy levels — and those are fixed by the structure of the atom. Hydrogen absorbs at specific wavelengths, calcium at different wavelengths, sodium at yet others. This is the fingerprinting mechanism.

But here is the catch: the atom can only absorb if it has electrons in the right place to begin with.

Consider hydrogen in a very hot star — say, 40,000 K. At this temperature, the thermal energy is high enough to strip electrons away from hydrogen nuclei entirely. Ionized hydrogen has no electrons. No electrons means no absorption transitions. Hydrogen is abundant, but completely invisible in the spectrum.

Now consider hydrogen in a very cool star — say, 3,000 K. Here, hydrogen atoms are neutral and their electrons sit mostly in the ground state (the lowest energy level, $n = 1$). To absorb visible light, an electron needs to be in the second energy level ($n = 2$), from which it can jump to higher levels and absorb photons in the visible Balmer series. But in a cool star, almost no electrons are thermally excited to $n = 2$. They are all in $n = 1$. Almost no visible hydrogen absorption.

The sweet spot is around 10,000 K. At this temperature, roughly 1 in 100 million hydrogen atoms has its electron in the $n = 2$ level — enough to produce very strong absorption lines without the bulk of the hydrogen being ionized. This is why the brightest hydrogen lines appear in white A-type stars: not because those stars have the most hydrogen, but because their temperature puts hydrogen's electrons exactly where they need to be to absorb visible light.

The same logic applies to every element and every ionization state. Calcium ionized once ($\text{Ca}^+$) produces its strongest visible lines around 6,000 K — which is why those lines dominate in G and K stars, even though there is far less calcium than hydrogen. Titanium oxide molecules form only below about 3,500 K — which is why molecular bands appear only in the coolest M stars. Each feature is a temperature indicator.

<!-- → [CHART: line strength vs. temperature for the major spectral features — x-axis: temperature from 2,000 K to 50,000 K; y-axis: relative line strength (0 to peak); draw overlapping bell curves for: hydrogen Balmer series (peaks ~10,000 K), neutral helium (peaks ~22,000 K), ionized helium (peaks ~40,000 K), ionized calcium Ca+ (peaks ~6,000 K), neutral iron (peaks ~4,500 K), titanium oxide TiO (peaks ~3,000 K); mark the OBAFGKM spectral types on the temperature axis below; this is the core visual of the chapter — it shows why different features appear at different types] -->

In the 1890s, Annie Jump Cannon at Harvard organized this understanding into a classification system. She kept seven letters from an earlier alphabetical attempt: O, B, A, F, G, K, M, ordered by decreasing temperature. She classified roughly 500,000 stars by eye, looking at photographic plates through a microscope, at a rate of up to three stars per minute. She subdivided each class into decimal subtypes 0 through 9. The Sun is G2 — second-hottest within the G class.

Here is the sequence, with temperatures and characteristic features:

**O stars** (above 30,000 K): ionized helium, weak hydrogen. Blue.

**B stars** (10,000–30,000 K): neutral helium, strong hydrogen. Blue-white.

**A stars** (7,500–10,000 K): strongest hydrogen lines, weak ionized metals. White. (Sirius, Vega.)

**F stars** (6,000–7,500 K): strong hydrogen, strong ionized calcium, metal lines appearing. Yellow-white.

**G stars** (5,200–6,000 K): weak hydrogen, strong ionized calcium, sodium. Yellow. (The Sun.)

**K stars** (3,700–5,200 K): weak hydrogen, strong neutral metals. Orange. (Arcturus.)

**M stars** (2,400–3,700 K): titanium oxide molecules, neutral metals. Red. (Betelgeuse.)

This is a thermometer, not a taxonomy. The sequence is not a collection of pigeonholes — it is a continuous scale of temperature, and what changes along it is the atomic physics of which electrons are in which states.

A common misconception is worth addressing directly: the absence of hydrogen lines does not mean the absence of hydrogen. It means the temperature is wrong for hydrogen to absorb visible light. O stars have essentially no visible hydrogen lines, but they are more than 70% hydrogen by mass. Every star in the sequence is mostly hydrogen. The lines tell you about temperature first.

---

## What Line Widths, Shifts, and Broadening Reveal

Temperature is the dominant story in a stellar spectrum, but not the only one. Once you know the temperature — from the pattern of which lines appear — you can ask more subtle questions by looking at the shapes and positions of the lines themselves.

**Line widths and stellar size**

In a dense gas, atoms collide frequently. Each collision slightly perturbs the energy of the transition, smearing the line over a range of wavelengths. More collisions mean broader lines. Fewer collisions mean sharper, narrower lines.

A giant star has an extended, low-density atmosphere — the material is spread over a large volume. Few collisions. Narrow lines. A dwarf star is compact and dense. More collisions. Broad lines. Two stars with identical surface temperatures will have the same line positions — the same temperature-sensitive features — but different line widths. Reading the widths distinguishes a giant from a dwarf without knowing the distance. This is not subtle. A giant and a main-sequence star of the same spectral type can be separated by careful photometry.

**Doppler shift and radial velocity**

A source of waves moving toward you emits waves that arrive more compressed — shorter wavelength, higher frequency. Moving away, the waves are stretched — longer wavelength, lower frequency. The magnitude of this shift depends on the velocity:

$$\frac{\Delta \lambda}{\lambda} = \frac{v}{c}$$

where $\Delta\lambda$ is the shift in wavelength, $\lambda$ is the rest wavelength, $v$ is the radial velocity (velocity along the line of sight), and $c$ is the speed of light.

In 1868, William Huggins observed the spectrum of Sirius and saw its hydrogen lines slightly shifted — the first measurement of a stellar radial velocity. The technique is now routine. A shift of 0.1 nm in a line normally at 656 nm (the Balmer-alpha line) corresponds to a velocity of about 46 km/s. The measurement is precise enough that astronomers routinely detect the radial velocity wobble of a star caused by an orbiting planet — amplitudes of a few meters per second over months.

**Line broadening and rotation**

Imagine a star rotating. The edge rotating toward you is Doppler-shifted to shorter wavelengths. The edge rotating away is shifted to longer wavelengths. The center of the disk contributes at the rest wavelength. The observed spectral line is the sum of all these contributions from different parts of the stellar surface — a smeared, broadened line rather than a sharp one.

The width of this rotational broadening is proportional to the star's equatorial rotation velocity. Vega rotates so fast — once every 12.5 hours — that it is noticeably oblate, roughly 23% wider at the equator than at the poles. Its spectral lines are measurably broadened. The Sun rotates once per month; its lines are narrow by comparison. Young stars tend to rotate fast; as they age, magnetic braking bleeds away angular momentum and they slow.

<!-- → [DIAGRAM: four panels showing how spectral line shape encodes different information — panel 1: sharp narrow line (non-rotating, low-pressure dwarf); panel 2: pressure-broadened wide line (high-density atmosphere); panel 3: sharp line shifted left/blue (star moving toward observer); panel 4: rotationally broadened line with smooth rounded profile (fast-rotating star); label each panel with the physical cause and the parameter it measures] -->

**Line strength and elemental abundance**

Given two stars with the same temperature and pressure, if a particular spectral line is stronger in one than the other, that star contains more of the corresponding element. The strength of an absorption line is proportional to the number of atoms producing it.

This is how we know that some stars are "metal-rich" — having two or three times the solar abundance of iron and other heavy elements — while others, old stars formed early in the galaxy's history, have heavy-element abundances a hundred times below the solar value. The word "metals" in this context means all elements heavier than helium; the usage is a legacy of early spectroscopy.

---

## The Chemical Biography of the Galaxy

These measurements, accumulated across hundreds of thousands of stars, tell a story.

Almost all stars are almost entirely hydrogen and helium. These two elements were created in the Big Bang, three minutes after the universe began. Everything else — carbon, oxygen, silicon, iron, calcium, the elements that make planets and people — was made later, in stellar cores, through nuclear fusion. A massive star spends its life fusing hydrogen into helium, helium into carbon, carbon into oxygen and neon and magnesium, all the way up toward iron. When the star exhausts its fuel and collapses, the outer layers are expelled in a supernova, scattering those elements into the surrounding gas. The next generation of stars forms from this enriched material.

The consequence is that the heavy-element abundance of a star tells you roughly when it was born. Old stars, formed when the galaxy was young and few previous stellar generations had yet enriched the gas, have low metal abundances — sometimes 100 or 1000 times less than the Sun's. Young stars, formed from gas already enriched by billions of years of stellar processing, have metal abundances at or above solar.

<!-- → [CHART: scatter plot of stellar metallicity (iron abundance [Fe/H] on y-axis, from −3 to +0.5 on a log scale) versus stellar age in billions of years (x-axis, 0 to 13); plot a representative sample of stars from survey data showing the trend of decreasing metallicity with increasing age; mark the Sun at age ~4.6 Gyr and [Fe/H] = 0; shade the region occupied by metal-poor halo stars (old, low metallicity) vs. disk stars (younger, higher metallicity); annotate the slope as "each generation of stars enriches the next"] -->

The Sun, at 0.2% metals by mass, sits in the middle of this distribution — neither unusually old nor unusually young. The fact that Earth exists, with its iron core and silicate mantle, its carbon-based life — that exists because earlier generations of massive stars lived and died, enriching the molecular cloud from which the solar system condensed.

When you measure the spectrum of a faint, metal-poor star in the outer halo of the galaxy, you are reading the chemistry of the early universe, preserved in an ancient object. When you measure the spectrum of a young star in a star-forming region, thick with metals, you are reading the output of billions of years of nucleosynthesis.

A star's spectrum is its biography. Temperature determines which lines dominate. Line widths tell you the pressure and the stellar size. Doppler shifts measure motion. Broadening measures rotation. Line strengths measure abundance. Point a spectrograph at a point of light, and in the pattern of dark lines crossing the rainbow you can read temperature, size, motion, rotation, and composition — a complete physical description of an object you will never visit, using light that left it years or centuries ago.

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

→ Search **"Antonia Maury"** on Wikipedia. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain in plain language why "sharp" vs. "fuzzy" spectral lines reveal stellar luminosity.
- Ask it to compare how Maury's contribution is usually credited next to Cannon's.

What changes? What gets better? What gets worse?
