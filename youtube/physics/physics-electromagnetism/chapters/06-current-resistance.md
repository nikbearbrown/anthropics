# Chapter 6 — Electric Current and Resistance

*A statistical bias on thermal chaos, and the model that got the right answer for the wrong reason.*

---

You flip the switch on the wall. The bulb on the ceiling — six meters of wire away — lights up. As far as your eye can tell, it lights *instantly*.

Do the arithmetic. The current is about 0.5 A. The wire is copper, cross-section roughly 1 mm². The conduction-electron density in copper is $n = 8.5 \times 10^{28}$ per cubic meter. The drift velocity — the average speed at which an individual electron actually moves down the wire — is

$$v_d = \frac{I}{nqA} = \frac{0.5}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(10^{-6})} \approx 3.7 \times 10^{-5} \text{ m/s}.$$

Less than four hundredths of a millimeter per second. Slower than continental drift. An electron sitting next to the switch when you flipped it would take *days* to physically reach the filament.

Yet the bulb lit immediately. Whatever traveled from switch to bulb in the time you perceived as "instant" was not the electrons.

---

## The four speeds

The wire hosts four distinct speeds simultaneously, and mixing them up is the most common conceptual failure in this subject.

<!-- → [TABLE: four speeds in copper — rows: drift velocity (~10⁻⁴ m/s), thermal velocity (~10⁵ m/s at 300 K), Fermi velocity (~1.6 × 10⁶ m/s), signal speed (~2 × 10⁸ m/s) — columns: speed, magnitude, what sets it, what it means for current — to make the ten-order-of-magnitude span visible in one glance] -->

The **drift velocity** is what we calculated: $3.7 \times 10^{-5}$ m/s. This is the mean bias the applied field imposes on the electron cloud. It *is* the current — directly. But it is not how fast current "travels."

The **thermal velocity** — what electrons' speeds would be if they were a classical gas bouncing around at temperature $T$ — is around $10^5$ m/s at room temperature. Each electron is flying at roughly a hundred kilometers per second in some direction, colliding with the lattice in tens of femtoseconds, careening off in another direction. It has nothing to do with whether there is a current. Zero current means the electron cloud has zero *average* velocity, not zero speed.

The **Fermi velocity** — the actual speed of electrons at the top of the filled quantum states — is $v_F \approx 1.6 \times 10^6$ m/s in copper. This is quantum mechanics: the Pauli exclusion principle forces electrons into higher and higher energy states, so even at absolute zero they are moving. At room temperature this speed is essentially unchanged from its zero-temperature value, because $k_BT \ll E_F$. When people say "the mean free time is $\tau$," they mean the mean time between collisions for electrons moving at *this* speed.

The **signal speed** — the speed at which the rearrangement of the electromagnetic field propagates along the wire — is something like $2 \times 10^8$ m/s, set by the dielectric and geometric properties of the wire and its surroundings. This is what tells you when the bulb lights. In a six-meter wire, the field rearrangement reaches the filament in roughly thirty nanoseconds. The filament begins Joule heating because the electrons *already inside it* start drifting — not because any electron has traveled from the switch.

Ten orders of magnitude separate the drift velocity from the signal speed. When someone says electricity "travels at the speed of light," they mean the signal. When they say "the current is 1 ampere," they mean the drift. These are not the same thing, and they are not close to the same thing.

---

## What current actually is

**Current** is the rate at which charge crosses a fixed cross-section of a conductor:

$$I = \frac{dQ}{dt}$$

Units: amperes, where one ampere is one coulomb per second.

A word on the sign convention. Benjamin Franklin set the direction of "positive current flow" in the 1750s, long before anyone knew that the actual charge carriers in metals are electrons. He was wrong about which thing moves, but he had a fifty-fifty chance and the convention stuck. **Conventional current** points the direction positive charges would move; in a copper wire, that is opposite to the direction the electrons actually drift. The two descriptions are physically identical — an electron drifting left is electrically indistinguishable from a positive charge drifting right — and every equation works the same way regardless of which you use. The convention is bookkeeping, not physics.

![two-panel diagram — left: electrons drifting left in a wire with conventional current arrow pointing right, labeled "copper wire"; right: positive ions drifting right in a solution with conventional current arrow poin...](../images/06-current-resistance-fig-01.png)
*Figure 6.1 — Four Speeds in a Copper Wire*

