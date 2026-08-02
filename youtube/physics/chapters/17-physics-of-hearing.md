# Chapter 17 — Physics of Hearing

*Thirteen orders of magnitude, compressed into "soft" and "loud."*

---

Stand in a quiet library at midnight. The ambient noise level is about 30 dB. Stand next to a working jackhammer. About 110 dB. In ordinary speech, the jackhammer is maybe four times louder than the whisper — that's the rough impression you get from the numbers.

The actual ratio of acoustic intensities is one hundred million.

That gap is not a rounding error. The decibel scale is logarithmic: each 10 dB step represents a tenfold increase in power. The jackhammer delivers a million times more acoustic energy per square meter per second than the library. But your brain registers it as about four times louder, because your ear processes intensity logarithmically — equal ratios feel like equal steps. Otherwise the dynamic range from a falling leaf to a thunderclap would overwhelm any biological sensor.

![dB ladder from threshold of hearing (0 dB, I₀=10⁻¹² W/m²) to threshold of pain (130 dB). Reference points: rustling leaves 10, whisper 30, conversation 60, busy street 80, lawnmower 100, rock concert 110, jet at 30 m 130. 10...](../images/17-physics-of-hearing-fig-02.png)
*Figure 17.2 — Decibel Scale — Compresses 13 Orders of Magnitude into a Single Ladder*

This chapter unpacks that. Sound is a pressure wave, governed by the same wave equation that describes a vibrating string or a ripple on water. Hearing is biological signal processing that compresses fourteen orders of magnitude of intensity into a scale we can navigate. The decibel is the meeting point. Everything else — the speed of sound, the Doppler shift, the resonant tubes inside trumpets and human vocal tracts — is the wave physics that makes the signal exist in the first place.

---

## Sound as a pressure wave

A clarinet produces a sustained note. What arrives at your ear is a tiny periodic variation in air pressure — the compression and rarefaction of air molecules as the instrument's column vibrates. For a normal clarinet tone, the peak pressure variation is about 0.02 Pa above and below atmospheric, which sits at 101,325 Pa. That's five parts per million.

Your eardrum detects this five-parts-per-million wobble, sends a signal to the brain, and the brain hears music.

![Schematic of the human ear: outer ear (pinna, ear canal) collects sound; middle ear (eardrum + three ossicles) impedance-matches air to fluid; inner ear (cochlea) uncoils to show the basilar membrane mapped by frequency — high...](../images/17-physics-of-hearing-fig-05.png)
*Figure 17.5 — Ear Anatomy — Outer/Middle/Inner + Cochlear Spectrum Analyzer*

At the threshold of human hearing (around 3,000–4,000 Hz, the frequency band of speech consonants), the ear detects intensities as low as $10^{-12} \text{ W/m}^2$. An eardrum with area about $60 \text{ mm}^2 = 6 \times 10^{-5} \text{ m}^2$ is receiving roughly half a femtowatt at threshold. No engineered pressure sensor comes close to that sensitivity-to-noise ratio across a comparable dynamic range.

Sound is a **longitudinal wave**: molecules oscillate parallel to the direction of propagation, forming alternating regions of compression (higher pressure) and rarefaction (lower pressure). The molecules don't travel with the wave — they oscillate locally, by less than a millimeter for ordinary sounds — and the pattern of oscillation propagates outward at the speed of sound. The standard wave relation applies:

$$v = f\lambda.$$

In air at room temperature ($20°\text{C}$), $v \approx 343 \text{ m/s}$. So a 440 Hz "A" note has wavelength $\lambda = 343/440 \approx 0.78 \text{ m}$ — almost a meter. A 20 Hz bass rumble has wavelength $\sim 17 \text{ m}$, approximately the size of a large room. A 20 kHz high-frequency limit of human hearing has wavelength $\sim 1.7 \text{ cm}$, about the size of a grape. The spatial scale of the wave determines how it diffracts around obstacles, resonates in rooms, and gets absorbed by materials.

### Speed of sound depends on temperature

In an ideal gas, the speed of sound depends on temperature as:

