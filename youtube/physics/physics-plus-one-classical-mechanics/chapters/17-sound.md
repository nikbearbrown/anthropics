# Chapter 17 — Sound: Pressure Waves and Perception

*Sound is not something traveling through space. It is something happening to matter.*

---

You stand in a thick forest at dawn. A large branch breaks from an oak tree fifty meters away. You hear the crack. It arrives — it seems — instantly.

But it didn't. Light from the same event reaches you in about 160 nanoseconds. Sound takes 0.15 seconds. The delay is real. Thunder demonstrates it plainly: the lightning flash arrives essentially at once, while the sound of the same stroke, from ten kilometers away, takes thirty seconds. Sound is slow. It travels at about 340 meters per second in air, which is fast by human standards and glacially slow compared to light.

More important than the delay, though, is the mechanism. Sound does not travel through empty space. It cannot. It needs matter to propagate. The vacuum between Earth and the Moon is absolute silence — not quieter than a library, but genuinely zero. If you detonated a nuclear weapon on the Moon, you would see the flash and the fireball. You would feel the light's heat. You would not hear anything.

Sound is not a thing traveling through space. It is a disturbance traveling through matter. A compression traveling from molecule to molecule. Nothing moves from the tree to your ear except a wave of pressure — and that wave cannot propagate except through the air between them.

This chapter is about what that means, how it works, and what follows from it. Three things: the mechanism by which pressure waves propagate, why your ear compresses the enormous range of natural sound intensities onto a logarithmic scale, and why an ambulance siren changes pitch as it passes — the Doppler effect.

---

## Sound as a Pressure Disturbance

Strike a tuning fork. The tines vibrate — moving outward, then inward, then outward again, at their natural frequency. When a tine moves outward, it pushes the air molecules immediately in front of it. Those molecules are crowded together, compressed into a region of higher pressure than the surrounding air. When the tine moves inward, it leaves a gap — a rarefaction, a region of lower pressure than normal.

Here is what happens next. The compressed molecules are squeezed. They push outward on their neighbors. Those neighbors push outward on their neighbors. The compression propagates away from the fork — not as molecules physically moving across the room, but as a pressure disturbance passed from molecule to molecule. The individual molecules oscillate back and forth around their average positions, each one barely moving. The disturbance itself travels across the room.

Behind the compression, the rarefaction propagates the same way. Molecules from adjacent regions rush inward to fill the low-pressure zone, overshoot, create a new rarefaction behind them. Compress, rarefy, compress, rarefy — a wave of pressure alternations spreading outward at a fixed speed determined entirely by the properties of the air.

This is a **longitudinal wave**: the molecules oscillate along the same direction the wave travels, not perpendicular to it. Shake a rope up and down and you get a transverse wave; the disturbance propagates forward while the rope moves sideways. Sound is different. The air moves forward and backward, pushing into the wave and pulling back from it, in exactly the direction the wave is going.

<!-- → DIAGRAM: side-by-side comparison of longitudinal and transverse waves — left panel: a horizontal row of dots (air molecules) with a compression region (dots packed tightly) and a rarefaction region (dots spread out) moving to the right; a double-headed arrow shows molecular displacement is LEFT-RIGHT (same as wave direction); labeled "longitudinal — sound"; right panel: a rope with a sinusoidal transverse wave, molecule displacement shown as UP-DOWN arrows perpendicular to the wave's rightward travel; labeled "transverse — light, water surface"; student should see the fundamental structural difference before any equations appear -->

The consequence of requiring a medium is that the wave's speed is a property of the medium, not of the wave. In air at 20°C, sound travels at 343 m/s. In water, it travels at about 1,480 m/s — four times faster. In steel, roughly 5,120 m/s — fifteen times faster than in air.

This seems backward. Steel is far denser than air, and denser media have more inertia, which should slow waves down. Yet steel transmits sound faster. The resolution: speed depends on both density and elasticity. Density provides inertia (slowing). Elasticity — how strongly the medium resists compression and springs back — provides the restoring force (speeding). Steel is denser than air, but it is incomparably more rigid. Rigidity wins. A compression propagates from atom to atom in steel nearly instantly because the atoms barely give at all; in air, the molecules must actually crowd together before any force is transmitted to the next layer.

