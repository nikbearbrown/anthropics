# Chapter 1 — Light as a Wave: Review and Reframe


## TL;DR

- A fast review of light as an electromagnetic wave — speed, wavelength, frequency, spectrum — reframed for optics.
- The chapter moves through Learning objectives, Opening case: when do we need wave optics?, Core concept, Light as a transverse EM wave, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A fast review of light as an electromagnetic wave — speed, wavelength, frequency, spectrum — reframed for optics.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State light as a transverse EM wave with $\vec{E}$ and $\vec{B}$ perpendicular to propagation, and identify the standard polarization options.
2. **(Apply)** Use $c = f\lambda$ and $E_{\text{photon}} = hc/\lambda$ to compute photon energies for any wavelength in the visible spectrum.
3. **(Apply)** Compute the speed of light in any material from $v = c/n$ and use this to compute wavelength in a medium.
4. **(Analyze)** Identify whether the ray approximation is valid for a given physical setup based on the ratio $\lambda$ / (relevant geometric size).
5. **(Apply)** Build a wavelength-to-color visualizer with the corresponding photon energy displayed.

---

## Opening case: when do we need wave optics?

A laser pointer shines a red dot on the wall across the room. The dot is sharp, well-defined, traveling in a straight line from pointer to wall — the canonical demonstration of geometric optics. *Rays work here.* The wall is illuminated where the pointer's beam hits and dark where it doesn't.

Now shine the same pointer through a narrow slit — a slit of width about 0.1 mm, comparable to the laser wavelength of 633 nm. The dot on the wall is no longer sharp. There is a bright central band with dark gaps and fainter side bands extending outward. *Rays no longer work.* You need wave optics — interference, diffraction — to describe what you see.

The difference between these two cases is captured by a single ratio: $\lambda / d$, the wavelength divided by the relevant geometric size. When $\lambda / d \ll 1$, rays work and we use **geometric optics** (Chapters 2–4). When $\lambda / d$ approaches 1, wave behavior dominates and we use **wave optics** (Chapters 5–7). When the experiment involves single photons or detection events, we need **quantum optics** (Chapter 10).

This chapter is a review of light as a wave. Students from the Electromagnetism volume will move through it quickly. Students without that background get the essential foundation. The simulation is the new content — a wavelength-to-color visualizer that ties the abstract numbers to what you actually see.

---

## Core concept

### Light as a transverse EM wave

Maxwell's equations (developed in the Electromagnetism volume) predict that oscillating electric and magnetic fields self-sustain and propagate at the speed
$$c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} = 2.998 \times 10^8 \text{ m/s}$$
where $\mu_0$ and $\varepsilon_0$ are the permeability and permittivity of free space.

For a plane wave propagating in $+\hat{x}$:
$$\vec{E}(x, t) = E_0 \cos(kx - \omega t)\hat{y}$$
$$\vec{B}(x, t) = B_0 \cos(kx - \omega t)\hat{z}$$
with $E_0 = c B_0$ and $\omega/k = c$.

Three immediate consequences:
- $\vec{E}$ and $\vec{B}$ are perpendicular to each other *and* to the direction of propagation (transverse wave).
- The product $\vec{E} \times \vec{B}$ points along propagation (the Poynting vector).
- $\vec{E}$ can point in any direction in the plane perpendicular to propagation — that direction is the **polarization** (Chapter 7).

### Wavelength, frequency, and speed

$$c = f \lambda$$
- $c$ = speed of light in vacuum: $3 \times 10^8$ m/s
- $f$ = frequency in Hz
- $\lambda$ = wavelength in meters

In a medium with refractive index $n > 1$, the speed drops to $v = c/n$. The frequency stays fixed (frequency is set by the source); the wavelength inside the medium is $\lambda_{\text{med}} = \lambda_0 / n$.

This is why colors don't change when light enters water or glass: $f$ is fixed, and color is determined by $f$.

### The electromagnetic spectrum

All EM waves obey the same wave equation. They differ only in frequency.

