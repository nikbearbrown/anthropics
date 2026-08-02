# Waves: Patterns That Travel

## Three title options

1. **Waves: How Disturbances Carry Energy Across Space**
2. **Traveling Waves: The Physics of Ripples, Strings, and Seismic Shaking**
3. **Waves in Motion: Why a Guitar String and a Tsunami Obey the Same Laws**

## TL;DR

A wave is a disturbance that propagates through a medium—or sometimes without one—carrying energy and momentum while the medium itself does not travel. The wave speed depends on the properties of the medium, not the disturbance itself. On a taut string, both the traveling wave and the standing wave are solutions to the same partial differential equation, one moving forward, one frozen in place.

---

## The Indian Ocean Learns About Wave Speed

On December 26, 2004, at 7:59 AM local time, the seafloor west of Sumatra ruptured. A magnitude 9.1 earthquake—one of the largest ever recorded—displaced a column of water roughly 30 meters (100 feet) vertically and several hundred kilometers in extent. What happened next was invisible at first. The water surface above the rupture began to oscillate. The disturbance spread outward as a gravity wave traveling across the Indian Ocean at roughly 800 kilometers per hour in deep water, where the ocean is over 4,000 meters deep.

Fifteen minutes later, the first wave arrived at Sumatra, Banda Aceh was hit hardest—a city of 400,000 people on the edge of the fault. The water receded so far that people could walk on the exposed seafloor, a sign that was often the only warning. By the time people realized what was happening, the backrush was upon them.

Here is the central puzzle: the wave traveled at 800 km/h across deep ocean, but the ocean is 4,000 meters deep. The water did not move 4,000 meters. It oscillated vertically, perhaps a few meters at most. How can a disturbance travel so fast when the medium itself barely moves? And why does the wave slow down as it approaches shallow water, where it eventually reaches heights of 30 meters and moves at only 35 km/h?

The answer is that wave speed is not the speed of the medium. Wave speed is determined by the properties of the medium itself. For gravity waves on the ocean, the speed is given by:

$$v = \sqrt{gh}$$

where $g$ is gravitational acceleration (9.8 m/s²) and $h$ is water depth. In the Indian Ocean's deep regions, with $h = 4000$ m, the wave speed is 198 m/s, or about 712 km/h. Close to shore, where $h = 10$ m, the speed drops to 10 m/s. The formula predicts the observed speeds perfectly.

This is the machinery of waves. Not particles flying through space. Not a "medium" that moves across a distance. A *pattern* that propagates because the medium exerts forces on adjacent regions, coupling the oscillations together. Understand this coupling—how tension in a string, or gravity in an ocean, or pressure in a gas creates the restoring force—and you understand what determines wave speed.

---

## Learning Objectives

By the end of this chapter, you will be able to:

- Identify whether a given wave is transverse or longitudinal, and describe the motion of the medium in each case
- Write and interpret the wave function $y(x,t) = A \sin(kx - \omega t + \phi)$ for a sinusoidal traveling wave
- Derive the wave equation $\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$ from Newton's second law applied to a string element
- Calculate the speed of a wave on a string using $v = \sqrt{F_T/\mu}$, and explain what determines this speed
- Find the energy and power transported by a sinusoidal wave in terms of amplitude, frequency, and wave speed
- Use the principle of superposition to predict the outcome when two waves overlap
- Determine the standing-wave modes on a string with fixed ends, and explain why only certain frequencies can produce resonance

---

## Prerequisites

You should be comfortable with:

- Single-variable calculus: partial derivatives, especially $\frac{\partial}{\partial t}$ and $\frac{\partial}{\partial x}$
- Trigonometry and trigonometric identities, including sine, cosine, and phase shifts
- Newton's second law ($F = ma$) and how to apply it to small elements of a system
- Simple harmonic motion, amplitude, frequency, period, and angular frequency $\omega = 2\pi f$
- Energy in oscillating systems: kinetic and potential energy in simple harmonic motion

---

## Concept 1: Traveling Waves and the Wave Function

### The Puzzle: Transverse and Longitudinal

Take two scenes: a guitar string plucked at one end, and a slinky held horizontally with one end shaken back and forth along its length.

In the first case, the string's ends oscillate *perpendicular* to the direction the disturbance travels. The wave moves horizontally along the string, but each small element of the string moves vertically. This is a *transverse wave*.

In the second case, the slinky's coils compress and expand *along* the direction of propagation. The disturbance moves along the slinky's length, and so does the motion of each coil. This is a *longitudinal wave*.

