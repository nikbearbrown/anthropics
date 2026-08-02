# Sound: Pressure Waves and Perception

**Suggested titles:**
- The Physics of Listening — How Pressure Waves Become Experience
- What Sound Actually Is — From Vibration to Sensation
- The Machinery of Hearing — Compression, Intensity, and Motion

---

**TL;DR:** Sound is a longitudinal pressure wave traveling through matter. Its speed depends on the medium's rigidity and density, not on frequency. How loud a sound appears depends on the logarithm of its intensity — which is why the decibel scale exists. And why an ambulance siren changes pitch as it passes: the Doppler effect compresses and stretches the waves based on motion.

---

## Chapter Opening — If a Tree Falls in the Forest

You stand in a thick forest at dawn, alone. A large branch breaks from an ancient oak tree fifty meters away. You hear a crack — sharp, loud, unmistakable. The sound arrives at your ear nearly instantaneously. You feel it, in fact: your eardrum vibrates.

But here's the puzzle. If sound is a wave — if it's something traveling through space like ripples on water — it should take time to reach you. Light from the sun takes eight minutes. A radio signal takes milliseconds. Why does sound seem to arrive *now*, in the present moment, when by all rights it should be delayed?

The answer reveals something fundamental about how waves work, and about what your ear is actually doing when you hear. Sound *is* delayed — but only by a few hundredths of a second. Thunder confirms it: the lightning flash reaches your eye in microseconds. The sound of the same explosion takes seconds to arrive. The delay is real and measurable.

But sound doesn't travel through empty space. It doesn't travel through space at all. It travels through *matter* — air, water, the material of your eardrum. And that matters enormously.

**Learning objectives:**
By the end of this chapter you will understand:
- What sound is: the mechanism at first principles, and why it requires a medium
- How speed of sound depends on the medium, not the frequency of the wave
- Why intensity is measured logarithmically, and what that tells you about how your ear works
- The Doppler effect: how motion changes what you hear, and what happens when an object outpaces its own sound

**Prerequisites:** Familiarity with waves (wavelength, frequency, amplitude), logarithms, and basic ideas about oscillation and periodic motion.

---

## Concept 1: Sound as Disturbance — The Machinery of Longitudinal Waves

**The Scene:** A tuning fork strikes the air.

A vibrating tuning fork is a machine for pushing. When the tines oscillate, they compress the air in front of them and leave a low-pressure region (a void) behind. That compression is not a single event — it's a series. As the tines move, the air molecules nearest them get pushed and cluster together. Higher pressure in that region.

The molecules that cluster together are now squeezed. They push back on the molecules behind them. Those molecules push on their neighbors. The disturbance propagates outward from the fork — not as a physical object moving away, but as a pressure wave traveling through the medium.

Behind the compression, the tines have also pulled back, creating a region of lower pressure — what we call a *rarefaction*. The same propagation happens here: molecules from high-pressure regions rush into the low-pressure void, equalizing, overshooting, and creating new rarefactions farther out.

This is a **longitudinal wave**. The medium oscillates back and forth *along the direction the wave is traveling*, not perpendicular to it (as in a transverse wave like a water ripple). The direction of vibration and the direction of propagation are parallel.

Compress-rarefact-compress-rarefact. The molecules themselves don't travel far — each one oscillates in place, passing the disturbance to its neighbor. But the disturbance itself travels outward at a fixed speed in that medium.

**The Trade-off:** Longitudinal waves require a medium. That's their constraint and their power. A sound wave cannot exist in a vacuum — no molecules means no compressions to relay, no rarefactions to fill. This is why space is silent. It's also why sound travels *so much faster in solids than in air*. Solids are rigid. Their atoms are tightly bound. A compression propagates quickly from atom to atom. Gases are compressible — lots of space between molecules — so sound dawdles.

This produces an inversion: solids are *denser* than gases, which should make sound slower (denser media have more inertia). Yet sound travels nearly *four times faster* in water than in air, and *twenty times faster* in steel than in water. Rigidity dominates density. The two compete, and rigidity usually wins.

