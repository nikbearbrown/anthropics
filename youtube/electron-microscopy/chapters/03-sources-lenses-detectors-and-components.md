# Chapter 3 — Electron Sources, Lenses, Detectors, and Instrument Components


## TL;DR

- The resolution number on the spec sheet is the joint output of a dozen design choices — and several of them you're going to make in the next ten minutes.
- The chapter moves through Where the electrons come from, What the lenses do, Detectors: a preview, Keeping the beam alive: vacuum, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*The resolution number on the spec sheet is the joint output of a dozen design choices — and several of them you're going to make in the next ten minutes.*

---

There is a moment every new graduate student has, standing in front of a field-emission SEM for the first time. The column hums. A small indicator says "ready." And somewhere on the console, usually printed on a laminated card taped near the monitor, is a number: 1 nm. That is what this instrument can do.

![The opening scene — an FE-SEM console with the laminated specification card.](../images/03-sources-lenses-detectors-and-components-fig-01.png)

*Figure 1.* The opening scene — an FE-SEM console with the laminated specification card.

What the laminated card does not explain is that the 1 nm is not a property of the machine the way the serial number is a property of the machine. It is the output of a chain of decisions, some made years ago by engineers in Japan, and some you are about to make. The gun was chosen for a reason. The lens was wound to a particular geometry for a reason. The vacuum system is running right now, while the column hums, because without it the beam would scatter into nothing before it reached your specimen. Every one of those choices couples to every other. This chapter is about understanding how.

The organizing question is simple: how does the instrument turn a source of electrons into a focused probe at the specimen? The answer involves four distinct subsystems — the gun, the lenses, the vacuum system, and the detectors — and the interesting thing is that you cannot understand any one of them without understanding what it demands from the others.

![Column schematic from gun to specimen showing the](images/03-sources-lenses-detectors-and-components-fig-01.png)
*Figure 3.1 — Column schematic from gun to specimen showing the*

## Where the electrons come from

Start at the top of the column, because everything downstream is downstream of this.

There are two ways to pull electrons out of metal. You can heat the metal until the thermal energy of electrons near the surface exceeds the work function — the energy barrier that normally keeps them inside. Or you can apply a strong enough electric field at the tip of a very sharp needle that the barrier becomes thin enough for electrons to tunnel quantum-mechanically through it. The first is thermionic emission. The second is field emission. Every electron gun is a variation on one of these two physics, or a hybrid of both.

The simplest gun is a V-shaped tungsten wire, about 100 μm across, heated resistively to something near 2700 K. At that temperature, the Richardson equation

$$J_c = A_c T^2 e^{-E_w / kT}$$

describes how much current density escapes — $E_w$ is the work function (4.5 eV for tungsten), $T$ is temperature, $k$ is Boltzmann's constant, $A_c$ is a materials constant. The hot filament sits at high negative potential; a cap called a Wehnelt grid, biased slightly more negative still, squeezes the emitted cloud into a small crossover; the anode at ground accelerates a fraction of it through a hole into the rest of the column.

![Cross-section diagram of a thermionic gun showing the](images/03-sources-lenses-detectors-and-components-fig-02.png)
*Figure 3.2 — Cross-section diagram of a thermionic gun showing the*

The operator's job with a tungsten gun is to find saturation. Increase filament current and emission increases — up to a point. Past that point, adding heat does nothing useful, because every electron that can escape has already escaped. Below saturation, the image has a halo: a ring of unfocused emission outside the main beam. The first thing you learn on a tungsten SEM is how to find the flat part of the saturation curve.

The problem with tungsten is not that the physics is wrong. It is that the work function is high, which means you need a lot of heat to get useful emission, which means the electrons leave the surface with a wide spread of energies — somewhere between 1 and 3 eV. That energy spread matters because of chromatic aberration, which we treated in Chapter 2. A wider spread means a larger chromatic aberration disk in the probe. At 30 kV, that disk is small enough not to matter much. At 1 kV, it dominates everything.