Both are waves. Both transport energy. Both obey the same fundamental wave equation. But the medium behaves differently in each. If you watch a single point on the guitar string, it traces a vertical path. If you watch a single coil on the compressed slinky, it traces a horizontal path, oscillating back and forth along the coil's own axis.

The specification: A wave is a disturbance that propagates through a medium, carrying energy and momentum but not mass. The disturbance can be oriented either perpendicular to (transverse) or parallel to (longitudinal) the direction of propagation. Electromagnetic waves are transverse—the electric and magnetic fields oscillate perpendicular to the direction the light travels. Sound waves in air are longitudinal—air molecules oscillate back and forth along the direction the sound travels. The ocean's surface waves are *both*—the water at the surface traces an elliptical path, moving both vertically (transverse component) and horizontally (longitudinal component).

### Mechanism: The Wave Function

A sinusoidal wave traveling in the positive $x$-direction can be written as:

$$y(x,t) = A \sin(kx - \omega t + \phi)$$

Here:
- $A$ is the *amplitude*: the maximum displacement from equilibrium.
- $k = 2\pi/\lambda$ is the *wave number*, where $\lambda$ is the wavelength (the distance between adjacent identical points, like two crests).
- $\omega = 2\pi f = 2\pi/T$ is the *angular frequency*, where $f$ is the frequency (how many cycles per second) and $T$ is the period (time for one cycle).
- $\phi$ is the *initial phase shift*, which accounts for the initial conditions at time $t = 0$.

The minus sign between the $kx$ and $\omega t$ terms tells you the wave is moving in the positive $x$-direction. (If you want a wave moving in the negative direction, use a plus sign: $y(x,t) = A \sin(kx + \omega t + \phi)$.)

Why this form? Imagine you take a snapshot of the wave at $t = 0$: $y(x,0) = A \sin(kx + \phi)$. This is a pure sine wave, with wavelength $\lambda = 2\pi/k$. Now imagine the entire pattern *shifts* in the positive $x$-direction by a distance $vt$ (where $v$ is the wave speed). The new snapshot is what you get by replacing $x$ with $x - vt$ in the spatial function: $y(x,t) = A \sin(k(x - vt) + \phi)$. Expanding, $y(x,t) = A \sin(kx - kvt + \phi) = A \sin(kx - \omega t + \phi)$, because $\omega = kv$.

The **fundamental relation** that connects all the wave parameters is:

$$v = \lambda f = \frac{\lambda}{T} = \frac{\omega}{k}$$

This holds for all mechanical waves. The wave speed $v$ is not arbitrary—it is determined entirely by the properties of the medium (tension and density for strings, pressure and density for sound, depth and gravity for ocean waves).

### Trade-off: Superposition works for small amplitudes

The wave equation is *linear*, which means if $y_1(x,t)$ and $y_2(x,t)$ are both solutions, then so is any linear combination $c_1 y_1(x,t) + c_2 y_2(x,t)$. This is the principle of superposition, and it has enormous power—it lets you build complex waves from simple ones.

But superposition only works when the restoring force of the medium is linear. For a taut string, this means the restoring force must be proportional to the displacement, like a spring. When the amplitude becomes too large—comparable to the wavelength—the restoring force stops being linear, and the principle of superposition breaks down. Shock waves and tsunami run-up in shallow water are examples where nonlinearity matters. You cannot build them by superposition. For this chapter, we assume amplitudes are small enough that the medium stays in the linear regime.

### Worked Example: A Sinusoidal Wave on a String

A transverse wave travels on a taut string with the wave function:

$$y(x,t) = 0.20 \, \text{m} \, \sin(6.28 \, \text{m}^{-1} x - 1.57 \, \text{s}^{-1} t)$$

What are the amplitude, wavelength, period, wave speed, and direction of motion?

**Amplitude:** Read straight from the coefficient: $A = 0.20$ m.

**Wave number and wavelength:** The coefficient of $x$ is $k = 6.28$ m$^{-1}$. Since $k = 2\pi/\lambda$:

$$\lambda = \frac{2\pi}{k} = \frac{6.28}{6.28} = 1.0 \, \text{m}$$

**Angular frequency and period:** The coefficient of $t$ is $\omega = 1.57$ s$^{-1}$. Since $\omega = 2\pi/T$:

$$T = \frac{2\pi}{\omega} = \frac{6.28}{1.57} = 4.0 \, \text{s}$$

