# Chapter 5 — The Sun

*A million-kelvin atmosphere on top of a 5,800-kelvin surface, powered by a reaction that almost never happens.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Understand)** Name the Sun's five structural regions (core, radiative zone, convection zone, photosphere, chromosphere, corona) and the temperature and dominant physics in each.
2. **(Understand)** State the proton-proton (pp) chain in three steps and identify the weak-force bottleneck.
3. **(Apply)** Compute the Sun's fusion rate, in reactions per second and protons per second, from its luminosity and the energy per fusion.
4. **(Apply)** Estimate the Sun's remaining main-sequence lifetime from its core mass and current luminosity.
5. **(Analyze)** Diagnose why the corona's high temperature is anomalous, and explain what evidence would settle the coronal heating problem.
6. **(Apply)** Build a D3 cross-section of the Sun with an inset animating the pp chain.

---

## Opening case: an eclipse, a glow, and a number that points the wrong way

On August 21, 2017, the Moon's umbra crossed the United States from Oregon to South Carolina. For about two and a half minutes at each location, the Moon covered the Sun's bright disk and the corona — the Sun's outer atmosphere — became visible to the naked eye. It looked like a pearly halo of streamers and loops reaching several solar radii into space.

Now ask what the photographs show. The disk the Moon blocked has a temperature of about 5,800 K — the temperature of a tungsten filament about to fail. The pearly atmosphere around it, plainly farther from the Sun's center, has a temperature between 1 and 3 million K. Move *outward* from the heat source, and the temperature goes up by a factor of nearly 200.

That is not how heat works. A poker in a fire glows red at the tip, dimmer along the handle. The air a meter from a campfire is cooler than the air a centimeter away. The Sun is doing the opposite of every cup of coffee you have ever held.

This chapter is about two things at once: what the Sun is (its layered structure) and how it works (the nuclear reaction that powers it). The two are not separate problems — the temperature anomaly above the photosphere and the proton-proton reaction in the core are connected by the same plasma machine. By the end, you will be able to compute how long the Sun has left, in years, with arithmetic a sophomore can do on paper.

---

## Core concept I — structure: five layers, three transport mechanisms

The Sun has no surface in the sense a rock has a surface. It is a ball of plasma — a soup of bare nuclei and free electrons, stripped of bound states by temperature — held together by gravity. What it has is **regions where different physics dominates**. Five of them, working inward to outward.

**The core** (inner ~25% of the radius). Temperature 15 million K, density ~150 g/cm³ — about 13 times denser than lead. Fusion happens here and nowhere else.

**The radiative zone** (~25% to ~70% of the radius). Energy moves outward by radiation, but not in the way you imagine. A gamma-ray photon born in the core travels about a centimeter before scattering off an electron and being re-emitted in a random direction. It performs a random walk through plasma so dense that crossing the radiative zone takes something like 10⁵ years. The light hitting your retina now was created in the core when our species did not yet exist. [verify]

**The convection zone** (outer ~30% of the radius). At ~2 million K the plasma cools enough that atoms recombine with some of their electrons. Atoms-with-electrons absorb photons far more efficiently than bare nuclei. Radiation can no longer carry the heat outward fast enough, so the plasma carries itself: hot blobs rise, cool blobs sink, and a slow rolling boil takes over. The tops of these convection cells are visible at the surface as **granulation** — bright polygons ~1,000 km across, surrounded by darker lanes, each granule rising and dissolving in about eight minutes.

**The photosphere.** Pronounced *photo-sphere*: the layer where photons can finally escape. About 400 km thick. Temperature ~5,800 K. This is what your eye records as "the Sun." Below it the plasma is opaque; above it the plasma is thin enough that photons fly free. This is also where **sunspots** appear — patches where strong magnetic flux tubes have punched through from below and locally suppressed convection. The trapped region cools to ~3,800 K. It still emits plenty of light; it looks dark only because the surrounding 5,800 K plasma is so much brighter. Lift a sunspot out of context and it would glow bright orange.

**The chromosphere** (*chromo-sphere*: the "color sphere," named for the reddish glow visible in eclipses). A ~2,000 km transition layer above the photosphere. Temperature rises through it, from a minimum of ~4,400 K just above the photosphere to ~25,000 K at the top.

