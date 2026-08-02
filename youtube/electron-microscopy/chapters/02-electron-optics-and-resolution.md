# Chapter 2 — Electron Optics, Resolution, and Microscope Design


## TL;DR

- The wavelength of an electron at 30 kV is seven picometers.
- The chapter moves through Warm-up, Application, Synthesis, Challenge.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The wavelength of an electron at 30 kV is seven picometers. The best image you can make at 30 kV shows features no smaller than about a nanometer. This chapter is about why.*

---

There is a number that will bother you until you understand it. A 30 kV electron has a de Broglie wavelength of roughly 7 picometers — about one-twentieth the diameter of a hydrogen atom. Abbe's criterion says you can resolve two features separated by about half a wavelength. So in principle, an electron microscope at 30 kV ought to resolve features smaller than a single atom.

In practice, a good 30 kV SEM resolves about one nanometer on a well-prepared specimen with an experienced operator at the controls. That is not atoms. That is a hundred times worse than what the wavelength alone would allow.

Why?

The short answer is: because the lens is bad. Not bad by poor engineering — bad by fundamental physics. Every magnetic lens that has ever been built, and every magnetic lens that will ever be built unless you invoke some very clever tricks, focuses electrons imperfectly. Off-axis electrons bend more than paraxial ones. Electrons with slightly different energies focus at slightly different points. The lens isn't perfectly symmetric. And if you respond to all of this by narrowing the aperture to exclude the badly-focused electrons, you then run into diffraction — the wave nature of the electron — which smears the image in the other direction.

The interesting thing about this problem is that it is not a failure of effort. The gap between 7 picometers and 1 nanometer is not a gap that better machining or higher-quality steel will close. It is a gap that comes from the same physics that makes a round lens converge a beam at all. To understand it, you have to understand how an electron is steered by a magnetic field, and then understand why that steering is inevitably imperfect.

---

Start with the wavelength, because we need it.

Louis de Broglie argued in 1924 that a particle with momentum $p$ behaves as a wave with wavelength

$$\lambda = \frac{h}{p}$$

where $h$ is Planck's constant. This isn't a classical statement — it says that the particle *is* the wave in some sense that quantum mechanics makes precise but we don't need here. What we need is the practical consequence: an electron accelerated through a voltage $V$ picks up kinetic energy $eV$, and its momentum can be read off from that:

$$\lambda = \frac{h}{\sqrt{2 m_e e V}}.$$

Plug in the constants and you get a formula simple enough to remember:

$$\lambda \approx \frac{1.226}{\sqrt{V}} \text{ nm}, \quad V \text{ in volts.}$$

| Accelerating voltage | Electron wavelength | Theoretical resolution at α = 0.6° | Practical SEM/TEM resolution |
|---|---|---|---|
| **1 kV** | 38.8 pm (0.0388 nm) | 1.85 Å | ~5 nm (SEM, low-kV imaging) |
| **10 kV** | 12.2 pm | 0.58 Å | ~2 nm (SEM standard) |
| **100 kV** | 3.70 pm | 0.18 Å | ~2 Å (TEM, conventional) |
| **300 kV** | 1.97 pm (relativistic) | 0.094 Å | <1 Å (aberration-corrected TEM) |

*Wavelength shrinks non-linearly with voltage. Practical resolution is far worse than theoretical because spherical and chromatic aberration, not the wavelength, are the binding constraints.*

At 30,000 volts, $\sqrt{30000} \approx 173$, so $\lambda \approx 7.1 \times 10^{-3}$ nm = 7.1 pm. At 5 kV, it is about 17 pm. At 200 kV — a typical transmission electron microscope — it is closer to 2.5 pm, and there you need a relativistic correction:

$$\lambda = \frac{h}{\sqrt{2 m_e e V \left(1 + \frac{eV}{2 m_e c^2}\right)}}.$$

At 200 kV the correction factor is about 20%, which matters for accurate work. For SEM voltages, the simpler formula is fine.