**Frequency:** $f = 1/T = 0.25$ Hz. One complete oscillation occurs every 4 seconds.

**Wave speed:** $v = \omega/k = 1.57/6.28 = 0.25$ m/s. Or equivalently, $v = \lambda f = 1.0 \times 0.25 = 0.25$ m/s.

**Direction:** The minus sign between $kx$ and $\omega t$ means the wave travels in the positive $x$-direction.

### Common Misconception: "The wave goes slower in a denser medium"

Students often confuse wave speed with particle speed. A denser string (higher $\mu$) actually makes waves *slower*, because inertia opposes the acceleration. But the particle oscillating in that dense string may have a high velocity—it depends on the amplitude and frequency, not just the density. Two independent quantities, two different concepts.

---

## Concept 2: Energy and Power in Waves

### The Puzzle: How Much Energy Does a Wave Carry?

An earthquake in the deep ocean displaces billions of cubic meters of water just a few meters. The energy released is enormous—enough to level cities thousands of kilometers away. A sound wave with a high amplitude makes your ear drum vibrate; a weak sound barely moves it. Loud sounds cause pain and damage; soft sounds do not.

The energy in a wave must depend on the amplitude, but how? If you double the amplitude, do you double the energy? Triple it?

### Mechanism: Energy Density and Power

Consider a small segment of a taut string of length $\Delta x$. Its mass is $\Delta m = \mu \Delta x$, where $\mu$ is the linear density (mass per unit length). As a sinusoidal wave passes through, this segment oscillates with the wave: $y(x,t) = A \sin(kx - \omega t)$. The vertical velocity of the segment is:

$$v_y(x,t) = \frac{\partial y}{\partial t} = -A\omega \cos(kx - \omega t)$$

The segment has kinetic energy $\Delta K = \frac{1}{2} (\Delta m) v_y^2 = \frac{1}{2} (\mu \Delta x) A^2 \omega^2 \cos^2(kx - \omega t)$.

It also has potential energy. As the string deforms, it stores elastic energy. For a linear system, the potential energy equals the kinetic energy (averaged over a complete oscillation). So the total mechanical energy in the segment is:

$$\Delta E = \Delta K + \Delta U \approx \mu A^2 \omega^2 (\Delta x) \cos^2(kx - \omega t)$$

The energy per unit length—the energy density—oscillates in time and space. But we care about the average, integrated over a full wavelength. When you integrate $\cos^2$ over one complete period, you get $1/2$, so the average energy in one wavelength is:

$$E_{\lambda} = \frac{1}{2} \mu A^2 \omega^2 \lambda$$

The **average power**—the rate at which energy flows past a fixed point—is this energy divided by the time it takes one wavelength to pass. That time is the period $T$:

$$P_{\text{ave}} = \frac{E_{\lambda}}{T} = \frac{1}{2} \mu A^2 \omega^2 \frac{\lambda}{T} = \frac{1}{2} \mu A^2 \omega^2 v$$

where $v = \lambda / T$ is the wave speed.

This is the key result: **Power is proportional to the square of amplitude and the square of frequency.**

If you double the amplitude, the power goes up by a factor of four. If you double the frequency while keeping the amplitude fixed, the power again goes up by a factor of four. This is why turning up the volume on a speaker requires exponentially more power.

### Trade-off: This holds for linear waves but not shock waves

For a tsunami in deep water, the linear formula works. But as the tsunami approaches shore, the water shallows, the wave slows, and the amplitude grows (because the energy that was spread over a long wavelength gets compressed into a shorter wavelength). Eventually, the amplitude becomes so large that the restoring force is no longer linear. The wave steepens, develops a front that is nearly vertical, and breaks. At that point, nonlinear dynamics take over, and you cannot use the $P \propto A^2 \omega^2$ formula. The actual energy transfer becomes more complex.

### Worked Example: Power in a Vibrating String

A 2-meter string has a linear density $\mu = 0.035$ kg/m and is under tension $F_T = 90$ N. The string is driven by a vibrator at frequency $f = 60$ Hz with amplitude $A = 0.04$ m. What is the average power delivered to the wave?

First, find the wave speed: $v = \sqrt{F_T / \mu} = \sqrt{90 / 0.035} = \sqrt{2571} \approx 50.7$ m/s.

Next, find the angular frequency: $\omega = 2\pi f = 2\pi \times 60 \approx 377$ rad/s.

Finally, calculate the power:

