# Chapter 10 — Electromagnetic Induction and Faraday's Law

*Change the flux and you get an EMF. The minus sign is energy conservation.*

---

On August 29, 1831, Michael Faraday wound two coils on opposite sides of a soft iron ring at the Royal Institution in London. One coil he connected through a switch to a battery. The other he ran across the room to a galvanometer.

He closed the switch. The galvanometer's needle jumped — and then returned to zero, while the battery current kept flowing steadily through the first coil. He opened the switch. The needle jumped the other way, and again returned to zero.

That was the whole discovery. Not current in coil A making current in coil B — that would have been exciting but simple. What Faraday found was stranger: the galvanometer only moved *at the transitions*. Steady current, however strong, did nothing. Only change produced an effect — the moment of switch-on, the moment of switch-off. The transient was the discovery.

Joseph Henry had seen essentially the same thing at the Albany Academy roughly a year earlier. He didn't publish until 1832; Faraday published first, in January of that year. The law bears Faraday's name. The unit of inductance bears Henry's.

James Clerk Maxwell, thirty years later, wrote the transient down as an equation. That equation — Faraday's law — is the subject of this chapter, and it is why roughly 85% of the electricity now in the grid arrived there through a spinning coil.

---

## What flux is

Before the law, the quantity it governs.

The **magnetic flux** through a surface $S$ bounded by a loop is:

$$\Phi_B = \iint_S \vec{B}\cdot d\vec{A}$$

For a flat loop of area $A$ in a uniform field $\vec{B}$, with the loop's normal making angle $\theta$ to the field, this simplifies to $\Phi_B = BA\cos\theta$. Units: the **weber** (Wb), where 1 Wb = 1 T·m².

Flux is a measure of how much field passes through the loop — not just the field strength, but how much of it is threading through, at what angle, over how much area. Think of it as counting field lines through the surface: more lines, more flux; field parallel to the surface, zero flux; area reduced to zero, zero flux.

Three things can change the flux through a loop. The field magnitude $B$ can change. The area $A$ can change. The angle $\theta$ between the loop and the field can change. Any one of these produces an EMF. Each corresponds to a different class of device: transformers respond to changing $B$; sliding-rod generators respond to changing $A$; rotating-coil generators respond to changing $\theta$. They are all one law.

![flux visualization for a flat loop — top row: loop face-on to a strong B field (high flux, dense field lines through the surface); middle row: same loop tilted 45° (reduced flux, fewer lines threading through); bottom...](../images/10-electromagnetic-induction-fig-01.png)
*Figure 10.1 — Three Routes to a Changing Flux*

<!-- → [IMAGE: flux visualization for a flat loop — top row: loop face-on to a strong B field (high flux, dense field lines through the surface); middle row: same loop tilted 45° (reduced flux, fewer lines threading through); bottom row: loop edge-on (zero flux, all lines parallel to surface) — to build intuition for Φ_B = BA cosθ before the formula appears] -->

---

## Faraday's law

$$\boxed{\;\varepsilon = -\frac{d\Phi_B}{dt}\;}$$

The **EMF** induced around a loop equals the negative time-derivative of the magnetic flux through it.

For a coil of $N$ turns, each turn contributes its own EMF in series:

$$\varepsilon = -N\frac{d\Phi_B}{dt}$$

The EMF is in volts — the same units as a battery — because it does the same job: it drives a current $I = \varepsilon/R$ through whatever resistance the loop presents.

A comment on language. In Chapter 4, voltage was the line integral of a conservative electric field, path-independent. The induced EMF is the line integral of a *non-conservative* electric field around a closed loop. $\oint \vec{E}\cdot d\vec{\ell} = -d\Phi_B/dt \neq 0$: the integral around a closed loop is nonzero, which means the field is not conservative, which means path matters. The word "EMF" marks this distinction. After we have made it once, we will relax back to "voltage" in examples; the distinction has done its work.

![three-panel diagram showing the three ways flux can change — panel 1: a stationary loop with B increasing (dB/dt ≠ 0, transformer case); panel 2: a rod sweeping out area at velocity v (dA/dt ≠ 0, motional EMF case); p...](../images/10-electromagnetic-induction-fig-02.png)
*Figure 10.2 — Lenz's Law as Energy Conservation*