The striking thing about these numbers is how small they are. Visible light has wavelengths between 400 and 700 nanometers. An electron at 30 kV is fifty thousand times shorter. The promise of the electron microscope is in that ratio.

Now. How do you focus something with a wavelength of seven picometers?

---

Not with glass. Electrons don't refract at a glass surface the way photons do. What *does* steer an electron is a magnetic field, through the Lorentz force:

$$\mathbf{F} = e(\mathbf{v} \times \mathbf{B}).$$

An electron moving along the optical axis of the microscope — call it the $z$-direction — doesn't feel much force from a field pointing along $z$. But if the field has radial and azimuthal components, and if the field is symmetric around the axis, something interesting happens. The radial component of $B$ kicks the electron into a circular orbit around the axis; the azimuthal velocity that creates in combination with the axial field component pulls the electron back toward the axis. The net result, for an electron that starts slightly off-axis, is that it spirals in toward the axis and crosses it at some point downstream. That crossing point is the focus.

![Magnetic lens cross-section. Three trajectories — paraxial, moderate, steep — cross the axis at different focal points: the geometric origin of spherical aberration.](../images/02-electron-optics-and-resolution-fig-01.png)

*Figure 1.* Magnetic lens cross-section. Three trajectories — paraxial, moderate, steep — cross the axis at different focal points: the geometric origin of spherical aberration.

The thing that makes this useful is that for electrons traveling close to the axis — *paraxial* electrons — the focal length is predictable from the field profile:

$$\frac{1}{f} \approx \frac{e^2}{8 m_e E_k} \int B_z^2(z) \, dz$$

where $B_z(z)$ is the on-axis field strength along the column and $E_k$ is the electron's kinetic energy. The integral runs over the length of the lens. This is the magnetic equivalent of the lensmaker's equation: stronger field, shorter focal length. Increase the lens current, strengthen the field, move the focal point closer to the lens. That is, physically, what the focus knob does — it changes a current.

The hardware that produces this field is an electromagnetic coil wrapped in soft iron. The iron serves as a flux-guiding structure, and where the iron has a gap — the *pole pieces*, two carefully machined iron faces with a narrow space between them — the field concentrates into the beam path. The geometry of the pole-piece gap is the dominant engineering variable for aberrations. A small gap concentrates the field more tightly, which is good for resolution. It also means the specimen has less room to maneuver, which is a practical constraint that lens designers spend careers navigating.

A real microscope column has multiple lenses. In an SEM there are typically two condenser lenses and one objective lens. The condensers form a demagnified image of the electron source — the *crossover* — and relay it toward the specimen. The objective lens is the final lens in the chain, the one that determines the probe size and hence the resolution. In a TEM the geometry is different: the objective lens is strong, immersing the specimen in its field, and a series of projector lenses below the specimen magnify the transmitted image onto a detector. But in both cases the optical logic is the same: lenses focus by bending electrons toward the axis, and the bending is produced by a controlled magnetic field.

![SEM places the specimen below the objective lens; TEM places it inside. The geometry decides how much aperture angle, working distance, and aberration the system has to live with.](../images/02-electron-optics-and-resolution-fig-02.png)

*Figure 2.* SEM places the specimen below the objective lens; TEM places it inside. The geometry decides how much aperture angle, working distance, and aberration the system has to live with.

---

Here is the problem. The formula above — the focal-length formula — is derived under the *paraxial approximation*: it assumes that the electrons are close to the axis and their angles are small. Real electrons are not perfectly paraxial. The electron gun doesn't emit a perfect pencil beam. And when electrons travel at any angle to the axis, even a small one, the lens doesn't treat them exactly as the paraxial formula predicts.

Four distinct effects follow from this, and they each deserve a name because they each demand a different response.

**Spherical aberration.** An electron traveling at a steeper angle to the axis passes through the stronger fringe field at larger radii, bends more strongly, and crosses the axis closer to the lens than a paraxial electron. Instead of all electrons converging to a point, they converge to a series of points spread along the axis, and the result at any given plane is a disk, not a point. The diameter of that disk scales as