<!-- → TABLE: three-column table — Medium | Density (kg/m³) | Speed of sound (m/s) — rows: Air at 20°C (1.2 / 343), Water (1000 / 1480), Steel (7800 / 5120); two annotation rows beneath: "Density effect alone: steel should be slowest"; "Actual result: rigidity dominates — steel is fastest despite 6,500× higher density than air"; student should see the paradox stated numerically and understand that it resolves via elasticity, not density -->

**The relationship between frequency, wavelength, and speed** is the same for sound as for any wave:

$$v = f\lambda.$$

Speed equals frequency times wavelength. Since $v$ depends only on the medium, not on the frequency, a higher-pitched sound (higher frequency) has a shorter wavelength, not a faster wave. A lower-pitched sound has a longer wavelength at the same speed.

**A worked example.** A tuning fork vibrates at 256 Hz (middle C on an older scale). Speed of sound in air at 0°C is 331 m/s. What is the wavelength?

$$\lambda = \frac{v}{f} = \frac{331}{256} \approx 1.29 \text{ m.}$$

The compressions are spaced 1.29 meters apart. In one second, 256 compressions exit the fork, so they are spread across $331 / 256 = 1.29$ meters from one to the next.

A note an octave higher (512 Hz) would have wavelength $331/512 \approx 0.65$ m. Same speed, half the wavelength, twice the frequency. This is why orchestras stay in tune across distance: every frequency travels at the same speed. If high frequencies outpaced low ones, a distant orchestra would arrive as garbled noise — the violins before the cellos before the bass drums. Instead, everything arrives together, in cadence, regardless of how far away you are.

---

## Intensity and the Decibel Scale

In a quiet forest, you can hear a single leaf strike the ground. The pressure variation caused by a falling leaf is on the order of $2 \times 10^{-5}$ Pa — about 200 billionths of atmospheric pressure. A rock concert generates peak pressure variations around 20 Pa. That is a factor of one million in pressure amplitude — a factor of $10^{12}$ in intensity.

Your ear handles both. You can hear the falling leaf and survive (with some discomfort) the concert. Not simultaneously, and not without damage in the latter case, but the same mechanical transducer in your ear does the job across twelve orders of magnitude of intensity. This is extraordinary.

**Why intensity scales with pressure squared.** Sound intensity — the power carried by the wave per unit area — depends on the pressure amplitude squared:

$$I = \frac{(\Delta P)^2}{2\rho v},$$

where $\Delta P$ is the pressure amplitude, $\rho$ is the medium's density, and $v$ is the speed of sound. Double the pressure amplitude and the intensity quadruples. This is the same rule as for any oscillating system: energy scales with amplitude squared.

The threshold of human hearing — the quietest sound a young person with undamaged hearing can detect — is an intensity of about $10^{-12}$ W/m². A rock concert reaches about 1 W/m². The ratio is $10^{12}$: a trillion to one.

**Why the decibel scale exists.** The human auditory system does not perceive intensity linearly. It perceives it logarithmically. This is not an accident of neuroscience — it is an optimal design. If the ear responded linearly to intensity, a system sensitive enough to detect $10^{-12}$ W/m² would be instantly saturated and useless at $10^{-6}$ W/m², let alone at 1 W/m². The logarithmic response compresses the entire range into a manageable span.

The decibel scale formalizes this:

$$\beta = 10 \log_{10}\!\left(\frac{I}{I_0}\right),$$

where $I_0 = 10^{-12}$ W/m² is the reference intensity (the threshold of hearing). Each factor of 10 in intensity corresponds to exactly 10 dB. A trillion-to-one intensity range maps onto a 0–120 dB scale.

A few reference points to calibrate the scale: 0 dB is the threshold of hearing — not silence, but the quietest detectable sound. Rustling leaves are about 10 dB. Normal conversation, 60 dB. A car horn at close range, 110 dB. The threshold of pain — where sound becomes physically harmful immediately — is around 130 dB.

<!-- → CHART: vertical logarithmic scale from 0 to 140 dB — each major gridline at 10 dB intervals; labeled reference points at key levels: 0 dB (threshold of hearing), 10 dB (rustling leaves), 30 dB (quiet library), 60 dB (normal conversation), 90 dB (lawnmower), 110 dB (car horn close range), 120 dB (jet engine 30 m), 130 dB (threshold of pain); a second axis alongside shows corresponding intensity in W/m² from 10⁻¹² to 10²; student should see both the logarithmic compression and the corresponding intensity scale together -->

**A worked example.** A car horn produces a pressure amplitude of 10 Pa in air ($\rho = 1.29$ kg/m³, $v = 331$ m/s at 0°C). What is the decibel level?

