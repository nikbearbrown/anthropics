# Chapter 16 — Waves and Their Properties
*What crosses the ocean when nothing moves.*

---

A seagull floats on the ocean. A wave rolls in from the horizon — a visible ridge of water, moving steadily toward shore. The wave reaches the seagull. The bird bobs up, then down, then settles back to where it was. The wave continues toward shore without the seagull.

Here is the puzzle: something moved across the ocean. You watched it. But the seagull — which is sitting on the water — barely moved at all. If the water had traveled, the seagull would have traveled. It didn't. So what, exactly, crossed the ocean?

That question is the whole chapter.

---

## What Is Actually Moving

The answer, once you see it, is almost embarrassing in its simplicity: the *disturbance* traveled. Not the water. The pattern of the disturbance.

<!-- → [IMAGE: two-panel illustration — left panel shows a seagull before wave arrival at resting water level; right panel shows the same seagull mid-bob as a crest passes beneath, with arrows showing the wave pattern moving horizontally and the bird moving vertically. Caption: the seagull's vertical motion traces the oscillation of the water at one point; the horizontal arrow shows what actually travels.] -->

Let me make that concrete. Imagine you're holding one end of a long rope, and the other end is tied to a wall. You give your end a single sharp flick — up, then back to center. A kink travels along the rope toward the wall. Watch carefully: no piece of rope travels from your hand to the wall. Every piece of rope moves perpendicular to the rope's length — up, then back down — and then it's done. The kink, the *pattern* of disturbance, is what travels. The rope itself just delivers the message and stays home.

This is the essential thing about waves, and it's worth sitting with until it feels obvious rather than strange. A wave is not a thing being transported. It is a pattern being passed along — from one piece of the medium to the next, through a chain of pushes.

Here is the machinery: you disturb a piece of the medium. That piece is now out of its resting position. The medium has a restoring force — gravity for water, tension for a rope, pressure for air — that pulls it back. But it overshoots, because it has inertia. So it passes through its resting position and ends up on the other side. Then the restoring force pulls it back again. The piece oscillates, back and forth, around its equilibrium.

But while it's oscillating, it's in contact with neighboring pieces. As it moves, it pulls or pushes on them. Those neighbors, disturbed by the first piece, begin to oscillate a moment later. Then they disturb *their* neighbors. The disturbance propagates outward, like a rumor that each person passes to the next — while staying where they are.

The seagull is not an anomaly. It is the rule. Every piece of the medium oscillates. The pattern moves.

---

## The Numbers That Describe a Wave

Once you see that a wave is an oscillation being passed along, you need four numbers to describe it completely.

The first is **amplitude** — how far each piece of the medium swings from its resting position. For a water wave, it's the height of the crest above the undisturbed surface, or equivalently, the depth of the trough below it. Amplitude is what you feel as intensity. Loud sound has large amplitude pressure variations. Bright light has large amplitude field oscillations. A big ocean wave has large amplitude. Amplitude is determined by how much energy you put in at the source.

The second is **frequency** — how many complete oscillations each piece of the medium goes through per second. The unit is hertz (Hz), where 1 Hz means one complete cycle per second. The seagull in our ocean wave was bobbing about once every five seconds, which is a frequency of 0.2 Hz. A concert A is 440 Hz — your eardrum goes through 440 complete oscillations every second. Frequency is what you perceive as pitch in sound and as color in light.

The third is **period** — the time for one complete oscillation. Period and frequency are inverses of each other:

$$T = \frac{1}{f}$$

If the frequency is 440 Hz, the period is $1/440$ second, about 2.3 milliseconds. If the seagull bobs once every 5 seconds, the period is 5 seconds and the frequency is 0.2 Hz. These are two ways of saying the same thing.

The fourth is **wavelength** — the distance between two adjacent identical points in the pattern. Crest to crest. Trough to trough. Any point on one cycle to the identical point on the next. Wavelength is measured in meters.

<!-- → [IMAGE: labeled diagram of a single sinusoidal wave — horizontal axis is distance, vertical axis is displacement. Annotations pointing to: one full wavelength (λ) measured crest to crest; amplitude (A) measured from equilibrium to crest; one complete cycle shaded. Caption: amplitude and wavelength are independent — a wave can be tall and short, or shallow and long.] -->

Now here is the relationship that locks all four together. In one period — the time for one complete oscillation — the disturbance travels exactly one wavelength. That is not a coincidence or a special case; it is definitional. The pattern repeats in space with period $\lambda$, and it repeats in time with period $T$. The speed of propagation is therefore:

$$v_w = \frac{\lambda}{T} = f\lambda$$

The wave speed equals frequency times wavelength.

This equation is not a recipe for making waves go faster. It is a constraint. The speed of a wave is set by the medium — by the tension and mass of the rope, the density and compressibility of the air, the depth and gravity of the ocean. Once the medium is fixed, the speed is fixed. If you increase the frequency, the wavelength must decrease to keep the product constant. Higher pitch means shorter wavelength. Longer wavelength means lower frequency. They are not independent.

This is why a loudspeaker's tweeter — the small driver that handles high frequencies — is small: it is built to the scale of the short wavelengths it produces. The woofer, for low frequencies, is large. Both produce sound that travels through the same air at the same speed. The geometry of the wave is different.

<!-- → [TABLE: three-column reference table — wave type, typical frequency range, typical wavelength range. Rows: audible sound (20 Hz–20 kHz, 17 m–17 mm), visible light (430–770 THz, 700–390 nm), AM radio (540–1600 kHz, 555–188 m), ocean surface waves (0.05–0.3 Hz, 5–600 m). Caption: all governed by v = fλ; the speed differs because the medium differs.] -->

---

## Two Kinds of Waves

So far I've talked about waves without specifying which direction things oscillate. There are two fundamentally different possibilities, and it matters.

In a **transverse wave**, the medium oscillates perpendicular to the direction the wave travels. The rope wave is transverse: the rope moves up and down, the disturbance travels sideways along the rope. Light waves are transverse: the electric and magnetic fields oscillate perpendicular to the direction of propagation. Ocean surface waves are approximately transverse.

In a **longitudinal wave**, the medium oscillates *along* the direction the wave travels. Sound is the canonical example. A sound wave moving through air is a pattern of compressions and rarefactions — regions where air is squeezed together (higher pressure) and regions where it is spread apart (lower pressure) — moving outward from the source. The air molecules oscillate back and forth along the direction the sound travels. The disturbance propagates in the same direction as the oscillation.

<!-- → [IMAGE: side-by-side comparison — top panel shows a transverse wave on a rope with arrows indicating particle motion (vertical) vs. wave travel direction (horizontal); bottom panel shows a longitudinal wave in air with compression/rarefaction bands and arrows indicating particle motion (horizontal, same axis as travel). Caption: same wave equation governs both; only the geometry of oscillation differs.] -->

A slinky demonstrates both. Send a sideways kink along it: transverse wave. Compress a few coils and release: longitudinal wave. The coils oscillate differently, but in both cases, it's the pattern that travels, not the coils.

Transverse waves can only exist in media that resist shearing — that push back when you try to slide one layer past another. Solids resist shear, so transverse waves can travel through solid rock. Liquids and gases don't resist shear (that's part of the definition of a fluid), so only longitudinal waves can travel through them. This is not a minor technical detail. It is why seismologists can determine that Earth's outer core is liquid: transverse seismic waves (called S-waves) cannot pass through it. They disappear on the far side. Geologists learned the internal structure of Earth by watching which waves arrive at distant seismometers and which don't.

