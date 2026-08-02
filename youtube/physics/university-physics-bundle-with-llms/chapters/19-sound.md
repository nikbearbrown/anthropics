# Chapter 19 — Sound

## Alternative titles

1. **Sound: The Longitudinal Wave the Human Ear Evolved to Hear**
2. **From Felix Baumgartner to Submarines: How Sound Carries Information at 343 Meters Per Second**
3. **Pressure Waves, Doppler Shifts, and the Physics of Why an Ambulance's Siren Changes Pitch**

---

## TL;DR

Sound is a longitudinal pressure wave traveling through a medium at speeds that depend on how rigid and how dense the material is. The human ear evolved to detect frequencies from 20 Hz to 20 kHz; intensity and intensity level explain why a whisper is tolerable but a rock concert can rupture an eardrum. The Doppler effect tells us what frequency we actually hear when a sound source moves toward or away from us — a fact that ER doctors rely on to know which ambulance is which, and one that led to a full understanding of how galaxies are moving through space.

---

## Opening Hook

**October 14, 2012. Felix Baumgartner is 39 kilometers above Earth, in a capsule smaller than a closet, wearing a spacesuit and breathing supplemental oxygen.** He checks the altimeter one more time. The jump is go. He steps out the door.

For 43 seconds he falls in near vacuum. Then, at about 37 kilometers altitude, as his velocity reaches 1,357 kilometers per hour (Mach 1.25), something dramatic happens: the air becomes thick enough that he outruns the sound he is creating. The pressure waves he generates cannot propagate ahead of him anymore. They pile up behind him like traffic backing up at a toll booth. The air compresses. A cone-shaped shock wave forms around his falling body — a visible Mach cone of compressed air, moisture, and dust.

He has become a supersonic object. The shock wave is real, visible on the video footage. It is the physical manifestation of the Doppler effect taken to its extreme: when you move faster than the speed of sound itself, the wave phenomenon reverses, inverts, and becomes something altogether more violent than any frequency shift an ambulance siren could produce.

That moment — when an object outruns sound — is the full realization of a principle that governs nearly everything in this chapter. Sound is not magic. Sound is not mysterious. Sound is a compression wave in a medium, traveling at a speed determined entirely by how stiff the medium is and how much mass it has. Understand the wave speed, understand the medium's density, and you understand why sound travels at 343 m/s in air at 20°C, 1480 m/s in water, and 5960 m/s in steel. Understand the Doppler effect, and you understand why a submarine's sonar operator knows the distance to a submerged wreck by timing the echo, and why an emergency room doctor can tell whether an ambulance is getting closer or farther away by the pitch of the siren. And understand what happens when you exceed that speed, and you understand why Felix Baumgartner's body generated a visible shock wave — and why the SR-71 Blackbird can cruise at Mach 2.85 without the structure tearing itself apart, despite what 1960s skeptics said was impossible.

This is the final chapter of the mechanics sequence. The book opened with units and dimensional analysis, moved through vectors and kinematics and the laws of motion, climbed through energy and momentum and rotation, descended into gravity, spiraled into fluids and oscillations and waves. Now, at the end, we are watching a student's own body become a measurement instrument for one of the most consequential wave phenomena in nature — one that governs not just the behavior of sound, but the motion of light from distant galaxies, the expansion of the universe itself, and the detection of gravitational waves that let us "hear" the collision of black holes billions of light-years away.

Let's understand how.

---

### Learning Objectives

By the end of this chapter you will be able to:

- **Represent** sound as a longitudinal pressure wave and explain why it travels at different speeds in different media.
- **Calculate** the speed of sound in air, water, or a solid from the elastic and inertial properties of the medium, and how temperature affects sound speed in gases.
- **Define and use** the decibel intensity level scale and explain why it is logarithmic rather than linear.
- **Analyze** constructive and destructive interference of sound waves and apply them to noise cancellation and musical instrument design.
- **Compute** resonant frequencies in tubes (open at both ends, or closed at one end) and explain how instruments use these to produce their characteristic pitches.
- **Apply** the Doppler effect formulas to moving sources and moving observers, and explain what happens when a source exceeds the speed of sound.

### Prerequisites

- Chapters 15–18 (oscillations, waves, traveling waves, standing waves, superposition)
- Ability to work with logarithms: $\log(ab) = \log a + \log b$, and $10^x$ functions
- Comfort with Greek letters ($\omega$, $\lambda$, $\rho$) and partial derivatives $\frac{\partial}{\partial x}$, $\frac{\partial}{\partial t}$

### Why This Chapter Matters

