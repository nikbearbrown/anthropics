# Chapter 5 — SEM Modes of Operation


## TL;DR

- Every knob on a scanning electron microscope is an argument about physics — and the image tells you whether your argument was right.
- The chapter moves through Warm-up, Application, Synthesis, Challenge.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Every knob on a scanning electron microscope is an argument about physics — and the image tells you whether your argument was right.*

---

Here is a scene that repeats itself in electron microscopy labs around the world. A graduate student is trying to image gold nanoparticles on a thin carbon film. The image is noisy. The student raises the accelerating voltage from 5 kV to 25 kV, reasoning that higher voltage means shorter wavelength and shorter wavelength means better resolution. The graininess gets worse. A halo appears around each particle. The student cranks the spot size up for more signal. The image goes soft. Forty minutes later, the lab manager walks by, looks at the screen, and says: wrong kV, probe too big, dwell time too long. Drop to 5 kV, tighten the spot, scan fast and average frames. The student does it. The next image shows individual 5 nm particles cleanly.

What the student was doing was treating "more" as a universal optimization. More voltage, more signal, more dwell time — each change in the direction of what seemed like improvement. What the lab manager understood was that each of those knobs acts on a specific piece of physics, and the physics of a 5 nm gold nanoparticle on a thin carbon film is not the physics that rewards high voltage or a large probe.

This chapter is about learning to read that physics before the image goes wrong. When you can set reasonable starting values from first principles — and more importantly, when you can look at a bad image and identify which parameter caused it — the microscope becomes a precision instrument rather than a frustration machine.

---

Start with the most consequential choice the operator makes: accelerating voltage.

The argument for higher voltage seems airtight. Chapter 2 established that electron wavelength falls with voltage as $\lambda \approx 1.226/\sqrt{V}$ nm, and that practical resolution scales roughly as $\lambda^{3/4}$. More voltage, shorter wavelength, better resolution. The argument is correct as far as it goes. The trouble is that it stops too early.

A 30 kV electron carries thirty kiloelectronvolts of kinetic energy into the specimen. The electron doesn't stop at the surface. It penetrates, loses energy gradually through inelastic scattering events, and ultimately comes to rest inside the material. The depth and shape of this interaction volume — the region inside the specimen where the beam deposits its energy — scales roughly as $V^{1.7}$ by the Kanaya-Okayama relation that Chapter 6 will derive properly. At 30 kV, in a material of moderate density, the interaction volume extends several micrometers below the surface. At 5 kV, a few hundred nanometers. At 1 kV, a few tens of nanometers.

![Interaction volume scales steeply with accelerating voltage. At 30 kV the volume dwarfs a 5 nm surface feature; at 1–5 kV they are comparable.](../images/05-sem-modes-of-operation-fig-01.png)

*Figure 1.* Interaction volume scales steeply with accelerating voltage. At 30 kV the volume dwarfs a 5 nm surface feature; at 1–5 kV they are comparable.

Secondary electrons, the signal that forms most SEM images, escape only from the top few nanometers of the specimen regardless of what voltage the beam carries in. They are low-energy electrons knocked loose by the beam, and they cannot travel far through matter before being reabsorbed. This means that at 30 kV, the secondary electron signal comes from a surface layer of fixed depth — a few nanometers — but it is excited by a beam whose energy is being deposited across several micrometers. The bulk of the beam's interaction is invisible to the SE detector. The only thing that changes is that more energy is going into the specimen, more into the substrate below your feature of interest, and the interaction volume extends well past the boundaries of a 5 nm nanoparticle into the carbon film below and the silicon substrate below that.

Now the gold nanoparticle is not being imaged; the carbon film is being imaged with a 5 nm perturbation. The contrast is from the wrong thing. And if the specimen is an insulator, more beam energy means more charge deposited per unit time and fewer secondary electrons escaping to neutralize it. The specimen charges, the image distorts, the bright haloes appear.