$$d_s = \frac{1}{2} C_s \alpha^3$$

where $\alpha$ is the aperture half-angle — the angular range of electrons admitted to the lens — and $C_s$ is the *spherical aberration coefficient*, typically a few millimeters for an uncorrected SEM objective. Notice the cube: doubling the aperture angle makes the spherical aberration disk eight times bigger. This is the dominant aberration for conventional electron lenses.

**Chromatic aberration.** The electron source doesn't emit electrons all at exactly the same energy. A tungsten filament produces electrons spread over about one to three electronvolts; a cold field-emission source narrows that to 0.2–0.3 eV. The lens's focal length depends on electron energy through the kinetic energy $E_k$ in the denominator of the focal-length formula. Electrons with slightly different energies therefore focus at slightly different planes, and the blur at any given plane has diameter

$$d_c = C_c \alpha \frac{\Delta E}{E_0}$$

where $C_c$ is the chromatic aberration coefficient and $\Delta E/E_0$ is the fractional energy spread. At low operating voltages — 1 to 2 kV — $E_0$ is small, so even a modest energy spread produces large fractional blur. This is why the choice of electron gun matters much more at low kV than at high kV, and why field-emission sources dramatically outperform tungsten hairpins for low-voltage imaging.

**Astigmatism.** A perfect lens has perfect cylindrical symmetry around the optical axis. Real lenses don't. Pole pieces aren't machined to atomic perfection; the iron isn't perfectly uniform; a speck of contamination in the bore changes the field locally. The consequence is that electrons in one plane focus at a slightly different distance than electrons in a perpendicular plane. A point object produces two line foci, orthogonal to each other, at slightly different distances along the axis. Between the two focal planes the image of a point is an ellipse that rotates 90° as you change focus. You have surely seen this if you've ever defocused an electron microscope: the soft-focus image of a round particle elongates in one direction, then appears round briefly near focus, then elongates in the perpendicular direction on the other side. That rotation is astigmatism.

![Astigmatism diagnostic — the same nanoparticle through three focus settings. The 90° rotation between underfocus and overfocus is the signature.](../images/02-electron-optics-and-resolution-fig-03.png)

*Figure 3.* Astigmatism diagnostic — the same nanoparticle through three focus settings. The 90° rotation between underfocus and overfocus is the signature.

Unlike spherical and chromatic aberration, astigmatism can be corrected. An *octupole stigmator* — a ring of eight small electromagnets around the beam — applies a controlled astigmatic field that cancels the lens's intrinsic astigmatism. The stigmator needs retuning whenever you change operating voltage, aperture, or working distance, because all of those shift the electron trajectories that encounter the lens's imperfections. Forgetting to retune the stigmator after a parameter change is one of the commonest ways an experienced operator loses an afternoon.

**Diffraction.** This one runs in the opposite direction from the other three. The aperture is a physical obstacle — a thin disk with a circular hole — and electrons passing its edge diffract. The smaller the aperture, the more the wave nature of the electron smears the image into an Airy disk:

$$d_d = \frac{0.61 \lambda}{\alpha}.$$

This is Abbe's equation applied to electrons. Notice that it rewards *larger* $\alpha$: open the aperture, reduce diffraction blur. But opening the aperture makes spherical and chromatic aberration worse. The two effects oppose each other, which means there is an optimum somewhere in the middle.

![Log-log plot of blur disk diameter vs](images/02-electron-optics-and-resolution-fig-01.png)
*Figure 2.1 — Log-log plot of blur disk diameter vs*

---

Finding that optimum is the key calculation of this chapter, and it is worth doing explicitly.

The total blur (combining the dominant terms) is roughly

$$d_{\text{total}}(\alpha) \approx \sqrt{\left(\frac{1}{2} C_s \alpha^3\right)^2 + \left(\frac{0.61\lambda}{\alpha}\right)^2}.$$

Minimize this with respect to $\alpha$, take the derivative, set it to zero. The algebra gives

$$\alpha_{\text{opt}} \approx \left(\frac{1.22\,\lambda}{C_s}\right)^{1/4}$$

