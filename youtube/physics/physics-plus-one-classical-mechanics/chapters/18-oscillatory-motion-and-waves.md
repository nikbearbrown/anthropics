# Chapter 18 — Oscillatory Motion and Waves

*One equation, applied everywhere: $F = -kx$.*

---

## A Connecticut quartz factory, 32,768 vibrations per second

Inside a Seiko quartz wristwatch sits a small fork-shaped sliver of crystalline silicon dioxide, machined to about 5 mm long, lacquered, and sealed in vacuum. A tiny voltage from the battery sets the fork vibrating. The crystal is cut so its natural mechanical resonance is exactly $2^{15} = 32{,}768 \text{ Hz}$ — chosen because dividing by 2 fifteen times gives 1 Hz, which the watch circuitry uses to advance the seconds hand.

The accuracy is stunning. A good quartz watch keeps time to about 15 seconds per month — roughly one part in $10^5$. The mechanism is ancient. It is the same mechanism that lets a child on a swing time their kicks to build amplitude: a small periodic push at the system's natural frequency makes the response grow. Take the push away and the system rings down, slowly, at exactly the same frequency.

That single fact — every restoring system has a natural frequency, and pushing it at that frequency builds large response — is the lever this chapter pulls. Pulled correctly, it predicts how a mass on a spring bounces, how a pendulum ticks, how a guitar string sings, and why the Tacoma Narrows Bridge collapsed in 1940. One equation, many consequences.

---

## Hooke's law and simple harmonic motion

In 1660, Robert Hooke was working out the mathematics of springs, trying to understand how a coiled spring could regulate the rate of a pocket watch. He found that for small displacements, the restoring force of a spring is proportional to how far you've stretched or compressed it:

$$F = -kx.$$

$k$ is the spring constant in N/m. The negative sign means the force always points back toward equilibrium — stretch the spring and it pulls back, compress it and it pushes back. Hooke published this as a Latin anagram — *ceiiinosssttuv* — to stake a priority claim without sharing the result. Two years later he revealed the unscrambling: *ut tensio, sic vis*, "as the extension, so the force."

The reason this transcends spring design is that *almost any restoring force, near equilibrium, looks like Hooke's law*. Pull an atom slightly from its lattice site in a crystal, and the neighboring atoms pull it back — linearly, for small displacements. Tilt a pendulum slightly off vertical; gravity's component along the arc is approximately proportional to the displacement. Compress the air in front of a speaker; the air springs back. The reason is mathematical: any smooth potential energy curve near its minimum looks like a parabola (the quadratic term is the first non-zero term in the Taylor expansion), and the gradient of a parabola is a linear force. Hooke's law for a spring is one special case of a general fact about any system near stable equilibrium.

Now apply Newton's second law. A mass $m$ displaced by $x$ experiences $F = -kx$, so $m\ddot{x} = -kx$, or

$$\ddot{x} + \frac{k}{m}x = 0.$$

The solution, for displacement $x_0$ at $t = 0$ and zero initial velocity, is

$$x(t) = x_0 \cos(\omega t),$$

where the **angular frequency** is

$$\omega = \sqrt{\frac{k}{m}},$$

the **period** is

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}},$$

and the **frequency** in cycles per second is $f = 1/T$.

Three things about this result.

First: the period depends on $m$ and $k$, but not on the amplitude $x_0$. Pull the spring 1 cm or 10 cm and it oscillates at the same frequency. This is the isochronism of the harmonic oscillator — what makes it useful as a clock. Galileo noticed it for pendulums in 1583 (supposedly watching a chandelier swing in Pisa Cathedral, timing the swings against his pulse). The period was the same regardless of how wide the chandelier swung.

Second: heavier masses oscillate slowly, stiffer springs oscillate fast. Both are intuitive. The formula gives the quantitative dependence.

Third: the formula gives a definite number before you run the experiment. For the quartz crystal in the watch: $k$ is the elastic stiffness of the cut crystal, $m$ is its mass, and the manufacturer cuts the crystal until $f = \sqrt{k/m}/(2\pi) = 32{,}768 \text{ Hz}$. The formula is the design specification.

<!-- → [CHART: two displacement-vs-time curves on the same axes — one with large amplitude x₀ = 10 cm (tall sinusoid), one with small amplitude x₀ = 1 cm (short sinusoid); both have identical periods T; annotate that period T = 2π√(m/k) is the same for both; caption: "isochronism — the period is independent of amplitude; this is what makes oscillators useful as clocks"] -->

