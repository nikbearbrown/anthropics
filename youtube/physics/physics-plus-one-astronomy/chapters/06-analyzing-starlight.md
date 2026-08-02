# Chapter 6 — Analyzing Starlight

*A Danish chemist in 1905, a Princeton astronomer in 1913, and the discovery that a scatter plot of two numbers contains the entire life cycle of a star.*

---

## Suggested titles

1. Analyzing Starlight
2. The Diagram That Reads a Star's Life
3. Temperature, Luminosity, and What Stars Are Doing

## TL;DR

If you plot every star's surface temperature against its luminosity, the stars do not scatter at random — they cluster into a few sharp bands, and each band corresponds to a different physical state. The Hertzsprung-Russell diagram is the single most important graph in stellar astronomy, and it works because surface temperature and luminosity are the two observables that pin down what a star is doing right now.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the OBAFGKM spectral sequence in order of decreasing surface temperature and explain why the dominant lines change along it.
2. **(Apply)** Use $L = 4\pi R^2 \sigma T^4$ to recover a stellar radius from a measured temperature and luminosity, and to predict the luminosity gap between stars of identical temperature but different size.
3. **(Analyze)** Read a star's position on an H-R diagram and infer its luminosity class — main sequence, giant, supergiant, or white dwarf — without additional information.
4. **(Analyze)** Distinguish a giant from a dwarf of the same spectral type using line width (pressure broadening), and explain the atomic-physics reason the test works.
5. **(Apply)** Build an interactive D3 simulation of the H-R diagram that lets a user place stars by luminosity and temperature, reveals the main sequence and giant branches, and returns physical properties on click.

**Prerequisites.** Chapter 3 (radiation laws, spectral lines, Doppler shift). Logarithms — the H-R diagram is log-log, and the math will not make sense if exponents do not. No prior stellar physics required; the relevant mechanism is built up from first principles in §3.2.

---

## Opening case: Hertzsprung's quiet plot, 1905

In 1905, Ejnar Hertzsprung was working as a chemist in Copenhagen with astronomy as his hobby. He had read Antonia Maury's spectral classification — a refinement of Annie Jump Cannon's catalog that flagged stars with unusually sharp absorption lines — and wondered whether the distinction meant anything physical. So he did a simple thing. He took stars whose distances were known from parallax, converted their apparent brightnesses into intrinsic luminosities, and plotted luminosity against spectral class.