$$P_{\text{ave}} = \frac{1}{2} \mu A^2 \omega^2 v = \frac{1}{2} (0.035)(0.04)^2 (377)^2 (50.7)$$

$$= \frac{1}{2} (0.035)(0.0016)(142129)(50.7) \approx 80.5 \, \text{W}$$

The vibrator must supply about 80 watts to maintain the wave. This is the power to keep the wave vibrating at constant amplitude; if you had any damping (friction, air resistance), you would need even more.

### Common Misconception: "A slower wave carries less energy"

A slower wave in a denser string can carry *more* energy than a faster wave in a light string, if they have the same amplitude and frequency. Why? Because $\mu$ appears in the formula. A denser string means more mass oscillating at each point, so more kinetic energy. The speed of the wave is not the energy; the speed is a consequence of the properties of the medium.

---

## Concept 3: Superposition, Interference, and Standing Waves

### The Puzzle: When Two Waves Meet

Drop two rocks in a pond at slightly different locations. Two circular ripples spread out from each impact point. When the ripples meet, do they bounce off each other like billiard balls? Do they stick together? No—they pass right through each other, and for a moment, you can see both ripples simultaneously in the region where they overlap. Their displacements add.

Now pluck a guitar string. The pulse you create travels toward the fixed end. When it hits the end, it reflects. On its way back, the reflected pulse meets a new pulse you have just sent down. In the overlap region, the two pulses interfere—they can reinforce each other (constructive interference) or cancel (destructive interference). If the conditions are just right—if the string length and the driving frequency are related in a specific way—the forward and reflected waves interfere in such a way that the string seems to vibrate in place, with certain points (called nodes) remaining perfectly still and other points (called antinodes) vibrating with maximum amplitude. This is a standing wave, and it is the basis of how musical instruments work.

### Mechanism: Superposition and Linear Waves

The principle of superposition is direct: when two waves occupy the same region of space, the total displacement at any point is the algebraic sum of the displacements from each wave alone.

$$y_{\text{total}}(x,t) = y_1(x,t) + y_2(x,t)$$

This is not obvious for mechanical waves. Intuitively, you might expect two disturbances to "interfere" with each other, to get tangled. Instead, they pass through as if the other were not there. Why? Because the wave equation is linear. If $y_1$ and $y_2$ each satisfy the wave equation:

$$\frac{\partial^2 y_1}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y_1}{\partial t^2}, \quad \frac{\partial^2 y_2}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y_2}{\partial t^2}$$

then their sum also satisfies it:

$$\frac{\partial^2 (y_1 + y_2)}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 (y_1 + y_2)}{\partial t^2}$$

This is a mathematical consequence of the linearity of the differential operator $\partial^2/\partial x^2$ and $\partial^2/\partial t^2$.

Constructive interference occurs when two waves add up to produce a larger amplitude. This happens when the crests of one wave line up with the crests of the other—when the waves are *in phase*. Destructive interference occurs when the crest of one wave lines up with the trough of another—when the waves are *180 degrees out of phase*. In the extreme case, the two waves cancel completely, and the displacement is zero everywhere.

### Standing Waves on a String

Consider two sinusoidal waves of equal amplitude and wavelength traveling in opposite directions:

$$y_1(x,t) = A \sin(kx - \omega t), \quad y_2(x,t) = A \sin(kx + \omega t)$$

The sum is:

$$y_{\text{total}}(x,t) = A \sin(kx - \omega t) + A \sin(kx + \omega t)$$

Using the trigonometric identity $\sin(\alpha - \beta) + \sin(\alpha + \beta) = 2 \sin(\alpha) \cos(\beta)$:

$$y_{\text{total}}(x,t) = 2A \sin(kx) \cos(\omega t)$$

This is a *standing wave*. Notice that it factorizes into a spatial part $\sin(kx)$ and a temporal part $\cos(\omega t)$. Every point on the string oscillates with the same frequency, but the *amplitude* of oscillation at each point is $2A \sin(kx)$. At positions where $\sin(kx) = 0$, the displacement is always zero—these are the *nodes*. At positions where $|\sin(kx)| = 1$, the displacement oscillates with maximum amplitude $2A$—these are the *antinodes*.

Nodes occur at $x = 0, \lambda/2, \lambda, 3\lambda/2, \ldots = n\lambda/2$ for $n = 0, 1, 2, \ldots$.
Antinodes occur at $x = \lambda/4, 3\lambda/4, 5\lambda/4, \ldots = (2m+1)\lambda/4$ for $m = 0, 1, 2, \ldots$.