---

## Energy, pendulums, and damping

A harmonic oscillator has two energy reservoirs that swap back and forth. Kinetic energy $KE = \frac{1}{2}mv^2$ lives in the moving mass. Potential energy $PE = \frac{1}{2}kx^2$ lives in the deformed spring. The total mechanical energy

$$E = \frac{1}{2}kx^2 + \frac{1}{2}mv^2$$

is constant when friction is absent. At maximum displacement ($x = x_0$), the mass is momentarily at rest — all energy is potential. At the equilibrium point ($x = 0$), the spring is relaxed — all energy is kinetic. The maximum speed follows from energy conservation:

$$\frac{1}{2}mv_\text{max}^2 = \frac{1}{2}kx_0^2 \implies v_\text{max} = x_0\sqrt{\frac{k}{m}} = x_0 \omega.$$

<!-- → [CHART: two panels on the same time axis — top panel: displacement x(t) = x₀cos(ωt), a cosine wave; bottom panel: kinetic energy (½mv²) and potential energy (½kx²) as two curves that are exactly out of phase, with their sum (total energy E) as a flat horizontal line; annotate "all PE, v=0" at the crests and "all KE, x=0" at the zero crossings; caption: "energy sloshes back and forth between kinetic and potential twice per cycle — the total never changes"] -->

The pendulum is a harmonic oscillator in disguise. For a pendulum of length $L$, mass $m$, the restoring force along the arc is $F = -mg\sin\theta \approx -mg\theta$ for small angles $\theta$. The arc length displacement is $s = L\theta$, so $F \approx -(mg/L) s$. The effective spring constant is $k_\text{eff} = mg/L$, and substituting into the mass-spring formula:

$$T = 2\pi\sqrt{\frac{m}{k_\text{eff}}} = 2\pi\sqrt{\frac{m}{mg/L}} = 2\pi\sqrt{\frac{L}{g}}.$$

Notice what is not in this formula: the mass $m$ has cancelled. A heavier pendulum bob does not change the period. This is the pendulum's most counterintuitive property, and it follows directly from the same cancellation that makes all objects fall at the same rate under gravity. Galileo demonstrated it by hanging two pendulums of different mass side by side and watching them keep lockstep.

A one-meter pendulum at Earth's surface: $T = 2\pi\sqrt{1.00/9.80} \approx 2.01 \text{ s}$. This is approximately why pendulum clocks are about a meter tall — the pendulum ticks once per second, and the case must fit the full swing.

Real oscillators lose energy. Add a damping force $-bv$ proportional to velocity and three regimes appear:

**Underdamped.** Damping is small. The system oscillates many cycles, with amplitude decaying exponentially. Tuning forks, musical instruments, the quartz crystal itself (which damps very slowly — that is why it keeps accurate time). The frequency is slightly less than the undamped value: $\omega_d = \sqrt{\omega_0^2 - (b/2m)^2}$.

**Critically damped.** $b$ is tuned to a specific value where the system returns to equilibrium as fast as possible *without overshooting*. Car shock absorbers. Door closers. The fastest return to rest without ringing.

**Overdamped.** $b$ is large. The system creeps slowly back toward equilibrium without oscillating. Very viscous systems.

A car suspension is designed to be slightly underdamped — it should settle quickly but not ring. When the shock absorbers wear out, the suspension becomes more underdamped: every bump produces a long bouncing oscillation. When the dampers clog with old oil, the ride becomes overdamped: the car wallows slowly in and out of every pothole. Tuning the damping is the engineer's job; the three regimes are the physicist's map.

<!-- → [CHART: three displacement-vs-time curves on the same axes — underdamped: oscillates with exponentially decaying envelope (many cycles visible); critically damped: returns to zero in minimum time without crossing zero; overdamped: creeps slowly back to zero from one side, slower than critical; all three start from the same initial displacement x₀; annotate each curve; caption: "same initial displacement, three fates — the damping coefficient b decides which regime you're in"] -->

---

## Waves

Now extend oscillation from a single mass to a medium.

When oscillation propagates through a medium — a string, air, water — it becomes a wave. The key insight about waves is easy to state and easy to forget: the wave is a propagating *pattern*, not a propagating *substance*. When a wave passes through water, the water molecules oscillate up and down; they do not travel with the wave. A cork on the surface of a wave bobs; it barely moves horizontally. The disturbance travels; the medium stays.