Intensity:
$$I = \frac{(10)^2}{2(1.29)(331)} = \frac{100}{854} \approx 0.117 \text{ W/m}^2.$$

Decibel level:
$$\beta = 10 \log_{10}\!\left(\frac{0.117}{10^{-12}}\right) = 10 \log_{10}(1.17 \times 10^{11}) \approx 10 \times 11.07 = 110.7 \text{ dB.}$$

About 111 dB. Prolonged exposure at this level causes permanent hearing damage.

The decibel is a ratio unit, not an absolute measure of loudness. It quantifies intensity *relative to a reference*. The reference $I_0$ is a convention — chosen to put the threshold of hearing at 0 dB. Nothing about the physics requires 0 dB to correspond to any particular absolute value; the choice of reference is human and practical.

An important corollary: doubling the physical intensity adds only 3 dB. Halving adds only −3 dB. This is because $\log_{10}(2) \approx 0.3$, so a factor of 2 in intensity is $10 \times 0.3 = 3$ dB. Perceptually, 3 dB is a barely noticeable change in loudness under ideal conditions. To double the perceived loudness of a sound, you need to increase the intensity by a factor of about 10 — which is 10 dB. The logarithm compresses your perception dramatically relative to the underlying physics.

---

## The Doppler Effect

You stand on a street corner. An ambulance approaches from two blocks away. The siren is audible at a certain pitch. As the ambulance passes — at its closest point — the pitch is highest. As it recedes, the pitch drops noticeably. The siren frequency has not changed; the ambulance electronics run at a fixed rate regardless of its motion. What changes is the frequency you hear.

This is the **Doppler effect**, and understanding it requires thinking about what a wave actually is.

The siren emits compressions at, say, 600 Hz — 600 compressions per second. Each compression moves outward at the speed of sound, 340 m/s, in all directions. When the ambulance is stationary, the compressions in any direction are equally spaced.

Now put the ambulance in motion. As it emits each successive compression, it has moved a bit closer to you. Each new compression starts its journey from a slightly more advanced position. The compressions in your direction pile up — the spacing between them (the wavelength) shrinks. Shorter wavelength at fixed wave speed means higher frequency. You hear a higher pitch.

<!-- → DIAGRAM: two-panel Doppler geometry — left panel: stationary ambulance at center, equally spaced circular wavefronts spreading in all directions, observer at right labeled "hears emitted frequency f_s"; right panel: moving ambulance (arrow pointing right toward observer), circular wavefronts compressed in the forward direction (crowded together on the right side) and stretched on the rear side (spread apart on the left); labels: "compressed λ → higher f_obs" (right) and "stretched λ → lower f_obs" (left); the wave speed arrows in both panels are the same length, showing v_wave unchanged — student should see that speed doesn't change, only spacing does -->

Behind the ambulance, the opposite happens. Each successive compression starts from a position farther away from where you'd be if you were behind it. The compressions are stretched apart. Longer wavelength means lower frequency. Lower pitch.

The motion of the source does not change the speed of the sound in the air. The speed of sound is set by the air, not by the source. What changes is the wavelength, and therefore the frequency you detect. Speed = frequency × wavelength; speed is fixed by the medium; if wavelength changes, frequency must change inversely.

The formula for a source moving at speed $v_s$ toward a stationary observer, in a medium where sound travels at $v_w$:

$$f_{\text{obs}} = f_s \left(\frac{v_w}{v_w - v_s}\right).$$

When the source moves away, replace the minus sign with a plus:

$$f_{\text{obs}} = f_s \left(\frac{v_w}{v_w + v_s}\right).$$

Notice that the approaching and receding shifts are not symmetric. The approaching formula makes the denominator smaller (less than $v_w$), giving a ratio greater than 1. The receding formula makes the denominator larger, giving a ratio less than 1. But the fractional increases and decreases are not equal in magnitude. Moving toward you at 35 m/s produces a larger absolute frequency shift than moving away at 35 m/s. The asymmetry arises because the denominator in the approaching formula is smaller — dividing by something smaller than $v_w$ gives a larger ratio than dividing by something larger than $v_w$.

**A worked example.** A train horn emits 150 Hz. The train approaches at 35 m/s. Speed of sound: 340 m/s. What do you hear?

$$f_{\text{obs}} = 150 \times \frac{340}{340 - 35} = 150 \times \frac{340}{305} = 150 \times 1.115 \approx 167 \text{ Hz.}$$

