# Chapter 6 — Analyzing Starlight

*A Danish chemist in 1905, a Princeton astronomer in 1913, and the discovery that a scatter plot of two numbers contains the entire life cycle of a star.*

---

In 1905, Ejnar Hertzsprung was a chemist in Copenhagen with astronomy as a hobby. He had read the spectral catalogs coming out of Harvard — specifically a refinement by Antonia Maury that flagged certain stars with unusually sharp, narrow absorption lines — and wondered whether the sharpness meant anything physical. So he did the simplest possible thing. He took stars whose distances were known from parallax, converted their apparent brightnesses into actual luminosities, and plotted luminosity against spectral class.

Most stars fell along a diagonal band. But the sharp-line stars Maury had flagged sat far above it — hundreds of times more luminous than other stars of the same spectral type.

![A reconstruction of Hertzsprung's 1905 spectral-class vs absolute-magnitude plot. Most stars fall along a diagonal main band. Maury's sharp-line c-type stars sit far above it as giants. Hertzsprung published in a jour...](../images/06-analyzing-starlight-fig-01.png)
*Figure 6.1 — Hertzsprung's 1905 Diagram Reconstructed*

Hertzsprung published in a photographic-industry journal that no astronomer read. The result was ignored for eight years. In 1913 Henry Norris Russell made the same plot independently and presented it to the Royal Astronomical Society. Russell's audience was the right one. The diagram entered astronomy bearing his name, with Hertzsprung's priority eventually acknowledged. The people who actually discovered the key — Maury, who identified the sharpness; Hertzsprung, who understood what it meant — came second in the naming.

What Hertzsprung had stumbled into is this: when you plot stars on a temperature-luminosity plane, they do not scatter at random. They cluster into three specific regions. Each region is a different physical state. The diagram is a snapshot of a movie we cannot otherwise see — every major phase in the life of a star, visible at once because the sky contains billions of stars in every stage simultaneously.

This chapter is about why the clustering exists and what it tells you.

---

## The thermometer: OBAFGKM

Before you can plot a temperature axis, you need to be able to measure stellar temperatures. You can do this two ways from a spectrum, and they give the same answer. Wien's law extracts temperature from the peak wavelength of the continuous emission. And the pattern of absorption lines — which atoms appear, which are missing — tells you the ionization state of the stellar atmosphere, which is a direct function of temperature. Two independent methods, consistent results: that agreement is what makes the temperature axis real.

The classification scheme is older than the physics behind it. In the 1890s Williamina Fleming sorted stellar spectra into 16 alphabetical classes by hydrogen line strength. The ordering tracked temperature non-monotonically, because hydrogen lines happen to peak at an intermediate temperature, not the highest one. Annie Jump Cannon, working at Harvard between 1901 and 1912, fixed this: she dropped most of Fleming's letters, kept seven (O, B, A, F, G, K, M), reordered them by actual temperature, and subdivided each with numerical subtypes 0–9. She classified roughly 225,000 stars personally for the Henry Draper Catalogue, reportedly at a rate of three stars per minute. The system still works a century later.

![Seven stacked spectra from hottest to coolest. Each shows a continuum strip with characteristic absorption features and an example star: Rigel (B8), Sirius (A1), Procyon (F5), Sun (G2), Arcturus (K1), Betelgeuse (M1)....](../images/06-analyzing-starlight-fig-02.png)
*Figure 6.2 — OBAFGKM Spectral Sequence with Example Spectra*

The sequence runs from hottest to coolest:

**O** stars are above 30,000 K. The identifying line is He II — ionized helium, visible only because the temperature is high enough to strip the first electron from helium, which costs about 24 electron-volts. Hot enough to do that. Weak hydrogen. Blue.

**B** stars run from 10,000 to 30,000 K. Neutral helium now, and hydrogen strengthening. Rigel is B8.

**A** stars are 7,500 to 10,000 K, and they have the strongest hydrogen Balmer lines in the entire sequence. White. Sirius is A1, Vega is A0.

**F** stars, 6,000 to 7,500 K. Hydrogen weakening, ionized calcium coming in. Yellow-white. Procyon is F5.

**G** stars, 5,200 to 6,000 K. Calcium lines now dominant, neutral metals appearing. The Sun is G2. Yellow.

