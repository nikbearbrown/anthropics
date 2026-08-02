# Chapter 6 — Electric Current and Resistance

*A statistical bias on thermal chaos, and the model that got the right answer for the wrong reason.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Define **current** $I = dQ/dt$ and **current density** $\mathbf{J} = nq\mathbf{v}_d$, and distinguish conventional current from electron flow.
2. **(Apply)** Compute **drift velocity** for a metal wire from $v_d = I/(nqA)$ and recognize it is ~mm/s — orders of magnitude below thermal, Fermi, and signal speeds.
3. **(Apply)** Derive Ohm's law $V = IR$ from the **Drude model** — free electron gas plus lattice collisions — and identify the three approximations on which the derivation rests.
4. **(Apply)** Use $R = \rho L/A$ to compute resistance from material **resistivity** and geometry; convert between $\rho$ and **conductivity** $\sigma = 1/\rho$.
5. **(Analyze)** Distinguish ohmic from non-ohmic materials and explain *which* of the three Drude approximations fails in each non-ohmic case.
6. **(Apply)** Compute power dissipation three ways — $P = IV = I^2R = V^2/R$ — and recognize **Joule heating** as ordered drift energy thermalized one collision at a time.
7. **(Apply)** Build a drift-velocity simulator that makes the statistical-bias picture of current visible against thermal chaos.

---

## Opening case: the four speeds of electricity

You flip the switch on the wall. The bulb on the ceiling — six meters of wire away — lights up. As far as your eye can tell, it lights *instantly*.