**Worked Example — The Relationship v = fλ:**

The speed of sound in air at 0°C is 331 m/s. A tuning fork vibrates at 256 Hz (middle C). What is the wavelength of the sound wave it produces?

We use the fundamental relationship for all waves:
$$v = f\lambda$$

Rearranging:
$$\lambda = \frac{v}{f} = \frac{331\text{ m/s}}{256\text{ Hz}} = 1.29\text{ m}$$

The wavelength is about 1.3 meters. The distance from one compression center to the next is 1.3 meters. This makes intuitive sense: the tuning fork vibrates 256 times per second. Each vibration creates one compression-rarefaction pair. In 1 second, 256 pairs move away at 331 m/s, so they're spaced $331/256 = 1.29$ m apart.

Here's the crucial point: *the speed is the same for all frequencies in the same medium at the same temperature*. A higher-pitched sound (higher frequency) produces shorter wavelengths, not faster waves. If this were not true — if high-frequency sounds traveled faster — then a distant orchestra would arrive garbled: the high notes would reach you first, the bass notes later. Instead, an orchestra stays in cadence no matter how far away it is. The speed depends only on the medium.

**Common Misconception:** "Louder sounds travel faster." They don't. Loudness relates to amplitude (the size of the pressure variation), not frequency. A quiet 1000 Hz note and a loud 1000 Hz note travel at the same speed through air. The loud one has bigger compressions and rarefactions, but they move at identical velocity.

---

## Concept 2: Intensity and Perception — The Logarithmic Ear

**The Scene:** A quiet forest. Then a car horn.

In a forest at dawn, you can hear a single leaf fall. The pressure variation caused by that falling leaf is perhaps 0.00001 pascals — one ten-millionth of atmospheric pressure. In a traffic jam, cars honk. A car horn produces a pressure variation of roughly 100 pascals. That's a factor of 10 million difference in pressure amplitude.

But when you experience them, the horn doesn't feel 10 million times louder. It feels *catastrophically loud*, yes, but not 10 million times more. Your ear compresses the scale somehow.

**The Mechanism — How Energy Relates to Amplitude:**

Sound intensity is the power per unit area carried by the wave:
$$I = \frac{P}{A}$$

where $P$ is power (in watts) and $A$ is the area (in square meters). The SI unit is watts per square meter (W/m²).

The intensity depends on the *pressure amplitude squared*. If the pressure variation doubles, the intensity increases by a factor of four.

$$I = \frac{(\Delta p)^2}{2\rho v_w}$$

where $\Delta p$ is the pressure amplitude, $\rho$ is the medium's density, and $v_w$ is the speed of sound in that medium.

This is the key physical relationship. Energy in a wave scales with amplitude squared — a universal rule for oscillating systems. Doubling the amplitude quadruples the energy. This makes sound intensity a useful physical quantity.

But your ear doesn't perceive intensity directly. Your ear perceives it logarithmically.

**The Logarithmic Scale — Why Decibels Exist:**

The human hearing system responds to ratios, not absolute values. A whisper is roughly 1/1,000,000 as intense as a car horn. But the difference you perceive between a whisper and normal speech (which is maybe 10× as intense as a whisper) *feels like a similar jump* to the difference between normal speech and a loud shout.

This is why we use the **decibel scale**, which compresses the enormous range of sound intensities down to a scale that matches human perception:

$$\beta \text{ (dB)} = 10 \log_{10}\left(\frac{I}{I_0}\right)$$

where $I$ is the sound intensity and $I_0 = 10^{-12}$ W/m² is the reference intensity — the quietest sound a person with normal hearing can perceive.

Because $\log_{10}(1) = 0$, the quietest audible sound is 0 dB. This is the *threshold of hearing*.

Here's the crucial arithmetic: each factor of 10 in intensity corresponds to exactly 10 dB. A sound that is 10 times as intense as another is 10 dB higher. A sound that is 100 times as intense (10² as intense) is 20 dB higher.

