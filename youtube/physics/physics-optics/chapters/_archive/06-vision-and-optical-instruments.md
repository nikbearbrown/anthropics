# Chapter 6 — Vision and Optical Instruments

**Suggested titles**

1. Vision and Optical Instruments
2. The Eye, the Microscope, the Telescope: Three Variations on a Lens
3. Why You Wear Glasses, and How a Microscope Sees Things You Can't

**TL;DR.** The same thin-lens equation that you used to predict image positions in Chapter 25 is the engine behind the human eye, the corrective lenses prescribed by every optometrist on Earth, the compound microscope that revealed bacteria, and the refracting and reflecting telescopes that opened up the universe. This chapter takes those instruments apart, shows how each is a simple combination of lenses (or a lens and a mirror), and gives you the equations to predict what each one will image.

---

## Delft, around 1674: a draper looks at his teeth

Antonie van Leeuwenhoek is forty-two years old, a draper and city official in Delft with no formal training in science. He has a hobby. He grinds tiny glass beads, mounts them in metal frames, and uses them as single-lens microscopes — magnifications of two or three hundred times, far beyond anything else on Earth. With one of these instruments he scrapes plaque off his own teeth, mixes it with rainwater, places a drop on the lens, and looks.

He sees, in his words, "many very little living animalcules, very prettily a-moving."

He has just become the first human to observe bacteria. Within a few years he will see protozoa, sperm cells, the structure of muscle fibers, the tail of a mosquito, the parasites in the gut of a flea. The Royal Society of London, after some skepticism (a draper? from Delft?), will publish his letters. Microbiology, as a field, traces its origin to the moment Leeuwenhoek pressed his eye to a tiny ground bead of glass and saw an entire ecosystem he didn't know existed.

He didn't invent the microscope. Compound microscopes — devices using two lenses in series — had existed for sixty years; Galileo had used a related arrangement to look at insects. But Leeuwenhoek's single-lens instruments were better than any compound microscope of his era. He kept his grinding techniques secret. After his death his microscopes were mostly lost. We know what he saw partly because his hand-drawn illustrations of "animalcules" are recognizable as named species today.

What lets a small piece of glass extend the reach of human vision by three orders of magnitude? The same physics that lets a fixed-focal-length camera lens form an image on a detector, that lets a spectacle lens correct nearsighted vision, that lets the Hubble Space Telescope resolve galaxies at the edge of the observable universe. It is geometric optics — the thin-lens equation — applied with care to one or two lenses in series, with the human eye as the final detector.

This chapter takes apart the eye, the corrective lens, the microscope, and the telescope. Each is a study in how a small set of equations predicts the behavior of an instrument that has changed the world.

**Learning objectives.** By the end of this chapter you should be able to:

1. Describe the optical elements of the human eye (cornea, aqueous humor, lens, vitreous humor, retina), identify which provides most of the focusing power, and explain accommodation as adjustment of focal length by the ciliary muscle.
2. Calculate the corrective lens power required for myopia (nearsightedness) and hyperopia (farsightedness) given a person's near or far point and the lens-to-eye distance.
3. Compute the total magnification of a compound microscope as the product of objective and eyepiece magnifications, applying the thin-lens equation to each lens in series.
4. Compute the angular magnification of a refracting telescope from the focal lengths of objective and eyepiece ($M = -f_o/f_e$) and explain why long objective focal length and short eyepiece focal length give greater magnification.
5. Identify three common lens aberrations (chromatic, spherical, coma) and explain at least one design choice (achromatic doublet, aspheric surface, mirror objective) used to correct them.

**Prerequisites.** Chapter 25 (geometric optics): the thin-lens equation, ray tracing, lens power $P = 1/f$ in diopters, magnification $m = -d_i/d_o$, mirror focal length $f = R/2$. Comfort with applying $1/d_o + 1/d_i = 1/f$ multiple times in sequence (one lens at a time).

**Why this chapter matters.** The eye is your first detector for everything in the universe. Understanding how it works — and how its failures are corrected — is foundational. The telescope and microscope are how science extends vision into regimes where the unaided eye cannot reach: microbiology, astronomy, materials science, medicine. Every instrument in those fields is a refinement of the principles laid out here.

---

## Concept 1 — The eye as a lens-on-a-screen

### A camera obscura at noon, anywhere

Stand in a darkened room with a single small hole punched in one window shade. Outside, the sun is bright. On the opposite wall, you will see a faint, full-color, *upside-down* image of the world outside — the trees, the cars, the sky — projected by the geometry of light passing through the hole. The Latin name is *camera obscura* — "dark chamber." The principle was understood in the 11th century by Ibn al-Haytham (Alhazen), the Arab polymath whose *Book of Optics* established that vision is the eye receiving light from objects, not the eye emitting rays.