**K** stars, 3,700 to 5,200 K. Strong neutral metal lines, no helium at all. Orange. Arcturus is K1.

**M** stars below 3,700 K. Titanium oxide molecular bands — molecules survive only because the temperature is finally low enough that collisions cannot break them apart. Red. Betelgeuse is M1, Proxima Centauri is M5.

<!-- → [TABLE: OBAFGKM sequence — columns: class, temperature range (K), identifying spectral feature, example star, color — rows O through M; helps student connect the abstract sequence to recognizable stars and specific atomic physics] -->

The non-monotonicity of hydrogen lines is the thing worth pausing on. The Balmer lines — the hydrogen absorption lines visible in optical spectra — are not strongest in the hottest stars. They peak in A stars around 10,000 K. To absorb visible light, hydrogen needs an electron sitting in the $n=2$ energy level. Whether electrons end up there is governed by the Boltzmann distribution. Too hot, and hydrogen is completely ionized — no bound electrons at all, no absorption. Too cool, and all the electrons sit in the ground state ($n=1$) and the Balmer transitions starve. Around 10,000 K, the $n=2$ level is optimally populated.

![Two coupled curves. Panel A: fraction of hydrogen atoms in the n=2 state vs temperature, peaking near 10,000 K. Panel B: measured Hα line strength across OBAFGKM, peaking at A stars. Cool stars: n=2 starved. Hot stars...](../images/06-analyzing-starlight-fig-03.png)
*Figure 6.3 — Why Hα Peaks at A Stars: Boltzmann Population*

Here is the thing that almost every non-astronomer gets wrong: the varying line strengths across the OBAFGKM sequence do *not* mean the stars have different compositions. Almost all of them are roughly the same mixture of hydrogen and helium. What changes from O to M is not what atoms are present but which atoms can absorb visible light at that surface temperature. The sequence is a thermometer, not a taxonomy.

<!-- → [CHART: Hydrogen Balmer line strength vs. surface temperature — single curve peaking around 10,000 K (A stars), dropping steeply toward hotter O stars (fully ionized, no bound electrons) and cooler K/M stars (electrons in ground state only); student should see why "strongest hydrogen lines" ≠ "hottest stars" and understand the Boltzmann distribution is the mechanism] -->

---

## The diagram and why it has structure

Now we have a temperature axis. Plot it horizontally, hot at the left by convention. Add a vertical luminosity axis — total power output in solar units, logarithmic, brightest at top. Collect every star whose distance and spectrum we know. Plot.

The result does not fill the plane. Ninety percent of stars crowd into a single diagonal band running from upper-left (hot and luminous) to lower-right (cool and faint). Two other clusters appear far off this band — one in the upper-right, one in the lower-left. Why?

The entire answer is one equation. The Stefan-Boltzmann law, applied to a sphere:

$$L = 4\pi R^2 \sigma T^4$$

Or in solar units:

$$\frac{L}{L_\odot} = \left(\frac{R}{R_\odot}\right)^2 \left(\frac{T}{T_\odot}\right)^4$$

This equation has three variables. Fix any two and the third is determined. On the H-R diagram, $T$ is the horizontal axis and $L$ is the vertical axis — so every point on the diagram corresponds to a specific stellar radius $R$. Lines of constant radius slope diagonally across the diagram, from upper-left to lower-right. A star at 10,000 K and $10^4 L_\odot$ has a radius of roughly 30 $R_\odot$. Move that star to 3,500 K at the same luminosity and the radius balloons past 200 $R_\odot$ — the cooler temperature means each square meter of surface radiates much less, so you need far more surface area to produce the same total output.

<!-- → [DIAGRAM: H-R diagram skeleton — log T horizontal axis (reversed, hot left), log L vertical axis; four diagonal lines of constant radius labeled 0.01, 0.1, 1, 10, 100 R_☉ sloping upper-left to lower-right; student should see that any (T, L) position implies a specific R via Stefan-Boltzmann] -->

The main sequence is about 90% of nearby stars, and it falls along a diagonal that roughly parallels the constant-radius lines — but not exactly. What the main sequence is, physically, is a mass ladder. High-mass stars sit at the upper-left: they are hot and luminous. Low-mass stars sit at the lower-right: cooler and fainter. The connection between mass and position runs through nuclear physics — a more massive star has a hotter, denser core, which burns hydrogen faster, which produces more luminosity, which pushes the surface to higher temperature. The mass-luminosity relation from binary-star measurements gives roughly $L \propto M^{3.5}$ to $M^4$ over most of the sequence. The main sequence is a single-parameter family, and the parameter is mass.