<!-- → [IMAGE: two-panel diagram — left: electrons drifting left in a wire with conventional current arrow pointing right, labeled "copper wire"; right: positive ions drifting right in a solution with conventional current arrow pointing right, labeled "electrolyte" — showing that conventional current direction is the same in both cases regardless of carrier sign] -->

For a wire of cross-section $A$ carrying current $I$, the **current density** is $\mathbf{J} = I/A$ (amperes per square meter), pointing in the direction of positive charge flow. In terms of microscopic quantities:

$$\mathbf{J} = nq\mathbf{v}_d$$

where $n$ is the carrier density, $q$ is the charge per carrier, and $\mathbf{v}_d$ is the drift velocity. The current is the slow collective creep of a cloud whose individual members are, at every instant, almost all moving somewhere else entirely.

---

## The Drude model

In 1900, three years after Thomson identified the electron and a quarter-century before quantum mechanics, Paul Drude proposed a microscopic model of conduction. The picture is unapologetically classical: each atom contributes a free electron to a gas filling the metal; between collisions an electron moves in a straight line, accelerated by any applied field; each collision randomizes its velocity back to a thermal distribution; the mean time between collisions is $\tau$. From these four assumptions the whole macroscopic theory of conductivity drops out.

![cartoon of the Drude model — an electron (dot) accelerating rightward under a field E between two collision events, then having its velocity randomized by a collision (zigzag change of direction), then accelerating ag...](../images/06-current-resistance-fig-02.png)
*Figure 6.2 — Resistivity from Silver to Fused Quartz*

<!-- → [IMAGE: cartoon of the Drude model — an electron (dot) accelerating rightward under a field E between two collision events, then having its velocity randomized by a collision (zigzag change of direction), then accelerating again — the drift is the small net rightward bias accumulated between each pair of collisions] -->

**Getting the drift velocity.** Between collisions, Newton's law for an electron in a field $\mathbf{E}$:

$$m\frac{d\mathbf{v}}{dt} = -e\mathbf{E}$$

A collision randomizes the velocity, so on average each electron starts each free flight with zero net drift. After a time $\tau$ (the mean time before the next collision), it has built up:

$$\Delta\mathbf{v} = -\frac{e\mathbf{E}}{m}\tau$$

The drift velocity is this mean accumulated kick:

$$\mathbf{v}_d = -\frac{e\tau}{m}\mathbf{E}$$

**Getting the current density.** Plug into $\mathbf{J} = nq\mathbf{v}_d$. For electrons, the two sign flips (charge $-e$ and drift opposite to $\mathbf{E}$) cancel, giving:

$$\mathbf{J} = \frac{ne^2\tau}{m}\mathbf{E} \equiv \sigma\mathbf{E}$$

The proportionality constant is the **conductivity**:

$$\boxed{\;\sigma = \frac{ne^2\tau}{m}\;}$$

**Getting Ohm's law.** For a uniform wire of length $L$ and cross-section $A$ with potential difference $V$ across its ends, the field inside is $E = V/L$ (Chapter 4). The total current is $I = JA = \sigma E A = \sigma V A/L$. Rearranging:

$$V = I \cdot \frac{L}{\sigma A} = I \cdot \frac{\rho L}{A} \equiv IR$$

with **resistivity** $\rho = 1/\sigma$ and:

$$\boxed{\;R = \frac{\rho L}{A}\;}$$

Ohm's law, derived from a microscopic model rather than postulated. Resistance is a geometric property of the wire ($L/A$) multiplied by a material property ($\rho$), and $\rho$ connects directly to how many free carriers there are and how long they fly between collisions.

---

## What the derivation actually rests on

Look carefully at what we just did. The derivation required three assumptions that are each separately true under limited conditions:

**First: the carrier density $n$ is fixed.** In a metal at ordinary temperatures, this is excellent — the number of conduction electrons per atom is set by the band structure and doesn't change with modest applied fields or temperature.

**Second: the mean free time $\tau$ doesn't depend on the applied field.** This requires that the energy an electron gains from the field between collisions, $eE\lambda$, is negligible compared to its thermal energy $k_BT$. For household fields across copper wire, that energy ratio is about $10^{-9}$ — the field is a negligible perturbation. At enormous fields (near dielectric breakdown), this fails.

