# Chapter 2 — Heat Transfer


## TL;DR

- Heat flows from hot to cold by three mechanisms: conduction (molecular collisions passing energy through matter), convection (bulk fluid carrying heat with it), and radiation (electromagnetic waves carrying energy...
- The chapter moves through The temperature of the Sun, What it means for heat to "flow", Conduction: the molecular relay race, Convection: heat on the move, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

Heat flows from hot to cold by three mechanisms: conduction (molecular collisions passing energy through matter), convection (bulk fluid carrying heat with it), and radiation (electromagnetic waves carrying energy through space, including vacuum). Each has a rate law. Fourier's law for conduction: $P = kA\,\Delta T/L$. Newton's law of cooling for convection: $P = hA\,\Delta T$. Stefan-Boltzmann for radiation: $P = \varepsilon\sigma A T^4$. Know these three and you can work out why your coffee cools, why fiberglass insulation works, and — remarkably — what temperature the surface of a star is, from its color, without going there.

---

## The temperature of the Sun

Here is something that ought to be astonishing. The Sun is 150 million kilometers away. No spacecraft has ever come close to its surface. No thermometer has ever touched it. And yet we know its surface temperature to four significant figures: $5{,}778\text{ K}$.

How?

The answer is that every object at any temperature radiates electromagnetic energy, and the *spectrum* of that radiation — which wavelengths are emitted most strongly — depends on temperature and temperature alone. The Sun's light peaks in the green-yellow, around $500\text{ nm}$. There is a law — Wien's displacement law — that says the peak wavelength $\lambda_{\max}$ and the temperature $T$ are related by

$$\lambda_{\max} T = 2.898 \times 10^{-3}\text{ m·K}.$$

Plug in $500 \times 10^{-9}\text{ m}$ and you get $T \approx 5{,}800\text{ K}$. No visit required. The color of the light *is* the thermometer.

Your body does the same thing, but at a much lower temperature. At $T \approx 310\text{ K}$, your peak emission is at $\lambda_{\max} = 2.898\times10^{-3}/310 \approx 9.4\text{ μm}$ — deep infrared, completely invisible to human eyes, perfectly visible to a thermal imaging camera. When you walk through a dark room, you glow like a furnace — just not at a frequency that your own eyes can see.

This is one mechanism of heat transfer: radiation. Energy moves as electromagnetic waves, no medium required — the Sun's heat crosses 150 million kilometers of vacuum before it touches your face. The other two mechanisms require matter. But to understand all three, we need to start with what heat transfer actually is.

---

## What it means for heat to "flow"

Temperature is a measure of the average kinetic energy of molecules. Heat is what we call energy when it moves from a hotter region to a cooler one — not because it's a different kind of energy, just because that direction of motion (hot to cold) is what the second law of thermodynamics enforces.

The question this chapter answers is: *how fast* does it flow, and *by what path*?

There are exactly three answers. The first is conduction: in any material, neighboring molecules collide and transfer kinetic energy directly. A hot end of a metal rod agitates its molecules; they bump the cooler neighbors; the disturbance propagates. No matter moves. Just energy, passed hand to hand through a molecular chain. The second is convection: in a fluid, the hot material itself moves — warm air rises, cool air sinks, and the fluid carries its thermal energy with it in bulk. The third is radiation: oscillating charges emit electromagnetic waves that carry energy away at the speed of light, whether or not any matter is in the way.

In most real situations, all three operate at once. Your coffee cooling in a cup loses heat by conduction through the cup walls, by convection from the hot liquid surface to the cooler air, and by radiation from every surface. To slow the cooling, you have to fight all three — which is exactly what a vacuum-insulated thermos does. The vacuum between the walls eliminates conduction (nothing to conduct through) and convection (no fluid to carry heat). The silvered walls, with emissivity near zero, suppress radiation. Block all three and the coffee stays hot for hours.

Let's look at each mechanism in turn.

---

## Conduction: the molecular relay race

Hold one end of a copper rod and put the other end in a flame. Within seconds the held end grows hot. Energy moved from flame to your hand through the copper, without any of the copper moving. That's conduction.

The rate of heat transfer through a slab of material depends on four things: the cross-sectional area $A$ (more area, more molecular contacts), the temperature difference $\Delta T = T_H - T_C$ across the slab (steeper gradient, faster transfer), the thickness $L$ (longer path, more resistance), and a material property called thermal conductivity $k$. Fourier's law puts them together:

$$P = k A \frac{\Delta T}{L}.$$

The units work out: $k$ is in W/(m·K), and $P$ in watts. Thermal conductivity spans four orders of magnitude across common materials. Silver and copper are near the top: $k \approx 390$–$430\text{ W/(m·K)}$. That's why copper cookware heats evenly and why copper heat sinks pull heat away from electronics quickly. Wood is around $0.13$. Glass and brick around $0.8$. And then the good insulators: fiberglass batting at $0.04$, aerogel at $0.013$. Air itself has $k = 0.026$ — almost as good as aerogel.

This last point is worth pausing on. Why does fiberglass insulate so well? Not primarily because of anything special about glass fibers. It insulates because it traps air in tiny pockets, and air conducts heat poorly. The fibers just prevent the air from circulating and carrying heat away by convection. The actual insulating agent is the trapped, still air. This is why dry clothing insulates and wet clothing doesn't: water's conductivity ($k \approx 0.6$) is twenty times higher than air's. Replace the air in your clothing with water and your insulation collapses.

There is a useful rewrite of Fourier's law that makes composite materials easy to handle. Define the thermal resistance of a slab as $R = L/(kA)$. Then Fourier's law becomes $P = \Delta T / R$ — exactly analogous to Ohm's law, $I = V/R$. And just as resistors in series add, thermal resistances in series add: $R_\text{total} = R_1 + R_2 + \ldots$. A composite wall — say, brick on the outside, foam insulation in the middle, drywall on the inside — is a series circuit. The total resistance is the sum of the three layer resistances, and the heat flow rate is $\Delta T / R_\text{total}$.

There is one immediate and important consequence of the series analogy: the temperature drop across each layer is proportional to that layer's resistance. In the wall example, if the foam has $R_2 = 3.75\text{ m}^2\text{·K/W}$ and the brick has $R_1 = 0.14$, then out of the total $25\text{ K}$ temperature difference nearly all of it — about $23.6\text{ K}$ — drops across the foam, and only $0.9\text{ K}$ drops across the brick. The temperature profile in the wall is almost flat through the brick, then plunges steeply through the insulation, then nearly flat through the drywall. Adding more brick does almost nothing to reduce heat loss. Adding more foam is everything.

This is why passive houses obsess over insulation thickness and not wall material. The material with the highest thermal resistance controls the system. Everything else is noise.

---

## Convection: heat on the move

Conduction requires no material motion. Convection is the opposite: it *is* material motion. When you heat water on a stove, the water near the burner warms, expands, becomes less dense, rises, and is replaced by cooler, denser water descending from above. The fluid circulates, continuously carrying warm water up and cool water down. The same mechanism operates in the atmosphere, in the oceans, and in the outer layers of the Sun — those churning convection cells in the solar photosphere are each the size of Texas.

The rate of convective heat transfer between a surface and a fluid is described by Newton's law of cooling:

$$P = h A (T_s - T_f),$$

where $T_s$ is the surface temperature, $T_f$ is the fluid temperature, $A$ is the surface area, and $h$ is the convection coefficient in W/(m²·K). The formula is deceptively simple because all the complexity — the fluid dynamics, the geometry, the flow regime — is absorbed into $h$. Computing $h$ from first principles requires solving the Navier-Stokes equations, which is why entire graduate courses exist on convective heat transfer. At this level, we treat $h$ as a measured empirical input.

But the *range* of $h$ values is physically significant. Natural convection in still air gives $h \approx 5$–$25\text{ W/(m}^2\text{·K)}$. Forced convection in a stiff wind pushes $h$ to $25$–$250$. Natural convection in water: $100$–$1{,}000$. Boiling water: $10{,}000$ or more. These are order-of-magnitude differences.

This explains why wind makes cold days feel so much colder. Your skin temperature is around $33\text{°C}$. On a still $0\text{°C}$ day, natural convection with $h \approx 5$ gives a heat loss of roughly $165\text{ W/m}^2$. In a $5\text{ m/s}$ wind, $h$ jumps to perhaps $30$, and heat loss climbs to nearly $1{,}000\text{ W/m}^2$ — six times higher. Your body must burn six times more fuel to maintain skin temperature. Wind doesn't lower the actual air temperature. It strips away the thin warm air layer your body had laboriously built up around itself, replacing it continuously with fresh cold air. The heat loss rate is the sensation.

Water is worse. Immersion in cold water is far more dangerous than standing in cold air at the same temperature, because $h$ for natural convection in water is twenty to a hundred times higher than in still air. A person immersed in $10\text{°C}$ water loses body heat so quickly that hypothermia becomes life-threatening within an hour. The same person, in $10\text{°C}$ air, would be cold but in no danger.

Newton's law of cooling can also be written as a differential equation. If a hot object at temperature $T$ is surrounded by fluid at $T_f$, its temperature changes at the rate

$$\frac{dT}{dt} = -\frac{hA}{mc}(T - T_f),$$

where $m$ is the mass and $c$ the specific heat. This equation has the solution $T(t) = T_f + (T_0 - T_f)\,e^{-t/\tau}$ with time constant $\tau = mc/(hA)$. Temperature decays exponentially toward ambient. Fresh coffee at $90\text{°C}$ in a $20\text{°C}$ room doesn't cool linearly; it cools fast at first and slow as it approaches room temperature. The time constant for a typical uncovered mug — maybe $20$–$40$ minutes — tells you how quickly it becomes unpleasantly lukewarm.

---

## Radiation: how the Sun heats the Earth

Every object at a temperature above absolute zero emits electromagnetic radiation. This is not a material process — no matter needs to be present, and no contact is required. The radiation propagates at the speed of light, carrying energy. Objects continuously emit and absorb radiation; whether they gain or lose heat depends on whether they absorb more than they emit or vice versa.

The total power emitted by a surface at absolute temperature $T$:

$$P_\text{emit} = \varepsilon \sigma A T^4,$$

where $\sigma = 5.67 \times 10^{-8}\text{ W/(m}^2\text{·K}^4)$ is the Stefan-Boltzmann constant and $\varepsilon$ is the emissivity — a dimensionless number between 0 and 1 that characterizes how closely the surface approximates a perfect radiator. A perfect blackbody has $\varepsilon = 1$ and emits the maximum possible radiation for its temperature. Human skin, regardless of color in the visible spectrum, has $\varepsilon \approx 0.97$ in the infrared — nearly a perfect blackbody. Polished aluminum has $\varepsilon \approx 0.04$ — it emits (and absorbs) almost nothing relative to a blackbody at the same temperature.

The $T^4$ dependence is not a minor detail. Double the temperature and you emit sixteen times as much power. The Sun at $5{,}800\text{ K}$ emits roughly $(5800/300)^4 \approx 140{,}000$ times more power per unit area than a room-temperature object. That factor is what makes the Sun visible from 150 million kilometers away and what makes staring at it dangerous.

The net radiation exchange between a surface at $T_s$ and surroundings at $T_\text{surr}$:

$$P_\text{net} = \varepsilon \sigma A (T_s^4 - T_\text{surr}^4).$$

A person in a room at $20\text{°C}$ ($293\text{ K}$) with skin temperature $33\text{°C}$ ($306\text{ K}$) and surface area $1.8\text{ m}^2$, emissivity $0.97$, radiates a net

$$P_\text{net} = 0.97 \times 5.67\times10^{-8} \times 1.8 \times (306^4 - 293^4) \approx 70\text{ W}.$$

Seventy watts, continuously, just standing still in a room. A resting adult generates about $80$–$100\text{ W}$ metabolically. Nearly all of it exits as radiation and convection. This is why a room full of people gets warm: each person is a $100\text{ W}$ space heater.

---

## Wien's law and the color of stars

Back to the question that opened this chapter. Wien's displacement law says that the wavelength at which a blackbody emits most intensely is inversely proportional to temperature:

$$\lambda_{\max} T = 2.898 \times 10^{-3}\text{ m·K}.$$

The consequences run across the entire electromagnetic spectrum. The Sun's surface at $5{,}800\text{ K}$ peaks at $500\text{ nm}$, in the visible — which is no coincidence, since our eyes evolved to be most sensitive to exactly the spectrum our sun emits most abundantly. The Earth's surface at $288\text{ K}$ peaks at $10\text{ μm}$, in the mid-infrared — invisible to our eyes but detectable by thermal cameras and by the atmosphere's greenhouse gases. The cosmic microwave background, a relic glow from the early universe, has temperature $2.7\text{ K}$ and peaks at about $1\text{ mm}$, in the microwave.

Astronomers read stellar temperatures from color. Blue-white stars like Rigel have surface temperatures near $12{,}000\text{ K}$, peaking in the ultraviolet. Red stars like Betelgeuse peak around $700\text{ nm}$, indicating surface temperatures around $3{,}500\text{ K}$. A star's color is its thermometer, available to anyone with a spectrometer and Wien's law.

This is a recurring theme in physics: a formula that looks narrow — the peak wavelength of thermal emission — turns out to be a key to an enormous range of phenomena, from the temperature of stars to the design of night-vision goggles to understanding why Earth doesn't overheat.

---

## The greenhouse effect and the asymmetry of the atmosphere

Earth's atmosphere is mostly transparent to the wavelengths the Sun emits — visible and near-infrared, with peak around $500\text{ nm}$. Sunlight passes through and warms the Earth's surface. The surface re-emits radiation, but at Earth's temperature ($288\text{ K}$), that emission peaks at $10\text{ μm}$ — mid-infrared. And mid-infrared is precisely the range at which molecules like CO₂, water vapor, and methane absorb efficiently.

The asymmetry is everything. In comes visible light, essentially unimpeded. Out tries to go infrared radiation; the atmosphere partially blocks it, absorbs the energy, and re-radiates some of it back downward. The surface is warmer than it would be if the atmosphere were transparent at all wavelengths.

Without any greenhouse effect, you can estimate Earth's equilibrium temperature from energy balance: incoming solar power equals outgoing thermal radiation. That calculation gives about $255\text{ K}$, or $-18\text{°C}$. The actual average is $288\text{ K}$, or about $15\text{°C}$. The natural greenhouse effect provides $33\text{ K}$ of warming. Without it, Earth would be perpetually frozen.

The mechanism behind anthropogenic climate change is the same Stefan-Boltzmann physics, shifted: adding CO₂ and methane increases the fraction of outgoing infrared absorbed by the atmosphere, which requires the surface to warm to a new equilibrium where it emits enough radiation to balance the incoming solar power at the increased atmospheric absorption. The formula doesn't change. The parameters do.

---

## What the framework hides

These three laws — Fourier, Newton, Stefan-Boltzmann — are extraordinarily good approximations in most macroscopic engineering situations. But they each carry hidden assumptions.

Fourier's law assumes that heat diffuses — that the thermal conductivity is a well-defined material property and that temperature gradients are smooth. At nanoscales, in materials like carbon nanotubes and graphene, heat moves more like a wave than a diffusion. This is called ballistic phonon transport, and it causes the apparent thermal conductivity of nanoscale systems to depend on system size in ways Fourier's law can't predict. The engineering frontier of nanoscale thermal management — critical for ever-smaller transistors — lives where Fourier fails.

Newton's law of cooling hides its complexity in $h$. The convection coefficient is not a material property; it depends on geometry, flow speed, fluid viscosity, whether the flow is laminar or turbulent, and the spatial distribution of temperature in the fluid. Computing $h$ from first principles requires fluid mechanics — specifically, matching solutions to the boundary-layer equations at the surface. This chapter takes $h$ as measured; the next step would be learning how to predict it.

The Stefan-Boltzmann law treats emissivity as a single number, but emissivity is generally wavelength-dependent. A surface can have high emissivity in the infrared and low emissivity in the visible, or vice versa. This selective absorption and emission is the basis of solar thermal collectors (designed to absorb visible light well and emit infrared poorly, so they stay hot) and emerging radiative cooling technologies (materials that emit strongly in a specific atmospheric transparency window — around $8$–$13\text{ μm}$ — allowing surfaces to shed heat to the cold sky above even in daylight, potentially below ambient air temperature). These are Stefan-Boltzmann physics, but with $\varepsilon(\lambda)$ rather than a constant $\varepsilon$.

The deeper puzzle underneath all three mechanisms is the same question we encountered at the end of the last chapter: *why* does heat flow from hot to cold? The three rate laws describe the *rate* of flow but not the *direction* — that comes from the second law of thermodynamics, and ultimately from the statistics of large numbers of molecules. We'll reach that in Chapter 5, when we get to entropy.

---

## LLM Exercises

### Build the composite wall simulator (`02-heat-conduction.html`)

> **Show.** Fourier's law: $P = kA(T_H - T_C)/L$. Resistance $R = L/(kA)$. Series resistances add.
>
> **Say.** Build an interactive composite-wall thermal conduction simulator.
>
> **Constrain.** D3 v7. Wall cross-section displayed horizontally. Toggle for number of layers (1–4). For each layer: dropdown for material (sets $k$: copper 390, glass 0.8, brick 0.7, wood 0.13, fiberglass 0.04, foam 0.04, aerogel 0.013, air 0.026), slider for thickness $L$. Slider for total wall area $A$. Sliders for $T_H$ (hot side) and $T_C$ (cold side). Display: temperature profile $T(x)$ across the wall as a piecewise-linear curve; heat flux $P$ in watts; thermal resistance per layer and total. Filename: `02-heat-conduction.html`.
>
> **Verify.** (a) A wall of pure copper transmits much more heat than a wall of foam at the same dimensions. (b) Adding foam thickness reduces heat loss. (c) Temperature gradient is steepest across the highest-resistance layer.

### Exploration

- Build a passive-house-grade wall and a typical-residential wall. Compare heat losses.
- Insert a copper layer in series with a foam layer. The copper barely contributes to the total resistance; foam dominates.
- Vary wall area $A$. Heat loss is proportional to area at fixed $\Delta T$.

### Extension prompt (chapter bridge)

> **Show.** I've handled conduction. Now I want to see how radiation works — Stefan-Boltzmann's $T^4$ law and Wien's $\lambda_{\max}T$ relationship.
>
> **Say.** Build a thermal radiation visualizer.
>
> **Constrain.** Slider for temperature (50–10000 K). Display the blackbody spectrum (power per unit wavelength) as a curve, with peak wavelength $\lambda_{\max}$ marked. Display total radiated power and where in the EM spectrum (radio, IR, visible, UV, X-ray) the peak falls.
>
> **Verify.** Sun temperature ~5800 K → peak in visible. Earth ~288 K → peak in mid-IR. Doubling T → 16× total power.

Save as `02b-radiation-preview.html`. Bridge to applications in Chapter 4 and 6.

---

##  AI Wayback Machine

**Run this:**

```
Who was Joseph Fourier, and what did he actually do for mathematics and physics beyond the heat equation? Keep it to three paragraphs. End with the single most surprising thing about his career.
```

→ Search **"Joseph Fourier"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to explain how Fourier series connect the heat equation to signal processing and modern audio compression.
- Ask it why the Fourier transform appears in quantum mechanics, optics, and MRI imaging.

What changes? What gets better? What gets worse?

---

**Tags:** conduction, Fourier's-law, convection, Newton's-law-of-cooling, radiation, Stefan-Boltzmann, Wien's-law, R-value, greenhouse-effect
![Cross-section of brick-foam-drywall wall with temperature profile above. T(x) is nearly flat across brick (small slope, low R), drops sharply across foam (steep slope, high R), nearly flat across drywall. Highest-R la...](../images/02-heat-transfer-fig-01.png)
*Figure 2.1 — Composite Wall T(x)*

![Coffee cooling from 90°C toward room temperature 20°C. Blue exponential curve T(t) = T_f + (T_0 - T_f)e^(-t/τ). Dashed vermillion reference line shows what naïve linear cooling would do — diverges and crosses zero aro...](../images/02-heat-transfer-fig-02.png)
*Figure 2.2 — Newton's Cooling*

![Three Planck blackbody spectra on log-log axes. Sun peaks in visible at 500 nm; Earth peaks in mid-IR at 10 micrometers; CMB peaks in microwave at 1 mm. Wien's law slides the peak right as T drops.](../images/02-heat-transfer-fig-03.png)
*Figure 2.3 — Blackbody Spectra*

![Cross-section of Earth and atmosphere. Solar visible light passes through. Earth re-radiates IR; part escapes, part absorbed and re-emitted downward. Inset: atmospheric transparency versus wavelength shows the visible...](../images/02-heat-transfer-fig-04.png)
*Figure 2.4 — Greenhouse Effect*

