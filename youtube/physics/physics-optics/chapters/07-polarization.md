# Chapter 7 — Polarization


## TL;DR

- The orientation of the electric field, the most distinctively wave-vector phenomenon in optics.
- The chapter moves through Learning objectives, Opening case: the LCD screen you're reading on, Core concept, Light as a transverse vector wave, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The orientation of the electric field, the most distinctively wave-vector phenomenon in optics.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Identify the three polarization types — linear, circular, elliptical — and explain how phase difference between $E_x$ and $E_y$ determines them.
2. **(Apply)** Use Malus's law $I = I_0 \cos^2\theta$ to predict the transmitted intensity through a polarizer.
3. **(Analyze)** Explain the three-polarizer "paradox" — why three crossed polarizers transmit light when two don't.
4. **(Apply)** Write Jones vectors for linear, circular, and elliptical polarization states and Jones matrices for polarizers, quarter-wave plates, and half-wave plates.
5. **(Apply)** Compute the output polarization state through a sequence of optical elements using Jones-calculus multiplication.
6. **(Apply)** Build a polarization-state visualizer that animates the $\vec{E}$ tip's path through a sequence of polarizers and wave plates.

---

## Opening case: the LCD screen you're reading on

Every pixel of every LCD screen — laptop, phone, monitor, TV — relies on polarization control. The structure: a backlight (usually white LEDs) → a polarizer that selects vertical polarization → a layer of liquid crystals that rotate polarization by a controlled angle → a second polarizer (typically horizontal). When the liquid crystals rotate the light by 90°, it gets through the second polarizer: white pixel. When the liquid crystals are switched off (a voltage applied to make them align with the field), the polarization isn't rotated: the second polarizer blocks the light, black pixel.

You're reading these words because billions of pixels' polarization states are being controlled, in real time, by electric signals running through the screen. The optics of polarization is the foundation of the display you're looking at.

This chapter is about *how* polarization works — the underlying physics that makes LCD screens, polarizing sunglasses, 3D cinema, and quantum cryptography possible.

---

## Core concept

### Light as a transverse vector wave

Light is a transverse EM wave. For a wave propagating in $+\hat{z}$, the electric field oscillates in the $xy$-plane. Two perpendicular components:
$$E_x(z, t) = E_{x0} \cos(kz - \omega t)$$
$$E_y(z, t) = E_{y0} \cos(kz - \omega t + \delta)$$

The *polarization state* is determined by:
- The amplitudes $E_{x0}, E_{y0}$
- The relative phase $\delta = $ phase of $E_y$ minus phase of $E_x$

### The three polarization types

**Linear polarization.** $\delta = 0$ (or $\pi$). The $\vec{E}$ tip oscillates along a straight line in the $xy$-plane. The line's angle from the $x$-axis is $\arctan(E_{y0}/E_{x0})$. The two perpendicular components oscillate in phase (or 180° out of phase, which gives the perpendicular line).

**Circular polarization.** $E_{x0} = E_{y0}$ and $\delta = \pm \pi/2$. The $\vec{E}$ tip traces a circle of radius $E_{x0}$. Two conventions:
- $\delta = +\pi/2$: *Left*-circular (LHC) — $\vec{E}$ rotates counter-clockwise looking toward the source.
- $\delta = -\pi/2$: *Right*-circular (RHC) — clockwise looking toward the source.

(Conventions vary across textbooks. The book commits to LHC = $\delta = +\pi/2$.)

**Elliptical polarization.** The general case. $\vec{E}$ tip traces an ellipse with axes along arbitrary directions.

Linear and circular are special cases of elliptical (a degenerate ellipse — a line or a circle).

### Unpolarized light

Light from thermal sources (Sun, light bulb) consists of many independent emitters with rapidly varying phases. Time-averaged: no preferred polarization direction. Called *unpolarized* — more precisely, *randomly polarized*.

