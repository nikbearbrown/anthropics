# Chapter 17 — Oscillations

## Cold open

On November 7, 1940, the Tacoma Narrows Bridge—a suspension bridge spanning the Puget Sound west of Tacoma, Washington—was less than five months old. The bridge was elegant, slender, a feat of engineering confidence. A moderate windstorm moved through that afternoon, and the bridge began to move in a way that would have sent engineers into crisis had they been watching from below. The roadway did not simply sway side to side. It twisted. The deck oscillated in torsion, the oscillations growing larger with each cycle, the motion feeding on itself. Motorists abandoned their cars and fled on foot. At 11:00 a.m., a 600-foot stretch of concrete and steel tore itself apart and fell into the water below.

The Tacoma Narrows collapse was not a freak accident. It was a lesson in resonance—what happens when an external force pushes a system at precisely the frequency the system wants to move on its own. The bridge had a natural frequency. The wind, moving at the right speed, drove the bridge at that frequency. Instead of resisting, the bridge surrendered to the rhythm, the amplitude of the oscillation growing until the structure failed. Every structural engineer since has written this disaster into their courses.

Or rewind 284 years earlier. Christiaan Huygens, the Dutch mathematician and physicist, is working on a problem that has frustrated clock-makers for generations: how to make a timepiece that keeps the same time whether the bob is displaced a tiny amount or a large amount. He hits on the pendulum. He discovers that the period—the time for one complete swing—does not depend on how far you pull the pendulum back. It depends only on the length of the string and the strength of gravity. A shorter pendulum ticks faster. The period follows a simple law: $T = 2\pi\sqrt{L/g}$. He patents the pendulum clock in 1657. Within a few decades, it becomes the standard. Ships navigate by it. Cities set their clocks by it.

Or look at your wrist. Inside a quartz watch, a small crystal of silicon dioxide oscillates back and forth 32,768 times per second, driven by an electrical current. That frequency is precise, stable, and known. A circuit counts the oscillations. When the counter reaches 32,768, one second has passed. The crystal has defined the second. No mechanical gear is involved. No mainspring. Just a piece of silicon, electric current, and the physics of oscillation.

These are not separate phenomena. They are three expressions of the same mathematics. Oscillation is everywhere—in springs, pendulums, clocks, bridges, crystals, molecules, atoms. The machinery is the same. Displacement creates a restoring force. The restoring force accelerates the system back toward equilibrium. But inertia carries it past equilibrium. The system overshoots. The restoring force pulls it back the other way. The cycle repeats. If you can describe the restoring force, you can predict the motion. If you understand resonance, you can explain why bridges collapse, why wine glasses can shatter at a singer's note, why a parent can make a child on a swing go higher and higher with small pushes at just the right moment.

This chapter teaches the mathematics of oscillation. It is motion that repeats itself. It is motion that can be predicted. And it is motion that, when driven at the wrong frequency, can destroy.

### Learning objectives

By the end of this chapter you will be able to:

- **Define** the concepts of period, frequency, amplitude, and phase shift in oscillatory motion.
- **Solve** the differential equation for simple harmonic motion and write down the position, velocity, and acceleration as functions of time.
- **Apply** the relationship $T = 2\pi\sqrt{m/k}$ to find the period of a mass on a spring, and $T = 2\pi\sqrt{L/g}$ for a simple pendulum.
- **Calculate** the total mechanical energy in simple harmonic motion and **explain** why it remains constant in the absence of damping.
- **Analyze** the motion of a pendulum (simple and physical) and **recognize** the small-angle approximation.
- **Model** damped oscillation using $x(t) = A_0 e^{-bt/2m}\cos(\omega t + \phi)$ and **classify** systems as underdamped, critically damped, or overdamped.
- **Predict** the amplitude response of a driven oscillator as a function of driving frequency and **explain** resonance in terms of energy transfer.
- **Apply** the quality factor $Q$ to characterize the sharpness of a resonance.

### Prerequisites