Now, if the string has both ends fixed (boundary condition: $y(0,t) = 0$ and $y(L,t) = 0$ for all $t$), then nodes must occur at both ends. The condition $y(0,t) = 0$ is automatically satisfied. For $y(L,t) = 0$ to hold for all $t$, we need $2A \sin(kL) \cos(\omega t) = 0$ for all $t$. Since the $\cos(\omega t)$ term oscillates, we need $\sin(kL) = 0$, which means:

$$kL = n\pi, \quad n = 1, 2, 3, \ldots$$

Since $k = 2\pi/\lambda$:

$$\frac{2\pi}{\lambda} L = n\pi \implies \lambda_n = \frac{2L}{n}$$

The allowed wavelengths are integer submultiples of $2L$. The corresponding frequencies are:

$$f_n = \frac{v}{\lambda_n} = \frac{nv}{2L}$$

The *fundamental frequency* (the lowest frequency at which the string resonates) is $f_1 = v/(2L)$. All other frequencies are integer multiples of the fundamental. These are called *harmonics* or *overtones*.

This is why a guitar string has a well-defined pitch. When you pluck it, the pluck excites multiple standing-wave modes at once, but the fundamental frequency dominates the sound you hear. The higher harmonics add the timbre—the "color" of the note. A piano string is heavier and shorter than a guitar string for the same pitch, so its harmonics lie at slightly different frequencies, giving it a different timbre.

### Trade-off: Standing waves are idealized; real strings have damping

In the real world, the string loses energy to the air and to internal friction. The "nodes" do not stay perfectly still; they oscillate slightly. The "antinodes" do not maintain constant amplitude; they decay over time. A more realistic model includes a *damping force* proportional to the velocity. The resulting motion is a standing wave whose amplitude decays exponentially with time: $y(x,t) = e^{-\gamma t} \cdot 2A \sin(kx) \cos(\omega t)$, where $\gamma$ is the damping coefficient. For a lightly damped system (small $\gamma$), the motion looks like an ideal standing wave for many oscillations before the amplitude becomes visibly smaller. For a heavily damped system, you do not see clear standing waves at all.

### Worked Example: Finding the Harmonic Frequencies of a Guitar String

A guitar string is 0.65 m long and has a linear density of $3.09 \times 10^{-4}$ kg/m. The tension is 56.4 N.

First, find the wave speed: $v = \sqrt{F_T / \mu} = \sqrt{56.4 / (3.09 \times 10^{-4})} = \sqrt{182520} \approx 427$ m/s.

The fundamental frequency is:

$$f_1 = \frac{v}{2L} = \frac{427}{2 \times 0.65} = \frac{427}{1.3} \approx 329 \, \text{Hz}$$

This is close to the note E4 (which is 330 Hz), so this is the E string of the guitar.

The harmonics are:
- $f_1 = 329$ Hz (fundamental, first harmonic, E4)
- $f_2 = 2 \times 329 = 658$ Hz (second harmonic, E5, one octave higher)
- $f_3 = 3 \times 329 = 987$ Hz (third harmonic, B5)
- And so on.

When you pluck the open E string, all of these frequencies are excited simultaneously. Your ear hears them as a blended tone, but an oscilloscope or a spectrum analyzer would show the energy distributed across all these frequencies.

### Common Misconception: "Standing waves do not transport energy"

True: a standing wave does not have a net flow of energy from one place to another (unlike a traveling wave). But energy *is* present in the standing wave—it is just sloshing back and forth between kinetic and potential forms. When the antinodes are at maximum displacement, the energy is mostly potential (elastic). When the string passes through equilibrium, the energy is mostly kinetic. The total mechanical energy oscillates between these two forms, but the sum remains constant (in the idealized, undamped case).

---

## Integration: How Everything Fits Together

We began with a puzzle: how does a disturbance traveling at 800 km/h across the Indian Ocean cause only a few meters of displacement? The answer lives in three mechanisms working together.

The **traveling wave** lets you describe any disturbance as a sinusoidal pattern propagating at a speed determined by the medium. The wave function $y(x,t) = A \sin(kx - \omega t)$ is not just notation—it is the complete solution to the wave equation for that medium. Once you know the wave speed, you can predict the pattern at any place and time.