Sound is the only wave phenomenon that humans evolved a dedicated sense organ to detect. The physics of sound touches neuroscience (how the cochlea converts pressure into neural signals), medicine (ultrasound imaging, Doppler echocardiography), engineering (noise reduction, acoustics of concert halls), seismology (using earthquake waves to map Earth's interior), astronomy (redshift of distant galaxies), and the detection of gravitational waves. The concepts here — traveling waves, resonance, the Doppler effect — reappear in electromagnetics, optics, and quantum mechanics. This chapter is where you see those abstract concepts take on a form you can hear and measure.

---

## Concept 1 — Sound as a Longitudinal Pressure Wave

**The physical phenomenon of sound is a disturbance of matter transmitted outward from a source.** Hearing is what your brain does when it receives that disturbance and interprets it. They are not the same thing. A tree falling in the forest makes a pressure wave whether anyone is there or not; the hearing is the perception that happens if an ear is present to receive it.

When a speaker cone vibrates back and forth, it pushes against the air molecules next to it, compressing them. As the cone moves in the opposite direction, those molecules are free to expand again. The compressions move outward as spherical wavefronts, each successive compression separated from the next by a distance equal to one wavelength. Between the compressions are rarefactions — regions of lower-than-average pressure where the air is less dense. 

Because the oscillation is parallel to the direction of wave propagation (back-and-forth motion in the same line the wave travels), sound is a **longitudinal wave**. This is different from water waves or waves on a string, where the oscillation is perpendicular to the propagation direction (transverse waves).

In a fluid, only longitudinal waves propagate easily, because fluids have almost no shear strength — no resistance to being deformed sideways. Solids, by contrast, can sustain both longitudinal waves (compressions) and transverse waves (shearing), and they travel at different speeds in the same material.

### Models for Sound: Pressure and Displacement

Sound can be modeled two ways. The **pressure model** describes how pressure varies with position and time:

$$\Delta P(x,t) = \Delta P_{\max} \sin(kx - \omega t + \phi)$$

where $\Delta P$ is the change in pressure from the ambient, $\Delta P_{\max}$ is the maximum pressure change (in pascals), $k = \frac{2\pi}{\lambda}$ is the wave number, and $\omega = 2\pi f$ is the angular frequency.

The **displacement model** describes the position of air molecules:

$$s(x,t) = s_{\max} \cos(kx - \omega t + \phi)$$

where $s$ is the displacement from equilibrium and $s_{\max}$ is the maximum displacement.

Notice that displacement lags pressure by 90°: when pressure is maximum (maximum compression), the displacement is zero (molecules have moved as far as they can and are momentarily stationary); when displacement is maximum, pressure is zero (molecules are farthest from equilibrium but pressure has returned to normal).

Both models describe the same phenomenon. The pressure model is more practical for measurement — we can measure pressure with a microphone. The displacement model is more useful for understanding the mechanism — it shows what's actually happening to the medium.

### The Speed of Sound in Different Media

Here is one of the most important facts in acoustics: **the speed of sound in any medium depends on two things and two things only: how stiff the medium is and how much mass it has.**

For any mechanical wave in a medium:

$$v = \sqrt{\frac{\text{elastic property}}{\text{inertial property}}}$$

For sound in a **fluid** (liquid or gas), the elastic property is the bulk modulus $B$, which measures how incompressible the fluid is:

$$v = \sqrt{\frac{B}{\rho}}$$

For sound in a **solid**, the elastic property is Young's modulus $Y$:

$$v = \sqrt{\frac{Y}{\rho}}$$

where $\rho$ is the density in both cases.

For sound in an **ideal gas**, we use the adiabatic index $\gamma$ (gamma), the gas constant $R$, temperature $T_K$ in kelvins, and molar mass $M$:

$$v = \sqrt{\frac{\gamma RT_K}{M}}$$

Let's check this against reality. At 0°C, the speed of sound in air is 331 m/s. At 20°C (293 K), it is 343 m/s. The formula predicts:

$$v = (331 \text{ m/s}) \sqrt{\frac{T_K}{273 \text{ K}}} = (331 \text{ m/s}) \sqrt{\frac{293}{273}} = 343 \text{ m/s}$$

It matches perfectly.

Notice what the gas formula tells us: **sound travels faster in hotter gas** (temperature increases) and **slower in heavier gas** (larger $M$). This is why a helium balloon, filled with a light gas, generates a higher pitch when you inhale and speak into it — the sound travels faster in helium than in air, and faster sound in the same vocal cavity means higher frequency.

Here is a table of sound speeds across media:

| Medium | Condition | $v$ (m/s) |
|--------|-----------|-----------|
| **Air** | 0°C | 331 |
| **Air** | 20°C | 343 |
| **Water** | Fresh, 20°C | 1480 |
| **Water** | Seawater, 20°C | 1540 |
| **Steel** | Longitudinal | 5960 |
| **Glass (Pyrex)** | — | 5640 |
| **Marble** | — | 3810 |
| **Rubber** | Vulcanized | 54 |

The pattern is clear: **the more rigid the material (higher $Y$ or $B$) and the less dense it is, the faster sound travels.** Steel, which is quite rigid and not particularly dense, wins. Water is faster than air by a factor of 4 because it is much less compressible, despite being denser. Rubber is nearly as slow as air because it is so easily compressed, even though it's far denser — the low rigidity dominates.

### Why Temperature Matters (and Why Musicians Care)

In gases, sound speed depends on temperature. In air, the relationship is:

$$v = 331 \frac{\text{m}}{\text{s}} \sqrt{1 + \frac{T_C}{273°C}} \quad \text{or} \quad v = 331 \frac{\text{m}}{\text{s}} \sqrt{\frac{T_K}{273 \text{ K}}}$$

where $T_C$ is in Celsius and $T_K$ is in kelvins.

The dependence is not strong (less than 4% change from 0°C to 20°C), but it matters. A wind instrument whose fundamental frequency depends on $f = \frac{v}{2L}$ (for a tube open at both ends) will sound sharp if brought into a warm room and flat if carried into a cold one. This is why musicians warm up their instruments before playing. A 1°C increase raises sound speed by about 0.2%, which shifts frequency by 0.2% — barely noticeable to most ears, but measurable and annoying to professionals.

### The Audible Range and Nomenclature

The human ear is sensitive to frequencies roughly between **20 Hz and 20 kHz** (20,000 Hz), though this range shrinks with age. Sounds below 20 Hz are called **infrasound** — elephants use these for long-distance communication. Sounds above 20 kHz are called **ultrasound** — bats and dolphins use ultrasound for echolocation; humans use ultrasound in medical imaging (safe because it doesn't ionize, unlike X-rays) and in nondestructive testing to find flaws in materials.

### Worked Example — Speed of Sound in Air at Temperature

A meteorologist measures the speed of sound in the Sahara Desert where the air temperature is 56°C. What is the sound speed?

**Given:** $T_C = 56°C$, so $T_K = 56 + 273 = 329 \text{ K}$

**Find:** $v$ using the temperature-dependent formula

**Solution:**

$$v = 331 \frac{\text{m}}{\text{s}} \sqrt{\frac{329 \text{ K}}{273 \text{ K}}} = 331 \sqrt{1.205} = 331 \times 1.098 = 363 \text{ m/s}$$

**Check against intuition:** 56°C is about 100°F — hot, but not impossibly so. A 20°C increase from the reference (0°C) is expected to raise sound speed by about 20 × 0.2% = 4%, or about 13 m/s. We have 363 − 331 = 32 m/s, which is about 10%. This is higher than the rough estimate; the relationship is nonlinear. The formula is right; the rough estimate was too linear.

**General lesson:** temperature affects gas sound speeds measurably. In liquids and solids, temperature effects are much smaller because the elastic properties are much less sensitive to temperature than gas pressures are.

### Common Misconceptions

**"Sound is faster in denser media."** Not always. Rubber is denser than air, but sound is slower in rubber. What matters is the ratio $\sqrt{\frac{\text{elastic property}}{\text{density}}}$. Water is denser than air but sound is 4 times faster in water because water is far less compressible.

**"Sound will travel through anything."** Not so. In a true vacuum, there are no molecules to compress, so sound cannot propagate. The phrase "in the vacuum of space, no one can hear you scream" is literally true.

**"Higher frequency sound travels faster."** False. In most media, sound speed is nearly independent of frequency — all frequencies travel at the same speed. This independence is what allows a band to play in a distant stadium and have the low and high notes arrive in the correct order. If high frequencies were faster, the high notes would arrive first and the music would sound like gibberish.

---

## Concept 2 — Intensity, Decibels, and Why We Use Logarithms

**The intensity of a wave is the power per unit area it carries.** For sound:

$$I = \frac{\langle P \rangle}{A}$$

where $\langle P \rangle$ is the time-averaged power and $A$ is the area over which it is spread. Units: watts per square meter (W/m²).

As a spherical sound wave spreads outward from a point source, the power is conserved but the area increases. At distance $r_1$, the power is spread over a sphere of area $4\pi r_1^2$. At distance $r_2$, it is spread over $4\pi r_2^2$. Thus:

$$I_2 = I_1 \left(\frac{r_1}{r_2}\right)^2$$

This is the **inverse square law**: intensity falls as the inverse of the square of the distance. Double the distance, and intensity drops to one-quarter.

### The Intensity-Amplitude Relationship

The intensity of a sound wave is related to the pressure amplitude:

$$I = \frac{(\Delta P_{\max})^2}{2\rho v}$$

where $\Delta P_{\max}$ is the maximum pressure change, $\rho$ is the medium density, and $v$ is the sound speed. 

This makes physical sense: higher pressure amplitude means more vigorous oscillation, so more energy. The dependence on $(\Delta P_{\max})^2$ reflects the fact that kinetic energy goes as the square of velocity — greater amplitude means molecules move faster, so they carry more energy.

### The Problem: A Range of 12 Orders of Magnitude

The human ear can detect sound intensities ranging from $10^{-12}$ W/m² (the quietest sound a person with normal hearing can perceive) to about 1 W/m² (where pain begins). That is a range of a trillion to one.

If we tried to measure and report sound in raw watts per square meter, we'd be writing numbers like:
- Threshold of hearing: $1 \times 10^{-12}$ W/m²
- Whisper at 1 meter: $1 \times 10^{-10}$ W/m²
- Normal conversation: $1 \times 10^{-6}$ W/m²
- Rock concert: 1 W/m²

The numbers are unwieldy. More important, **they don't reflect how the ear perceives loudness.** If you double the intensity of a sound, it doesn't sound twice as loud to your ear — it sounds only slightly louder. This is the signature of a logarithmic response.

### The Decibel Scale

The **sound intensity level** $\beta$, measured in **decibels** (dB), is defined as:

$$\beta(\text{dB}) = 10 \log_{10}\left(\frac{I}{I_0}\right)$$

where $I_0 = 10^{-12}$ W/m² is the reference intensity (the threshold of hearing at 1 kHz).

This scale has several virtues:

1. **Compresses the range.** Instead of writing $10^{-12}$ to $10^0$, we write 0 to 120 dB. A factor of 10 in intensity becomes a difference of 10 dB. A trillion-fold range becomes 120 dB.

2. **Reflects human perception.** The logarithmic scale matches how the ear responds. Each tenfold increase in intensity is heard as a similar perceptual increment in loudness.

3. **Makes addition intuitive.** If you have two equally loud sources, the combined intensity is twice the individual intensity. But the combined decibel level is only 10 log₁₀(2) ≈ 3 dB higher — a rule so common that sound technicians use it without thinking.

Here is a reference table:

| Source | $\beta$ (dB) | $I$ (W/m²) | Observation |
|--------|-------------|-----------|-------------|
| Threshold of hearing | 0 | $10^{-12}$ | Barely detectable |
| Whisper at 1 m | 20 | $10^{-10}$ | Very quiet |
| Normal conversation | 60 | $10^{-6}$ | Comfortable |
| Busy traffic | 70 | $10^{-5}$ | Noisy |
| Loud alarm | 80 | $10^{-4}$ | Painful prolonged |
| Loud rock concert | 110 | $10^{-1}$ | Damage risk, short term |
| Threshold of pain | 120 | 1 | Immediate damage |
| Jet airplane at 30 m | 140 | $10^2$ | Severe damage, seconds |

### Worked Example — Decibel Level of a Pressure Wave

A sound wave in air has a pressure amplitude of 0.656 Pa. Find the sound intensity level in decibels.

**Given:** $\Delta P_{\max} = 0.656 \text{ Pa}$, air at 0°C: $\rho = 1.29$ kg/m³, $v = 331$ m/s

**Find:** $\beta$ (dB)

**Solution:**

First, find the intensity from $I = \frac{(\Delta P_{\max})^2}{2\rho v}$:

$$I = \frac{(0.656)^2}{2(1.29)(331)} = \frac{0.430}{852.98} = 5.04 \times 10^{-4} \text{ W/m}^2$$

Now find the decibel level:

$$\beta = 10 \log_{10}\left(\frac{5.04 \times 10^{-4}}{10^{-12}}\right) = 10 \log_{10}(5.04 \times 10^8) = 10(8.70) = 87 \text{ dB}$$

**Check:** An 87 dB sound is loud — like a busy restaurant or noisy office. A pressure amplitude of 0.656 Pa is noticeable but not painful. The result is reasonable.

**General lesson:** translating between pressure amplitude and decibel level requires knowing the medium's density and sound speed. The formula connects a microscopic quantity (how much individual air molecules are pushed around) to a macroscopic measurement (what a decibel meter reports).

### Why Not Linear? The Weber-Fechner Law

The decibel scale is logarithmic because the human ear is logarithmic. The **Weber-Fechner law** states that the perceived magnitude of a sensory stimulus is proportional to the logarithm of the stimulus intensity. In other words:

$$\text{Perceived loudness} \propto \log(I)$$

This is why a 3 dB increase (a doubling of intensity) sounds like a noticeable but not dramatic change. A 10 dB increase (a tenfold increase) sounds roughly twice as loud to the ear.

This logarithmic response is not unique to hearing. Vision, touch, smell — they all follow this pattern. It allows organisms to detect a very wide range of stimuli (from barely detectable to painfully intense) with a single sensory organ. If ears were linear, we could either hear whispers or hear gunshots, but not both — we'd have to choose.

### Common Misconceptions

**"Doubling the volume doubles the loudness."** If you see "volume" as intensity, this is false — doubling intensity adds only 3 dB. If you mean "perceived loudness," the relationship is logarithmic.

**"The decibel scale only goes up to 120 dB."** No. Intensities higher than 1 W/m² produce decibel levels above 120 dB. A jet engine at close range can exceed 140 dB.

**"Decibels measure loudness."** Decibels measure intensity level. Loudness is the perceptual response, which depends on frequency, duration, and individual hearing sensitivity.

---

## Concept 3 — The Doppler Effect and Shock Waves

**The Doppler effect is an alteration in the observed frequency of a sound due to relative motion between the source and the observer.**

You experience this constantly: an ambulance siren shifts from a high pitch as it approaches to a lower pitch after it passes. The siren is emitting a constant frequency, but what you hear changes. The **Doppler shift** is the actual change in frequency.

### Physical Cause: Wave Bunching and Stretching

Imagine a sound source moving toward you at constant velocity $v_s$ less than the speed of sound. The source emits successive wavefronts at regular intervals. But because the source is moving toward you, each new wavefront is emitted from a point slightly closer to you than the previous one. The wavefronts are closer together in front of the source than they would be if the source were stationary.

Wavelength is the distance between successive wavefronts. If the wavefronts are bunched up, the wavelength is shorter. Since $v = f\lambda$ and $v$ (the speed of sound in air) is constant, a shorter wavelength means a higher frequency.

Behind the moving source, the opposite happens: the wavefronts are stretched out, wavelength is longer, and frequency is lower.

This explains the siren shift without invoking anything mystical — it's just geometry and the wave equation.

### Doppler Shift Formulas: Source Moving, Observer Stationary

When a source moves toward a stationary observer at speed $v_s$ (where $v_s < v$, the speed of sound):

$$f_o = f_s \left(\frac{v}{v - v_s}\right)$$

When the source moves away:

$$f_o = f_s \left(\frac{v}{v + v_s}\right)$$

where $f_o$ is the observed frequency, $f_s$ is the source frequency, $v$ is the sound speed, and $v_s$ is the source speed.

### Doppler Shift Formulas: Observer Moving, Source Stationary

When an observer moves toward a stationary source at speed $v_o$:

$$f_o = f_s \left(\frac{v + v_o}{v}\right)$$

When the observer moves away:

$$f_o = f_s \left(\frac{v - v_o}{v}\right)$$

### Unified Formula: Both Source and Observer Moving

When both source and observer are moving:

$$f_o = f_s \left(\frac{v \pm v_o}{v \mp v_s}\right)$$

where the top signs apply for approaching motion and the bottom signs for receding motion.

**Critical insight:** the effect is not symmetric. If a source moves toward you at 10 m/s, the frequency shift is not the same as if you move toward a stationary source at 10 m/s. This asymmetry is subtle but real, and it teaches us something deep: there is a preferred reference frame — the medium itself. Motion relative to the air matters, not just relative to each other.

### Worked Example — Ambulance Siren

A speeding ambulance approaches at 30 m/s with a siren frequency of 1000 Hz. The speed of sound on this day is 343 m/s. What frequency does a stationary observer hear?

**Given:** $f_s = 1000$ Hz, $v_s = 30$ m/s (approaching), $v = 343$ m/s

**Find:** $f_o$ (observed frequency)

**Solution:** Use the source-approaching formula:

$$f_o = f_s \left(\frac{v}{v - v_s}\right) = 1000 \left(\frac{343}{343 - 30}\right) = 1000 \left(\frac{343}{313}\right) = 1000 \times 1.096 = 1096 \text{ Hz}$$

After the ambulance passes and recedes at 30 m/s:

$$f_o = f_s \left(\frac{v}{v + v_s}\right) = 1000 \left(\frac{343}{343 + 30}\right) = 1000 \left(\frac{343}{373}\right) = 1000 \times 0.920 = 920 \text{ Hz}$$

The shift is dramatic: from 1096 Hz to 920 Hz is a drop of 176 Hz, or about 16% — easily heard.

**Check against intuition:** A 30 m/s speed is about 67 mph, reasonable for an ambulance. The sound speed is 343 m/s, so the ambulance is moving at less than 10% the speed of sound. The frequency shift should be a few percent on either side of 1000 Hz. We have 1096 (9.6% high) and 920 (8% low). Reasonable.

**General lesson:** even at speeds much slower than sound speed, the Doppler effect is noticeable to the human ear, which can detect frequency changes of as little as 0.3%.

### Sonic Booms: When the Source Exceeds Sound Speed

Now suppose the source speed $v_s$ equals or exceeds the speed of sound $v$. The formula $f_o = f_s \left(\frac{v}{v - v_s}\right)$ predicts infinite frequency when $v_s = v$, and negative frequency when $v_s > v$. Negative frequency is nonsensical. What actually happens?

When $v_s = v$, the sound source moves at the speed of its own sound waves. No wave can get ahead of the source. All the compressions pile up at a single location — the source itself. The pressure builds to enormous values.

When $v_s > v$, the source outruns its sound. The sound waves behind the source do not interact with the source; instead, they form a cone-shaped disturbance called a **shock wave**, a constructive interference pattern of sound created by the object moving faster than sound.

The geometry is simple. Imagine the source moves a distance $v_s t$ in time $t$. In that same time, a sound wave travels $vt$. The angle $\theta$ of the shock wave cone satisfies:

$$\sin \theta = \frac{v}{v_s} = \frac{1}{M}$$

where $M = \frac{v_s}{v}$ is the **Mach number**.

At Mach 1.5, for example, $\sin \theta = 1/1.5 = 0.667$, so $\theta = 41.8°$. The shock wave forms a cone at an angle of about 42° behind the object.

### Sonic Booms Are Not "Breaking the Sound Barrier"

A **sonic boom** is the intense sound heard on the ground as the shock wave sweeps past. **This is a common misconception:** the sonic boom does not occur when the aircraft first reaches Mach 1. It occurs when the shock wave reaches the observer — which is continuously as the aircraft flies at supersonic speed. An aircraft flying at Mach 2 at constant altitude generates a shock wave that sweeps along the ground in a cone trailing the aircraft. Observers within that cone hear a continuous rumble; those outside hear nothing until the shock wave reaches them, at which point they hear a sudden loud boom.

For this reason, supersonic aircraft are restricted in where they can fly at full speed. The shock wave pressure can be severe enough to break windows and disturb populations on the ground.

### Bow Wakes

The shock wave is a special case of a broader phenomenon: whenever an object moves through a medium faster than waves can propagate in that medium, a **bow wake** forms. 

A boat moving faster than water waves forms the familiar V-shaped wake behind it. 

A charged particle moving through a medium (such as water) faster than light travels through that medium forms a cone of **Cerenkov radiation** — actual light emitted as the particle's electromagnetic field "piles up" in a conical shock wave. This was how Cerenkov discovered that particles could travel faster than light through a medium (though never faster than light in vacuum). The phenomenon is used in particle detectors to identify particle types.

### Common Misconceptions

**"The Doppler effect is symmetric between source and observer."** False. A source moving toward you at $v_s$ produces a different frequency shift than you moving toward a stationary source at $v_s$. The asymmetry reflects the fact that the medium (air) defines a preferred frame of reference.

**"Sonic booms only happen once, when breaking the sound barrier."** False. A supersonic aircraft produces a continuous shock wave as long as it travels faster than sound. The boom heard on the ground occurs as the shock wave sweeps past.

**"Negative frequency means the sound reverses direction."** The negative frequency in the Doppler formula when $v_s > v$ is a sign that the formula breaks down. The physics changes fundamentally — the Doppler effect as we derived it no longer applies. A shock wave is a different phenomenon.

---

## Concept 4 — Interference, Resonance, and Musical Sound

*[This section synthesizes standing waves from Chapter 18 and applies them specifically to sound.]*

Sound is the only wave phenomenon that humans evolved a dedicated sense organ to detect. That evolutionary investment reflects an important fact: **sound carries a lot of information, and a lot of that information is encoded in resonance and standing wave patterns.**

### Interference of Sound Waves: From Noise Cancellation to Silence

When two sound waves overlap, they interfere — constructively if they are in phase, destructively if they are out of phase.

**Destructive interference is the basis for noise-canceling headphones.** A microphone on the outside of the earcup picks up ambient noise (say, airplane engine roar). A circuit analyzes the sound, generates a copy that is 180° out of phase, and plays that inverted sound through the speaker. Inside the earcup, the original noise and the inverted copy interfere destructively. The result can be a 30 dB reduction in noise — a thousandfold decrease in intensity.

This only works well for steady, low-frequency noise (aircraft engines, for instance). Higher frequencies and transient sounds (voices) are harder to cancel because the path length from the microphone to the earcup can vary, throwing off the phase cancellation.

### Standing Waves in Tubes: The Physics of Wind Instruments

Wind instruments (flute, oboe, clarinet, saxophone, trombone, trumpet) can be modeled as tubes with specific boundary conditions. At a closed end, air molecules cannot move far — a **node** forms (zero displacement). At an open end, molecules are free to move — an **antinode** forms (maximum displacement).

**Case 1: Tube Closed at One End, Open at the Other**

The fundamental frequency has a single node at the closed end and an antinode at the open end. The distance from node to antinode is one quarter of a wavelength:

$$\lambda_1 = 4L$$

where $L$ is the tube length. Thus:

$$f_1 = \frac{v}{4L}$$

The first overtone (next resonance) has three nodes and two antinodes, fitting $3\lambda_3/4 = L$, or $\lambda_3 = 4L/3$:

$$f_3 = 3\frac{v}{4L}$$

Higher overtones are $f_5, f_7, f_9, \ldots$ — only odd harmonics. This is why a tube closed at one end (like a clarinet) sounds different from a tube open at both ends (like a flute): different harmonic content.

The general formula is:

$$f_n = n\frac{v}{4L}, \quad n = 1, 3, 5, \ldots$$

**Case 2: Tube Open at Both Ends**

Both ends have antinodes. The fundamental has a single node in the middle and antinodes at the ends. One half wavelength fits in the tube:

$$\lambda_1 = 2L, \quad f_1 = \frac{v}{2L}$$

The first overtone fits a full wavelength:

$$f_2 = 2\frac{v}{2L}$$

All harmonics are present:

$$f_n = n\frac{v}{2L}, \quad n = 1, 2, 3, \ldots$$

An open tube produces a richer harmonic series than a closed tube.

### Timbre: Why a Violin and a Piano Sound Different on the Same Note

When a violin and a piano both play middle C, they emit the same fundamental frequency. But they sound completely different. Why?

**Timbre** (pronounced "TAM-ber") — also called **tone quality** — is determined by the mix of overtones and their relative intensities. The fundamental carries the pitch, but the overtones carry the personality.

When a violin bow excites a string, the string vibrates in multiple modes simultaneously. The resonant sounding box amplifies some frequencies more than others, depending on the box's own resonant frequencies. A piano hammer strikes a string and lets it ring. The soundboard (the wooden plate attached to the strings) vibrates at resonances determined by its shape and mass. Each instrument has a characteristic harmonic fingerprint.

A trumpet and a clarinet playing the same written note produce the same fundamental, but the clarinet emphasizes odd harmonics (reflecting the closed-tube physics of its bore), while the trumpet produces a richer harmonic mixture. To an ear trained to distinguish them, they are unmistakable.

### Worked Example — Flute Fundamental Frequency

A flute (open at both ends) is 0.60 m long. What is its fundamental frequency when played in air at 20°C?

**Given:** $L = 0.60$ m, $T = 20°C$, so $v = 343$ m/s

**Find:** $f_1$

**Solution:** For a tube open at both ends:

$$f_1 = \frac{v}{2L} = \frac{343}{2(0.60)} = \frac{343}{1.20} = 286 \text{ Hz}$$

**Check:** 286 Hz is close to the musical note D4 (about 294 Hz). A 0.60 m flute is plausibly a concert flute. The calculation is reasonable.

**General lesson:** the fundamental frequency of a wind instrument scales inversely with length. Longer instruments produce lower pitches. A piccolo is short and shrill; a bassoon is long and deep.

### The End Correction

In real tubes, the effective acoustic length is slightly longer than the physical length because the sound wave doesn't entirely fit inside the tube — it bulges out a bit at the open end before fully radiating away. An **end correction**, roughly 0.6 times the tube radius, should be added to the physical length.

For a thin-walled tube of radius $r$:

$$L_{\text{eff}} = L + 0.6r$$

This matters for precision tuning but is negligible for order-of-magnitude estimates.

### Common Misconceptions

**"A louder sound has more harmonics."** Not necessarily. Loudness (intensity) and harmonic content are independent. A soft note and a loud note on the same instrument may have identical harmonic distributions.

**"Harmonics are undesirable noise."** For musical instruments, harmonics are essential to the desired sound. They give an instrument its character. Electronic synthesizers that produce pure sine waves (single frequencies with no harmonics) sound thin and mechanical.

**"All wind instruments are tubes."** Approximately, yes, but the model is a simplification. The shape of the bore (conical vs. cylindrical), the material (wood vs. metal), and the presence of finger holes all affect the effective boundary conditions and resonances.

---

## Integration and Synthesis: A Return to Sound as a Window on the Universe

This chapter began with Felix Baumgartner falling from 39 kilometers, his body creating a visible shock wave as he exceeded the speed of sound.

It has taken us through the properties of sound in different media, the intensity and loudness scales that match human perception, the Doppler effect that explains everyday observations (sirens, train horns, the redshift of distant galaxies), and the resonances inside tubes that let us build instruments and hear music.

All of these concepts flow from a single principle: **sound is a mechanical wave governed by the wave equation.** The wave equation is universal — it describes vibrations in strings, oscillations in cavities, light waves in electromagnetic fields, and gravitational waves rippling through spacetime. What differs is the medium and the speed.

This is why the methods you learned in Chapter 18 (traveling waves, superposition, standing waves) apply to sound. And why they will apply again in your next physics course (electromagnetic waves and optics) and in every advanced course that follows.

The student who understands that a flute is a resonant cavity, that a shock wave is constructive interference of compressions, that the Doppler shift reflects the geometry of wave propagation in a preferred medium — that student has unlocked a framework that extends far beyond acoustics.

You have arrived at the end of the mechanics sequence. You have learned to measure motion, to predict forces, to conserve energy and momentum, to describe rotation and gravity and fluids and oscillations. Now you have watched all those concepts converge in a single phenomenon that you can hear.

In the next course — electricity and magnetism — light will be revealed as an electromagnetic wave. The same wave equation governs it. The same Doppler formula (with relativistic corrections) explains the redshift of galaxies and the blueshift of an approaching star. The same superposition principle lets light interfere with itself to produce diffraction patterns. The same resonance physics explains why a laser cavity produces coherent light, why a microwave oven heats food at a specific frequency, why your smartphone operates on bands allocated by the FCC.

The machinery does not change. Only the substance that oscillates.

---

## Graduated Exercises

### Warm-Up (Conceptual)

1. **Pressure vs. Displacement.** In a sound wave, when the pressure is at its maximum, is the displacement of air molecules at its maximum, minimum, or zero? Explain.

2. **Media Comparison.** Sound travels much faster in water than in air (about 4 times faster), even though water is denser. Why doesn't the higher density slow sound down?

3. **Decibel Direction.** Explain why a 10 dB sound is not "slightly louder" than a 0 dB sound, even though 10 is only slightly larger than 0.

4. **Doppler Asymmetry.** If you run toward a stationary speaker at 5 m/s, and the speaker plays a 440 Hz tone, you will hear a frequency shift. Is this shift the same as the shift you would hear if the speaker approached you at 5 m/s while you stood still? Why or why not?

### Application (Numerical)

5. **Speed of Sound in Different Gases.** At 20°C, the speed of sound in air is 343 m/s. Using the gas formula $v = \sqrt{\frac{\gamma RT_K}{M}}$, predict the speed of sound in helium (M = 4 g/mol) and in carbon dioxide (M = 44 g/mol). Both are at 20°C and have $\gamma$ ≈ 1.4 for diatomic gases or 1.67 for monatomic helium. (Note: CO₂ is triatomic but still approximately 1.3.)

6. **Inverse Square Law.** A speaker emits sound uniformly in all directions. At 1 meter away, the intensity is 0.1 W/m². What is the intensity at 5 meters away?

7. **From Decibels to Intensity.** A sound meter reads 85 dB. What is the intensity in W/m²?

8. **Doppler with Both Moving.** A fire truck siren has a frequency of 800 Hz. The truck approaches at 20 m/s. You are walking toward the truck at 2 m/s. The speed of sound is 340 m/s. What frequency do you hear? (Use the general Doppler formula.)

9. **Flute Design.** A flute player wants to lower the fundamental frequency by one octave (factor of 2). Should they lengthen the flute or shorten it? By what factor?

### Synthesis (Conceptual and Calculation)

10. **Shock Wave Angle.** An aircraft flies at Mach 1.8. What is the angle of the shock wave cone relative to the aircraft's direction of motion?

11. **Resonance in a Pipe.** A 50 cm long pipe is closed at one end. What are the first three resonant frequencies if the speed of sound is 343 m/s?

12. **Noise Cancellation Limits.** Noise-canceling headphones work well for low-frequency engine noise but poorly for speech. Explain why in terms of wavelength and path-length differences.

13. **Temperature and Instrument Tuning.** A clarinet (closed at one end, open at the other) is tuned to A₄ (440 Hz) at room temperature (20°C). If the musician takes it outside on a cold day (0°C), what frequency will it produce? (Assume the length stays constant.) What will the listener perceive?

14. **Putting It Together.** A bat emits echolocation clicks at 50 kHz. It flies toward a wall at 5 m/s. The speed of sound is 343 m/s. (a) What frequency does the wall "hear" (i.e., what frequency does the sound have when it hits the wall)? (b) This reflected sound travels back toward the moving bat. What frequency does the bat hear when the echo returns? (This is a Doppler shift in two stages: first the bat to the wall, then the wall to the bat.)

---

## Chapter Summary

**Sound is a longitudinal pressure wave that travels at a speed determined entirely by the elastic and inertial properties of the medium.** In air, this speed is 343 m/s at 20°C; it scales with temperature as $v = 331\sqrt{T_K/273}$ in kelvins.

**Intensity is power per unit area (W/m²).** Because human hearing spans a range of a trillion to one, we use a logarithmic scale, the decibel, defined as $\beta = 10 \log_{10}(I/I_0)$ where $I_0 = 10^{-12}$ W/m² is the threshold. This scale matches the logarithmic response of the human ear.

**When a source moves relative to an observer, the observed frequency shifts (Doppler effect).** For a source approaching a stationary observer, $f_o = f_s(v/(v - v_s))$; for a source receding, $f_o = f_s(v/(v + v_s))$. The effect arises because motion changes the wavelength and spacing of wave crests.

**When a source exceeds the speed of sound, constructive interference creates a shock wave** with a cone angle $\sin \theta = 1/M$ where $M$ is the Mach number. Sonic booms are not one-time events but the continuous shock wave sweeping past an observer.

**Standing waves in tubes create resonances.** A tube closed at one end resonates at frequencies $f_n = nv/(4L)$ for $n = 1, 3, 5, \ldots$ (odd harmonics only). A tube open at both ends resonates at $f_n = nv/(2L)$ for $n = 1, 2, 3, \ldots$ (all harmonics). This is how wind instruments work and why their harmonic content (and timbre) differs.

**Destructive interference of sound waves can cancel noise,** a principle used in active noise reduction headphones. Constructive and destructive interference are the basis of all acoustic phenomena from concert hall resonance to how the cochlea in your inner ear detects different frequencies.

---

## What Would Change My Reading

If it were established that the speed of sound in a given medium were *not* determined by its elastic modulus and density ratio, but instead depended significantly on frequency or source characteristics, this entire framework would need revision. (It does not — the speed-of-sound formula is one of the most robust in physics.)

---

## Still Puzzling

I do not yet fully understand why the human ear evolved sensitivity precisely to the 20 Hz to 20 kHz range. Infrasound (below 20 Hz) can be felt and carries information (elephant communication, earthquake warnings). Ultrasound (above 20 kHz) is used by many animals (bats, dolphins, rodents). Why this particular band? Is there something about primate predators or primate prey in our ancestral environment that selected for it?

---

## Tags

sound-waves, longitudinal-waves, doppler-effect, standing-waves, decibel-scale, acoustic-resonance, shock-waves, mach-number, supersonic-flight, wave-interference, noise-cancellation, wind-instruments, timbre, intensity-level, speed-of-sound


---

## LLM Exercise — Chapter 19: Doppler, Intensity, and the Toolkit Closes

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** Sound-intensity and decibel-level calculations, the Doppler effect simulated for moving sources and observers, shock-wave geometry, and the toolkit's final commit — a top-level README summarizing what 17 chapters of simulation built.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 19 task in the physics-simulation-toolkit. Final chapter.
Build sound-specific simulations, then commit the toolkit's capstone
README.

In `chapters/ch19_sound/`:

1. `simulations.py`:
   - `sound_intensity(power, distance, geometry='spherical' | 'plane')` —
     for a point source, $I = P / (4\pi r^2)$.
   - `intensity_level(intensity, reference=1e-12)` — sound-pressure
     level in decibels: $\beta = 10 \log_{10}(I/I_0)$.
   - `doppler_observed(f_source, v_sound, v_source, v_observer,
     direction)` — the four cases (source moving toward/away,
     observer moving toward/away) and the combined formula
     $f_o = f_s (v_s + v_o)/(v_s - v_{\text{source}})$ with sign
     conventions.
   - `mach_cone_half_angle(mach_number)` — $\sin\alpha = 1/M$ for
     $M > 1$.
   - `beat_frequency(f1, f2)` — $|f_1 - f_2|$, verified by
     superposition of two close-frequency traveling waves (Ch 18
     solver).

2. `test_simulations.py`:
   - Inverse-square law: doubling distance from a point source
     decreases intensity by factor of 4. Verify, in dB.
   - Threshold of hearing: 0 dB at 1 kHz. A jackhammer at 1 m emits
     around 110 dB. Compute the power emitted (the answer is around
     1 W — surprisingly small).
   - Doppler: a 1000 Hz source moving at 30 m/s toward a stationary
     observer. Verify the observed frequency formula numerically by
     simulating the source emitting pulses, the pulses traveling at
     speed of sound, and the observer's reception rate.
   - Mach cone: an airplane at Mach 2 produces a Mach cone with
     half-angle 30°. Verify the geometry.

3. `benchmarks.py` — simulate beat-frequency by adding two close-
   frequency traveling waves on the Ch 18 wave solver. Plot the
   envelope; verify the beat frequency matches $|f_1 - f_2|$ as
   $f_1 \to f_2$. The envelope's amplitude modulation period should
   be $1/(f_1 - f_2)$.

4. `README.md` — decision cards. "Surprising findings": the
   point-source intensity falloff in dB; the everyday-sounds dB
   table.

5. **Capstone section** in `README.md`: a one-paragraph reflection
   on what the 17-chapter toolkit can now do that it couldn't at
   Chapter 2. Name three real physics questions you could now
   answer from your repository. This is the "what was built" summary
   of the whole toolkit.

Commit as `ch19: sound intensity, Doppler, Mach cone, and beat
frequency`.

Then create a final commit `repo: top-level README capstone summary`
that updates the top-level README with a 17-chapter summary, each
chapter's empirical-verification headline, and the cross-references
between modules.
```

**What this produces:** Sound-intensity / decibel calculations, the Doppler effect verified by simulation, Mach-cone geometry, beat-frequency demonstration via Ch 18's wave solver, plus the capstone README summarizing the 17-chapter toolkit.

**How to adapt this prompt:**

- *For your own project:* Acoustic engineering (room acoustics, sound design, music synthesis) is a substantial domain. The toolkit's wave-equation and Doppler primitives are the foundation.
- *For ChatGPT / Gemini:* Both work for the formulas. The Doppler-by-simulation verification is the pedagogically nice piece — don't just verify the formula by the formula.
- *For Claude Code:* Native fit. This is the chapter where the toolkit's 17-chapter accumulation pays off — the wave solver from Ch 18 is reused for beat frequency.
- *For a Claude Project:* After Ch 19 closes, *now* is when a Claude Project earns its keep — load the repo's README and chapter READMEs into a project and you have a personal physics-simulation consultant.

**Connection to previous chapters:** Closes the arc. Wave-equation solver from Ch 18, energy infrastructure from Ch 8–9, integrators from Ch 4–5. The full 17-chapter physics-simulation toolkit is complete.

**Preview of next chapter:** None — this is the volume's final chapter. The toolkit is built. Open issues for Volume 2 (thermodynamics, E&M, optics, modern physics) extensions and you have a continuation plan.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Wallace Clement Sabine** was the founding of architectural acoustics at Harvard in the 1890s — Sabine's reverberation-time formula ($T = 0.161V/A$, derived from his Fogg Lecture Hall experiments) was developed in time to acoustically design Boston Symphony Hall (1900), which remains one of the most acoustically excellent concert halls in the world — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Wallace Clement Sabine, and how does their work on reverberation time and the Sabine formula for architectural acoustics connect to sound and especially the acoustic design of performance spaces? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Wallace Clement Sabine"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Sabine's specific 1895–1900 experimental method — how he measured reverberation time at the Fogg Lecture Hall, what he varied (curtains, seat cushions, audience seats), and how he derived the inverse relationship between reverberation time and absorption
- Ask: "Boston Symphony Hall opened in 1900. The hall is held up as acoustically near-perfect, but no other hall in the next century replicated Sabine's success on the first try. What did Sabine know about his hall's design that didn't transfer to imitators?"
- Add the framing: "Answer as if you're writing the historical sidebar in a 2026 textbook on concert-hall acoustics aimed at architecture students"

What changes? What gets better? What gets worse?
