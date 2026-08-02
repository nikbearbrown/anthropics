# Chapter 27 — Wave Optics

*What happens when the apparatus is smaller than the wavelength.*

---

In November 1803, Thomas Young stood before the Royal Society in London and presented a result that, for any careful observer, settled a century of argument about the nature of light.

He had taken sunlight, passed it through a single pinhole (to create a spatially coherent source), and then through two more pinholes spaced a fraction of a millimeter apart. On the wall behind: not two bright spots, not one fuzzy blotch, but a series of alternating bright and dark *stripes* — a pattern of regularly spaced bands across the screen.

He knew immediately what it meant. Particles can pile up; they cannot subtract. If light were corpuscles — Newton's position, and the dominant view — two pinholes should produce at most some overlap of two blobs. Nothing about two streams of particles predicts cancellation. But waves cancel. Waves from the two pinholes, arriving at certain angles in phase, add to give bright bands. Arriving out of phase, they give darkness. Young measured the stripe spacing, computed the wavelength of the light, and got numbers in the hundreds of nanometers. He was right. Newton was wrong. Light is a wave.

The story wasn't over — Maxwell revealed that light was an electromagnetic wave, and then quantum mechanics revealed that the question "wave or particle?" was wrong from the start. But Young's experiment is still the cleanest demonstration in all of physics that light has wave character. This chapter is about the phenomena that arise when that wave character takes over.

---

## What happens at two slits

Start with Huygens's principle: every point on a wavefront is itself a source of secondary wavelets that expand outward at the wave's speed. The new wavefront is the envelope of all the wavelets. From this single rule you can derive the laws of reflection and refraction, and the entire theory of interference and diffraction.

Apply it to a plane wave hitting a barrier with two narrow slits. Each slit, admitting the wave, becomes a source of outgoing spherical wavelets. The wavelets from the two slits expand and overlap. At any point in the space behind the barrier, the total field is the *sum* of the two contributions — and that sum depends on whether they arrive in phase (constructive) or out of phase (destructive).

Consider a point on a distant screen at angle $\theta$ from the axis. The wave from slit 1 has traveled some distance $r_1$; from slit 2, $r_2$. If the slits are separated by distance $d$, and the screen is far enough that the paths are nearly parallel (Fraunhofer geometry), the path difference is $d\sin\theta$.

- If $d\sin\theta = m\lambda$ for integer $m$: waves arrive in phase. Bright fringe (constructive).
- If $d\sin\theta = (m + \tfrac{1}{2})\lambda$: waves arrive half a wavelength apart. Destructive cancellation. Dark fringe.

The bright-fringe condition:

$$d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2, \ldots$$

The $m = 0$ fringe at the center is always bright (path difference zero, phases identical regardless of wavelength). The $m = \pm 1$ fringes appear symmetrically on either side. The pattern repeats indefinitely.

![Sunlight through a pinhole illuminates two slits separated by d. Waves emerging from each slit overlap on a screen distance L away, producing alternating bright (constructive) and dark (destructive) fringes. d sin θ = mλ for...](../images/27-wave-optics-fig-01.png)
*Figure 27.1 — Young's Double-Slit (1803) — Light Is a Wave*

**A worked calculation.** Red laser light at $\lambda = 633\text{ nm}$, slits separated by $d = 0.10\text{ mm}$, screen at $L = 2.00\text{ m}$. For small angles, $\sin\theta \approx y/L$, so the bright fringe positions are $y_m = m\lambda L/d$. Spacing between adjacent fringes:

$$\Delta y = \frac{\lambda L}{d} = \frac{(633\times10^{-9})(2.00)}{0.10\times10^{-3}} = 1.27\text{ cm.}$$

About a centimeter between fringes — easily visible and measurable. From this one measurement you can work backward to get the wavelength. This is how Young extracted wavelengths from sunlight in 1803.

<!-- → [FIGURE: Double-slit geometry. Two slits separated by distance d. Wavefronts expanding from each slit as circular arcs. Screen at distance L. Path difference d sinθ labeled to a point at angle θ on the screen. Bright fringe (solid arc) where d sinθ = mλ, dark fringe (dashed arc) where d sinθ = (m+½)λ. Caption: The path difference d sinθ determines whether waves from the two slits reinforce or cancel at each point on the screen. The interference pattern is a direct consequence of wave superposition.] -->