$$v = 331\sqrt{\frac{T}{273}} \text{ m/s},$$

where $T$ is in kelvin. Or equivalently, $v \approx 331 + 0.6\,T_C$ m/s with $T_C$ in Celsius. At $0°\text{C}$: 331 m/s. At $20°\text{C}$: 343 m/s. At $-10°\text{C}$: 325 m/s.

The temperature dependence is not large in absolute terms, but it matters for musicians. A wind instrument's resonant frequencies depend on the speed of sound inside the tube. A brass player who warms up their instrument — literally blowing warm air through it — is raising the speed of sound inside and shifting the resonant frequencies upward. Outdoor performances in winter require retuning.

In other media, sound is faster: $\sim 1{,}480 \text{ m/s}$ in water, $\sim 5{,}000 \text{ m/s}$ in steel. The reason is the same physics as the wave on a string: speed scales as $\sqrt{\text{stiffness}/\text{inertia}}$. Steel is enormously stiffer than water, more than compensating for its greater density. This is why putting your ear to a railroad track lets you hear an approaching train long before the airborne sound arrives.

<!-- → [INFOGRAPHIC: speed of sound in four media — air at 0°C (331 m/s), air at 20°C (343 m/s), water at 20°C (1480 m/s), steel (5000 m/s) — shown as horizontal bars on a log scale from 100 to 10,000 m/s; annotate with the physical reason: stiffer medium = faster wave; denser medium = slower wave; but stiffness increases faster than density going from gas → liquid → solid, so speed increases overall] -->

---

## Intensity and the decibel scale

**Intensity** is acoustic power per unit area, in W/m². For a point source radiating power $P$ uniformly in all directions, intensity falls as the inverse square of distance:

$$I = \frac{P}{4\pi r^2}.$$

Every time you double the distance from a point source, intensity drops by a factor of four. Halve the distance, intensity quadruples. This is pure geometry: the same power spread over four times the area.

**Sound intensity level** $\beta$ converts intensity to decibels relative to the threshold of hearing $I_0 = 10^{-12} \text{ W/m}^2$:

$$\beta = 10\log_{10}\!\left(\frac{I}{I_0}\right) \text{ dB}.$$

The formula is the entire decibel scale in one equation. To decode any dB value: $I = I_0 \times 10^{\beta/10}$. Some landmarks:

<!-- → [TABLE: sound intensity levels — columns: sound source, intensity (W/m²), level (dB), description; rows: threshold of hearing (10⁻¹², 0, barely audible), rustling leaves (10⁻¹¹, 10, very quiet), quiet library (10⁻⁹, 30), normal conversation (10⁻⁶, 60), heavy traffic (10⁻³, 90, hearing damage with prolonged exposure), jackhammer at 1 m (10⁻¹, 110, painful), threshold of pain (10¹, 130), jet engine at 30 m (10², 140, hearing damage from brief exposure)] -->

The key pattern: each 10 dB increment is a tenfold intensity increase. Each 3 dB increment is approximately a twofold intensity increase (since $\log_{10} 2 \approx 0.30$). The whisper and the jackhammer are 80 dB apart, meaning the jackhammer delivers $10^8$ — a hundred million — times the acoustic intensity.

A trap that catches everyone: you cannot add decibel levels. Two identical 70 dB sources combine to give 73 dB, not 140 dB. The reason: intensity is what adds, not dB values. Two sources each at $10^{-6} \text{ W/m}^2$ combine to $2 \times 10^{-6} \text{ W/m}^2$, and $10\log_{10}(2 \times 10^6) \approx 63 \text{ dB}$... wait — more carefully:

$$\beta = 10\log_{10}\!\left(\frac{2 \times 10^{-6}}{10^{-12}}\right) = 10\log_{10}(2 \times 10^6) = 10(6 + \log_{10} 2) \approx 73 \text{ dB}.$$

The procedure: convert each dB level to intensity, add intensities, convert the sum back to dB. Skipping any step gives nonsense.

### A concert speaker at 50 m

A rock-concert speaker delivers 1 kW of acoustic power. What is the sound level at 50 m distance?

