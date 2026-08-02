# Chapter 28 — Special Relativity

*The universe has a speed limit, and the consequences are not negotiable.*

---

![Schematic of the Michelson-Morley interferometer: light source, half-silvered beam splitter, two mirrors at equal distances along perpendicular arms, and a detector. Looked for a fringe shift as Earth moved through the...](../images/28-special-relativity-fig-01.png)
*Figure 28.1 — Michelson-Morley, 1887 — The Null Result That Killed the Ether*

In 1887, Albert Michelson and Edward Morley floated an interferometer on a slab of sandstone in a pool of mercury in Cleveland, isolated it from vibration, split a beam of light into two perpendicular arms, and waited for the interference pattern to shift as they rotated the apparatus. The shift they were looking for was the signature of Earth's motion through the luminiferous aether — the medium that everyone assumed must exist to carry light waves the way air carries sound.

The pattern didn't shift. Not detectably. In seventeen years of attempted explanations, nobody could make the null result go away.

In 1905, a 26-year-old patent clerk in Bern named Albert Einstein submitted a paper with a different approach. He didn't try to explain the null result. He took it as given — elevated it to a postulate — and asked what the rest of physics must look like if you insist that the speed of light is the same for every observer regardless of how the observer or the source is moving.

The answer was: completely different from what anyone had assumed.

---

## Two postulates

Einstein's construction rests on exactly two assumptions.

**First postulate:** The laws of physics are the same in every inertial reference frame. An *inertial frame* is one that is neither accelerating nor rotating — a frame in which an object left to itself stays put or drifts at constant velocity. Galileo already knew this one: you cannot tell, from inside a smoothly moving ship, whether the ship is moving or at rest. The laws are the same.

**Second postulate:** The speed of light in vacuum, $c = 2.998 \times 10^8$ m/s, is the same for every observer regardless of the relative motion of the source or the observer.

The first postulate is comfortable. The second is alarming. If you shine a flashlight out of a moving rocket, the light doesn't travel at $c + v_\text{rocket}$ relative to a stationary observer. It travels at $c$. The same $c$ as measured by a stationary observer, as measured by the rocket pilot. Not approximately the same. Exactly the same. Postulate 2 is not a claim about the weakness of our instruments; it is a claim about the structure of spacetime.

From these two postulates — and nothing else — everything in this chapter follows. There is no additional physics. There is only geometry and logic, applied with unusual care.

---

## Simultaneity is not absolute

Here is the first thing that falls apart.

Newton's mechanics ran on a universal clock — a single time that was the same everywhere, ticking at the same rate for every observer. Einstein's second postulate makes that impossible. Here is why.

Imagine a train moving at high constant speed. Two lamps are mounted at the front and back of the train. At the exact moment Alice, standing midway on the train, passes Bob, standing on the embankment, both lamps flash. In Bob's frame, the two flash events are simultaneous — Bob is equidistant from both lamps, and light from both reaches him at the same instant.

Now ask: what does Alice observe? She is moving toward the flash from the front lamp and away from the flash from the back lamp, in Bob's frame. Light travels at $c$ in Bob's frame. So the front flash reaches Alice before the back flash does — from Bob's perspective, Alice receives the two signals at different times. But Alice is stationary in her own frame, equidistant from the lamps in her frame too, and by postulate 2, light travels at $c$ in her frame as well. If light from the front reaches her first, she must conclude the front lamp fired first. The two events are not simultaneous in Alice's frame.

Two events that are simultaneous in one inertial frame are *not simultaneous* in a frame moving relative to the first. Simultaneity is not a property of events — it is a relationship between events and observers. Time is not universal.

This is not a philosophical point. It is a logical consequence of insisting that $c$ is the same for everyone. If you accept postulate 2, you are forced to accept the relativity of simultaneity. There is no escape.

<!-- → [INFOGRAPHIC: Train simultaneity thought experiment — top panel (Bob's frame): train moving right, two lamps at front and back flashing simultaneously, light waves expanding as equal-radius circles from each end, Bob at embankment center receives both simultaneously; bottom panel (Alice's frame): Alice at center of train, front flash arrives first because Alice moves toward it, back flash arrives later; caption: same two flash events, two frames — simultaneous in Bob's frame, not simultaneous in Alice's; the only assumption needed is that light travels at c in both frames] -->