and at that optimal aperture angle, the minimum resolvable distance is

$$d_{\min} \approx 0.91\,(C_s\,\lambda^3)^{1/4}.$$

Read that last formula carefully. Resolution scales as $\lambda^{3/4}$, not $\lambda$. Halving the wavelength — which means going to four times the voltage — improves resolution by only $2^{3/4} \approx 1.68$, not by 2. The lever is weaker than it looks.

And resolution scales as $C_s^{1/4}$. To halve the minimum resolvable distance by reducing spherical aberration alone, you need to reduce $C_s$ by a factor of sixteen. This is extraordinarily hard with a round magnetic lens — $C_s$ is determined by the pole-piece geometry, and the geometry is constrained by the need to leave room for the specimen. The fourth-root scaling is actually the reason aberration correctors were worth building: they attack $C_s$ directly, rather than trying to squeeze more from wavelength.

Let's put numbers on this for a 100 kV TEM with $C_s = 1.0$ mm. The relativistic wavelength at 100 kV is $\lambda \approx 3.89$ pm.

$$\alpha_{\text{opt}} \approx \left(\frac{1.22 \times 3.89 \times 10^{-12}}{1.0 \times 10^{-3}}\right)^{1/4} = \left(4.75 \times 10^{-9}\right)^{1/4} \approx 8.3 \times 10^{-3} \text{ rad} \approx 0.48°.$$

$$d_{\min} \approx 0.91\,(10^{-3} \times (3.89 \times 10^{-12})^3)^{1/4} \approx 0.45 \text{ nm}.$$

Modern uncorrected TEMs at 100 kV are typically quoted at 0.2–0.3 nm point resolution. We got 0.45 nm. The gap comes partly from chromatic aberration, which we dropped, and partly from the fact that careful instrument design pushes $C_s$ below 1.0 mm. But the order of magnitude is right, and the contrast with the raw wavelength (3.89 pm) is stark: practical resolution is more than a hundred times worse than what the wavelength alone would permit.

---

There is a consequence of all this that operators encounter even without doing the calculation: *empty magnification*.

Every microscope image is displayed at some magnification — the ratio of the image size on screen to the corresponding size on the specimen. Push the magnification beyond the instrument's resolving power and you aren't discovering new detail; you are zooming into a blur. The pixels get bigger; the structure does not. The maximum useful magnification is set by the resolving power, not by the electronics. An SEM resolving 2 nm has no business being operated at a magnification that maps individual pixels to sub-nanometer specimen features. The image will look like a watercolor of a micrograph.

The test is simple: if the image looks the same at 500,000× and at 300,000×, you are above the useful magnification. Back off until structure appears that wasn't visible at lower magnification. If it never appears, either the specimen doesn't have finer structure, or the microscope is running at the edge of its capability and needs better conditions to cross it.

---

There is one more trade-off encoded in the aperture that doesn't appear in the resolution formula: depth of focus.

A small aperture means electrons from the specimen arrive at the lens within a narrow cone angle. A narrow cone angle means the beam converges and diverges slowly on either side of the focal plane. The axial range over which the image stays acceptably sharp is the *depth of focus*, and it scales inversely with aperture. Close down the aperture, extend the depth of focus.

For imaging a flat, polished specimen, depth of focus is irrelevant — everything is in the same plane. For imaging a rough fracture surface, a porous material, a particle sitting atop a substrate, depth of focus is everything. The SEM's celebrated ability to image highly three-dimensional surfaces with apparent sharpness throughout — the thing that makes SEM images look so different from light microscopy images of the same objects — comes largely from the small aperture angles used in SEM, which happen to produce exceptional depth of focus as a side effect.

![Triangle or three-axis diagram showing aperture size on](images/02-electron-optics-and-resolution-fig-02.png)
*Figure 2.2 — Triangle or three-axis diagram showing aperture size on*