- Calculus I (derivatives and integrals; comfort with differential equations presented symbolically).
- Chapter 6 of this book (Newton's laws and force; free-body diagrams).
- Chapter 8 of this book (potential energy and energy conservation).
- Trigonometry (sine, cosine, the unit circle; angle measurement in radians).

### Why this chapter matters

Oscillatory motion is fundamental to nearly every field of science and engineering. Seismic waves propagate through the Earth as oscillations; understanding them requires knowing how damping works. AC electrical circuits oscillate at 50 or 60 Hz; the mathematics is identical to mechanical oscillation. Quantum mechanics is built on oscillating wavefunctions. Acoustic engineering uses resonance to amplify or dampen sound. Materials scientists study how atoms oscillate around their equilibrium positions in a solid, and how the amplitude and frequency of those oscillations determine the material's properties. Any system that returns toward equilibrium under a restoring force will oscillate. This chapter gives you the tools to analyze every such system.

---

## Concept 1 — Simple Harmonic Motion: The Foundation

### The defining equation

You have a mass attached to a spring lying on a frictionless table. You pull the mass a distance $A$ from equilibrium, then release it from rest. What happens?

Two forces compete: the spring's restoring force, which tries to return the mass to equilibrium, and the mass's inertia, which resists the change. The spring exerts a force proportional to displacement:

$$\vec{F}_{\text{spring}} = -k\vec{x}$$

where $k$ is the force constant (also called the spring constant) and $\vec{x}$ is the displacement from equilibrium. The negative sign means the force points toward equilibrium—it opposes displacement.

Applying Newton's second law:

$$m a = -kx$$

where $a = d^2x/dt^2$ is the acceleration. Rewrite this as a differential equation:

$$m \frac{d^2 x}{dt^2} = -kx$$

or, rearranging,

$$\frac{d^2 x}{dt^2} = -\frac{k}{m}x$$

This is the equation of *simple harmonic motion* (SHM). The equation says: the second time-derivative of position is proportional to the negative of position itself. This is not obvious at first, but it has a very specific solution.

Let $\omega_0 = \sqrt{k/m}$. This quantity has units of inverse time (rad/s) and is called the *natural angular frequency* or *angular frequency* of the system. The general solution to the differential equation is:

$$x(t) = A \cos(\omega_0 t + \phi)$$

where $A$ is the amplitude (the maximum displacement from equilibrium) and $\phi$ is the *phase shift*, an angle that accounts for the initial conditions—where the mass starts and with what velocity.

To verify this solution, compute the derivatives:

$$v(t) = \frac{dx}{dt} = -A \omega_0 \sin(\omega_0 t + \phi) = -v_{\max} \sin(\omega_0 t + \phi)$$

where $v_{\max} = A \omega_0$ is the maximum velocity (which occurs at equilibrium, where the displacement is zero and the velocity is greatest).

$$a(t) = \frac{dv}{dt} = -A \omega_0^2 \cos(\omega_0 t + \phi) = -a_{\max} \cos(\omega_0 t + \phi)$$

where $a_{\max} = A \omega_0^2$ is the maximum acceleration (which occurs at maximum displacement, where the restoring force is strongest).

Substitute $a(t)$ back into the differential equation:

$$\frac{d^2 x}{dt^2} = -A \omega_0^2 \cos(\omega_0 t + \phi) = -\omega_0^2 x(t)$$

which gives $d^2x/dt^2 = -(k/m) x(t)$. The solution checks.

### Period, frequency, and angular frequency

A *period* is the time for one complete oscillation. We denote it $T$. Since the cosine function repeats every $2\pi$ radians, the period is:

$$T = \frac{2\pi}{\omega_0}$$

Substituting $\omega_0 = \sqrt{k/m}$:

$$T = 2\pi \sqrt{\frac{m}{k}}$$

This is a profound result. The period depends only on the mass and the stiffness of the spring. It does not depend on the amplitude. Whether you pull the mass back 1 cm or 10 cm, the time to complete one oscillation is the same. This is why pendulum clocks work: a pendulum oscillates at a constant frequency regardless of how high you let it swing (as long as the swings are small).

The *frequency* is the number of oscillations per unit time:

$$f = \frac{1}{T} = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$$

Frequency is measured in hertz (Hz), which is cycles per second. If a mass oscillates at 5 Hz, it completes 5 cycles in one second.

The *angular frequency* $\omega_0 = 2\pi f = \sqrt{k/m}$ is measured in radians per second. The relationship between the three is:

$$\omega_0 = 2\pi f = \frac{2\pi}{T}$$

### A worked example: the mass-spring system

A 2.00-kg mass is attached to a spring with spring constant $k = 32.0 \text{ N/m}$ on a frictionless table. The mass is pulled to $x = 0.020 \text{ m}$ and released from rest. Find the period, frequency, angular frequency, maximum velocity, and maximum acceleration.

*Find the angular frequency:*

$$\omega_0 = \sqrt{\frac{k}{m}} = \sqrt{\frac{32.0}{2.00}} = \sqrt{16.0} = 4.00 \text{ rad/s}$$

*Find the period:*

$$T = \frac{2\pi}{\omega_0} = \frac{2\pi}{4.00} = 1.57 \text{ s}$$

*Find the frequency:*

$$f = \frac{1}{T} = \frac{1}{1.57} = 0.637 \text{ Hz}$$

*Find maximum velocity:*

$$v_{\max} = A \omega_0 = 0.020 \times 4.00 = 0.080 \text{ m/s}$$

*Find maximum acceleration:*

$$a_{\max} = A \omega_0^2 = 0.020 \times 16.0 = 0.32 \text{ m/s}^2$$

The equations of motion are:

$$x(t) = (0.020 \text{ m}) \cos(4.00 t)$$
$$v(t) = -(0.080 \text{ m/s}) \sin(4.00 t)$$
$$a(t) = -(0.32 \text{ m/s}^2) \cos(4.00 t)$$

where $t$ is in seconds. Notice that velocity is zero when displacement is maximum (at $t = 0, T/2, T, \ldots$) and maximum when displacement is zero (at $t = T/4, 3T/4, \ldots$). The system trades kinetic and potential energy with each oscillation.

### Trade-offs in the idealized model

The model we have built assumes:

1. **No damping.** There is no friction, no air resistance, no energy loss. The oscillation continues forever at constant amplitude.
2. **Linear restoring force.** The force obeys Hooke's law: $F = -kx$. This is exact for ideal springs over a limited range of displacement, but real springs deviate when stretched or compressed too much.
3. **One degree of freedom.** The mass moves in one dimension only. Real systems can have coupled oscillations in multiple directions.

Real systems depart from these assumptions. The friction assumption is particularly important—we will return to it when we discuss damping.

### A second worked example: how to find $k$ from a hanging mass

A student suspends a mass from a spring hanging vertically. When a 0.50 kg mass is added to the spring, the spring stretches an additional 0.10 m before the system comes to rest at a new equilibrium. The student then pulls the mass down an additional 0.05 m and releases it. What is the period of oscillation?

*Step 1: Find the spring constant from the equilibrium condition.*

At equilibrium, the spring force balances the weight:

$$kx_0 = mg$$

where $x_0 = 0.10$ m is the stretch. Rearrange to find $k$:

$$k = \frac{mg}{x_0} = \frac{0.50 \times 9.8}{0.10} = 49 \text{ N/m}$$

*Step 2: Find the period.*

The period is given by $T = 2\pi\sqrt{m/k}$:

$$T = 2\pi\sqrt{\frac{0.50}{49}} = 2\pi\sqrt{0.0102} = 2\pi \times 0.101 = 0.634 \text{ s}$$

*Step 3: Understand why the amplitude doesn't matter.*

The amplitude of this oscillation is 0.05 m. But the period depends only on $m$ and $k$, not on the amplitude. The mass will oscillate up and down, taking 0.634 s per cycle, regardless of whether we release it from 0.05 m below equilibrium or 0.02 m below equilibrium. The higher amplitude carries more total energy, but the frequency remains the same. This is the whole reason Huygens could invent an accurate pendulum clock—the period does not drift as the amplitude decays due to air resistance.

*General lesson:* To find the spring constant from a hanging mass, use the equilibrium stretch. To find the period, use the mass and the spring constant. The two pieces of information are separate, which allows great flexibility in experimental design. A different student could find the spring constant by using a different hanging mass (or even by pulling the spring horizontally and measuring the restoring force directly), and the period would be the same.

### Common misconceptions

**The period depends on amplitude.** No. The period of a simple harmonic oscillator depends only on the mass and the force constant (for a spring) or length and gravity (for a pendulum). A guitar string plucked gently and plucked hard produce the same frequency. This independence from amplitude is what makes SHM useful for timekeeping—the frequency does not drift as the amplitude decays.

**Velocity is maximum at maximum displacement.** No. Velocity is zero at maximum displacement (the turning points). Velocity is maximum at equilibrium, where the displacement is zero and all the energy is kinetic.

**A stiffer spring always leads to a higher frequency, even if the mass changes.** Not necessarily. The period depends on the ratio $\sqrt{k/m}$. A spring that is twice as stiff but attached to a mass that is four times as heavy will have a longer period than the original system, not a shorter one.

**Gravity makes a hanging spring oscillate differently than a horizontal spring.** No. For a hanging spring, gravity merely shifts the equilibrium position downward. The oscillations about that new equilibrium follow the same mathematics. The period is still $T = 2\pi\sqrt{m/k}$, independent of whether the spring is horizontal or vertical.

---

## Concept 2 — Energy in SHM and the Pendulum

### Energy conservation in the oscillator

In simple harmonic motion without damping, mechanical energy is conserved. At any instant, the total energy is the sum of kinetic and potential energy:

$$E_{\text{total}} = \frac{1}{2}m v^2 + \frac{1}{2}k x^2$$

At maximum displacement ($x = A$), the mass is at rest ($v = 0$), so all energy is potential:

$$E_{\text{total}} = \frac{1}{2}k A^2$$

At equilibrium ($x = 0$), the displacement is zero and all energy is kinetic:

$$E_{\text{total}} = \frac{1}{2}m v_{\max}^2 = \frac{1}{2}m (A \omega_0)^2 = \frac{1}{2}m A^2 \omega_0^2 = \frac{1}{2}k A^2$$

(The last step uses $\omega_0 = \sqrt{k/m}$, so $m \omega_0^2 = k$.)

The key result: energy is proportional to the square of amplitude.

$$E_{\text{total}} = \frac{1}{2}k A^2 = \text{constant}$$

This constant total energy is the contract of SHM. It means that a larger amplitude means more total energy—four times the amplitude means four times the energy. But the oscillation frequency stays the same.

### Energy as a function of position

You can use energy conservation to find the velocity at any position without solving the equations of motion explicitly. Rearrange the energy equation:

$$\frac{1}{2}m v^2 = E_{\text{total}} - \frac{1}{2}k x^2 = \frac{1}{2}k A^2 - \frac{1}{2}k x^2 = \frac{1}{2}k(A^2 - x^2)$$

Therefore,

$$|v| = \sqrt{\frac{k}{m}(A^2 - x^2)} = \omega_0 \sqrt{A^2 - x^2}$$

This tells you: (1) velocity is real only for $|x| \leq A$ (you cannot be displaced beyond the amplitude), and (2) the closer you are to equilibrium, the faster you are moving.

### The simple pendulum

A simple pendulum consists of a point mass (the bob) suspended from a string of length $L$, with the mass of the string negligible compared to the bob. When you displace the pendulum by a small angle and release it, what is the period?

The restoring torque about the pivot is:

$$\tau = -L(mg \sin \theta)$$

where $\theta$ is the angle from vertical. Using $\tau = I \alpha = I (d^2\theta/dt^2)$ and $I = mL^2$ for a point mass:

$$mL^2 \frac{d^2\theta}{dt^2} = -mgL \sin \theta$$

$$\frac{d^2\theta}{dt^2} = -\frac{g}{L} \sin \theta$$

For small angles (less than about 15°, or 0.26 radians), $\sin \theta \approx \theta$. Under this approximation:

$$\frac{d^2\theta}{dt^2} \approx -\frac{g}{L} \theta$$

This is the equation of SHM in the angle variable $\theta$, with $\omega_0^2 = g/L$. Therefore:

$$\omega_0 = \sqrt{\frac{g}{L}}$$

$$T = 2\pi \sqrt{\frac{L}{g}}$$

This is the period of a simple pendulum. The period depends only on the length and gravity, not on the mass of the bob or the amplitude of the swing (as long as the angle is small). This is the insight that made pendulum clocks possible. It is also why a pendulum of precise known length can be used to measure the local acceleration due to gravity.

**A worked example: measuring gravity with a pendulum**

A simple pendulum of length 0.75000 m is timed to have a period of 1.7357 s. What is the local acceleration due to gravity?

From $T = 2\pi\sqrt{L/g}$, solve for $g$:

$$T^2 = 4\pi^2 \frac{L}{g}$$

$$g = 4\pi^2 \frac{L}{T^2} = 4\pi^2 \frac{0.75000}{(1.7357)^2} = 4\pi^2 \frac{0.75000}{3.0126} = 9.8281 \text{ m/s}^2$$

This method is accurate to the precision of the length and period measurements—which is why such measurements are given to five significant figures.

### Trade-offs and limitations

The small-angle approximation $\sin \theta \approx \theta$ is excellent for angles less than 15°. The error is less than 1%. But for larger angles, the error grows. A pendulum released at 45° has a period about 7% longer than the simple formula predicts. The true period requires elliptic integrals, which have no closed form.

### Common misconceptions

**A longer pendulum is less useful for timekeeping.** No. A longer pendulum has a longer period, which means longer cycles, which means more time to accumulate precision. A seconds pendulum (one that swings once per second, period 2 seconds) is about 1 meter long. Longer pendulums are actually more stable.

**The mass of the bob affects the period.** Not for a simple pendulum in a uniform gravitational field. The inertia (mass) appears in both the numerator and denominator of the equation and cancels out. This is a consequence of the equivalence of gravitational and inertial mass.

---

## Concept 3 — Damping and Resonance: When Real Systems Fail

### Damped oscillations

In the real world, oscillations do not continue forever. Friction, air resistance, and internal dissipation in materials remove energy. A guitar string plucked and left alone decays to silence in seconds. A mass on a spring in a viscous fluid slows down and comes to rest.

Model damping as a velocity-dependent force:

$$F_{\text{damping}} = -b v = -b \frac{dx}{dt}$$

where $b$ is the damping coefficient. This is a reasonable model for slow motion through a fluid. The damping force opposes the velocity—it always acts to slow the motion.

The equation of motion becomes:

$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = 0$$

The solution to this equation depends on the relative magnitudes of the damping and the restoring force. Define the critical damping coefficient:

$$b_c = 2\sqrt{mk} = 2m\omega_0$$

There are three regimes:

**Underdamped** ($b < b_c$): The system oscillates, but the amplitude decreases exponentially. The solution is:

$$x(t) = A_0 e^{-bt/2m} \cos(\omega t + \phi)$$

where $\omega = \sqrt{\omega_0^2 - (b/2m)^2} < \omega_0$ is the damped angular frequency. The oscillation continues, but at a slightly lower frequency than the undamped system, and the amplitude envelope decays as $A_0 e^{-bt/2m}$.

**Critically damped** ($b = b_c$): The system returns to equilibrium as fast as possible without overshooting. There is no oscillation. The displacement approaches zero smoothly from whatever initial condition it started with.

**Overdamped** ($b > b_c$): The system returns to equilibrium slowly without oscillating. The motion is sluggish.

**Trade-offs**: A lightly damped system oscillates many times before coming to rest—useful for a clock escapement, where you want the oscillation to continue. A critically damped system is efficient—it returns to equilibrium quickly without wasting time oscillating about it. This is why car shock absorbers are designed to be nearly critically damped. A heavily damped system is slow to respond—useful when you want to isolate a sensitive instrument from vibration, but bad for responsiveness.

The damping coefficient $b$ determines how quickly energy leaves the system. In the underdamped case, the exponential envelope $A_0 e^{-bt/2m}$ tells you how fast the amplitude shrinks. The time constant $\tau = 2m/b$ is the time for the amplitude to decay by a factor of $e \approx 2.718$. For a lightly damped oscillator, this time constant is much longer than the period $T$, so the system completes many oscillations while the amplitude slowly decays. For a heavily damped oscillator, the time constant is short compared to the period, and the oscillation is snuffed out quickly—or, if damping is heavy enough, there is no oscillation at all.

The physical origin of damping is friction. In a mass on a spring, the damping can come from air resistance (proportional to velocity at moderate speeds), friction at the point where the spring is attached, or internal friction within the spring material itself. In a pendulum, it is primarily air resistance. In an electrical circuit, it is the resistance of the wire. In a molecule oscillating in a gas, it is collisions with other molecules. The common thread is that damping is velocity-dependent—the damping force opposes motion and grows stronger when the system moves faster. This is why the damping force in our model is $F_d = -bv$.

### Driven oscillations and resonance

Now suppose you do not just release the oscillator and let it decay. Instead, you apply a periodic driving force:

$$F_{\text{driving}} = F_0 \sin(\omega_d t)$$

where $\omega_d$ is the driving angular frequency (which you control) and $F_0$ is the amplitude of the driving force. The equation of motion becomes:

$$m \frac{d^2 x}{dt^2} + b \frac{dx}{dt} + k x = F_0 \sin(\omega_d t)$$

After the transient oscillations die away, the system reaches a steady state in which it oscillates at the driving frequency $\omega_d$ (not the natural frequency $\omega_0$). The amplitude of oscillation in steady state depends on how close $\omega_d$ is to $\omega_0$:

$$A(\omega_d) = \frac{F_0}{\sqrt{m^2(\omega_d^2 - \omega_0^2)^2 + b^2 \omega_d^2}}$$

This formula says:

- When $\omega_d \ll \omega_0$ (driving much slower than the natural frequency), the system barely responds. The denominator is large because $m^2(\omega_0^2 - \omega_d^2)^2$ dominates.
- When $\omega_d = \omega_0$ (driving at the natural frequency), the $(ω_d^2 - \omega_0^2)$ term vanishes. The denominator becomes small, and the amplitude becomes large. This is **resonance**.
- When $\omega_d \gg \omega_0$ (driving much faster than the natural frequency), the system again barely responds.

At resonance, the amplitude is:

$$A_{\max} = \frac{F_0}{b \omega_0}$$

Notice that $A_{\max}$ is inversely proportional to $b$. A system with very little damping can achieve enormous amplitudes at resonance, even with a small driving force. If damping is zero, the amplitude becomes infinite—a purely theoretical limit.

The **quality factor** $Q$ characterizes how sharp the resonance peak is:

$$Q = \frac{m \omega_0}{b} = \frac{\omega_0}{\Delta \omega}$$

where $\Delta \omega$ is the width of the resonance curve at half maximum amplitude. A high-$Q$ system has a sharp, narrow resonance—it responds strongly only at frequencies very close to its natural frequency. A low-$Q$ system has a broad resonance—it responds over a wider range of driving frequencies.

**The Tacoma Narrows explanation**: The bridge had a natural torsional frequency. Wind gusts at that frequency drove the bridge in torsion. Because the damping was low (a long, elegant structure has little internal friction), the quality factor was high and the resonance was sharp. The system responded dramatically to a modest driving force. The amplitude grew with each cycle until the internal stresses exceeded the strength of the steel and concrete. The bridge destroyed itself.

### Common misconceptions

**Damping always decreases the frequency.** True for light damping (underdamped). But if you add more and more damping, the frequency decreases and approaches zero. In the critically damped and overdamped regimes, there is no oscillation at all.

**Resonance means the oscillator and driver are in sync.** Not quite. At exact resonance, the driving force is 90° out of phase with the displacement (it leads the velocity). The force and displacement are perpendicular in phase space. This phase relationship is what allows the maximum energy transfer.

**You can tune any system to any frequency by changing damping.** No. Damping affects how sharply the system responds near its natural frequency, not the location of the natural frequency itself. The natural frequency is determined by stiffness and inertia.

---

## Integration and Synthesis

The journey from the Tacoma Narrows bridge to the quartz crystal in your watch is the same journey from the equation $d^2x/dt^2 = -\omega_0^2 x$ to its solution $x(t) = A \cos(\omega_0 t + \phi)$.

Every system with a restoring force proportional to displacement will oscillate. The frequency depends only on how stiff the system is relative to its inertia. The energy in the oscillation depends on how far you displace it. And if you drive such a system at its natural frequency, the amplitude can grow without limit—or, in real systems with damping, reach a maximum determined by the balance between the energy you are pumping in and the energy the damping removes.

### Why the same mathematics appears everywhere

The reason oscillatory motion follows the same pattern in a spring, a pendulum, a vibrating molecule, and a quartz crystal is that they all have the same structure: a system at equilibrium, a restoring force when displaced, and inertia that carries it past equilibrium. The differential equation that describes this structure is always $d^2x/dt^2 = -\omega_0^2 x$ (where the meaning of $x$ changes—it is displacement for a spring, angle for a pendulum, atomic position for a molecule, polarization for a crystal, but the mathematical form is identical).

Once you solve this equation once—which you now have—you have solved it for every system. The rest is substitution. For a spring, substitute $\omega_0 = \sqrt{k/m}$ and you have the period. For a pendulum, substitute $\omega_0 = \sqrt{g/L}$ and you have the period. For a molecule vibrating in an interatomic potential, substitute $\omega_0 = \sqrt{(\text{curvature of potential})/\text{reduced mass}}$ and you have the vibrational frequency. The structure is the same; the constants are different.

### Applications of oscillations

This mathematics applies directly to:

- **A child on a swing** (a physical pendulum, with a parent supplying the driving force at just the right moment). Every small push at the right phase of the swing adds energy. Pushes at the wrong phase remove energy. This is resonance in action. The child (and parent) understand intuitively that there is a "right time" to push. Physics explains why.

- **A tuning fork** (the tines act as cantilever beams that oscillate at a fixed frequency determined by their material, shape, and thickness). When struck, the tines vibrate at their natural frequency. The damping is very low, so the $Q$ factor is high, and the fork rings at a pure, recognizable pitch. This is how a musical instrument maintains its tone.

- **A radio receiver circuit** (an inductor and capacitor form an LC circuit that oscillates electrically at a frequency determined by $\omega_0 = 1/\sqrt{LC}$). A weak incoming radio signal at the natural frequency of the circuit is amplified by resonance. Signals at other frequencies pass through with very little amplification. This is how a radio can select one station out of dozens on the air.

- **An atom in a molecule** (vibrates about its equilibrium position with a frequency determined by the strength of the chemical bond and the masses of the atoms). The vibrational frequency is typically in the infrared part of the electromagnetic spectrum (frequencies around $10^{13}$ Hz). Infrared spectroscopy detects the frequencies at which a molecule absorbs photons—these are the vibrational frequencies. A molecule with a strong, stiff bond vibrates faster than one with a weaker bond.

- **A seismic wave traveling through the Earth** (the ground oscillates as the wave passes, with amplitude and frequency that depend on the magnitude of the earthquake and the properties of the rock). Understanding how the amplitude decays with distance depends on understanding damping. Seismic engineers use this knowledge to design earthquake-resistant buildings—they make the building's natural frequency very different from the frequencies present in earthquakes, so the building does not resonate with the ground motion.

- **A crystal oscillator in an atomic clock** (a crystal is driven at a microwave frequency very close to its natural frequency, and the resonance is so sharp that the frequency is precise to better than one part in $10^{12}$). This is the most precise frequency standard available before moving to atomic transitions.

The principles are universal. The algebra changes with the physics, but the structure does not. Once you understand the mathematics of oscillation, you have a tool that applies to every system with a restoring force.

---

## Graduated Exercises

### Warm-up

1. A mass on a spring has a period of 2.0 s. If you double the mass, what is the new period?

2. A simple pendulum is 1.0 m long. What is its period on Earth, where $g = 9.8 \text{ m/s}^2$? What would the period be on the Moon, where $g = 1.62 \text{ m/s}^2$?

3. A 0.50-kg mass is attached to a spring with spring constant 200 N/m and oscillates with amplitude 0.10 m. What is the maximum kinetic energy of the mass?

### Application

4. A car's suspension can be modeled as a mass on a spring. A 1500-kg car compresses its suspension by 0.050 m under its own weight at rest. (a) What is the effective spring constant of the suspension? (b) What is the natural frequency of the car's vertical oscillations? (c) For comfortable riding, the damping should be such that the suspension is slightly underdamped. If the shock absorbers provide a damping coefficient of $b = 6500 \text{ kg/s}$, is the suspension underdamped, critically damped, or overdamped?

5. A 0.200-kg mass on a spring (k = 10.0 N/m) oscillates in a viscous medium. Measurements show the amplitude decreases by 50% after 10 complete oscillations. (a) What is the damping coefficient $b$? (b) Is the system underdamped, critically damped, or overdamped?

### Synthesis

6. A driven, damped oscillator has $m = 1.0 \text{ kg}$, $k = 100 \text{ N/m}$, and $b = 2.0 \text{ kg/s}$. A sinusoidal driving force of amplitude $F_0 = 10 \text{ N}$ is applied. (a) Find the natural angular frequency $\omega_0$, the natural frequency $f_0$, and the quality factor $Q$. (b) Calculate the steady-state amplitude when driven at (i) $\omega_d = \omega_0$, (ii) $\omega_d = 0.8 \omega_0$, and (iii) $\omega_d = 1.2 \omega_0$. (c) Sketch the amplitude-versus-frequency curve and identify the resonance peak.

7. A 50-kg person stands on a diving board. When the person is removed, the board oscillates with a frequency of 2.0 Hz. (a) What is the effective spring constant of the board? (b) If the person now stands on the board and bounces gently, at what frequency should they bounce to achieve resonance? (c) Why is bouncing at exactly the resonant frequency dangerous for a diving board?

### Challenge

8. A physical pendulum consists of a uniform rod of mass $M$ and length $L$ pivoted at one end. (a) Show that the moment of inertia about the pivot is $I = ML^2/3$. (b) Find the period of oscillation for small angles. (c) For what length would the period equal that of a simple pendulum of the same length?

---

## Chapter Summary

Simple harmonic motion occurs whenever a restoring force is proportional to displacement and opposite in direction. The equation $d^2x/dt^2 = -\omega_0^2 x$ has the solution $x(t) = A \cos(\omega_0 t + \phi)$, where $\omega_0 = \sqrt{k/m}$ for a spring and $\omega_0 = \sqrt{g/L}$ for a simple pendulum.

The period is $T = 2\pi/\omega_0$ and is independent of amplitude. The energy in SHM is constant in the absence of damping and is proportional to the square of amplitude: $E = \frac{1}{2}kA^2$.

Damping removes energy from the system. The system is underdamped if it oscillates while decaying, critically damped if it returns to equilibrium without oscillating, and overdamped if it returns slowly without oscillating.

When driven at a frequency near the natural frequency, an oscillator exhibits resonance. The amplitude at resonance is inversely proportional to the damping. The quality factor $Q = m\omega_0/b$ characterizes how sharp the resonance is. This is the mechanism by which the Tacoma Narrows Bridge destroyed itself, by which a crystal defines a second, and by which understanding oscillations protects structures from failure.

---

## Connections Forward

Waves are oscillations in space as well as time. A traveling wave can be thought of as a continuous chain of coupled oscillators, each one pulling on its neighbors. The wave equation emerges from the same kinds of restoring forces and inertia that govern oscillators.

Electrical circuits with resistors, capacitors, and inductors are the electrical analogs of mechanical oscillators. The voltage across a capacitor plays the role of displacement; the inductance plays the role of inertia. Resonance in electrical circuits is the same phenomenon as resonance in mechanical systems—it is the reason you can tune a radio to pick one station out of a crowded electromagnetic spectrum.

In quantum mechanics, the harmonic oscillator is one of the few systems that can be solved exactly. The energy levels are quantized: $E_n = \hbar \omega_0 (n + 1/2)$ for integer $n$. This quantization is the source of the vibrational spectra observed in molecular spectroscopy—each transition between levels corresponds to an infrared photon absorbed or emitted.

---

**What would change my mind:** If a real oscillator were found whose period varied significantly with amplitude (beyond the 1% error in the small-angle approximation), I would need to reconsider whether the restoring force truly obeys Hooke's law or whether nonlinear terms become important. But decades of precision timekeeping have verified that the small-angle approximation holds.

**Still puzzling:** I do not yet fully understand the deep reason why the phase relationship at resonance is exactly 90° between force and displacement (or 0° between force and velocity). The mathematics shows this is where maximum energy transfer occurs, but the intuition behind it—the reason why being "in sync" with velocity rather than position is optimal—could be clearer.

---

**Tags:** #simple-harmonic-motion #pendulum #damping #resonance #energy-conservation #driven-oscillators #quality-factor #SHM #oscillation

---

*Author: Nik Bear Brown*

*This chapter is a draft for review. It shows the reasoning step by step and carries all the mathematics on the page. Feedback on clarity, pace, or missing worked examples is welcome.*


---

## LLM Exercise — Chapter 17: SHM, Damping, and Resonance

**Project:** *Physics Simulation Toolkit*.

**What you're building this chapter:** A simple-harmonic-motion solver, damped oscillator (underdamped, critically damped, overdamped), and a driven oscillator that exhibits resonance.

**Tool:** Claude Code.

**The prompt:**

```
Chapter 17 task in the physics-simulation-toolkit. The chapter
covered SHM, damping, and resonance — the math behind clocks,
musical instruments, and the Tacoma Narrows collapse. Build the
simulator and verify against the analytical solutions.

In `chapters/ch17_oscillations/`:

1. `simulations.py`:
   - `shm_analytical(amplitude, omega, phase, t)` — $x(t) = A\cos(\omega t + \phi)$.
   - `damped_oscillator(m, k, c, x0, v0, t_end, dt)` — solve
     $m\ddot{x} + c\dot{x} + kx = 0$ numerically. Identify regime
     (under/critical/over) from the damping ratio.
   - `driven_oscillator(m, k, c, F0, omega_drive, t_end, dt)` — solve
     $m\ddot{x} + c\dot{x} + kx = F_0 \cos(\omega_{\text{drive}} t)$.
   - `resonance_curve(m, k, c)` — return amplitude as a function of
     drive frequency. Plot the peak at $\omega \approx \omega_0 =
     \sqrt{k/m}$.
   - `simple_pendulum(length, theta0, t_end)` — both small-angle
     ($T = 2\pi\sqrt{L/g}$) and large-angle (numerical) solutions.
     Compare.
   - `physical_pendulum(I, M, d, theta0, t_end)` — pendulum with
     distributed mass.

2. `test_simulations.py`:
   - Spring-mass oscillator: $T = 2\pi\sqrt{m/k}$. Verify by FFT of
     the numerical position record.
   - Energy in SHM: $K(t) + U(t) = \text{const}$. Verify with the
     Ch 9 infrastructure.
   - Damping: with critical damping ($c = 2\sqrt{mk}$), the system
     returns to equilibrium without oscillation. With $c$ slightly
     smaller, it overshoots once. With $c = 0$, it oscillates
     forever. Verify each regime.
   - Driven oscillator at resonance: $\omega_{\text{drive}} = \omega_0$
     produces unbounded amplitude with no damping; with damping, the
     amplitude approaches $F_0/(c\omega_0)$. Verify both limits.
   - Pendulum: small-angle agrees with $T = 2\pi\sqrt{L/g}$ to 0.1%
     for amplitude < 10°. Large-angle differs measurably by 30°
     amplitude.

3. `benchmarks.py` — generate the resonance curve (amplitude vs.
   drive frequency) for several damping levels. Identify the Q factor
   for each. This is the signature plot of oscillation physics.

4. `README.md` — decision cards. "Surprising findings": the large-
   angle pendulum-period correction (the Tacoma Narrows collapse
   was technically a coupling problem, not pure resonance — but the
   resonance framework is the right starting point).

Commit as `ch17: oscillations, damping, and resonance verified`.
```

**What this produces:** SHM and damped/driven-oscillator simulations, the resonance curve, and pendulum small-angle-vs-large-angle comparison.

**How to adapt this prompt:**

- *For your own project:* Coupled oscillators (Ch 17 doesn't cover them explicitly, but they're the natural extension) underlie wave behavior, normal modes, and the Tacoma Narrows torsional instability.
- *For ChatGPT / Gemini:* Both work. The driven-oscillator transient is interesting; verify the long-time steady-state separately from initial conditions.
- *For Claude Code:* Native fit. Let it generate the resonance curve.
- *For a Claude Project:* Not the fit.

**Connection to previous chapters:** Uses Ch 9 energy conservation, Ch 4–5 integrators. The damped oscillator is the natural-frequency analog of Ch 7's drag.

**Preview of next chapter:** Chapter 18 implements the wave equation numerically — traveling waves, standing waves, superposition, and the boundary conditions that create musical-instrument resonance.


---

## AI Wayback Machine

The physics in this chapter didn't appear from nowhere. **Hertha Ayrton** was the 1902 *Electric Arc* book — a systematic experimental study of the singing-arc oscillations in electric streetlamps — and the 1904 *Origin and Growth of Ripple-Mark* paper that explained, through fluid-mechanical oscillation theory, the regular patterns sand makes under wave action — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Hertha Ayrton, and how does their work on electric arc oscillations and the wave-driven formation of sand ripples connect to oscillations across physical systems — from electric arcs to sand patterns? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Hertha Ayrton"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to describe Ayrton's specific 1904 experiments on sand ripples — the tank setup, the oscillation parameters, the dimensional analysis — and how she connected the patterns to standing-wave physics
- Ask: "Ayrton was the first woman elected to the Institution of Electrical Engineers (1899) and the first woman to win the Royal Society's Hughes Medal (1906). She was denied Royal Society fellowship as a married woman. What was the explicit legal reasoning, and when was it overturned?"
- Add the framing: "Answer as if you're writing the historical introduction to a 2026 reissue of *The Electric Arc*"

What changes? What gets better? What gets worse?