<!-- → [INFOGRAPHIC: three-panel diagram showing the three ways flux can change — panel 1: a stationary loop with B increasing (dB/dt ≠ 0, transformer case); panel 2: a rod sweeping out area at velocity v (dA/dt ≠ 0, motional EMF case); panel 3: a loop rotating in a fixed B field (dθ/dt = ω, generator case) — each panel labeled with which device it corresponds to] -->

---

## The minus sign

Heinrich Lenz, 1834: **the induced current flows in whichever direction opposes the change in flux that produced it.**

This is not a second law. It is the physical content of the minus sign in Faraday's law. But it is worth understanding why that sign must be there, rather than just accepting it.

Suppose the sign were positive. Push a bar magnet toward a coil. The increasing flux would induce a current in the sense that *helps* the approaching magnet — the coil's own magnetic field would attract the magnet, pulling it in faster. As it moves faster, the rate of flux change increases. The induced current grows. The force grows. The magnet accelerates. The coil dissipates $I^2R$ in its resistance — producing heat — while the kinetic energy of the magnet is simultaneously increasing. You have a closed system gaining energy from nothing. Perpetual motion, first kind. Prohibited.

The only escape is the minus sign. The induced current must oppose the change. Push the magnet in, the coil pushes back. Pull the magnet out, the coil pulls it back. Your hand pays the bill. Every joule of electrical output traces back to a joule of mechanical work done against that opposing force.

Lenz's law is energy conservation, wearing electromagnetic clothing.

![two-panel Lenz's law diagram — left panel: bar magnet approaching a coil, induced current direction shown circling the coil face, the coil's resulting magnetic moment shown opposing the approaching field — right panel...](../images/10-electromagnetic-induction-fig-03.png)
*Figure 10.3 — Motional EMF*

<!-- → [IMAGE: two-panel Lenz's law diagram — left panel: bar magnet approaching a coil, induced current direction shown circling the coil face, the coil's resulting magnetic moment shown opposing the approaching field — right panel: magnet receding, induced current reversed, coil moment now attracting the departing magnet — arrows showing the force on the magnet is always opposing the motion] -->

---

## Motional EMF: the rod on rails

Here is the simplest possible geometry for motional EMF. Two long parallel rails, connected at one end by a resistor $R$. A conducting rod of length $L$ slides along the rails at velocity $v$, perpendicular to both the rails and to a uniform magnetic field $\vec{B}$ pointing out of the page.

![rod-on-rails diagram — two parallel horizontal rails connected at left by resistor R, rod of length L sliding right at velocity v, uniform B out of page shown as dots, the enclosed rectangular area growing as the rod...](../images/10-electromagnetic-induction-fig-04.png)
*Figure 10.4 — AC Generator*

<!-- → [IMAGE: rod-on-rails diagram — two parallel horizontal rails connected at left by resistor R, rod of length L sliding right at velocity v, uniform B out of page shown as dots, the enclosed rectangular area growing as the rod moves, and the induced current direction shown by an arrow] -->

As the rod moves right, the area enclosed by the circuit grows at $dA/dt = Lv$. The flux grows at $d\Phi_B/dt = BLv$. By Faraday's law:

$$\varepsilon = BLv$$

Now forget the flux and think about the electrons in the moving rod. Each electron is moving with the rod at velocity $v$ in the field $\vec{B}$. The Lorentz force on each electron is $q\vec{v} \times \vec{B}$ — directed along the rod, toward one end. Charge separates until an electrostatic field inside the rod exactly balances the magnetic force. The potential difference that builds up end-to-end is exactly $BLv$.

Two completely different routes — Faraday's law applied to the changing flux, and the Lorentz force applied to each electron in the moving rod — give the same answer. This agreement is not an accident. It is a consequence of the fact that $\vec{E}$ and $\vec{B}$ are, at bottom, two faces of a single relativistic field tensor. A moving observer sees a different mix of electric and magnetic field than a stationary observer, but the forces on charges come out the same.

The power accounting is clean. If the rails close a circuit through $R$, the current is $I = BLv/R$. The rod carrying this current through field $\vec{B}$ experiences a retarding force $F = BIL = B^2L^2v/R$ opposing its motion (Lenz, necessarily). The mechanical power you supply pushing the rod:

$$P_{\text{mech}} = Fv = \frac{B^2L^2v^2}{R}$$

