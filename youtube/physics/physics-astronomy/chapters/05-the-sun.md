# Chapter 5 — The Sun

*A million-kelvin atmosphere on top of a 5,800-kelvin surface, powered by a reaction that almost never happens.*

---

On August 21, 2017, the Moon's shadow crossed the continental United States. For about two and a half minutes at each location along the path, the Moon covered the Sun's bright disk and the corona — the Sun's outer atmosphere — became visible to the naked eye: a pearly halo of streamers and loops extending several solar radii into space.

Now look at what the photographs actually show. The disk the Moon blocked has a surface temperature of about 5,800 K. The corona surrounding it — plainly farther from the Sun's center — has a temperature between one and three million Kelvin. Move *outward* from the heat source, and the temperature jumps by a factor of nearly 200.

![Schematic of a total solar eclipse. The Moon-blocked disk is the 5,800 K photosphere; the pearly halo is the 1–3 million K corona. Moving outward from the heat source, temperature rises by 200x. Inset shows the temper...](../images/05-the-sun-fig-01.png)
*Figure 5.1 — Total Eclipse: The Million-Kelvin Atmosphere Above a 5,800-K Surface*

That is not how heat works. A poker in a fire glows red at the hot end and dim along the handle. The air a meter from a campfire is cooler than the air a centimeter away. The corona is doing the opposite of every cup of coffee you have ever let go cold. Heat flows down a temperature gradient. The Sun's outer atmosphere violates your intuition about which way is down.

This chapter is about two things at once: what the Sun is made of, layer by layer, and how it produces energy. The two problems are connected. The same plasma machine that runs nuclear reactions in the core also generates the magnetic fields that heat the corona. By the end, I want you to be able to sit down with four numbers — the Sun's luminosity, the energy per fusion, the mass of a proton, and a rough estimate of the fusible hydrogen fraction — and derive, on paper, how many years the Sun has left.

---

## Five layers, three transport mechanisms

The Sun has no surface in the sense a rock has a surface. It is a ball of plasma — nuclei and free electrons, stripped of their bound states by temperature — held in shape by gravity. What it has is regions where different physics dominates. Five of them.

**The core** occupies the inner quarter of the Sun's radius. Temperature: 15 million Kelvin. Density: about 150 g/cm³, thirteen times denser than lead. This is where fusion happens, and nowhere else. The rest of the Sun is along for the ride.

**The radiative zone** extends from 25% to 70% of the radius. Energy moves outward here by radiation, but the word "moves" is generous. A gamma-ray photon born in the core travels roughly one centimeter before scattering off a free electron and flying off in a random direction. It then travels another centimeter and scatters again. The plasma is so dense that the photon executes a random walk — equally likely to scatter inward as outward at any step. Working out how long it takes to cross the radiative zone by this drunken walk: about $10^5$ years. The sunlight reaching your eye today was produced in the Sun's core roughly when Homo erectus walked the Earth.

**The convection zone** fills the outer 30% of the radius. Around 2 million Kelvin the plasma has cooled enough that some ions can recapture electrons. Atoms with electrons absorb photons far more efficiently than bare nuclei — the opacity shoots up, and radiation can no longer carry the heat outward fast enough. So the plasma starts carrying itself. Hot blobs rise, cool blobs sink. A slow rolling boil takes over from the radiative diffusion. Look at the photosphere through a good telescope and you see the tops of these convection cells directly: bright polygons about 1,000 km across, each rising and dissolving in roughly eight minutes, surrounded by darker lanes where cool material descends. This is called granulation, and it is the Sun's weather, one layer deep.

![A quarter-cross-section of the Sun showing six concentric regions from core to corona, each with temperature ranges and dominant energy-transport mechanisms. Six orders of magnitude in temperature; three transport reg...](../images/05-the-sun-fig-02.png)
*Figure 5.2 — Solar Cross-Section: Five Layers*