For unpolarized light passing through an ideal polarizer, half the intensity is transmitted (the projection of any random polarization onto the polarizer's axis averages to 1/2).

### Polarizers and Malus's law

A polarizer transmits only the component of $\vec{E}$ along its *transmission axis*. For incident linearly-polarized light at angle $\theta$ to the transmission axis:
- Transmitted *amplitude*: $E_{\text{trans}} = E_0 \cos\theta$
- Transmitted *intensity*: $I_{\text{trans}} = I_0 \cos^2\theta$

This is **Malus's law**, named for Étienne-Louis Malus (1809).

For unpolarized incident light, the time-average of $\cos^2\theta$ over a random distribution of incident polarization angles is $1/2$:
$$I_{\text{after first polarizer}} = I_0 / 2$$

The first polarizer in a chain reduces unpolarized light's intensity to half regardless of orientation.

### The three-polarizer "paradox"

Two crossed polarizers (axes 90° apart): no light gets through. The first polarizer transmits the component along its axis; the second polarizer (perpendicular) blocks it.

Now insert a *third* polarizer at 45° between them. Light gets through.

**Why.** The first polarizer transmits a horizontally polarized component (intensity $I_0/2$). The middle polarizer at 45° passes the component along its 45° axis: $(I_0/2) \cos^2 45° = I_0/4$. The light emerging from the middle polarizer is now at 45°. The third polarizer (originally crossed to the first, now 45° from the middle): $(I_0/4) \cos^2 45° = I_0/8$.

Non-zero. Inserting a polarizer between crossed polarizers *adds* light, doesn't subtract.

The lesson: each polarizer re-polarizes the light along its own axis. The first polarizer's output is "memory" of the original polarization; subsequent polarizers further filter it. The three-polarizer arrangement transmits because the middle polarizer rotates the polarization in stages.

### Mechanisms producing polarization

**1. Reflection at Brewster's angle.** Light reflecting off a non-metallic surface at $\theta_B = \arctan(n_2/n_1)$ is fully $s$-polarized (perpendicular to the plane of incidence). Vertical polarizers in sunglasses block horizontally-polarized glare from horizontal surfaces (water, road).

**2. Rayleigh scattering.** Light scattered by small particles in the atmosphere is partially polarized. Looking 90° from the Sun, the sky is strongly linearly polarized. Bees and other animals use this for navigation.

**3. Birefringence.** Some crystals have different indices of refraction for two perpendicular polarizations. Calcite, quartz, and many polymers are birefringent. An unpolarized beam entering a birefringent crystal splits into two beams ("double refraction").

**4. Dichroic absorption (Polaroid).** A material with aligned absorbing molecules (Edwin Land's 1929 invention) transmits one polarization while absorbing the perpendicular. Most consumer polarizers use this.

### Wave plates (retarders)

A wave plate is a slab of birefringent material cut so the two polarization components ("fast axis" and "slow axis") travel at different speeds. The thickness is chosen to produce a specific phase shift between them.

- **Quarter-wave plate (QWP)**: $\pi/2$ phase shift. Converts linear polarization at 45° to the fast axis into circular polarization (and vice versa).
- **Half-wave plate (HWP)**: $\pi$ phase shift. Rotates linear polarization: incident at angle $\theta$ to fast axis exits at angle $-\theta$.

### Jones calculus

A clean linear-algebra formalism. Each polarization state is a *Jones vector* — a 2-component complex column vector. Each optical element is a $2 \times 2$ complex *Jones matrix*.

**Standard Jones vectors:**
- Horizontal linear: $\mathbf{H} = (1, 0)^T$
- Vertical linear: $\mathbf{V} = (0, 1)^T$
- 45° linear: $\mathbf{D} = (1/\sqrt{2})(1, 1)^T$
- Right-circular: $\mathbf{R} = (1/\sqrt{2})(1, -i)^T$
- Left-circular: $\mathbf{L} = (1/\sqrt{2})(1, i)^T$

**Standard Jones matrices:**
- Horizontal polarizer: $\mathbf{P}_H = \begin{pmatrix}1 & 0\\0 & 0\end{pmatrix}$
- Vertical polarizer: $\mathbf{P}_V = \begin{pmatrix}0 & 0\\0 & 1\end{pmatrix}$
- Polarizer at angle $\theta$: $\mathbf{P}(\theta) = \begin{pmatrix}\cos^2\theta & \sin\theta\cos\theta\\\sin\theta\cos\theta & \sin^2\theta\end{pmatrix}$
- QWP with fast axis along $\hat{x}$: $\mathbf{Q} = \begin{pmatrix}1 & 0\\0 & i\end{pmatrix}$
- HWP with fast axis along $\hat{x}$: $\mathbf{H} = \begin{pmatrix}1 & 0\\0 & -1\end{pmatrix}$
- Rotator by angle $\alpha$: $\mathbf{R}(\alpha) = \begin{pmatrix}\cos\alpha & -\sin\alpha\\\sin\alpha & \cos\alpha\end{pmatrix}$

For an element at angle $\theta$: $\mathbf{M}_\theta = \mathbf{R}(\theta) \mathbf{M} \mathbf{R}(-\theta)$.

**Train of elements:** matrices multiply in *reverse order* (the *last* element acts first if you read right-to-left):
$$\mathbf{J}_{\text{out}} = \mathbf{M}_N \mathbf{M}_{N-1} \cdots \mathbf{M}_2 \mathbf{M}_1 \mathbf{J}_{\text{in}}$$

Output intensity: $|\mathbf{J}_{\text{out}}|^2$.

---

## Worked example: linear to circular via quarter-wave plate

Linear polarization at 45° passes through a QWP with fast axis along $\hat{x}$. Compute the output.

**Setup.** Input Jones vector: $\mathbf{D} = (1/\sqrt{2})(1, 1)^T$. QWP matrix with fast axis along $\hat{x}$: $\mathbf{Q} = \text{diag}(1, i)$.

**Apply:**
$$\mathbf{J}_{\text{out}} = \mathbf{Q} \cdot \mathbf{D} = \begin{pmatrix}1 & 0\\0 & i\end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}$$

This is the LHC Jones vector — left-circular polarization.

**Check.** $|J_{\text{out}}|^2 = (1/\sqrt{2})^2 [1^2 + |i|^2] = 1/2 \cdot 2 = 1$. Intensity preserved.

**The lesson.** A QWP at 45° to incident linear polarization converts it to circular. Reversed: an LHC beam passing through the same QWP comes out as linear at 45°.

**The limit.** This works at one specific wavelength — the wavelength the QWP was designed for. At other wavelengths the phase shift isn't exactly $\pi/2$ and the output is elliptical, not pure circular.

---

## Common misconceptions

**"Unpolarized light has no defined polarization at any instant."** It has a rapidly and randomly varying polarization at any instant. The *time-average* over many cycles has no preferred direction. The polarization at any single instant exists but changes too fast for ordinary measurement.

**"Circular polarization is the wave spinning."** The $\vec{E}$ vector tip *traces a circle* at each fixed point in space as time advances. It's not the wave rotating around its propagation axis; it's the field oscillation direction rotating.

**"Crossing polarizers always blocks light."** A *single* crossed pair blocks. *Three* in the right configuration (0°, 45°, 90°) lets some light through. The "filter and re-orient" effect of each polarizer is the resolution.

**"The polarizer is selecting from existing waves."** More precisely, the polarizer is filtering the $\vec{E}$ field by projecting it onto the transmission axis. Quantum-mechanically: a polarizer is a measurement of polarization in the basis aligned with its axis. For classical light, the result is what Malus's law says.

**"Brewster's angle is where reflection is maximum."** It's where reflection of the p-polarized component is *zero*; the s-component is partially reflected. The reflected light at Brewster's angle is *fully* polarized (only s-component), but it's not particularly intense.

---

## Exercises

**Warm-up (Apply).** Unpolarized light of intensity $I_0$ passes through a horizontal polarizer, then a vertical polarizer. Final intensity? Now insert a 45° polarizer between them. Final intensity?

**Apply.** Linearly polarized light at 30° from vertical passes through a vertical polarizer. (a) What fraction of intensity is transmitted? (b) After a second polarizer at 90° from the first (i.e., horizontal): what fraction now?

**Apply (Jones).** Write the Jones matrix for a polarizer with transmission axis at 30° from $\hat{x}$. Apply it to a horizontally polarized input. What is the output Jones vector and intensity?

**Apply (QWP).** A QWP with fast axis along $\hat{x}$ is followed by a vertical polarizer. The input is right-circular polarization. What is the output intensity?

**Analyze (three-polarizer).** Construct a system: polarizer at 0°, then at angle $\theta$, then at 90°. Find the value of $\theta$ that maximizes the final intensity. (Answer: 45°. Maximum transmitted intensity: $I_0/8$.)

**Challenge.** A *quarter-wave plate* converts vertical linear polarization to right-circular polarization for a specific orientation. Find the angle the QWP's fast axis must make with the vertical. (Hint: write linear vertical as a superposition of two equal-amplitude components in the QWP's eigenbasis; the QWP shifts the phase between them.)