The Sun sits about two-thirds of the way down — mid-mass, mid-temperature, mid-luminosity. Below about 0.08 solar masses, cores never reach the temperature needed for sustained hydrogen fusion, and those objects form a separate population: brown dwarfs, sub-stellar objects, not quite stars.

Now the two outlier populations.

**Upper right: giants and supergiants.** These stars are cool — 3,000 to 5,000 K — but enormously luminous, $10^2$ to $10^5$ solar luminosities. The Stefan-Boltzmann equation has only one solution for that combination: enormous radii. Betelgeuse, an M1 supergiant, has a radius of roughly 700 solar radii. Placed at the Sun's position, it would engulf Mars. These stars are not on the main sequence because they are no longer burning hydrogen in their cores. They have exhausted core hydrogen and swollen into giants — the core contracts, the outer layers expand, the surface cools while total luminosity rises.

**Lower left: white dwarfs.** Hot — 10,000 to 30,000 K — but very faint, $10^{-3}$ to $10^{-4}$ solar luminosities. Tiny: Sirius B has a radius of about 0.008 solar radii, roughly Earth-sized, at nearly one solar mass. Densities a million times the Sun's average. White dwarfs are stellar corpses — stars that have exhausted both their hydrogen and helium fuel and shed their outer layers. What holds them up against gravity is not thermal pressure from fusion reactions but electron degeneracy pressure, a purely quantum-mechanical effect. The electrons are packed so tightly that the Pauli exclusion principle itself resists further compression. There is no classical analog.

<!-- → [DIAGRAM: Full H-R diagram with all three populations populated — main sequence diagonal band upper-left to lower-right, giant/supergiant cloud upper-right, white dwarf cluster lower-left; each region labeled with its evolutionary state (core H burning / post-main-sequence expansion / stellar corpse); the near-empty "Hertzsprung gap" between main sequence and giant branch annotated as a fast evolutionary transit] -->

The clustering is the point. If stars populated the temperature-luminosity plane uniformly, the diagram would be a formless cloud. Instead they live in three specific regions — main sequence, giant branch, white dwarf box — each corresponding to a different evolutionary phase. A long-lived phase (core hydrogen burning, tens of billions of years for a solar-mass star) concentrates many stars; a fast phase (the crossing from main sequence to giant branch) shows almost none.

![Hertzsprung-Russell diagram with reversed temperature axis. The main sequence runs diagonally from hot luminous upper-left to cool faint lower-right. The giant branch sits at cool high-luminosity upper-right. White dw...](../images/06-analyzing-starlight-fig-04.png)
*Figure 6.4 — Modern H-R Diagram: Three Regions and Constant-Radius Lines*

The diagram is not a description of stellar types. It is a map of stellar time. Where a star sits tells you what it is doing at this moment in a life measured in billions of years.

---

## The second axis from a spectrum alone

Here is the useful part. To use the H-R diagram in the way I have described, you need two numbers: a temperature (from the spectrum) and a luminosity (which requires both the spectrum *and* a distance). Distance measurement is hard. For most stars, we do not have a reliable parallax. Can you get both axes from the spectrum alone?

Yes, because of line width.

Maury had noticed in the 1890s that some stars showed unusually sharp absorption lines while others of the same spectral class showed broader ones. Cannon thought this was a measurement artifact and dropped the distinction from the official catalog. Hertzsprung, plotting Maury's "sharp-line" stars, found they were exactly the upper-right outliers — the luminous giants. Maury had not found a measurement artifact. She had found a luminosity diagnostic.

The mechanism is pressure broadening. In a dense stellar atmosphere, atoms collide frequently. Each collision perturbs an atom's energy levels slightly and randomly. The combined effect of millions of such collisions is to smear the otherwise sharp absorption line into a broader profile. More collisions, broader lines.