Lanthanum hexaboride — LaB₆, a ceramic — has a work function of 2.5 eV instead of 4.5 eV. Half the work function means you reach the same emission at lower temperature, which means a narrower energy spread (0.5–2.5 eV rather than 1–3 eV) and a longer filament lifetime (200–1000 hours rather than 40–100 hours for tungsten). LaB₆ is fragile — thermal shock will shatter it — and it contaminates easily, so the vacuum requirement is 100× more stringent than tungsten: $10^{-7}$ Torr instead of $10^{-5}$ Torr. The brightness is 10× higher. Whether that trade is worth it depends on what you are trying to image.

The Schottky emitter is a tungsten tip coated with a layer of zirconium oxide, which drops the effective work function from 4.5 eV to 2.8 eV. It operates at about 1800 °C — hot enough to keep the surface clean and emission stable, cool enough that the energy spread is only 0.3–1.0 eV. A suppressor electrode catches stray thermal emission; an extraction electrode pulls electrons specifically from the very tip. The result is a small, bright, stable source with an energy spread narrow enough to make low-kV imaging practical and a lifetime around 4,000 hours. This is the gun in most modern high-resolution SEMs.

The cold field emitter is the extreme case. No heat at all. A tungsten tip with a radius below 100 nm — sharp enough that an applied voltage of a few kilovolts produces a field around 10 V/nm at the apex. At that field strength, the surface barrier is thin enough for electrons to tunnel through directly. The source size is around 3 nm, the energy spread is 0.2–0.3 eV, and the brightness is the highest of any source: roughly $2 \times 10^7$ A/(cm²·sr·kV). The vacuum requirement is the most demanding: $10^{-10}$–$10^{-13}$ Torr, ultra-high vacuum that requires its own ion pump separate from the rest of the column.

The catch with cold field emission is that residual gas molecules slowly adsorb onto the tip even in UHV, and emission decays noticeably over 10–15 minutes. The operator periodically flashes the tip — heats it briefly to around 2500 K — to clean the surface and reset the emission cycle. If you are running a CFE instrument and the beam keeps getting dim, you are not imagining things. You need to flash.

The comparison in numbers:

| Property | W (thermionic) | LaB₆ | Schottky | Cold FE |
|---|---|---|---|---|
| Brightness (A/cm²·sr·kV) | $10^4$ | $10^5$ | $5 \times 10^6$–$10^7$ | $2 \times 10^7$ |
| Energy spread ΔE | 1–3 eV | 0.5–2.5 eV | 0.3–1.0 eV | 0.2–0.3 eV |
| Vacuum required | $10^{-4}$–$10^{-6}$ Torr | $10^{-6}$–$10^{-8}$ | $10^{-9}$–$10^{-11}$ | $10^{-10}$–$10^{-13}$ |
| Effective source size | 15,000 nm | 5,000 nm | 15 nm | 3 nm |
| Lifetime | 100–200 h | 600–1,000 h | 4,000 h | 5,000 h |

![Bar chart of brightness (log scale) for the](images/03-sources-lenses-detectors-and-components-fig-03.png)
*Figure 3.3 — Bar chart of brightness (log scale) for the*

The pattern in that table is the fundamental trade. Every step toward higher brightness, smaller source size, and narrower energy spread demands a harder vacuum and more operational discipline. There is no free lunch. A tungsten thermionic gun asks almost nothing of you and gives you what it can. A cold field emitter demands UHV, demands flashing, and in return gives you a probe that can do things the tungsten gun simply cannot.

The single most important concept for understanding everything the gun does to the column is brightness. Electron-optical brightness — measured in A/(cm²·sr·kV) — is the current density per unit solid angle of the beam, and it is a conserved quantity. No lens in the column can increase it. You cannot make a brighter probe than the gun makes; you can only spend the brightness on different combinations of probe size, aperture angle, and beam current. A rough way to see this: at the probe, brightness and probe diameter $d$ and aperture half-angle $\alpha$ and beam current $i_b$ are related by

$$\beta = \frac{4 i_b}{\pi^2 d^2 \alpha^2}.$$