The **energy and power** in that wave scale with $A^2 \omega^2$. The Indian Ocean earthquake released enormous energy, but it was distributed over a huge area. In deep water, where the wave spreads over a long distance, the energy density per unit area is small, so the amplitude is small. As the wave approaches shallow water, the same energy gets compressed into a shorter distance, so the amplitude grows. The power (energy per unit time) passing a fixed point is what causes the destruction—not the amplitude alone, but the rate at which energy arrives.

The **superposition and standing waves** emerge naturally from the linearity of the wave equation. When the Sumatra earthquake sent pulses traveling both inland and back out to sea, the reflected waves could interfere with the incident waves. In harbors and enclosed basins where tsunami waves bounce off the coastline, standing-wave patterns can form, creating regions of constructive and destructive interference. Some harbors are hit hard; others nearby are spared. This is a direct consequence of how waves superpose.

A guitar string in your hands is much smaller and safer than an ocean tsunami, but the physics is identical. Pluck the string. A disturbance travels down to the fixed end at the bridge, reflects, and travels back. The incident and reflected waves interfere, creating standing waves at specific frequencies determined by the length of the string and the wave speed. Those frequencies are what you hear as the pitch of the note. Turn up the tension, and the wave speed increases, so the frequency increases, and the note gets higher. This is how the tuning pegs on a guitar work.

---

## Synthesis: What You Now Understand

You began this chapter not knowing how to think about waves at all—only seeing them as vague disturbances on water or the sound from speakers. Now you can:

- **Identify the mechanism.** You know that wave speed is determined by the restoring force and the inertia of the medium: $v = \sqrt{F_T/\mu}$ for strings. You can derive this from Newton's second law applied to a small element.
- **Predict the pattern.** Given the amplitude, frequency, and initial phase, you can write down the wave function and calculate the displacement at any position and time.
- **Calculate the energy.** You know that power goes as $A^2 \omega^2 v$, so you can estimate how much energy a wave carries and predict how loudness or intensity scales with amplitude and frequency.
- **Understand interference.** You see why two waves do not bounce off each other but add algebraically. You can predict constructive or destructive interference depending on the phase relationship.
- **Explain standing waves.** You understand why a plucked string vibrates at discrete frequencies determined by its length and the wave speed. You can calculate those frequencies and explain why a longer string or a looser string produces a lower note.

The wave equation—$\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$—is one of the most important partial differential equations in all of physics. It governs not just waves on strings, but sound waves, light waves, seismic waves, and even the quantum waves (wavefunctions) in quantum mechanics. Master this equation, and you have a key that unlocks an enormous range of phenomena.

---

## Graduated Exercises

### Warm-up

1. A sinusoidal wave on a string has amplitude 3 cm, wavelength 0.5 m, and wave speed 20 m/s. Calculate the frequency and period of the wave.

2. A longitudinal wave in a spring travels at 5 m/s. If the distance between two consecutive compressions is 0.2 m, what is the frequency of the wave?

3. Write the wave function $y(x,t)$ for a sinusoidal transverse wave with amplitude 0.1 m, frequency 10 Hz, wavelength 2 m, traveling in the negative $x$-direction.

### Application

4. A taut rope 3 m long has a mass of 0.15 kg and is under a tension of 200 N. A sinusoidal wave is driven at one end with a frequency of 5 Hz. Find (a) the wave speed, (b) the wavelength, and (c) the average power delivered to the wave if the amplitude is 5 cm.

5. Two identical sinusoidal waves with amplitude 2 cm and wavelength 40 cm travel in opposite directions on a string. At a certain point on the string, the two waves are in phase. Describe the resulting displacement at that point. What is the maximum displacement? Where are the nodes of the resulting standing wave?

6. A guitar string 0.75 m long has a linear mass density of $4.0 \times 10^{-3}$ kg/m and is under tension 150 N. What are the frequencies of the first three harmonics?

### Synthesis and Challenge

7. A tsunami is generated by an underwater earthquake. In deep ocean (depth 5 km), it travels at about 220 m/s. As it approaches shallow water (depth 10 m), it slows to about 10 m/s. Use the shallow-water gravity-wave formula $v = \sqrt{gh}$ to verify these speeds, and explain why the amplitude of the tsunami grows as it enters shallow water if energy is conserved.

8. A long string is attached to a vibrating source at one end and has a fixed support at the other end (distance $L$ away). The source oscillates at frequency $f$. Using the condition that a node must exist at the fixed end, derive the relationship between the driving frequency $f$ and the wave speed $v$ that must be satisfied for a standing wave to form. What are the first three frequencies that produce standing waves?