<!-- → [IMAGE: High-resolution photograph of solar granulation (e.g., from DKIST or Hinode) showing the polygonal cell pattern — bright centers where hot plasma rises, dark lanes where cooler plasma descends — with a scale bar showing Earth for size comparison] -->

**The photosphere** is the layer where photons finally escape. About 400 km thick; temperature about 5,800 K. Below it the plasma is opaque; above it the plasma is thin enough for photons to fly free. This is what your eye registers as "the Sun." It is also where sunspots appear — darker patches where bundles of magnetic field have punched up from below and locally suppressed convection. The suppressed region cools to about 3,800 K. It still radiates plenty of light. It looks dark only because the surrounding 5,800 K plasma is so much brighter. Lift a sunspot out of context and it would glow bright orange.

**The chromosphere and corona** extend above the photosphere and behave paradoxically. The chromosphere — a 2,000 km transition layer — rises from a temperature minimum of about 4,400 K just above the photosphere to roughly 25,000 K at its top. The corona above that runs at one to three million Kelvin. Both defy the expectation that temperature should fall as you move away from the energy source. The energy driving this heating is magnetic. The mechanism is not settled.

<!-- → [CHART: Temperature profile T(r) from Sun's center (r = 0) to several solar radii — x-axis: radius in units of R_sun from 0 to ~3; y-axis: log temperature in Kelvin; curve drops from 1.5×10⁷ K at center through radiative zone to ~5,800 K at photosphere, then rises sharply through chromosphere to ~10⁶ K in corona; the anomalous upturn above the photosphere should be visually prominent; regions labeled; student should see the temperature inversion clearly] -->

The structure has a clock. In the 1840s, an amateur German pharmacist named Heinrich Schwabe spent seventeen years counting sunspots daily, looking for a hypothetical planet inside Mercury's orbit. He never found the planet. What he found was that sunspot counts rise and fall on an eleven-year cycle. The explanation involves differential rotation: the Sun's equator completes a rotation every 25 days while its poles take 36 days. This shear winds the Sun's magnetic field around itself over years until the field becomes tangled and unstable, breaks, and reconnects with reversed polarity. The full magnetic cycle — field building, breaking, and rebuilding with opposite polarity — is 22 years; the sunspot cycle is half of that, because sunspots form during both halves.

![Annual sunspot count 1700–2026, showing the 11-year periodic oscillation. The Maunder Minimum (1645–1715) is the long quiet gap before instruments resolved it. Schwabe's discovery period 1826–1843 and Solar Cycle 25 p...](../images/05-the-sun-fig-06.png)
*Figure 5.6 — Schwabe's 11-Year Sunspot Cycle*

---

## How four protons become one helium nucleus

Move down through all those layers to the core. This is where the energy comes from.

The Sun radiates at $L_\odot \approx 3.828 \times 10^{26}$ W. Where does this come from?

Not from chemistry. If the Sun were a ball of coal burning at its observed rate, it would last about 5,000 years. The Earth's rocks contain fossils 500 million years old. The chemistry answer is wrong by five orders of magnitude.

Not from gravitational contraction. In the 1800s, William Thomson (Lord Kelvin) and Hermann von Helmholtz independently worked out that a contracting gas cloud could release gravitational potential energy as heat. The Sun could shine for about $10^7$ to $10^8$ years this way. Charles Darwin needed at least $10^8$ years for evolution; the geologists needed more. The gravitational answer was close but not close enough.

The answer is nuclear fusion. Specifically, the **proton-proton chain**: the conversion of four hydrogen nuclei into one helium nucleus. The net reaction is:

$$4\,{}^1\text{H} \longrightarrow {}^4\text{He} + 2e^+ + 2\nu_e + \gamma$$

Four protons weigh slightly more than one helium-4 nucleus — by about 0.7% of the total starting mass. That mass difference does not go somewhere else. It ceases to exist as mass and becomes energy by $E = mc^2$. Released per complete chain: about 26.7 MeV, equal to $4.27 \times 10^{-12}$ J.

The chain happens in three steps. The timescales are the point.

**Step 1.** Two protons collide. One undergoes a weak-force conversion: it becomes a neutron, emitting a positron and a neutrino. The result is deuterium — one proton, one neutron.

$$p + p \longrightarrow {}^2\text{H} + e^+ + \nu_e$$

This step is the bottleneck. It requires the weak nuclear force, which fires rarely. The average proton in the Sun's core waits about $10^{10}$ years — longer than the current age of the universe — before this reaction happens to it. But there are about $10^{57}$ protons in the Sun's core, so the rare event happens constantly in aggregate.

**Step 2.** The deuterium collides almost immediately with another proton and fuses, releasing a gamma-ray photon.

$${}^2\text{H} + p \longrightarrow {}^3\text{He} + \gamma$$

Deuterium survives only about six seconds in the solar core before this happens.

**Step 3.** Two helium-3 nuclei meet and fuse, producing helium-4 and returning two free protons to the pool.

$${}^3\text{He} + {}^3\text{He} \longrightarrow {}^4\text{He} + 2p$$

Net balance: four protons in, one helium-4 and 26.7 MeV out, plus neutrinos that leave immediately.

<!-- → [INFOGRAPHIC: Three-panel diagram of the pp chain — panel 1: two protons colliding, producing deuterium + positron + neutrino; panel 2: deuterium + proton producing helium-3 + gamma; panel 3: two helium-3 nuclei producing helium-4 + two protons; arrows showing net result: 4H → He-4 + energy; timescales labeled: step 1 ~10¹⁰ years, step 2 ~6 seconds, step 3 fast] -->

![Three sequential panels: weak-force decay produces deuterium (10^10 year average wait per proton), deuterium captures a proton to make helium-3 (seconds), two helium-3s fuse to helium-4 returning two protons. Net: fou...](../images/05-the-sun-fig-03.png)
*Figure 5.3 — Proton-Proton Chain in Three Steps*

The slow step is what makes the Sun's existence possible in its current form. If the weak force fired easily — if step 1 were fast — the Sun would consume its hydrogen in a few thousand years. Because the weak force is genuinely weak, the Sun can shine steadily for billions of years. The rarity of the reaction is not a defect in the design; it is the reason the design works.

A second fusion pathway exists: the **CNO cycle**, which uses carbon, nitrogen, and oxygen as catalysts. In the Sun, it contributes about 1% of the energy. In more massive stars — above about 1.3 solar masses — higher core temperatures favor the CNO cycle and it dominates. For our Sun, the pp chain is almost everything.

After the energy is released, it makes two completely different journeys to the surface. Neutrinos leave at close to the speed of light through plasma that is, to them, effectively transparent. They cross the Sun in about two seconds and reach Earth eight minutes after that. The gamma photons scatter endlessly through the radiative zone, diffusing outward over $10^5$ years, then convect to the surface and reach Earth in eight minutes. Neutrinos and photons from the same fusion event arrive at Earth separated by a hundred thousand years. The same event, two messengers, one of them in the distant past.

![Two messengers from the same fusion event. The neutrino flies straight through the Sun in 2 seconds and reaches Earth 8 minutes later. The photon random-walks through the radiative zone for ~10^5 years, rides convecti...](../images/05-the-sun-fig-04.png)
*Figure 5.4 — Photon vs Neutrino Race from the Core*

This is directly testable. The Sudbury Neutrino Observatory measured the total solar neutrino flux across all three flavors (solving the "solar neutrino problem" — an earlier apparent deficit that turned out to be neutrinos oscillating between types in transit) and found agreement with the standard-solar-model prediction to within a few percent. The Sun really is burning hydrogen at the rate its luminosity implies.

---

## How long does the Sun have left?

This is arithmetic, not a mystery. Let me work through it.

**Fusions per second.** The Sun emits $3.828 \times 10^{26}$ W. Each pp-chain fusion releases $4.27 \times 10^{-12}$ J. Divide:

$$\text{fusion rate} = \frac{3.828 \times 10^{26}}{4.27 \times 10^{-12}} \approx 9 \times 10^{37}\,\text{fusions/s}$$

Nearly $10^{38}$ complete pp chains every second.

**Protons consumed per second.** Each fusion burns four protons:

$$4 \times 9 \times 10^{37} \approx 3.6 \times 10^{38}\,\text{protons/s}$$

**Mass consumed per second.** Each proton has mass $1.67 \times 10^{-27}$ kg:

$$3.6 \times 10^{38} \times 1.67 \times 10^{-27} \approx 6 \times 10^{11}\,\text{kg/s}$$

Six hundred million metric tons of hydrogen per second. The 0.7% of that which disappears as radiation by $E = mc^2$ comes to about four million tons per second — light, leaving the Sun, made of converted mass.

**Available hydrogen.** The Sun's total mass is $M_\odot \approx 2 \times 10^{30}$ kg. About 73% is hydrogen by mass. But only the core hydrogen — roughly 10% of the Sun's total mass — is hot and dense enough to fuse. Fusible hydrogen:

$$M_\text{fuse} \approx 0.10 \times 2 \times 10^{30} = 2 \times 10^{29}\,\text{kg}$$

**Lifetime.** Divide available hydrogen by consumption rate:

$$t \approx \frac{2 \times 10^{29}\,\text{kg}}{6 \times 10^{11}\,\text{kg/s}} \approx 3.3 \times 10^{17}\,\text{s}$$

Convert: one year is $3.15 \times 10^7$ s, so:

$$t \approx 10^{10}\,\text{yr}$$

Ten billion years total. The Sun is 4.5 billion years old. It has roughly **five billion years of main-sequence life remaining**.

Four numbers — luminosity, energy per fusion, proton mass, fusible fraction — and one division. The Sun's fate falls out of freshman arithmetic.

The calculation is approximate, and I want to be honest about the approximations. The luminosity is not constant: the Sun has brightened by roughly 30% since formation, which gives rise to the *Faint Young Sun paradox* — early Earth, under a dimmer Sun, should have been frozen solid, but the geological record shows liquid water. The 10% fusible fraction is a result from stellar-evolution models and helioseismology, not something you can derive from what we have covered here. But neither approximation changes the answer by more than a factor of two, and the answer is already in the right ballpark. The mechanism is right; the arithmetic confirms it.

<!-- → [TABLE: Summary of the lifetime calculation — four rows: (1) Solar luminosity L_sun = 3.828×10²⁶ W; (2) Energy per pp fusion = 4.27×10⁻¹² J (26.7 MeV); (3) Fusion rate = L/E = 9×10³⁷ s⁻¹; (4) Proton consumption rate = 4 × fusion rate × m_p = 6×10¹¹ kg/s; (5) Fusible mass = 0.10 × M_sun = 2×10²⁹ kg; (6) Lifetime = fusible mass / consumption rate ≈ 10¹⁰ yr — so student can see the chain of reasoning in one place and check each step independently] -->

![Four arithmetic steps from solar luminosity to total main-sequence lifetime. L = 3.828e26 W, divide by 26.7 MeV per fusion to get fusion rate, multiply by 4 protons per fusion, multiply by proton mass to get mass burn...](../images/05-the-sun-fig-05.png)
*Figure 5.5 — Sun's Lifetime Calculation: From L_⊙ to 10 Billion Years*

---

## The coronal heating problem

I want to return to the eclipse photograph.

A million-kelvin corona above a 5,800-kelvin photosphere is not just surprising; it is thermodynamically backward. Heat conducts from hot to cold. Radiation intensity falls with temperature to the fourth power. By either mechanism, the corona should be colder than the photosphere, not hotter. That it is not means energy is being deposited in the corona by some mechanism other than conduction or radiation from below.

The energy source is magnetic. That part is not controversial. The Sun's magnetic field is generated deep in the convection zone and emerges through the photosphere in bundles that make sunspots, loops, and arches visible in ultraviolet and X-ray photographs. The energy stored in these fields is more than sufficient to account for the corona's temperature. The question is the mechanism.

Two candidates have dominated the literature for decades.

**Magnetic reconnection.** Field lines in the corona are constantly being swept around by convective motions below, tangled and braided until adjacent lines with opposing directions are forced close together. When this happens, the field can snap into a new, lower-energy configuration — reconnection — releasing the stored energy impulsively as heat and particle acceleration. Small-scale reconnection events, sometimes called "nanoflares," happen continuously across the entire solar disk. The Feynman test here: reconnection is observed directly, in large-scale solar flares and coronal mass ejections. The question is whether the small, continuous version carries enough energy flux to maintain the corona's temperature.

![Two side-by-side schematics of the photosphere-to-corona transition. Panel A: tangled field lines snap and reconnect, releasing stored magnetic energy as flares and possible nanoflares. Panel B: convective motions plu...](../images/05-the-sun-fig-07.png)
*Figure 5.7 — Coronal Heating: Two Candidate Mechanisms*

**Alfvén waves.** Convective motions jiggle the footpoints of magnetic field lines. The disturbance propagates up the field line as a wave — an Alfvén wave, a shear oscillation of the magnetic field. If the wave damps before reaching the top of the corona, its energy thermalizes as heat. Alfvén waves have been directly detected in the corona by instruments on the Solar Dynamics Observatory. The question is whether they deposit their energy at the right heights and at sufficient rates.

<!-- → [IMAGE: Split-panel solar image — left: visible-light photograph of the Sun showing the photosphere and sunspots; right: extreme-ultraviolet or X-ray image of the same Sun (e.g., from SDO/AIA at 171 Å) showing the corona's hot loop structures; caption should emphasize that the two panels show the same star at the same time, but the right panel reveals structure invisible to the eye because it requires million-Kelvin plasma to emit at those wavelengths] -->

Both mechanisms are observed. Neither has been shown sufficient on its own to explain the full coronal energy budget. The Parker Solar Probe, launched in 2018, has been diving into the corona closer than any previous spacecraft and measuring the wave and field structure in situ. Results so far suggest that both mechanisms operate, with reconnection apparently dominant near the Sun and waves more important at larger distances. The problem is not solved but is narrowing.

I find the reconnection picture more compelling, but I want to be honest that this is a judgment about the weight of evidence, not a settled matter. If a Parker Solar Probe result next year showed that Alfvén-wave dissipation accounts for 90% of the coronal energy input, I would update. That is what the observation would require.

---

## What would change my mind

The central quantitative claim — that the Sun's luminosity is supplied by the pp chain at roughly $10^{38}$ fusions per second, releasing 26.7 MeV apiece — is directly confirmed by the solar neutrino flux. The Sudbury Neutrino Observatory measured the total neutrino output across all three flavors and found agreement with the standard solar model to within a few percent. A reproducible disagreement larger than 10%, with neutrino-oscillation effects properly accounted for, would force a revision of either the solar model or our understanding of neutrino physics. The qualitative coronal-heating picture would be revised if a single mechanism — reconnection or waves — were shown by Parker Solar Probe data to supply 90% or more of the total heating budget. Either would be a major result; neither has happened yet.

---

## Exercises

**Warm-up.** Name the five structural regions of the Sun in order from center to surface. For each, give an approximate temperature and state whether energy transport is primarily by radiation (photon random walk), convection (bulk plasma motion), or fusion (energy generation). *(Tests: solar structure, transport mechanisms.)*

**Warm-up.** The pp chain releases 26.7 MeV per fusion. (a) Convert this to joules. (b) A typical chemical reaction (say, burning one carbon atom) releases about 4 eV. By what factor does nuclear fusion release more energy per reaction? (c) If the Sun ran on chemical energy rather than fusion, and its mass were entirely burnable fuel, how long would it last at its current luminosity? *(Tests: unit conversion, energy scale comparison, order-of-magnitude estimation.)*

**Application.** A photon undergoes a random walk through the solar radiative zone. Each step is about 1 cm. The radiative zone spans roughly 45% of the Sun's radius (~$3.1 \times 10^8$ m). (a) Estimate the number of steps needed to cross this distance. (b) In a random walk, the expected displacement after $N$ steps of length $\ell$ is $\sqrt{N} \cdot \ell$. Invert this: given a required displacement of $3.1 \times 10^8$ m, how many steps are needed? (c) At the speed of light, how long does this take in years? *(Tests: random-walk scaling, order-of-magnitude derivation of $10^5$ year diffusion time.)*

**Application.** Repeat the solar lifetime calculation for a star with luminosity $100\,L_\odot$ and mass $10\,M_\odot$, assuming the same 10% fusible fraction and the same 26.7 MeV per fusion. (a) Compute the fusion rate in reactions per second. (b) Compute the hydrogen consumption rate in kg/s. (c) Compute the main-sequence lifetime in years. (d) Compare to the Sun's lifetime. What does this tell you about the relationship between stellar mass and longevity? *(Tests: applying the lifetime calculation to a different star, mass-luminosity-lifetime scaling.)*

**Application.** A sunspot has a temperature of 3,800 K. The surrounding photosphere has a temperature of 5,800 K. (a) Use the Stefan-Boltzmann law ($P \propto T^4$) to find the ratio of power radiated per unit area by the sunspot to that of the surrounding photosphere. (b) If the photosphere appears white (roughly equal emission across all visible wavelengths), use Wien's law to find the peak emission wavelength of the sunspot. What color would it appear in isolation? (c) Explain in two sentences why sunspots appear dark in photographs of the Sun. *(Tests: Stefan-Boltzmann, Wien's law, contrast vs. absolute brightness.)*

**Synthesis.** The "solar neutrino problem" lasted from the late 1960s to 2001. Ray Davis's Homestake detector measured roughly one-third the number of solar neutrinos predicted by the standard solar model. Two proposed resolutions were: (a) the standard solar model was wrong about the core temperature, or (b) neutrinos change flavor in transit and Davis's detector was only sensitive to one flavor. Describe one additional observation that would distinguish between these hypotheses. The SNO detector ultimately measured the total neutrino flux across all flavors and found agreement with the model — which hypothesis did this confirm, and what does it imply about neutrinos? *(Tests: distinguishing model error from physics error, neutrino oscillation, multi-messenger reasoning.)*

**Synthesis.** Sunspot activity follows an 11-year cycle driven by the Sun's differential rotation. (a) Explain in your own words why differential rotation — equator rotating faster than poles — winds up the magnetic field over time. (b) What happens to the field after it becomes sufficiently tangled? (c) Why is the *sunspot* cycle 11 years but the full *magnetic* cycle 22 years? (d) What does the existence of the sunspot cycle imply about the likely periodicity of coronal activity and solar wind strength? *(Tests: differential rotation mechanism, magnetic reconnection, cycle period reasoning, connection to corona.)*

**Challenge.** The *Faint Young Sun paradox*: the Sun was roughly 70% as luminous 4 billion years ago as it is today, yet geological evidence shows liquid water on Earth's surface throughout that period. (a) Use the Stefan-Boltzmann law to estimate how much colder Earth's average surface temperature would be if the Sun were 70% as luminous, assuming all else equal. (b) Earth's average temperature today is ~288 K. Would your estimate for the ancient Earth put it above or below freezing? (c) The leading resolutions involve higher concentrations of greenhouse gases in the early atmosphere. Describe, in physical terms (not chemistry), how a greenhouse gas increases surface temperature. (d) What observation — ancient rock chemistry, isotope ratios, something else — could constrain the atmospheric composition of the early Earth, and thereby test a proposed resolution to the paradox? *(Tests: Stefan-Boltzmann scaling, climate physics, habitability, connecting model prediction to observational test.)*

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

**Tags:** Sun, proton-proton chain, solar structure, corona, sunspots, nuclear fusion, neutrinos, coronal heating problem