| Region | Frequency | Wavelength | Photon energy | Sources/uses |
|---|---|---|---|---|
| Radio | < 10⁹ Hz | > 30 cm | < 4 µeV | FM, AM, mobile |
| Microwave | 10⁹–10¹² Hz | 30 cm – 0.3 mm | 4 µeV – 4 meV | WiFi, ovens, radar |
| Infrared | 10¹²–4×10¹⁴ Hz | 0.3 mm – 700 nm | 4 meV – 1.7 eV | Heat, fiber optics |
| **Visible** | 4×10¹⁴–8×10¹⁴ Hz | **700–400 nm** | **1.7–3.1 eV** | Sight, photosynthesis |
| Ultraviolet | 8×10¹⁴–10¹⁶ Hz | 400–10 nm | 3.1–124 eV | Sunburn, sterilization |
| X-ray | 10¹⁶–10¹⁹ Hz | 10 nm – 0.01 nm | 124 eV – 124 keV | Medical imaging |
| Gamma | > 10¹⁹ Hz | < 0.01 nm | > 124 keV | Nuclear physics |

The visible spectrum spans about an octave of frequency (a factor of 2). The full EM spectrum spans 24 orders of magnitude. Visible light is a remarkably narrow slice.

### Photon energy: a preview

Light delivers energy in quanta (photons). The energy of one photon of frequency $f$ (wavelength $\lambda$) is
$$E_{\text{photon}} = hf = \frac{hc}{\lambda}$$
where $h = 6.626 \times 10^{-34}$ J·s is Planck's constant.

A useful shortcut: $hc = 1240$ eV·nm. So a 500 nm green photon carries $1240/500 = 2.48$ eV.

The photon picture is a preview here — Chapter 10 develops it. For Chapters 1–9, the wave picture is the operating description.

### Index of refraction

The refractive index $n$ of a material is the ratio of the speed of light in vacuum to the speed in the material:
$$n = c/v$$

For visible light: air n ≈ 1.0003, water n = 1.33, ordinary glass n ≈ 1.5, diamond n = 2.42, gallium phosphide n ≈ 3.4 (some semiconductors are very high).

Index depends slightly on wavelength: $n(\lambda)$. Blue light travels slower than red in glass (n_blue > n_red), so blue refracts more than red. This is *dispersion*, the physics behind a prism rainbow. Cauchy's empirical fit: $n(\lambda) \approx A + B/\lambda^2$.

### Intensity

The intensity $I$ of an EM wave is the time-averaged power per unit area:
$$I = \frac{P}{A} = \frac{1}{2} c \varepsilon_0 E_0^2$$
Units: W/m². For sunlight at Earth's surface: $I \approx 1000$ W/m² (solar constant).

Intensity is what your eye and a photometer respond to. It scales as the square of the electric-field amplitude.

### The ray approximation

When the wavelength is much smaller than every relevant length scale (slit width, lens radius, aperture diameter), light behaves *ray-like*. This is the regime of Chapters 2–4. The wavelength becomes invisible in the math; only geometry matters.

When the wavelength approaches relevant length scales — slits of a fraction of a millimeter, gratings with sub-micron spacing, apertures comparable to $\lambda$ — wave behavior dominates and the ray picture breaks. That's Chapters 5–7.

The dividing line is fuzzy, but a useful operational test: $\lambda < d/100$ → ray optics suffices. $\lambda \sim d$ → wave optics required. $d/10 < \lambda < d$ → both pictures contribute; the answer typically requires both.

---

## Worked example: green light in a glass slab

A green photon ($\lambda_0 = 550$ nm in vacuum) enters a glass slab of index $n = 1.52$. Find: (a) frequency in vacuum, (b) wavelength in the glass, (c) photon energy.

**(a) Frequency.** $f = c/\lambda_0 = (3 \times 10^8)/(550 \times 10^{-9}) = 5.45 \times 10^{14}$ Hz. About 545 THz.

**(b) Wavelength in glass.** Frequency stays the same; speed drops to $c/n$. So $\lambda_{\text{glass}} = \lambda_0 / n = 550/1.52 = 362$ nm. Shorter inside.