**Worked Example — Calculating Sound Intensity Level:**

A car horn produces a pressure amplitude of 10 Pa in air (at 0°C, density 1.29 kg/m³, sound speed 331 m/s). What is the decibel level?

First, calculate the physical intensity:
$$I = \frac{(\Delta p)^2}{2\rho v_w} = \frac{(10)^2}{2(1.29)(331)} = \frac{100}{852.98} = 0.117 \text{ W/m}^2$$

Now the decibel level:
$$\beta = 10\log_{10}\left(\frac{0.117}{10^{-12}}\right) = 10\log_{10}(1.17 \times 10^{11}) = 10(11.07) = 110.7 \text{ dB}$$

The car horn is roughly 111 dB. This is loud enough to cause hearing damage with prolonged exposure. The ear's logarithmic response means that doubling the physical intensity (which would double the pressure amplitude times √2) adds only about 3 dB to the perceptual loudness.

**The Trade-off — Sensitivity vs. Survivability:**

Your ear's logarithmic response is a brilliant compromise. It gives you the sensitivity to detect a falling leaf (0 dB) and the robustness to survive a rock concert (110 dB) using the same transduction mechanism. If your ear responded linearly, the same device that detected a whisper would be completely saturated by normal speech.

But there's a cost: the logarithmic compression means you lose information. You can't distinguish between a 110 dB and a 111 dB sound as easily as you can distinguish between a 0 dB and a 1 dB sound, because dB is already a logarithmic scale. The absolute sensitivity drops at high intensities.

**Common Misconception:** "The decibel is a unit of loudness." No. Decibel is a *ratio* unit, expressed logarithmically. It measures intensity level *relative to a reference*. Different reference intensities would give different dB values for the same physical sound. For sound in air, we use $I_0 = 10^{-12}$ W/m² because that's the threshold of human hearing. It's a standard choice, not a fundamental constant.

---

## Concept 3: The Doppler Effect — Motion Compresses Wavelength

**The Scene:** An ambulance approaches on a city street.

You hear the siren from blocks away. As the ambulance gets closer, the pitch gets higher — sharper, more urgent. At the moment it passes directly in front of you, the pitch is highest. Then, as it recedes, the pitch drops — a clear shift downward, a falling tone.

The siren itself produces the same frequency all the time. The frequency doesn't change. What changes is what you *hear*. This is the **Doppler effect**: motion between the source and observer shifts the observed frequency.

**The Mechanism — Compression and Rarefaction:**

Imagine the siren emits compressions at a fixed frequency, say 600 Hz. Each compression is separated by the wavelength $\lambda = v/f$ in still air.

When the ambulance is stationary, the compressions spread out in all directions at equal spacing. You detect them passing your ear at the emitted frequency.

Now the ambulance moves toward you at 35 m/s. As it emits the *next* compression, it's moved 35 m closer to you. The next compression after that starts from a point 35 m closer still. The compressions are now *bunched together* in the direction of motion.