<!-- → [FIGURE: Simulated double-slit intensity pattern on a screen. Horizontal axis: position y on screen. Vertical axis: intensity I. Pattern shows evenly spaced bright peaks (at y = mλL/d) separated by dark minima. Central peak (m=0) labeled, first-order peaks (m=±1) labeled. Fringe spacing Δy = λL/d marked with bracket. Caption: The predicted intensity pattern on the screen for λ = 633 nm, d = 0.10 mm, L = 2.00 m. Fringe spacing Δy ≈ 1.27 cm. Each bright fringe corresponds to a path difference of exactly mλ from the two slits.] -->

When light enters a medium with index $n$, its frequency is unchanged but its wavelength shrinks: $\lambda_n = \lambda/n$. The interference conditions are governed by the wavelength *in the medium*, not in vacuum. This matters for thin-film calculations.

![Light incident on a grating with N parallel slits (e.g., 600 lines/mm). Sharp bright maxima at d sin θ = mλ. Different wavelengths diffract to different angles — basis of modern spectroscopy. Inset shows solar spectrum...](../images/27-wave-optics-fig-04.png)
*Figure 27.4 — Diffraction Grating — Many Slits, Sharp Maxima, Color Separation*

**From two slits to many.** A diffraction grating is simply many slits — hundreds or thousands, evenly spaced. The same condition $d\sin\theta = m\lambda$ gives the bright maxima, but now each maximum is the constructive interference of many slits simultaneously. With $N$ slits, the maxima are $N$ times as bright and $N$ times as narrow. A thousand-slit grating produces maxima a thousand times sharper than a two-slit pattern — sharp enough to distinguish wavelengths separated by a fraction of a nanometer. This is spectroscopy: disperse white light through a grating, measure where each wavelength lands, and you know the spectrum. A CD's surface reflects the same rainbow for the same reason.

---

## The resolution limit

Even a single aperture — one slit, one lens, one mirror — diffracts. When light passes through a single slit of width $D$, it doesn't cast a sharp shadow; it spreads into a pattern of bright and dark bands, with a wide bright central maximum flanked by dimmer secondary maxima. The first minima occur where waves from opposite edges of the slit cancel pairwise:

$$D\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \ldots \quad \text{(minima).}$$

The first minimum at $\sin\theta_1 = \lambda/D$ sets the half-width of the central maximum. For $D \gg \lambda$ this angle is tiny — the shadow looks sharp as geometric optics predicts. For $D \sim \lambda$, the central maximum spreads over a large angle and the wave nature is unmistakable.

For a *circular* aperture — a lens, a telescope mirror, the pupil of an eye — the geometry produces a factor of 1.22 from the circular symmetry:

$$\theta_\text{min} = 1.22\frac{\lambda}{D}.$$

![Two panels. Single-slit intensity pattern: central bright max, first dark fringe at a sin θ = λ, side lobes diminishing. Rayleigh criterion: two point sources resolved when central peak of one falls on first dark fringe of the...](../images/27-wave-optics-fig-02.png)
*Figure 27.2 — Single-Slit Diffraction and Rayleigh's Resolution Limit*

This is the angular position of the first dark ring in the diffraction pattern from a circular aperture. It is also the **Rayleigh criterion**: two point sources are *just resolved* when the central maximum of one falls on the first minimum of the other. Closer than this angular separation, and they blur into a single smeared blob.

This is a fundamental limit. Not an engineering limit. Not a limit that better grinding of lenses can overcome. Any wave-based instrument using a circular aperture of diameter $D$ at wavelength $\lambda$ cannot resolve structure finer than the angle $1.22\lambda/D$. The physics imposes it.

**A few applications:**

The human eye, pupil diameter $D \approx 2.5\text{ mm}$, $\lambda = 550\text{ nm}$:

$$\theta_\text{min} = 1.22\frac{550\times10^{-9}}{2.5\times10^{-3}} \approx 2.7\times10^{-4}\text{ rad} \approx 0.92\text{ arcmin.}$$

The Snellen 20/20 eye-chart line is designed so that letter strokes subtend exactly 1 arcminute — right at the diffraction limit of a normal pupil. Good vision is diffraction-limited vision.

Hubble Space Telescope, $D = 2.4\text{ m}$, $\lambda = 550\text{ nm}$:

$$\theta_\text{min} = 1.22\frac{550\times10^{-9}}{2.4} \approx 2.8\times10^{-7}\text{ rad} \approx 0.058\text{ arcsec.}$$