Most stars fell along a diagonal band. But the sharp-line stars Maury had flagged sat far above it — hundreds of times more luminous than main-sequence stars of the same spectral type. Hertzsprung published in a photographic-industry journal that no astronomer read ([Hertzsprung, 1905](https://articles.adsabs.harvard.edu/cgi-bin/nph-iarticle_query?bibcode=1905WisZP...3..429H&db_key=AST&page_ind=0&data_type=GIF&type=SCREEN_VIEW&classic=YES)). The result was ignored for eight years. In 1913 Henry Norris Russell, at Princeton, made the same plot independently and presented it to the Royal Astronomical Society ([Russell, 1914](https://ui.adsabs.harvard.edu/abs/1914Obs....37..165R/abstract)). Russell's audience was the right one, and the diagram entered astronomy by his name. Hertzsprung's priority was eventually acknowledged.

What Hertzsprung had stumbled into was that stars are not a continuum. They live in specific regions of the temperature-luminosity plane, and which region tells you what they are doing — burning hydrogen in the core, swelling into a giant, cooling as a corpse. This chapter is about how that plot works and what it reveals.

---

## Core concept

### Stellar classification: the OBAFGKM sequence

Before any plotting, you need a temperature axis you can measure. Surface temperature is recoverable two ways from a spectrum (Chapter 3): Wien's law from the continuum peak, and the pattern of absorption lines from the ionization state of the absorbing atoms. The two methods agree to a few percent for normal stars. That agreement is what makes the temperature axis a real number rather than a convention.

The classification scheme itself is older than the physics. In the 1890s Williamina Fleming, working under Edward Pickering at Harvard, sorted spectra into 16 alphabetical classes A–P by hydrogen line strength ([Pickering & Fleming, 1890](https://articles.adsabs.harvard.edu/pdf/1890AnHar..27....1P)). The ordering — by hydrogen strength — tracked temperature non-monotonically, because hydrogen lines peak at an intermediate temperature. Annie Jump Cannon fixed this between 1901 and 1912: she dropped most of Fleming's letters, kept seven (O, B, A, F, G, K, M), reordered them by temperature, and subdivided each with subtypes 0–9. The Sun is G2. Cannon classified roughly 225,000 stars personally for the Henry Draper Catalogue at a rate that reportedly reached three per minute ([Hoffleit, 1971](https://articles.adsabs.harvard.edu/pdf/1971PASP...83..107H)). The system still works a century later, extended only by L, T, and Y classes for brown dwarfs and cold sub-stellar objects ([Kirkpatrick, 2005](https://www.annualreviews.org/doi/10.1146/annurev.astro.42.053102.134017)).

The sequence, with approximate temperatures and the lines that earn each class its membership:

- **O** ($> 30{,}000$ K). Ionized helium lines (He II) — visible only because the gas is hot enough to remove the first electron from helium, which requires about 24 eV. Weak hydrogen. Blue.
- **B** (10,000–30,000 K). Neutral helium (He I), strengthening hydrogen. Blue-white. Rigel is B8.
- **A** (7,500–10,000 K). Strongest hydrogen Balmer lines in the whole sequence. Weak ionized metals. White. Sirius is A1, Vega is A0.
- **F** (6,000–7,500 K). Hydrogen weakening, ionized calcium (Ca II) strengthening. Yellow-white. Procyon is F5.
- **G** (5,200–6,000 K). Ca II lines now dominant, hydrogen weaker still, neutral metals appearing. Yellow. The Sun is G2.
- **K** (3,700–5,200 K). Strong neutral metal lines, weak hydrogen, no helium features at all. Orange. Arcturus is K1.
- **M** ($< 3,700$ K). Titanium oxide (TiO) molecular bands — molecules survive only because the temperature is low enough that thermal collisions do not break them apart. Red. Proxima Centauri is M5, Betelgeuse is M1.

The instructive part is the non-monotonicity. Hydrogen lines are not strongest in the hottest stars; they peak in A stars near 10,000 K. To absorb visible light, hydrogen needs an electron in the $n=2$ level, and the fraction of atoms with electrons there is set by the Boltzmann distribution. Too hot, hydrogen is fully ionized — no bound electrons to absorb. Too cool, electrons sit in the ground state and the Balmer lines starve. Near 10,000 K, $n=2$ is populated optimally. Almost every star is mostly hydrogen and helium; the varying line strengths reflect varying temperatures, not varying composition.

**The sequence is a thermometer, not a taxonomy.** What changes from O to M is not what atoms are in the star but which atoms can absorb visible light at that surface temperature.

### The Hertzsprung-Russell diagram

Now the deep-dive. We have a temperature axis (spectral class, OBAFGKM, hot at left by convention) and a luminosity axis (total power radiated, solar units, log scale, brightest at top). Plot every star whose distance and spectrum we know. The question is why the result has structure.

The mechanism is one equation. The Stefan-Boltzmann law applied to a sphere gives a star's total luminosity:

$$L = 4\pi R^2 \sigma T^4 \quad\Longrightarrow\quad \frac{L}{L_\odot} = \left(\frac{R}{R_\odot}\right)^2 \left(\frac{T}{T_\odot}\right)^4$$

That is the entire underlying machinery. Fix $T$ on the horizontal axis and $L$ on the vertical, and you have one equation in one unknown ($R$). Every point on the H-R diagram corresponds to a specific stellar radius; **lines of constant radius are lines on the diagram**, sloping diagonally from upper-left to lower-right. A star at $T = 10{,}000$ K and $L = 10^4 L_\odot$ is roughly 30 $R_\odot$. A star at $T = 3{,}500$ K and the same luminosity is over 200 $R_\odot$ — the cooler temperature is overpowered by the surface area needed to match.

Now run the test. About 90% of stars near the Sun land in a single diagonal band from upper-left (hot, luminous) to lower-right (cool, dim) ([ESA Gaia DR3, 2023](https://www.cosmos.esa.int/web/gaia/data-release-3)). This is the **main sequence** — approximately a single-parameter family. That parameter is mass. The mass-luminosity relation from binary-star measurements (Chapter 7) gives $L \propto M^{3.5}$ to $M^4$ over most of the band. The main sequence is a mass ladder: high-mass at the hot, luminous end, low-mass at the cool, faint end. The Sun sits about two-thirds of the way down. Below about 0.08 $M_\odot$, cores never get hot enough for sustained fusion — those objects form a separate family, the brown dwarfs.

Two regions break the pattern.

**Upper right: giants and supergiants.** Cool (3,000–5,000 K) but very luminous ($10^2$–$10^5 L_\odot$). By Stefan-Boltzmann, this combination demands enormous radii. Betelgeuse, an M1 supergiant, has a radius around 700 $R_\odot$ — placed at the Sun's position, it would engulf Mars ([Joyce et al. 2020](https://iopscience.iop.org/article/10.3847/1538-4357/ab86b8)). These stars are not on the main sequence because they are no longer fusing hydrogen in their cores; they have exhausted core hydrogen and swollen.

**Lower left: white dwarfs.** Hot (10,000–30,000 K) but very faint ($10^{-3}$–$10^{-4} L_\odot$). Tiny radii — roughly Earth-sized. Sirius B has a radius of about 0.008 $R_\odot$ at nearly 1 $M_\odot$, densities a million times the Sun's average. What holds them up is not thermal pressure but electron degeneracy pressure, a quantum effect with no classical analog ([Chandrasekhar, 1931](https://articles.adsabs.harvard.edu/pdf/1931ApJ....74...81C)).

The clustering is the entire reason the diagram works. If stars filled the plane uniformly, the plot would teach us nothing. They live in three specific regions, each a distinct evolutionary phase: core hydrogen burning, post-main-sequence expansion, stellar corpse. The diagram is a snapshot of a movie we cannot otherwise see.

One honest caveat. The H-R diagram tells you what a star is doing now and roughly its mass. It does not tell you how old it is or which direction it will move next. To turn the diagram into a clock requires theoretical evolutionary tracks (Chapter 22) or cluster age fitting. The plot itself just shows the population.

### Luminosity classes and what the H-R diagram reveals

Spectral class fixes temperature. The H-R diagram revealed a second observable that fixes the other axis from the spectrum alone — line width.

Maury had noticed in the 1890s that some stars showed unusually sharp, narrow absorption lines, others of the same spectral class broader ones. She added "a," "b," "c" sub-divisions ([Maury & Pickering, 1897](https://articles.adsabs.harvard.edu/pdf/1897AnHar..28....1M)). Cannon thought it was a measurement artifact and dropped it. Hertzsprung, plotting Maury's "c" stars on his diagram, found they were exactly the upper-right outliers — the giants. Maury had unwittingly discovered a luminosity diagnostic.

The mechanism is **pressure broadening**. In a dense stellar atmosphere, atoms collide frequently; each collision perturbs the energy levels slightly, smearing the otherwise sharp transition. More collisions, broader lines. A main-sequence star has high surface gravity (the Sun's is 274 m/s², 28 times Earth's), high photospheric pressure, broad lines. A giant has the same composition spread over a much larger volume; surface gravity is hundreds of times lower, collisions rare, lines sharp. A K0V star and a K0III star have nearly identical line *positions* — same temperature, same transitions — but differ in line *width* by an unmistakable amount. From a single spectrum at sufficient resolution, you can sort a star into one of six **luminosity classes** without needing its distance:

- **Ia** luminous supergiants — **Ib** supergiants — **II** bright giants — **III** normal giants — **IV** subgiants — **V** main sequence (dwarfs)

The Sun is G2V. Betelgeuse is M1Ia. Sirius B is DA — white dwarfs get the "D" prefix because they behave so differently.

This is what makes the H-R diagram physical, not just descriptive. Two observables (spectral type, luminosity class) deliver the two physical coordinates (temperature, luminosity) from a spectrum alone. A G2V star and a G2III star look almost identical at modest resolution; the H-R diagram plus line-width discrimination shows they differ in luminosity by a factor of about 50 — in radius by a factor of about 7. A G2III is the size of Mercury's orbit. A G2V is the Sun. Two objects with apparently identical spectra are physically dissimilar by a factor of 350 in volume. Without the H-R diagram you would never have known.

---

## Worked example: classifying a star from one spectrum and one parallax

You observe a star and measure: continuous peak at $\lambda_{\text{peak}} = 580$ nm; strong Ca II H/K lines, moderate hydrogen, prominent neutral metals (Fe I, Mg I); lines notably sharp; parallax 0.025 arcsec (distance 40 pc); apparent magnitude $V = 3.5$.

**Temperature.** Wien's law: $T = (2.9 \times 10^{-3})/(580 \times 10^{-9}) = 5{,}000$ K. The line pattern is consistent with K0. Two methods, one answer.

**Absolute magnitude.** $M_V = m_V - 5\log_{10}(d/10\text{ pc}) = 3.5 - 5\log_{10}(4) = 0.49$.

**Luminosity.** With the Sun at $M_V \approx +4.83$: $\log_{10}(L/L_\odot) = (4.83 - 0.49)/2.5 = 1.74$, so $L \approx 55 L_\odot$.

**Radius.** From $L/L_\odot = (R/R_\odot)^2 (T/T_\odot)^4$:

$$\left(\frac{R}{R_\odot}\right)^2 = \frac{55}{(5000/5772)^4} = \frac{55}{0.563} \approx 98 \quad\Longrightarrow\quad R \approx 9.9 R_\odot$$

**Luminosity class.** Sharp lines plus radius $\sim 10 R_\odot$ at K0: a class III giant. Full designation: K0III. Aldebaran (K5III) has similar properties.

From one spectrum and one parallax — a few hours of telescope time — we have located the star on the H-R diagram, measured its radius to within 10%, and identified it as a post-main-sequence giant fusing helium.

---

## Common misconceptions

- **"O stars are bright because they have lots of hydrogen."** O stars are bright because they are massive. Hydrogen abundance is similar across the sequence; what differs is the rate of consumption. Mass sets core temperature, which sets fusion rate, which sets luminosity. A 30 $M_\odot$ O star burns through its hydrogen in a few million years; a 0.3 $M_\odot$ M dwarf takes trillions.
- **"Stars move along the main sequence as they age."** They do not. A main-sequence star stays at roughly the same H-R position for most of its life, then leaves the main sequence relatively quickly to reach the giant branch. The diagram is mostly populated by stars in long-lived phases; transits across the "Hertzsprung gap" are rare snapshots of a fast phase.
- **"Sharp lines mean the star rotates slowly."** Sharp lines mean low pressure broadening, which usually means low atmospheric density, which usually means a giant or supergiant. Rotation produces a separate, distinguishable line profile; modern spectrographs can usually separate the two mechanisms.
- **"A red star is fundamentally different from a blue star."** Same composition, same physics. The color difference is a temperature difference, set by mass (on the main sequence) or evolutionary phase (off it). One mechanism, expressed at different mass and age.

---

## Exercises

**Warm-up (Understand).** List the seven OBAFGKM classes in order of decreasing surface temperature. For each, name one identifying spectral feature and one specific example star.

**Application (Apply).** A star has spectral type A0V. Vega is a reasonable reference: $T \approx 9{,}600$ K, $L \approx 40 L_\odot$. (a) Use $L = 4\pi R^2 \sigma T^4$ to compute the radius in solar units. (b) Compare to the Sun's radius. (c) Without doing more arithmetic, explain why Vega looks brighter in the sky than the Sun would from the same distance, even though its radius is only modestly larger.

**Synthesis (Analyze).** Two stars have identical spectral type K2 but different luminosity classes. Star A is K2V; Star B is K2III. (a) State which has the broader spectral lines and explain the mechanism. (b) Estimate the ratio of their radii using typical H-R diagram values ($L_{\text{K2V}} \approx 0.3 L_\odot$, $L_{\text{K2III}} \approx 50 L_\odot$). (c) Both stars have nearly identical spectral line *positions*. What does this tell you about what spectral type fundamentally measures?

**Challenge (Analyze).** A newly discovered star sits at $T = 25{,}000$ K and $L = 10^{-3} L_\odot$ on the H-R diagram. (a) Compute its radius in Earth radii, given $R_\odot \approx 110 R_\oplus$. (b) State which luminosity class this object belongs to and explain why pressure broadening is *not* a useful diagnostic for it (hint: the atmosphere is qualitatively different from that of a main-sequence star). (c) Explain in one sentence why the existence of this kind of star was a discovery that forced new physics into astrophysics rather than something predicted from the main sequence alone.

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

---

## What would change my mind

The chapter rests on one structural claim: the H-R diagram has the structure it has because stellar physics is well-determined by mass and composition (the Vogt-Russell theorem), with the clusters tracing distinct evolutionary phases. A population of stars that consistently violates Stefan-Boltzmann when their radii are measured independently (interferometry, eclipsing-binary timing, asteroseismology) would force revision. Recent eclipsing-binary measurements of low-mass M dwarfs do show a persistent 5–10% radius discrepancy with stellar-evolution models ([Parsons et al. 2018](https://academic.oup.com/mnras/article/481/1/1083/5085023)). The leading explanation is magnetic inflation of the atmosphere. If the discrepancy turned out to be larger, more universal, or unexplained by atmospheric physics, the H-R diagram's clean one-parameter readout would crack, and the claim that Stefan-Boltzmann gives a tight constraint would need softening.

## Still puzzling

- *Why is the slope of the lower main sequence what it is?* The mass-luminosity relation flattens from $L \propto M^{3.5}$ at solar mass to roughly $L \propto M^{2.3}$ for M dwarfs ([Cuntz & Wang 2018](https://iopscience.iop.org/article/10.3847/2515-5172/aaaa67)). The change is understood as a transition from radiative to fully convective interiors, but the exact slope and where the transition happens are sensitive to opacity calculations we cannot fully verify in the laboratory.
- *What does the gap on the lower main sequence at M3.5 mean?* There appears to be a small but persistent "kink" in the H-R diagram around $0.35 M_\odot$, near where stellar interiors become fully convective. The structural cause is debated and the observational signature is at the edge of what current parallax precision can resolve ([Jao et al. 2018](https://iopscience.iop.org/article/10.3847/2041-8213/aab2ae)).
- *Antonia Maury's contribution.* Maury identified the dimension that would become the luminosity-class axis ten years before Hertzsprung used her classification to discover giants — and her name appears almost nowhere in the eventual naming of the diagram. The episode is a useful reminder that the priority of an idea and the priority of the right credit are not the same thing, and that recognizing a pattern in data without yet knowing what it means still counts as the discovery.

---

**Tags:** stellar classification, OBAFGKM, Hertzsprung-Russell diagram, luminosity class, main sequence, white dwarfs, red giants, Stefan-Boltzmann, Annie Jump Cannon, Antonia Maury