Your eye is essentially a camera obscura with a lens added to focus the image more sharply, an iris to control how much light gets in, a fovea to give you high-resolution central vision, and a retina full of photoreceptors to convert the optical image into nerve signals. The image on your retina is *upside down* — the geometry of any single converging lens guarantees inversion. The brain flips it back upright before you become conscious of it.

That's the eye in one sentence: a converging optical system projecting a real, inverted image onto a curved detector at a fixed distance behind the lens.

### The mechanism — anatomy and accommodation

Light entering the eye passes through, in order:

- The **cornea** (refractive index $n \approx 1.38$): the transparent dome at the front. The biggest single change in refractive index — air ($n = 1.00$) to cornea — happens here, so the cornea provides about *two-thirds* of the eye's total focusing power.
- The **aqueous humor** ($n \approx 1.34$): a watery fluid between cornea and lens.
- The **iris** and **pupil**: the iris is the colored ring; the pupil is the hole in the middle, varying from about $1 \text{ mm}$ in bright light to $8 \text{ mm}$ in darkness — a 64:1 area ratio that helps the eye function across about 10 orders of magnitude of light intensity.
- The **lens** ($n$ varies from ~$1.41$ at center to less at the edges, *graded index*): provides the remaining focusing power. Its shape — and therefore its focal length — is changed by the surrounding ciliary muscle.
- The **vitreous humor** ($n \approx 1.34$): a gel filling the back chamber.
- The **retina**: a layer of light-sensitive cells at the back of the eye, on which the image must form for clear vision.

The cornea-lens system together can be modeled, to good accuracy, as a single thin lens with adjustable focal length. The image distance $d_i$ from this effective lens to the retina is *fixed* — anatomically determined, about $2 \text{ cm}$ in an adult eye — so to focus on objects at different distances the eye must change its focal length. This adjustment is *accommodation*. The ciliary muscle squeezes the lens to make it more curved (shorter $f$, more power) for nearby objects, and relaxes for distant ones (longer $f$, less power).

A "normal" relaxed eye is focused at infinity. A relaxed normal eye has a near point — the closest distance at which a clear image can be formed — of about $25 \text{ cm}$. The near point recedes with age (presbyopia) because the lens stiffens.

### The trade-off

The eye trades **dynamic range for fixed geometry.** The retinal distance is fixed; rather than moving the lens (as in a camera), the eye changes the lens's focal length. This works elegantly for a wide range of object distances but introduces a fundamental limit: the lens cannot become arbitrarily curved. Beyond the near point, the lens has reached its maximum curvature and cannot focus closer. With age, lens flexibility declines, and the near point recedes — eventually past arm's length, which is why most people need reading glasses by their mid-forties.

### Worked example — the lens power for relaxed distant vision

A relaxed adult eye focusing on a very distant object has $d_o \to \infty$ and $d_i = 2.0 \text{ cm}$ (typical lens-to-retina distance). What is the eye's total optical power?

Apply $P = 1/f = 1/d_o + 1/d_i$:

$$P = \frac{1}{\infty} + \frac{1}{0.020 \text{ m}} = 0 + 50 \text{ D} = 50 \text{ D}.$$

A relaxed eye is roughly a 50-diopter optical system. Most of this comes from the cornea ($\sim 40 \text{ D}$); the lens itself adds only about $10 \text{ D}$ when relaxed. To focus on an object $25 \text{ cm}$ away (the near point), the eye must increase its power by

$$\Delta P = \frac{1}{0.25} = 4 \text{ D},$$

going from $50 \text{ D}$ to $54 \text{ D}$. This is roughly the dynamic range of accommodation a healthy young eye can produce.

**Sanity check.** A standard eyeglass prescription rarely exceeds $\pm 10 \text{ D}$, so the eye's $\sim 50 \text{ D}$ baseline is much larger than any correction. Glasses are tweaks, not replacements.

### Common misconceptions

- *"The lens of the eye does most of the focusing."* No — the cornea does, by about a 2:1 ratio. The lens is the *adjustable* element, but the cornea provides the bulk of the static focusing power. This is also why LASIK reshapes the cornea (not the lens) to correct vision.
- *"The image on the retina is right-side up."* It's inverted. Your brain processes it as upright. Experiments where people wear inverting goggles for several days show the brain eventually re-inverts the inverted input — perception is plastic.

↳ **Dig Deeper — How the brain handles binocular depth**