As the train recedes:

$$f_{\text{obs}} = 150 \times \frac{340}{340 + 35} = 150 \times \frac{340}{375} = 150 \times 0.907 \approx 136 \text{ Hz.}$$

The approaching train sounds 17 Hz higher than the emitted frequency; the receding train sounds 14 Hz lower. The upward shift is larger in absolute terms. The difference — from 136 Hz to 167 Hz — is a pitch change that listeners find unmistakable.

**What happens when the source reaches the speed of sound?** Look at the approaching formula: as $v_s$ approaches $v_w$, the denominator $(v_w - v_s)$ approaches zero. The observed frequency approaches infinity. In practice, what happens before you reach infinity is that all the compressions the source has been emitting pile up on top of each other in the direction of motion. The source is traveling as fast as its own sound. Every compression the source has ever emitted in the forward direction is stacked right at the source's nose.

Exceed the speed of sound, and the source outruns all those compressions. The compressions cannot warn you of the source's approach — they arrive only after the source itself has passed. All the piled-up energy arrives as a single pressure spike: a shock wave, the **sonic boom**. A supersonic aircraft continuously drags a cone-shaped shock wave behind it; the boom you hear on the ground is not the moment the plane broke the sound barrier (which it did far away, at another time). It is the moment the shock wave cone — spreading outward from the aircraft's path — sweeps past your position.

<!-- → DIAGRAM: three-panel Mach number progression — panel 1: subsonic (v_s < v_w), source inside its own wavefronts, circular wavefronts spread ahead; panel 2: exactly Mach 1 (v_s = v_w), source at the leading edge of all wavefronts, wavefronts stacking up at a single point; panel 3: supersonic (v_s > v_w), aircraft ahead of all wavefronts, a Mach cone drawn behind it, angle labeled θ = sin⁻¹(v_w/v_s); ground observer below the cone labeled "hears boom when cone sweeps past" — student should see the progression and understand why the boom arrives after the aircraft, not as it approaches -->

---

## How the Three Ideas Connect

These three concepts hang together on a single underlying idea: sound is a wave, and waves carry energy through matter by the repetitive action of local interactions.

The propagation mechanism — compressions and rarefactions passed from molecule to molecule — explains why sound requires a medium, why its speed depends on the medium's elastic properties rather than frequency, and why the relationship $v = f\lambda$ holds universally.

The logarithmic perception — encoded in the decibel scale — is not a curiosity about human ears. It is the solution to an engineering problem: how to build a single sensor that responds usefully to twelve orders of magnitude of signal intensity. The physics of the wave (intensity scales with amplitude squared) combined with the neuroscience (perception scales with the logarithm of intensity) gives the decibel system its structure. You are not perceiving the wave; you are perceiving a logarithmically compressed version of it.

The Doppler effect is the consequence of the source moving relative to the medium in which the wave propagates. The key insight is that the wave's speed in the medium is fixed; therefore, any change in the spacing of the compressions (change in wavelength) directly translates to a change in frequency. The source's motion compresses or stretches the wavelength. The frequency you hear reflects the geometry of how those compressions arrive at your ear.

At the extreme of the Doppler effect — the source moving at the speed of its own wave — compression piles on compression and energy concentrates into a shock front. The mathematics of the Doppler formula predicts infinite observed frequency at that limit, which is the formula's way of telling you that something qualitatively different is happening: the wave equation itself breaks down in a new regime.

---

## What Would Change My Mind

The foundational claim of this chapter — that sound speed in a given medium at a given temperature is independent of frequency — is exceptionally well-tested. It is the acoustic statement of dispersion-free propagation, and for sound in air at normal conditions, it holds to very high precision. Were it demonstrated that particular frequencies in air systematically travel faster or slower than others at normal temperatures, the entire framework would require revision. In practice, corrections for frequency-dependence (absorption, dispersion) exist only under extreme conditions or for ultrasound in special media.

## Still Puzzling

Why has the human ear's logarithmic response evolved to have the specific range it has — roughly 120 dB from threshold to pain — rather than some other range? The environmental conditions facing evolving hominids required detecting both very quiet sounds (rustling prey, quiet footsteps) and surviving very loud ones (thunder, falling trees). Whether there is a deeper optimization principle that predicts the specific range, or whether it is largely contingent on accident and evolutionary constraint, is not settled. The logarithmic compression itself is well-understood; the precise parameters of the human auditory system are not fully derived from first principles.