---

## What Happens When Waves Collide

Here is something that should seem strange but is true: waves pass through each other.

Drop two stones into a still pond, a meter apart. Two sets of circular ripples expand from the impact points and collide in the middle. Watch the collision point carefully. There is no bouncing, no scattering, no explosion. After the collision, the two patterns continue outward, each looking exactly as it would have if the other stone had never been dropped.

Waves pass through each other as though the other wave doesn't exist. This is deeply unlike particles, which do bounce off each other. It is one of the defining characteristics of waves.

But while two waves overlap, in the region where they coexist, something interesting happens. The displacement at any point is the sum of the displacements from each wave individually. This is called **superposition**, and it follows directly from the fact that forces add. If wave A pushes the water up by 0.4 meters and wave B, arriving at the same moment, pushes it up by 0.3 meters, the water rises 0.7 meters. If wave A pushes up and wave B pushes down by equal amounts, the water doesn't move at all — momentarily flat, even though two waves are passing through it.

The first case is **constructive interference**: crest meets crest, and they add. The second is **destructive interference**: crest meets trough, and they cancel. What you actually get at any given point depends on the relative timing — the phase — of the two waves when they arrive.

<!-- → [IMAGE: three-panel diagram showing superposition — top panel: wave A alone (amplitude 1); middle panel: wave B alone (amplitude 1); bottom panel: their sum, showing constructive interference at one location (amplitude 2) and destructive interference at another (amplitude 0). Caption: superposition is arithmetic — the displacements simply add. The waves do not interact; they pass through each other and the medium responds to both simultaneously.] -->