The Arecibo radio telescope (305 m diameter, $\lambda = 21\text{ cm}$, the hydrogen line):

$$\theta_\text{min} = 1.22\frac{0.21}{305} \approx 8.4\times10^{-4}\text{ rad} \approx 3\text{ arcmin.}$$

Hubble resolves $\sim$0.06 arcseconds. Arecibo could resolve only 3 arcminutes — fifty times coarser — despite being 127 times bigger in diameter, because the radio wavelength is 380,000 times longer than visible light. The relevant number is always $\lambda/D$, not $D$ alone.

<!-- → [FIGURE: Two-panel comparison. Left: Two point sources separated by exactly θ_min — their diffraction disks shown overlapping, central maximum of one on first minimum of other. Right: Two sources separated by 0.5 θ_min — diffraction disks merged into one peak, unresolvable. Caption: The Rayleigh criterion. When the angular separation equals 1.22λ/D, the two sources are just distinguishable. Closer together, they merge. This limit applies to every optical instrument — microscope, telescope, eye, camera.] -->

<!-- → [TABLE: Diffraction limits for real instruments. Columns: instrument, aperture D, wavelength λ, θ_min (radians), θ_min (arcsec). Rows: Human eye in daylight (3 mm, 550 nm, 2.2×10⁻⁴ rad, 46 arcsec), Human eye in dim light (7 mm, 550 nm, 9.6×10⁻⁵ rad, 20 arcsec), Hubble Space Telescope (2.4 m, 550 nm, 2.8×10⁻⁷ rad, 0.058 arcsec), James Webb Space Telescope (6.5 m, 2 μm, 3.8×10⁻⁷ rad, 0.08 arcsec), Arecibo radio (305 m, 21 cm, 8.4×10⁻⁴ rad, 174 arcsec). Caption: Diffraction limits across instruments spanning five orders of magnitude in aperture and six orders in wavelength. The relevant figure is always λ/D — Arecibo is far larger than Hubble but far coarser in resolution.] -->

The implication for astronomy: every generation of telescopes has been a story of pushing $\lambda/D$ toward smaller values — either by increasing $D$ (the Extremely Large Telescope, 39 m, under construction) or by moving to shorter wavelengths (UV telescopes, X-ray telescopes), or by combining separated dishes to achieve $D$ equivalent to their spacing (the Very Long Baseline Array, which achieves Earth-spanning $D$ at radio wavelengths).

---

## Polarization