Treat the speaker as a point source radiating into a hemisphere (the floor absorbs or reflects downward):

$$I = \frac{P}{2\pi r^2} = \frac{1{,}000}{2\pi(50)^2} \approx 0.064 \text{ W/m}^2.$$

$$\beta = 10\log_{10}\!\left(\frac{0.064}{10^{-12}}\right) = 10\log_{10}(6.4 \times 10^{10}) \approx 108 \text{ dB}.$$

Dangerous territory, even at 50 m. The reason front-row concert attendees are often handed earplugs. The inverse-square law is not kind: at 1 m from the same speaker, $I \approx 159 \text{ W/m}^2$ — sixteen times the pain threshold.

The reason your brain handles this range gracefully is that hearing is logarithmic. Equal perceived steps in loudness correspond to equal ratios of intensity. The brain doesn't report "I'm receiving $10^{-7} \text{ W/m}^2$ right now." It reports a sensation along a scale from silence to deafening, and the calibration of that scale compresses the hundred-million-fold range into something navigable.

---

## Doppler, resonant tubes, and sonic booms

A motorcycle passes you at 27 m/s, engine humming at a steady 200 Hz. As it approaches, you hear a higher pitch. The moment it passes, the pitch drops abruptly. After it recedes, you hear the lower note steady.