---

## LLM Exercises

### Build the polarization visualizer (`07-polarization.html`)

> **Show.** Polarization is the direction of $\vec{E}$ in a transverse wave. Linear: phase $\delta = 0$. Circular: equal amplitudes, $\delta = \pm \pi/2$. Elliptical: general case.
>
> **Say.** Build an interactive Jones-calculus polarization simulator.
>
> **Constrain.** D3 v7. Input polarization controls: sliders for $E_x$ amplitude, $E_y$ amplitude, and phase difference $\delta$. Or radio buttons for standard inputs (H, V, R, L, 45°). Optical-element sequence: drag-and-drop polarizers, QWPs, HWPs onto an optical path (each with its own angle). Compute output Jones vector via Jones-matrix multiplication. Display: input polarization ellipse animated; final-output ellipse animated; intensity bar (relative to input). Filename: `07-polarization.html`.
>
> **Verify.** (a) Linear at 0° → polarizer at 90°: transmitted intensity = 0 (Malus's law with $\theta = 90°$). (b) Linear at 0° → polarizer at 45° → polarizer at 90°: transmitted intensity = $I_0 / 4$ (three-polarizer result with first two; full chain is $I_0/8$). (c) Linear at 45° → QWP at 0° → output is circular.

### Exploration

- Linear at 0° → QWP at 45°: what is the output? (Answer: left-circular.) Reverse the QWP angle to -45°: now right-circular.
- Verify the three-polarizer arrangement: 0°, 45°, 90°. Predict $I/I_0 = 1/8$ analytically; verify.
- Set up a "polarization scrambler": linear input, HWP at random angle, output is linear at angle reflected from the HWP axis.

### Extension prompt (chapter bridge)

> **Show.** I've built the wave optics. Now I want to integrate lenses and apertures into real optical instruments and find their resolution limits.
>
> **Say.** Build a telescope-resolution simulator: two point stars at varying angular separation, viewed through a circular aperture of variable diameter.
>
> **Constrain.** Show two Airy disk patterns at the image plane, separated by the angular separation × focal length. As the angular separation drops below the Rayleigh criterion ($\theta_{\min} = 1.22 \lambda/D$), the two stars merge into one apparent blob. Sliders for $D$, $\lambda$, angular separation.
>
> **Verify.** With $D = 100$ mm, $\lambda = 550$ nm: $\theta_{\min} \approx 1.4$ arcsec. Two stars 2 arcsec apart should be just resolvable; 0.5 arcsec apart should merge.

Save as `07b-telescope-preview.html`. This is the bridge to Chapter 8.

---

## What would change my mind

Polarization is a direct consequence of light being a transverse vector wave, derivable from Maxwell's equations. Every result in this chapter — Malus's law, the polarization mechanisms, Jones calculus — is well-tested. A confirmed experimental result contradicting Malus's law for ideal polarizers would force a re-derivation; none exists. The Jones-calculus formalism is mathematically exact for fully polarized light. For partially polarized light, the more general Mueller calculus (with 4×4 Stokes-vector matrices) is required; this is the calibrated extension, not a revision.

## Still puzzling

- *The choice of sign convention for circular polarization.* Different textbooks use opposite conventions for "right" vs. "left." There's no physical preference — just a choice that must be stated clearly and used consistently.
- *Quantum polarization.* For single photons, polarization is a two-level quantum-mechanical system. Jones calculus over classical states is the high-photon-count limit of quantum-mechanical state manipulation. The deep connection: a photon's polarization is a *qubit*. BB84 quantum cryptography (Chapter 10) is polarization-encoded quantum information.
- *Birefringence and the speed-of-light direction-dependence.* In some crystals, the speed of light depends on its polarization direction. The classical wave equation still holds; the dispersion relation just becomes anisotropic. Crystal-optics analysis goes beyond intro scope.

---

**Tags:** transverse wave, linear polarization, circular polarization, elliptical polarization, Malus's law, Brewster's angle, Jones calculus, wave plate, birefringence, LCD

![Three side-by-side panels showing the E-field tip trajectory in the plane perpendicular to propagation. Linear: E-x and E-y in phase, the tip oscillates along a straight line. Circular: equal amplitudes with quarter-c...](images/07-polarization-fig-01.png)
*Figure 7.1 — Polarization States*

![Two rows comparing polarizer configurations. Top: unpolarized light through a vertical polarizer then a horizontal polarizer — completely blocked. Bottom: same crossed polarizers but with a 45-degree polarizer inserte...](images/07-polarization-fig-02.png)
*Figure 7.2 — Three-Polarizer Paradox*

![A quarter-wave plate has a fast axis along x and a slow axis along y. Incident linear polarization at 45 degrees to the fast axis can be decomposed into equal x and y components, in phase. The QWP delays the y compone...](images/07-polarization-fig-03.png)
*Figure 7.3 — Quarter-Wave Plate*

![Two stacked pixel diagrams, off and on. In both, light from a backlight passes through a vertical polarizer, a liquid-crystal layer, and a horizontal polarizer. Off state, no voltage: the liquid crystals form a 90-deg...](images/07-polarization-fig-04.png)
*Figure 7.4 — LCD Pixel*