*The chapter treats one eye in isolation. Stereoscopic depth — your sense of 3D — comes from comparing the slightly different images formed in your left and right eyes. The geometry of how two images become one perceived depth is one of the most studied topics in perceptual neuroscience, and underlies modern VR headsets and 3D movies.*

**Prompt:**
> Explain how binocular vision produces depth perception. Walk me through (a) the geometry of *retinal disparity* — the slight horizontal offset between the same object's image in the left and right eyes, (b) how the brain combines the two images into a single perceived 3D scene (*stereopsis*), and (c) the limits of stereopsis (objects too far away produce essentially no disparity; that's why distance perception beyond ~10 m relies more on monocular cues like perspective and shading). End with one sentence on how a VR headset exploits this physiology to create the illusion of 3D from two flat displays.

**What to do with the output:** Save it. The geometry of binocular vision is also the basis of stereo cameras, photogrammetry, and all 3D reconstruction algorithms in computer vision.

---

## Concept 2 — Why your friends wear glasses: vision correction

### An optometrist's chair, this afternoon

You look at a chart of letters. The optometrist swaps lenses in front of your eye and asks "better, or worse?" When the smallest line snaps into focus, she writes a prescription: a number in *diopters* for each eye, possibly with extra numbers for astigmatism. The number is the optical power of a corrective lens that, placed about $1.5 \text{ cm}$ from your eye, will compensate for whatever your eye is doing wrong.

What is your eye doing wrong? Two main things, and the geometry of each is straightforward.

### The mechanism — myopia, hyperopia, and the corrective lens

**Myopia (nearsightedness).** The eye is too long, or the cornea/lens system is too powerful. Light from a distant object is over-focused — it converges to a point *in front of* the retina, then diverges before reaching it, producing a blurry image. The far point (the most distant object the eye can focus on) is closer than infinity.

The fix: a *diverging* lens (negative focal length, negative diopters). The diverging lens takes light from a distant object and produces a virtual image *closer* than the actual object. If that virtual image lies at or within the eye's far point, the eye can focus on it.

**Hyperopia (farsightedness).** The eye is too short, or the cornea/lens system is too weak. Light from a nearby object converges toward a point *behind* the retina, never quite reaching focus on the retina. The near point is farther than the normal $25 \text{ cm}$.

The fix: a *converging* lens (positive focal length, positive diopters). The converging lens takes light from a nearby object and produces a virtual image *farther* than the actual object — pushed out to or beyond the eye's near point.

In both cases, the prescribed power is calculated by demanding that the image formed by the corrective lens lie at the limit of the eye's focusing range. The corrective lens does not change the eye; it puts the image of every real-world object at a distance where the eye *can* focus.

A third defect, **astigmatism**, comes from a non-spherical (cylindrical) shape of cornea or lens. Different planes through the optical axis have different focal lengths, so vertical and horizontal lines focus at different distances. Correction uses a cylindrical lens oriented to match the patient's astigmatism axis.

A fourth, **presbyopia**, is the age-related loss of accommodation as the lens stiffens. Treated with reading glasses (converging lenses for near work), bifocals (different power in upper and lower halves of the lens), or progressive lenses (a smooth gradient).

### The trade-off

Corrective lenses trade **anatomical perfection for additional optical hardware.** The eye's focal range has a limited window; corrective lenses are a way to shift external objects into that window without surgery. The cost: glasses can fog up, slip, or be left at home; contact lenses sit on a sensitive surface; refractive surgery (LASIK, PRK) reshapes the cornea permanently and trades flexibility for one-time correction. Each option has a different set of trade-offs.

### Worked example — correcting nearsightedness

A patient has a far point of $30.0 \text{ cm}$. What power eyeglass lens corrects this? Assume the lens sits $1.50 \text{ cm}$ in front of the eye.

The corrective lens must produce a virtual image at the patient's far point ($30.0 \text{ cm}$ from the eye, or $30.0 - 1.50 = 28.5 \text{ cm}$ from the lens itself) for an object infinitely far away. Therefore $d_o = \infty$ and $d_i = -28.5 \text{ cm} = -0.285 \text{ m}$ (negative because the virtual image is on the same side as the object — incoming-light side).

Apply the thin-lens equation:

$$P = \frac{1}{d_o} + \frac{1}{d_i} = 0 + \frac{1}{-0.285 \text{ m}} = -3.51 \text{ D}.$$

A diverging lens, $-3.51 \text{ D}$. The negative sign tells you it is a diverging (concave) lens — exactly what's needed for myopia.

**Sanity check.** A typical mild-to-moderate myopia prescription is in the range of $-1$ to $-6$ diopters; $-3.51$ is in the middle. The patient with a 30 cm far point is moderately nearsighted — they can read clearly at arm's length but cannot make out a road sign across the street.