![Two panels. Left: stationary source; concentric circular wavefronts at equal spacing. Right: source moving right; wavefronts compressed in front (higher frequency) and stretched behind (lower frequency). f' = f(v ± v_obs)/(v ∓...](../images/17-physics-of-hearing-fig-03.png)
*Figure 17.3 — Doppler Effect — Wavefronts Bunched Ahead, Stretched Behind*

The **Doppler effect**: wave fronts emitted by a moving source pile up in the direction of motion (shorter wavelength, higher frequency) and stretch out behind (longer wavelength, lower frequency). For a source moving toward a stationary observer:

$$f_\text{obs} = f_\text{src}\,\frac{v_\text{sound}}{v_\text{sound} - v_\text{src}}.$$

For the motorcycle approaching at 27 m/s:

$$f_\text{obs} = 200 \times \frac{343}{343 - 27} = 200 \times \frac{343}{316} \approx 217 \text{ Hz}.$$

After passing:

$$f_\text{obs} = 200 \times \frac{343}{343 + 27} \approx 185 \text{ Hz}.$$

A drop of 32 Hz — roughly a minor third on a piano — at the instant of passing. Easily audible. The general formula accommodating both moving source and moving observer:

$$f_\text{obs} = f_\text{src}\left(\frac{v_\text{sound} \pm v_\text{obs}}{v_\text{sound} \mp v_\text{src}}\right),$$

with upper signs when approaching and lower when receding. The same formula, applied to radar and ultrasound, underlies speed traps, weather radar, and real-time cardiac imaging.

<!-- → [INFOGRAPHIC: Doppler wave diagram — a moving source (motorcycle icon) traveling rightward; wave crests drawn as concentric arcs compressed ahead of the source (shorter spacing = higher frequency at observer on the right) and stretched behind (longer spacing = lower frequency at observer on the left); label v_src, v_sound, and the observed frequencies 217 Hz (approaching) and 185 Hz (receding) from the worked example; student should see the geometric origin of the frequency shift] -->

![Top: sound as longitudinal pressure wave traveling through air at 343 m/s — compressions and rarefactions of molecules in the direction of propagation. Bottom: light as transverse electromagnetic wave at 3×10⁸ m/s —...](../images/17-physics-of-hearing-fig-01.png)
*Figure 17.1 — Sound vs Light — Longitudinal Pressure Wave vs Transverse EM Wave*

![Three panels. Subsonic (v < c): wavefronts compressed ahead, normal Doppler. Sonic (v = c): wavefronts pile up at the source — sound barrier. Supersonic (v > c): wavefronts form a Mach cone behind, sonic boom along the shock...](../images/17-physics-of-hearing-fig-04.png)
*Figure 17.4 — Mach Cone — Subsonic, Sonic, Supersonic Wavefronts*

When $v_\text{src} = v_\text{sound}$, the denominator vanishes. Wave fronts pile up into a **sonic boom** — a shock wave traveling with the aircraft, creating a continuous boom that people on the ground hear as a single sharp bang when the shock front passes over them. This is why supersonic flight over populated land is heavily regulated.

### Resonant tubes

A tube of length $L$ supports standing waves at specific frequencies, just as a string does. The boundary conditions set the allowed modes:

**Both ends open** (flute, organ pipe open at both ends): pressure nodes at both ends.

$$f_n = \frac{nv}{2L}, \quad n = 1, 2, 3, \ldots$$

All harmonics — fundamental, octave, twelfth, double octave — are present.

**One end closed** (clarinet, panpipe, the human vocal tract at its back end): pressure antinode at the closed end, node at the open end.

$$f_n = \frac{(2n-1)v}{4L}, \quad n = 1, 2, 3, \ldots$$

Only odd harmonics — fundamental, fifth, second octave-plus-third — are present. This is why a clarinet and a flute, playing the same pitch, sound different: the clarinet's overtone structure is missing the even harmonics. Timbre is the combination of which harmonics are present and in what proportion.

A concert flute is about 67 cm long, open at both ends. Its fundamental:

$$f_1 = \frac{v}{2L} = \frac{343}{2 \times 0.67} \approx 256 \text{ Hz}.$$

Middle C is 261.6 Hz. The small discrepancy is the end correction — real tube ends radiate slightly beyond their physical edge — which the simple formula ignores.

<!-- → [INFOGRAPHIC: standing wave patterns in open and closed tubes — side by side diagrams for open-open (L = λ/2 for n=1, λ for n=2) and open-closed (L = λ/4 for n=1, 3λ/4 for n=2); show pressure nodes (N) and antinodes (A) in each; label the frequency formulas; student should see why closed tubes support only odd harmonics and why the fundamental of a closed tube at the same length is lower than an open tube] -->

### Ultrasound

Above 20 kHz, sound is inaudible to humans but physically ordinary. Medical ultrasound runs at 1–10 MHz; the wavelengths in soft tissue (sound speed $\approx 1{,}540 \text{ m/s}$) are 1.5 mm to 0.15 mm — fine enough to resolve small anatomical structures. Imaging works by sending a pulse and timing the echo:

$$d = \frac{v_\text{tissue} \times t_\text{echo}}{2}.$$

A 50 μs echo corresponds to a structure at depth $d = (1{,}540)(50 \times 10^{-6})/2 \approx 3.9 \text{ cm}$. Doppler ultrasound adds the frequency-shift measurement to map blood flow velocity in real time — using the same formula that governs the passing motorcycle, applied at megahertz frequencies inside the body.

---

## What the three ideas make together

Sound is wave physics in a particular medium. Intensity is how much power that wave carries per unit area. The decibel scale is the logarithmic compression that lets human perception span the full range from silence to pain without saturating.

The Doppler effect is what happens when the source or the observer moves: frequency shifts in proportion to the ratio of their speeds to the speed of sound. Resonant tubes are what happen when a wave is trapped between boundaries: standing wave patterns at discrete frequencies that determine pitch and timbre. Both follow from the wave equation introduced in Chapter 16; this chapter applies it to the specific case of longitudinal pressure waves in air.

The human ear is a biological instrument tuned, over evolutionary time, to the acoustic signatures of speech, predators, and prey. It is sensitive to frequencies from 20 Hz to 20 kHz — three orders of magnitude in frequency — with peak sensitivity at 3,000–4,000 Hz, exactly the range where speech consonants are most information-dense. It compresses thirteen orders of magnitude in intensity into the range from barely-heard to painful. Every feature of that sensitivity is a solution to a biological signal-processing problem, operating on physical inputs described by the equations in this chapter.

---

## Exercises

### Warm-up

**17.1** *(LO 1, 2)* Compute the speed of sound in air at (a) $-15°\text{C}$, (b) $35°\text{C}$, and (c) $100°\text{C}$. For each, find the wavelength of a 440 Hz "A" note.

**17.2** *(LO 3)* A jet engine at takeoff produces an intensity of $100 \text{ W/m}^2$ at $30 \text{ m}$ distance. (a) What is the sound level in dB? (b) At what distance would the level drop to 100 dB?

**17.3** *(LO 3)* Two friends are talking simultaneously, each producing 65 dB at your location. What is the combined sound level?

**17.4** *(LO 4)* A fire engine siren at $800 \text{ Hz}$ approaches you at $25 \text{ m/s}$. (a) What frequency do you hear as it approaches? (b) What frequency do you hear as it recedes? (c) What is the frequency shift (in Hz) as it passes?

### Application

**17.5** *(LO 3, 6)* A portable speaker rated at $5 \text{ W}$ acoustic output is placed on a picnic table outdoors. (a) Assuming hemispherical spreading, what is the sound level at $3 \text{ m}$ distance? (b) At what distance does the level drop to 70 dB (comfortable conversation level)?

**17.6** *(LO 5)* An organ pipe is open at both ends and $2.0 \text{ m}$ long. At $20°\text{C}$: (a) What are the first three resonant frequencies? (b) If the pipe were closed at one end, what would the first three resonant frequencies be?

**17.7** *(LO 5)* A singing bowl has a rim diameter of about $20 \text{ cm}$. Estimate the fundamental resonant frequency if the bowl is treated as a closed tube of length equal to the diameter. Does the answer land in the audible range?

**17.8** *(LO 4)* You are standing still and a bus drives past at $15 \text{ m/s}$. The engine emits a steady $120 \text{ Hz}$ tone. (a) What frequency do you hear before the bus passes? (b) After? (c) Now suppose the bus is stationary and you run toward it at $5 \text{ m/s}$. What frequency do you hear? Is it the same as (a)?

### Synthesis

**17.9** *(LO 3, 6)* OSHA limits occupational noise exposure to 8 hours at 90 dB per day. The "equal energy" rule says that halving the time allows a 5 dB increase. Using this rule: (a) How long is the safe exposure at 95 dB? At 100 dB? At 110 dB? (b) At a concert at 105 dB, how many minutes of safe exposure remain?

**17.10** *(LO 2, 5)* A flute player performs outdoors at $30°\text{C}$. (a) What is the speed of sound inside the flute? (b) The flute is $67 \text{ cm}$ long (open-open). What is the fundamental frequency? (c) How does this compare to the same flute indoors at $20°\text{C}$? By how many Hz does the pitch shift? Is that musically significant? (A semitone shift is about 6%.)

**17.11** *(LO 3, 4)* Bat echolocation: a bat emits 50 kHz pulses and listens for echoes. (a) What is the wavelength of 50 kHz sound in air at $20°\text{C}$? (b) The bat flies at $8 \text{ m/s}$ toward a moth. What frequency does the bat hear in the echo from the moth (the moth is stationary)? Hint: the bat is both the moving source and the moving observer for the two-step reflection. (c) Why does echolocation work better at 50 kHz than at 5 kHz?

### Challenge

**17.12** *(LO 3, 6, beyond chapter)* The "cocktail party effect" is the brain's ability to focus on one voice among many. (a) Compute the wavelength of a 3 kHz speech consonant. (b) The human head is about 18 cm wide. At 3 kHz, by what fraction of a wavelength does a sound from your left side arrive later at your right ear than your left? (c) Why does this interaural time difference help locate a source at 3 kHz better than at 300 Hz?

**17.13** *(LO 4, 7, beyond chapter)* A medical ultrasound at 5 MHz images a fetal heart. (a) Compute the wavelength in soft tissue ($v = 1{,}540 \text{ m/s}$) — this is approximately the resolution. (b) Doppler imaging detects peak blood-flow velocities of $1.2 \text{ m/s}$ at a beam angle of $45°$ to the vessel. Compute the frequency shift. (c) Explain why doctors use 5 MHz rather than 50 MHz for deep fetal imaging. (Hint: absorption increases with frequency.)

---



By the end of this chapter you should be able to:

1. Describe sound as a longitudinal pressure wave; identify wavelength, frequency, and period for a given sound.
2. Compute the speed of sound in air at any temperature using $v = 331\sqrt{T/273}$ m/s.
3. Compute sound intensity in W/m² and convert between intensity and decibel level using $\beta = 10\log_{10}(I/I_0)$.
4. Compute the Doppler-shifted frequency for a moving source or moving observer.
5. Compute the resonant frequencies of open and closed tubes and explain the difference in harmonic content.
6. Apply the inverse-square law for intensity and interpret the decibel values of common sounds in terms of health and perception.

**Prerequisites.** Chapter 16 (wave equation, $v = f\lambda$, standing waves). Chapter 13 (temperature in kelvin, for the speed-of-sound formula).

**Why this chapter matters.** Sound is the primary human communication channel, and wave physics governs every practical application: concert-hall acoustics, medical ultrasound, noise-cancelling headphones, weather radar, and the microphone converting this sentence into a digital signal. The decibel scale generalizes to any context with wide dynamic range — seismic magnitudes, stellar brightness, electrical signal-to-noise ratios.

---

## ↳ Dig Deeper — Why sound is faster in solids than in liquids than in gases

*Wave speed scales as $\sqrt{\text{stiffness}/\text{inertia}}$. Steel is enormously stiffer than water, which is enormously stiffer than air, and the stiffness difference dominates the density difference — so sound gets faster as you go solid → liquid → gas.*

**Prompt:**
> Explain why the speed of sound in a medium goes as $v = \sqrt{B/\rho}$, where $B$ is the bulk modulus (resistance to compression) and $\rho$ is the density. Then explain why sound is faster in steel ($\sim 5{,}000 \text{ m/s}$) than in water ($\sim 1{,}480 \text{ m/s}$) than in air ($\sim 343 \text{ m/s}$) despite the increasing densities — show that the bulk modulus increases far faster than density across these materials. End with one sentence on why this matters for non-destructive testing of metals using ultrasound.

**What to do with the output:** Save it. The $v = \sqrt{\text{stiffness}/\text{inertia}}$ pattern appears for every wave type: strings, electromagnetic waves in media, matter waves in quantum mechanics.

---

## ↳ Dig Deeper — Why hearing is logarithmic (Weber-Fechner law)

*The logarithmic compression of the decibel scale is not arbitrary — it matches how human perception actually works. Equal ratios of intensity produce equal perceived steps in loudness. This is Weber's law applied to hearing, and it holds (approximately) across many senses.*

**Prompt:**
> Explain the Weber-Fechner law: perceived stimulus intensity scales as the logarithm of physical intensity. Walk through how it applies to (a) hearing (the dB scale), (b) vision (the stellar magnitude scale), and (c) weight perception. Then critique it: where does the law fail? In what regimes does perception become linear or sub-logarithmic? End with one sentence on why this matters for designing user interfaces — audio volume sliders, display brightness controls.

**What to do with the output:** Save it. Weber-Fechner generalizes across psychophysics and reappears in the context of vision (Chapter 26) and signal-processing engineering.

---

## ↳ Dig Deeper — How Doppler ultrasound measures blood flow

*The same Doppler formula that explains the shifting pitch of a passing motorcycle, applied at megahertz frequencies inside the body, lets doctors measure blood flow velocity in real time. It is one of the most elegant translations of undergraduate physics into clinical practice.*

**Prompt:**
> Walk through how Doppler ultrasound measures blood flow velocity. Setup: a transducer emits ~5 MHz waves; they reflect off moving red blood cells; the round-trip Doppler shift depends on blood velocity, sound speed in tissue, and the angle between the beam and the flow direction. Derive the formula and compute a sample case: 50 cm/s blood velocity, 5 MHz transducer, 60° beam angle. End with one sentence on why misestimating the angle produces a systematic error in the velocity reading.

**What to do with the output:** Save it. This is a clean, computable medical application of Chapter 17 physics, and it demonstrates how undergraduate-level wave equations appear directly in clinical cardiology.

---

## LLM Exercise — Chapter 17: Sound in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** An acoustic measurement of one component of your anchor phenomenon — a frequency, an intensity level, or a Doppler shift.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 17 (Physics of Hearing), I want to identify ONE acoustic component of my phenomenon and characterize it.

Please:

1. Identify the sound. Examples:
   - Bike commute: tire-road noise, wind whistling past helmet, brake squeal.
   - Coffee maker: pump noise, steam wand whistle.
   - Marathon: cadence of footstrikes, breathing sound.
   - Espresso machine: pump pulse frequency.
   - Basketball: bounce thump frequency, swish of net.

2. Estimate:
   (a) Frequency in Hz — what part of the audible range?
   (b) Intensity at the listener's location in dB SPL (use a smartphone app or estimate).
   (c) Wavelength.

3. If a Doppler shift is relevant (e.g., someone passing you on a bike), compute it.

4. Identify whether the sound is harmless, annoying, or potentially damaging (>85 dB sustained).

5. State inputs and uncertainty.

6. Connect to Chapter 18 (Electric Charge) — how a microphone converts the acoustic signal into an electrical signal.

Save the output as logbook/chapter-17-sound.md.
```

### What this produces

Your seventeenth Logbook entry — a quantified acoustic component of your phenomenon.

### How to adapt this prompt

- *For phenomena that are nearly silent:* use ambient room noise, or consider any ultrasound or infrasound that would be present but inaudible.
- *For Claude Code:* if you have a smartphone audio recording, run a Fourier transform and identify the spectral peaks. Compare with the resonance formulas.

### Connection to previous chapters

Builds on Chapter 16's wave equation. The decibel scale applies logarithmic compression you've seen in astronomy and electronics contexts. The Doppler formula is kinematic — it uses speeds, not forces — so it connects back to Chapter 3.

### Preview of next chapter

Chapter 18 introduces electric charge and electric fields — the physics of the microphone that converts the sound analyzed here into an electrical signal, and ultimately the foundation of all electronics and electromagnetic theory.

---

## What would change my mind

The chapter argues that classical wave physics captures sound and hearing across the full practical range. The argument would need revision at two extremes: at the threshold of hearing, where acoustic energies are close to thermal noise and the question of whether single phonons play a role is genuinely open in biophysics; and at very high amplitudes, where nonlinear acoustics (shock formation, harmonic generation) requires corrections beyond the linear wave equation.

## Still puzzling

The deepest puzzle this chapter raises: *why is human hearing approximately logarithmic?* The Weber-Fechner law is empirical, not derived from the molecular physiology of the cochlea. The physical mechanism — compression at multiple stages of the auditory pathway, from the basilar membrane to the auditory cortex — is partially understood. But why the logarithm, specifically, rather than some other compressive function? That we cannot yet fully derive from first principles.

---

## AI Wayback Machine

**Hermann von Helmholtz** wrote *On the Sensations of Tone* in 1863, building a comprehensive theory of how the ear analyzes sound into its frequency components. Modern audiology, psychoacoustics, and audio engineering all begin with him.

**Run this:**

```
Who was Hermann von Helmholtz, and how does his work on hearing connect to the physics of hearing we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Hermann von Helmholtz"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Helmholtz's resonance theory of hearing — and where modern cochlear mechanics has revised it.
- Ask it about Helmholtz's range across physiology, physics, and philosophy of perception.

What changes? What gets better? What gets worse?

---

## Connections forward

Chapter 18 begins electricity — electric charge, Coulomb's law, electric fields. The wave physics established here recurs in Chapter 24 when Maxwell shows that light is an electromagnetic wave, and again in Chapter 29 when quantum mechanics assigns wave properties to particles. The decibel scale generalizes to any wide-dynamic-range context: the Richter scale for earthquakes, stellar magnitudes in astronomy, and signal-to-noise ratios in electronics and communications engineering.

---

**Tags:** sound, decibels, doppler-effect, wave-physics, hearing