The right mental model for choosing kV is this: put the interaction volume where the information lives. Surface morphology on a bulk metal — a few hundred nanometers of interesting texture — can tolerate moderate voltage, say 10–15 kV. A 5 nm nanoparticle on a thin support requires the interaction volume to be comparable to or smaller than the particle, which means 1–5 kV. A biological specimen coated with a few nanometers of platinum needs the beam to stay within the platinum rather than punching through it into the insulating tissue below, which means 2–5 kV. EDS analysis — detecting characteristic X-rays from elements in the specimen — requires the beam energy to exceed the ionization threshold for the element of interest, typically with a factor of 1.5–2 overhead, which sometimes forces you to higher voltages even at the cost of other image quality.

The kV decision, then, is not a resolution decision. It is an information-depth decision. Resolution follows from it, but resolution is not the primary axis.

| Specimen type | Feature of interest | Recommended kV range | Primary constraint |
|---|---|---|---|
| **Bulk metal surface** | Topography, grain structure | 10–20 kV | Beam-specimen interaction volume; signal-to-noise |
| **Nanoparticle on thin support** | Particle size, shape, dispersion | 5–10 kV | Penetration depth — too high penetrates substrate and washes out particle contrast |
| **Insulating polymer (Pt-coated)** | Surface morphology | 5–15 kV | Charging through the coating layer |
| **Insulating polymer (uncoated)** | Surface morphology | 1–3 kV (low-kV imaging with E-T or in-lens detector) | Charging without conductive coating |
| **Biological tissue (Pt-coated)** | Cell surface, ultrastructure | 2–5 kV | Beam damage; charging through coating |
| **EDS mapping** | Elemental composition at depth | 15–30 kV | Need overvoltage ratio of 2–3× the highest-Z element's K-edge |

---

Once kV is set, the next critical variable is working distance — the gap between the bottom of the objective lens and the specimen surface.

The reason working distance matters is subtler than it first appears. The objective lens focuses the electron probe to its smallest point at a specific plane below the lens. If the specimen sits at that plane, the probe is as small as the lens can make it: maximum resolution. But as the specimen moves farther from the lens — longer working distance — the probe has diverged by the time it reaches the specimen surface. You might think this simply means worse resolution, and at first order that is right. But there is a second effect that often matters more: as working distance increases, the aperture half-angle $\alpha$ decreases, because the same physical aperture subtends a smaller angle when it is farther from the specimen plane. And from Chapter 2, depth of focus scales as $d_0/\alpha$ — the acceptable disk diameter divided by the aperture half-angle. Smaller $\alpha$ means more depth of focus.

This is the deep logic behind a characteristic of SEM images that everyone notices but not everyone explains: SEM images of rough, three-dimensional surfaces look sharp throughout, in a way that optical microscope images never do. A fractured surface, an insect's compound eye, a porous scaffold — the whole thing is in focus simultaneously. This isn't an accident of detector sensitivity or beam geometry; it is a direct consequence of the small aperture angles used in SEM, which produce exceptional depth of focus as a side effect of suppressing aberrations. A typical SEM operates at aperture half-angles of 5–15 milliradians, compared to the tens of degrees that an oil-immersion optical objective uses. The depth of focus scales inversely with aperture angle, so the SEM has orders of magnitude more axial range than an optical instrument at comparable lateral resolution.

The practical rule is simple: if the specimen is flat and polished, use short working distance (4–8 mm) for maximum resolution. If the specimen has substantial topography, trade some resolution for depth of focus by moving to longer working distance (15–30 mm). The calculus can be done explicitly: if peak-to-valley topography is $\Delta z$ and the minimum acceptable feature size at the displayed magnification is $d_0$, then you need a depth of focus $D > \Delta z$, which means an aperture half-angle $\alpha < d_0 / \Delta z$.

Suppose a fracture surface has 8 μm of topography and the imaging requires 100 nm resolution. Then $\alpha < 100 \text{ nm} / 8 \text{ μm} = 12.5$ mrad. Any aperture giving a half-angle below 12.5 mrad will keep the surface in focus throughout the field. Whether the resulting resolution is adequate is a separate question — but the physics at least tells you what the constraint is.

---

The third control is probe size, which the operator adjusts through the condenser lens current and which physically determines how much current the probe carries.

The connection between probe size and current is not optional — it is forced by the conservation of beam brightness. The electron gun has a certain brightness $\beta$, defined as current per unit area per unit solid angle. Lenses can demagnify the source to make a smaller probe, but they cannot increase the brightness; they can only accept a smaller solid angle of electrons as the probe shrinks. The result is that current scales as $i_b \propto d^2 \alpha^2 \beta$ — proportional to the square of the probe diameter at fixed aperture angle. Halve the probe size, quarter the current.