### Common misconceptions

- *"Wearing glasses makes your eyes weaker."* No. Glasses do not change the eye. They form an image at a distance the eye can focus on. The eye's underlying defect is unaffected.
- *"Reading without glasses 'strains' the eye and makes vision worse."* For uncorrected presbyopia or hyperopia, you may strain the ciliary muscle squinting at fine print, which can cause headaches and fatigue but does not progressively damage vision. The defect itself is anatomical.
- *"Laser eye surgery cures vision."* It permanently reshapes the cornea to a different (often less defective) curvature. It can correct myopia, hyperopia, and astigmatism in many patients. It cannot restore lost accommodation (presbyopia) or reverse age-related lens stiffening, and it does not fix the underlying biology — it just relocates the focal length.

↳ **Dig Deeper — How LASIK actually reshapes the cornea**

*The chapter mentions laser eye surgery in passing. The procedure uses an excimer laser at 193 nm — far ultraviolet — to ablate (vaporize) extremely thin layers of corneal tissue. The 193 nm wavelength is chosen because it is absorbed by corneal tissue within about a quarter-micron of the surface, so a single pulse removes a precisely controlled amount.*

**Prompt:**
> Walk me through how LASIK reshapes the cornea step by step: the creation of a thin corneal flap (microkeratome or femtosecond laser), the sculpting of the underlying stroma with an excimer laser, and the replacement of the flap. Compute roughly how much tissue must be removed to change the cornea's curvature enough to correct $-3 \text{ D}$ of myopia (you'll need approximate corneal radius of curvature ~$7.7 \text{ mm}$). Explain why 193-nm UV is specifically chosen rather than visible or longer-wavelength UV. End with one sentence on the most common LASIK complications and why the procedure has nevertheless become routine.

**What to do with the output:** Save it. LASIK is a beautiful intersection of geometric optics, laser physics, and tissue absorption — and one of the most-performed elective surgeries in medical history.

---

## Concept 3 — Microscopes and telescopes: lenses in series

### Mount Wilson, October 1923

Edwin Hubble is on the floor of the 100-inch telescope at Mount Wilson Observatory, just outside Pasadena, California. He has been imaging a fuzzy patch in the constellation Andromeda — what astronomers of his era called the "Andromeda Nebula" — and he has just identified, on a recent photographic plate, a particular type of variable star (a Cepheid) inside it. Cepheids have a property Henrietta Leavitt had discovered in 1912: their pulsation period predicts their absolute brightness. Compare the absolute brightness to the apparent brightness, and you get the distance.