The basic vocabulary:

- **Wavelength** $\lambda$: distance between consecutive crests.
- **Frequency** $f$: number of crests passing a fixed point per second.
- **Period** $T = 1/f$: time between consecutive crests at a fixed point.
- **Amplitude** $A$: maximum displacement of the medium.
- **Wave speed** $v$: how fast the pattern moves.

The fundamental relationship:

$$v = f\lambda.$$

In one period $T$, the wave advances one wavelength $\lambda$. So wave speed = distance/time = $\lambda/T = \lambda f$.

Two structural types of waves. In a **transverse wave**, the medium oscillates perpendicular to the direction of travel — waves on a string, light. In a **longitudinal wave**, the medium oscillates parallel to the direction of travel — compressions and rarefactions moving through air, sound.

<!-- → [DIAGRAM: two panels — left: transverse wave on a string, with horizontal arrows showing the wave traveling right and vertical arrows on each segment of string showing the medium oscillating up and down (perpendicular); right: longitudinal sound wave in air, with horizontal arrows showing the wave traveling right and the air molecules shown as dots compressed and rarefied in the same horizontal direction; label each type; caption: "the wave travels the same direction in both — what differs is which direction the medium moves"] -->

The wave speed depends on the medium, not on the frequency or amplitude. For a wave on a string under tension $T$ with mass per unit length $\mu$:

$$v = \sqrt{\frac{T}{\mu}}.$$

For sound in air at room temperature: $v \approx 343 \text{ m/s}$. For light in vacuum: $v = 2.998 \times 10^8 \text{ m/s}$.

A worked example. You see lightning. Five seconds later, you hear thunder. Light travels at $3 \times 10^8 \text{ m/s}$ — the flash arrives essentially instantaneously. Sound travels at $343 \text{ m/s}$.

$$d = v_\text{sound} \times t = 343 \times 5 \approx 1{,}715 \text{ m} \approx 1.7 \text{ km}.$$

Or: about $1 \text{ km}$ for every $3$ seconds of delay. The lightning is roughly a mile away.

When a wave reflects from a boundary and overlaps itself, the result is a **standing wave** — a pattern that oscillates in place. A guitar string fixed at both ends can sustain standing waves only at wavelengths where the string length is a half-integer multiple of $\lambda$. The lowest mode (fundamental) has wavelength $\lambda = 2L$; the higher modes (harmonics) have $\lambda = L, 2L/3, L/2, \ldots$. The corresponding frequencies are

$$f_n = \frac{nv}{2L}, \quad n = 1, 2, 3, \ldots$$

This is a harmonic series, and its structure is responsible for musical timbre. Pluck a guitar string and you excite the fundamental plus a decaying superposition of harmonics; different instruments emphasize different harmonics, which is what makes a middle C on a piano sound different from the same note on a violin.

<!-- → [DIAGRAM: a guitar string of length L fixed at both ends — show the first four standing wave modes stacked vertically; mode 1 (n=1): one half-arch, λ=2L, f₁; mode 2 (n=2): two half-arches, λ=L, f₂=2f₁; mode 3: three half-arches, f₃=3f₁; mode 4: four half-arches, f₄=4f₁; label each with its wavelength and frequency; caption: "the string can only oscillate at wavelengths where an integer number of half-waves fits between the fixed ends — this is the harmonic series"] -->

The intensity of a wave — power per unit area — falls off with the inverse square of distance from a point source:

$$I = \frac{P}{4\pi r^2}.$$

Sound, light, gravity — any wave spreading spherically from a point source obeys this law. Walk twice as far from a speaker and the intensity drops by a factor of four. This is not because the wave is dying; it is because the same power is being distributed over a sphere of four times the area.

---

## One equation, many systems

Return to the thread. Three things in this chapter — mass on a spring, pendulum, wave on a string — all reduce to the same differential equation: displacement oscillates as a cosine (or sine) at a single characteristic frequency. The frequency is set by the ratio of the restoring-force strength to the inertia:

- Spring: $\omega = \sqrt{k/m}$.
- Pendulum: $\omega = \sqrt{g/L}$.
- Wave on string: $\omega = v k$ where $k = 2\pi/\lambda$ is the wave number.

In each case, the denominator is some form of inertia (mass, or mass per length) and the numerator is some form of stiffness (spring constant, gravity, tension). The structure is always the same.