This means the choice of aperture in practice involves three simultaneous considerations: resolution (wants the diffraction-spherical optimum), beam current (larger aperture admits more electrons, giving better signal-to-noise), and depth of focus (smaller aperture gives more depth). These don't all point in the same direction. The operator's judgment about which matters most for a given specimen is one of the core skills the rest of this book is trying to develop.

---

Now you can see why the graduate student at the beginning of this chapter couldn't focus their way to atomic resolution. The wavelength of 7 pm is real. The lens that produces a probe from that beam is not perfect, and cannot be. Spherical aberration, chromatic aberration, and the diffraction limit imposed by the aperture conspire to put the practical floor near 1 nm. The stigmator corrects astigmatism, but astigmatism is already the correctable one. The other aberrations are built into the round-lens geometry and can only be balanced against each other, not eliminated.

The modern escape from this constraint is aberration correction. Since the late 1990s it has become practical to add multipole lens elements — hexapoles and octupoles with specific orientations — that introduce precisely controlled aberrations of opposite sign to those of the round objective lens. The combined system achieves a $C_s$ that can be pushed below one micron, orders of magnitude smaller than an uncorrected objective. With $C_s \sim 1$ μm at 200 kV, the minimum resolution formula gives $d_{\min}$ in the range of tens of picometers — genuine sub-angstrom imaging. TEM images of individual atomic columns, now routine in aberration-corrected instruments, are a direct consequence of this.

But the design philosophy of aberration correction is one for a more advanced course. What matters here is that the problem it solves is exactly the one this chapter named: the fourth-root scaling of resolution with $C_s$ means that only a drastic intervention — not just better machining, not just higher voltage — could break through the conventional barrier. It took multipole correctors, decades of engineering, and the mathematical framework laid down by Otto Scherzer in 1936 (who also proved, in the same paper, that round magnetic lenses *must* have positive spherical aberration — which is why correction required multipoles rather than a cleverer round lens).

The gap between the wavelength and the image is not an accident. It is the physics of bending charged particles with a field that must, by its symmetry, bend them imperfectly. Understanding that gap is what makes the rest of the decisions in this book legible.

| Aberration | Physical cause | Blur diameter (approx.) | Scales with aperture | Correctable? |
|---|---|---|---|---|
| **Spherical (Cs)** | Off-axis rays focus closer than paraxial rays — the lens lacks a single focal point | $d_s = \frac{1}{2} C_s \alpha^3$ | Cubic in α — large aperture *amplifies* it | Yes — multipole correctors (Cs-corrected TEM/STEM) |
| **Chromatic (Cc)** | Energy spread in the beam → different focal lengths for different energies | $d_c = C_c \alpha (\Delta E / E)$ | Linear in α | Partially — Cc correctors exist but are rare; cold-FEG / monochromator reduces ΔE |
| **Astigmatism** | Lens fields non-rotationally symmetric (ovalized) | Direction-dependent; image elongates along one axis | Roughly linear in α | **Yes** — operator-correctable in real time using the stigmator |
| **Diffraction** | Wave nature of electrons; Airy disk at the aperture stop | $d_d = 0.61 \lambda / \alpha$ | *Inverse* — small aperture *amplifies* it | Not correctable — fundamental limit |

*Optimal aperture balances spherical (grows with α³) against diffraction (grows with 1/α). The Scherzer condition is the resulting sweet spot.*

---

**What would change my mind:** evidence that uncorrected round magnetic lenses can routinely achieve $C_s$ values below current best (~0.5 mm for production SEM objectives). This would narrow the wavelength-to-resolution gap without requiring multipole correctors. Nothing in the current literature suggests this is achievable; Scherzer's theorem sets a theoretical floor for rotationally symmetric lenses that hasn't been found to have exceptions.

**Still puzzling:** the prefactors in the optimum-aperture and minimum-resolution formulas vary across textbooks — 0.61 versus 0.91 versus 1.22, depending on what you include and how you sum the aberration disks. The scaling laws are robust. The constants depend on convention.

---

## Exercises

### Warm-up