---

## Exercises

### Warm-up

**1.** A sound wave in air at 20°C ($v = 343$ m/s) has a frequency of 440 Hz (concert A). (a) What is its wavelength? (b) The same 440 Hz note is played underwater ($v = 1480$ m/s). What is its wavelength there? (c) Does the pitch you hear change when the sound moves from air to water? Explain why or why not.

*Tests: $v = f\lambda$; speed is medium-dependent, frequency is source-dependent; pitch is tied to frequency, not wavelength.*

**2.** A sound has intensity $I = 10^{-7}$ W/m². (a) What is its decibel level? (b) A second sound is 20 dB louder. What is its intensity in W/m²? (c) By what factor does the pressure amplitude change between the two sounds?

*Tests: decibel formula; 20 dB = factor of 100 in intensity; intensity ∝ (ΔP)² so pressure amplitude scales as √100 = 10.*

**3.** A fire truck siren emits 900 Hz. The truck approaches you at 25 m/s. Speed of sound: 340 m/s. (a) What frequency do you hear? (b) As the truck recedes at the same speed, what frequency do you hear? (c) Is the upward shift larger or smaller than the downward shift, and why?

*Tests: Doppler formula for approaching and receding; asymmetry of the two shifts.*

**4.** You see a lightning bolt and hear the thunder 4.5 seconds later. How far away was the lightning? ($v_{\text{sound}} = 340$ m/s, $v_{\text{light}} \approx 3 \times 10^8$ m/s — treat light as instantaneous.)

*Tests: basic $d = vt$ applied to sound travel time; connection to the chapter's opening.*

---

### Application

**5.** A rock concert is measured at 110 dB at the front row. (a) What is the intensity in W/m²? (b) At what distance from the stage would the intensity drop to 80 dB? (Intensity falls as $1/r^2$ for a point source; if $I_1 r_1^2 = I_2 r_2^2$, find $r_2$ given $r_1 = 2$ m.) (c) How many times more intense is the front row than the 80 dB location?

*Tests: decibel-to-intensity conversion; inverse-square law; intensity ratio from dB difference.*

**6.** An ambulance drives toward you at 30 m/s emitting a 1,000 Hz siren. Speed of sound is 340 m/s. (a) What frequency do you hear? (b) The ambulance passes and recedes. What frequency do you hear then? (c) The frequency suddenly jumps from what you heard receding back to the emitted frequency — at what moment does this happen?

*Tests: Doppler applied to a full pass-by scenario; identifying the moment of closest approach.*

**7.** A bat emits ultrasonic clicks at 50,000 Hz while flying toward a stationary moth at 8.0 m/s. Speed of sound: 340 m/s. (a) What frequency does the moth "receive"? (b) The sound reflects off the moth and returns to the bat. Now the moth acts as a stationary source and the bat is a moving observer. Use the observer-moving form of Doppler to find the frequency the bat hears in the echo. (This double-Doppler shift tells the bat how fast it is closing on the moth.)

*Tests: two-step Doppler (source moving to stationary reflector, then stationary source to moving observer); biological application.*

---

### Synthesis

**8.** You hear a train horn at 800 Hz as it approaches and at 680 Hz as it recedes. The speed of sound is 340 m/s. (a) Set up two Doppler equations (one for approaching, one for receding) with $f_s$ and $v_s$ as unknowns. (b) Solve simultaneously for the emitted frequency $f_s$ and the train's speed $v_s$. (c) Verify your answers by plugging back into both equations.

*Tests: using the Doppler formula inversely to extract source properties from observed frequencies — a technique used in police radar and medical ultrasound.*

**9.** A 120 dB sound is produced at a point source. (a) What is its intensity at 1 m? (b) Using the inverse-square law, at what distance does the intensity fall below 85 dB (the threshold for occupational hearing damage under 8-hour exposure)? (c) A construction worker spends a full shift at that threshold distance. A second worker stands 3 m closer. By how many decibels is the closer worker's exposure higher?

*Tests: combining decibels with inverse-square law; translating physical intensity to occupational health implications.*

---

### Challenge

