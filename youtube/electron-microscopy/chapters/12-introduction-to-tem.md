# Chapter 12 — Introduction to Transmission Electron Microscopy


## TL;DR

- The SEM looks at surfaces; the TEM looks through them — and that single difference in preposition reorganizes everything: the physics, the specimen, the image, the question you can ask.
- The chapter moves through What TEM does that SEM cannot, What happens to the beam inside the specimen, The image is a projection, What the numbers look like, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The SEM looks at surfaces; the TEM looks through them — and that single difference in preposition reorganizes everything: the physics, the specimen, the image, the question you can ask.*

---

In 1924, Louis de Broglie proposed, in his doctoral thesis, that moving particles have a wavelength. The relation is simple:

$$\lambda = \frac{h}{mv}$$

where $h$ is Planck's constant, $m$ is the particle's mass, and $v$ is its velocity. For an electron accelerated through 60,000 volts, the velocity is a substantial fraction of the speed of light, and the wavelength works out to about 0.005 nm — five picometers. For comparison, the spacing between adjacent silicon atoms in a crystal is about 0.235 nm. The electron's wavelength is 47 times smaller than the thing it might resolve.

The optical microscope is limited by the wavelength of visible light, roughly 400–700 nm. Below a few hundred nanometers, features simply diffract around the probe and blur together — not a failure of the instrument but a consequence of wave physics that no lens arrangement can circumvent. De Broglie's insight meant that electrons, if you could make them into a beam and focus them, could in principle resolve individual atoms. The question was whether the engineering could catch up to the physics.

Fourteen years later, in 1938, Ernst Ruska and Bodo von Borries demonstrated a practical transmission electron microscope with 10-nanometer resolution. Ruska received the Nobel Prize for the work in 1986 — fifty-two years after the first working instrument, in one of the longer Nobel delays on record.

Today's instruments resolve below 0.1 nm routinely. The wavelength was always there; the engineering caught up.

## What TEM does that SEM cannot

The scanning electron microscope works by sweeping a focused probe across the surface of a bulk specimen and reading what comes back: secondary electrons, backscattered electrons, X-rays. The image is a map of surface responses. The specimen can be a rock, a circuit board, a bone fragment — essentially anything that fits in the chamber and survives the vacuum.

The transmission electron microscope works differently in every respect. Instead of a focused probe scanning a surface, it shines a wide, coherent electron beam onto a specimen thin enough for the electrons to pass through. Post-specimen lenses magnify the transmitted beam and project it onto a detector. The image is not a map of what came back from the surface — it is a projection of what came through the volume.

The difference is more than instrumental. It is about what question you can ask. When a cardiologist's lab wants to know whether mitochondria in a diseased cardiac cell have fragmented inner membranes, they cannot answer that question with an SEM. The SEM sees the surface of the cell. The mitochondria are inside. The TEM — with the cell sectioned to 70 nm and the beam passing through — shows the mitochondrial cristae directly, sharp at the 10-nm level, inside a single cell. That is what transmission means: you are looking through the specimen, at its interior, not at its face.

The price is the specimen. To transmit the beam, the specimen must be thin. Not thin in the way a polished surface is thin, but genuinely, pervasively thin — typically less than 100 nm across its entire imaging area, often less than 50 nm for high-resolution work. Preparing a bulk object to those dimensions is a major undertaking, and in biological microscopy it consumes most of the effort: days of fixation, dehydration, resin embedding, and ultramicrotomy to produce 70 nm sections suitable for imaging. For materials science specimens — metals, semiconductors, ceramics — the thinning is done by mechanical grinding followed by ion milling, which can take a full day. The imaging itself may take an hour. The specimen preparation typically takes ten times as long.

That asymmetry between prep and imaging defines the practical economy of TEM: you do not reach for it unless the question genuinely requires what only it can give.

## What happens to the beam inside the specimen

Three things can happen to an electron as it traverses a thin TEM specimen.

The first is nothing particularly dramatic. The electron passes between the atoms, through the low-density interstices of the material, and arrives at the detector with essentially full energy and essentially unchanged direction. This is the **direct beam** — the unscattered electrons. In the default imaging mode, **bright-field**, the objective aperture is centered on the direct beam and excludes most scattered electrons. Regions where electrons passed through unscattered appear bright. Regions where they scattered appear darker. The image is a projection-shadow of the specimen's scattering distribution.

The second thing that can happen is **elastic scattering**: the electron interacts with an atomic nucleus and is deflected, sometimes by a large angle, without losing kinetic energy. The same process that produces backscattered electrons in the SEM (Chapter 6) here scatters the beam through the thin specimen. Heavy nuclei scatter more strongly than light ones — the elastic cross-section scales roughly as $Z^2$ — so a gold nanoparticle inside a carbon matrix appears darker than the surroundings in bright-field, not because the gold absorbs electrons but because it scatters them outside the aperture.