Hubble does the calculation. The "nebula" is roughly $900{,}000$ light-years away. (Modern measurements put Andromeda at about $2.5$ million light-years; Hubble's original calibration was off by a factor of about three.) Either way, it is far outside our own Milky Way galaxy. Andromeda is not a nebula at all. It is *another galaxy*, comparable in size to ours, separated by a vast intergalactic distance.

Within five years, Hubble will discover that *all* such "nebulae" are receding from us, with velocities proportional to their distances — the expansion of the universe. The 100-inch telescope (objective mirror diameter 100 inches = $2.54 \text{ m}$) was, at the time, the largest in the world. It was the instrument that revealed that the Milky Way is one galaxy among uncountable many.

The microscope and the telescope — two-lens (or lens-plus-mirror) instruments built from the equations of Chapter 25 — are how human eyesight has been extended to the microscopic and to the cosmological. We work out their geometry now.

### The mechanism — the compound microscope

A *compound microscope* uses two converging lenses in series (Figure 26.3 in OpenStax). The object — a tiny specimen on a slide — is placed just outside the focal length of the first lens (the *objective*). The objective forms a real, inverted, magnified image at some intermediate position inside the microscope tube. That image becomes the *object* for the second lens (the *eyepiece*). The eyepiece is positioned so the intermediate image lies just inside its focal length, making the eyepiece act as a magnifying glass — producing a final, virtual, very-magnified image far enough from the observer that the eye can focus on it relaxed.

The total magnification is the product of the two magnifications:

$$m = m_o \cdot m_e,$$

where $m_o = -d_i / d_o$ is the magnification of the objective (computed from its image and object distances) and $m_e$ is the magnification of the eyepiece. This product rule is general — for any chain of thin lenses or mirrors, the total magnification is the product of the individual magnifications.

### Worked example — a 60.0× compound microscope

A compound microscope has objective focal length $f_o = 6.00 \text{ mm}$ and eyepiece focal length $f_e = 50.0 \text{ mm}$. The object is placed $d_o = 6.20 \text{ mm}$ from the objective. The objective and eyepiece are separated by $23.0 \text{ cm}$.

**Objective stage.** Apply the thin-lens equation to find the image position:

$$\frac{1}{d_i} = \frac{1}{f_o} - \frac{1}{d_o} = \frac{1}{6.00} - \frac{1}{6.20} = \frac{0.00538}{\text{mm}}.$$

$$d_i \approx 186 \text{ mm}.$$

The objective forms an image $186 \text{ mm}$ to the right of itself. The objective magnification:

$$m_o = -\frac{d_i}{d_o} = -\frac{186}{6.20} = -30.0.$$

The image is inverted (negative sign) and 30 times the size of the object.

**Eyepiece stage.** This image is the object for the eyepiece. The eyepiece is $230 \text{ mm}$ from the objective, so the intermediate image is at $230 - 186 = 44 \text{ mm}$ in front of the eyepiece — that is, $d_o' = 44 \text{ mm}$, slightly inside the eyepiece's focal length of $50 \text{ mm}$. The eyepiece thus acts as a magnifying glass.

For a magnifying glass producing a virtual image at infinity, the magnification is $m_e = (25 \text{ cm}) / f_e$ (the comparison being to viewing the same object at the standard near point of $25 \text{ cm}$ unaided). In our case:

$$m_e = \frac{25 \text{ cm}}{5.00 \text{ cm}} = 5.0.$$

**Total magnification.**

$$m = m_o \cdot m_e = (-30.0)(5.0) = -150.$$

The minus sign indicates inversion. The microscope produces an image $150 \times$ larger than the object, with the orientation flipped relative to looking at the object directly through unaided eyes.

**Sanity check.** Standard high-school microscopes top out at about $400×$ magnification (e.g., $40×$ objective $\times$ $10×$ eyepiece). Our $150×$ system is in the middle of that range. Higher magnifications are possible but limited by the diffraction limit (Chapter 27): visible-light microscopes cannot resolve features smaller than about $200 \text{ nm}$, regardless of magnification.

### The mechanism — the refracting telescope

A *refracting telescope* (also called Keplerian, after Johannes Kepler who designed the first one in 1611) is similar to a compound microscope but with very different focal lengths and a very distant object. The objective lens has a long focal length; the eyepiece has a short one. The object is essentially at infinity (a star, the moon), so the objective forms an image at $d_i = f_o$ — exactly at its own focal point. The eyepiece is positioned with this intermediate image just inside its focal length, again acting as a magnifying glass.

The relevant figure of merit for a telescope is *angular magnification* $M$ — the ratio of the angle subtended by the final image to the angle subtended by the object as seen by the unaided eye:

$$\boxed{M = -\frac{f_o}{f_e}.}$$

The minus sign indicates inversion. Long objective focal length and short eyepiece focal length produce large angular magnification. To increase a refracting telescope's magnification you can either lengthen the objective focal length (making the tube longer) or shorten the eyepiece focal length (making the eyepiece more powerful). The latter has practical limits — eyepieces with focal lengths below a few millimeters become uncomfortable to look through — so very high magnifications usually come from very long objective focal lengths.

### Why most large telescopes use mirrors instead of lenses

Refracting telescopes have practical limits: large lenses sag under their own weight, are expensive to make defect-free, and chromatic aberration (different colors focusing at different distances) gets worse with size. A *reflecting telescope* (invented by Newton in 1668) uses a concave mirror as its objective. Mirrors can be made much larger than lenses (no internal stress, can be supported from behind), have no chromatic aberration (the law of reflection is wavelength-independent), and can be aluminized to high reflectivity. Every research-grade optical telescope built in the past 150 years uses a mirror objective. The Hubble (2.4 m), Keck (10 m), and the James Webb Space Telescope (6.5 m segmented mirror) all reflect.

### The trade-off

Multi-element optical instruments trade **complexity for capability.** A single magnifying glass can deliver maybe $5×$ magnification before image quality suffers. A two-element microscope routinely hits $400×$. A three- or four-element design with corrective elements can image diffraction-limited at much higher magnification. The cost: more lenses mean more aberrations to correct, more surfaces to polish, more alignment tolerances, more cost. A research-grade microscope objective contains 10+ elements and costs as much as a small car.

### Common misconceptions

- *"Bigger telescopes magnify more."* No, bigger telescopes *gather more light* and *resolve finer detail* (the diffraction limit scales as $\lambda / D$). Magnification is set by the eyepiece. A bigger objective doesn't make the moon look more magnified; it makes it look brighter and reveals finer features.
- *"Microscopes have unlimited magnification."* No. The diffraction limit (Chapter 27) caps optical microscope resolution at roughly half the wavelength of the light used — about $200 \text{ nm}$ for visible light. Beyond that, magnification just blurs. Electron microscopes (using electron de Broglie wavelengths) reach atomic resolution; super-resolution fluorescence techniques (STED, PALM, STORM) circumvent the diffraction limit by clever physics.

↳ **Dig Deeper — Aberrations and how multi-element designs correct them**

*The chapter mentions aberrations briefly. Real optical instruments use carefully chosen combinations of lens materials and shapes to cancel aberrations. The achromatic doublet (a converging crown-glass lens cemented to a diverging flint-glass lens) is the classic example — it cancels chromatic aberration to first order.*

**Prompt:**
> Explain how an achromatic doublet works to correct chromatic aberration. Walk through (a) why a single converging lens has chromatic aberration (the index of refraction depends on wavelength, so different colors focus at different points), (b) how pairing it with a weaker diverging lens of a different glass type (different dispersion) can cancel the wavelength dependence of focal length to first order, (c) why the two lenses must be different glass types (typically crown and flint) rather than just different powers of the same glass. End with one sentence on what an *apochromatic* triplet does that an achromatic doublet cannot.

**What to do with the output:** Save it. The achromatic doublet is the cleanest example in optics of "two engineered defects canceling each other to produce a near-perfect result" — and the same logic underlies many compensation schemes throughout physics and engineering.

---

## Synthesis — from one lens to a telescope

Step back. Three concepts in this chapter, all built from one tool: the thin-lens equation $1/d_o + 1/d_i = 1/f$ from Chapter 25, applied to one lens at a time, with image of one becoming object of the next.

**Concept 1** showed that the eye is a single adjustable converging lens forming a real, inverted image on the retina. The cornea provides most of the static power; the lens itself adjusts focal length via the ciliary muscle.

**Concept 2** showed that vision defects are mostly geometric — eye too long (myopic), too short (hyperopic), too stiff (presbyopic), too cylindrical (astigmatic) — and that the corrective lens is just an additional element placed in front of the eye to put the world's image into the eye's focusing range. The math is $P = 1/d_o + 1/d_i$ with $d_i$ chosen to be the eye's far or near point.

**Concept 3** showed that the microscope and the telescope are simply two lenses in series. The objective forms a real intermediate image; the eyepiece magnifies that image into a comfortable virtual final image. The thin-lens equation applies twice.

The deepest single fact: **everything in this chapter is one equation applied carefully.** No new physics — just patient ray tracing and arithmetic. The eye, the spectacle lens, the LASIK procedure, the microscope, the refracting telescope, the reflecting telescope — all of it falls out of the geometry of Chapter 25.

### A worked example using all three concepts — a stargazer with glasses

A nearsighted observer with a far point of $40.0 \text{ cm}$ wants to look at Saturn through a refracting telescope with $f_o = 1.20 \text{ m}$ and $f_e = 25.0 \text{ mm}$. He keeps his glasses on. The glasses sit $1.5 \text{ cm}$ from his eye.

**Concept 2 — corrective lens for the eye.** His glasses have to bring distant objects to the eye's far point of $40.0 \text{ cm}$ — that is, $40.0 - 1.5 = 38.5 \text{ cm}$ from the lens. So $d_i = -38.5 \text{ cm} = -0.385 \text{ m}$, $d_o = \infty$:

$$P_{\text{glasses}} = 0 + \frac{1}{-0.385} = -2.60 \text{ D}.$$

**Concept 3 — telescope angular magnification.** The telescope's intrinsic magnification:

$$M = -\frac{f_o}{f_e} = -\frac{1.20 \text{ m}}{0.025 \text{ m}} = -48.$$

The minus sign means inverted; the magnitude is $48×$.

**Putting it together.** Through the telescope, Saturn (about $1.4 \text{ billion km}$ away) subtends an angle that is $48$ times its naked-eye angular size. That image then passes through his glasses, which adjust the convergence to put the final image where his eye can focus. The eye, properly accommodating, forms a sharp image on his retina.

**Concept 1 — image on retina.** The eye, with glasses providing $-2.60 \text{ D}$ correction, can focus from about $25 \text{ cm}$ near (with strong accommodation) to infinity. The telescope, plus glasses, plus eye delivers a sharp $48×$-magnified image of Saturn to the observer's retina.

**Scale shift.** That same chain of optics, scaled up, is what Edwin Hubble used at Mount Wilson in 1923 to discover that Andromeda was a separate galaxy. The physics is identical: lens forms image, image is the object for next element, total magnification is the product. Scale up the objective from 1.2 m to 2.5 m, replace the lens with a parabolic mirror, replace the eyepiece-and-eye with a high-resolution photographic plate (or, today, a CCD), and you have an instrument that can resolve individual Cepheid variables in galaxies millions of light-years away.

---

## Exercises

### Warm-up

**26.1** *(LO 1)* What is the optical power, in diopters, of a relaxed normal eye whose cornea-to-retina distance is $2.10 \text{ cm}$ when focused on a very distant object?

**26.2** *(LO 1)* Identify which structure provides each of the following functions in the eye: (a) most of the focusing power, (b) adjustable focal length, (c) light intensity control, (d) photoreceptor array, (e) high-acuity central vision.

**26.3** *(LO 2)* A patient's far point is $50.0 \text{ cm}$. What corrective lens power (in diopters) does she need? Assume glasses sit $1.50 \text{ cm}$ from the eye.

**26.4** *(LO 4)* A telescope has $f_o = 800 \text{ mm}$ and $f_e = 20.0 \text{ mm}$. Find the angular magnification.

### Application

**26.5** *(LO 2)* A patient's near point is $1.00 \text{ m}$. What power lens does he need to read a book at $25.0 \text{ cm}$? (Assume lens at the eye.)

**26.6** *(LO 3)* A compound microscope has $f_o = 8.00 \text{ mm}$ and $f_e = 25.0 \text{ mm}$, separated by $20.0 \text{ cm}$. The object is placed $9.00 \text{ mm}$ from the objective. Find (a) the objective magnification, (b) the eyepiece magnification, (c) the total magnification.

**26.7** *(LO 4)* A telescope is used to view the moon (angular diameter ~$0.50°$). With $M = -100$, what is the angular size of the moon's image? Convert to arcminutes.

**26.8** *(LO 1, LO 2)* You have a $-3.0 \text{ D}$ pair of glasses. Without glasses, your far point is at what distance from the eye? (Assume glasses 1.5 cm from eye.)

### Synthesis

**26.9** *(LO 2)* A presbyopic patient with otherwise normal distance vision has a near point at $80.0 \text{ cm}$. What reading-glass power (lens at the eye) lets him read at $30.0 \text{ cm}$?

**26.10** *(LO 3, LO 5)* Microscope objectives are typically labeled with their magnification (e.g., $40×$). A standard objective has $40×$ magnification when used with the standard tube length and a $10×$ eyepiece. Compute the total magnification, and sketch why the diffraction limit ($\sim 200 \text{ nm}$ for visible light) means $1000×$ is roughly the practical maximum for optical microscopy.

**26.11** *(LO 4, LO 5)* The Keck telescopes on Mauna Kea have $f_o \approx 17.5 \text{ m}$ and use eyepieces (when used visually) of $f_e \approx 50 \text{ mm}$. (a) Compute the angular magnification. (b) Why are research-grade telescopes essentially never used visually anymore — what's used instead?

### Challenge

**26.12** *(beyond chapter)* Astigmatism is corrected with cylindrical lenses oriented at a specific axis. (a) Explain in your own words why a cylindrical lens has different focal lengths along different axes. (b) Why does the astigmatism prescription include both a power and an axis (in degrees)?

**26.13** *(beyond chapter)* The James Webb Space Telescope uses a 6.5-m segmented primary mirror and operates primarily in the infrared (0.6–28 μm). (a) Why is the primary segmented? (b) Why infrared and not visible? (c) The optical path includes a secondary mirror and additional optics before the detectors — sketch how this matches the two-lens microscope/telescope geometry from Concept 3, with the secondary playing the role of the eyepiece in some sense.

---

## LLM Exercise — Chapter 26: Vision and Optical Instruments in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An entry analyzing the optical-instrument or vision-system aspect of your anchor phenomenon — your eye, glasses, contact lenses, the optics of any camera or display involved, or any magnifying or focusing element.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 26, I want to apply optical-instrument physics — the eye, corrective lenses, microscope/telescope geometry — to my phenomenon.

Please:

1. Identify ONE optical instrument or vision-related element in my phenomenon. Examples: for a bike commute — my own eye (with prescription if I wear glasses), my bike's reflectors (which work via the corner-cube principle), the rear-view camera display in newer cars. For a coffee maker — the magnifying loupe a barista might use to inspect espresso crema, the eye observing the brew. For a basketball shot — my eye tracking the ball, the camera that records the game, the gym's overhead screens. For a marathon — the GPS watch's display optics, sunglasses, contact lenses.

2. Compute one quantitative property: corrective lens power needed (if you wear glasses, use your actual prescription); angular magnification if a telescopic element is involved; or focal length of a camera lens given its specs.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report with units.

5. One sanity check: does the computed value match the actual prescription, the camera's documented spec, or the qualitative behavior you observe?

6. One sentence on how this entry connects to Chapter 27 (wave optics) — diffraction will set fundamental limits on what any optical system can resolve.

Save the output as logbook/chapter-26-vision.md.
```

### What this produces

A Logbook entry that pins down the optics of seeing your phenomenon, ideally including your own eye and any optical aid you use.

### How to adapt this prompt

- *If you don't wear glasses:* Compute your eye's effective optical power for distant viewing ($\sim 50 \text{ D}$) and for near work, and reflect on accommodation.
- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* If you have an actual prescription, use Claude Code to convert prescription notation (sphere, cylinder, axis) into focal lengths and identify which type of correction it represents.

### Connection to previous chapters

Builds directly on Chapter 25 — every equation here is the thin-lens equation applied with care.

### Preview of next chapter

Chapter 27 (wave optics) returns to the wave nature of light. The diffraction limit in particular will explain why no optical microscope can resolve features smaller than ~200 nm and why telescope resolution depends on aperture diameter.

---

## Chapter summary

The human eye is a converging optical system that projects a real inverted image onto the retina. The cornea provides about two-thirds of the focusing power; the lens provides the rest and adjusts (accommodation) for objects at different distances. Common vision defects (myopia, hyperopia, presbyopia, astigmatism) are geometric and corrected with appropriately chosen lenses or surgery. The compound microscope uses an objective and an eyepiece in series; the magnification is the product of individual magnifications. The refracting telescope uses the same series geometry with a long objective focal length and short eyepiece focal length, giving angular magnification $M = -f_o/f_e$. Reflecting telescopes substitute mirrors for lenses to reach larger apertures and avoid chromatic aberration.

The one idea that matters most: **every instrument in this chapter is the thin-lens equation applied with care.** No new physics beyond Chapter 25 is needed — only patient bookkeeping of one lens at a time.

The common mistake to watch for: **confusing magnification with light-gathering or with resolution.** Magnification is set by eyepiece (or eyepiece-objective ratio); light-gathering is set by aperture; resolution is set by aperture and wavelength (Chapter 27). Bigger telescope ≠ more magnification; it = more light + finer resolution.

What you should now be able to teach someone else: how the eye focuses on objects at different distances, why a nearsighted person needs a diverging lens and a farsighted person a converging lens, and how a microscope or telescope multiplies magnification by chaining two lenses. If you can also explain why eyeglass prescriptions are written in diopters (and not in centimeters), you've understood the practical core of this chapter.

---

## What would change my mind

The chapter argues that geometric optics — applied carefully, lens by lens — is sufficient to explain the imaging behavior of the eye, corrective lenses, and standard microscopes and telescopes. The argument needs revision when you push to ultra-high resolution (the diffraction limit, Chapter 27) or to instruments where wave effects dominate (interferometric telescopes, super-resolution microscopes). Within the regime where the wavelength is small compared to apparatus, the thin-lens equation is essentially exact.

## Still puzzling

The deepest unresolved question this chapter touches without answering: **why does the brain perceive the inverted retinal image as upright?** Experiments where subjects wear inverting goggles show the brain re-inverts within days, then needs another adjustment when the goggles come off. The neural mechanism is partially mapped but not fully understood. Perception is not just optics; it is also massive neural processing that geometric optics says nothing about.

---

## Connections forward

Chapter 27 (wave optics) reveals the diffraction limit — the fundamental cap on the resolution of any optical instrument — and explains polarization, interference, and diffraction phenomena that geometric optics misses. Chapter 28 (special relativity) revisits the speed of light and asks what happens to length and time at speeds approaching $c$. Chapter 32 (medical applications of nuclear physics) uses fiber-optic endoscopes (Chapter 25) and high-resolution imaging in medical contexts. The telescopes built on this chapter's principles — Hubble, JWST, Keck, the next generation of 30-m-class ground telescopes — are how we now study the chemistry of exoplanet atmospheres, the cosmic microwave background, and the early universe.

---

**Tags:** vision, eye, corrective-lenses, microscope, telescope

---

## AI Wayback Machine

**Hans Lippershey** filed the first known patent for the telescope in 1608 in the Netherlands — beating Galileo to publication, though Galileo improved the design and turned it on the sky. The vision-correcting power of lenses had been understood for centuries before Lippershey combined two into an instrument.

**Run this:**

```
Who was Hans Lippershey, and how does his work on the telescope connect to the optical instruments we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hans Lippershey"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through how Lippershey's combination of an objective and eyepiece lens produces magnification.
- Ask it about the contested priority — Lippershey vs. Janssen vs. Metius — over who actually invented the telescope.

What changes? What gets better? What gets worse?