If you want a 5 nm probe carrying 10 pA from a source with $\beta = 10^7$ A/(cm²·sr·kV), the required aperture half-angle works out to about 1 mrad — a small angle, close to the brightness limit. A tungsten gun at $\beta = 10^4$ would not be able to deliver 10 pA into a 5 nm probe at all; the numbers simply do not close. That is why you cannot image nanoparticles at 1 kV on a tungsten thermionic SEM by turning any knob. The gun is the ceiling.

## What the lenses do

The column turns the gun's crossover — the smallest point of the emitted beam just below the Wehnelt — into a focused probe at the specimen. It does this with a stack of magnetic lenses.

Chapter 2 explained how a magnetic lens works: an axially symmetric field that bends off-axis electrons back toward the axis, with focal length that depends on lens excitation. Here the question is what each lens in the stack is actually doing, and what the operator controls when turning a knob.

Between the gun and the specimen, every SEM has at least one condenser lens, and the objective lens. The condenser's job is demagnification: it takes the source crossover — which might be 15 μm across for a tungsten thermionic gun and around 3 nm for a cold FE — and shrinks it. When you turn the "spot size" or "C1" knob on the console, you are changing the excitation of the condenser, and therefore its focal length, and therefore the degree of demagnification. More excitation means a smaller probe diameter. But brightness is conserved: a smaller probe means a smaller probe current, because you are squeezing the same cone of electrons into a smaller disk. If you need more current for an X-ray analysis and you open the spot size knob, you are getting a brighter image at the cost of resolution. That is not a knob miscalibration. That is the physics.

The objective lens does the final step: it focuses the demagnified crossover onto the specimen surface. It is also the lens whose aberration coefficients — specifically $C_s$ for spherical aberration and $C_c$ for chromatic aberration — dominate the probe size budget. The manufacturer's resolution spec comes almost entirely from how well they designed the objective pole pieces. The tighter the gap between the pole pieces and the smaller the bore, the lower $C_s$ and $C_c$ will be — and the less room there is for the specimen.

This is the central design tension in SEM column engineering. Three broad objective designs sit at different positions on the trade:

![Cross-sections of pinhole, immersion, and snorkel objective lenses](images/03-sources-lenses-detectors-and-components-fig-04.png)
*Figure 3.4 — Cross-sections of pinhole, immersion, and snorkel objective lenses*

In a **pinhole lens**, the specimen sits below the objective, in a field-free region. Aberrations are relatively large. Specimens can be large — centimeters across, centimeters tall. This is the geometry of a general-purpose SEM, and the geometry in which most biological imaging happens.

In an **immersion lens**, the specimen sits inside the strong field of the objective. $C_s$ is as low as the design can make it. But the field restricts specimen size to a few millimeters, and magnetic materials are out of the question.

In a **snorkel lens**, a strong field projects out of the pole piece down to the specimen, which sits below the lens gap. A compromise: better aberrations than pinhole, less specimen restriction than immersion.

Modern FE-SEMs increasingly use in-lens detectors — detectors that work because the strong objective field spirals secondary electrons up through the lens to a detector above. The detector design is thus coupled to the objective design. You cannot understand why the secondary electron image looks the way it does without knowing which objective geometry produced it.

In an SEM, after the objective lens come the scan coils. These are not a lens at all. They are a pair of deflection coils that swing the focused probe across the specimen in a raster pattern. The magnification displayed on the monitor is electronically the ratio of the monitor edge to the size of the scanned region: higher magnification means a smaller raster. There is no additional optic. The probe is the same probe regardless of magnification; you are just moving it across a smaller area.

In a TEM, the architecture diverges completely after the objective. Instead of scan coils, there are projector lenses — intermediate and projector — that cascade the post-specimen image to higher and higher magnification and project it onto a fluorescent screen or a camera. The whole specimen is illuminated at once. There is no scanning.

Apertures live inside the lens stack, and they matter because every lens introduces aberration. A smaller aperture blocks off-axis rays and reduces spherical aberration. But a smaller aperture also reduces beam current, and the smaller opening makes the diffraction limit worse. The optimum aperture size — the one that minimizes total probe size — balances the diffraction disk against the spherical aberration disk, and it depends on the aberration coefficients of the objective and the energy spread of the gun. This is why "what aperture should I use" has an answer that changes depending on whether you are running a tungsten or a Schottky instrument.