The third is **inelastic scattering**: the electron interacts with a bound electron in the specimen, transfers energy, and continues with reduced kinetic energy. This produces characteristic X-rays (detectable by EDS, as in Chapter 9) and also excites plasmons, phonons, and valence electrons in ways that the energy-loss spectrum can decode (Chapter 18, EELS). Inelastic scattering also slows the beam and, in soft materials, breaks chemical bonds — the beam damage problem that haunts biological TEM.

The reason the specimen must be thin is not that electrons at 200 kV cannot penetrate further. They can penetrate several micrometers in most materials before stopping. The thinness requirement comes from image quality. In a thick specimen, each electron scatters many times before exiting. The directions randomize. The image becomes a diffuse smear with no contrast and no spatial information. The depth of field at high magnification means that features at different depths contribute simultaneously to the projected image, blurring fine detail. The 100 nm limit is the empirical point at which the single-scattering approximation — one electron, one scattering event, predictable exit angle — holds well enough to interpret the image. Below that thickness, the image is meaningful. Above it, interpretation becomes increasingly unreliable.

## The image is a projection

This point deserves its own emphasis because it is the most consequential difference between TEM and SEM for how you read images.

An SEM image is a surface map. Each pixel corresponds to a specific location on the specimen surface, and the signal comes from a known depth range in the interaction volume. You can think of the image as a bird's-eye photograph of the surface, with topographic shading from the secondary electron yield.

A TEM image is a projection through the full thickness of the specimen. Every electron that reaches the detector has traveled through the entire specimen from entrance face to exit face, scattering at various depths along the way. The final image superimposes all of those scattering events. A spherical nanoparticle and a disk viewed edge-on can look identical in a single TEM image because both project to the same circular shadow. A particle that appears solid might be hollow if viewed from the right angle; a particle that appears hollow might be solid viewed from the wrong angle.

This projection ambiguity is not a flaw in the instrument. It is a geometric consequence of imaging a three-dimensional object with a two-dimensional projection. The TEM knows this and has a solution: tilt the specimen and collect images from multiple angles, then reconstruct the three-dimensional structure computationally. That technique — electron tomography — is Chapter 19. For a single image, the rule is: suspect projection artifacts, tilt when you can, and interpret cautiously.

The practical consequence is that TEM images require interpretation in a way that SEM images do not. An SEM image of a nanoparticle population looks like a photograph — you see the shapes, you count them, you measure them. A TEM image of the same population projects the three-dimensional structure onto a two-dimensional plane, and interpreting that projection requires understanding what the projection contains.

## What the numbers look like

At 200 kV, the electron wavelength is about 2.5 pm. The theoretical resolution limit from diffraction is therefore on the order of the wavelength — sub-angstrom. The actual limit is set by lens aberrations, primarily spherical aberration of the objective lens ($C_s$), and by chromatic aberration from the energy spread of the gun. In a well-aligned modern instrument with aberration correction, routine information limit is below 0.1 nm. Atomic columns in silicon, spaced 0.136 nm apart in the ⟨110⟩ projection, are separately resolvable. Columns in gold, spaced 0.204 nm, are very comfortably resolved.

The magnification range spans from about 1,000× (useful for survey imaging, comparable to the low end of an optical microscope) to over 1,000,000× (high-resolution lattice imaging of atomic columns). In practice, most imaging happens between 10,000× and 200,000×, covering features from a few micrometers down to a few nanometers.

The field of view scales inversely with magnification. At 50,000×, a typical TEM camera captures roughly 2 μm × 2 μm. At 200,000×, that shrinks to 500 nm × 500 nm. This is the sampling problem of TEM: to image with sufficient resolution to see what you came to see, you accept a field of view so small that any single image is a tiny sample of the specimen. The standard practice — and the one that produces credible science — is to survey at low magnification to find representative regions, image those regions at high magnification, and report enough fields to establish that the high-magnification images are not outliers.

## Why the energy matters

The choice of accelerating voltage in TEM is a genuine trade, unlike in SEM where higher kV mostly means more interaction volume.

Higher kV gives shorter wavelength — better diffraction-limited resolution. It also gives greater penetrating power, which allows slightly thicker specimens. But higher kV also increases the probability of **knock-on damage**: a 300 kV electron can transfer enough momentum to a nucleus in a collision to displace it from its lattice site, creating a vacancy-interstitial pair. In light elements — carbon, nitrogen, oxygen — the displacement threshold is low, and biological and organic specimens become structurally altered during imaging at high kV.

Lower kV reduces knock-on damage but worsens the wavelength limit and reduces the specimen's effective transparency. The biological TEM community has largely standardized on 80–120 kV as a practical compromise. High-resolution materials work runs at 200–300 kV, accepting the radiation damage risk on inorganic specimens that are generally more robust.