**10.** A supersonic aircraft flies at Mach 1.8 ($v_s = 1.8 \times v_{\text{sound}} = 1.8 \times 340 = 612$ m/s) at an altitude of 10,000 m. (a) What is the half-angle of the Mach cone? (The sine of the cone's half-angle equals $v_w / v_s$.) (b) How far behind the aircraft does the shock wave intersect the ground when the aircraft is directly overhead? (c) How long after the aircraft passes directly overhead do you on the ground hear the boom?

*Tests: sonic boom geometry; Mach cone angle; converting geometry to a time delay.*

---

## LLM Exercise — Chapter 17: Sound (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the Doppler effect demo — using a phone, a passing car, or a swung sound source.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 17 demo. Notebook in this Claude Project. Chapter 17
taught: sound as longitudinal pressure waves; speed of sound
~343 m/s in air; intensity and the decibel scale (logarithmic);
the Doppler effect (frequency shifts when source and observer
have relative motion — observed frequency higher when approaching,
lower when receding); resonance.

**The Demo:** Three options. Pick at least one.

**Option A — Recorded Passing Car (Doppler Effect)**

Easiest. With your phone:
1. Record audio (a few seconds long) as a car approaches and
   passes.
2. Listen back. The pitch is HIGHER as the car approaches and
   LOWER as it recedes.
3. Use a free phone app (Spectroid, Phyphox, n-Track Tuner) to
   measure the actual frequency shift.

The chapter's prediction: f_observed / f_source = (v_sound) /
(v_sound - v_source) when source approaches.

Estimate the car's speed from the frequency shift:
v_source = v_sound × (f_observed - f_source) / f_observed
(approximation valid for v << v_sound).

Compare to your visual estimate of the car's speed.

**Option B — Swung Sound Source**

Tie a small bluetooth speaker (or a buzzer, or even a phone
playing a steady tone) to a string. Spin it in a horizontal
circle. Stand outside the circle.

When the source moves TOWARD you, frequency rises.
When AWAY, frequency falls.

You'll hear a wahh-wahh-wahh oscillation as it swings.

**Option C — Beat Frequency (Resonance/Interference)**

Two tones at slightly different frequencies played together
produce a beat: an audible amplitude oscillation at the
difference frequency.

1. Use two phones playing two different tones (use a tone
   generator app: try 440 Hz and 444 Hz).
2. Listen. You'll hear a beat at 4 Hz (4 oscillations per
   second).

This isn't Doppler but it's the chapter's superposition concept
applied to sound. Both options A/B and option C are valuable.

**Use Claude as a thinking partner:**
- Before: "What frequency shift should I expect for a car
  passing at 30 mph (~13 m/s) carrying a 500 Hz horn?"
- After: "The recorded shift was X Hz on a Y Hz source. The
  predicted speed is Z m/s. The visual speed estimate was W
  m/s. Where's the discrepancy?"

**Notebook entry should include:**
- Audio recording or video.
- Spectrogram (Phyphox can produce one).
- Frequency shift measurement.
- Computed source velocity (Doppler) or beat frequency
  (interference).
- One real-world application: Doppler radar for weather, or
  Doppler ultrasound for measuring blood flow.

End with: why don't we hear the Earth's rotation as a Doppler
shift on starlight (which becomes the equivalent for light)?
```

---

**What this produces:** A demo entry confirming the Doppler effect with measured frequencies. The free spectrogram apps make this much more rigorous than a "I heard the pitch change" demo.

**How to adapt this prompt:**

- *For your own project:* The phone-based spectrogram apps (Spectroid, Phyphox, n-Track Tuner) are excellent and free. If you don't have a phone, the qualitative pitch comparison still works.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — if you record the audio file, Claude Code with a library like librosa can produce a spectrogram and extract frequency.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Chapter 16's wave concepts; Chapter 17 specializes to sound and adds the Doppler effect.

**Preview of next chapter:** Chapter 18 is light. You'll do a refraction demo with a glass of water (the broken-pencil illusion) and a dispersion demo with a CD (which acts as a diffraction grating producing a rainbow).

---

## AI Wayback Machine

**Ernst Chladni** discovered the patterns of vibrating plates in 1787 — visible nodes that founded the modern study of acoustics.

**Run this:**

```
Who is Ernst Chladni, and how does their work connect to sound
we covered in this chapter? Keep it to three paragraphs. End
with the single most surprising thing about their career or ideas.
```

→ Search **"Ernst Chladni"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Ernst Chladni's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Ernst Chladni's framework."

What changes? What gets better? What gets worse?

---

*Tags: longitudinal-waves; intensity; decibels; doppler-effect; pressure-waves; sound-propagation; acoustic-perception*