This has consequences everywhere. Two speakers playing the same frequency in the same room produce loud spots (where waves from both speakers arrive in phase) and quiet spots (where they arrive out of phase). If you've walked through a room with two speakers and noticed the volume change as you moved, that's interference. Noise-canceling headphones measure the incoming sound and generate a wave with exactly the opposite phase. Destructive interference. The two waves cancel in your ear canal, and the noise disappears.

Interference is not an exotic phenomenon. It is how waves work.

---

## Standing Waves: Interference's Most Beautiful Consequence

Pluck a guitar string and let go. The disturbance travels to the fixed end, where the string is attached to the bridge, and bounces back. It travels to the other fixed end and bounces back again. The string is now full of waves traveling in both directions, superposing continuously.

The result is a **standing wave** — a pattern that appears to vibrate in place rather than travel. Some points on the string never move at all: these are **nodes**. Other points oscillate with maximum amplitude: **antinodes**. The fixed endpoints are always nodes, because the string cannot move there. The pattern between them depends on the frequency.

The fixed ends impose a constraint: a whole number of half-wavelengths must fit exactly between them. A string of length $L$ can sustain standing waves at wavelengths $\lambda = 2L, L, 2L/3, L/2, \ldots$ — in other words, at wavelengths $\lambda_n = 2L/n$ for any positive integer $n$. The corresponding frequencies are $f_n = v/\lambda_n = nv/2L$. The lowest frequency ($n=1$) is called the **fundamental**; the others are **harmonics** or **overtones**.

<!-- → [IMAGE: four-panel diagram of standing wave harmonics on a fixed string of length L — panels show n=1 (fundamental, one antinode), n=2 (one node in middle, two antinodes), n=3, n=4. Each panel labels nodes (N) and antinodes (A) and shows the wavelength. Caption: only wavelengths that fit a whole number of half-cycles between the fixed ends are permitted — this is why strings produce discrete pitches rather than a continuous smear of frequency.] -->

This is the physics of musical instruments. A guitar string of length $L$, under a given tension (which sets the wave speed $v$), can only vibrate at those discrete frequencies. When you press a fret, you shorten the effective length and shift all those frequencies upward. When you loosen the string (reducing tension and therefore $v$), all frequencies shift downward. The instrument is a machine for selecting which standing waves can exist.

The same principle governs organ pipes, where standing sound waves form in air columns. It governs the resonant frequencies of drumheads (though there the geometry is two-dimensional and the math becomes more involved). It governs microwave ovens, where standing electromagnetic waves create hot and cold spots — the reason your food needs to rotate. Everywhere there are boundaries, standing waves form. Boundaries constrain wavelengths. Constrained wavelengths mean discrete frequencies. Discrete frequencies mean what we recognize as *musical* notes rather than noise.

---

## What Happens at Boundaries