**The corona** (*corona*: Latin for "crown"). The pearly halo of the eclipse. Million-kelvin plasma extending several solar radii into space, gradually fading into the **solar wind** — a constant outflow of protons, electrons, and helium nuclei at ~400 km/s. The wind reaches Earth at densities of ~5 particles per cubic centimeter and shapes our magnetosphere.

The structure has a clock. Heinrich Schwabe, an amateur pharmacist, counted sunspots daily from 1826 onward looking for a hypothetical planet inside Mercury's orbit. He never found one. By 1843 he had spotted something better: the sunspot count rises and falls on an **11-year cycle**. Differential rotation — equator 25 days per turn, poles 36 — winds the Sun's magnetic field around itself until the field becomes unstable, breaks, and reconnects with reversed polarity. The full magnetic cycle is 22 years; sunspot counts cycle at half of that.

The puzzle that opened this section — million-kelvin corona above a 5,800-kelvin photosphere — has a name: the **coronal heating problem**. The energy must come from below; nothing else can supply it. The two leading candidates are (a) magnetic reconnection events releasing energy when tangled field lines snap to new partners, and (b) Alfvén waves — magnetic disturbances propagating up from the convection zone and dissipating in the thin upper atmosphere. Both are observed. Neither has been shown sufficient on its own. I find the reconnection picture more compelling, but the case is not closed.

---

## Core concept II — energy: how four protons become one helium

Move down through the layers to the core. Here is where the energy comes from.

The Sun radiates at **L_sun ≈ 3.828 × 10²⁶ W**. Where does this come from? Not from chemistry. If the Sun were a ball of coal, burning at its observed rate, it would last about 5,000 years. The Earth is 4.5 billion years old and the Sun is older. Chemistry is wrong by six orders of magnitude.

The answer is nuclear fusion. Specifically, the **proton-proton chain** (the pp chain), which converts four hydrogen nuclei into one helium nucleus. The net reaction:

$$4\,{}^1\text{H} \longrightarrow {}^4\text{He} + 2e^+ + 2\nu_e + \gamma$$

Released per fusion: about **26.7 MeV**, equal to $4.27 \times 10^{-12}$ J. (One electron-volt = $1.602 \times 10^{-19}$ J; "MeV" is one million of them.) Where does the energy come from? Four protons weigh slightly more than one helium-4 nucleus — by about 0.7% of their starting mass. That missing mass becomes energy by $E = mc^2$. The 0.7% is *not* released from a chemical bond; it has ceased to exist as mass.

The chain happens in three steps. Pay attention to the timescales.