![Two-axis diagram showing probe diameter on x-axis and](images/05-sem-modes-of-operation-fig-01.png)
*Figure 5.1 — Two-axis diagram showing probe diameter on x-axis and*

This coupling is the source of the central tension in SEM operation. A small probe gives high spatial resolution but low current, which means the signal from each pixel is small. You can compensate by spending more time on each pixel — longer dwell — but longer dwell means more time for specimen drift, contamination growth, and charging to accumulate. Or you can compensate by averaging many fast scans, which helps with drift but not with fundamental Poisson noise. High current gives better signal-to-noise and faster acquisition, but at the cost of a larger probe, which means lower resolution.

For imaging surface morphology at the highest resolution, the choice is usually a small probe with fast frame averaging: accept the low current per pixel, but add up enough frames to beat the noise down. For EDS elemental mapping — where you need to collect enough X-rays to get statistical significance from each pixel — the choice is usually a large probe with high current and a slow acquisition: accept the lower spatial resolution because the signal requirement is binding. The probe size choice is inseparable from the question of what you are trying to measure.

---

Now the aperture. Three things happen simultaneously when you change the aperture.

First, aberrations change. From Chapter 2, spherical aberration disk diameter scales as $C_s \alpha^3$. Smaller aperture, dramatically smaller spherical aberration — cubic scaling means halving the aperture angle reduces the spherical aberration disk by a factor of eight. Diffraction disk goes the other way: $0.61\lambda/\alpha$, so smaller aperture means more diffraction blur. The optimum is where the two cross, and it corresponds to a specific physical aperture size at a given working distance and kV. Modern SEMs have two or three aperture disks — typically 30, 60, and 100 μm — and the choice between them is an implicit choice of where to land on the aberration-diffraction trade.

Second, depth of focus changes, as described above. Smaller aperture, more depth of focus.

Third, current changes. Smaller aperture intercepts a smaller solid angle of the beam cone, so less current reaches the specimen. The signal falls.

All three effects are present simultaneously for every aperture choice. The practical heuristic is: for high-resolution imaging of flat specimens, use the medium aperture and let the optimization calculation from Chapter 2 do its job. For rough topographic specimens, use the smallest available aperture to maximize depth of focus, and compensate the lower current with more frames. For EDS or other high-current applications on flat specimens, use the largest aperture. The aperture should be a deliberate choice, not a default.

---

Setting these three controls — kV, working distance, probe size — in a principled way still leaves one important variable: what happens when the image is wrong. The most useful single skill in SEM operation is artifact diagnosis, because the image will be wrong sometimes, and the correct response is a specific change to a specific parameter rather than a general retreat to "try different settings."

Charging is the most common artifact on non-conductive specimens. The visual signature is immediate and distinctive: bright regions that grow during the scan, sudden reversals of contrast, or streaks and distortions that propagate across the image as if a static electricity discharge is happening inside the frame. The mechanism is straightforward — more electrons arriving at the surface than leaving, net negative charge accumulating, the resulting electric field deflecting subsequent beam electrons and perturbing SE trajectories. The fix depends on the mechanism. The secondary electron yield — the number of SEs emitted per incoming beam electron — exceeds 1 at low kV for many materials, which means the specimen actually loses charge to the detector faster than the beam deposits it. At higher kV, the yield falls below 1. So for an insulating specimen, there is a crossover energy, typically 1–3 kV depending on material, below which the specimen charges positively by a small amount (harmless) rather than negatively (destructive). Imaging at or below the crossover energy eliminates charging without coating. If the feature of interest requires higher kV, a thin conductive coating — 3–10 nm of gold-palladium or platinum — drains charge to ground and restores the image. If coating is undesirable because it obscures fine surface features, fast scanning with frame averaging is the remaining option: reduce dwell time per pixel so charge has less time to accumulate per frame, and sum enough frames for adequate SNR.