The electrical power dissipated in $R$:

$$P_{\text{elec}} = I^2R = \frac{(BLv)^2}{R}$$

They are equal. Mechanical work in equals electrical energy out, exactly, always.

![energy flow diagram for the rod-on-rails — external agent shown pushing rod right at velocity v, rod labeled with EMF = BLv and internal resistance r_rod, current I = BLv/R shown flowing around the circuit to the exte...](../images/10-electromagnetic-induction-fig-05.png)
*Figure 10.5 — Transformer*

<!-- → [IMAGE: energy flow diagram for the rod-on-rails — external agent shown pushing rod right at velocity v, rod labeled with EMF = BLv and internal resistance r_rod, current I = BLv/R shown flowing around the circuit to the external resistor R, power labels P_mech = F·v on the left and P_elec = I²R on the right, with an equals sign between them — the mechanical-to-electrical energy conversion made explicit] -->

---

## The generator

Rotate a coil. That's the whole machine.

A flat coil of $N$ turns and area $A$ spins at angular frequency $\omega$ inside a uniform field $\vec{B}$. At time $t$ the coil's normal makes angle $\omega t$ with $\vec{B}$:

$$\Phi_B(t) = NBA\cos(\omega t)$$

Faraday's law:

$$\varepsilon(t) = -\frac{d\Phi_B}{dt} = NBA\omega\sin(\omega t)$$

The output is sinusoidal. Peak value $\varepsilon_0 = NBA\omega$. RMS value $\varepsilon_{\text{rms}} = \varepsilon_0/\sqrt{2}$, which is what voltmeters read and what's labeled on appliances.

The frequency is a mechanical choice. A generator with a two-pole rotor on a steam turbine running at 3600 rpm produces $\omega = 2\pi \times 60 = 120\pi$ rad/s — US line frequency, 60 Hz. European standard is 50 Hz, requiring 3000 rpm. These frequencies were chosen in the 1890s to match available steam-turbine shaft speeds and locked in by decades of installed infrastructure. There is nothing fundamental about 60 Hz; it is history calcified into electrical code.

