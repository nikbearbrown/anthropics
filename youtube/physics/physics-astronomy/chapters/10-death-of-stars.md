# Chapter 10 — The Death of Stars

*A photographic plate in Chile in February 1987, twenty ghostly particles in a tank of water in Japan, and the discovery that a star's final second outshines a billion galaxies.*

---

## Suggested titles

1. The Death of Stars
2. The Last Second of a Star's Life
3. How Atoms Heavier Than Iron Get Made

## TL;DR

Whether a star ends as a slowly fading white dwarf or a violent supernova is decided by a single number — the Chandrasekhar limit at about 1.4 solar masses — beyond which electron degeneracy pressure runs out of room. What is left behind (a cooling carbon-oxygen sphere, a neutron star, or a black hole) is the universe's way of seeding the next generation of stars and planets with every element heavier than helium.

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Describe the two channels of stellar death — low-mass (planetary nebula + white dwarf) and high-mass (core-collapse supernova + neutron star or black hole) — and state the approximate progenitor mass that separates them.
2. **(Apply)** Use the relativistic-electron-gas argument to sketch why electron degeneracy pressure fails at $M \approx 1.4\, M_\odot$.
3. **(Apply)** Use Stefan-Boltzmann together with the inverse-square law to estimate a Type Ia supernova's peak brightness as a standard candle.
4. **(Analyze)** Read a stellar remnant — given mass, radius, and rotation period — and identify it as white dwarf, neutron star, or black hole, with one observational check for each.
5. **(Apply)** Build an interactive D3 stellar-death router that maps progenitor mass to endpoint and shows where the Chandrasekhar limit appears.

![A flowchart that splits at 8 solar masses. Low-mass stars become red giants, eject a planetary nebula, and leave a white dwarf. High-mass stars run through advanced burning to an iron core, undergo core collapse, and...](../images/10-death-of-stars-fig-02.png)
*Figure 10.2 — Two Death Channels by Mass*