When a wave hits a fixed boundary — the wall, the bridge of the guitar, the end of a pipe — it reflects. The reflected wave travels back the way it came. At a fixed end, it also inverts: a crest comes back as a trough. This inversion is not arbitrary. It follows from Newton's third law. The wave pushes on the fixed wall; the wall pushes back with equal and opposite force. The reflected disturbance is flipped.

At a free end (a boundary that can move), the reflected wave is not inverted. The open end of an organ pipe behaves this way. The wave reflects, but without flipping.

When a wave passes from one medium into another — sound from air into water, light from air into glass, ocean waves from deep water into shallow water — something more interesting happens: the wave **refracts**. It bends.

Here is why. On one side of the boundary, the wave moves at speed $v_1$. On the other side, it moves at speed $v_2$. The wavefronts — the lines of constant phase — must remain connected across the boundary. If $v_2 < v_1$, the part of the wavefront that has entered the new medium slows down while the rest is still moving fast. The wavefront bends toward a line perpendicular to the boundary. This is exactly what happens when you look at a straw in a glass of water: light from the straw travels faster in air than in water, bends at the surface, and your eye traces it back along the bent path to an apparent position that doesn't match the real one.

<!-- → [IMAGE: top-down diagram of ocean wave refraction approaching a curved coastline — parallel wavefronts in deep water arrive at an angle; as they enter shallow water (shaded), the wavefronts bend to become more parallel to the shore. Arrows show wave travel direction. Caption: the seafloor geometry, not the storm direction, determines the angle at which waves break on shore.] -->

Ocean waves refract as they approach shore. In deep water, they might be traveling at an angle to the coastline. As the leading edge of the wave enters shallower water, it slows. The trailing edge, still in deeper water, continues at full speed. The wavefront swings around, rotating toward alignment with the shore. By the time the wave breaks, it is nearly parallel to the beach — not because of the direction of the original storm, but because refraction forced the alignment.

This is why waves at almost every beach hit the shore nearly straight on. The geometry of the seafloor did the work.

---

## Waves as the Connective Tissue of Physics

Step back and look at what we have.

A wave is a disturbance that propagates by coupling oscillations at adjacent points in a medium. The medium doesn't travel. The energy does. The pattern does. The medium is the channel; the wave is the message.

Amplitude tells you how much energy the wave carries. Frequency tells you how fast each piece oscillates. Wavelength tells you the spatial scale of the pattern. Speed — determined entirely by the medium — locks frequency and wavelength together through $v = f\lambda$.

Superposition lets waves pass through each other and add. This produces interference: constructive when they reinforce, destructive when they cancel. Standing waves are a special case of interference, where the same wave, reflected back and forth, sets up a pattern of nodes and antinodes that selects certain frequencies over all others.

Boundaries cause reflection; transitions between media cause refraction. Fixed boundaries invert the reflected wave; free boundaries don't.

Why does any of this matter beyond waves on strings and water?

Because waves are how the universe moves energy from one place to another without moving matter. Sound carries speech. Light carries the energy of the Sun to Earth. Seismic waves carry information about Earth's interior that no drill has ever reached. Radio waves carry your phone call. Quantum mechanics — which we'll reach in a later chapter — describes electrons and photons as waves, with wavelengths that determine how they interact with atoms.

The wave equation, $v = f\lambda$, is one of the most compact and universal descriptions in physics. It applies to sound, light, water, strings, seismic disturbances, matter waves in quantum mechanics. Every time you encounter something that oscillates and propagates, you are looking at a wave. Learning to see waves — to ask what is oscillating, what is propagating, what frequency and what wavelength — is to acquire a lens that reveals structure in almost everything.

The seagull that barely moved while an ocean wave passed beneath it was telling you something true: what travels is not the medium. What travels is the pattern. That distinction is the whole subject.

---

## Exercises

**Warm-up**

1. A tuning fork vibrates at 256 Hz. What is its period? If sound travels at 343 m/s in air, what is the wavelength of the sound it produces? *(Tests: period–frequency inverse relationship; $v = f\lambda$.)*