![rotating coil generator diagram — rectangular coil in uniform B field shown at three moments: normal parallel to B (maximum flux, zero EMF), normal at 45° (intermediate), normal perpendicular to B (zero flux, maximum...](../images/10-electromagnetic-induction-fig-06.png)
*Figure 10.6 — RL Circuit*

<!-- → [IMAGE: rotating coil generator diagram — rectangular coil in uniform B field shown at three moments: normal parallel to B (maximum flux, zero EMF), normal at 45° (intermediate), normal perpendicular to B (zero flux, maximum EMF) — with the sinusoidal output waveform plotted below showing the 90° phase relationship between flux and EMF] -->

The formula $\varepsilon_0 = NBA\omega$ shows exactly how to build a more powerful generator: more turns, bigger area, stronger field, or faster rotation. Large utility generators run at the thermal and mechanical limits of all four.

---

## The transformer

Wind two coils on the same iron core. Run AC through the first. The changing current produces changing flux through the core. By Faraday's law, that changing flux induces an EMF in the second coil.

The iron core is there to channel essentially all of the flux from one coil through the other — it is the thing that makes the coupling tight. Without it, most of the flux from coil 1 would miss coil 2 entirely, and the device would be inefficient.

In the ideal limit — perfect flux coupling, no resistive losses — the same $d\Phi/dt$ threads through every turn on both sides. Each turn on the primary contributes one unit of EMF; each turn on the secondary contributes one unit. The EMF *per turn* is identical on both sides, so the voltages are in proportion to the turn counts:

$$\frac{V_2}{V_1} = \frac{N_2}{N_1}$$

Power is conserved — the transformer does not amplify energy:

$$V_1 I_1 = V_2 I_2 \implies \frac{I_2}{I_1} = \frac{N_1}{N_2}$$

Step up the voltage by ten, the current falls by ten. Power stays the same.

![transformer schematic — iron core (shown as a rectangle) with primary coil (N₁ turns) on left and secondary coil (N₂ turns) on right, flux lines threading the core, input voltage V₁ and output voltage V₂ labeled, with...](../images/10-electromagnetic-induction-fig-07.png)
*Figure 10.7 — RC and RL*

<!-- → [IMAGE: transformer schematic — iron core (shown as a rectangle) with primary coil (N₁ turns) on left and secondary coil (N₂ turns) on right, flux lines threading the core, input voltage V₁ and output voltage V₂ labeled, with the ratio equation — both an isolation transformer (N₁ = N₂) and a step-up transformer (N₂ > N₁) shown side by side] -->

This is why long-distance power transmission runs at hundreds of kilovolts. Line losses go as $I^2R$. The same power $P = IV$ can be transmitted at high $V$ and correspondingly low $I$. At 345 kV instead of 240 V, the current is smaller by a factor of about 1,440, so the $I^2R$ loss in the line is smaller by a factor of roughly two million. Without the transformer — without the ability to step voltage up for transmission and back down for use — every city would have to be within a few kilometers of its power plant, because the wire losses would be prohibitive at low voltage.

Real transformers lose 1–3% to copper resistance, eddy currents in the iron core, and hysteresis as the core's magnetic domains cycle. Large utility transformers achieve 98–99.5% efficiency. The ideal-transformer formula is what real transformers deliver when those losses are small.

---

## Self-inductance

Every coil carrying current creates a magnetic field. That field passes through its own turns. If the current changes, the flux changes, and by Faraday's law there is an induced EMF in the coil itself — opposing the change. The coil resists changes in its own current.

Define the **self-inductance** $L$ of a coil by:

$$N\Phi = LI$$

If $I$ changes in time:

$$\varepsilon = -L\frac{dI}{dt}$$

Units: the **henry** (H) = V·s/A. Joseph Henry's name on the unit that bears his name for the discovery he made first but published second.

For a long solenoid of $n$ turns per meter, cross-section $A$, length $\ell$, the interior field is $B = \mu_0 n I$ (Chapter 9), so the flux per turn is $\mu_0 n I A$, and the total flux linkage $N\Phi = n\ell \cdot \mu_0 n I A = \mu_0 n^2 V \cdot I$, where $V = \ell A$ is the interior volume. Therefore:

$$\boxed{\;L_{\text{solenoid}} = \mu_0 n^2 V\;}$$

The inductance depends only on geometry. $n$ is the winding density; $V$ is the physical size. An iron core multiplies this by $\mu_r$ (hundreds to thousands), reaching the henry range.

<!-- → [IMAGE: solenoid inductance diagram — cross-section of a long solenoid with n turns/m labeled, interior field B = μ₀nI shown as uniform horizontal arrows, a single turn highlighted with flux Φ = BA through it, and the labeling L = μ₀n²V — also a side-by-side comparing an air-core solenoid (μ_r = 1) with an iron-core solenoid (μ_r ≫ 1) to show how the core multiplies inductance] -->

---

## Energy in the magnetic field

Build a current $I$ in an inductor from zero. The back-EMF $\varepsilon = -L\,dI/dt$ opposes the rise; the external source must supply power $P = LI\,(dI/dt)$ to push current through against it. Integrate:

$$U = \int_0^I L I'\, dI' = \tfrac{1}{2}LI^2$$

For a solenoid with $L = \mu_0 n^2 V$ and $B = \mu_0 n I$:

$$U = \tfrac{1}{2}\frac{B^2}{\mu_0} \cdot V$$

which gives a **magnetic energy density**:

$$\boxed{\;u_B = \frac{B^2}{2\mu_0}\;}$$

This is the magnetic partner of the electric energy density $u_E = \tfrac{1}{2}\varepsilon_0 E^2$ from Chapter 5. The claim is that the energy is stored *in the field*, distributed through the volume the field occupies. A superconducting loop carrying persistent current has $\tfrac{1}{2}LI^2$ of energy stored in the magnetic field of that loop — energy that was put in when the current was established, held indefinitely with zero loss, and recoverable by letting the current decay through a load. Cut the current path suddenly and the field collapses: the energy comes out as a voltage spike, a spark, a flash of heat. The energy was in the field, not in the wire.

This is not just bookkeeping. In Chapter 11, when we find that electromagnetic waves carry energy through empty space far from any source, the energy they carry is exactly $u_E + u_B$ integrated over the wave's volume, propagating at $c$. The field energy is real. It travels. It can be deposited in a distant antenna.

---

## The RL circuit

Close a switch connecting a battery $\varepsilon$, a resistor $R$, and an inductor $L$ in series. Kirchhoff's voltage law:

$$\varepsilon - IR - L\frac{dI}{dt} = 0$$

The solution is:

$$\boxed{\;I(t) = \frac{\varepsilon}{R}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{L}{R}\;}$$

The current rises exponentially toward $\varepsilon/R$ with time constant $\tau = L/R$. At $t = 0$, the inductor carries zero current and its back-EMF equals the full source voltage — the inductor looks like an open circuit at the instant of switch-on. At $t \gg \tau$, the current has reached $\varepsilon/R$ and $dI/dt \to 0$ — the inductor looks like a short circuit at steady state.

<!-- → [CHART: I(t) vs. t for an RL circuit — exponential rise from 0 to ε/R, with τ = L/R marked on the time axis, and the 63% point (I = ε/R · (1 - 1/e)) labeled — also show the back-EMF ε_L(t) = L dI/dt as a decaying exponential on the same axes] -->

There is a table worth building. The RL circuit and the RC circuit from Chapter 5 are structural mirrors of each other:

<!-- → [TABLE: RC vs. RL circuit comparison — columns: quantity, RC circuit, RL circuit — rows: time constant (RC vs. L/R), stored energy (½CV² vs. ½LI²), stored in (electric field vs. magnetic field), energy density (½ε₀E² vs. B²/2μ₀), element resists changes in (voltage vs. current), behavior at t = 0 (capacitor: open circuit → wait, inductor: open circuit → same), behavior at t → ∞ (capacitor: open circuit, inductor: short circuit)] -->

The inverted dependence on $R$ is the thing that catches people. In RC circuits, larger $R$ makes the charging slower: $\tau = RC$. In RL circuits, larger $R$ makes the rise faster: $\tau = L/R$. Derive the time constant from the ODE every time rather than borrowing intuition from the RC case.

---

## Eddy currents

Faraday's law applies to every closed conducting path — including ones you didn't intend to create.

A solid block of metal inside a region of changing $\vec{B}$ has countless closed paths available to induced currents: loops threading through the bulk in every direction. These **eddy currents** circulate, and by Lenz, they produce magnetic fields opposing the change. The block feels a retarding force whenever the flux through it changes.

Three consequences worth knowing.

**Magnetic braking.** Drop a strong neodymium magnet down a copper tube. It falls slowly — far slower than free fall — because eddy currents in the tube wall produce a Lenz-opposing force that nearly balances gravity. The magnet's kinetic energy is being continuously converted to heat in the copper. This is used in regenerative braking systems for trains and elevators, and in the braking of rotating machinery where mechanical contact wear is unacceptable.

**Transformer lamination.** A solid iron transformer core would itself act as a fat conducting loop and dissipate enormous eddy-current losses — the power delivered to the load would mostly end up as heat in the core. The fix is to build the core from thin insulated sheets, each about 0.3 mm thick, stacked in the direction that forces any induced loop to be confined to one thin lamina rather than threading the bulk. Eddy currents scale as the square of the sheet thickness; halving the thickness quarters the loss.

<!-- → [IMAGE: transformer core lamination diagram — left showing a solid core with broad circular eddy current paths drawn in the bulk; right showing the same core laminated into thin insulated sheets, with eddy current loops confined to each thin layer — illustrating how lamination reduces the available loop area and thus the eddy current magnitude] -->

**Induction cooktops.** Drive a flat spiral coil at ~25 kHz beneath glass. The AC magnetic field induces eddy currents in ferromagnetic cookware sitting on top; the pan heats from $I^2R$ in its own bulk. The glass surface stays cool because it's an electrical insulator and doesn't support eddy currents. The requirement for ferromagnetic cookware is real: aluminum and copper have large skin depth at 25 kHz and couple poorly to the field, so they barely heat.

---

## What induction is not

**It does not require motion.** Faraday's own iron-ring experiment had no moving parts — only a switch being thrown. The changing current in coil A produced a changing flux in the iron ring, which induced an EMF in coil B. A stationary loop near an AC power line develops an induced voltage from $\partial \vec{B}/\partial t$ alone. A stationary loop inside an MRI scanner picks up an EMF when the field gradients switch — at $dB/dt \sim 50$ T/s this is large enough to produce peripheral nerve stimulation in tissue if the gradient switches fast enough.

**A wire is not necessary.** The non-conservative electric field created by a changing $\vec{B}$ exists throughout space whether or not a wire is present to respond to it. The wire makes the effect measurable by giving the field somewhere to do work. Remove the wire, and the induced $\vec{E}$ is still there, circling the region of changing flux, pointing perpendicular to every radius. This is the form Faraday's law takes in Maxwell's equations — not a statement about circuits, but a statement about fields:

$$\oint \vec{E}\cdot d\vec{\ell} = -\frac{d\Phi_B}{dt}$$

True everywhere in space, whether or not a conductor closes the loop on the left side.

---

## Looking forward: where this chapter leads

There is a symmetry in Maxwell's equations that this chapter half-reveals. Faraday says: a changing $\vec{B}$ creates a circulating $\vec{E}$. The arrow goes one way: $\dot{B} \to E$.

Maxwell, in 1861, stared at the equations available to him — Coulomb, Gauss, Ampère — and asked the obvious symmetric question: does a changing $\vec{E}$ create a circulating $\vec{B}$? The un-augmented Ampère's law said no. Maxwell noticed this was inconsistent with charge conservation at a capacitor that is charging: current flows into the plates, but in the gap between the plates there is no conduction current, so Ampère's law (then written) said the magnetic field around the gap would be discontinuous. Maxwell added a term — the **displacement current** $\varepsilon_0\,\partial\vec{E}/\partial t$ — to fix the inconsistency.

That fix completed the symmetry: $\dot{B} \to E$ and $\dot{E} \to B$. And the consequence was immediate. If a changing $\vec{E}$ produces a $\vec{B}$, and a changing $\vec{B}$ produces an $\vec{E}$, the two fields can sustain each other without any source charges or currents — a self-propagating disturbance. Maxwell computed the speed at which it would propagate:

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$$

Plugging in the constants measured by wholly different experiments — the permittivity of free space from electrostatics, the permeability from magnetostatics — he got $3 \times 10^8$ m/s. The speed of light, known since Rømer's observations of Jupiter's moons in 1676. Maxwell wrote in 1865 that this result "suggests" that light is an electromagnetic disturbance. He was being characteristically modest. It is not a suggestion. It is the prediction of a theory that has not failed a single experimental test in 160 years.

Chapter 11 is that prediction.

---

## Exercises

**Warm-up.** A square loop of side $a = 10$ cm sits in a uniform field $B = 0.4$ T perpendicular to the loop's plane. The field decreases linearly to zero over $\Delta t = 0.2$ s. (a) Compute the magnitude of the induced EMF. (b) If the loop has resistance $R = 2$ Ω, find the induced current. (c) Identify the direction of the induced current (clockwise or counterclockwise as seen from the direction $\vec{B}$ originally pointed) using Lenz's law — and explain the reasoning in one sentence. *Tests: Faraday's law from changing B, Lenz direction.*

**Warm-up.** A rectangular loop of sides $a$ and $b$, resistance $R$, enters a region of uniform $\vec{B}$ (out of the page) at constant velocity $v$. (a) Find $\varepsilon$, $I$, and the net force on the loop while the leading edge is inside but the trailing edge is still outside. (b) Find the same three quantities once the loop is fully inside the uniform-field region. (c) Find them as the loop exits on the far side. Sketch $\varepsilon$ as a function of position $x$ across the full traversal from outside-in to inside to outside-out. *Tests: motional EMF from changing area, Lenz retarding force, recognizing the flux-constant case.*

**Warm-up.** The generator worked example: $N = 100$ turns, $A = 0.01$ m², $\omega = 120\pi$ rad/s (60 Hz), $B = 0.5$ T. (a) Compute the peak EMF. (b) Compute the RMS EMF. (c) What shaft speed in rpm corresponds to $\omega = 120\pi$ rad/s for a two-pole rotor? (d) If $N$ is doubled, what happens to the peak EMF and the frequency? *Tests: generator formula, RMS, mechanical–electrical connection, sensitivity to parameters.*

**Application.** An RL circuit has $L = 2$ H, $R = 10$ Ω, and is driven by $\varepsilon = 20$ V. The switch is closed at $t = 0$. (a) Find the steady-state current. (b) Find the time constant $\tau$. (c) At what time does the current reach 90% of its final value? (d) Find the energy stored in the inductor at steady state. (e) Compare $\tau = L/R$ to the RC time constant $\tau = RC$ — explain in one sentence why a larger $R$ makes RL rise *faster* but RC rise *slower*. *Tests: RL solution, energy stored, the inverted-R intuition trap.*

**Application.** A solenoid is 30 cm long, has a circular cross-section of radius 1 cm, and carries 3000 turns. (a) Find the self-inductance $L$. (b) If the current through it is 4 A, find the stored magnetic energy. (c) Find the magnetic energy density inside the solenoid. (d) Confirm that energy density × volume equals the stored energy from (b). *Tests: solenoid inductance formula, energy storage, energy density, internal consistency check.*

**Application.** A phone charger transformer steps 120 V AC down to 5 V to charge a device drawing 2 A. The primary has $N_1 = 1000$ turns. (a) Find $N_2$. (b) Find the primary current, assuming an ideal transformer. (c) The real transformer dissipates 0.5 W as heat. What is its efficiency? (d) Explain physically what generates that heat — which of the three loss mechanisms (copper resistance, eddy currents, hysteresis) does each part of the transformer experience? *Tests: transformer ratio, power conservation, real losses.*

**Synthesis.** A conducting rod of length $L = 0.5$ m slides at $v = 3$ m/s along two frictionless rails in a uniform field $B = 0.8$ T perpendicular to the rod and rails. The rails are closed by a resistor $R = 4$ Ω. (a) Find the induced EMF using Faraday's law (changing area). (b) Find the same EMF using the Lorentz force on the conduction electrons. (c) Find the current and the retarding force on the rod. (d) Find the mechanical power required to keep the rod moving at constant $v$, and verify it equals the electrical power dissipated in $R$. *Tests: two-route motional EMF derivation, power balance, Lenz retarding force.*

**Synthesis.** A power-grid transmission line has total resistance $R_\text{line} = 30$ Ω and must carry $P = 500$ MW over 200 km. (a) Find the line current and $I^2R$ loss at $V = 110$ kV. (b) Repeat at $V = 345$ kV. (c) Repeat at $V = 765$ kV. (d) Express the loss in part (c) as a fraction of the delivered power. (e) Show algebraically that the fractional loss scales as $1/V^2$, which is the quantitative reason every long-haul transmission line uses the highest voltage feasible. *Tests: P = IV and I²R together, transformer's role in grid economics, algebraic scaling argument.*

**Challenge.** A 5 cm × 5 cm flat coil of $N = 500$ turns sits in an MRI gradient field ramping at $dB/dt = 30$ T/s, with the coil normal aligned with the ramping component. (a) Find the induced EMF. (b) If the coil has resistance $R = 8$ Ω, find the induced current. (c) Estimate the magnitude of the induced electric field at the rim of the coil (treat the coil as circular and use $\oint \vec{E}\cdot d\vec{\ell} = -d\Phi_B/dt$ with the path being the coil's circumference). (d) The FDA peripheral-nerve-stimulation threshold for tissue is approximately 6 V/m. Compare your answer from (c) to this threshold. What does this tell you about the design constraints on MRI gradient switching rates? *Tests: Faraday's law from dB/dt, working backward to find E from EMF, real-world safety implication.*

<!-- → [CHART: three-panel time-series for a bar magnet moving toward and then through a stationary coil — top panel: Φ_B(t) rising then falling as magnet passes; middle panel: ε(t) = −dΦ_B/dt showing positive peak as magnet approaches, zero at closest approach, negative peak as magnet recedes; bottom panel: I(t) = ε/R with same shape — the classic induction signature students should recognize before building the simulator] -->

---

## LLM Exercises

### Build the Faraday induction simulator (`10-faraday-induction.html`)

> **Show.** Faraday's law: $\varepsilon = -N\,d\Phi_B/dt$ where $\Phi_B$ is the magnetic flux through one turn of the coil. For a bar magnet modeled as a dipole with moment $m$, the axial field at distance $r$ is $B(r) = (\mu_0/4\pi)(2m/r^3)$. As the magnet moves toward or away from a stationary coil, $\Phi_B$ through the coil changes, and an EMF appears.
>
> **Say.** Build an interactive electromagnetic-induction simulator: a bar magnet moves along the axis of a stationary coil, and you display the flux, the induced EMF, and the induced current direction (Lenz) in real time.
>
> **Constrain.** D3 v7. Sliders: magnet speed (signed — positive toward coil, negative away), coil turns $N$ (10–500), coil area $A$ (0.001–0.05 m²), coil resistance $R$ (1–100 Ω). Render: a bar magnet (north red, south blue per `DESIGN.md`) moving along the horizontal axis of a stationary circular coil. Show static field-line approximation around the magnet. Compute $\Phi_B(t)$ via the dipole-axis formula at the current magnet–coil separation. Numerically differentiate to get $\varepsilon(t) = -N\,d\Phi_B/dt$ and $I(t) = \varepsilon/R$. Display three time-series panels (purple per `DESIGN.md`): $\Phi_B(t)$, $\varepsilon(t)$, $I(t)$. Add an animated arrow on the coil showing the induced-current direction predicted by Lenz, and an ammeter readout. Filename: `10-faraday-induction.html`.
>
> **Verify.** (a) Faster motion → larger EMF (peak EMF scales linearly with magnet speed when other parameters are fixed). (b) Reverse magnet direction → induced current reverses. (c) Doubling $N$ doubles the EMF at the same motion. (d) Doubling $A$ approximately doubles the EMF (only "approximately" because of the dipole's non-uniformity across the coil's area at small separations).

### Exploration

- Set $N = 100$, $A = 0.01$ m², $R = 10$ Ω. Move the magnet toward the coil at constant speed. Read off the peak induced current; confirm it scales linearly when you double the speed.
- Move the magnet *through* the coil (toward, then away). Confirm the induced current reverses sign at the moment the magnet is closest to the coil's center — that's when $d\Phi_B/dt$ changes sign.
- Increase $R$. Does the EMF change? Does the current? (EMF should be unaffected — it depends only on $d\Phi_B/dt$. Current scales as $1/R$.)
- Set the coil $N = 500$ turns and slowly bring the magnet up. Read the EMF at small displacements. Compare to the analytic prediction $\varepsilon = -N\,dB/dt \cdot A$ evaluated at the magnet–coil separation.

### Extension prompt (chapter bridge to Chapter 11)

> **Show.** Faraday's law says: a changing magnetic flux drives a circulation of $\vec{E}$. Schematically, **changing $\vec{B}$ creates $\vec{E}$**. Maxwell stared at the equations of electromagnetism in 1861 and asked the obvious symmetric question: does a changing $\vec{E}$ create $\vec{B}$? The un-augmented Ampère's law from Chapter 9 said no — only conduction currents create $\vec{B}$. Maxwell noticed this answer was inconsistent with charge conservation at a charging capacitor.
>
> **Say.** Modify the simulator to also show, in a side panel, the electric flux $\Phi_E$ through a horizontal disk between two capacitor plates that are being charged. Show $d\Phi_E/dt$ as a third time-series.
>
> **Constrain.** Two parallel circular plates, plate area $A_{\text{cap}}$, separation $d$, being charged at controllable rate $dQ/dt$. Compute $E = \sigma/\varepsilon_0$ between the plates (treat plates as infinite, ignore fringing). Compute $\Phi_E = EA_{\text{cap}}$ through a disk between the plates. Display $\Phi_E(t)$ and $d\Phi_E/dt$ alongside the $\Phi_B$, $\varepsilon$, and $I$ panels from the main simulator.
>
> **Verify.** While the capacitor is charging at constant $dQ/dt$, the displacement current $I_d = \varepsilon_0 \, d\Phi_E/dt$ should equal the conduction current $dQ/dt$ flowing in the wire. That is the bridge to Chapter 11.

Save as `10b-displacement-current-preview.html`. In Chapter 11 you will see that Maxwell's added "displacement-current" term — that $\varepsilon_0\,d\Phi_E/dt$ — closes Ampère's law against charge conservation, and that this completed pair of equations *predicts the existence of light* with speed $c = 1/\sqrt{\mu_0\varepsilon_0}$. Faraday says changing $\vec{B}$ makes $\vec{E}$. Maxwell adds: changing $\vec{E}$ makes $\vec{B}$. Together, they propagate.

---

**Tags:** Faraday's law, Lenz's law, electromagnetic induction, motional EMF, generator, transformer, self-inductance, RL circuit, eddy currents, magnetic energy density