## Detectors: a preview

The probe hits the specimen and generates signals. Different detectors catch different signals, which is why the same specimen imaged with different detectors produces what look like completely different images. A complete treatment is in Chapter 7 for SEM and Chapter 13 for TEM. For now, the orientation.

Low-energy secondary electrons — energies mostly below 50 eV, peaking around 3–5 eV — come from near the surface of the specimen. They carry surface topography information. The classic way to detect them is the Everhart-Thornley detector: a scintillator behind a Faraday cage biased at +300 V to attract SEs, sitting at +10 kV to give them enough energy to excite the phosphor, coupled by a light guide to a photomultiplier. This was described in 1960 and it remains the most common SEM detector. It works because the +300 V cage draws in SEs from a wide solid angle, not just from the narrow cone pointing directly at the detector.

Backscattered electrons — energies 70–90% of the primary beam energy — come from deeper and carry compositional information. Heavier elements backscatter more electrons, so in a backscatter image a higher-Z region appears brighter than a lower-Z region. Backscatter detectors are solid-state semiconductor diodes, often annular and mounted close to the specimen, or YAG scintillators. They do not need the +300 V cage because the BSEs have enough energy to reach the detector directly.

In FE-SEMs with strong immersion objective fields, a through-the-lens detector is mounted above the objective. The lens field spirals secondary electrons upward through the bore and delivers them to the detector. Because the path is through the lens, not around it, the image is primarily SEs from very near the impact point — the highest-resolution SE signal you can get.

Characteristic X-rays, generated when beam electrons knock inner-shell electrons out of specimen atoms, carry elemental information. They are detected with a silicon drift detector — the energy-dispersive X-ray spectrometer, or EDS. Chapter 9 covers EDS in full.

In TEM, the "detector" is usually a camera. Early TEMs used a fluorescent viewing screen directly. CCD and CMOS cameras used a scintillator to convert electrons to light before detection. The direct-detection cameras that became practical after 2010 use CMOS sensors that detect electrons without an intervening scintillator — the improvement in detective quantum efficiency is what made single-particle cryo-EM reconstructions below 3 Å feasible.

The key thing to understand about detectors is that you cannot read an SEM image without knowing what detector made it. "SEM image" is incomplete documentation. The same specimen with an E-T detector and a backscatter detector looks like two different specimens.

## Keeping the beam alive: vacuum

Atmospheric pressure is 760 Torr. At that pressure, an electron travels a fraction of a millimeter before hitting a gas molecule. The column is hundreds of millimeters long. Without vacuum, no beam reaches the specimen.

The relevant figure is mean free path — the average distance a particle travels before a collision. Mean free path scales inversely with pressure. At rough vacuum (around 1 mbar), it is a fraction of a centimeter. At high vacuum ($10^{-5}$ mbar), it is tens of kilometers. The column needs to keep the beam flying freely from gun to specimen.

Different parts of the column need different pressure targets. The specimen chamber of a typical SEM runs at $10^{-3}$–$10^{-5}$ Pa. A TEM column needs $10^{-5}$ Pa or better across the full optical path. A cold field emission gun needs ultra-high vacuum at $10^{-10}$–$10^{-13}$ Torr in its own chamber — because contaminant molecules that would be harmless elsewhere adsorb onto the tip and kill emission within minutes.

![Logarithmic pressure scale from atmosphere to UHV with](images/03-sources-lenses-detectors-and-components-fig-05.png)
*Figure 3.5 — Logarithmic pressure scale from atmosphere to UHV with*

No single pump spans the 14 orders of magnitude from atmosphere to UHV. The pumps are staged.

A roughing pump — usually a dry scroll pump in modern systems — takes the chamber from atmosphere down to about $10^{-1}$ Torr. It works by mechanically pushing gas out. Below that pressure, momentum-transfer pumps take over. Turbomolecular pumps spin a rotor at tens of thousands of RPM; gas molecules hitting the spinning blades are kicked toward the exhaust. A good turbomolecular pump reaches $10^{-9}$–$10^{-10}$ Torr. For the gun chamber on a CFE instrument, an ion getter pump takes the remaining gas, ionizes it, and buries it in a titanium cathode — reaching $10^{-11}$ Torr or below.