Drift is more insidious because it can look like poor resolution. The signature is directional blurring — features are sharp in one direction and smeared in another, and the smear direction is consistent across the field. The cause is usually thermal: the specimen or stage has not reached thermal equilibrium after insertion or after a large kV change, and the slow mechanical motion of a thermally expanding column or stub shifts the image. The fix is patience — five to fifteen minutes after any major thermal perturbation before high-magnification work — and fast acquisition with frame averaging, which distributes the drift's effect over many frames rather than integrating it into one.

Astigmatism produces a different directional signature: features are elongated, but the elongation direction rotates 90° as you pass through focus. Underfocus elongates in one direction; overfocus elongates perpendicularly; at nominal focus the image briefly looks sharp but soft at the same time, and there is a narrow range of focus where the elongation is minimized rather than a single sharp optimum. This is the through-focus astigmatism rotation that Chapter 2 described geometrically. The fix is the stigmator cycle: adjust the x-stigmator, refocus, adjust the y-stigmator, refocus, iterate. The stigmator needs to be repeated every time kV, aperture, or working distance changes, because each of those shifts the electron trajectories that intersect the lens's mechanical imperfections.

| Image symptom | Most likely cause | First parameter to change | Diagnostic confirmation |
|---|---|---|---|
| **Bright regions growing during scan** | Charging accumulating on insulating regions | Lower the kV (try 5 kV); add coating or use VP mode | Effect persists across multiple frames; spreads outward from specific features |
| **Directional smear consistent across the field** | Stage drift (thermal or mechanical) | Wait 10–20 min for thermal equilibration; check stage clamp | Drift direction stays consistent across all frames |
| **Streak rotates 90° through focus** | Astigmatism | Adjust the stigmator | Reverse blur direction at over- vs. under-focus |
| **Uniform softness across a flat specimen** | Defocus | Refocus | Sharpens at correct working distance |
| **Edges sharp but interior blurred** | Insufficient depth of focus | Reduce aperture diameter; raise kV | Effect concentrated where specimen has height variation |
| **Dim image with asymmetry** | Aperture misalignment | Re-center the objective aperture | Dimming asymmetric across field; corrects on aperture wobble |

---

The patterns across all of these — charging, drift, astigmatism, depth-of-focus errors — point to a discipline that distinguishes experienced operators from novices.

The novice turns multiple knobs simultaneously when something is wrong. Each change modifies the image, but in a correlated way that makes it impossible to isolate cause from effect. After four simultaneous changes, the image may have improved, but no understanding has been gained. The next session starts from scratch.

The experienced operator identifies the artifact, names the most likely single cause, changes exactly that parameter, and observes the result. If the change helps, the diagnosis was right. If the change makes things worse or has no effect, the diagnosis was wrong, and a different parameter gets tried. This is experimental method applied to instrument operation. It is slower in the short run and dramatically faster across many sessions, because the mental model of the instrument accumulates.

The discipline also applies to parameter choices before the image is acquired. What is the feature of interest? What depth does it live at? What is the specimen's conductivity? What is the required lateral resolution? What is the required depth of focus? Each of these questions has a physics-based answer that constrains a parameter. kV is not arbitrary; working distance is not arbitrary; aperture is not arbitrary. They are arguments about where information lives in the specimen and what the beam must do to extract it.

When the image comes out right on the first try, it is because the operator thought through the physics before touching the knobs. When it doesn't — and sometimes it won't, because real specimens are complicated and the heuristics are starting points, not guaranteed solutions — the operator who understands the physics can reason toward the fix in minutes rather than hours.

The graduate student from the beginning of this chapter eventually became that operator. It took time at the instrument, but more than that it took the habit of asking why before asking what. Why is the image grainy? Because current per pixel is too low. Why is current low? Because the probe is small and the dwell is short. What is the fix? More frames or a larger probe, depending on which matters more. Why are there haloes? Because the kV is putting the interaction volume well below the particle. What is the fix? Drop the kV until the interaction volume is comparable to the particle size. Each fix follows from the physics. The knobs are just where the physics lives.

---

**What would change my mind:** evidence from a systematic study that image quality in SEM is primarily determined by a single dominant parameter — say, kV alone — independent of the specimen type. Every account of SEM practice I have encountered, including the materials in this course, confirms the coupling: kV, probe size, working distance, and aperture interact through the physics of the interaction volume and the lens. A specimen regime where one parameter genuinely dominated all others would require physics that doesn't appear in the standard model of beam-specimen interaction.

