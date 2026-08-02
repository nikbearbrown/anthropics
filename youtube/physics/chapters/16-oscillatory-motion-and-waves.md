# Chapter 16 — Oscillatory Motion and Waves

*One equation. Everything that oscillates.*

---

Here is a claim worth sitting with: a spring in your kitchen, a chandelier in Pisa Cathedral, the crystalline quartz inside a wristwatch, the air molecules in front of a speaker, the atoms in a crystal lattice, and the electrons bound in atoms — all of these, in the right limit, obey exactly the same equation of motion. The same solution, the same frequency formula, the same energy exchange, the same mathematics of resonance.

The equation is $F = -kx$. A force that pulls back toward equilibrium, proportional to how far you've moved from it. The minus sign is everything — without it, the force pushes you further away (an unstable equilibrium), and nothing oscillates. With it, you get sinusoidal motion at a single characteristic frequency determined entirely by the restoring stiffness and the amount of mass being restored.

![Top: x(t) cosine curve. Bottom: bars showing KE (½mv²) and PE (½kx²) over one period. At extremes: PE = E_total, KE = 0. At zero crossing: KE = E_total, PE = 0. Sum is always constant for an ideal oscillator.](../images/16-oscillatory-motion-and-waves-fig-02.png)
*Figure 16.2 — SHM Energy — KE and PE Swap Every Quarter Period, Total Constant*

Why does the same equation govern such different systems? Because near any stable equilibrium, any smooth potential energy function looks like a parabola — and the gradient of a parabola is a linear restoring force. The specific physics (spring tension, gravity, electromagnetic binding) determines the proportionality constant; the mathematics does the rest. This is one of those places where physics shows its hand: the apparent diversity of oscillating systems is mostly superficial. Underneath, it's all the same.

<!-- → [INFOGRAPHIC: Five different physical systems listed in a column: mass on spring, pendulum, quartz crystal tuning fork, atom in crystal lattice, LC electrical circuit. Each labeled with its effective "spring constant" expression (k, mg/L, mechanical k_crystal, interatomic force constant, 1/C). Single equation F = -kx shown connecting all five. Caption: The same restoring-force structure appears in every oscillating system. The physics differs; the mathematics is identical. This is the universality of simple harmonic motion.] -->

---

## The restoring force

Start with the simplest case. A mass $m$ hangs from a spring with spring constant $k$ (units: N/m). Pull it a distance $x$ from equilibrium and release it. The spring exerts a force:

$$F = -kx.$$

This is Hooke's law, named for Robert Hooke who extracted it from spring data in 1660 and published it as a Latin anagram — *ceiiinosssttuv*, unscrambling to *ut tensio, sic vis*, "as the extension, so the force" — to claim priority without sharing the result. The negative sign encodes the physics: the force opposes the displacement. Displaced to the right, pulled to the left. Displaced to the left, pulled to the right.

Apply Newton's second law, $F = ma = m\ddot{x}$:

$$m\ddot{x} = -kx \implies \ddot{x} + \frac{k}{m}x = 0.$$

This differential equation has the general solution:

$$x(t) = A\cos(\omega t + \phi),$$

where $A$ is the amplitude (set by initial conditions), $\phi$ is a phase offset (also set by initial conditions), and

$$\omega = \sqrt{\frac{k}{m}}$$

is the **angular frequency** in radians per second. The period — time for one full cycle — is:

$$T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}.$$

![Two SHM curves x(t) = A cos(ωt) for the same mass-spring system. Small amplitude A₁ and large amplitude A₂ traced together. Both cross zero and peak at identical times. Period T = 2π√(m/k) depends only on the system, not on...](../images/16-oscillatory-motion-and-waves-fig-01.png)
*Figure 16.1 — Isochronism — Same Spring, Different Amplitudes, Same Period*

Three things are immediately striking. First, the motion is sinusoidal — cosines and sines — which is the unique mathematical signature of a linear restoring force. Second, heavier masses oscillate more slowly, stiffer springs faster — both intuitively right. Third, and most important: *the period doesn't depend on the amplitude*. Whether you pull the mass 1 cm or 10 cm from equilibrium, it takes the same time to complete one cycle. This is what makes oscillating systems useful as clocks.