The deepest consequence of this is resonance. Every harmonic oscillator has a natural frequency. Apply a periodic driving force at that frequency and the response grows. If damping is small (the system is underdamped), the amplitude can grow until it is limited only by nonlinearity or structural failure. This is why bridges must avoid resonance with wind, why wine glasses shatter at the right note from a soprano, and why MRI machines use magnetic resonance — they drive hydrogen atoms at the precise frequency at which those atoms naturally oscillate in the magnetic field.

Taipei 101 — a 508-meter skyscraper in earthquake- and typhoon-prone Taiwan — has a natural sway frequency around $0.15 \text{ Hz}$ (period about $6.7 \text{ s}$). The architects installed a 660-tonne steel pendulum at the top, tuned to the same frequency. When the building sways east, the pendulum swings west; the pendulum's inertia exerts a force that pushes the building back toward vertical. The pendulum length:

$$L = \frac{T^2 g}{4\pi^2} = \frac{(6.7)^2 (9.80)}{4\pi^2} \approx 11 \text{ m}.$$

This is a **tuned-mass damper** — the engineering answer to resonance. The building still has a natural frequency; the damper ensures that when that frequency is excited (by wind or earthquake), the energy is absorbed rather than amplified. Same physics as a child on a swing, applied in reverse.

<!-- → [DIAGRAM: cross-section schematic of Taipei 101's upper floors — show the building structure with a large sphere (labeled "660-tonne tuned-mass damper, L ≈ 11 m") suspended by cables; two frames side by side: left shows building swaying right while damper swings left; right shows the opposite; arrows indicate the reaction force the damper exerts on the building opposing the sway; caption: "the damper is tuned to the building's natural sway period — when the building goes one way, the pendulum goes the other, absorbing the resonant energy"] -->

The quartz watch, the pendulum clock, the guitar string, the skyscraper — all of them are restoring-force systems. All of them have a natural frequency set by $\sqrt{\text{stiffness/inertia}}$. All of them respond to periodic driving; all of them damp over time. The phenomenon is not special to any one physical system. It is the universal behavior of stable equilibria disturbed slightly from rest.

<!-- → [TABLE: four-column reference table of harmonic systems — rows: mass-spring, pendulum, wave on string, LC circuit (preview of Ch 23), atomic bond vibration; columns: system, restoring force, effective k, effective m, natural frequency formula; caption: "the same structure, ω = √(stiffness/inertia), appears across mechanical, acoustic, electrical, and molecular systems — different physics, one equation"] -->

Feynman put the point bluntly in his lectures: the simple harmonic oscillator is the most important problem in physics. Not because it appears in isolation, but because every complicated system, analyzed carefully near any one of its many equilibria, turns out to be a collection of weakly coupled harmonic oscillators. Quantum field theory does this; molecular dynamics does this; acoustics does this. The world oscillates.

---

## Exercises

### Warm-up

**18.1** A $0.20 \text{ kg}$ mass on a spring oscillates with period $0.50 \text{ s}$. What is the spring constant?

**18.2** A pendulum on the Moon ($g_\text{Moon} = 1.62 \text{ m/s}^2$) is $1.00 \text{ m}$ long. What is its period?

**18.3** A wave on a string has frequency $500 \text{ Hz}$ and wavelength $0.40 \text{ m}$. What is its speed?

**18.4** A $0.50 \text{ kg}$ mass on a spring ($k = 100 \text{ N/m}$) is pulled $0.10 \text{ m}$ from equilibrium and released. What is its maximum speed?

### Application

**18.5** A car of mass $1200 \text{ kg}$ sits on four identical springs. Push it down and release; it bounces with period about $0.80 \text{ s}$. What is the spring constant of each spring?

**18.6** A car shock absorber should be critically damped. If it becomes underdamped (worn), describe what the driver feels going over a bump. If it becomes overdamped (clogged), describe what the driver feels.

**18.7** A guitar's high-E string has fundamental $329.6 \text{ Hz}$. The string is $0.65 \text{ m}$ long. What is the wave speed on the string? Compare to the speed of sound in air ($343 \text{ m/s}$).

**18.8** You build a pendulum exactly $0.50 \text{ m}$ long and observe a period of $1.42 \text{ s}$. What is the local value of $g$?

### Synthesis

**18.9** A child on a swing has effective length $2.5 \text{ m}$. (a) What is the natural period? (b) An adult pushes the swing at intervals matching that period. After 5 pushes, the amplitude has built to $1 \text{ m}$. Ignoring damping, what energy did each push deliver on average?

**18.10** A piano A above middle C is $440 \text{ Hz}$. You strike it; the sound reaches your ear $0.10 \text{ s}$ later. (a) How far is the piano? (b) What is the wavelength of the sound in air? (c) What is the wavelength of the same frequency in water (sound speed $\approx 1480 \text{ m/s}$)?

**18.11** The 1940 Tacoma Narrows Bridge collapsed under a steady $19 \text{ m/s}$ wind. The standard textbook story attributes this to resonance, but engineers now agree it was *aeroelastic flutter*. Without doing detailed math, explain the difference in one paragraph: what is resonance, what is flutter, and why does flutter not require the wind to oscillate?

### Challenge

**18.12** A quartz crystal in a wristwatch resonates at $32{,}768 \text{ Hz}$. The watch keeps time to about $15 \text{ s/month}$. (a) Express the timekeeping accuracy as a fractional uncertainty in frequency. (b) Estimate the quality factor $Q$ needed for this accuracy. (c) Compare to a typical pendulum's $Q$ ($\sim 100$) and a tuning fork's $Q$ ($\sim 1{,}000$).

**18.13** Two identical pendulums of length $1.0 \text{ m}$ are coupled by a weak spring connecting their bobs. If you start one swinging and leave the other at rest, energy slowly transfers back and forth — a "beating" pattern. Sketch the amplitudes of both pendulums over time. Explain qualitatively why the energy-transfer rate depends on the strength of the coupling spring.

---

## LLM Exercise — Chapter 18: Find the Oscillation in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** Identification of one oscillatory or wave-like component of your anchor phenomenon, with computed period, frequency, and wavelength as appropriate.  
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 18 (Oscillations and Waves), I want to find ONE periodic or wave-like component of my phenomenon and analyze it.

Please:

1. Identify the oscillation. Examples:
   - Bike commute: pedal cadence (cyclic crank rotation), or the bike's natural wheel-and-spring suspension frequency.
   - Coffee maker: thermostat heating cycle frequency.
   - Marathon: cardiac frequency (heart rate), respiratory rate, stride frequency.
   - Espresso machine: pump pulsation frequency, or the resonance of the boiler.
   - Basketball shot: the wobble frequency of the ball's spin.

2. Identify the underlying restoring mechanism. Is it Hooke's-law-like (a spring or pendulum)? A driven oscillator (heart muscle pacemaker)? A wave (sound)?

3. Compute the period and frequency. State inputs and uncertainty.

4. If it's a wave, also compute the wavelength using v = fλ.

5. Identify the damping in the system. Is it underdamped (rings for many cycles), critically damped (settles fast), or overdamped (creeps back)?

6. Identify whether resonance is helping or hurting the system.

7. Connect to Chapter 19 (Sound), where we extend wave physics to acoustics.

Save the output as logbook/chapter-18-oscillations.md.
```

### What this produces

Your eighteenth Logbook entry — a quantified periodic component of your phenomenon.

### How to adapt this prompt

- *For phenomena with no obvious oscillation:* every system has a natural frequency. A coffee cup has a "ringing" frequency if you tap it; a bike frame has a vibrational mode; a marathon runner has stride and heartbeat frequencies. Find one.
- *For Claude Code:* If you have an audio recording or accelerometer log, fit a Fourier transform and extract the dominant frequency.

### Connection to previous chapters

Builds on Chapters 4–9 (Newton's laws, work and energy). The energy-conservation argument for max velocity uses Chapter 9 directly.

### Preview of next chapter

Chapter 19 zooms in on sound waves specifically — speed, intensity, the decibel scale, hearing, Doppler effect. The Chapter 19 LLM Exercise will analyze the acoustic component of your phenomenon.

---

## AI Wayback Machine

**Robert Hooke** worked out the law of elasticity in 1660 — the stress-strain relationship for springs that still bears his name. He published it as the anagram "ceiiinosssttuv" before revealing the law to ensure priority.

**Run this:**

```
Who was Robert Hooke, and how does Hooke's law connect to the oscillatory motion we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Robert Hooke"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through why a spring obeying Hooke's law produces simple harmonic motion when displaced.
- Ask it about Hooke's bitter rivalry with Isaac Newton and how it shaped his historical reputation.

What changes? What gets better? What gets worse?