**Third: the drift velocity is linear in the field.** This follows from the second assumption. If $\tau$ is field-independent, $v_d = (e\tau/m)E$ is strictly linear.

When all three hold, the material is **ohmic** — $V \propto I$ exactly, and plotting $V$ against $I$ gives a straight line through the origin. When any one fails, you have a **non-ohmic** device, and $V = IR$ is wrong.

Semiconductors fail the first assumption. Temperature excites electrons across a band gap, so $n$ rises exponentially with $T$. A semiconductor gets *more* conductive as it heats up — opposite to a metal. The thermistor, the transistor, and the solar cell all live in this failure mode.

A tungsten filament fails the second assumption in practice. The filament runs at roughly 2,800 K in operation. Heating tightens up the lattice vibrations and shortens $\tau$, raising the resistance tenfold between cold and hot. An old incandescent bulb most often fails at the moment of switch-on, not during steady operation — because that's when the cold, low-resistance filament draws maximum inrush current, which is the highest stress the filament ever sees.

A diode fails the first assumption geometrically — a p-n junction has asymmetric carrier densities on its two sides, and the potential hill between them lets current flood easily in one direction and trickle in the other.

This is the chapter's central intellectual honesty: Ohm's law is not a law of nature in the way Coulomb's law is. It is a consequence of three reasonable approximations that happen to hold simultaneously over a wide range of conditions for most metals. The mature position is to know *why* it works when it works, and exactly *where* it stops.

![three-column decision tree — column 1: "Is n fixed?" YES → ohmic candidate, NO → semiconductor/diode; column 2: "Is τ field-independent?" YES → continue, NO → breakdown regime; column 3: "Is v_d linear in E?" YES → Oh...](../images/06-current-resistance-fig-03.png)
*Figure 6.3 — Drift Velocity*