2. A seagull bobs up and down with a period of 4 seconds as ocean waves pass. The crests are 6 meters apart. What is the wave speed? *(Tests: $v_w = \lambda/T$ applied directly.)*

3. A wave on a rope has amplitude 0.2 meters and wavelength 0.8 meters. A second wave on the same rope has amplitude 0.1 meters and wavelength 0.8 meters. Which wave carries more energy? Which has a higher frequency? *(Tests: independence of amplitude and wavelength; energy proportional to amplitude.)*

**Application**

4. Two speakers face each other across a 4-meter room, both playing a 430 Hz tone. Sound travels at 343 m/s. What is the wavelength of this sound? A student walks slowly from one speaker toward the other. Describe qualitatively what she hears — and why. *(Tests: $v = f\lambda$; constructive and destructive interference produced by path-length difference.)*

5. A guitar string is 65 cm long and the wave speed on it is 520 m/s. What is the fundamental frequency? What are the frequencies of the second and third harmonics? If you press a fret that shortens the string to 48.75 cm, what is the new fundamental frequency? *(Tests: standing wave harmonics $f_n = nv/2L$; effect of length on pitch.)*

6. A transverse pulse travels along a rope toward a fixed wall at 3 m/s. The pulse is a crest (upward displacement). Describe the reflected pulse: direction of travel, speed, orientation. Now repeat for a free end. *(Tests: fixed-end inversion vs. free-end reflection; speed is unchanged on reflection.)*

7. Sound travels at 343 m/s in air and 1,480 m/s in water. A sound wave in air strikes a water surface at an angle. Does it bend toward or away from the perpendicular to the surface when it enters the water? Explain using the wavefront argument. *(Tests: refraction direction from speed difference; wavefront geometry.)*

**Synthesis**

8. A 2-meter rope is fixed at both ends. You drive one end at increasing frequencies until you see the first standing wave (fundamental mode). The wave speed on the rope is 6 m/s. At what frequency does the first standing wave appear? Describe where the nodes and antinodes are. Now double the driving frequency — describe the new standing wave pattern. *(Tests: $\lambda_n = 2L/n$ and $f_n = nv/2L$; node/antinode location for $n=1$ and $n=2$.)*

9. Two identical wave pulses, each with amplitude 0.5 m, travel toward each other on a rope. At the moment they completely overlap, a student measures the rope's displacement at the center. What does she observe if the pulses are both crests? What if one is a crest and one is a trough? After they pass through each other, what do each of the pulses look like? *(Tests: superposition arithmetic; wave identity preserved after interference.)*

**Challenge**

10. Earthquakes produce P-waves (longitudinal, ~6 km/s through crust) and S-waves (transverse, ~3.5 km/s through crust). A seismometer records the P-wave arriving 85 seconds before the S-wave. Estimate the distance from the seismometer to the epicenter. Then explain why S-waves cannot pass through Earth's liquid outer core, but P-waves can. What does this tell geologists? *(Tests: relative speed and time delay to infer distance; shear resistance as condition for transverse wave propagation; application to Earth's interior structure.)*

11. A microwave oven operates at 2.45 GHz ($2.45 \times 10^9$ Hz). The speed of light is $3 \times 10^8$ m/s. What is the wavelength of the microwaves? If the oven creates a standing wave pattern, how far apart are the hot spots (antinodes)? This is why rotating turntables exist — but some ovens instead rotate the antenna. What problem does each solution address, and what does each trade off? *(Tests: $v = f\lambda$ for electromagnetic waves; standing wave antinode spacing = $\lambda/2$; design-philosophy reasoning about a real appliance.)*

---

## LLM Exercise — Chapter 16: Waves and Their Properties (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the slinky wave demos — transverse vs. longitudinal pulses, superposition, and reflection.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 13 demo. Notebook in this Claude Project. Chapter 13
taught: amplitude, frequency, wavelength, speed (v = fλ);
transverse waves (oscillation perpendicular to propagation) vs.
longitudinal (oscillation parallel); superposition (waves add);
constructive vs. destructive interference; reflection at
boundaries; standing waves.