9. Two speakers separated by 1 meter emit sound waves of the same frequency (512 Hz) in phase. The speed of sound in air is 340 m/s. At a point on the line connecting the two speakers, 0.5 m from the first speaker and 1.5 m from the second, will the two waves interfere constructively or destructively? Calculate the phase difference between the two waves at this point.

---

## Chapter Summary

A wave is a disturbance that propagates through a medium, carrying energy and momentum but not mass. The wave speed is determined by the mechanical properties of the medium: tension and density for strings, pressure and bulk density for sound, water depth and gravity for ocean waves.

A sinusoidal traveling wave is described by the wave function $y(x,t) = A \sin(kx - \omega t + \phi)$, where the amplitude $A$, wave number $k = 2\pi/\lambda$, and angular frequency $\omega = 2\pi/f$ are related by the fundamental wave relation $v = \lambda f = \omega/k$.

The wave equation $\frac{\partial^2 y}{\partial x^2} = \frac{1}{v^2} \frac{\partial^2 y}{\partial t^2}$ is the fundamental equation governing wave motion. Any function of the form $y(x,t) = f(x \mp vt)$ is a solution.

The energy in a wave is proportional to the square of the amplitude and the square of the frequency: $P_{\text{ave}} = \frac{1}{2} \mu A^2 \omega^2 v$. This is why doubling the amplitude quadruples the power.

The principle of superposition states that the displacement at any point is the algebraic sum of the displacements from individual waves. This leads to interference: constructive (amplitudes add) when waves are in phase, destructive (amplitudes cancel) when they are 180° out of phase.

Standing waves result from the superposition of two traveling waves moving in opposite directions. For a string with fixed ends, standing waves occur only at specific frequencies: $f_n = nv/(2L)$ for $n = 1, 2, 3, \ldots$. These are the natural frequencies of the string, and they are the basis of musical pitch.

---

## Connections Forward

The next chapter takes up sound waves—longitudinal mechanical waves in air and other media. The same wave equation governs sound, but the restoring force now comes from pressure, not tension. You will see how the speed of sound depends on the medium's elasticity, and how the ear perceives the frequency (pitch) and amplitude (loudness) of sound.

After sound, the subject shifts to electromagnetic waves. These are transverse waves that do not require a medium—they oscillate through empty space. Light is an electromagnetic wave. The wave speed is always $c = 3 \times 10^8$ m/s. The wave equation is the same, but the physics is different: no tension, no pressure, but rather oscillating electric and magnetic fields that reinforce each other.

Standing waves in enclosed cavities (resonant cavities or waveguides) are central to lasers, microwave ovens, and radio transmitters. The principle is the same: confine a wave to a region with reflecting boundaries, and only certain frequencies can exist in that cavity. Build up the energy in one of those frequencies, and you have a powerful, coherent beam. This is the idea behind the laser.

Finally, in quantum mechanics, matter itself has wave properties. Electrons, protons, atoms—all exhibit wave behavior described by a wavefunction that obeys a wave-like equation (the Schrödinger equation). The standing-wave patterns of an electron in an atom determine the allowed energy levels and the chemical properties of elements. The wave equation, in its quantum form, is the foundation of modern physics.

---

## What Would Change My Mind

If a single experiment were to show that wave speed in a string is *not* determined by tension and density—that is, if a string with a different tension produced a different wave speed for the same wavelength and frequency—then the entire framework of this chapter would need revision. But 300 years of experiments, from Galileo to modern times, have confirmed the relationship $v = \sqrt{F_T/\mu}$ with high precision. It is not a law that will change.

More subtle: if it were shown that the restoring force of a real string (or water, or air) stops being linear at surprisingly low amplitudes—much lower than currently accepted—then the superposition principle and the linear wave equation would need to be replaced with a nonlinear version for most practical cases. This would make analysis much harder. But experiments show linearity extends to quite large amplitudes relative to the wavelength, so this is unlikely.

---

## Still Puzzling

I do not fully understand why the principle of superposition holds so well in practice, given that all media are ultimately made of particles and atoms. At the atomic scale, there should be a distance scale below which the continuum assumption (that the string is infinitely divisible) breaks down. Yet waves on macroscopic strings behave as if superposition is exact. There must be a range of scales where the continuum approximation is valid and superposition emerges naturally, but I have not traced through the atomic-scale physics carefully enough to see where the transition happens.

---

## Tags

wave-equation, traveling-waves, standing-waves, mechanical-waves, string-tension, wave-speed, superposition, interference, resonance, energy-in-waves, tsunami-physics, musical-acoustics