A rough estimate of how long pump-down takes is useful for planning. For a constant-speed pump on a fixed volume, the pressure falls exponentially:

$$P(t) = P_0 e^{-St/V}$$

where $S$ is the pump speed and $V$ is the chamber volume. A 50 L chamber pumped by a 1.4 L/s scroll pump from atmosphere to $10^{-1}$ Torr takes roughly $t = (50/1.4) \ln(760/0.1) \approx 320$ seconds — about five minutes. Real systems take longer because of conductance limits in the plumbing and outgassing from chamber walls, but the exponential structure is real: the early part of pump-down goes fast, and the last decade of pressure takes longer per decade than the first.

The "monolayer time" — how long before a clean surface acquires a monolayer of contaminant from residual gas — is the other quantity operators care about. At high vacuum, $10^{-5}$ Pa, a fresh surface stays clean for a few hundred seconds. At UHV, for hours. This is why surface-sensitive techniques, and CFE tips, demand UHV: they cannot afford even monolayer-scale contamination.

Gauges are as staged as the pumps. A Pirani gauge — a heated wire whose thermal conductance to surrounding gas changes with pressure — covers atmosphere to about $10^{-3}$ Torr. A Penning discharge gauge covers $10^{-3}$ to $10^{-7}$ Torr. A hot-cathode ionization gauge reaches below $10^{-12}$ Torr. Most instruments run all three, daisy-chained: the Pirani watches the pump-down, the Penning monitors the chamber during operation, the ion gauge watches the gun.

Two hazards are worth naming explicitly. Viewport implosion — glass viewing ports under vacuum can shatter inward if damaged — is a documented and serious risk. Inspect seals before working chamber-side; never lean on the chamber. High voltage in the gun and accelerating stage runs from 1 kV to 300 kV depending on the instrument. Modern interlocks prevent casual contact; service work in the high-voltage section is for trained engineers only.

## The column as a system

The picture, end to end: the gun sets brightness, energy spread, and source size. Those three numbers are the ceiling for everything downstream. The condenser lens takes the source crossover and demagnifies it, trading probe current for probe diameter depending on its excitation. The objective lens performs the final demagnification — or the first imaging step, in a TEM — and contributes the dominant aberrations. The aperture balances diffraction and spherical aberration to find the smallest achievable probe for the current conditions. The scan coils raster the probe across the specimen in SEM, or the projector lenses magnify the transmitted image in TEM. Detectors measure different emitted signals and produce images that look different because they are measuring different things. The vacuum system keeps the beam alive and the gun clean at the pressure each component requires.

The coupling between subsystems is the reason a single knob change can affect so many things at once. Changing the accelerating voltage shifts the chromatic aberration (which scales as $\Delta E / E_0$), changes the interaction volume in the specimen, changes the secondary-electron yield, changes the X-ray emission energy range, and changes the optimal aperture size — all simultaneously. Changing the spot-size knob changes probe diameter and probe current together, not independently, because brightness is conserved. You cannot have a small probe and high current from a given gun. You can only choose how to spend what the gun provides.

The rest of this book describes how to drive this hardware. Chapter 4 starts with the SEM as an operating instrument. Chapter 5 turns the physics of the lens stack into the practical decisions you make every session: accelerating voltage, working distance, probe current, aperture, magnification, and how each couples to image quality. Chapter 7 unpacks detector contrast in full. Chapter 13 returns to lens design at the TEM scale.

But the hardware is what you just learned. When the rest of the book names a subsystem, you should know what it is made of, what it optimizes for, and what it costs.

---

## Exercises

### Warm-up

**3.1** A tungsten thermionic SEM and a cold field emission SEM are both set to 1 kV accelerating voltage. Which produces a smaller probe, and why? Your answer should name the specific aberration that dominates at low kV and explain how it connects to gun choice. *(Tests: gun energy spread → chromatic aberration → probe size at low kV)*