Now compare a main-sequence star to a giant of the same spectral type — say, two K2 stars. The main-sequence K2 star has high surface gravity, roughly 274 m/s² for the Sun and higher for stars of similar mass. High gravity means high atmospheric density, high collision rate, broad lines. The K2 giant has the same composition spread over a radius perhaps ten times larger. Surface gravity falls as $g \propto M/R^2$, and a giant with twice the mass but ten times the radius has surface gravity $1/50$ of the main-sequence star. Low gravity, low density, rare collisions, sharp lines.

![Two K0 spectra side by side. The dwarf has broad absorption lines from high photospheric pressure and frequent atomic collisions; the giant has sharp narrow lines from low surface gravity and thin atmosphere. Below: t...](../images/06-analyzing-starlight-fig-05.png)
*Figure 6.5 — Pressure Broadening: How to Distinguish a Dwarf from a Giant*

The two stars have nearly identical line *positions* — same temperature, same transitions, same elements absorbing. They differ in line *width* by an amount that a decent spectrograph can measure directly.

<!-- → [DIAGRAM: Side-by-side spectral line profiles for K2V and K2III — same central wavelength (identical temperature/transition), K2V showing broad Gaussian profile (high pressure, many collisions), K2III showing narrow sharp profile (low pressure, few collisions); student should see that position encodes temperature while width encodes surface gravity / luminosity class] -->

This is how the six **luminosity classes** work:

- **Ia** — luminous supergiants
- **Ib** — supergiants
- **II** — bright giants
- **III** — normal giants
- **IV** — subgiants
- **V** — main sequence (dwarfs)

The Sun is G2V. Betelgeuse is M1Ia. From a spectrum at sufficient resolution — no distance required — you can assign both the spectral type (temperature) and the luminosity class (approximate position on the luminosity axis), and from those two you can read off temperature, luminosity, and via the Stefan-Boltzmann equation, radius.

A G2V star and a G2III star look nearly identical at casual inspection. The luminosity difference is a factor of about 50. The radius difference is a factor of about 7. The volume difference is roughly 350. Without line-width analysis and the H-R diagram framework, you would classify them as the same kind of object.

---

## Reading a star from one spectrum

Let me show you how this works in practice.

You observe a star. Continuous peak at 580 nm; strong ionized calcium lines, moderate hydrogen, prominent neutral metals; lines notably sharp; parallax 0.025 arcseconds (distance 40 parsecs); apparent magnitude $V = 3.5$.

**Temperature.** Wien's law: $T = (2.9 \times 10^{-3} \text{ m K}) / (580 \times 10^{-9} \text{ m}) = 5{,}000$ K. The line pattern — strong Ca II, moderate hydrogen, neutral metals, no helium — is consistent with K0. Two methods agree.

**Absolute magnitude.** The distance modulus: $M_V = m_V - 5\log_{10}(d/10\,\text{pc}) = 3.5 - 5\log_{10}(4) = 0.49$.

**Luminosity.** The Sun sits at $M_V \approx +4.83$. The difference is 4.34 magnitudes. Each 2.5 magnitudes is a factor of 10 in luminosity:

$$\log_{10}(L/L_\odot) = (4.83 - 0.49)/2.5 = 1.74 \quad\Longrightarrow\quad L \approx 55\,L_\odot$$

**Radius.** From Stefan-Boltzmann in solar units, with $T_\odot = 5{,}772$ K:

$$\left(\frac{R}{R_\odot}\right)^2 = \frac{L/L_\odot}{(T/T_\odot)^4} = \frac{55}{(5000/5772)^4} = \frac{55}{0.563} \approx 98 \quad\Longrightarrow\quad R \approx 9.9\,R_\odot$$

**Luminosity class.** Sharp lines at K0, radius $\sim 10\,R_\odot$: a class III giant. Full designation: K0III. Aldebaran is K5III with comparable properties.

From a few hours of telescope time — one spectrum, one parallax — you have located the star on the H-R diagram, measured its radius to within 10%, and identified it as a post-main-sequence giant no longer fusing hydrogen in its core.