---

## LLM Exercise — Chapter 18: The Wave Equation Solver

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A numerical solver for the wave equation $\partial^2 y/\partial t^2 = v^2 \partial^2 y/\partial x^2$, with traveling waves, standing waves, and superposition verified.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 18 task in the physics-simulation-toolkit. The chapter
introduced the wave equation and traced from it: traveling waves,
standing waves, energy and power, superposition, and interference.
Build the solver and verify the canonical cases.

In `chapters/ch18_waves/`:

1. `simulations.py`:
   - `wave_solver_1d(initial_y, initial_v, length, v_wave, dt, t_end,
     boundary='fixed' | 'free' | 'periodic')` — finite-difference
     solver for the 1D wave equation. Use the second-order central
     scheme: $y(x, t+dt) = 2y(x, t) - y(x, t-dt) + (v\,dt/dx)^2 [y(x+dx, t) - 2y(x, t) + y(x-dx, t)]$.
     Enforce the CFL condition $v\,dt/dx < 1$.
   - `traveling_wave_analytical(amplitude, wavelength, frequency, x, t,
     direction='right' | 'left')` — $y = A\sin(kx \mp \omega t)$.
   - `standing_wave_analytical(amplitude, wavelength, frequency, x, t)` —
     $y = 2A \sin(kx)\cos(\omega t)$.
   - `superposition(wave1_fn, wave2_fn, x, t)` — sum of two waves.

2. `test_simulations.py`:
   - Traveling wave: a single right-moving pulse on a periodic-
     boundary domain travels at $v$ and returns to its starting
     position after $T = L/v$. Verify.
   - Standing wave: a string of length L with fixed boundaries has
     resonant frequencies $f_n = n v / (2L)$. Excite the n=1, 2, 3
     modes; verify each is a standing-wave shape with the predicted
     frequency.
   - Superposition: two waves moving in opposite directions sum to a
     standing wave. Verify numerically by adding two traveling-wave
     solutions and comparing to the analytical standing wave.
   - Reflection: a pulse moving toward a fixed end reflects inverted;
     toward a free end reflects upright. Verify both.

3. `benchmarks.py` — pluck a string (initial triangular displacement)
   and compute its Fourier decomposition. The energy distribution
   among harmonics should match the analytical pluck-spectrum (which
   depends on where the string is plucked relative to its length).
   Plot the energy in each harmonic. The 1/n² rolloff for central
   plucks should be visible.

4. `README.md` — decision cards. "Surprising findings": the
   plucking-position effect on harmonic content — guitar players
   exploit this to get a brighter or darker tone.

Commit as `ch18: 1D wave equation solver with standing-wave and
plucking analysis`.
```

**What this produces:** A working 1D wave-equation solver, verification of standing waves and traveling waves, superposition, reflection, and a pluck-position harmonic-content analysis.

**How to adapt this prompt:**

- *For your own project:* 2D and 3D wave equations are the natural extensions. Drumhead modes, ocean-surface waves, electromagnetic waves all share the same math.
- *For ChatGPT / Gemini:* Both work. The CFL condition is easy to violate; build the check into the solver.
- *For Claude Code:* Native fit. Let it animate the wave evolution.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 9 energy conservation (wave energy = sum of K and U over the medium).

**Preview of next chapter:** Chapter 19 specializes to sound — intensity, intensity level (decibels), the Doppler effect, and shock waves. The toolkit's final piece.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Elmer Imes** was the 1919 PhD thesis at the University of Michigan — the first high-resolution infrared spectroscopy of HCl and DCl gas — which resolved individual molecular rotational lines and provided crucial early experimental evidence for quantum theory of molecular structure (long before quantum mechanics was systematized) — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Elmer Imes, and how does their work on the infrared spectroscopy of diatomic molecules and the early evidence for quantum mechanical rotation connect to waves and the spectroscopic measurement of molecular structure? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Elmer Imes"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Imes's specific 1919 measurement — the spectrometer, the resolution he achieved, the rotational fine structure he observed, and what that pattern told physicists about molecular structure
- Ask: "Imes was the second African American to earn a PhD in physics in the US (1918), after Edward Bouchet (1876) and before the third (Walter McAfee) in 1949. Why was there a 30-year gap, and what was Imes's later career?"
- Add the constraint: "Answer using one of Imes's actual measured wavelengths for an HCl rotational line and what the spacing told physicists about the molecule's moment of inertia"

What changes? What gets better? What gets worse?