The cryo-EM revolution that produced atomic-resolution protein structures was enabled partly by dose-fractionation — collecting movies of the specimen rather than single exposures, then averaging many particles across many frames to build up signal while keeping dose per frame low. That technique requires direct-detection cameras with fast frame rates and high quantum efficiency. The combination of cryo-preparation (Chapter 21), direct-detection cameras, and computational particle averaging took the technique from near-single-molecule resolution at 0.3 nm in the 2010s to 0.15 nm and below by the early 2020s.

## Where TEM lives in the technique landscape

The choice between TEM and SEM is, in most cases, a choice determined by the question rather than by convenience.

Surface morphology of a bulk specimen — SEM. Fast, low prep, large field of view, rugged imaging conditions. Tissue-scale anatomy, powder particle shape, fracture surface characterization, integrated circuit defect survey — all SEM first.

Internal structure at sub-nanometer resolution — TEM. Mitochondrial ultrastructure, nanoparticle interior, semiconductor multilayer cross-section, protein complex, grain boundary atomic structure — TEM only.

Crystallographic structure — TEM. Selected-area electron diffraction from a 100 nm region gives a single-crystal diffraction pattern that identifies phase, orientation, and lattice parameters directly. X-ray diffraction gives bulk-averaged patterns; TEM gives local, site-specific ones.

Analytical chemistry at high spatial resolution — both. EDS maps at 1 μm resolution in SEM; EDS maps at 2 nm resolution in STEM mode on a TEM; EELS at near-atomic spatial resolution for light-element chemistry in TEM. The question is spatial resolution: if you need better than a few hundred nanometers on composition, you need TEM.

The overlap zone is real. A 30 nm particle in SEM with a field-emission gun at low kV and a TTL detector gives good morphological information. The same particle in TEM at 200 kV gives better morphological information and also tells you whether the particle is crystalline, what phase it is, and whether its interior matches its exterior. If you have the TEM access and the time to prep, TEM gives more. If you do not, SEM gives quite a lot.

The decision hierarchy that works in practice: start with the question, determine what information is required, choose the coarsest technique that provides it. Optical microscopy for anything above ~200 nm. SEM for surface features above ~1 nm. TEM for internal structure, sub-nanometer features, crystallography, or high-resolution analytical chemistry. Cryo-EM for biological structures in near-native state. Tomography when the 2D projection ambiguity is unacceptable.

## The instrument, briefly

Chapter 13 will walk the TEM column from gun to camera in full. A brief orientation here.

The TEM column is vertical, with the beam traveling downward. The gun at the top generates the high-energy electron beam — field-emission guns in modern instruments, at 200 or 300 kV. Below the gun, a condenser lens system spreads the beam to illuminate the specimen with a controlled beam diameter and angle. The specimen sits in the objective lens — not below it, as in SEM, but inside the lens field, which is why TEM objective lenses have very small $C_s$ values and can achieve diffraction-limited resolution near the atomic scale.

Below the specimen, the objective lens forms the first image of the transmitted beam (in imaging mode) or the first diffraction pattern (in diffraction mode). Intermediate lenses then magnify either the image or the diffraction pattern and project it to the final projector lens, which places it on the detector. Modern TEMs use direct-detection CMOS cameras; older instruments used CCD cameras and, before that, photographic film.

The operator switches between imaging mode and diffraction mode by changing the intermediate lens excitation — a matter of pressing a button. The same region of specimen can be imaged at 50,000× and then immediately examined by selected-area diffraction to determine the crystal structure, without moving the specimen.

That combination — atomic-resolution image and site-specific diffraction from the same 100 nm region — is what makes TEM the workhorse of materials characterization at the nanoscale. The SEM tells you what is there and what it looks like. The TEM tells you what it is made of, how it is arranged atom by atom, and what defects it carries.

De Broglie wrote a nine-page thesis appendix sketching what would follow from his wavelength relation. He did not have a working vacuum system, a high-voltage source, or a magnetic lens. He had a mathematical argument. Fourteen years later, Ruska had an instrument. The resolution was 10 nm. Today it is 0.1 nm. The physics was correct; the engineering took time.

---

*What would change my mind:* evidence that the thin-specimen requirement could be substantially relaxed — to, say, 1 μm — without sacrificing atomic-resolution imaging. High-voltage TEMs at 1–3 MV extend the limit somewhat, but the fundamental contrast-and-multiple-scattering argument holds across the practical accelerating voltage range.

*Still puzzling:* the gap between specimen-preparation effort and imaging time remains stubbornly large in biological TEM. A typical session is at least 10:1 prep-to-imaging. Cryo-EM vitrification and fast-prep methods have helped at one end of the problem; the ultramicrotomy bottleneck for sectioned specimens has not changed fundamentally in fifty years.