---

## Moving clocks run slow

The relativity of simultaneity leads immediately to time dilation. The cleanest way to see it is with a light clock.

![Two panels. Left: light clock at rest. Photon bounces vertically between two mirrors; tick = 2L/c. Right: clock moving at speed v. Photon takes diagonal path of longer length; tick' = 2L/(c·√(1−v²/c²)) — time dilates.](../images/28-special-relativity-fig-02.png)
*Figure 28.2 — Light Clock — Same Speed of Light, Longer Path, Slower Tick*

Take two mirrors facing each other, separated by distance $D$. A light pulse bounces between them. Each round trip is one tick. In the clock's own rest frame, one tick takes

$$\Delta t_0 = \frac{2D}{c}.$$

This is the *proper time* between two ticks — the time measured by an observer riding with the clock.

Now watch the same clock fly past you at speed $v$. The light pulse still travels at $c$ by postulate 2 — but in your frame, the clock is moving sideways, so the pulse traces a longer zigzag path. Geometry: one leg of the trip is the hypotenuse of a right triangle with legs $D$ (vertical) and $v \Delta t/2$ (horizontal). The hypotenuse must equal $c \Delta t / 2$. So:

$$\left(\frac{c \Delta t}{2}\right)^2 = D^2 + \left(\frac{v \Delta t}{2}\right)^2.$$

Solving for $\Delta t$:

$$\Delta t = \frac{2D/c}{\sqrt{1 - v^2/c^2}} = \frac{\Delta t_0}{\sqrt{1 - v^2/c^2}}.$$

Define the **Lorentz factor**:

$$\boxed{\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.}$$

Then:

$$\boxed{\Delta t = \gamma \, \Delta t_0.}$$

Since $\gamma \geq 1$ always, $\Delta t \geq \Delta t_0$. A moving clock takes *longer* between ticks, as observed from a stationary frame. A moving clock runs slow.

This is not a mechanical effect — not friction, not vibration. Every physical process in the moving frame is affected: radioactive decay, heartbeats, the oscillations of atoms, the reading on a quartz watch. Time itself runs slower in the moving frame, relative to the stationary one.

![Plot of γ = 1/√(1−v²/c²) vs v/c. Stays near 1 until v ≈ 0.5c. Doubles by 0.866c. Diverges as v → c. Markers: highway speed (γ ≈ 1.000000001), LHC protons (γ ≈ 7000).](../images/28-special-relativity-fig-03.png)
*Figure 28.3 — Lorentz Factor γ — Flat Until v ≈ 0.5c, Then Diverges to Infinity*

<!-- → [TABLE: Lorentz factor γ at selected speeds — columns: v/c, γ, time dilation factor, length contraction factor; rows: 0.1c (γ = 1.005), 0.5c (γ = 1.155), 0.9c (γ = 2.29), 0.99c (γ = 7.09), 0.999c (γ = 22.4), 0.9999c (γ = 70.7); student should see that γ is negligible below 0.1c and explodes near c] -->

---

## Moving rulers shrink

![Top: meter stick at rest, length L₀ = 1 m. Bottom: same stick measured from a frame moving at v = 0.866c relative to it. Observer sees L = L₀/γ = 0.5 m. Contraction only along the direction of motion; perpendicular dimensions...](../images/28-special-relativity-fig-05.png)
*Figure 28.5 — Length Contraction — L = L₀/γ, Along the Direction of Motion Only*

The same logic forces length contraction. The *proper length* $L_0$ is the length of an object measured in its own rest frame. An observer moving at velocity $v$ relative to the object, measuring along the direction of motion, gets

$$\boxed{L = \frac{L_0}{\gamma}.}$$

A meter stick flying past you at $0.99c$ (where $\gamma \approx 7.1$) measures about 14 centimeters in your frame.

![Cosmic-ray muons (τ_rest = 2.2 μs) created 15 km up. Newtonian: should not reach ground. Earth frame: muon clock runs slow (γ ≈ 22), so muon lives long enough. Muon frame: Earth approaches at v, atmosphere contracted, distance...](../images/28-special-relativity-fig-04.png)
*Figure 28.4 — Muon Decay — Earth Sees Time Dilation, Muon Sees Length Contraction, Both Agree*

The muon experiment makes both effects vivid. Cosmic-ray muons are created in the upper atmosphere, about 10 km up, when high-energy cosmic rays hit air nuclei. Muons are unstable; their proper lifetime is $\tau_0 = 2.20$ μs. Traveling at $v \approx 0.999c$, a muon covers at most $c \tau_0 = 3 \times 10^8 \times 2.2 \times 10^{-6} \approx 660$ m before decaying — classically. It should not reach sea level. But about 1 muon per cm² per minute does exactly that.

In Earth's frame: the muon's lifetime is dilated by $\gamma \approx 22.4$ to $\tau = 22.4 \times 2.20 \approx 49$ μs. In 49 μs at $0.999c$, it travels about 14.7 km. It makes it.

In the muon's frame: the 10 km distance is contracted to $10/22.4 \approx 0.45$ km. The muon lives its normal 2.20 μs, and travels 0.45 km. It also makes it.

Both frames agree the muon reaches the ground. They disagree on the explanation. This is the hallmark of relativity: the *events* are frame-independent; the *description* of them is not.

Muon survival was quantitatively measured in 1941 by Rossi and Hall on Mount Washington in New Hampshire. The results agreed with time dilation to within a few percent. The experiment can be reproduced in a university laboratory today.

<!-- → [TABLE: Muon experiment in two frames — columns: quantity, Earth's frame, muon's frame; rows: muon speed (0.999c, 0.999c), γ (22.4, 22.4), distance traveled (10 km, 0.45 km = 10/γ), muon lifetime (49 μs = γτ₀, 2.20 μs = τ₀), does muon survive? (yes, yes); caption: the event "muon reaches ground" is frame-independent; the explanation — dilated lifetime vs. contracted distance — is frame-dependent. Both are correct.] -->

---

## Velocities don't add the way you think

If special relativity modifies time and length, it must also modify how velocities combine. In Newtonian mechanics, a ball thrown at $30$ m/s from a train moving at $20$ m/s has speed $50$ m/s relative to the ground. Simple addition. But what if the "ball" is a light pulse emitted forward from a rocket? The ground observer must measure it at $c$ — not $c + v_\text{rocket}$. Newtonian addition must be wrong.

The correct relativistic velocity addition rule, derivable from the postulates:

$$\boxed{u = \frac{v + u'}{1 + vu'/c^2}.}$$

Here $u'$ is the velocity of an object measured in one frame, $v$ is the relative velocity between two frames, and $u$ is the object's velocity in the second frame. For $v, u' \ll c$, the denominator is essentially 1 and you recover classical addition. For $u' = c$:

$$u = \frac{v + c}{1 + vc/c^2} = \frac{v + c}{1 + v/c} = \frac{c(1 + v/c)}{1 + v/c} = c.$$

Light is still $c$. The second postulate is preserved automatically by the addition formula.

Two ships approaching each other at $0.9c$ each (relative to a station) have a relative velocity of

$$u = \frac{0.9c + 0.9c}{1 + 0.81} = \frac{1.8c}{1.81} \approx 0.994c,$$

not $1.8c$. The speed limit is enforced not by some external barrier but by the mathematics of how velocities combine.

<!-- → [CHART: Relativistic vs. classical velocity addition — x-axis: u' (speed of object in moving frame, from 0 to c); y-axis: combined speed u (from 0 to c); two curves: classical u = v + u' (straight line, exceeds c for large u') shown dashed, and relativistic u = (v + u')/(1 + vu'/c²) (curve asymptoting to c) shown solid; plotted for v = 0.5c and v = 0.9c; shaded region above c labeled "forbidden"; caption: no matter how fast each component, the relativistic formula keeps the combined speed below c — the speed of light is a genuine asymptote, not just a large number] -->

---

## Mass is frozen energy

In 1905, Einstein derived a further consequence of the two postulates: the energy content of a body at rest is

$$\boxed{E_0 = mc^2.}$$

Mass and energy are the same thing. Mass is an extraordinarily dense form of energy, and energy has an equivalent mass.

Let that sit for a moment. A 1-gram object at rest has

$$E_0 = (10^{-3})(3 \times 10^8)^2 = 9 \times 10^{13} \text{ J},$$

equivalent to about 20 kilotons of TNT. The Hiroshima bomb released about 15 kilotons. That much energy is sitting in the rest mass of 1 gram of anything — a paper clip, a raisin, a drop of water — locked up in the binding energies that hold matter together. Nuclear fission unlocks a fraction of a percent of it; matter-antimatter annihilation would unlock all of it.

![Bar chart of E = γmc² for an object at different speeds. At rest (γ=1): E = mc² alone. At v = 0.866c (γ=2): kinetic energy equals rest energy. At v = 0.99c (γ=7): KE is 6× rest energy. Reference: 1 kg rest mass = 9 × 10¹⁶ J.](../images/28-special-relativity-fig-06.png)
*Figure 28.6 — E = mc² — Rest Energy Is the Floor; Kinetic Adds on Top*

In the nuclear reactor Enrico Fermi started up under the stands at the University of Chicago on December 2, 1942, uranium-235 fissions into lighter nuclei, and the total rest mass of the products is *less* than the rest mass of the starting materials. The missing mass — about 0.1% — shows up as kinetic energy of the fragments. A gram of uranium-235 fully fissioned releases roughly $8 \times 10^{10}$ joules. A gram of coal burned releases roughly $3 \times 10^4$ joules. The ratio is about three million. The energy density of nuclear fuel is not greater by a little — it is greater by a factor of millions. That is the operating principle of every nuclear reactor and every star.

The full relativistic expressions for momentum and energy are:

$$p = \gamma m u, \qquad E = \gamma m c^2.$$

The kinetic energy is $KE = (\gamma - 1)mc^2$. For $u \ll c$, expand $\gamma$:

$$\gamma = \frac{1}{\sqrt{1 - u^2/c^2}} \approx 1 + \frac{1}{2}\frac{u^2}{c^2} + \ldots$$

so $KE \approx \frac{1}{2}mu^2$ — Newton's kinetic energy recovered as a limit. Special relativity does not contradict classical mechanics; it contains it.

A useful identity relating energy, momentum, and rest mass:

$$E^2 = (pc)^2 + (mc^2)^2.$$

For a massless particle ($m = 0$), this gives $E = pc$. Photons are massless and obey this: they carry momentum, can exert radiation pressure, and can do work — but they have no rest mass. This is the equation that particle physicists use to identify particles from collision debris: measure $E$ and $p$ in a detector, compute $\sqrt{E^2 - (pc)^2}/c^2$, and you get the rest mass.

<!-- → [TABLE: Rest energies and typical kinetic energies — columns: particle/object, rest mass (kg), rest energy (MeV or J), typical KE at relevant speed, γ; rows: electron (rest 0.511 MeV), proton (938 MeV), uranium-235 nucleus, LHC proton at 7 TeV (γ ≈ 7460), cosmic-ray muon at 0.999c (γ ≈ 22.4); student should see when KE ≪ rest energy (non-relativistic) and when KE ≫ rest energy (ultra-relativistic)] -->

---

## A calculation worth doing: LHC protons

At the Large Hadron Collider, protons are accelerated to a kinetic energy of 7 TeV = $7 \times 10^{12}$ eV. The proton's rest energy is $m_p c^2 = 938$ MeV. The kinetic energy is roughly $7 \times 10^6$ MeV — about $7,500$ times the rest energy. So:

$$\gamma = \frac{E}{m_p c^2} = \frac{E_0 + KE}{m_p c^2} \approx \frac{7 \times 10^6}{938} \approx 7{,}460.$$

What is the proton's speed?

$$1 - \frac{v^2}{c^2} = \frac{1}{\gamma^2} \approx \frac{1}{7460^2} \approx 1.8 \times 10^{-8}, \qquad \frac{v}{c} \approx 1 - 9 \times 10^{-9}.$$

The LHC proton travels at $c$ minus about 9 parts per billion.

The LHC ring is 27 km in circumference. In the proton's frame, it is length-contracted to $27 / 7460 \approx 3.6$ meters. One circuit of the ring takes $27 \text{ km}/c \approx 9 \times 10^{-5}$ s in the lab frame; in the proton's frame, the same circuit takes $9 \times 10^{-5} / 7460 \approx 12$ nanoseconds.

Both observers (proton and lab) agree the proton completes one circuit. They disagree on how long the circuit is and how long it took. The physics is the same; the description is not.

From LHC protons at $\gamma = 7{,}460$, scale down to GPS satellites at $v \approx 3{,}870$ m/s and $\gamma - 1 \approx 8 \times 10^{-11}$. The special-relativistic time dilation is tiny — about $-7$ μs/day (satellite clocks slow). But the general-relativistic gravitational effect (clocks run fast at altitude) adds $+45$ μs/day, for a net $+38$ μs/day. Without that correction applied to each satellite's clock, GPS positions would drift by $c \times 38 \text{ }\mu\text{s} \approx 11$ km per day. Your phone's map app depends on Einstein being right.

<!-- → [INFOGRAPHIC: GPS clock correction diagram — satellite orbit at ~20,200 km altitude; two effects labeled with arrows: special-relativistic (satellite moves at 3.87 km/s, clock runs slow by 7 μs/day) and general-relativistic (satellite is higher in gravity well, clock runs fast by 45 μs/day); net correction: +38 μs/day applied to each satellite clock; without correction, position error accumulates at ~11 km/day; caption: both special and general relativity are operating in a device almost everyone uses every day] -->

---

## The correspondence principle

Whenever the chapter has introduced a relativistic formula — time dilation, length contraction, velocity addition, $p = \gamma mu$, $KE = (\gamma - 1)mc^2$ — the formula has a classical limit. As $v/c \to 0$, $\gamma \to 1$, and every relativistic expression reduces to the classical one. This is not a coincidence; it is a requirement that Einstein's theory must satisfy, because Newton's theory is right — in the regime where it was tested.

This is the **correspondence principle**: any new theory must reproduce the predictions of the theories it replaces, in the regime where the old theories worked. Relativity satisfies it. Quantum mechanics, which we reach in Chapter 29, satisfies it too. A theory that didn't satisfy it would be contradicting the successful experiments of the previous centuries, and that is not something a theory gets to do.

The correspondence principle is also a practical tool. A car at 30 m/s has $v/c \approx 10^{-7}$ and $\gamma - 1 \approx 5 \times 10^{-15}$. Relativistic corrections are unmeasurable. A muon at $0.999c$ has $\gamma \approx 22$. Relativistic corrections dominate. When you're not sure whether to use Newton or Einstein, compute $v/c$. If it's much less than 1, classical mechanics is fine. If it's close to 1, use Einstein.

---

## Three commitments

**Time and length are frame-dependent.** Moving clocks run slow by $\gamma$; moving rulers shrink by $\gamma$ in the direction of motion. Both effects are real — not apparent, not instrumental — and they must be consistent with each other, as the muon experiment shows.

**No massive object can reach $c$.** The relativistic momentum $p = \gamma mu$ diverges as $u \to c$: it would take infinite energy. Velocities add according to $u = (v + u')/(1 + vu'/c^2)$, and no combination of sub-$c$ velocities produces a result at or above $c$.

**Mass is one form of energy.** $E_0 = mc^2$, and the total energy is $E = \gamma mc^2$. The missing mass in nuclear reactions shows up as kinetic energy of products. The energy-momentum relation $E^2 = (pc)^2 + (mc^2)^2$ holds for all particles, massive or massless.

The single deepest fact: **what is invariant — the same in every frame — is more fundamental than what changes.** The speed of light is invariant. The rest mass is invariant. The spacetime interval between two events is invariant. The laws of physics are invariant. These are the fixed points of the theory. Everything else — time between events, distance between events, simultaneity — depends on who's asking.

---

## Exercises

### Warm-up

**28.1** *(Postulates)* State Einstein's two postulates of special relativity in one sentence each. Which one was present in some form in Galileo's mechanics, and which one was the genuinely new ingredient in 1905?

**28.2** *(Lorentz factor)* Compute $\gamma$ for the following speeds: (a) $v = 0.10c$, (b) $v = 0.50c$, (c) $v = 0.90c$, (d) $v = 0.99c$. For each, state whether classical mechanics would introduce a significant error (say, more than 1%).

**28.3** *(Time dilation)* A muon at rest has a proper lifetime of $\tau_0 = 2.20$ μs. If it moves at $v = 0.95c$, what is its lifetime as measured in Earth's frame?

**28.4** *(Length contraction)* A spaceship has a proper length of 500 m. At what speed must it travel for an observer on Earth to measure its length as 250 m? Express your answer in terms of $c$.

**28.5** *(Rest energy)* Compute the rest energy of a proton ($m_p = 1.67 \times 10^{-27}$ kg) in joules and in MeV. Verify it equals 938 MeV.

### Application

**28.6** *(Time dilation — GPS)* A GPS satellite moves at approximately 3,870 m/s relative to Earth's surface. Compute $\gamma - 1$ for the satellite. By how many nanoseconds per day does the satellite's clock run slow due to special relativity alone? (Ignore the general-relativistic correction for this problem.)

**28.7** *(Velocity addition)* Two protons approach each other in the lab frame, each moving at $0.85c$. (a) Compute their relative velocity using the relativistic addition formula. (b) Compute what the classical formula would give. (c) By what fraction do the results differ?

**28.8** *(Relativistic momentum)* An electron ($m = 9.11 \times 10^{-31}$ kg) moves at $v = 0.98c$. (a) Compute $\gamma$. (b) Compute its relativistic momentum. (c) Compute its classical momentum. (d) By what factor does the relativistic result exceed the classical one?

**28.9** *(Kinetic energy)* A proton is accelerated to $v = 0.999c$. (a) Compute its kinetic energy $KE = (\gamma - 1)m_p c^2$ in MeV. (b) How does this compare to the classical prediction $\frac{1}{2}m_p v^2$? Express the ratio.

### Synthesis

**28.10** *(Muon experiment — both frames)* A cosmic-ray muon is created 8.0 km above sea level and travels at $v = 0.994c$. (a) Compute $\gamma$. (b) In Earth's frame, how long does it take to reach the ground? (c) In the muon's frame, what is the distance from creation point to ground? (d) In the muon's frame, how long does the trip take? (e) Show that the muon survives the trip in both frames (compare to $\tau_0 = 2.20$ μs).

**28.11** *(Mass-energy equivalence)* A nuclear power plant produces 1,000 MW of thermal power. (a) At what rate is mass being converted to energy (kg/s)? (b) How much mass is converted in one year of operation? (c) A 1,000 MW coal plant burns roughly $3 \times 10^9$ kg of coal per year. Compare the mass converted to energy in each case.

**28.12** *(Correspondence principle)* A car moves at $v = 30$ m/s. (a) Compute $v/c$ and $\gamma - 1$. (b) By what fraction does the relativistic kinetic energy differ from the classical kinetic energy $\frac{1}{2}mv^2$? (c) For what speed (in m/s) would the relativistic and classical kinetic energies differ by exactly 1%?

### Challenge

**28.13** *(Twin paradox)* Alice rockets to a star 6.0 light-years away at $v = 0.80c$, immediately turns around, and returns at the same speed. Bob stays on Earth. (a) Compute the round-trip time in Earth's frame. (b) Compute Alice's elapsed time during the outbound leg in her frame. (c) Compute the total elapsed time for Alice over the full round trip. (d) When Alice returns, how much younger is she than Bob? (e) Explain in one sentence why Alice ages less even though both observers see the other's clock running slow during the constant-velocity legs.

**28.14** *(Energy-momentum invariant)* A particle detector measures a particle's total energy as $E = 1200$ MeV and its momentum as $p = 1100$ MeV/$c$. (a) Compute $m c^2 = \sqrt{E^2 - (pc)^2}$ and identify the particle (compare to the proton rest energy of 938 MeV, the pion rest energy of 135 MeV, and the electron rest energy of 0.511 MeV). (b) Compute $\gamma$ and $v/c$ for this particle. (c) Explain in one sentence why $E^2 - (pc)^2$ is useful for particle identification even when $E$ and $p$ individually depend on the observer's frame.

---

## Still puzzling

The deepest unresolved question this chapter raises: *why does light have a finite, universal speed, and why exactly $c = 2.998 \times 10^8$ m/s?* Maxwell's equations give $c = 1/\sqrt{\mu_0 \varepsilon_0}$, but the values of $\mu_0$ and $\varepsilon_0$ are themselves unexplained at a deeper level. General relativity identifies $c$ as a geometric property of spacetime — the conversion factor between meters and seconds in a unified spacetime — but still doesn't derive the numerical value from first principles. Some quantum-gravity programs aim to; none has yet succeeded.

---

## LLM Exercise — Chapter 28: Special Relativity in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry for special relativity. *Note:* most everyday phenomena involve speeds far below $c$, so relativistic effects are tiny. You have two options: (a) compute the (microscopic) relativistic correction to your phenomenon, or (b) write an "exception entry" explaining why this chapter doesn't apply directly and identifying the most distant connection.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 28, I want to think about special relativity. Most everyday phenomena are non-relativistic, so the direct effects are negligible. I want to choose between two options:

Option A — compute the (tiny) relativistic correction to my phenomenon. For a bike commute at ~5 m/s: time dilation is unimaginably small. For an espresso machine pumping water at a few m/s: same. I'd compute γ, find that γ - 1 ~ 10^(-16), and report that classical physics is essentially exact.

Option B — find the most distant connection. For a bike commute: my GPS uses relativistic corrections (~38 μs/day for the satellites). For a coffee maker: the precision atomic clocks underlying GPS rely on relativistic atomic-physics calculations. For a basketball shot: the lights overhead are filaments emitting EM radiation, and Einstein's photoelectric explanation (Chapter 29) was awarded the same year as his special-relativity papers. For a marathon: the GPS watch I wear depends on relativistic clock corrections in its satellites.

Please:

1. Identify which option fits better for my phenomenon, and explain why.

2. If Option A: compute the relativistic correction (γ - 1) to whatever quantity is most relevant. Report with units. This will likely be a very small number — that's the point.

3. If Option B: identify the most distant relativistic connection (likely GPS satellite clock corrections) and explain how it indirectly impacts my phenomenon.

4. Either way: write one sentence on what would happen if relativity were "off" — what specific failures would occur in technology I use.

5. One sentence connecting this to Chapter 29 (quantum mechanics) — the next chapter takes EM radiation and reveals it has discrete photon structure.

Save the output as logbook/chapter-28-relativity.md.
```

### What this produces

A Logbook entry that either quantifies the (tiny) relativistic effect on your phenomenon or honestly admits the chapter is an exception and identifies the indirect technology link.

### How to adapt this prompt

- *For phenomena with no relativistic content:* Option B almost always reveals a GPS/atomic-clock link.
- *For phenomena involving fast-moving particles:* If you happen to be analyzing cosmic rays, particle accelerators, or astrophysics, Option A is fully applicable.
- *For ChatGPT/Gemini:* Identical with interface substitutions.

### Connection to previous chapters

Builds on Chapter 24 (the speed of light $c$ as electromagnetic wave speed). Uses Chapter 1's discipline of significant figures and uncertainty.

### Preview of next chapter

Chapter 29 (quantum mechanics) introduces the photon and shows that classical wave optics (Chapter 27) cannot fully explain the photoelectric effect. The 1905 paper that won Einstein the 1921 Nobel Prize was on the photoelectric effect, not relativity.

---

## Connections forward

Chapter 29 (quantum mechanics) introduces the photon, the photoelectric effect, and wave-particle duality — completing the modernization of physics that special relativity began. Chapter 30 (atomic physics) uses relativistic energy-mass equivalence to interpret the binding energies of atoms. Chapter 31 (radioactivity) builds entirely on $E = mc^2$ to explain the energies released in nuclear decays. Chapter 33 (particle physics) uses $E^2 = (pc)^2 + (mc^2)^2$ routinely to identify particles from their tracks in detectors. Chapter 34 (frontiers) introduces general relativity — the extension to accelerating frames and gravity — and to current attempts to merge it with quantum mechanics.

---

**Tags:** special-relativity, time-dilation, length-contraction, $E=mc^2$, Lorentz-factor, Feynman-style