**Still puzzling:** the gap between physics-based prescription and working practice in most research labs. The protocol described in this chapter is derivable from Chapters 2 and 3; yet most working scientists learn operating conditions by imitation and tribal knowledge rather than calculation. The chapter is an attempt at one bridge across that gap. Whether it is the right bridge is an empirical question.

---

## Exercises

### Warm-up

**5.1** A student images a polished copper surface cleanly at 10 kV, then switches to 30 kV without changing any other parameter. Describe two distinct physical changes the higher voltage causes inside the specimen, and predict qualitatively how each would affect the image. *(Tests: interaction volume scaling with kV and its consequences for signal origin.)*

**5.2** You are imaging a rough fracture surface and notice that the left side of the image is sharp while the right side is blurred. The specimen has about 15 μm of topographic relief across the field. What is the most likely cause, and which single parameter should you change first? *(Tests: depth-of-focus limitation and aperture as the corrective lever.)*

**5.3** Explain in one paragraph why the focus knob and the kV control are not independent — that is, why changing accelerating voltage requires refocusing even if nothing else changes. *(Tests: focal-length dependence on electron energy from Chapter 2.)*

### Application

**5.4** A student is imaging chemically fixed, Pt-coated lung tissue (5 nm Pt) at 20 kV. The image shows bright haloes at cell edges and regions of extreme contrast reversal. Identify the artifact, explain its mechanism at 20 kV on this specimen, and give three mitigations in priority order with a one-sentence trade-off for each. *(Tests: charging diagnosis, crossover-energy concept, and mitigation hierarchy.)*

**5.5** You need to image a fractured ceramic with 12 μm of peak-to-valley topography. The displayed magnification requires a resolution of 150 nm. Calculate the maximum aperture half-angle that keeps the entire surface in focus. If the available aperture choices give half-angles of 5, 10, and 18 mrad at your working distance, which do you choose and why? *(Tests: depth-of-focus calculation and aperture selection.)*

**5.6** A beam-sensitive polymer specimen shows visible contamination growth within 20 seconds of imaging at 10 kV with a slow single-frame scan. You need a high-SNR image at 80,000×. Describe a complete acquisition strategy — kV, scan rate, number of frames — and explain the physical rationale for each choice. *(Tests: beam-sensitivity mitigation through scan strategy and SNR accumulation.)*

**5.7** An EDS measurement requires characteristic X-rays from titanium (Ti K$\alpha$ edge at 4.51 keV). What is the minimum acceptable accelerating voltage, and what voltage would you actually use in practice? What resolution penalty do you accept by operating at this voltage compared to 5 kV? *(Tests: EDS overvoltage rule and the resolution cost of high-kV EDS work.)*

### Synthesis

**5.8** A research group wants to image 5 nm gold nanoparticles dispersed on a 20 nm amorphous carbon support film mounted on a silicon stub, using a cold field-emission SEM. Specify all operating parameters: kV, working distance, probe size (qualitative), aperture choice, detector, and scan strategy. Then predict two artifacts the chosen parameters might still produce at these conditions and describe how to recognize each from the image alone. *(Tests: integrated parameter selection for a demanding specimen and prospective artifact diagnosis.)*

**5.9** Two images of the same uncoated polymer are acquired: one at 25 kV and one at 1.5 kV. The 25 kV image shows severe charging artifacts; the 1.5 kV image is clean. Explain the physical mechanism behind the difference using the concept of secondary electron yield, without using the word "yield." Then explain why the same approach would fail on a metallic specimen. *(Tests: charging mechanism, crossover energy, and material-dependence of the fix.)*

### Challenge

**5.10** The Kanaya-Okayama penetration depth scales as $R \propto V^{1.7} / \rho Z^{0.89}$ (where $\rho$ is density and $Z$ is atomic number). A research group claims their uncoated 10 nm polymer nanoparticles on a silicon substrate can be imaged charge-free at 5 kV. Use the scaling relation to estimate whether 5 kV puts the interaction volume primarily within the particle, within the substrate, or spanning both. Then look up or estimate a crossover energy for a typical polymer and assess whether their claim is physically plausible. *(Tests: interaction-volume estimation, crossover-energy reasoning, and critical reading of experimental claims.)*