**3.2** You are at the SEM console and the image has a bright halo ring around the central beam spot. Name the cause and the fix in one sentence each. *(Tests: saturation mechanics for thermionic guns)*

**3.3** Match each pump to a pressure range and to its physical mechanism: (a) dry scroll pump, (b) turbomolecular pump, (c) ion getter pump. Ranges: atmospheric–$10^{-1}$ Torr; $10^{-3}$–$10^{-10}$ Torr; $10^{-9}$–$10^{-12}$ Torr. Mechanisms: mechanical compression; spinning rotor imparts momentum to gas molecules; ionization and burial in a titanium cathode. *(Tests: vacuum pump staging)*

### Application

**3.4** A Schottky FE-SEM has brightness $\beta = 5 \times 10^6$ A/(cm²·sr·kV) at 10 kV. The operator wants a probe of diameter 8 nm carrying 50 pA. Using the brightness equation $\beta = 4i_b / (\pi^2 d^2 \alpha^2)$, compute the required aperture half-angle in milliradians. Is this within the typical SEM range of 5–15 mrad? What does your answer tell you about whether this operating point is brightness-limited? *(Tests: brightness conservation calculation)*

**3.5** A lab is choosing between a LaB₆ SEM and a Schottky FE-SEM for a project that requires (i) imaging biological cells at 2 kV to minimize charging, and (ii) EDS mapping of metal nanoparticles inside those cells at 15 kV with high beam current. Which gun serves each task better, and what trade does the lab have to make if it can only have one instrument? *(Tests: gun selection against competing requirements)*

**3.6** A 30 L SEM chamber is pumped by a scroll pump with effective speed 0.8 L/s. Using the exponential pump-down formula, estimate the time to reach $10^{-1}$ Torr from atmosphere (760 Torr). Then explain in one sentence why the real pump-down will take longer than your estimate. *(Tests: pump-down calculation and its limits)*

**3.7** An operator images the same specimen twice — once with the Everhart-Thornley detector, once with an annular backscatter detector — and the two images look almost like different specimens. Describe what each image is showing physically and why the contrast reverses for a region containing both carbon (Z = 6) and gold nanoparticles (Z = 79). *(Tests: detector signal origin and compositional vs. topographic contrast)*

### Synthesis

**3.8** A cold field emission TEM has been vented to atmosphere for a specimen change. The operator pumps down and wants to begin imaging as quickly as possible. Describe the pump sequence from atmosphere to operating pressure, name the gauge used at each stage, and explain why the CFE gun chamber must reach UHV before the tip can be used. Connect your answer to both the vacuum physics from this chapter and the brightness concept. *(Tests: pump staging + gauge matching + gun physics as an integrated system)*

**3.9** The manufacturer's spec sheet for an FE-SEM states "resolution: 1.0 nm at 15 kV, 1.8 nm at 1 kV." Using what you know about chromatic aberration, objective lens design, and brightness conservation, construct an explanation for why the low-kV number is worse — even though lower kV is often preferred for biological and surface-sensitive imaging. What would need to be different about the instrument to close that gap? *(Tests: integrating gun energy spread, chromatic aberration, and the resolution spec as a system output)*

### Challenge

**3.10** A materials scientist wants to image grain boundaries in a steel sample at 0.5 nm resolution. She is specifying a new instrument from scratch. Using the framework of this chapter, argue for a specific gun type, objective geometry, aperture strategy, and vacuum configuration. For each choice, name the trade you are accepting. Then identify which single design choice most limits the final resolution, and explain what would have to change to push past it. *(Tests: instrument specification as a constrained optimization across all four subsystems)*

---

*What would change my mind:* evidence that a tungsten thermionic gun could be operated stably at $10^{-9}$ Torr with brightness comparable to Schottky for many hours. That would close the gun-family gap the table above describes. The underlying physics does not absolutely forbid it, but it is not what current technology delivers.

*Still puzzling:* the practical question of how often field-emission users actually flash their cold-FE tips versus what the manufacturer recommends. The answer varies by lab, shaped more by usage patterns and institutional culture than by any physics I can derive.