**The Demo:** Use a slinky (or long stretchy spring) to produce
transverse and longitudinal waves, observe their behavior, and
demonstrate superposition.

**Materials:**
- A slinky (the original metal kind works best; plastic also fine)
  OR a long stretchy spring (rope alternative — works for
  transverse only).
- A long flat surface — hallway floor or table.
- A partner (helpful but not required — can wedge one end against
  a wall).
- Phone for video.

**Procedure A: Transverse pulse**

1. Stretch the slinky between you and a wall (or partner).
2. Send a transverse pulse: jerk one end perpendicular to the
   slinky's length (left-right or up-down).
3. Watch the pulse travel down the slinky and reflect off the
   far end.
4. Observation: the slinky coils move PERPENDICULAR to the
   pulse's direction of travel. The pulse moves; the coils
   oscillate in place.
5. Time the pulse round trip. Compute speed = 2L / T_round_trip.

**Procedure B: Longitudinal pulse**

1. Same setup. Now compress (push) several coils at one end and
   release.
2. The compression travels down the slinky as a longitudinal
   pulse — coils oscillate ALONG the slinky's length, not
   perpendicular.
3. Compare speed to the transverse pulse. (Often similar but
   may differ due to slinky construction.)

**Procedure C: Superposition**

1. With a partner: send a transverse pulse from each end
   simultaneously.
2. Watch what happens when the pulses meet:
   - Same-side pulses (both up, say): they ADD at the meeting
     point — peak amplitude is briefly doubled.
   - Opposite-side pulses (one up, one down): they CANCEL at
     the meeting point — momentary flat slinky.
3. Critical observation: the pulses pass through each other.
   They don't bounce off each other; they emerge unchanged on
   the other side.

**Procedure D: Reflection**

1. Send a pulse toward a fixed end (the wall).
2. Observe: the reflected pulse is INVERTED (flipped to the
   opposite side).
3. Now release the wall end (the partner lets go); send a pulse.
4. Observe: the reflected pulse is NOT inverted (same side as
   the incident pulse).

The chapter's claim: fixed-end reflection inverts; free-end
reflection doesn't. This pattern is universal across waves.

**Use Claude as a thinking partner:**
- Before: "Why would superposition pulses pass through each
  other instead of bouncing off?"
- After: "I observed [effects]. Why does the fixed-end reflection
  invert? What's happening at the boundary?"

**Notebook entry should include:**
- Photos or video stills of all four procedures.
- Measured pulse speed.
- Description of superposition behavior.
- Description of reflection inversion (with photo at the moment
  of reflection if possible).
- One application: how does noise-canceling headphones use
  destructive interference?

End with: standing waves. Find the slinky's natural standing-wave
frequency by oscillating one end at increasing rates until you
see a clear standing wave pattern. Why are some frequencies
"resonant"?
```

---

**What this produces:** A demo entry covering transverse, longitudinal, superposition, and reflection. The slinky is one of physics's most generous demo objects.

**How to adapt this prompt:**

- *For your own project:* If you don't have a slinky, a long jump rope works for transverse waves only.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Not the primary tool here.
- *For a Claude Project:* Append.

**Connection to previous chapters:** First chapter where energy travels without mass traveling. Ch 9's energy framework gets a new vehicle.

**Preview of next chapter:** Chapter 14 is sound. You'll demo the Doppler effect by swinging a buzzer in a circle (or by recording a passing car).

---

## AI Wayback Machine

**Hertha Marks Ayrton** — first woman elected to the Institution of Electrical Engineers — and her work on ripples in sand explained wave-driven coastal processes.

**Run this:**

```
Who is Hertha Marks Ayrton, and how does their work connect to waves
we covered in this chapter? Keep it to three paragraphs. End with
the single most surprising thing about their career or ideas.
```

→ Search **"Hertha Marks Ayrton"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Hertha Marks Ayrton's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Hertha Marks Ayrton's framework."

What changes? What gets better? What gets worse?