**(c) Photon energy.** $E = hc/\lambda_0 = 1240 / 550 = 2.25$ eV. The photon energy is set by the *vacuum* wavelength (equivalently the frequency); it doesn't change in the material because frequency doesn't change.

**The lesson.** Frequency is the invariant. Speed and wavelength change when entering a denser medium; frequency does not. Color = frequency.

**The limit.** This calculation assumes $n$ is the same for all visible wavelengths. In reality, n_blue > n_red — and that's exactly what makes a prism split white light into colors (Chapter 2, dispersion).

---

## Common misconceptions

**"Color is a property of light."** Color is the *brain's response* to a particular range of frequency. Physics has frequency and wavelength; perception has color. Two different physical situations can produce the same perceived color (different spectral compositions averaging to the same response).

**"Light slows down in glass because it bumps into atoms."** The classical picture is that the wave's $\vec{E}$ field induces oscillating dipoles in atoms that re-radiate slightly out of phase with the original wave; the superposition propagates slower. The simplified "bumping" picture is misleading. The energy and frequency are preserved; the speed is what changes.

**"Photons exist only in light." or "Photons are what light *really* is."** Both are wrong. Photons are the quantum-mechanical excitations of the EM field. Classical wave optics is the high-photon-number (coherent-state) limit. Chapter 10 develops this; for now, the wave picture suffices.

**"The visible spectrum is a wide band of frequencies."** It's an octave — about 4 × 10¹⁴ to 8 × 10¹⁴ Hz. Radio waves span trillions of times more frequency. Visible light is a narrow slice the eye evolved to detect because that's where the Sun's emission peaks and water is transparent to it.

---

## Exercises

**Warm-up (Apply).** Compute the frequency and photon energy for light of wavelength 400 nm (violet), 550 nm (green), and 700 nm (red). Photon energies in eV.

**Apply.** A laser pointer emits 1 mW at 633 nm. (a) How many photons per second does it emit? (b) If the beam diameter is 2 mm, what is the intensity?

**Apply.** A signal at frequency 2.4 GHz (WiFi). Find the wavelength. Is this in the radio, microwave, or other region of the spectrum?

**Apply + Analyze.** A ray of light enters water from air at the surface. Inside the water: (a) what happens to the frequency? (b) what happens to the wavelength? (c) what happens to the speed? (d) what happens to the photon energy?

**Apply.** For each setup below, decide whether ray optics, wave optics, or both are needed:
- (a) Sunlight illuminating a 10 cm-wide window.
- (b) Sunlight passing through a 0.2 mm slit.
- (c) Sunlight reflecting off a CD (the colors you see are interference).
- (d) X-rays (λ = 0.1 nm) through a 1 mm aperture.

**Challenge.** A photon of green light is absorbed by an isolated atom, exciting an electron to a higher energy level. The atom later emits a photon of slightly longer wavelength (lower energy) due to vibrational losses ("Stokes shift" in fluorescence). Why must the emitted photon be lower in energy than the absorbed? What conservation law applies here?

---

## LLM Exercises

### Build the wavelength-to-color visualizer (`01-em-wave-review.html`)

> **Show.** Light is a transverse EM wave. $c = f\lambda$. The visible spectrum runs from 400 nm (violet) to 700 nm (red).
>
> **Say.** Build a wavelength-to-color visualizer with the EM wave displayed alongside.
>
> **Constrain.** D3 v7. Slider for wavelength (200–800 nm). Display:
> - Animated transverse EM wave: $\vec{E}$ in orange (vertical oscillation), $\vec{B}$ in purple (horizontal oscillation, perpendicular).
> - The corresponding visible color as a background band. (400 nm = violet, 700 nm = red; use the standard CIE wavelength-to-RGB approximation. Outside 380–780 nm: black background, labeled "invisible.")
> - Numerical readouts: frequency $f = c/\lambda$ in THz, photon energy $E = hc/\lambda$ in eV, period $T = 1/f$.
> - A second panel: full EM spectrum bar (radio to gamma in log scale) with the current wavelength marked.
>
> Filename: `01-em-wave-review.html`.
>
> **Verify.** (a) At 550 nm (green): $f ≈ 545$ THz, $E ≈ 2.25$ eV. (b) Doubling $\lambda$ halves $f$ and halves $E$. (c) Wavelengths below ~380 nm or above ~780 nm show as "invisible."