Do the arithmetic. The current is about 0.5 A. The wire is copper, cross-section roughly 1 mm². The conduction-electron density in copper is $n = 8.5 \times 10^{28}$ per cubic meter ([Ashcroft & Mermin, *Solid State Physics* (1976), Ch. 1](https://www.cengage.com/c/solid-state-physics-1e-ashcroft-mermin/9780030839931/)). The drift velocity — the average speed at which an individual electron actually moves down the wire — is

$$v_d = \frac{I}{nqA} = \frac{0.5}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(10^{-6})} \approx 3.7 \times 10^{-5} \text{ m/s}.$$

Less than four hundredths of a millimeter per second. Slower than continental drift. An electron that was sitting next to the switch when you flipped it would take *days* to physically arrive at the bulb's filament.

Yet the bulb lit immediately. Whatever traveled from switch to bulb in the time you perceived as "instant" was not the electrons. The electrons were already everywhere along the wire — including inside the filament — when you flipped the switch. What traveled was the *signal* — the rearrangement of the electric field guided by the wire's surface and dielectric environment — propagating at something like $2 \times 10^8$ m/s. In a six-meter wire, that's about 30 nanoseconds. The bulb lights because the electrons *already inside the filament* begin drifting (and scattering, and dissipating energy) the moment the field arrives.

Three speeds in play. The wire hosts a fourth.

| Speed | Magnitude in Cu | What it is |
|---|---|---|
| Drift velocity $v_d$ | $\sim 10^{-4}$ m/s | The bias on thermal motion set by the applied field. *This is the current.* |
| Thermal velocity | $\sim 10^5$ m/s at 300 K | What electrons' speeds *would* be if they were a classical gas. |
| Fermi velocity $v_F$ | $\sim 1.6 \times 10^6$ m/s | The actual speed of electrons at the top of the filled states. Quantum, T-independent. |
| Signal speed | $\sim 2 \times 10^8$ m/s | Rearrangement of the EM field guided by the wire. Sets when the bulb lights. |

Ten orders of magnitude span those four numbers. Mixing them up is the most common conceptual failure in this material. The rest of the chapter is consequences: where resistance comes from, why Ohm's law works, and what it costs in dissipated heat to push current through a wire.

---

## Core concept

### Current: rate of charge flow

Electric **current** is the time rate at which charge crosses a fixed cross-section of a conductor:

$$I = \frac{dQ}{dt}.$$

Units: ampere (A) = coulomb per second. For steady DC, $I = Q/t$ collapses to the familiar form; for time-varying signals, only the derivative form is honest.

**Conventional current** points the direction *positive* charges would move — out of the + terminal of a battery, through the external circuit, back to the − terminal. Franklin set this convention in the 1750s, decades before anyone knew electrons were the carriers in metals. So in a copper wire, the *electrons* drift from − to +, and the *conventional current* points from + to −. The two are identical in physical effect: an electron moving left is electrically indistinguishable from a positive charge moving right. The convention is bookkeeping — it lets every equation look the same regardless of who the actual carriers are (electrons in metals, ions in solutions, holes in p-type semiconductors).

### Current density and drift velocity

For a wire of cross-section $A$ carrying current $I$, the **current density** is $J = I/A$ (units A/m²). As a vector, $\mathbf{J}$ points in the direction positive charge flows.

In terms of carriers:

$$\mathbf{J} = nq\mathbf{v}_d$$

where $n$ is the carrier number density (per m³), $q$ is the charge per carrier (signed), and $\mathbf{v}_d$ is the **drift velocity** — the average velocity of the carrier population. For electrons with $q = -e$, $\mathbf{J}$ points opposite to $\mathbf{v}_d$. The conventional current and the electron drift point opposite ways, as required.

The drift velocity is *not* a separate motion. It is the small mean bias on top of the much faster random thermal motion. In a metal with no applied field, every electron is bouncing at the Fermi velocity in some direction; collectively their mean velocity is zero. Apply a field $\mathbf{E}$ along the wire, and each electron feels a small steady force $\mathbf{F} = -e\mathbf{E}$ between collisions, picking up a sliver of velocity in that direction before its next collision wipes its memory. Average that sliver over the whole population and you get $\mathbf{v}_d$. The current is the slow collective creep of a cloud whose individual members are, at any given instant, almost all moving in some other direction. This is what the simulator at the end of the chapter makes visible.

### The Drude model — and the derivation of Ohm's law

Paul Drude proposed his model in 1900, three years after Thomson identified the electron and a quarter-century before anyone had quantum mechanics ([Drude, *Annalen der Physik* **306**, 566 (1900)](https://onlinelibrary.wiley.com/doi/10.1002/andp.19003060312)). The picture is unapologetically classical: each atom contributes a free electron to a gas filling the metal; between collisions an electron moves in a straight line, accelerated by any applied field; each collision (with an ion core, in Drude's original picture) randomizes the velocity to a thermal distribution; the mean time between collisions is $\tau$, the **mean free time**. From these four assumptions the whole macroscopic theory of conductivity falls out.

**Step one: drift velocity.** Between collisions, Newton's second law for an electron in a field $\mathbf{E}$ is

$$m\frac{d\mathbf{v}}{dt} = -e\mathbf{E}.$$

A collision randomizes $\mathbf{v}$, so on average each electron starts each free flight with zero net velocity along $\mathbf{E}$. After a time $\tau$ (the average time before its next collision), it has built up

$$\Delta\mathbf{v} = -\frac{e\mathbf{E}}{m}\tau.$$

The drift velocity is this average post-collision gain:

$$\mathbf{v}_d = -\frac{e\tau}{m}\mathbf{E}.$$

(The minus sign is because electrons are negative; the drift is opposite to $\mathbf{E}$. For a generic carrier of charge $q$, $\mathbf{v}_d = (q\tau/m)\mathbf{E}$.)

**Step two: current density.** Plug the drift velocity into $\mathbf{J} = nq\mathbf{v}_d$. For electrons, with two sign flips that cancel,

$$\mathbf{J} = \frac{ne^2\tau}{m}\mathbf{E} \equiv \sigma\mathbf{E}.$$

The proportionality constant is the **conductivity**:

$$\boxed{\;\sigma = \frac{ne^2\tau}{m}\;}$$

This is the **microscopic form of Ohm's law**. Current density is proportional to applied field, with a constant determined entirely by how many carriers there are, how long they fly between collisions, and how heavy they are. **Resistivity** is the reciprocal: $\rho = 1/\sigma = m/(ne^2\tau)$.

**Step three: the macroscopic law.** For a uniform wire of length $L$ and cross-section $A$ with potential difference $V$ across its ends, the field inside is $E = V/L$ (Chapter 4: uniform potential gradient). The total current is $I = JA = \sigma E A = \sigma V A / L$. Rearranging:

$$V = I \cdot \frac{L}{\sigma A} = I \cdot \frac{\rho L}{A} \equiv IR$$

with

$$\boxed{\;R = \frac{\rho L}{A}\;}$$

That is Ohm's law, **derived** rather than postulated. Resistance is a *geometric* property of a wire ($L/A$) times a *material* property of what it's made of ($\rho$), and $\rho$ in turn comes from microscopic carrier dynamics.

Look at what the derivation rests on. **Three approximations**, each separately falsifiable: (1) carrier density $n$ is fixed; (2) mean free time $\tau$ does not depend on the field; (3) drift velocity is linear in the field. When all three hold, the material is **ohmic** and $V = IR$ is accurate. When any one fails, you have a **non-ohmic** device. Semiconductors fail (1) — heating excites more carriers across the band gap, so $n(T)$ rises sharply. Diodes fail it geometrically — a p-n junction has asymmetric $n$ on the two sides. Tungsten filaments fail (2) in practice — heating shrinks $\tau$, raising $R$ tenfold between cold and hot. Near dielectric breakdown, assumption (3) breaks.

This is the chapter's central honesty. Ohm's law is not a fundamental law of nature like Coulomb's. It is a consequence of three reasonable assumptions that happen to hold for most metals across a wide range. The mature view is to know *why* it works when it works, and *where* it stops.

### Resistivity — twenty-six orders of magnitude

Resistivity spans an astonishing range. Selected values at 20 °C ([CRC Handbook of Chemistry and Physics, 102nd ed.](https://hbcp.chemnetbase.com/)):

| Material | $\rho$ (Ω·m) | Notes |
|---|---|---|
| Silver | $1.59 \times 10^{-8}$ | Best room-T conductor. |
| Copper | $1.68 \times 10^{-8}$ | The workhorse of wiring. |
| Aluminum | $2.65 \times 10^{-8}$ | High-voltage transmission lines. |
| Tungsten | $5.60 \times 10^{-8}$ | Filaments — chosen for melting point, not $\rho$. |
| Nichrome (Ni-Cr alloy) | $1.10 \times 10^{-6}$ | Heating elements. |
| Pure silicon | $\sim 640$ | Useless as a conductor. Doped, it is the basis of every chip. |
| Fused quartz | $\sim 7.5 \times 10^{17}$ | Among the best room-T insulators. |

Twenty-six orders of magnitude separate quartz from silver. There is no smooth interpolation across that range. Metals and insulators are qualitatively different states of matter, separated by a band gap. Doping silicon adds carriers into nearly-empty bands at parts-per-billion concentrations and slides the Fermi level — six orders of magnitude of resistivity tuning out of one element.

### What's actually scattering the electrons

Drude said "ion cores," and quantum mechanics says that's wrong. In a *perfectly periodic* lattice, electrons propagate as Bloch waves with infinite mean free path. The lattice itself doesn't scatter them; only *departures* from periodicity do — lattice vibrations (phonons), defects and impurities, and weakly, other electrons. Phonon scattering grows linearly with $T$ above the Debye temperature; defect scattering is $T$-independent; electron-electron scattering goes as $T^2$ and matters mainly at very low temperatures. Matthiessen's rule adds them: $\rho(T) = \rho_{\text{defects}} + \rho_{\text{phonon}}(T)$. The mean free path in pure copper at room temperature is about 40 nm ([Gall, *J. Appl. Phys.* **119**, 085101 (2016)](https://pubs.aip.org/aip/jap/article/119/8/085101/143910/)) — about 150 lattice spacings. Drude's "billiard balls hitting ions" gives the right $\sigma = ne^2\tau/m$ with the wrong mechanism for $\tau$.

### Temperature dependence

For most metals near room temperature, resistance varies approximately linearly with temperature:

$$R(T) = R_0\left[1 + \alpha(T - T_0)\right]$$

where $\alpha$ is the **temperature coefficient of resistance**. Sample values (per kelvin, at 20 °C): copper $4.04 \times 10^{-3}$; aluminum $3.9 \times 10^{-3}$; tungsten $4.5 \times 10^{-3}$; nichrome $4 \times 10^{-4}$ (much smaller — alloy disorder dominates over phonons, which is why nichrome makes good precision resistors). For semiconductors, $\alpha$ is *negative* and large: heating excites more carriers across the band gap, so $n$ rises exponentially. Pure silicon has $\alpha \approx -0.07$ /K — twenty times the magnitude of copper's, opposite sign. This is the basis of the thermistor.

### Power and Joule heating

When current $I$ flows across a potential difference $V$, the power delivered is

$$P = IV.$$

For a resistor obeying Ohm's law ($V = IR$), the same power can be written three ways:

$$\boxed{\;P = IV = I^2R = \frac{V^2}{R}\;}$$

All three forms are algebraically equivalent. Pick the one that matches the variables you have: $V^2/R$ for a voltage source driving a known load; $I^2R$ for a current source; $IV$ for measured terminal values.

The microscopic picture: each carrier picks up energy $-e\mathbf{E}\cdot d\mathbf{x}$ between collisions and dumps it into the lattice in the next collision. The rate of energy dumping per unit volume is $\mathbf{J}\cdot\mathbf{E} = \sigma E^2$. Integrate over the wire and you recover $P = I^2R$. This conversion of ordered drift energy to disordered lattice vibration — heat — is **Joule heating**, after James Prescott Joule's 1841 measurements that established the equivalence ([Joule, *Phil. Mag.* **19**, 260 (1841)](https://www.tandfonline.com/doi/abs/10.1080/14786444108650416)). Every electrical device that warms up while running dumps $I^2R$ into something.

### EMF and internal resistance

A real battery is not an ideal voltage source. It has an **electromotive force** $\varepsilon$ (open-circuit voltage, set by its chemistry) and an **internal resistance** $r$ (set by ion mobility in the electrolyte and electrode kinetics). Loaded with external resistance $R$:

$$\varepsilon = I(R + r), \quad V_{\text{terminal}} = \varepsilon - Ir.$$

A fresh AA alkaline has $\varepsilon \approx 1.5$ V and $r \approx 0.15$–$0.30$ Ω. As it discharges, $r$ rises (reaction products clog the electrolyte path), and the terminal voltage sags under any load — which is why "dead" batteries often measure 1.4 V with nothing connected but fail to push current through a flashlight bulb.

Chapter 7 will use $\varepsilon$ and $r$ inside Kirchhoff's circuit laws. For this chapter, the point is that EMF is the *non-conservative* push that keeps current flowing against $I^2R$ losses. Without an EMF source, $\oint \mathbf{E}\cdot d\boldsymbol{\ell} = 0$ around every loop (Chapter 4 electrostatics), and no steady current can flow. The battery, the photovoltaic cell, the dynamo — each converts some other form of energy into a non-conservative line integral of $\mathbf{E}$ around a closed loop.

### Superconductivity — the limit $R = 0$

In April 1911, Heike Kamerlingh Onnes — having three years earlier been the first person to liquefy helium (4.2 K) — cooled solid mercury through 4.2 K and watched its resistance drop, not toward some small value, but to *unmeasurably zero*. His lab notebook from 8 April 1911, 4:00 PM reads in Dutch: *"Kwik nagenoeg nul"* — "Mercury nearly zero." This was the discovery of **superconductivity** ([Onnes, *Comm. Leiden* **120b** (1911)](https://ethw.org/Milestones:Discovery_of_Superconductivity,_1911); Onnes won the 1913 Nobel Prize for the helium work, with superconductivity as the bonus discovery the technique made possible).

Below a critical temperature $T_c$, the resistance is not just small but *exactly zero*. A current set up in a superconducting loop persists for years without measurable decay. The phenomenon stayed unexplained for forty-six years. In 1957, John Bardeen, Leon Cooper, and Robert Schrieffer published *Theory of Superconductivity* ([Bardeen, Cooper & Schrieffer, *Phys. Rev.* **108**, 1175 (1957)](https://link.aps.org/doi/10.1103/PhysRev.108.1175)). The mechanism, counterintuitively, requires the electrons to *attract* each other — mediated by the lattice, which deforms slightly around one electron and pulls another toward it. Bound pairs ("**Cooper pairs**") are bosons; they condense into a single coherent quantum state that carries current without scattering. BCS won the 1972 Nobel; Bardeen's second.

In 1986, J. Georg Bednorz and K. Alex Müller at IBM Zurich found superconductivity at ~35 K in a barium-lanthanum-copper-oxide ceramic ([Bednorz & Müller, *Z. Phys. B* **64**, 189 (1986)](https://link.springer.com/article/10.1007/BF01303701)) — far above the previous record. The 1987 Nobel followed *the next year*, the shortest such interval in physics history. Within months, Wu, Chu and collaborators synthesized YBa₂Cu₃O₇ with $T_c \approx 92$ K ([Wu et al., *Phys. Rev. Lett.* **58**, 908 (1987)](https://link.aps.org/doi/10.1103/PhysRevLett.58.908)) — the first material superconducting above the boiling point of *liquid nitrogen* (77 K). Liquid N₂ is cheap; the engineering economics of superconductivity changed overnight.

The mechanism in cuprate high-$T_c$ materials remains, as of 2026, *unsettled*. BCS does not predict $T_c$ this high; the binding is widely believed to involve antiferromagnetic spin fluctuations in the copper-oxide planes, but no quantitative microscopic theory has emerged in forty years. Periodic dramatic claims get tested rapidly — most recently the **LK-99** Korean preprint of July 2023 claiming room-temperature ambient-pressure superconductivity in copper-doped lead apatite, whose anomalies were traced within weeks to a Cu₂S impurity phase transition near 385 K ([Wikipedia, "LK-99"](https://en.wikipedia.org/wiki/LK-99)). High-pressure hydrogen-rich compounds (H₃S at 203 K and 150 GPa; LaH₁₀ at ~250 K and 170 GPa) are real but require diamond-anvil pressures. As of 2026, no credible ambient-pressure room-temperature superconductor exists.

The point for this chapter: the resistance you measure in a metal at room temperature is *not inevitable*. Cool the right material enough and it vanishes.

---

## Worked example: drift velocity, resistance, and power in a copper wire

A copper wire of length $L = 10$ m and diameter $d = 1$ mm carries a current $I = 1$ A. Use $\rho_{\text{Cu}} = 1.68 \times 10^{-8}$ Ω·m and $n_{\text{Cu}} = 8.5 \times 10^{28}$ electrons/m³.

**(a) Cross-sectional area.** $A = \pi(d/2)^2 = \pi(0.5 \times 10^{-3})^2 = 7.85 \times 10^{-7}$ m².

**(b) Resistance.** $R = \rho L/A = (1.68 \times 10^{-8})(10)/(7.85 \times 10^{-7}) = 0.214$ Ω. About a fifth of an ohm. House wiring with comparable gauges has voltage drops of fractions of a volt across the run from breaker to outlet, not tens of volts.

**(c) Voltage drop and field.** $V = IR = 0.214$ V; $E = V/L = 0.0214$ V/m. A tenth of a volt per meter is what it takes to push 1 A through copper of this gauge.

**(d) Drift velocity.**
$$v_d = \frac{I}{nqA} = \frac{1}{(8.5 \times 10^{28})(1.6 \times 10^{-19})(7.85 \times 10^{-7})} \approx 9.4 \times 10^{-5} \text{ m/s}.$$

Roughly 0.094 mm/s. Continental plates move faster than electrons in your house wiring.

**(e) Power dissipated.** $P = I^2R = 0.214$ W. About a fifth of a watt of heat in 10 m of wire — distributed over the wire's surface, the temperature rise is a couple of degrees. Push 10 A through the same wire and $P = 21.4$ W in ten meters, approaching the gauge's safe limit.

**(f) Mean free time.** Inverting $\sigma = ne^2\tau/m$ with $\sigma = 1/\rho = 5.95 \times 10^7$ S/m and $m = 9.11 \times 10^{-31}$ kg:
$$\tau = \frac{m\sigma}{ne^2} \approx 2.5 \times 10^{-14} \text{ s}.$$

Twenty-five femtoseconds. At the Fermi velocity $v_F \approx 1.6 \times 10^6$ m/s, the mean free path is $\lambda = v_F\tau \approx 40$ nm — about 150 lattice spacings, in good agreement with thin-film measurements.

**The lesson.** Three macroscopic quantities — $R$, $V$, $P$ — derive from one microscopic quantity, $\tau$, plus $n$ and geometry. The Drude model is a single relation, $\sigma = ne^2\tau/m$, doing all the connecting work.

**The limit.** The derivation assumed $n$ and $\tau$ are field-independent. For these fields (tens of mV/m), the energy gained between collisions is $eE\lambda \approx 10^{-9}$ eV — vastly smaller than $k_BT \approx 0.026$ eV at room temperature. The field is a negligible perturbation; Ohm's law is safe. Push the field a million times higher and you would see non-ohmic effects in copper. You would also see the wire vaporize, so the failure regime is academic for ordinary copper.

---

## Common misconceptions

**"Current flows at the speed of light."** The *signal* — the rearrangement of the field — propagates near $c$. The *electrons* drift at mm/s. The bulb lights instantly because the electrons already in the filament begin drifting the moment the field arrives, not because any single electron has traveled from the switch to the bulb.

**"Current is used up by a resistor."** Charge is conserved at every node and through every series branch. The current that exits a resistor equals the current that entered. What is dissipated is *energy* — power $I^2R$ becomes heat. An ammeter on either side of the resistor reads the same value. This is documented as the single most persistent failure mode in intro E&M ([McDermott & Shaffer, *Am. J. Phys.* **60**, 994 (1992)](https://doi.org/10.1119/1.17008)); the simulator at the end is calibrated to break it visually.

**"Ohm's law is a fundamental law of physics."** It is an empirical approximation, derivable from three Drude assumptions (constant $n$, field-independent $\tau$, linear response). Semiconductors, diodes, transistors, and incandescent filaments all violate at least one. Ohm's law is to electrodynamics what Hooke's law is to mechanics — a useful linear-response result wrongly elevated to universal status in many intro courses.

**"Resistance is a property of the wire alone."** $R$ depends on $\rho$ and $L/A$, but the resistance of a *path* depends on every joint and contact along it. The 1970s US aluminum-house-wiring fires were caused not by aluminum's resistivity (only 60% higher than copper) but by aluminum-on-brass joints loosening with thermal cycling, oxidizing, and developing high-$R$ contact points where $I^2R$ heating concentrated. A wire with low $\rho$ does not save you if one connection has 0.1 Ω at 15 A — that is 22 W in a half-cubic-centimeter of metal, enough to start a fire ([CPSC, "Aluminum Wiring," 2011](https://www.cpsc.gov/Safety-Education/Safety-Guides/Home/Aluminum-Wiring)).

**"Doubling voltage doubles power."** Only for a fixed current source. For an ohmic resistor at fixed $R$, doubling $V$ also doubles $I$, so $P = V^2/R$ *quadruples*. A 100 Ω resistor with 5 V across it dissipates 0.25 W (within a quarter-watt rating). With 10 V across it, 1.0 W — well above rating, likely smoke. The form $P = IV$ misleads students who treat $V$ and $I$ as independent; Ohm's law ties them together.

---

## Exercises

**Warm-up (Understand).** State the four speeds of electricity in a copper wire (drift, thermal, Fermi, signal) and put them in order of magnitude. Explain in one sentence each what physical phenomenon sets the size of that particular speed. Then answer: which one is "the current"? Which one tells you when the bulb lights up?

**Apply (drift velocity).** A 14-gauge copper wire has cross-section $A = 2.08 \times 10^{-6}$ m². It carries 10 A — a typical household branch-circuit limit. Compute the drift velocity. Compare to the speed of a snail (~1 mm/s). Compare to the Fermi velocity in copper ($1.6 \times 10^6$ m/s). How long would a *single* electron take to travel 5 m from the breaker box to a kitchen outlet at this drift velocity?

**Apply (resistance from geometry).** A copper wire of length 25 m and diameter 1.5 mm. Compute (a) the cross-sectional area, (b) the resistance, (c) the voltage drop if it carries 5 A, (d) the power dissipated as heat in the wire. Use $\rho_{\text{Cu}} = 1.68 \times 10^{-8}$ Ω·m.

**Apply (power three ways).** A 100 Ω resistor with 5 V across it. Compute $P$ using each of $P = IV$, $P = I^2R$, $P = V^2/R$. Verify all three give the same answer. Then: if the voltage is doubled to 10 V, by what factor does the power increase? Why not by a factor of 2?

**Apply + Analyze (inrush current).** A 60 W incandescent bulb at 120 V draws 0.5 A in steady-state operation; its tungsten filament runs at ~2,800 K (about 2,500 °C above room temperature). Using $\alpha_{\text{W}} = 4.5 \times 10^{-3}$ /K, (a) estimate the ratio $R_{\text{hot}}/R_{\text{cold}}$ from the linear-$\alpha$ formula, (b) compute $R_{\text{cold}}$ and the instantaneous inrush current at switch-on, (c) explain why old filament bulbs most often fail *at the moment of turn-on*, rather than during steady operation.

**Apply + Analyze (transmission lines).** A power line of resistance 10 Ω is to deliver 1 GW of electrical power over 200 km. Compute the fractional power lost to $I^2R$ heating in the line if the transmission voltage is (a) 110 kV, (b) 345 kV, (c) 765 kV. Argue from the numbers why high-voltage transmission is not a design choice but a physical necessity. (Hint: $P_{\text{load}} = IV$ at the load; $P_{\text{loss}} = I^2R$ along the line.)

**Challenge (Synthesize: deriving Drude).** Starting from $\mathbf{F} = -e\mathbf{E}$ on an electron in a uniform field, with mean free time $\tau$ between memory-erasing collisions, derive in order: (a) the drift velocity $v_d = e\tau E/m$ (magnitude only; sign-keeping is bookkeeping), (b) the current density $J = (ne^2\tau/m)E$, (c) the conductivity $\sigma = ne^2\tau/m$ and resistivity $\rho = m/(ne^2\tau)$, (d) Ohm's law $V = IR$ with $R = \rho L/A$ for a uniform wire. Then plug in copper's $n = 8.5 \times 10^{28}$ /m³ and $\tau = 2.5 \times 10^{-14}$ s and verify $\rho \approx 1.7 \times 10^{-8}$ Ω·m, in agreement with measured. Name the three approximations the derivation requires for Ohm's law to hold.

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

## What would change my mind

The central claims of this chapter — that current is $nqv_dA$, that the Drude model gives $\sigma = ne^2\tau/m$, that Ohm's law follows from this plus three approximations, that $P = I^2R$ accounts for the dissipation — are mature, well-tested physics. The Drude conductivity formula reproduces measured $\rho$ in free-electron metals to within a small factor, with $\tau$ computable from band-structure plus phonon and impurity scattering ([Ashcroft & Mermin, *Solid State Physics*, Ch. 1–2, 13](https://www.cengage.com/c/solid-state-physics-1e-ashcroft-mermin/9780030839931/)). A confirmed observation of persistent macroscopic DC current in a closed conservative-field circuit (no EMF source) would overturn energy conservation; none has ever been seen. Reproducible non-ohmic behavior in a pure metal at small fields and constant temperature would mean one of the three Drude approximations is failing in unexpected territory; none has been observed. A microscopic theory of high-$T_c$ superconductivity comparable in completeness to BCS would not overturn the chapter's claims but would replace the "mechanism unclear" qualifier; as of 2026 the spin-fluctuation picture is the leading candidate but a quantitative theory has not arrived.

Time-varying conditions are different. In AC circuits at high frequency, skin effect and inductive coupling change the simple Drude picture. None of these *contradict* the chapter; they require more physics on top.

## Still puzzling

- *Why does $\sigma = ne^2\tau/m$ survive the Drude → Sommerfeld transition essentially unchanged?* Sommerfeld (1928) replaced Maxwell-Boltzmann statistics with Fermi-Dirac, fixing Drude's catastrophically wrong specific-heat prediction (off by ~100×). The conductivity formula came through nearly intact, with $\tau$ now reinterpreted as the relaxation time at the Fermi surface. The two definitions happen to coincide for free-electron-like metals at room temperature. The agreement is closer than any first-principles argument seems to require.
- *Why is the world full of ohmic materials?* Three approximations (constant $n$, field-independent $\tau$, linear response) all hold *together* across decades of $V$ and $I$ for most metals. The honest partial answer is that $eE\lambda \ll k_BT$ for any field a metal can sustain without breaking down, so the linearity part is robust; $n$ is fixed by the band structure; $\tau(T)$ is well-modeled as a sum of phonon plus defect contributions. Each piece is understood; the combined robustness across so much of everyday operating range remains more impressive than any one piece.
- *Room-temperature superconductivity at ambient pressure.* Whether *any* material is superconducting at room temperature and one atmosphere remains an open empirical question. LK-99 (2023) and the Ranga Dias retractions (2022, 2023) show how the field rapidly self-corrects when claims are concrete enough to replicate. The hunt continues.

---

**Tags:** electric current, drift velocity, Drude model, Ohm's law, resistivity, conductivity, Joule heating, superconductivity