<!-- → [DIAGRAM: H-R diagram with this worked example's star plotted — position at T ≈ 5,000 K, L ≈ 55 L☉, clearly above the main sequence in the giant branch; dashed lines showing the constant-radius line passing through the point at ~10 R☉; annotations showing the three-step calculation path: spectrum → T, parallax+magnitude → L, Stefan-Boltzmann → R] -->

![A five-step worked example. Wien's law gives temperature from peak wavelength. Parallax gives distance. Apparent magnitude with distance gives absolute magnitude and luminosity. Stefan-Boltzmann gives radius. The star...](../images/06-analyzing-starlight-fig-06.png)
*Figure 6.6 — Worked Example: From Spectrum and Parallax to Position on H-R Diagram*

---

## What the diagram does not tell you

The H-R diagram tells you what a star is doing right now and roughly what mass it has. It does not, by itself, tell you how old the star is or which direction it will move next.

To turn the diagram into a clock — to say "this cluster of stars is 500 million years old" — you need theoretical evolutionary tracks: calculations of how a star of a given mass moves through the temperature-luminosity plane as it burns through hydrogen, then helium, then the heavier elements. Those tracks come from stellar structure theory, not from the diagram alone. The diagram plots the population. The theory predicts the trajectories. Together they give you stellar ages.

One honest limit worth flagging: the H-R diagram's clean readout assumes the Vogt-Russell theorem — that a star's structure is determined entirely by its mass and composition, with nothing else mattering. For most normal stars this is an excellent approximation. For low-mass M dwarfs, eclipsing-binary measurements show a persistent 5–10% radius discrepancy with theoretical models. The leading explanation is magnetic inflation of the stellar atmosphere. It is a small crack in the framework, worth knowing about, not yet a revision of the main story.

---

## What you should be able to do now

You should be able to place any of the seven spectral classes on a temperature scale, name the identifying feature of each, and explain why hydrogen lines peak in the middle of the sequence rather than at the hot end.

You should be able to use $L = 4\pi R^2 \sigma T^4$ to work in either direction: given temperature and luminosity, recover the radius; given temperature and radius, predict the luminosity.

You should be able to look at a point on the H-R diagram and say which of the three main populations it belongs to — main sequence, giant branch, or white dwarf region — and give a physical account of what is happening inside a star at that position.

You should be able to explain why two stars with the same spectral type but different luminosity classes have different line widths, and name the physical mechanism responsible.

And you should understand that the H-R diagram's structure — the fact that it has three populations rather than a uniform cloud — is not a classification scheme. It is a consequence of stellar evolution. Stars spend most of their time in long-lived phases and almost none in fast ones. The diagram shows you where the time is spent.

---

## Exercises

**Warm-up** *(Tests: OBAFGKM sequence; spectral line identification; temperature-composition distinction)*

1. List the seven OBAFGKM classes in order of decreasing surface temperature. For each, give the approximate temperature range, the identifying spectral feature, and one example star.

2. Hydrogen Balmer lines are strongest in A stars (~10,000 K), not in O stars (~40,000 K). Explain why, in terms of what determines the fraction of hydrogen atoms with electrons in the $n=2$ level. Your answer should invoke the Boltzmann distribution — but you do not need to calculate anything.

3. Two stars show identical absorption lines — same elements, same wavelengths. Is it possible for them to have different compositions? Why or why not? What does the OBAFGKM sequence actually measure?

**Application** *(Tests: Stefan-Boltzmann for radius; distance modulus; luminosity class from line width)*

4. Vega is an A0V star with $T \approx 9{,}600$ K and $L \approx 40\,L_\odot$. (a) Use $L/L_\odot = (R/R_\odot)^2(T/T_\odot)^4$ to compute Vega's radius in solar units. (b) A hypothetical star has the same temperature as Vega but sits on the giant branch at $L = 400\,L_\odot$. How does its radius compare to Vega's? Show the calculation.

5. A star has apparent magnitude $V = 6.2$ and parallax 0.050 arcseconds. (a) Compute the distance in parsecs. (b) Compute the absolute magnitude $M_V$. (c) The Sun has $M_V \approx +4.83$. How many times more luminous is this star than the Sun?

6. You observe two stars with spectral type G8. Star A has broad absorption lines; Star B has unusually sharp ones. (a) Assign a luminosity class (V or III) to each and justify your assignment. (b) Estimate the ratio of their surface gravities, given that Star B has roughly $10\times$ the radius of Star A at similar mass. (c) Which star has the higher atmospheric pressure, and why does that produce broader lines?

**Synthesis** *(Tests: connecting Stefan-Boltzmann, spectral class, luminosity class, and H-R diagram position)*

7. A star is observed to have spectral type M2 and luminosity class Ia (a luminous supergiant). Its temperature is approximately 3,500 K. Using $L/L_\odot = (R/R_\odot)^2(T/T_\odot)^4$ and a typical M2Ia luminosity of $\sim 10^5\,L_\odot$, calculate the radius in solar radii. Then state: (a) which H-R diagram region this star occupies; (b) what it is doing physically — i.e., what energy source is or is not operating in its core; (c) why it is not on the main sequence despite being more luminous than any main-sequence star visible to the naked eye.

8. The H-R diagram has a near-empty zone between the main sequence and the giant branch — the Hertzsprung gap. Explain why this gap exists, using the argument about how long different evolutionary phases last. Your answer should not invoke any specific timescale number; it should be a qualitative argument from first principles about why some phases are long-lived and others are not.

**Challenge** *(Tests: white dwarf physics; applying the diagram as a distance tool)*

9. Sirius B has $T \approx 25{,}000$ K and $L \approx 0.026\,L_\odot$. (a) Calculate its radius in Earth radii, given $R_\odot \approx 110\,R_\oplus$. (b) Its mass is approximately $1\,M_\odot$. Compute its average density relative to the Sun ($\rho_\odot \approx 1{,}400$ kg/m³). (c) Electron degeneracy pressure — not thermal pressure — supports Sirius B. Explain in one sentence why this is a fundamentally different support mechanism than what holds up a main-sequence star, and name the physical principle that prevents the electrons from being compressed further.

---

## LLM Exercises

### Build the H-R diagram simulator (`06-hr-diagram.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** An interactive H-R diagram with temperature on the x-axis (reversed, 40,000 K to 2,500 K, log scale) and luminosity on the y-axis ($L_\odot$, log, $10^{-4}$ to $10^6$). Three shaded regions: main sequence, giant branch, white dwarf box. Plot ~200 pre-loaded sample stars. Clicking anywhere returns inferred radius, spectral class, and luminosity class. Clicking a sample star reveals its name and properties.
>
> **Say.** Build an interactive D3 v7 visualization. Use $R/R_\odot = \sqrt{L/L_\odot} \cdot (T_\odot/T)^2$ for radius. Hardcode ~200 stars with name, T, L, class (Gaia DR3 or textbook table). Color-encode temperature: blue hot to red cool. Draw faint dashed lines of constant radius (0.01, 0.1, 1, 10, 100, 1000 $R_\odot$).
>
> **Constrain.** D3 v7 only. No stellar-evolution libraries. Filename: `06-hr-diagram.html`. Click events populate an info panel.
>
> **Verify.** (a) Sun position (5,772 K, 1 $L_\odot$): $R \approx 1 R_\odot$, G2V. (b) Betelgeuse (3,500 K, $10^5 L_\odot$): $R \approx 700 R_\odot$, M1Ia. (c) Sirius B (25,000 K, 0.026 $L_\odot$): $R \approx 0.008 R_\odot$, DA.

### Exploration

- Move along the main sequence from upper-left to lower-right. Radius changes slowly while luminosity changes by six orders of magnitude. The main sequence is a sequence of temperatures, not sizes.
- Fix temperature at 5,000 K, click five luminosities along the vertical. Verify $R \propto \sqrt{L}$ — factor of 100 in $L$, factor of 10 in $R$.
- Find the upper-left "forbidden" region (very hot, very luminous, very large). Are there stars there? What does the absence say about the largest stable hot stars?

### Bridge to Chapter 7

> **Show.** I can now place a star on the H-R diagram from its spectrum. But to get the luminosity axis right, I needed a distance. How are stellar distances measured — and how does the H-R diagram itself become a distance ruler?
>
> **Say.** Add a "distance mode": take apparent magnitude and spectral type, infer absolute magnitude from the main sequence, return a spectroscopic-parallax distance. Compare to Gaia parallax distances.
>
> **Verify.** For Sun-like stars within 50 pc, spectroscopic parallax agrees with Gaia to within ~20%. For evolved stars with ambiguous luminosity class, disagreement is much larger — that is the method's limit.

Save as `06b-spectroscopic-parallax-preview.html`. Lead-in to Chapter 7 — *Stellar Distances*.