**Prerequisites.** Chapter 3 (spectra, blackbody radiation), Chapter 5 (the Sun's interior, nuclear fusion). Basic algebra and an honest willingness to take one quantum-mechanical fact — the Pauli exclusion principle — as a stated rule rather than a derived one.

---

## Opening case: SN 1987A, Chile and Kamioka, February 1987

On February 24, 1987, Ian Shelton pulled a photographic plate from the developer at Las Campanas Observatory in Chile and saw a bright spot where nothing had been two nights earlier. He went outside and looked at the sky. The object was naked-eye visible in the Large Magellanic Cloud, 160,000 light-years away — the closest supernova visible without a telescope since Kepler's in 1604.

The interesting detail is not the light. It is what arrived three hours before the light.

Twenty-five neutrinos: eleven in the Kamiokande-II water-Cherenkov detector under a mountain in Japan, eight in the Irvine-Michigan-Brookhaven (IMB) detector in a salt mine in Ohio, five in the Baksan scintillator under the Caucasus ([Hirata et al. 1987](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.58.1490); [Bionta et al. 1987](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.58.1494)). All within about thirteen seconds of each other, all about three hours before the photons arrived.

A typical neutrino can pass through a light-year of lead with even odds. The flux at Earth that night was about $5 \times 10^{10}$ neutrinos per square centimeter — roughly $10^{14}$ neutrinos from SN 1987A passed through every human alive. Two dozen interacted with the few hundred tons of clean water under Japanese and American mountains.

![February 23, 1987 timeline. Core collapses in the LMC; neutrino burst of 10^46 J escapes immediately and reaches Earth in a 13-second pulse, registered by Kamiokande-II, IMB, and Baksan. Light from the shock breakout...](../images/10-death-of-stars-fig-01.png)
*Figure 10.1 — SN 1987A: Neutrinos Before Light*

Those interactions confirmed something theorists had calculated for decades and never observed: the energy budget of a core-collapse supernova is carried overwhelmingly by neutrinos. About 99 percent of the energy released — $\sim 10^{46}$ joules — comes out as neutrinos in the first ten seconds. The visible light, bright enough to outshine the host galaxy for weeks, is a one-percent leftover.

![Multi-messenger timeline for August 17, 2017. LIGO/Virgo detect gravitational waves from a binary neutron star merger. Fermi catches a gamma-ray burst 1.7 seconds later. Optical follow-up identifies NGC 4993 11 hours...](../images/10-death-of-stars-fig-07.png)
*Figure 10.7 — GW170817 Kilonova: r-Process Nucleosynthesis Confirmed*

This chapter is what those twenty-five neutrinos tell us. Why do some stars end quietly and others explode? Why is the dividing line so sharp? Why does the explosion produce the matter your body is made of?

---

## Core concept

### Low-mass star death: planetary nebula and white dwarf

The Sun has about another 5 billion years of hydrogen-burning ahead of it. When the hydrogen runs out, the helium core has no nuclear energy source. Gravity squeezes; squeezing heats. Eventually the temperature reaches $\sim 10^8$ K, hot enough to ignite helium fusion through the *triple-alpha* process: three helium nuclei fusing into one carbon. (Fred Hoyle predicted in 1953 that this reaction had to pass through a specific resonance in carbon-12 near 7.65 MeV, or there would be essentially no carbon in the universe. The resonance was found shortly afterward, [Cook et al. 1957](https://journals.aps.org/pr/abstract/10.1103/PhysRev.107.508).)

Helium burning is brief — $\sim 100$ million years for a Sun-like star, against 10 billion for hydrogen. The outer layers expand enormously and cool; the star becomes a red giant. The loosely bound envelope drifts away in slow stellar winds. Lit by ultraviolet from the exposed hot core, it glows as a *planetary nebula* — a name William Herschel gave the round green disks in the 1780s because they looked like planets through his telescope. They are not planets. They are stellar atmospheres in the act of departing.

What remains is the core: a sphere of carbon and oxygen the size of Earth carrying most of a star's mass. About $10^6$ kg/cm³ — a teaspoon weighs as much as a loaded cargo ship. This is a *white dwarf*.

The white dwarf is not held up by heat — the carbon and oxygen are inert at its temperatures. What holds it up is quantum-mechanical, and decides the rest of the chapter.

### The Chandrasekhar limit and core collapse

Here is the one rule from quantum mechanics this chapter asks you to accept: **no two electrons can occupy the same quantum state**. This is the Pauli exclusion principle ([Pauli 1925](https://link.springer.com/article/10.1007/BF02980631)). A "state" specifies position, momentum, and spin together. Stack enough electrons in a small volume and they are forced into higher and higher energy states, because the lower ones are full.

Now compress a chunk of matter. Squeezing localizes each electron in a smaller volume; by Heisenberg's uncertainty principle, $\Delta x \cdot \Delta p \gtrsim \hbar/2$, smaller $\Delta x$ forces larger $\Delta p$. The electrons resist being squeezed not because of thermal collisions (the resistance survives down to absolute zero) but because there is no room left at low momentum. This is **electron degeneracy pressure**.

Now show why the pressure has a ceiling. The argument is Chandrasekhar's, worked out on the steamship *Pilsna* between Bombay and Venice in July 1930 ([Chandrasekhar 1931](https://articles.adsabs.harvard.edu/full/1931ApJ....74...81C)). He was nineteen.

Consider a white dwarf of mass $M$ and radius $R$. The number of electrons is $N \sim M/m_p$. Each electron sits in a volume $\sim R^3/N$, so the uncertainty principle forces a typical momentum

$$p \sim \hbar \left(\frac{M}{m_p R^3}\right)^{1/3}.$$

The electron's kinetic energy depends on whether it is moving slowly or fast. In the **non-relativistic** regime ($p \ll m_e c$), kinetic energy goes as $p^2/2m_e$. In the **ultra-relativistic** regime ($p \gg m_e c$), kinetic energy goes as $pc$ — a different power of $p$, and that change in exponent is what makes the limit exist.

The total electron kinetic energy is roughly $N$ times the energy per electron:

$$E_{\text{kin, NR}} \sim \frac{\hbar^2}{m_e m_p^{5/3}} \cdot \frac{M^{5/3}}{R^2}, \qquad E_{\text{kin, UR}} \sim \frac{\hbar c}{m_p^{4/3}} \cdot \frac{M^{4/3}}{R}.$$

Gravitational self-energy is $E_{\text{grav}} \sim - G M^2 / R$. The total $E = E_{\text{kin}} + E_{\text{grav}}$ tells you whether a stable size exists.

**Non-relativistic.** $E \sim A/R^2 - B/R$. There is a single minimum at finite $R$ — a stable size. The mass-radius relation has a strange consequence: *more massive white dwarfs are smaller*. Pile on mass; the star shrinks.

**Ultra-relativistic.** $E \sim A'/R - B/R$. Kinetic and gravitational terms share the *same* power of $R$. They compete only as coefficients, with no size dependence. If $A' > B$, the electrons re-enter the non-relativistic regime. If $A' < B$, $E$ decreases without bound as $R \to 0$. Gravity wins at every size. The star collapses.

The crossover $A' = B$ gives a critical mass:

$$M_{\text{Ch}} \sim \left(\frac{\hbar c}{G}\right)^{3/2} \frac{1}{m_p^2}.$$

Plug in: $\hbar c / G \approx 2.6 \times 10^{-18} \text{ kg}^2$, $m_p \approx 1.67 \times 10^{-27}$ kg, $M_{\text{Ch}} \sim 2 \times 10^{30}$ kg — about a solar mass. The careful calculation, accounting for the equation of state and the electron-per-baryon ratio of carbon-oxygen, gives

$$M_{\text{Ch}} \approx 1.4 \, M_\odot.$$

That is the Chandrasekhar limit. The cleverness is that it is built out of $\hbar$, $c$, $G$, and the proton mass — nothing else. The maximum mass of a white dwarf is fixed by four constants of nature. The same combination ($\hbar c/G$ is the Planck mass squared) sets the scale of every gravitational quantum problem.

Eddington, the leading astrophysicist of the era, refused to accept the result. At a 1935 Royal Astronomical Society meeting he called the calculation a *reductio ad absurdum* — a sign there must be a law of nature preventing the collapse ([Wali 1991](https://doi.org/10.1063/1.881290)). He was wrong. Chandrasekhar was right. The Nobel Prize came in 1983, 53 years after the steamship.

![Left: total energy versus radius. Non-relativistic case has a stable minimum. Ultra-relativistic case shows energy decreasing without bound — gravity wins. Right: white dwarf maximum stable radius shrinks to zero at 1...](../images/10-death-of-stars-fig-03.png)
*Figure 10.3 — Chandrasekhar Limit Derivation*

### Supernovae: neutron stars and black holes

When a star much more massive than the Sun (above about $8\, M_\odot$ at the main sequence) reaches the end, the core is hot enough to burn beyond helium. Carbon fuses to neon and magnesium; neon to oxygen; oxygen to silicon; silicon to iron. Each stage runs faster than the last. In a 20-solar-mass star: hydrogen $\sim 10^7$ years, helium $\sim 10^6$ years, carbon $\sim 10^3$ years, oxygen months, silicon roughly a day ([Woosley, Heger & Weaver 2002](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.74.1015)).

Iron is the wall. Binding energy per nucleon peaks near iron-56; fusing iron *costs* energy. The instant the core is iron, the furnace stops. Gravity wins in under a second.

The Earth-sized iron core collapses to a sphere about 20 km across in under a second. Outer-core infall reaches a quarter of $c$. When the inner core hits nuclear density ($\sim 2 \times 10^{17}$ kg/m³) it stiffens and rebounds. A shock propagates outward — and stalls within milliseconds, eaten up by the energy cost of dissociating still-infalling iron.

What restarts it (actively debated, see *Still puzzling*) is the neutrino flood. As protons and electrons merge into neutrons ($p + e^- \to n + \nu_e$), about $10^{46}$ J of neutrino energy is released over ten seconds. A tiny fraction reheats the stalled shock from behind. The shock revives. The outer layers are ejected at thousands of km/s.

What is left depends on the mass of the collapsing core.

**Below $\sim 3\, M_\odot$ of remnant**, neutron degeneracy pressure halts the collapse (same Pauli mechanism, applied to neutrons). The result is a **neutron star**: 10–20 km across, density $\sim 4 \times 10^{17}$ kg/m³, surface gravity $\sim 10^{12}$ times Earth's. A teaspoon would weigh a billion metric tons. The upper limit — the **Tolman-Oppenheimer-Volkoff limit** — depends on the nuclear equation of state and is observationally about $2.2\, M_\odot$ ([Cromartie et al. 2020](https://www.nature.com/articles/s41550-019-0880-2)).

**Above the TOV limit**, no known pressure stops the collapse. The remnant becomes a **black hole**. Stellar-mass black holes from 5 to 60 solar masses are routinely observed in gravitational-wave binary mergers ([Abbott et al. 2016, GW150914](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102)).

A neutron star is born spinning fast. Conservation of angular momentum during collapse — Earth-sized to 20 km — multiplies the rotation rate by $\sim 10^8$. It inherits the stellar magnetic field, compressed to $\sim 10^{12}$ tesla. Charged particles along the magnetic poles emit beamed radiation. If Earth lies in the sweeping beam, we see a regular pulse: a **pulsar**. Jocelyn Bell observed the first one as a Cambridge graduate student in November 1967 ([Hewish, Bell et al. 1968](https://www.nature.com/articles/217709a0)). The pulses arrived every 1.337 seconds with atomic-clock regularity. She and her supervisor briefly labeled the source "LGM-1" — little green men. They were dead stars.

![Schematic of the Crab Nebula — the canonical core-collapse supernova remnant from 1054 CE. Center: the Crab Pulsar, a 1.4 solar-mass neutron star 10 km across spinning at 30 Hz. Nebular luminosity ~10^5 L_sun is power...](../images/10-death-of-stars-fig-05.png)
*Figure 10.5 — Crab Nebula + Pulsar*

The Crab Nebula, expanding from the supernova that Chinese astronomers recorded as a daytime "guest star" on July 4, 1054 CE ([Stephenson & Green 2002](https://global.oup.com/academic/product/historical-supernovae-and-their-remnants-9780198507666)), contains a pulsar spinning 30 times per second. The nebula glows at $\sim 10^5$ solar luminosities — powered by the pulsar's slowing rotation. Multiply the moment of inertia of a $1.4\, M_\odot$ neutron star by the measured spin-down rate; the rotational energy loss matches the nebula's luminosity. The pulsar is the engine, the nebula what it lights up.

---

## Worked example: Type Ia supernova as a standard candle

White dwarfs near the Chandrasekhar limit explode. A white dwarf in a binary system accretes from a companion. As it approaches $1.4\, M_\odot$, the central temperature crosses carbon's ignition threshold. Because the matter is degenerate, fusion does not raise the pressure proportionally — degeneracy pressure is temperature-independent, that is the whole point. Carbon burning runs away thermally throughout the interior. The white dwarf is destroyed completely in seconds. This is a **Type Ia supernova**.

![Three panels. Left: a white dwarf accretes from a companion toward the Chandrasekhar limit, ignites carbon, and detonates in a thermonuclear runaway. Middle: raw Type Ia light curves scatter in peak brightness. Right:...](../images/10-death-of-stars-fig-06.png)
*Figure 10.6 — Type Ia Supernovae: Mechanism and Standardization*

The useful feature is uniformity. Every Type Ia explodes near the same mass with the same composition, so the peak luminosity is nearly the same event to event. The standardized peak absolute magnitude in the B band is about $M_B \approx -19.3$ ([Phillips 1993](https://articles.adsabs.harvard.edu/full/1993ApJ...413L.105P)), corresponding to $L_{\text{peak}} \approx 2 \times 10^{36}$ W — roughly $5 \times 10^9 L_\odot$, brighter than a small galaxy.

Suppose we observe a Type Ia in a distant galaxy at peak flux $F = 1.0 \times 10^{-12}$ W/m². By inverse-square, $F = L / (4 \pi d^2)$:

$$d = \sqrt{\frac{L}{4 \pi F}} = \sqrt{\frac{2 \times 10^{36}}{4 \pi \times 10^{-12}}} \approx 4 \times 10^{23} \text{ m} \approx 40 \text{ Mpc.}$$

A cosmological distance from a single brightness comparison, calibrated by physics derived from $\hbar$, $c$, $G$, and the proton mass.

In the late 1990s two teams measured Type Ia supernovae in galaxies billions of light-years away ([Riess et al. 1998](https://iopscience.iop.org/article/10.1086/300499); [Perlmutter et al. 1999](https://iopscience.iop.org/article/10.1086/307221)). They were systematically *fainter* than expected — farther than their redshifts predicted in a coasting universe. The economical explanation: the expansion is accelerating. The 2011 Nobel followed. The physics of how a star dies turned out to be the most precise distance ruler on cosmological scales.

---

## Common misconceptions

- **"A white dwarf is held up by leftover heat."** White dwarfs cool over billions of years, but their structural support is electron degeneracy pressure, which is temperature-independent. Cool one to absolute zero and it would still resist collapse. The mechanism is quantum-mechanical, not thermal.
- **"A planetary nebula is the explosion."** Planetary nebulae are slow, gentle exhalations — gas drifting outward at tens of km/s over thousands of years, lit by UV from the exposed hot core. Supernovae eject material at thousands of km/s and outshine entire galaxies. Different events, different remnants.
- **"Supernovae are powered by the rebound shock."** The bounce shock alone stalls. *Neutrino heating* of the post-shock region delivers the energy that drives the ejection. Details are not fully settled — see *Still puzzling*.
- **"All supernovae leave neutron stars or black holes."** Type Ia leave nothing — the white dwarf is destroyed completely. Only core-collapse (Type II, Ib, Ic) supernovae leave compact remnants. Hydrogen-line presence in the spectrum distinguishes them: Type II has hydrogen (massive-star envelope), Type Ia does not.
- **"The Chandrasekhar limit is the maximum mass of any star."** It is the maximum mass of a *white dwarf*. Main-sequence stars can be far more massive — the most massive observed are around $200\, M_\odot$ ([Crowther et al. 2010](https://academic.oup.com/mnras/article/408/2/731/1071189)). The limit governs the endpoint, not the starting line.

![Iron core forms, collapses to about 20 km at 0.25c, rebounds at nuclear density, the shock stalls and is revived by a neutrino burst, then the envelope is ejected and a neutron star or black hole remains.](../images/10-death-of-stars-fig-04.png)
*Figure 10.4 — Core-Collapse Sequence*

---

## Exercises

**Warm-up (Understand).** One sentence each: (a) what holds a white dwarf against gravity; (b) what holds a neutron star against gravity; (c) what happens when a remnant exceeds the TOV limit.

**Application (Apply).** A white dwarf has mass $0.6\, M_\odot$ and radius $9 \times 10^6$ m. (a) Compute its average density. (b) Compute the surface gravity. (c) State both as ratios to Earth's ($\bar\rho \approx 5500$ kg/m³, $g \approx 9.8$ m/s²).

**Synthesis (Analyze).** The Crab pulsar: $M = 1.4\, M_\odot$, $R = 10$ km, period $P = 33$ ms. (a) Compute the rotational kinetic energy ($I = \frac{2}{5} M R^2$). (b) The Crab Nebula radiates $\sim 5 \times 10^{31}$ W. If all of that came from spin-down, how long until the pulsar stops? (c) The measured spin-down age is $\sim 1300$ years; the supernova happened 970 years ago. Comment.

**Challenge (Analyze).** A binary contains a $1.38\, M_\odot$ white dwarf accreting at $\dot M = 10^{-8} \, M_\odot$/yr. (a) Estimate the time to reach the Chandrasekhar limit. (b) State one observable in the meantime (hint: classical novae). (c) State one observable at the moment the limit is crossed.

---

## LLM Exercises

### Build the stellar death router (`10-stellar-death-router.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A D3 v7 visualization with a slider for progenitor zero-age-main-sequence mass from $0.5\, M_\odot$ to $80\, M_\odot$. A schematic flowchart shows the path: helium flash and red giant $\to$ planetary nebula + white dwarf for low mass; advanced burning $\to$ iron core $\to$ core collapse $\to$ neutron star or black hole for high mass. The endpoint highlights as the slider moves.
>
> **Say.** Two panels. Left: slider plus a flowchart of fates. Right: progenitor mass (log scale, 1–80 $M_\odot$) horizontal and remnant mass vertical. Piecewise remnant curve: $0.5$–$8\, M_\odot \to$ white dwarf rising from $0.5$ to $1.4\, M_\odot$; $8$–$25\, M_\odot \to$ neutron star near $1.4$–$2.2\, M_\odot$; $> 25\, M_\odot \to$ black hole rising from $\sim 5$ to $\sim 30\, M_\odot$. Horizontal dashed lines at $1.4$ ("Chandrasekhar") and $2.2$ ("TOV"). [verify: standard initial-final mass relation for the neutron-star and black-hole branches]
>
> **Constrain.** D3 v7 only. Filename: `10-stellar-death-router.html`. Slider updates the endpoint and the marker in real time.
>
> **Verify.** (a) $1\, M_\odot$ $\to$ planetary nebula + white dwarf at $\sim 0.6\, M_\odot$. (b) $15\, M_\odot$ $\to$ core-collapse supernova + neutron star at $\sim 1.5\, M_\odot$. (c) $40\, M_\odot$ $\to$ core-collapse supernova + black hole at $\sim 10\, M_\odot$, marker above both dashed limit lines.

### Exploration

- Slide across the boundary at $8\, M_\odot$. The remnant mass jumps discontinuously even though the progenitor mass is continuous. Why? (Hint: the iron-core-collapse pathway turns on between these values.)
- The Chandrasekhar limit is one horizontal line on this plot, but it does two jobs: it sets the white-dwarf / neutron-star boundary in progenitor space *and* it sets the mass at which an accreting white dwarf is destroyed as a Type Ia. One constant, two roles.
- The neutron-star branch is nearly flat near $1.4\, M_\odot$ regardless of progenitor mass between 8 and ~25 $M_\odot$. The remnant mass is set by the nuclear equation of state, not by how much sat outside.

### Bridge to Chapter 11

> **Show.** Three remnants. The third — the black hole — does something neither of the others does: it bends spacetime so steeply that a path back out does not exist. Chapter 11 is about how general relativity describes that.
>
> **Say.** Add a second tab: plot the Schwarzschild radius $r_s = 2GM/c^2$ vs. remnant mass from $1$ to $100\, M_\odot$. Overlay each remnant's physical radius at a representative mass: white dwarf $\sim 6 \times 10^6$ m, neutron star $\sim 10^4$ m, black hole at exactly $r_s$.
>
> **Verify.** A $10\, M_\odot$ black hole has $r_s \approx 30$ km, comparable to a neutron star. The Sun, compressed to a black hole, would fit inside Boston.

Save as `10b-schwarzschild-preview.html`. Lead-in to Chapter 11 — *Black Holes and Curved Spacetime*.

---

## What would change my mind

The dividing-line value of $1.4\, M_\odot$ for the Chandrasekhar limit is a derived number — it follows from $\hbar$, $c$, $G$, $m_p$, and an assumption about electron-to-baryon ratio. A reproducible observation of a stable, non-accreting, isolated white dwarf with mass clearly above $1.5\, M_\odot$ — confirmed by independent spectroscopic and gravitational-redshift mass measurements, with no rapid rotation or strong magnetic field invoked as a structural rescue — would force a serious rewriting of this chapter. ([Howell et al. 2006](https://www.nature.com/articles/nature05103) reported a "super-Chandrasekhar" Type Ia progenitor inferred from SN 2003fg; the natural reading is rapid rotation rather than a true violation, but the case is the closest thing to a real challenge so far.) Watch this question; the limit is calculated, not assumed, and that means it is in principle falsifiable.

## Still puzzling

- *The supernova problem.* Three-dimensional simulations of core collapse with full neutrino transport are right at the edge of producing explosions reliably. Some succeed, some fail; success often depends on the nuclear equation of state, neutrino opacities, or turbulent dynamics behind the stalled shock ([Janka 2012](https://www.annualreviews.org/doi/10.1146/annurev-nucl-102711-094901); [Burrows & Vartanyan 2021](https://www.nature.com/articles/s41586-021-03790-y)). The general mechanism — neutrino-driven revival of a stalled shock — is broadly accepted; the specifics of why a particular star explodes when it does are not.
- *Where the heaviest elements come from.* The 2017 LIGO-Virgo detection of the neutron-star merger GW170817 ([Abbott et al. 2017](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.119.161101)) and its kilonova afterglow ([Kasen et al. 2017](https://www.nature.com/articles/nature24453)) made a strong case that mergers contribute substantially — perhaps dominantly — to r-process production of gold, platinum, and uranium. Whether core-collapse supernovae are a major or minor r-process site is now an open question rather than the settled answer textbooks used to give.

---

**Tags:** stellar evolution, white dwarf, Chandrasekhar limit, electron degeneracy, supernova, SN 1987A, neutron star, pulsar, black hole, nucleosynthesis