The spacing between compressions (the wavelength, from your perspective) is smaller. Since $v = f\lambda$ and $v$ is fixed (the speed of sound in air doesn't change), smaller $\lambda$ means higher $f$. You hear a higher pitch.

When the ambulance moves away, it emits compressions from progressively farther positions. The compressions are stretched apart — longer wavelengths, lower frequency, lower pitch.

**The Formula for Moving Source, Stationary Observer:**

If a source moves toward you at speed $v_s$ and emits sound at frequency $f_s$, the frequency you observe is:

$$f_{obs} = f_s \left(\frac{v_w}{v_w - v_s}\right)$$

where $v_w$ is the speed of sound in the medium.

If the source moves away, use a plus sign:
$$f_{obs} = f_s \left(\frac{v_w}{v_w + v_s}\right)$$

**Worked Example — Train Horn Doppler Shift:**

A train horn emits 150 Hz. The train moves at 35 m/s toward you. The speed of sound is 340 m/s. What frequency do you hear?

$$f_{obs} = 150 \left(\frac{340}{340 - 35}\right) = 150 \left(\frac{340}{305}\right) = 150 (1.115) = 167 \text{ Hz}$$

You hear 167 Hz instead of 150 Hz — a shift of about 17 Hz upward.

As the train passes and recedes:
$$f_{obs} = 150 \left(\frac{340}{340 + 35}\right) = 150 \left(\frac{340}{375}\right) = 150 (0.907) = 136 \text{ Hz}$$

Now you hear 136 Hz — a shift of 14 Hz downward. Note that the upward shift and downward shift are *not symmetric*. Motion toward you produces a bigger frequency change than motion away. This is because the denominator is smaller when approaching.

**The Trade-off — Speed vs. Compression:**

The Doppler effect is stronger at higher source speeds. An ambulance moving at 70 m/s would produce a more dramatic pitch shift than one moving at 35 m/s. But there's a limit. What happens when the source speed approaches the speed of sound itself?

**At the Speed of Sound — Sonic Booms:**

As the source speed $v_s$ approaches $v_w$, the denominator $(v_w - v_s)$ approaches zero. The observed frequency approaches infinity. The pressure variations become more and more extreme, bunching all the energy of the sound waves into a shock wave.

If the source actually exceeds the speed of sound — becomes supersonic — it outruns the sound waves it emitted while approaching. All those compressed waves pile up behind it in a cone-shaped shock wave called a **sonic boom**.

An aircraft flying faster than sound creates *two* sonic booms: one from the nose cone and one from the tail. As the aircraft passes overhead, both reach you in succession. You don't hear the aircraft coming — it has already passed before the shock wave reaches you.

The boom is not an explosion. It's constructive interference: all the sound waves that would have been heard over the next few seconds are stacked on top of each other in a single, violent pressure spike.

**Common Misconception:** "Sonic booms are only produced once, when breaking the sound barrier." Not true. Any supersonic object continuously produces sonic booms — one ahead and one behind. The boom you hear is not the moment the object passes the speed of sound, but the moment the shock wave from that object reaches your ear.

---

## Integration — How the Pieces Connect

These three concepts form a coherent understanding of sound:

1. Sound is *not* a substance traveling through space. It's a pressure disturbance propagating through matter via molecular interaction. This is why it requires a medium and why its speed depends on the medium's properties.

2. The intensity of sound — the energy carried per unit area — scales with pressure amplitude squared. But our ears don't perceive intensity linearly; they perceive it logarithmically. The decibel scale is not a convenience; it's a map of how your nervous system works.

3. Motion between source and observer compresses or stretches the wavelength without changing the speed of the wave in the medium. Higher compression means higher frequency. Higher frequency means higher pitch. The effect is dramatic enough that we use it technologically — police radar uses the Doppler shift of radio waves to detect speeding cars.

These three mechanisms explain a huge range of phenomena: why a concert hall's acoustics depend on its materials, why hearing protection must address both absolute intensity and frequency-dependent damage patterns, why emergency vehicles' sirens change pitch as they pass, and why a supersonic jet leaves a shock wave in its wake.

---

## Graduated Exercises

**Warm-up:**

1. A frequency of 440 Hz (musical note A) travels through air at 343 m/s and through water at 1480 m/s. Calculate the wavelength in each medium. Why is the wavelength longer in water even though sound travels faster there?

2. A sound at 50 dB is how many times more intense than the threshold of hearing (0 dB)? (Hint: Use the definition: each 10 dB = factor of 10 in intensity.)

**Application:**

3. You observe an ambulance siren shift from 1200 Hz (approaching) to 800 Hz (receding). The speed of sound is 343 m/s. Assuming the ambulance's speed is the same in both cases, estimate its speed. (This requires setting up two Doppler equations and solving simultaneously.)

4. A rock concert measures 110 dB at the front row. The threshold of hearing is 0 dB. Express the physical intensity ratio (not in dB) between the concert and the quietest audible sound.

**Synthesis:**

5. Why does a foghorn produce a lower pitch than a whistle, even if both create the same frequency sound wave? (Consider the role of pressure amplitude, medium, and how intensity relates to perception.)

6. A bat echolocates by emitting ultrasonic clicks (40 kHz) and listening for echoes. As the bat approaches a moth, the returning echo is Doppler-shifted. Explain why the bat hears a higher frequency in the echo than it emitted, and why this might help it track faster prey.

**Challenge:**

7. A supersonic jet flies overhead at Mach 2 (twice the speed of sound). Describe the shock wave it creates, and explain why you hear the boom *after* the jet has passed, not when it reaches you.

---

## Chapter Summary

Sound is a longitudinal pressure wave that propagates through matter. Its speed depends on the medium's rigidity and density, not on frequency — all frequencies travel at the same speed in a given medium at a given temperature.

The intensity of a sound wave scales with pressure amplitude squared. Because the human ear responds logarithmically to intensity, we measure sound on the decibel scale, which compresses the enormous range from the threshold of hearing (0 dB) to deafening levels (120 dB+) into a scale that reflects perceptual reality.

The Doppler effect occurs because motion between source and observer changes the wavelength of the waves without changing their speed. Compression of wavelengths yields higher observed frequency (higher pitch); stretching yields lower frequency. At supersonic speeds, the effect is extreme: shock waves pile up, producing sonic booms.

These three concepts — wave propagation through matter, logarithmic perception, and motion-induced frequency shift — explain most of everyday acoustic phenomena and the design of technologies from microphones to radar.

---

## Connections Forward

The next chapter explores how sound waves interact with objects and spaces: reflection, refraction, diffraction, and how these behaviors shape music and speech in rooms. You'll see that the speed of sound, the wavelength, and the properties of the medium determine which frequencies "fit" in a space and which get absorbed. This is why a cathedral rings and a carpeted studio is dead — very different acoustics, same sound.

You'll also learn about resonance: how objects oscillate best at their natural frequency. This explains why bridges can collapse from marching troops (frequency matching) and why certain musical notes make wine glasses vibrate themselves to pieces.

---

**What would change my mind:** If it could be shown that the speed of sound depends on frequency in a given medium at fixed temperature, the entire framework would need revision. But this has been consistently disproven. The speed is a property of the medium, not the signal.

**Still puzzling:** Why the human ear's logarithmic response evolved to have *exactly* the range it has (roughly 120 dB from threshold to pain) is not fully understood. There may be an optimization principle at work, but the details elude me.

**Tags:** #longitudinal-waves #intensity #decibels #doppler-effect #pressure-waves #sound-propagation #acoustic-perception #first-principles

---

*Byline: Nik Bear Brown*

*This chapter explains sound from first principles: the machinery of pressure waves, the logarithmic nature of human hearing, and the Doppler effect as a consequence of relative motion. Each section unpacks one mechanism fully rather than surveying many partially. The voice is that of a curious companion figuring out the subject alongside the reader, not a lecturer dispensing facts.*
---

## LLM Exercise — Chapter 14: Sound (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the Doppler effect demo — using a phone, a passing car, or a swung sound source.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 14 demo. Notebook in this Claude Project. Chapter 14
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
- One real-world application: doppler radar for weather, or
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

**Connection to previous chapters:** Ch 13's wave concepts; Ch 14 specializes to sound and adds the Doppler effect.

**Preview of next chapter:** Chapter 15 is light. You'll do a refraction demo with a glass of water (the broken-pencil illusion) and a dispersion demo with a CD (which acts as a diffraction grating producing a rainbow).


---

## AI Wayback Machine

**Ernst Chladni** discovered the patterns of vibrating plates in 1787 — visible nodes that founded the modern study of acoustics.

**Run this:**

```
Who is Ernst Chladni, and how does their work connect to sound we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Ernst Chladni"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Ernst Chladni's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Ernst Chladni's framework."

What changes? What gets better? What gets worse?