### Exploration

- Sweep from 400 to 700 nm. Watch the color transition through the visible spectrum.
- Set to 100 nm (UV) — is this visible? What's the photon energy?
- Set to 10 µm (far-IR — typical of room-temperature blackbody emission). Energy?

### Extension prompt (chapter bridge)

> **Show.** A wave in vacuum travels at $c$. In a medium of index $n$, it travels at $c/n$.
>
> **Say.** Modify the simulator to add a "medium" — a region with adjustable $n$. Show the wave's wavelength shrinking when it enters the medium.
>
> **Constrain.** Slider for $n$ (1 to 2.5). The display should show two regions: vacuum on the left, medium on the right. The wave's frequency stays constant; its wavelength inside is $\lambda/n$.
>
> **Verify.** With $n = 1.5$ (glass), the wavelength inside should be 2/3 of the vacuum wavelength. Frequency and period unchanged.

Save as `01b-medium-preview.html`. This is the bridge to Chapter 2.

---

## What would change my mind

Light's nature as an EM wave is established at every measured scale in the regime where classical optics applies. A confirmed deviation from $c = 1/\sqrt{\mu_0\varepsilon_0}$ at any tested precision would force the rewriting of this and the next ten chapters. None exists. At the single-photon level, the wave picture is supplemented by the photon picture (Chapter 10); this is not a contradiction but a refinement at smaller scales.

## Still puzzling

- *Why is the visible spectrum exactly where it is?* Because the Sun's blackbody peak is at ~550 nm, water (the medium of life) is transparent at those wavelengths, and Earth's atmosphere is also transparent there. Multiple coincidences? Or selection effects from the conditions for life? An open question.
- *The classical wave picture and the photon picture meet in coherent states (laser light) — but they don't always agree.* The photoelectric effect (Chapter 10) requires the photon. The double-slit pattern at high intensity is the classical wave. The intermediate cases are where the deeper theory (QED) lives.
- *Color perception.* The human eye uses three cone types peaking at ~440 (S), 540 (M), and 570 nm (L). Light of any spectral composition that triggers the same response *looks the same* — metamers. Physics has spectra; color has tristimulus values. They are not the same.

---

**Tags:** electromagnetic wave, wavelength, frequency, photon, visible spectrum, index of refraction, dispersion, intensity, ray approximation

![Pseudo-3D diagram of a plane electromagnetic wave propagating in the positive x direction. The electric field E oscillates sinusoidally in orange along the vertical y axis. The magnetic field B oscillates in reddish p...](images/01-light-as-wave-fig-01.png)
*Figure 1.1 — Transverse EM Wave*

![Horizontal log-scale bar showing the electromagnetic spectrum from radio waves at 100 meters wavelength to gamma rays at 10 to the minus 13 meters. Regions are radio, microwave, infrared, visible, ultraviolet, X-ray,...](images/01-light-as-wave-fig-02.png)
*Figure 1.2 — EM Spectrum*

![Three-panel comparison of light hitting a slit at three regime ratios. Panel A: wide slit with lambda much smaller than d, ray optics suffices, sharp bright spot on wall. Panel B: slit width comparable to ten lambdas,...](images/01-light-as-wave-fig-03.png)
*Figure 1.3 — Ray vs Wave Regime*

![Plane wave propagating left to right crosses a boundary from vacuum n equals 1 on the left into glass with n equals 1.5 on the right. The sinusoidal electric field is continuous across the boundary but the wavelength...](images/01-light-as-wave-fig-04.png)
*Figure 1.4 — Light Crossing a Boundary*