<!-- → [INFOGRAPHIC: three-column decision tree — column 1: "Is n fixed?" YES → ohmic candidate, NO → semiconductor/diode; column 2: "Is τ field-independent?" YES → continue, NO → breakdown regime; column 3: "Is v_d linear in E?" YES → Ohm's law holds, NO → non-linear response — shows which Drude assumption fails for each non-ohmic device] -->

---

## Resistivity: twenty-six orders of magnitude

The formula $\rho = m/(ne^2\tau)$ gives a number you can look up in a table. Here is a slice of what those tables say:

<!-- → [TABLE: resistivity values — rows: silver (1.59 × 10⁻⁸ Ω·m), copper (1.68 × 10⁻⁸), aluminum (2.65 × 10⁻⁸), tungsten (5.60 × 10⁻⁸), nichrome (1.10 × 10⁻⁶), pure silicon (~640), fused quartz (~7.5 × 10¹⁷) — columns: material, ρ (Ω·m), notes on why it's interesting — to show the 26-order-of-magnitude range in one table] -->

Twenty-six orders of magnitude from silver to fused quartz. There is no smooth interpolation across that range. Metals and insulators are qualitatively different states of matter, separated by a band gap. What makes silicon astonishing is that you can move it six orders of magnitude in resistivity by adding impurity atoms at parts-per-billion concentrations — doping shifts the Fermi level into an energy range where carriers exist, and $n$ changes by factors of millions. Every transistor on every chip is made from silicon whose resistivity has been tuned by doping.

---

## What's actually doing the scattering

Drude said electrons collide with ion cores. Quantum mechanics says that's wrong — and illuminatingly wrong.

In a *perfectly periodic* lattice, electrons propagate as Bloch waves with *infinite* mean free path. The lattice doesn't scatter them at all. Only *departures from periodicity* do: lattice vibrations (phonons), substitutional impurities, vacancies, grain boundaries. At room temperature in pure copper, phonon scattering dominates and the mean free path is about 40 nm — roughly 150 lattice spacings. Cooling a pure metal toward absolute zero reduces phonon scattering dramatically, and the residual resistance comes almost entirely from defects.

![resistivity vs. temperature for copper — showing the linear rise above the Debye temperature (phonon scattering) and the flat residual resistivity floor at low temperature (defect scattering) — the Matthiessen's rule...](../images/06-current-resistance-fig-04.png)
*Figure 6.4 — Drude Model*

<!-- → [CHART: resistivity vs. temperature for copper — showing the linear rise above the Debye temperature (phonon scattering) and the flat residual resistivity floor at low temperature (defect scattering) — the Matthiessen's rule picture: ρ(T) = ρ_defects + ρ_phonon(T)] -->

The linear-$T$ resistivity of metals above their Debye temperature, the residual resistance at low $T$, and the $T^2$ electron-electron term at very low temperatures all follow from quantum treatments. Drude's billiard-ball model gives the right formula $\sigma = ne^2\tau/m$ with the wrong mechanism for $\tau$. It happened to survive the Sommerfeld quantum correction intact — with $\tau$ reinterpreted as the relaxation time at the Fermi surface rather than the classical mean collision time. The two definitions agree numerically for free-electron-like metals, which is why Drude's 1900 formula is still in every textbook.

That a classical model gave the right answer for the wrong reason for twenty-eight years, and that fixing it with quantum mechanics gave nearly the same formula — this is one of the better jokes physics has ever played on its practitioners.

---

## Resistance depends on temperature

For most metals near room temperature, resistance increases roughly linearly with temperature:

$$R(T) = R_0\left[1 + \alpha(T - T_0)\right]$$

where $\alpha$ is the **temperature coefficient of resistance**. Copper: $\alpha \approx 4.0 \times 10^{-3}$ /K. Tungsten: $\alpha \approx 4.5 \times 10^{-3}$ /K. Nichrome (the alloy used in heating elements and toasters): $\alpha \approx 4 \times 10^{-4}$ /K — ten times smaller, because alloy disorder already dominates over phonons, making the resistance relatively insensitive to further temperature changes. That's exactly why nichrome makes good precision resistors and stable heating elements.

For semiconductors, $\alpha$ is *negative* — resistance *falls* with rising temperature, as thermal energy kicks more carriers across the gap. Pure silicon has $\alpha \approx -0.07$ /K, twenty times the magnitude of copper's coefficient and opposite in sign. This is the thermistor.

---

## Power and the cost of driving current

When charge $dQ$ moves across a potential difference $V$, the work done is $V\,dQ$. The power delivered is:

$$P = V\frac{dQ}{dt} = IV$$

For an ohmic resistor, $V = IR$, so the same power can be written three ways:

$$\boxed{\;P = IV = I^2R = \frac{V^2}{R}\;}$$

All three are correct. Pick the form that matches what you know. If you know the voltage source and the resistance, use $V^2/R$. If you know the current through the resistor, use $I^2R$.

The microscopic picture is worth holding: each electron accelerates under the field, picking up kinetic energy between collisions. At each collision it dumps that energy into the lattice — a lattice vibration, which is heat. The process is called **Joule heating**: ordered drift energy converted to disordered thermal motion, one collision at a time. Every electrical device that warms up in operation is doing this. The $I^2R$ formula is not an approximation; it is the exact account of where the electrical energy goes.

![microscopic Joule heating diagram — electron accelerating rightward under E, gaining kinetic energy (shown as speed), then colliding with a lattice site and emitting a phonon (shown as a vibrating lattice wave) — the...](../images/06-current-resistance-fig-05.png)
*Figure 6.5 — Ohm's Law Is Not Fundamental*

<!-- → [IMAGE: microscopic Joule heating diagram — electron accelerating rightward under E, gaining kinetic energy (shown as speed), then colliding with a lattice site and emitting a phonon (shown as a vibrating lattice wave) — the ordered-to-disordered energy conversion made visual] -->

One practical warning about the three forms. For an ohmic resistor at fixed resistance $R$, doubling the voltage doubles the current, so the power goes as $V^2/R$ — it *quadruples*. A resistor rated for 0.25 W handles 5 V easily; double the voltage to 10 V and you are delivering four times the power. That is often above the part's rating, and the result is smoke. Students who reach for $P = IV$ and treat $V$ and $I$ as independent — not connected by Ohm's law — make this mistake.

---

## The battery's role: electromotive force

Ohm's law tells you how energy is dissipated. Something has to supply that energy. In a circuit, it's the battery (or generator, or solar cell — any **EMF source**).

A real battery is not an ideal voltage source. It has an **electromotive force** $\varepsilon$ — the open-circuit voltage set by its chemistry — and an **internal resistance** $r$ set by ion mobility in the electrolyte. Loaded with external resistance $R$:

$$\varepsilon = I(R + r), \qquad V_{\text{terminal}} = \varepsilon - Ir$$

A fresh AA alkaline has $\varepsilon \approx 1.5$ V and $r \approx 0.2$ Ω. As it discharges, $r$ rises — reaction products clog the ion paths — and the terminal voltage sags under load. A "dead" battery often measures 1.4 V with a voltmeter (nearly nothing connected, drawing negligible current) but fails to light a flashlight bulb (which needs current, which means $Ir$ drops subtract from the terminal voltage). The battery is not dead because the chemistry is exhausted; it's dead because the internal resistance has risen enough that the terminal voltage collapses under any real load.

From Chapter 4: in a static field, $\oint \vec{E}\cdot d\vec{\ell} = 0$ around any closed loop — no net work done going around a loop. That means no steady current can flow in a purely conservative field. The battery provides a *non-conservative* push — a chemical force on the charges inside it — that maintains a potential difference against the dissipation. The battery converts chemical energy to electrical energy; the resistor converts electrical energy to heat. The loop closes. Chapter 7 will use these ideas inside Kirchhoff's laws.

![energy flow diagram for a simple circuit — battery labeled with ε and r showing chemical energy → electrical energy, wire showing small I²r loss, resistor showing I²R → heat, with arrows tracing the energy path around...](../images/06-current-resistance-fig-06.png)
*Figure 6.6 — Superconductivity Timeline*

<!-- → [IMAGE: energy flow diagram for a simple circuit — battery labeled with ε and r showing chemical energy → electrical energy, wire showing small I²r loss, resistor showing I²R → heat, with arrows tracing the energy path around the loop and labels for each conversion — makes the energy accounting concrete before Kirchhoff] -->

---

## Superconductivity: the limit $R = 0$

Everything above assumes the resistance is nonzero. In April 1911, Heike Kamerlingh Onnes — who had been the first person to liquefy helium three years earlier — cooled mercury through 4.2 K and watched its resistance fall not to some small value but to *unmeasurably zero*. His lab notebook for 8 April 1911 reads: *"Kwik nagenoeg nul"* — "Mercury nearly zero."

Below a **critical temperature** $T_c$, the resistance is not small but exactly zero. A current set up in a superconducting loop persists for years without measurable decay. The phenomenon went unexplained for forty-six years. In 1957, Bardeen, Cooper, and Schrieffer published the microscopic theory. The mechanism, counterintuitively, requires electrons to *attract* each other — mediated by a slight distortion of the lattice around one electron that draws another toward it. Bound pairs ("Cooper pairs") are bosons; they condense into a single coherent quantum state that carries current without scattering, because scattering would have to scatter the *entire* condensate, not a single electron.

![conceptual diagram of Cooper pair formation — one electron moving right slightly deforms the positive ion lattice, creating a local positive charge density; a second electron is drawn toward this density — the indirec...](../images/06-current-resistance-fig-07.png)
*Figure 6.7 — Joule Heating*

<!-- → [IMAGE: conceptual diagram of Cooper pair formation — one electron moving right slightly deforms the positive ion lattice, creating a local positive charge density; a second electron is drawn toward this density — the indirect attraction mediated by the lattice that binds the pair] -->

In 1986, Bednorz and Müller found superconductivity at 35 K in a copper-oxide ceramic — far above the previous record. The 1987 Nobel Prize followed the next year, the shortest such lag in physics history. Within months, researchers synthesized YBa₂Cu₃O₇ with $T_c \approx 92$ K — the first material superconducting above the boiling point of liquid nitrogen (77 K). Liquid nitrogen is cheap. The engineering economics changed overnight.

The mechanism in these cuprate materials remains, as of 2026, *unsettled*. BCS does not predict $T_c$ this high; the leading hypothesis involves spin fluctuations in the copper-oxide planes, but no quantitative microscopic theory has emerged in forty years. In July 2023 a Korean group published a preprint claiming room-temperature ambient-pressure superconductivity in copper-doped lead apatite ("LK-99"). Replication attempts worldwide traced the anomalies, within weeks, to a Cu₂S impurity phase transition near 385 K. High-pressure hydrogen-rich compounds achieve $T_c$ near 250 K — but only under diamond-anvil pressures of 170 GPa, which is not useful engineering.

The point: the resistance you measure in a metal at room temperature is not inevitable. Cool the right material enough, and it vanishes. The right material, at room temperature and atmospheric pressure, has not yet been found. Whether it exists is an open empirical question.

---

## The worked numbers: how it all connects

A copper wire, $L = 10$ m, diameter 1 mm, carrying $I = 1$ A.

Cross-section: $A = \pi(0.5 \times 10^{-3})^2 = 7.85 \times 10^{-7}$ m².

Resistance: $R = \rho L/A = (1.68 \times 10^{-8})(10)/(7.85 \times 10^{-7}) = 0.214$ Ω.

Voltage drop: $V = IR = 0.214$ V. Field inside: $E = V/L = 0.021$ V/m — about two hundredths of a volt per meter, which is what it costs to push 1 A through copper of this gauge.

Drift velocity: $v_d = I/(nqA) = 1/[(8.5 \times 10^{28})(1.6 \times 10^{-19})(7.85 \times 10^{-7})] \approx 9.4 \times 10^{-5}$ m/s. Roughly 0.1 mm/s.

Power dissipated: $P = I^2R = 0.214$ W — about a fifth of a watt of heat distributed over 10 m of wire.

Mean free time: inverting $\sigma = ne^2\tau/m$ with $\sigma = 5.95 \times 10^7$ S/m:

$$\tau = \frac{m\sigma}{ne^2} = \frac{(9.11 \times 10^{-31})(5.95 \times 10^7)}{(8.5 \times 10^{28})(1.6 \times 10^{-19})^2} \approx 2.5 \times 10^{-14} \text{ s}$$

Twenty-five femtoseconds. At the Fermi velocity $v_F \approx 1.6 \times 10^6$ m/s, the mean free path is $\lambda = v_F\tau \approx 40$ nm — about 150 lattice spacings, in good agreement with direct measurements on thin copper films.

The lesson from these numbers is the connection. Three macroscopic quantities — $R$, $V$, $P$ — all trace back to one microscopic number, $\tau$, combined with $n$ and geometry. The Drude formula $\sigma = ne^2\tau/m$ is a single relation doing all the connecting work. When it holds, everything is consistent. When it fails, the specific way it fails tells you which of the three approximations broke first.

---

## One misconception I want to name directly

The most persistent failure mode in intro circuits — documented repeatedly in the physics education literature — is the belief that current is "used up" by a resistor. Students draw a circuit with an ammeter on each side of a resistor and expect the downstream reading to be smaller.

Charge is conserved at every node. The current that enters a resistor exits the same resistor. What a resistor consumes is not charge — it is *energy*. Power $I^2R$ is converted to heat. The current, the rate of charge flow, is identical on both sides. Kirchhoff's current law in Chapter 7 is the formalization of this, but it is really just charge conservation with no place for charge to accumulate.

The confusion persists partly because "uses up" is how batteries are described in everyday life — and batteries do get depleted. But it's the *energy* that depletes, stored in chemical form, converted to electrical form, then dissipated as heat. The charge returns to the battery through the external circuit and is recycled.

---

## Exercises

**Warm-up.** State the four speeds of electricity in a copper wire in order of magnitude. For each, write one sentence explaining what physical phenomenon sets that speed. Then answer: which speed *is* the current? Which speed determines when the bulb lights up when you flip a switch? *Tests: conceptual map of the chapter's opening section.*

**Warm-up.** A 14-gauge copper wire has cross-section $A = 2.08 \times 10^{-6}$ m² and carries $I = 10$ A — a typical household branch-circuit load. Using $n = 8.5 \times 10^{28}$ /m³ and $q = 1.6 \times 10^{-19}$ C, compute the drift velocity. Express it in mm/s. A garden snail moves at roughly 1 mm/s. How does the drift compare? How long would a single electron take to travel 5 m from a breaker box to a kitchen outlet at this drift? *Tests: drift velocity formula, unit fluency, building intuition for the number's smallness.*

**Warm-up.** A copper wire has length $L = 25$ m, diameter $d = 1.5$ mm, and carries current $I = 5$ A. Compute (a) the cross-sectional area $A$, (b) the resistance $R = \rho L/A$ using $\rho = 1.68 \times 10^{-8}$ Ω·m, (c) the voltage drop $V = IR$, (d) the power dissipated as heat $P = I^2R$. *Tests: mechanical application of the geometry formula, units, the three power expressions.*

**Application.** A 100 Ω resistor has 5 V across it. Compute the power three ways: $P = IV$, $P = I^2R$, $P = V^2/R$. Verify all three agree. Now double the voltage to 10 V. By what factor does the power increase — and why is it not a factor of 2? *Tests: equivalence of the three forms, the quadratic dependence on voltage at fixed R.*

**Application.** A 60 W incandescent bulb runs at 120 V in steady state. Its tungsten filament operates at approximately 2,800 K, about 2,780 K above room temperature. Using $\alpha_W = 4.5 \times 10^{-3}$ /K: (a) estimate $R_\text{hot}/R_\text{cold}$ from the linear formula $R(T) = R_0[1 + \alpha \Delta T]$; (b) compute $R_\text{cold}$ and the instantaneous inrush current at switch-on; (c) explain, using this number, why old filament bulbs most often fail *at the moment of turn-on* rather than during steady operation. *Tests: temperature coefficient of resistance, connecting R(T) to real failure mode.*

**Application.** A power line has total resistance $R_\text{line} = 10$ Ω and must deliver $P_\text{load} = 1$ GW over 200 km. Compute the fractional power lost as $I^2R$ heating in the line at transmission voltages of (a) 110 kV, (b) 345 kV, (c) 765 kV. Argue from your results why high-voltage transmission is a physical necessity, not a design preference. *Tests: power and current at different voltages, I²R losses, engineering consequence of the quadratic.*

**Synthesis.** Starting from $\mathbf{F} = -e\mathbf{E}$ on a free electron with mean free time $\tau$ between velocity-randomizing collisions, derive in sequence: (a) drift velocity $v_d = e\tau E/m$; (b) current density $J = (ne^2\tau/m)E$; (c) conductivity $\sigma = ne^2\tau/m$ and resistivity $\rho = m/(ne^2\tau)$; (d) Ohm's law $V = IR$ with $R = \rho L/A$ for a uniform wire. Then plug in $n = 8.5 \times 10^{28}$ /m³ and $\tau = 2.5 \times 10^{-14}$ s and verify $\rho \approx 1.7 \times 10^{-8}$ Ω·m. Name the three approximations the derivation requires. *Tests: full Drude derivation chain, connecting micro to macro, explicit identification of where Ohm's law can fail.*

**Synthesis.** The Drude model predicts $\sigma = ne^2\tau/m$. In a real metal, phonon scattering gives $\tau \propto 1/T$ above the Debye temperature, while impurity scattering gives a temperature-independent $\tau_\text{imp}$. Matthiessen's rule adds the scattering rates: $1/\tau = 1/\tau_\text{phonon} + 1/\tau_\text{imp}$. (a) Show that this gives $\rho(T) = \rho_\text{imp} + \rho_\text{phonon}(T)$ with $\rho_\text{phonon} \propto T$. (b) Sketch $\rho(T)$ from near 0 K to 300 K for a pure metal and for a metal with impurities. (c) What does the low-temperature floor of the curve tell you that a room-temperature measurement alone cannot? *Tests: connecting Drude to quantum scattering picture, Matthiessen's rule, reading information from a $\rho$-vs-$T$ plot.*

**Challenge.** An ideal battery of EMF $\varepsilon$ and internal resistance $r$ drives current through an external resistor $R$. (a) Show that the power delivered to the external resistor is $P_R = \varepsilon^2 R/(R+r)^2$. (b) Find the value of $R$ that maximizes $P_R$ — this is the **maximum power transfer theorem**. (c) At that optimal $R$, what fraction of the total power from the EMF is delivered to the load versus lost in internal resistance? (d) A car battery has $\varepsilon = 12$ V and $r = 0.05$ Ω. The starter motor draws 150 A. Compute the terminal voltage during cranking and the power lost in the battery's internal resistance. Why does the dashboard dim when you start the car? *Tests: EMF and internal resistance, optimization by calculus, real-world consequence of internal resistance.*

<!-- → [CHART: I-V curves for three devices on the same axes — a linear (ohmic) resistor, a tungsten filament (resistance rising with temperature, so current increases sub-linearly with V), and a diode (near-zero current for negative V, exponential rise for forward bias) — student should see which device obeys which Drude assumption and where each line departs from ohmic] -->

---

## LLM Exercises

### Build the drift-velocity simulator (`06-drift-velocity.html`)

> **Show.** Current in a metal as a statistical bias on thermal chaos. Each conduction electron does random thermal hopping; an applied field $\mathbf{E}$ adds a small steady drift. The average drift velocity is $v_d = (e\tau/m)E$; the resulting current is $I = nqv_dA$. Power dissipated is $P = I^2R$.
>
> **Say.** Build an interactive drift-velocity visualizer. Show ~50 conduction electrons inside a wire cross-section box. Each electron has thermal motion (random direction kicks every collision) plus a slow drift along the wire when a field is applied. Display $v_d$, $I$, $P$, and the centroid of the electron cloud live as the user changes the applied voltage.
>
> **Constrain.** D3 v7. A rectangular "wire" canvas, periodic boundary conditions (electrons exiting the right edge re-enter on the left). 50 dots, each with $\vec{v} = \vec{v}_{\text{thermal}} + \vec{v}_{\text{drift}}$. Thermal-speed magnitude set to $10\times$ the maximum drift speed for visual clarity (label this — the real ratio is $10^{10}$, unanimatable). At each timestep, a random subset of dots "collide" (resampling thermal direction). Slider for applied voltage $V$ (0–10 V across a 10 cm imagined wire); compute $E = V/L$ and $v_d = (e\tau/m)E$ using $\tau = 2.5 \times 10^{-14}$ s. Live readouts: $v_d$ (mm/s), $I$ ($n_{\text{Cu}} = 8.5 \times 10^{28}$ /m³, 1 mm² imagined cross-section), $P = I^2R$ with $R = 0.21$ Ω. A "trail" toggle showing each electron's recent path. A temperature-scaling slider that changes visible chaos but does not change $v_d$. A "field off" button. Filename: `06-drift-velocity.html`.
>
> **Verify.** (a) $V = 0$: cloud centroid stationary; $v_d = I = 0$; dots bounce randomly. (b) $V > 0$: centroid drifts steadily; $v_d$ readout on the order of $10^{-4}$ m/s. (c) Doubling $V$ doubles $v_d$ and $I$, quadruples $P$. (d) Raising the temperature slider increases visible chaos but does *not* change $v_d$ at fixed $V$ — drift is a bias, not a separate motion. (e) The drift is visibly small compared to thermal motion; the eye sees chaos and the centroid display makes the drift quantitatively visible.

### Exploration

- Run with $V = 1$ V. Read off $v_d$ and compare to your hand calculation using $v_d = (e\tau/m)(V/L)$.
- Cut the temperature slider in half. Does $v_d$ change? Does $I$ change? Why or why not? (The simulator's $\tau$ is set independent of $T$; in real metals, $\tau$ shortens with rising $T$ as phonon density grows.)
- Set $V = 10$ V (well into the regime where a real copper wire of this length would smoke). Read $P$. The simulator keeps doing Drude algebra; it doesn't know about thermal limits.
- Turn the field off. The cloud centroid stays put even though every dot is moving fast — "zero current in equilibrium" is many fast carriers with no net flow.
- Turn the field back on and watch a single tagged electron. Its path is dominated by random thermal hops, with a tiny drift bias on top. Average over many electrons (or many timesteps) to see the bias clearly.

### Extension prompt (chapter bridge)

> **Show.** I've watched current as a drift bias on chaos. Now I want to set up real circuits with multiple resistors and batteries, and solve for the currents and voltages systematically.
>
> **Say.** Modify or build a new simulator: a small DC circuit with two batteries and three resistors arranged in a two-loop topology. Solve for the branch currents using Kirchhoff's laws (KCL at nodes, KVL around loops) or equivalently nodal analysis.
>
> **Constrain.** D3 v7 schematic. Sliders for $\varepsilon_1, \varepsilon_2, R_1, R_2, R_3$. Solve the linear system automatically as the sliders move. Display branch currents as animated orange arrows (length proportional to $|I|$, direction set by sign). Display node voltages as labels. Live readout of total power dissipated and power delivered by each source.
>
> **Verify.** With $\varepsilon_1 = 12$ V, $\varepsilon_2 = 8$ V, $R_1 = 4$ Ω, $R_2 = 6$ Ω, $R_3 = 3$ Ω, the top-node voltage should come out around 5.78 V; check by writing KCL at that node by hand and comparing. KCL at every node should be satisfied to numerical precision.

Save as `06b-circuit-preview.html`. This is the lead-in to Chapter 7.

---

**Tags:** electric current, drift velocity, Drude model, Ohm's law, resistivity, conductivity, Joule heating, superconductivity