**Step 1.** Two protons collide. One of them undergoes a weak-force conversion: a proton becomes a neutron, emitting a positron (the electron's antimatter twin) and a **neutrino** (a nearly-massless, nearly-non-interacting particle that escapes the Sun directly). What remains is deuterium — one proton plus one neutron.

$$p + p \longrightarrow {}^2\text{H} + e^+ + \nu_e$$

This step is the **bottleneck**. It requires the weak nuclear force, which — as the name suggests — almost never fires. The average proton in the Sun's core waits about $10^{10}$ years before this happens to it. Longer than the current age of the universe.

**Step 2.** The deuterium nucleus collides with another proton and fuses, releasing a gamma photon.

$${}^2\text{H} + p \longrightarrow {}^3\text{He} + \gamma$$

This step is fast — deuterium survives only seconds before being struck.

**Step 3.** Two helium-3 nuclei collide and fuse, producing helium-4 plus two free protons that return to the soup.

$${}^3\text{He} + {}^3\text{He} \longrightarrow {}^4\text{He} + 2p$$

Net effect of one full chain: four hydrogen nuclei in, one helium-4 out, 26.7 MeV of energy released, and a few neutrinos in flight.

A second pathway, the **CNO cycle**, uses carbon, nitrogen, and oxygen as catalysts to fuse hydrogen into helium. In the Sun, the CNO cycle contributes only about 1% of the energy; in stars more than about 1.3 solar masses, it dominates. For our Sun, the pp chain is the engine.

The bottleneck is what saves us. If step 1 were fast — if the weak force fired easily — the Sun would fuse all its hydrogen in millennia. Because step 1 is rate-limited by quantum tunneling through the proton-proton Coulomb barrier *and* by the slow weak-force conversion, the Sun shines steadily for tens of billions of years. The improbability is the feature.

After fusion, the energy makes two journeys. Neutrinos leave at nearly the speed of light through plasma that, to them, might as well be vacuum — they cross the Sun in about two seconds and reach Earth eight minutes later. The gamma photons scatter incessantly, diffusing through the radiative zone over ~10⁵ years, then ride convection cells to the surface and fly to Earth in eight minutes. **Neutrinos and photons from the same fusion event arrive 10⁵ years apart** — two messengers carrying the same news, separated by the opacity of the plasma between.

This is not theoretical. In 2001, the Sudbury Neutrino Observatory measured the total solar neutrino flux across all three flavors and matched the standard-solar-model rate to within experimental error. [verify]

---

## Worked example — how long does the Sun have left?

Given: L_sun = $3.828 \times 10^{26}$ W. Energy per pp-chain fusion: 26.7 MeV = $4.27 \times 10^{-12}$ J.

**Step 1: fusions per second.** Divide power by energy per reaction:

$$\text{Fusion rate} = \frac{3.828 \times 10^{26}\,\text{W}}{4.27 \times 10^{-12}\,\text{J}} \approx 9.0 \times 10^{37}\,\text{fusions/s}$$

About $10^{38}$ pp chains complete every second.

**Step 2: protons consumed per second.** Each fusion consumes four protons:

$$4 \times 9.0 \times 10^{37} \approx 3.6 \times 10^{38}\,\text{protons/s}$$

**Step 3: mass consumed per second.** Each proton has mass $1.67 \times 10^{-27}$ kg:

$$3.6 \times 10^{38} \times 1.67 \times 10^{-27} \approx 6.0 \times 10^{11}\,\text{kg/s}$$

About **600 million metric tons of hydrogen per second**. The "0.7% lost to radiation" piece of this, by $E = mc^2$, comes to ~$4 \times 10^9$ kg/s — four million tons disappearing as light every second.

**Step 4: how long does the available hydrogen last?** The Sun's total mass is $M_\odot \approx 2 \times 10^{30}$ kg. About 73% is hydrogen, but only the **core's** hydrogen is hot enough to fuse — roughly 10% of the Sun's mass, by helioseismology and stellar-evolution modeling. [verify] So the fusible hydrogen mass is approximately:

$$M_\text{fuse} \approx 0.10 \times 2 \times 10^{30} \approx 2 \times 10^{29}\,\text{kg}$$

Divide by the proton consumption rate (mass-wise):

$$t_\text{remaining} \approx \frac{2 \times 10^{29}\,\text{kg}}{6 \times 10^{11}\,\text{kg/s}} \approx 3.3 \times 10^{17}\,\text{s}$$

Convert to years (~$3.15 \times 10^{7}$ s/yr):

$$t_\text{remaining} \approx 10^{10}\,\text{yr}$$

About **10 billion years total**, of which 4.5 billion have already gone. The Sun has roughly **5 billion years of main-sequence life left**. This number — five billion — is the headline result for stellar lifetimes, and we just got it from L, the fusion energy, the mass of a proton, and the fraction of the Sun's hydrogen that is in the core. Four numbers and division.

**The lesson.** The Sun's lifetime is not a black box. It is L_sun divided by (energy per fusion × protons per fusion × mass per proton × accessible hydrogen fraction). When you understand the mechanism, you can do the calculation.

**The limit.** This treats L_sun as constant. It is not. The Sun has brightened by about 30% since its formation — the **Faint Young Sun paradox** is the problem that early Earth, under a dimmer Sun, should have frozen solid but evidently did not. The constant-L approximation is good to a factor of order unity for total lifetime, but the brightening matters for habitability over geological time.

---

## Common misconceptions

**"The Sun burns its fuel."** No. Burning is a chemical reaction — electrons rearranging between atoms, releasing a few eV per bond. Fusion is a nuclear reaction — protons and neutrons rearranging between nuclei, releasing millions of eV per reaction. Per reaction, fusion releases about **six orders of magnitude more energy** than burning. The Sun is not on fire in any chemical sense. The vocabulary borrowed from combustion ("burns hydrogen") is a metaphor; the physics is utterly different.

**"The corona is hot because it's closer to the Sun's interior."** It is *farther* from the interior than the photosphere is, and by simple thermodynamics it should be cooler — heat flows down a temperature gradient. That the corona is hundreds of times hotter than the photosphere is precisely the anomaly. The energy must arrive by something other than ordinary conduction or radiation from below — most likely magnetic energy released in the thin upper atmosphere by reconnection or wave dissipation. The coronal heating problem is unresolved as of 2026. [verify]

**"Sunspots are dark because they're cold."** They are *cooler* than their surroundings — ~3,800 K vs. 5,800 K — but 3,800 K is hotter than any flame on Earth. In isolation a sunspot would shine bright orange and be uncomfortable to look at. Sunspots appear dark only against the brighter photosphere. "Dark" is contrast, not absolute.

**"The Sun's energy is from gravitational contraction."** That was Thomson and Helmholtz's nineteenth-century answer, and they were not wrong about the physics — gravitational contraction *does* heat young protostars before fusion ignites. But the energy reservoir is only good for ~$10^8$ years, two orders of magnitude short of the Earth's geological age. Darwin worried about exactly this gap. Fusion closes it.

---

## Exercises

**Warm-up (Understand).** State the five regions of the Sun in order, give an approximate temperature for each, and identify which energy-transport mechanism (radiation, convection, fusion, radiation+random-walk) dominates in each.

**Apply.** Reverse the worked example. Given that the proton-proton chain releases 26.7 MeV per reaction, and assuming a star fuses hydrogen at $5 \times 10^{37}$ reactions per second, compute the star's luminosity in watts. Compare to L_sun and decide whether this star is brighter or dimmer than the Sun.

**Apply (quantum tunneling).** The Sun's core temperature is ~15 million K. The classical kinetic energy needed for two protons to surmount their mutual Coulomb barrier is ~1 GeV — roughly $10^4$ times the average thermal energy at 15 million K. Argue, in three sentences, why fusion happens anyway. (Hint: protons are not bullets; they are wave functions, and barriers can be tunneled.)

**Apply + Analyze (corona).** Predict, using ordinary thermodynamic intuition, what should happen to the temperature of the Sun's atmosphere as altitude increases above the photosphere. Then state what is actually observed (numbers, please) and identify *the smallest set of assumptions* in your intuition that must be wrong for the observation to be consistent with energy conservation. What kind of measurement would distinguish reconnection heating from Alfvén-wave heating?

**Challenge (Analyze).** Suppose tomorrow the Sun's core fusion rate doubled. By the worked example, L would double. What happens next? (Hint: pressure, gravity, hydrostatic equilibrium. The Sun is a self-correcting system. Sketch the negative feedback loop that returns it to equilibrium, and estimate the timescale on which the surface luminosity would respond — radiative-zone diffusion time, ~$10^5$ years. The Sun is robustly stable, but slowly.)

---

## LLM Exercises

### Build the solar-structure simulator (`05-sun-structure-fusion.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** The Sun in cross-section has five labeled regions: core (0–0.25 R), radiative zone (0.25–0.7 R), convection zone (0.7–1.0 R), photosphere (a thin layer at 1.0 R), chromosphere (1.0 R to ~1.003 R), and corona (extending to several R). Approximate temperatures in K: 1.5×10⁷, 7×10⁶ → 2×10⁶ across the radiative zone, 2×10⁶ → 5,800 across the convection zone, 5,800 at photosphere, 4,400 → 25,000 across the chromosphere, 1–3×10⁶ in the corona. The proton-proton chain has three steps as given above.
>
> **Say.** Build an interactive cross-section of the Sun showing the five regions, with a temperature-display toggle. Include an inset panel that animates one full proton-proton chain — step 1 (p+p → D+e⁺+ν), step 2 (D+p → ³He+γ), step 3 (³He+³He → ⁴He+2p) — with a slider to control playback speed.
>
> **Constrain.** D3 v7. Cross-section as concentric annuli, brutalist palette (gray-scale or five-color sequential). Hover region → tooltip with name, T-range, dominant physics. Toggle button: "Show temperatures." Inset (300×200 px, lower-right): three frames cycling the pp-chain steps with labeled particles. Slider: 0.1× to 5× playback. Filename: `05-sun-structure-fusion.html`.
>
> **Verify.** (a) Five region names and T-ranges match the spec within 10%. (b) Each pp-chain cycle emits one positron, two neutrinos, and one helium-4. (c) Region radii match the spec (convection zone is ~30% of the radial extent, not 30% of area).

### Exploration

- Sketch T(r) from the simulator data. Where does the slope flip sign? (Answer: just above the photosphere — the corona is the puzzle.)
- The inset runs the pp chain at constant speed. The *real* chain has step 1 taking ~$10^{10}$ years and step 2 taking ~6 seconds. Redesign the animation on a log-scaled timeline. What does the redesign teach that the constant-speed version hides?
- Find the radii where the dominant energy-transport mechanism changes. Annotate them.

### Extension prompt (chapter bridge to Chapter 6)

> **Show.** I have a cross-section of the Sun. The Sun is a G2V main-sequence star: surface temperature 5,800 K, luminosity $3.83 \times 10^{26}$ W. Other stars have different surface temperatures (Wien's law) and different luminosities (Stefan-Boltzmann), and these can be plotted against each other on a Hertzsprung-Russell diagram.
>
> **Say.** Extend the simulator: add a button "Compare to other stars" that opens a small H-R-diagram panel with the Sun marked, and lets the user click points on the main sequence to see their estimated radius, surface temperature, and approximate spectral class.
>
> **Constrain.** New file `05b-sun-vs-stars.html`. Representative main-sequence data for ~30 stars (OBAFGKM). Click → tooltip with surface T, L/L_sun, mass, lifetime. Brutalist: small markers, no glow, no gradients.
>
> **Verify.** The Sun lands at log L = 0, T ≈ 5,800 K on the diagram. Higher-mass main-sequence stars are hotter and more luminous; lower-mass main-sequence stars are cooler and less luminous. Click a few and check the lifetimes against the rough scaling $\tau \sim M^{-2.5}$ (a 2-solar-mass star lasts about $1/(2^{2.5}) \approx 1/6$ as long as the Sun).

Save as `05b-sun-vs-stars.html`. This is the bridge to Chapter 6, where we apply the Sun's machinery to the rest of the main sequence.

---

## What would change my mind

The central quantitative claim of this chapter — that the Sun's luminosity is supplied by the proton-proton chain at a rate of ~$10^{38}$ fusions per second, releasing ~26.7 MeV apiece — has been confirmed by direct measurement of the solar neutrino flux at SNO and Super-Kamiokande, which matches the rate predicted by the standard solar model to within a few percent. [verify] A reproducible measurement of the total solar neutrino flux that disagreed with the L_sun-based fusion rate by more than ~10% — across all three neutrino flavors, ruling out oscillation effects — would force the rewriting of this chapter. The qualitative picture of the corona's anomalous temperature would also be revised if a single mechanism (say, Alfvén-wave dissipation) were shown by Parker Solar Probe data to supply ≥90% of the coronal heating budget — that would close a problem currently open.

## Still puzzling

- *The coronal heating problem.* We know the energy is magnetic and arrives from below. We do not know the relative contributions of reconnection events and wave dissipation, and the answer probably varies between quiet-Sun regions and active regions.
- *The exact chromospheric heating budget.* Same family of question, one layer down. The chromosphere is the staging ground for whatever heats the corona, and its energetics are not pinned down.
- *Why the Sun's neutrino flux precisely matches the standard model.* It matches now — but it took thirty years and the discovery of neutrino mass to make the books balance. Future improvements in flux measurement (precision better than 1%) could reopen the question. [verify]

---

**Tags:** Sun, proton-proton chain, solar structure, corona, sunspots, nuclear fusion, neutrinos, coronal heating problem