<!-- → [FIGURE: Four snapshots of mass-spring system at t = 0, T/4, T/2, 3T/4. At t=0: mass at +A (maximum displacement), v=0. At T/4: mass at 0 (equilibrium), v=v_max. At T/2: mass at -A, v=0. At 3T/4: mass at 0, v=v_max. Spring shown compressed/extended. Caption: One complete cycle of a mass-spring oscillator. The position follows x = A cos(ωt). Maximum speed occurs at x = 0; maximum displacement occurs where speed is zero.] -->

Now: the reason this matters for systems other than springs. Any smooth potential energy function $U(x)$ near a stable minimum can be Taylor-expanded:

$$U(x) \approx U(x_0) + \underbrace{U'(x_0)}_{=0} (x-x_0) + \frac{1}{2}\underbrace{U''(x_0)}_{=k}(x-x_0)^2 + \cdots$$

The constant drops out, the linear term vanishes (it's a minimum — the slope is zero), and the leading non-trivial term is the quadratic. The force is $F = -dU/dx \approx -U''(x_0)(x-x_0)$, which is Hooke's law with $k = U''(x_0)$. The second derivative of the potential at the minimum is the spring constant. Every oscillating system has one; you just have to evaluate it.

This is why atomic vibrations, pendulums, LC circuits, and acoustic resonances all follow the same mathematics. They're all sitting at the bottom of a potential well that looks like a parabola — not because nature is lazy, but because near any minimum, that's just what smooth functions look like.

<!-- → [FIGURE: Generic U(x) potential energy curve with a stable minimum at x₀. Curve shown in blue. Parabola approximation U ≈ ½k(x-x₀)² shown in dashed orange, matching the blue curve closely near x₀ but diverging at larger displacements. Labels: "true potential," "parabolic approximation," "valid for small oscillations." Caption: Near any stable equilibrium, the true potential (blue) is well approximated by a parabola (orange). The parabolic approximation gives a linear restoring force — Hooke's law — regardless of the specific physics. The approximation breaks down for large displacements.] -->

---

## Pendulums and energy

A pendulum is another restoring system, with gravity playing the role of the spring. A mass $m$ on a string of length $L$, displaced by angle $\theta$ from vertical, experiences a tangential restoring force:

$$F = -mg\sin\theta.$$

For small angles, $\sin\theta \approx \theta$ (with $\theta$ in radians), so $F \approx -mg\theta$ — Hooke's law in angular form. The effective spring constant works out to give:

$$T = 2\pi\sqrt{\frac{L}{g}}.$$

Galileo discovered the key property of this formula in 1583, supposedly watching a chandelier in Pisa Cathedral during a long Mass and timing the swings against his pulse: the period doesn't depend on the mass of the bob. A heavier pendulum and a lighter pendulum of the same length swing in lock-step. You can verify this with two pendulums of different masses hanging side by side. It's the same cancellation that makes all objects fall at the same rate in free fall — mass appears in both the force (weight) and the inertia ($F = ma$) and divides out.

Notice also that the formula predicts a specific, calculable pendulum length for any desired period. A pendulum with period 2 seconds (ticking once per second) needs length:

$$L = \frac{T^2 g}{4\pi^2} = \frac{(2)^2(9.80)}{4\pi^2} \approx 0.993 \text{ m}.$$

About 99 cm. This is approximately why grandfather clocks are about a meter tall — the mechanism is sized to the pendulum. In the 17th century, astronomers used this formula in reverse: by measuring pendulum periods at different latitudes, they found that $g$ varies, and from that inferred that Earth is slightly oblate — fatter at the equator. The equation $T = 2\pi\sqrt{L/g}$ became a precision measurement of the Earth's shape.

### Energy in an oscillator

A mass-spring system has two reservoirs of energy, and they trade back and forth every half-cycle. At maximum displacement, the mass is momentarily at rest and all energy is potential:

$$PE = \frac{1}{2}kA^2.$$

At equilibrium, all energy is kinetic and the mass is moving at its fastest:

$$KE = \frac{1}{2}mv_\text{max}^2.$$

Setting them equal (energy is conserved in an undamped oscillator):

$$v_\text{max} = A\sqrt{\frac{k}{m}} = A\omega.$$

The maximum speed is the amplitude times the angular frequency. Larger amplitude, faster motion — not a constant, which is why we can't simply say "speed is constant" in oscillatory motion the way we could in uniform circular motion.

This KE-PE trade repeats exactly twice per cycle — once going through equilibrium in each direction. It's the energy fingerprint of simple harmonic motion, and it's what connects the oscillating spring to the oscillating pendulum: both have a trade between a kinetic and potential energy term at the same frequency.

<!-- → [FIGURE: Two panels. Top: x-vs-t graph, one full cycle, with position of mass labeled. Bottom: energy-vs-t graph for same cycle, showing KE (dashed) and PE (solid) as sinusoidal curves that are π/2 out of phase, summing to a horizontal line E_total. Labels at t=0: KE=0, PE=max. At t=T/4: KE=max, PE=0. Caption: Kinetic and potential energy trade back and forth, always summing to the same total. KE is maximum when the mass passes through equilibrium; PE is maximum at the turning points.] -->

### Damping

![Three decay curves on a single set of axes starting from x = A. Underdamped: oscillates with shrinking envelope. Critically damped: returns to zero fastest without oscillating. Overdamped: returns slowly with no oscillation.](../images/16-oscillatory-motion-and-waves-fig-03.png)
*Figure 16.3 — Damping Regimes — Underdamped, Critically Damped, Overdamped*

Every real oscillator loses energy — to air drag, friction, internal material losses. Add a damping force proportional to velocity, $F_\text{damp} = -bv$, and three regimes appear depending on how large $b$ is relative to $m$ and $k$.

**Underdamped**: small $b$. The system oscillates many cycles, with amplitude decaying exponentially. A tuning fork, a bell, a quartz crystal. Ring for a while, then stop.

**Critically damped**: $b$ tuned to exactly $b = 2\sqrt{mk}$. The system returns to equilibrium as fast as possible without overshooting once. Car shock absorbers are designed for approximately this — settle the bounce fast, no lingering oscillation.

**Overdamped**: large $b$. The system creeps slowly back to equilibrium, slower than critical. A door closer filled with thick oil.

The criterion is not just about speed. Critically damped is the boundary between oscillating (under) and non-oscillating (over). Engineering the damping is how you control whether a system rings, settles, or creeps — music versus machinery versus furniture.

<!-- → [FIGURE: Three curves of displacement vs. time for underdamped, critically damped, and overdamped oscillators, all starting at x = A at t = 0. Underdamped: decaying sinusoid. Critically damped: smooth exponential decay to zero, fastest without crossing zero. Overdamped: slower exponential decay, never crosses zero. Caption: The three damping regimes. Critically damped returns to equilibrium fastest without oscillating — the engineering target for shock absorbers and many control systems.] -->

---

## Waves: oscillation that moves

So far, oscillation has been happening in place — a mass bouncing on a spring, a pendulum swinging. Now suppose the medium through which the oscillation occurs is continuous and connected. A disturbance at one point can propagate to the next, because each piece of medium is coupled to its neighbor by the same restoring force. The result is a **wave**: oscillation that propagates through space.

The most important thing to say about waves is also the one that daily language makes hardest to internalize: a wave carries energy, not matter. The medium oscillates in place; the pattern moves. Ocean waves roll across thousands of kilometers of Pacific water, but a given water molecule just bobs up and down as the wave passes. A sound wave crosses a room by setting each parcel of air vibrating, not by blowing air from speaker to ear.

The fundamental quantities for a wave:

- **Wavelength** $\lambda$: distance between consecutive crests (or any two adjacent points in identical phase).
- **Frequency** $f$: number of complete cycles passing a fixed point per second.
- **Wave speed** $v$: speed at which the pattern moves.

These three are related by:

$$v = f\lambda.$$

A wave covers one wavelength in one period $T = 1/f$, so $v = \lambda/T = f\lambda$. This is exact — not an approximation, not a special case. For any wave, in any medium.

![Two panels. Transverse wave (string): particles oscillate up-down while the wave travels left-right; sine-shape envelope. Longitudinal wave (sound): particles oscillate back-and-forth along the propagation direction;...](../images/16-oscillatory-motion-and-waves-fig-04.png)
*Figure 16.4 — Transverse vs Longitudinal — Particle Motion Perpendicular vs Parallel to Wave*

Two types: **transverse** (medium oscillates perpendicular to propagation direction — waves on a string, light) and **longitudinal** (medium oscillates parallel to propagation — sound, seismic P-waves).

The speed depends on the medium. For a wave on a taut string:

$$v = \sqrt{\frac{T}{\mu}},$$

where $T$ is tension and $\mu$ is mass per unit length. For sound in air near room temperature, $v \approx 343$ m/s. For light in vacuum, $v = 2.998 \times 10^8$ m/s. The medium dictates the speed; the wave equation — $F = ma$ applied to the local oscillating element — gives you the formula.

<!-- → [FIGURE: Two-panel diagram. Top: transverse wave on string — sinusoidal displacement perpendicular to propagation direction, wavelength λ labeled. Bottom: longitudinal wave (sound) — compression and rarefaction regions, same λ labeled but oscillation parallel to propagation. Caption: Transverse waves oscillate perpendicular to their direction of travel (string waves, light). Longitudinal waves oscillate parallel (sound, seismic P-waves). Both obey v = fλ.] -->

### Standing waves

When a wave reflects from a fixed boundary and the reflected wave overlaps the incoming wave, the two interfere to produce a **standing wave** — a pattern that oscillates in place with fixed nodes (where displacement is always zero) and antinodes (where displacement reaches maximum). Nothing travels; both waves are moving in opposite directions and their superposition is stationary.

![Four modes of a string fixed at both ends. n=1 fundamental: one antinode in the middle. n=2: one node in the middle. n=3: two interior nodes. n=4: three interior nodes. Frequencies are integer multiples of f₁ = v/(2L).](../images/16-oscillatory-motion-and-waves-fig-05.png)
*Figure 16.5 — Standing Wave Harmonics — n = 1, 2, 3, 4 on a Fixed String*

A string of length $L$ fixed at both ends supports standing waves only when an integer number of half-wavelengths fits in $L$:

$$L = n\frac{\lambda}{2} \implies \lambda_n = \frac{2L}{n}, \quad n = 1, 2, 3, \ldots$$

The corresponding frequencies:

$$f_n = \frac{v}{\lambda_n} = \frac{nv}{2L}.$$

The lowest, $f_1 = v/2L$, is the **fundamental**. The higher ones ($f_2 = 2f_1$, $f_3 = 3f_1$, ...) are the **harmonics** or overtones. Pluck a guitar string and you excite the fundamental plus a mixture of harmonics that decay at different rates; the blend is what makes different instruments sound different despite playing the same note.

This is resonance in its spatial form. The string "wants" to vibrate at specific frequencies, and external forcing at any of those frequencies builds a large response. Forcing at other frequencies produces small response. The quartz crystal in a watch is a standing-wave resonator — the crystal's geometry is machined to make the fundamental at exactly 32,768 Hz.

<!-- → [FIGURE: Standing wave modes n = 1, 2, 3 on a string of length L. Each mode shown at maximum displacement. Nodes (zero displacement) labeled with dots; antinodes labeled with arrows. Fundamental n=1 has λ = 2L, one antinode. n=2 has λ = L, two antinodes. n=3 has λ = 2L/3, three antinodes. Caption: The first three harmonics of a string fixed at both ends. Only wavelengths satisfying L = nλ/2 produce standing waves. All other wavelengths destructively interfere and don't build up.] -->

### Wave intensity and the inverse-square law

A wave carries power. The intensity — power per unit area crossing a surface — is:

$$I = \frac{P}{A}.$$

For a spherical wave radiating outward from a point source, the same total power spreads over ever-larger spheres. At radius $r$, the sphere has area $4\pi r^2$, so:

$$I = \frac{P}{4\pi r^2}.$$

Intensity falls as $1/r^2$. Move twice as far from a speaker and you get one-quarter the intensity. Move ten times as far and you get one-hundredth. This is the inverse-square law — we've already met it for gravity and for radiation; it applies to any quantity spreading uniformly from a point source into three-dimensional space.

---

## Resonance

Everything we've built — linear restoring forces, natural frequencies, wave propagation, standing waves — converges on one culminating idea: **resonance**.

Every oscillating system has one or more natural frequencies. If you drive the system at its natural frequency, each successive push adds energy in phase with the existing oscillation, and the amplitude builds. In a perfectly undamped system driven at resonance, the amplitude would grow without bound. Real systems always have some damping, which limits the final amplitude to a finite value — but near the natural frequency, the response is dramatically larger than at other frequencies.

The ratio of resonant amplitude to off-resonant amplitude is measured by the **quality factor** $Q$, roughly the number of oscillations before the system's amplitude decays to $1/e$ of its original value in free decay. High-Q systems (tuning forks, quartz crystals) ring for many cycles, respond only to a very narrow band of driving frequencies, and build to very large amplitudes at resonance. Low-Q systems (shock absorbers, door closers) ring briefly or not at all, respond to a wider band, and don't build much amplitude at any frequency.

<!-- → [CHART: Frequency-response curves (amplitude vs. driving frequency) for three values of Q: Q = 2 (broad, low peak), Q = 10 (moderate peak), Q = 100 (sharp, tall peak). All three curves peak at the same natural frequency ω₀. Caption: Higher Q means sharper resonance — large amplitude response in a narrow frequency band. A quartz watch crystal has Q ~ 10⁵; a car suspension has Q ~ 1. The height of the resonance peak scales with Q; the width scales as 1/Q.] -->

The wineglass on the table has a natural frequency (tap it and it rings). A soprano singing that exact frequency can shatter the glass — not because the sound is loud in an absolute sense, but because the sustained on-resonance driving builds the glass's vibration amplitude until the structural stress exceeds the material limit. Turn up the volume on a speaker until the cone hits the same frequency, same result. The physics is $F = -kx$, driven with phase coherence, accumulating energy.

The engineering flip side: buildings, bridges, and aircraft wings all have natural frequencies. Wind loading, earthquakes, and engine vibration can drive structures at or near those frequencies. The 1940 Tacoma Narrows Bridge collapse was attributed for decades to resonance with gusting wind — a neat, textbook story. The actual mechanism was **aeroelastic flutter**, a more complex nonlinear feedback between the bridge's motion and the aerodynamic forces it generated. But the relevant physics is the same lesson: a structure that oscillates freely at some frequency can be driven into catastrophic motion by sustained forcing near that frequency, however it arises. Modern bridges and skyscrapers incorporate **tuned mass dampers** — deliberately installed masses on springs, tuned to the building's natural frequency, so that when the structure starts to sway, the damper swings in opposition and absorbs energy. Same physics, used to prevent the buildup instead of cause it.

![Schematic of Taipei 101's tuned-mass damper: a 5.5 m diameter, 660-tonne steel sphere suspended near the top of the 508 m tower. Tuned to the building's natural period (~6.7 s) but with phase opposing wind-driven sway. Absorbs...](../images/16-oscillatory-motion-and-waves-fig-06.png)
*Figure 16.6 — Taipei 101 Tuned-Mass Damper — A 660-Tonne Pendulum That Saves Skyscrapers*

Taipei 101 has such a damper: a 660-tonne steel ball suspended from cables in the upper floors, tuned to match the tower's natural sway frequency around 0.15 Hz. To match that period ($T \approx 6.7$ s), the cable length should be:

$$L = \frac{T^2 g}{4\pi^2} = \frac{(6.7)^2(9.80)}{4\pi^2} \approx 11 \text{ m}.$$

Eleven meters of cable for a pendulum inside a skyscraper. The 660 tonnes swinging gently, out of phase with the building, is what keeps occupants from feeling sick in a typhoon.

---

## The chapter in one sentence

A linear restoring force produces sinusoidal motion at a fixed frequency; any wave is just this oscillation propagating through a connected medium; and when you drive a system at its own frequency, you build resonance — which is either the mechanism you're exploiting (clocks, speakers, MRI machines) or the catastrophe you're preventing (bridges, buildings, aircraft).

The mathematical machinery is one differential equation. The consequences span from the atom to the suspension bridge.

---

## Exercises

### Warm-up

**16.1** *(LO 1, 2)* A 0.20 kg mass on a spring oscillates with period 0.50 s. What is the spring constant?

**16.2** *(LO 3)* A 1.00 m pendulum on the Moon ($g_\text{Moon} = 1.62$ m/s²). What is its period?

**16.3** *(LO 6)* A wave on a string has frequency 500 Hz and wavelength 0.40 m. Speed?

**16.4** *(LO 4)* A 0.50 kg mass on a spring ($k = 100$ N/m) pulled 0.10 m and released. Maximum speed?

### Application

**16.5** *(LO 1, 2)* A 1,200 kg car bounces on four identical springs with period 0.80 s. Spring constant of each?

**16.6** *(LO 5)* A worn car shock absorber has become underdamped. Describe what the driver feels over a bump. A clogged absorber has become overdamped. Describe that.

**16.7** *(LO 6, 7)* A guitar's high-E string plays 329.6 Hz. String length 0.65 m. Wave speed on the string? Compare to sound in air (343 m/s).

**16.8** *(LO 3)* A 0.5 m pendulum swings with period 1.42 s. What is the local value of $g$?

### Synthesis

**16.9** *(LO 1, 4, 7)* A child on a swing of effective length 2.5 m. (a) Natural period? (b) An adult pushes at intervals matching that period. After 5 pushes, amplitude has grown to 1 m from essentially zero. What energy was delivered per push, ignoring damping?

**16.10** *(LO 6, 7)* Piano A above middle C is 440 Hz. You hear it 0.10 s after the hammer strikes. (a) Distance to piano? (b) Wavelength in air? (c) Wavelength in water (sound speed ~1480 m/s)?

**16.11** *(LO 5, 7)* The 1940 Tacoma Narrows Bridge collapsed under steady 19 m/s wind. Textbooks call it resonance; engineers say aeroelastic flutter. Without math, explain the difference in one paragraph: what would resonance require that flutter does not?

### Challenge

**16.12** *(beyond chapter)* A quartz watch crystal at 32,768 Hz keeps time to 15 s/month. (a) Fractional frequency accuracy? (b) Estimate the Q factor needed. (c) Compare to a pendulum's Q (~100) and a tuning fork's Q (~1000).

**16.13** *(beyond chapter)* Two identical pendulums (length 1.0 m) are weakly coupled by a spring connecting their bobs. You start one swinging, the other at rest. Sketch what you predict the amplitudes look like over time. Explain why the energy transfer rate depends on coupling strength.

---

## LLM Exercise — Chapter 16: Find the Oscillation in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** Identification of one oscillatory or wave-like component of your anchor phenomenon, with computed period/frequency/wavelength as appropriate.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste from Chapter 1].

For Chapter 16 (Oscillations and Waves), I want to find ONE periodic or wave-like component of my phenomenon and analyze it.

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

7. Connect to Chapter 17 (Sound), where we extend wave physics to acoustics.

Save the output as logbook/chapter-16-oscillations.md.
```

### What this produces

Your sixteenth Logbook entry — a quantified periodic component of your phenomenon.

### How to adapt this prompt

- *For phenomena with no obvious oscillation*: every system has a natural frequency. A coffee cup has a "ringing" frequency if you tap it; a bike frame has a vibrational mode; a marathon runner has stride and heartbeat frequencies. Find one.
- *For Claude Code:* if you have an audio recording or accelerometer log, fit a Fourier transform and extract the dominant frequency.

### Connection to previous chapters

Builds on Chapters 4–7 (Newton's laws, work and energy). The energy-conservation argument for max velocity uses Chapter 7 directly.

### Preview of next chapter

Chapter 17 zooms in on sound waves — speed, intensity, the decibel scale, Doppler effect. The Chapter 17 LLM Exercise will analyze the acoustic component of your phenomenon.

---

**Tags:** oscillation, simple-harmonic-motion, pendulum, waves, resonance