![Unpolarized light (E in random orientations) hits a linear polarizer; only the component along the polarizer axis transmits. A second polarizer at angle θ transmits an intensity I = I₀ cos² θ (Malus's law). Crossed polarizers...](../images/27-wave-optics-fig-05.png)
*Figure 27.5 — Polarization — Linear Polarizer Selects an Axis, Malus's Law Trims by cos²θ*

Electromagnetic waves are transverse: the electric field oscillates perpendicular to the direction of propagation. For unpolarized light (sunlight, incandescent bulbs), the direction of oscillation is random — all orientations perpendicular to the beam are equally represented. A polarizing filter selects one orientation and transmits only the component of $\vec{E}$ aligned with its transmission axis, blocking the perpendicular component. Unpolarized light through a polarizer emerges with half the original intensity and a definite polarization direction.

Once polarized, what happens at a second polarizer whose transmission axis is at angle $\theta$ to the first? The transmitted amplitude is $E_0\cos\theta$ (only the projection along the second axis passes). Intensity is proportional to amplitude squared:

$$I = I_0\cos^2\theta.$$

**Malus's law.** Polarizers aligned ($\theta = 0$): full intensity passes. Crossed ($\theta = 90°$): nothing passes. Rotated $45°$: half intensity. This is easy to verify with two pairs of polarized sunglasses.

Light can become polarized by reflection as well as by a filter. When light strikes a non-metallic surface (glass, water) at a specific angle — **Brewster's angle** — the reflected light is completely polarized parallel to the surface. The condition is $\tan\theta_B = n_2/n_1$; for water ($n = 1.33$) in air, $\theta_B \approx 53°$. Sunlight reflecting from a horizontal water surface at angles near 53° is almost entirely horizontally polarized. Polarized sunglasses with vertical transmission axes block this glare while passing the overhead-coming vertically polarized light relatively freely. Fly fishers, photographers, and drivers all benefit from Brewster's physics without knowing his name.

Skylight is also polarized: Rayleigh scattering (Chapter 24) produces partly polarized light, with the maximum polarization in the direction 90° from the sun. Some insects and birds use this polarization pattern as a navigation compass when the sun is hidden by clouds.

<!-- → [FIGURE: Malus's law diagram. Polarizer 1 with transmission axis vertical. Polarizer 2 at angle θ to first. Unpolarized beam enters polarizer 1 (intensity I₀), emerges polarized at intensity I₀/2. Passes polarizer 2, emerges at I = (I₀/2)cos²θ. Three cases shown: θ=0° (full transmission), θ=45° (half), θ=90° (zero). Caption: Malus's law. Two polarizers parallel transmit half the incident unpolarized intensity; at 90° they transmit nothing. The cos²θ dependence applies to any pair of linear polarizers.] -->

<!-- → [FIGURE: Brewster's angle diagram. Unpolarized light incident on water surface at angle θ_B ≈ 53°. Reflected beam shown with horizontal polarization only (vertical component absent — labeled "s-polarization blocked"). Refracted beam shown entering water, partially polarized vertically. Inset showing the perpendicular condition: reflected and refracted rays at 90° to each other at Brewster's angle. Caption: At Brewster's angle, the reflected beam is completely horizontally polarized. Polarized sunglasses with vertical transmission axes block this reflected glare. The condition tan θ_B = n₂/n₁ gives θ_B ≈ 53° for water (n = 1.33) in air.] -->

---

## Thin-film interference

Look at a soap bubble in sunlight. The film of soap is colorless — no pigment, no dye. Yet you see a swirling pattern of red, green, blue, and yellow that changes as the bubble thins and evaporates. The colors come from interference between light reflected off the bubble's two surfaces.

Light hitting the soap film reflects partly from the outer surface (air-to-soap, going into a denser medium — this reflection picks up a $180°$ phase shift, equivalent to a path addition of $\lambda/2$) and partly from the inner surface (soap-to-air, going into a less-dense medium — no phase shift). These two reflected beams have traveled different distances and have different phase histories. Their sum — constructive or destructive — depends on the film thickness $t$ and the wavelength.

For near-normal incidence, the optical path difference between the two reflections is $2t$ (the light traverses the film twice), but must be computed in the film medium, where wavelength is $\lambda_n = \lambda/n$. Combined with the half-wavelength phase shift at one surface, the conditions for *constructive* reflection are:

$$2nt = (m + \tfrac{1}{2})\lambda, \qquad m = 0, 1, 2, \ldots$$

![Light hits a thin film (soap bubble or anti-reflective lens coating). Partial reflection from top surface and bottom surface; the two reflected rays interfere. Constructive when 2nt = (m+½)λ — bright colors. Destructive when...](../images/27-wave-optics-fig-03.png)
*Figure 27.3 — Thin-Film Interference — Two Reflections, One Path Difference*

For very thin films ($t \to 0$), the path difference is negligible but the $\lambda/2$ phase flip makes the reflections destructive — thin soap films look dark in reflected light. As the film thickens, specific wavelengths become constructively reflected. Different thicknesses across the bubble face mean different colors are bright at different locations. As the film drains under gravity and evaporates, the thickness changes continuously, cycling through colors from the soap's crown to its equator.

The same physics makes oil slicks on wet pavement iridescent, makes peacock feather barbules produce brilliant color without pigment, and makes anti-reflection coatings on camera lenses possible. A quarter-wavelength-thick coating (with appropriate index) creates equal path-length and equal-phase-shift conditions that make both reflected beams cancel — killing the surface reflection at the design wavelength. This is why coated camera lenses often show a faint purple sheen (the green wavelength is most suppressed; red and blue remain slightly).

<!-- → [FIGURE: Thin-film diagram. Incident beam hitting soap film of thickness t. Reflected beam 1 from top surface (air to film, phase shift λ/2 labeled). Reflected beam 2 from bottom surface (film to air, no phase shift). Path difference 2nt labeled. Constructive interference condition shown as equation. Caption: Thin-film interference. Two reflected beams travel different optical path lengths and experience different phase shifts. The combination of path difference 2nt and the phase shift at the denser surface determines which wavelengths constructively reflect, producing the colors of soap bubbles and oil slicks.] -->

<!-- → [TABLE: Thin-film constructive interference thicknesses for visible colors. Columns: color, λ (nm in air), λ_n = λ/n (nm in film, n=1.33), minimum thickness t for m=0 (nm). Rows: Violet (400 nm, 301 nm, 75 nm), Blue (450 nm, 338 nm, 85 nm), Green (550 nm, 414 nm, 103 nm), Yellow (590 nm, 444 nm, 111 nm), Red (700 nm, 526 nm, 132 nm). Caption: The thinnest film producing each color in reflected light (m=0 order, one phase-reversal reflection). As a soap bubble drains from ~130 nm down to zero, colors disappear in reverse order — red last, then a final dark region as the film becomes too thin to constructively reflect anything.] -->

---

## The common thread

![Log-log plot of feature size vs wavelength. Diagonal feature = λ separates regimes: above diagonal (feature ≫ λ) geometric optics works; below diagonal (feature ~ λ or smaller) wave optics dominates. Reference points: human...](../images/27-wave-optics-fig-06.png)
*Figure 27.6 — When Geometric Optics Breaks Down — Feature Size vs Wavelength*

These three phenomena — double-slit interference, single-aperture diffraction, thin-film interference — all arise from the same thing: the need to add up wave *amplitudes with phase*, not just intensities. Geometric optics adds intensities (power per area) because, when apertures and objects are much larger than $\lambda$, phase differences wash out and only average intensities matter. Wave optics tracks phases, and when phases matter, amplitudes add — sometimes constructively, sometimes destructively.

The deepest consequence is the resolution limit. Once you accept that an aperture of diameter $D$ only admits the wavefront in a finite region, and that every finite wavefront diffracts upon truncation, you cannot escape $\theta_\text{min} = 1.22\lambda/D$. Every optical instrument, from your eye to the James Webb Space Telescope, operates under this constraint. The Webb mirror is 6.5 m across; observing at $\lambda = 2\,\mu\text{m}$:

$$\theta_\text{min} = 1.22\frac{2\times10^{-6}}{6.5} \approx 3.8\times10^{-7}\text{ rad} \approx 0.08\text{ arcsec.}$$

Same equation. A microscope examining a single cell and a space telescope examining the early universe are governed by the same $1.22\lambda/D$.

There is also something worth pausing on philosophically. Young's 1803 experiment proved light is a wave. Chapter 24 revealed the wave is electromagnetic — electric and magnetic fields propagating at $c$. This chapter has shown three consequences of that wave nature. The next chapter (quantum mechanics) will reveal that light is also, somehow, particles. And Chapter 29 will show that the same two-slit interference pattern appears when you send electrons — matter, not light — through two slits. At that point you will realize that the question Young answered — "is light a wave?" — wasn't quite the right question. The right question is "what kind of thing produces interference patterns?" And the answer turns out to be: everything.

---

## Exercises

### Warm-up

**27.1** *(LO 2)* Double slit: $\lambda = 500\text{ nm}$, $d = 0.20\text{ mm}$, screen at $L = 1.50\text{ m}$. Spacing between adjacent bright fringes?

**27.2** *(LO 3)* Single slit: width $0.10\text{ mm}$, $\lambda = 633\text{ nm}$. Angle of first minimum on each side of center?

**27.3** *(LO 4)* Telescope mirror: $D = 0.50\text{ m}$, $\lambda = 500\text{ nm}$. Diffraction-limited resolution in arcseconds?

**27.4** *(LO 5)* Two polarizing filters at $30°$ to each other. Unpolarized light of intensity $I_0$ passes through both. Final intensity?

### Application

**27.5** *(LO 2)* Diffraction grating: $5000\text{ lines/cm}$. First-order maxima for $\lambda = 700\text{ nm}$ (red) and $\lambda = 400\text{ nm}$ (violet)?

**27.6** *(LO 3, LO 4)* Eye pupil $D = 4.0\text{ mm}$ (dim light). Diffraction-limited resolution at $\lambda = 550\text{ nm}$. Compare to visual acuity of ~1 arcmin — is human vision diffraction-limited or photoreceptor-limited?

**27.7** *(LO 5)* Anti-reflection coating ($n_\text{coat} = 1.38$) on glass ($n_\text{glass} = 1.50$), designed for $\lambda = 550\text{ nm}$. Required coating thickness?

**27.8** *(LO 4)* Hubble ($D = 2.4\text{ m}$) at $\lambda = 500\text{ nm}$ has resolution ~$0.05\text{ arcsec}$. At the Andromeda distance (~$2.5\times10^6\text{ ly}$), what physical separation does this correspond to? What aperture would resolve a Sun-radius structure in Andromeda?

### Synthesis

**27.9** *(LO 2, LO 4)* Bird eye: pupil $D = 4\text{ mm}$, retina distance $\sim 7\text{ mm}$. (a) Diffraction-limited resolution at $\lambda = 550\text{ nm}$. (b) Angular size of one ~$2\,\mu\text{m}$ cone photoreceptor as seen from the lens. (c) Is bird vision optics-limited or photoreceptor-limited?

**27.10** *(LO 5)* Soap bubble ($n = 1.33$). Estimate the film thicknesses producing constructive interference at red ($\lambda = 700\text{ nm}$), green ($550\text{ nm}$), and blue ($450\text{ nm}$) in reflected light.

**27.11** *(LO 1, LO 2)* Two pinholes replace two slits. Using Huygens, explain why the pattern on a far screen is the same. Then: what changes if the source is polychromatic (white light) rather than monochromatic?

### Challenge

**27.12** *(beyond chapter)* The Very Large Array: 27 antennas with maximum baseline $36\text{ km}$, operating at $\lambda = 21\text{ cm}$. (a) Effective angular resolution? (b) Compare to a single 25-m dish. (c) Why doesn't combining 27 dishes give 27× the light-gathering power of a 36-km filled aperture?

**27.13** *(beyond chapter)* (a) Standard diffraction limit for $\lambda = 488\text{ nm}$, $NA = 1.4$ microscope. (b) STED super-resolution achieves ~20 nm in practice. Why doesn't this violate the diffraction limit? Explain in your own words using the concept of encoding spatial information in molecular on/off states.

---

## LLM Exercise — Chapter 27: Wave Optics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An entry analyzing a wave-optics aspect of your anchor phenomenon — diffraction, interference, polarization, or the resolution limit of an instrument involved.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 27, I want to apply wave optics — interference, diffraction, the Rayleigh resolution limit, polarization, thin-film effects — to my phenomenon.

Please:

1. Identify ONE wave-optics aspect of my phenomenon. Examples: for a bike commute — the Rayleigh limit on my own eye's resolution (can I see a road sign from how far?), polarized sunglasses for road glare, oil-slick rainbow on a rainy street, the diffraction pattern of a streetlight through condensation on glasses. For a coffee maker — thin-film interference in the oil layer that forms on espresso ("crema" reflectivity), the iridescence of a steamed-milk surface, the diffraction pattern of light through espresso grounds. For a basketball shot — the resolution limit of my eye for tracking the ball at distance, the polarization of sky glare on the gym windows. For a marathon — sunglasses (polarization), the diffraction limit of my eye, the iridescent colors of certain athletic fabrics.

2. Compute one quantitative quantity using a chapter equation. For diffraction limit: angular resolution from pupil diameter and wavelength. For thin films: thickness corresponding to a particular color. For polarization: Malus's law for intensity through crossed polarizers.

3. Specify input numbers, sources, uncertainty.

4. Run the calculation. Report value with units and uncertainty.

5. One sanity check.

6. One sentence on how this entry connects to Chapter 28 (special relativity) — the next chapter takes light's wave nature for granted but pushes on the idea that the speed of light is the same for everyone.

Save the output as logbook/chapter-27-wave-optics.md.
```

### What this produces

A Logbook entry capturing the wave-optical limits or effects in your phenomenon — often surprising once you go looking for them.

### How to adapt this prompt

- *If the phenomenon has no wave-optics content directly:* The diffraction limit of your own eye observing the phenomenon is always available.
- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* If you photographed your phenomenon, use Claude Code to estimate the angular size of features and check whether your camera resolved them at its diffraction limit.

### Connection to previous chapters

Builds directly on Chapter 24 ($c = f\lambda$ and EM-wave structure), Chapter 25 (geometric optics regime), and Chapter 26 (eye, microscope, telescope optics).

### Preview of next chapter

Chapter 28 (special relativity) takes $c$ as a fixed constant in every reference frame — leading to time dilation, length contraction, and the impossibility of exceeding $c$.

---

**Tags:** wave-optics, double-slit, diffraction-limit, polarization, thin-film-interference
