# Chapter 4 — The Solar System

*A two-zone disk, frozen four and a half billion years ago, still readable in the stones it left behind.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** State the two-zone structure of the solar system (terrestrial vs. giant planets) and explain why a single temperature boundary — the frost line — produces it.
2. **(Understand)** Name the major populations of small bodies (asteroids, comets, Kuiper Belt objects, Oort Cloud objects) and the IAU 2006 criteria that distinguish planets from dwarf planets.
3. **(Apply)** Estimate the frost line's position from the equilibrium-temperature condition and the Sun's luminosity.
4. **(Apply)** Compute the solar system's age from the uranium-to-lead ratio in a CAI grain.
5. **(Analyze)** Diagnose what the solar nebula hypothesis predicts versus what it cannot yet explain (planetary migration timescales, Late Heavy Bombardment).
6. **(Apply)** Build a D3 simulation of a protoplanetary disk evolving into planetesimals, with a frost-line marker that correctly sorts rocky from icy worlds.

---

## Opening case: a stone over Chihuahua, February 1969

At about 1:05 a.m. local time on 8 February 1969, a fireball broke up over the state of Chihuahua, Mexico, scattering blackened lumps across roughly fifty square kilometers near the village of Pueblito de Allende ([NASA Cosmic Dust & Meteorite Catalog](https://curator.jsc.nasa.gov/antmet/index.cfm) [verify]). The Smithsonian and a NASA team arrived within days and collected something like two metric tons of stone before it could weather. Allende is the most-studied meteorite in human history.

Cut a piece open and polish it. Embedded in the dark carbon-rich matrix are small, pale, irregular blebs — millimeter to centimeter across — made mostly of calcium, aluminum, titanium, and oxygen. These are **calcium-aluminum-rich inclusions**, CAIs: the first solid material that condensed from the cooling solar nebula. Older than the planets, older than the Sun's main-sequence ignition, older than anything else we can hold.

Measure the ratios of uranium isotopes to their lead daughter products in a CAI from Allende and the number you get is 4.5682 ± 0.0003 billion years ([Connelly et al., 2012, *Science* 338, 651](https://www.science.org/doi/10.1126/science.1226919)). That is the age of the solar system, with an uncertainty of less than three parts in ten thousand. A stone fell on a paddock in Mexico, and we read off the date the solar system was assembled.

This chapter is about how that works. Two questions: *what* the solar system contains, and *how* the contents got arranged. Both have one answer — a rotating disk of gas and dust around a young star, where temperature decided what could freeze and gravity did the rest. We will not tour the planets one by one. The architecture is what matters, and the architecture is what you need for the rest of this book.

---

## Core concept I — what is out there

The Sun holds about 99.8% of the solar system's mass ([NASA Sun Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html) [verify]). Jupiter is most of the remaining 0.2%. Everything else — every other planet, moon, asteroid, comet, grain of dust — fits in the scraps. We live on a scrap.

The eight major planets split sharply into two populations.

**Terrestrial planets.** Mercury, Venus, Earth, Mars. Small, dense, rocky, with solid surfaces. Silicate minerals and iron-nickel metal. Diameters 4,900–12,800 km. Orbits 0.4–1.5 AU.

**Giant planets.** Jupiter, Saturn, Uranus, Neptune. Large, low-density, mostly hydrogen and helium with significant water, methane, and ammonia. No solid surface — gas to supercritical fluid to a small dense core as you descend. Jupiter alone could swallow the four terrestrials three hundred times over. Orbits 5.2–30 AU.

Between the two populations sits the **main asteroid belt**: rocky and metallic bodies that never coalesced, gravitationally stirred by Jupiter. Total mass about 4% of the Moon's. Beyond Neptune is the **Kuiper Belt**, a disk of icy bodies from 30 to 50 AU. Beyond *that*, in a spherical shell out to perhaps 100,000 AU, is the hypothesized **Oort Cloud** — a comet reservoir so diffuse we infer it from where long-period comets come *from*, not from direct imaging.

And then there are the **dwarf planets**, of which Pluto is now the famous example. The 2006 vote of the International Astronomical Union ([IAU Resolution B5, 2006](https://www.iau.org/static/resolutions/Resolution_GA26-5-6.pdf) [verify]) defined a planet as a body that (1) orbits the Sun, (2) has enough self-gravity to pull itself into hydrostatic equilibrium (a roughly spherical shape), and (3) has cleared the neighborhood around its orbit. Pluto satisfies (1) and (2) but fails (3) — it shares the Kuiper Belt with thousands of comparable bodies, including Eris, Haumea, and Makemake.

Pluto was not demoted for being small. Mercury is smaller than Ganymede, and Mercury is still a planet. Pluto was demoted because the 2005 discovery of Eris ([Brown et al., 2005, *ApJL* 635, L97](https://iopscience.iop.org/article/10.1086/499336) [verify]) — slightly more massive than Pluto — forced the IAU to either admit Eris as a tenth planet or draw a line. They drew the line.

Every category here is a checkpoint on one assembly line, frozen at a different stage. To see why, we need to know how the line worked.

---

## Core concept II — the frost line and the two-zone solar system

The cleanest single fact about the solar system is the two-zone split: rocky in close, giant farther out. That split is not a coincidence. It is the fossil of a temperature boundary in the disk the planets formed from.

A young star is surrounded by a **protoplanetary disk** — a flattened, rotating cloud of gas (mostly hydrogen and helium) and dust (silicate grains and ices) that did not fall onto the star because angular momentum kept it spread out. The dust starts as micrometer-sized grains, sticks into pebbles, accumulates into kilometer-sized **planetesimals** (literally "little planets" — the things planets grow from), and then planetesimals collide and merge gravitationally into protoplanets and finally planets.

The disk is hotter close to the star and cooler farther out. At distance $r$ from a star of luminosity $L_\star$, a grain in radiative equilibrium reaches a temperature roughly

$$T_\text{eq}(r) \approx \left( \frac{L_\star}{16 \pi \sigma r^2} \right)^{1/4} \propto r^{-1/2}$$

where $\sigma$ is the Stefan-Boltzmann constant. The exact prefactor depends on the grain's albedo and emissivity; the *scaling* — $T_\text{eq} \propto r^{-1/2}$ — is robust.

Water ice condenses, in the partial-pressure conditions of a protoplanetary disk, at about 150–170 K. The **frost line** — sometimes called the snow line — is the distance at which $T_\text{eq}$ drops below that condensation threshold. Inside the frost line, water stays gaseous and cannot stick to growing planetesimals. Outside, water freezes onto grains and becomes a building material.

This single boundary explains the two-zone split. Inside the frost line, planetesimals are built only from refractory materials — silicates and metals. There is not much of that by mass, so the terrestrial planets stay small. Outside, planetesimals can use ice as well as rock, roughly doubling the available solid mass. Outer-disk cores grow much larger, much faster. When a core reaches roughly ten Earth masses, its escape velocity exceeds the thermal velocity of nearby hydrogen and helium. It captures gas runaway-style, and you get a giant planet: a small rocky-icy core wrapped in a vast hydrogen-helium envelope.

One temperature, one phase transition, and the entire architecture follows.

---

## Worked example: where the frost line sits

The young Sun was about 70% of its present luminosity ([Gough, 1981, *Solar Physics* 74, 21](https://link.springer.com/article/10.1007/BF00151270) [verify]), so $L_\star \approx 2.7 \times 10^{26}$ W. Set $T_\text{cond} \approx 170$ K, $\sigma = 5.67 \times 10^{-8}$ W m⁻² K⁻⁴, and solve $T_\text{eq} = T_\text{cond}$:

$$r_\text{frost} = \sqrt{\frac{L_\star}{16 \pi \sigma T_\text{cond}^4}}$$

Plug in: $T_\text{cond}^4 \approx 8.35 \times 10^8$ K⁴; $16\pi\sigma \approx 2.85 \times 10^{-6}$; denominator $\approx 2.38 \times 10^3$ W m⁻²; ratio $\approx 1.13 \times 10^{23}$ m²; $r_\text{frost} \approx 3.4 \times 10^{11}$ m $\approx$ **2.3 AU**.

The literature places the early frost line slightly farther out (2.7–3.0 AU); the real disk had finite optical depth and lower water partial pressures. Order of magnitude is what matters: between Mars (1.5 AU) and Jupiter (5.2 AU), with the asteroid belt straddling the line. Mars is the outermost rocky planet. Jupiter is the innermost giant.

**The lesson.** A single equation — the radiative-equilibrium temperature in a disk — predicts the most prominent feature of the solar system. The same physics that gives you a grain's temperature in a lab gives you the boundary that decides what kind of world Earth will be.

**The limit.** This assumes a static, optically thin disk. Real disks evolve — accretion heating dominates while gas flows in; the frost line moves inward as the disk cools. Recent work has it sweeping from beyond 5 AU at disk formation to about 1 AU by gas dispersal ([Martin & Livio, 2012, *MNRAS* 425, L6](https://academic.oup.com/mnrasl/article/425/1/L6/981660) [verify]). Earth may have formed at a location that was inside the frost line at the end but outside it earlier — one proposed solution to how Earth got its water.

---

## Core concept III — the solar nebula hypothesis, from Kant to ALMA

The idea that the solar system formed from a rotating cloud of gas and dust is older than the evidence that confirmed it. Kant proposed it in 1755; Laplace gave it a mathematical version in 1796. A slowly rotating cloud, contracting under gravity, must spin faster (conservation of angular momentum) and flatten into a disk in which planets condense. For two centuries this floated as the most plausible story without being decisively confirmed.

What confirmed it, finally, was a photograph.

In 2014 the **Atacama Large Millimeter Array** (ALMA), 66 radio dishes on the Chilean Altiplano, imaged the disk around HL Tauri, 450 light-years away ([ALMA Partnership et al., 2015, *ApJL* 808, L3](https://iopscience.iop.org/article/10.1088/2041-8205/808/1/L3) [verify]). HL Tau is about a million years old. The image showed a flat, rotating dust disk with multiple concentric bright rings separated by dark gaps — orbital lanes already cleared by planet-mass bodies. Roughly the size of our solar system.

That image is what the solar nebula hypothesis looks like when it is right. ALMA has since imaged dozens more disks with the same structure ([DSHARP survey, Andrews et al., 2018, *ApJL* 869, L41](https://iopscience.iop.org/article/10.3847/2041-8213/aaf741) [verify]). The geometry is generic.

N-body simulations fill in the dynamics — gap-carving, migration of giants, and the catastrophes that shape the inner system. The most famous catastrophe happened to Earth. About 4.5 Ga, the mostly-assembled Earth was struck obliquely by a Mars-sized body, **Theia**; the debris coalesced into the Moon ([Canup, 2012, *Science* 338, 1052](https://www.science.org/doi/10.1126/science.1226073) [verify]). Apollo samples have nearly identical oxygen-isotope ratios to Earth's mantle (same orbital zone), the Moon is iron-depleted (Theia hit after Earth's iron had sunk), and the Earth-Moon angular momentum is what a giant oblique impact would deposit. We did not invent Theia to explain the Moon — we worked backward from measurements that did not fit any other story.

The **Nice model** ([Tsiganis et al., 2005, *Nature* 435, 459](https://www.nature.com/articles/nature03539) [verify]) proposes that Jupiter and Saturn formed closer together than now; a slow resonance pushed Neptune and Uranus past each other, scattering icy Kuiper Belt planetesimals inward. Some hit the Moon, leaving impact basins dated to about 3.9 Ga — the **Late Heavy Bombardment** (LHB).

The LHB is contested. The original evidence — Apollo sample ages clustering at 3.9 Ga — has been partly explained as a sampling bias (most samples come from a single basin's ejecta) ([Boehnke & Harrison, 2016, *PNAS* 113, 10802](https://www.pnas.org/doi/10.1073/pnas.1611535113) [verify]). I find the spike version under pressure but not falsified; the gentler-taper version is gaining ground. An active fight.

---

## Worked example: dating the solar system from a CAI

Now let me show you how the 4.568-Ga number comes out of a stone.

The most precise method is **lead-lead (Pb-Pb) dating**. Uranium has two long-lived radioactive isotopes: $^{238}$U decays to $^{206}$Pb with a half-life of 4.4683 Ga; $^{235}$U decays to $^{207}$Pb with a half-life of 0.7038 Ga. For any closed-system sample,

$$\frac{^{206}\text{Pb}_\text{rad}}{^{238}\text{U}} = e^{\lambda_{238} t} - 1$$

with $\lambda_{238} = \ln 2 / 4.4683$ Ga $\approx 0.1551$ Ga⁻¹. Same form for $^{207}$Pb and $^{235}$U with $\lambda_{235} \approx 0.9849$ Ga⁻¹.

The trick is to divide the two equations. The present-day uranium ratio $^{235}\text{U}/^{238}\text{U} \approx 1/137.88$ is constant across the solar system, so

$$\frac{^{207}\text{Pb}_\text{rad}}{^{206}\text{Pb}_\text{rad}} = \frac{1}{137.88} \cdot \frac{e^{\lambda_{235} t} - 1}{e^{\lambda_{238} t} - 1}$$

One equation, one unknown $t$. Solve numerically.

The measured radiogenic ratio for an Allende CAI is approximately 0.6271 ([Connelly et al., 2012](https://www.science.org/doi/10.1126/science.1226919) [verify]). At $t = 4.5682$ Ga: $e^{\lambda_{235} t} - 1 \approx 89.0$ and $e^{\lambda_{238} t} - 1 \approx 1.031$. Ratio $\approx 86.3$; divide by 137.88, get 0.6260. That matches the measurement within experimental error. The age is 4.568 Ga, from one equation with no fitting parameters.

The method requires no initial uranium amount and no chemical assumption — only that the CAI has been a closed system since it crystallized. CAIs condensed directly from nebula gas and sat inside parent asteroids never hot enough to melt them. Closed system, near-perfect.

**The lesson.** We date the solar system with fossils from the solar nebula. Find a CAI, measure four numbers ($^{204}$Pb, $^{206}$Pb, $^{207}$Pb, $^{238}$U), read off the age. Among the most precise measurements in any natural science.

**The limit.** 4.568 Ga is the age of the *oldest CAIs*. Other events happened later — chondrules form 1–4 Ma after CAIs; the Moon-forming impact was perhaps 50–100 Ma after; the LHB (if it happened in the spike form) around 3.9 Ga. The CAI age is the *start* of the solar system, not a summary of it.

---

## Common misconceptions

**"Pluto was demoted because it's small."** No. Mercury is smaller than Ganymede and Titan, both moons, and Mercury is still a planet. Pluto was demoted because it shares its orbital zone with thousands of comparable Kuiper Belt objects, failing the "cleared its neighborhood" criterion. Orbital dominance is what matters, not size.

**"The asteroid belt is densely packed."** Hollywood is wrong about this. The belt's total mass is about 4% of the Moon's, spread over a volume billions of times larger. Mean spacing between asteroids larger than a kilometer is more than a million kilometers. Every probe that has flown through — Pioneer 10 and 11, Voyager 1 and 2, Galileo, Cassini, New Horizons — has reached the other side without needing to dodge anything.

**"Comets come from interstellar space."** Most are bound to the Sun. Short-period comets (orbits under 200 years) come from the Kuiper Belt; long-period comets come from the Oort Cloud, perhaps 50,000–100,000 AU out. Truly interstellar comets have been detected only twice: 1I/'Oumuamua (2017) and 2I/Borisov (2019) ([Meech et al., 2017, *Nature* 552, 378](https://www.nature.com/articles/nature25020) [verify]). The comets in your telescope are locals.

**"The solar system formed all at once."** It assembled over tens of millions of years. CAIs first, chondrules a few Ma later, planetesimals, protoplanets, giant planets, terrestrial planets (Earth reached final mass 30–100 Ma after CAIs), Moon-forming impact, giant-planet migration. "4.568 Ga old" is shorthand for "the oldest solids in it are 4.568 Ga" — a start date, not a summary.

---

## Exercises

**Warm-up (Understand).** List the eight planets in order of distance from the Sun, mark each as terrestrial or giant, and state what dominates the composition of each category and why distance produced that split.

**Apply.** Estimate the frost line for a young star at $L_\star = 0.5 L_\odot$, then at $L_\star = 4 L_\odot$ (use 170 K condensation). What does this imply about where giants form around different stellar masses?

**Apply.** A CAI has $^{207}\text{Pb}/^{206}\text{Pb}_\text{rad} = 0.5800$. Using $\lambda_{238} = 0.1551$ Ga⁻¹, $\lambda_{235} = 0.9849$ Ga⁻¹, and $^{235}\text{U}/^{238}\text{U} = 1/137.88$, estimate the age. (Iterate from 4.5 Ga.)

**Analyze.** Name three independent observational tests — from lunar samples, terrestrial zircons, Mars, or asteroid ages — that could distinguish the LHB spike scenario from a smoothly tapering impact flux.

**Challenge (Synthesize).** The frost line sits at ~2.3 AU; Earth is at 1 AU. Propose two physically distinct hypotheses for where Earth's water came from, state what evidence would distinguish them, and explain why the question is still open. (Hint: D/H ratios.)

---

## LLM Exercises

### Build the protoplanetary-disk simulator (`04-solar-system-formation.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A protoplanetary disk evolving from a uniform dust-and-gas distribution to a system of planetesimals and protoplanets, with a visible frost-line marker.
>
> **Say.** Build an interactive D3 simulation. The disk extends from 0.3 AU to 30 AU around a young Sun. Over ~60 seconds of real time (= 10 Myr simulated), dust coagulates into pebbles, pebbles into planetesimals, planetesimals into protoplanets. A vertical dashed line marks the frost line at ~3 AU. Inside, bodies are brown/red (rocky); outside, white/blue (icy). When a body outside the frost line reaches ~10 Earth masses, it accretes a gas envelope and becomes a giant.
>
> **Constrain.** D3 v7. Top-down 2D view. Frost line labeled "FROST LINE: T = 170 K, water ice condenses outside." Three real-time readouts: number of planetesimals (>1 km), protoplanets (>1000 km), giants (>10 M_Earth + envelope). Physical constraint: bodies inside the frost line cannot become giants regardless of core mass. Filename: `04-solar-system-formation.html`.
>
> **Verify.** (a) At end: inside the frost line, 2–5 terrestrial-mass bodies; outside, at least one body that crossed 10 Earth masses and gained an envelope. (b) Frost line marker at 3 AU. (c) Planetesimal stage completes in the first 10–20% of the run; giant-planet stage by 50%.

### Exploration

- Vary disk mass. Below what threshold does the system fail to make any giant? Above what threshold does it make multiple giants?
- Move the frost line inward to 1 AU. Does Earth's orbit now form a giant? Connect to why hot Jupiters are common around fainter stars.
- Move the frost line outward to 10 AU. Is there still an analog to the terrestrial zone?

### Extension prompt (chapter bridge)

> Add an inset panel showing the central star's luminosity over time. Pre-main-sequence dimming, then a sharp transition at hydrogen ignition (~30–50 Myr after disk formation). Final stellar mass should be ~99.8% of the total system mass.

Save as `04b-sun-ignition-preview.html`. Lead-in to Chapter 5.

---

## AI Wayback Machine

The ideas in this chapter didn't appear from nowhere. **Clair Patterson** measured the age of the Earth in 1956 by analyzing lead isotopes in primitive meteorites, settling the question at about 4.55 billion years — within the uncertainty of the modern CAI measurement. The work led him to discover the staggering scale of lead contamination from leaded gasoline. He spent the next thirty years fighting to get tetraethyl lead out of fuel.

**Run this:**

```
Who was Clair Patterson, and how does his lead-isotope dating of meteorites connect to the modern CAI age of the solar system? Three paragraphs. End with the single most surprising thing about his career.
```

→ Search **"Clair Cameron Patterson"** on Wikipedia. See what the model got right, wrong, or left out.

**Now make the prompt better.** Either ask it to walk through Patterson's 1956 lead-lead method step by step in plain numbers, or add a constraint: "Answer as Patterson's 1965 Senate testimony on the health risk of leaded gasoline." What changes?

---

## What would change my mind

The central claim — that the solar system formed from a rotating gas-and-dust disk, that a single temperature boundary produced the two-zone architecture, and that the system is 4.568 Ga old — would be forced into serious revision by any of these: (1) a CAI age outside the 4.55–4.58 Ga range from two or more independent isotopic systems; (2) a protoplanetary disk clearly lacking the rocky-inside/icy-outside pattern; (3) a demonstration that the giant planets formed by direct gravitational instability rather than core accretion (a live debate for the outermost giants). The strongest current tension is the LHB timing — new lunar samples from Chang'e 5 and 6 may force a revision of the Nice-model spike scenario within the next decade.

## Still puzzling

- *Where did Earth's water come from?* The frost line calculation says Earth's zone was too hot for local water ice. The standard answer is volatile-rich planetesimals — comets, hydrated asteroids — delivering water late. The deuterium-to-hydrogen ratio in Earth's oceans matches some carbonaceous chondrites better than Oort comets, which complicates the picture. The mix of sources is not settled.
- *Was there a Late Heavy Bombardment, or a smoothly tapering flux?* The Apollo evidence is consistent with a spike, but the sampling is biased toward one basin's ejecta. Chang'e far-side samples are starting to test this. I lean toward smoother decline, but the case is open.
- *Why is our solar system architecturally weird?* Exoplanet surveys show the most common planet type is a super-Earth in a tight orbit — we have none. Hot Jupiters are common; our Jupiter is far out. Either our formation was unusual, or our detection methods are biased, or both. One of the largest open problems in planet formation.

---

**Tags:** solar system, protoplanetary disk, frost line, solar nebula hypothesis, CAI dating, Allende meteorite, Pluto demotion, IAU 2006, Late Heavy Bombardment, Nice model