**2.1** Compute the de Broglie wavelength of an electron at 15 kV using the non-relativistic formula. Then compute it at 120 kV using both the non-relativistic and relativistic formulas. By what percentage do they differ at 120 kV? *(Tests: wavelength calculation and when the relativistic correction matters.)*

**2.2** A student is focusing an SEM image of gold nanoparticles. At slight underfocus the particles appear elongated left-to-right; at slight overfocus they appear elongated top-to-bottom; at nominal focus they appear nearly round but still soft. What aberration is responsible, what is the diagnostic signature they observed, and what is the corrective action? *(Tests: astigmatism identification and stigmator response.)*

**2.3** Explain in one paragraph why the focus knob on a scanning electron microscope is, at a physical level, a current control rather than a mechanical adjustment. *(Tests: magnetic-lens focusing mechanism.)* Difficulty: easy.

### Application

**2.4** A 200 kV TEM has $C_s = 0.7$ mm. Compute the optimum aperture half-angle and the minimum resolvable distance. The manufacturer quotes a point resolution of 0.19 nm. Identify at least one physical contribution that the simplified formula omits and that could account for the remaining discrepancy. *(Tests: optimum aperture calculation and limits of the two-term model.)* Difficulty: medium.

**2.5** You are imaging a carbon-coated biological specimen on an SEM at 2 kV. The image is soft and you have already corrected astigmatism. List three distinct aberration-related causes that could still limit resolution at this voltage, ranked by which is most likely dominant, and give one diagnostic observation for each. *(Tests: low-kV aberration hierarchy and chromatic aberration dependence on $E_0$.)* Difficulty: medium.

**2.6** An SEM has a practical resolution of 3 nm. The monitor is 30 cm wide and displays 1024 pixels across. At what displayed magnification does each pixel correspond to exactly 3 nm on the specimen? What happens to image quality if you double that magnification, and what name applies to this regime? *(Tests: empty magnification concept and the relationship between resolving power and displayed scale.)* Difficulty: medium.

**2.7** You are imaging a fractured ceramic surface with topographic relief of roughly 50 μm. Rank the following aperture choices — 10 μm, 30 μm, 120 μm — in order of preference for this specimen, and justify each step by naming which aperture-dependent quantity you are prioritizing or sacrificing. *(Tests: depth-of-focus vs. resolution vs. beam-current trade-off.)* Difficulty: medium.

### Synthesis

**2.8** A lab is choosing between two instruments for imaging 3 nm catalyst particles on a thin carbon support at low voltage (3 kV): a tungsten-gun SEM ($\Delta E \approx 2$ eV, $C_s = 5$ mm) and a cold field-emission SEM ($\Delta E \approx 0.3$ eV, $C_s = 5$ mm). Using the chromatic blur formula, estimate the chromatic contribution to resolution for each at 3 kV with $\alpha = 5$ mrad and $C_c = 5$ mm. Explain why the gun choice matters far more at 3 kV than it would at 30 kV. *(Tests: chromatic aberration calculation and low-kV gun-choice logic.)* Difficulty: hard.

**2.9** The minimum resolution formula gives $d_{\min} \propto (C_s \lambda^3)^{1/4}$. A colleague argues that switching from 100 kV to 300 kV is a cheap way to double resolution. Use the scaling law to compute the actual improvement factor, then explain why they are wrong — and name what intervention would actually double resolution. *(Tests: $\lambda^{3/4}$ scaling, voltage lever weakness, and motivation for aberration correction.)* Difficulty: hard.

### Challenge

**2.10** Look up the $C_s$ value of an aberration-corrected TEM objective (any commercial instrument) and compare it to an uncorrected objective at the same nominal voltage. Using $d_{\min} \approx 0.91\,(C_s \lambda^3)^{1/4}$, predict the resolution improvement factor. Then find the manufacturer's quoted point resolution for both instruments and compute the actual improvement factor. If the two factors disagree, propose a physical reason — what does the formula leave out that matters more at very small $C_s$? *(Tests: aberration-correction payoff, limits of the scaling formula, and independent literature search.)* Difficulty: open-ended.
