# Chapter 12 — Fluid Dynamics and Its Biological and Medical Applications

*Why narrowing a pipe accelerates the flow, and why that kills people.*

---

Here is a fact that should make you think twice about cardiovascular disease. If an artery's radius is reduced by thirty percent — not cut in half, not blocked, just narrowed by thirty percent, which is plausible from moderate atherosclerosis — the blood flow through it at the same pressure drops to about twenty-four percent of normal. Not seventy percent. Twenty-four percent. A thirty percent reduction in radius produces a seventy-six percent reduction in flow.

The reason is that flow through a tube scales as the *fourth* power of the radius. Halve the radius and you get one-sixteenth the flow. Reduce the radius by a third and you lose three-quarters of the flow. The heart has to work dramatically harder to push enough blood through. That's not a metaphor for why atherosclerosis is dangerous — it's the quantitative prediction.

This chapter develops the physics behind that number. There are three pieces, and each one is a conservation law in disguise: mass conservation for fluids (the continuity equation), energy conservation for fluids (Bernoulli's equation), and the role of viscosity in determining whether flow is smooth or chaotic. Together they explain blood pressure measurement, how the heart works, why airplane wings generate lift, what makes a fire hose work, and why a bacterium can't coast through water.

---

## Mass conservation: the continuity equation

If fluid is flowing through a pipe, and the pipe narrows, the fluid speeds up. This isn't surprising — but let's be precise about why.

Suppose a pipe has cross-sectional area $A_1$ at one point and area $A_2$ at another. Fluid flows through at speeds $v_1$ and $v_2$ respectively. In a small time $\Delta t$, the volume of fluid passing through the wide section is $A_1 v_1 \Delta t$, and the volume passing through the narrow section is $A_2 v_2 \Delta t$. For an incompressible fluid — one where density doesn't change, which is a very good approximation for liquids — those volumes must be equal. Fluid can't pile up or disappear. So:

$$A_1 v_1 = A_2 v_2.$$

This is the **continuity equation**. The product $Av$ — volume per unit time, also called the **volume flow rate** $Q$ — is constant along the pipe.

$$Q = Av.$$

The consequences are immediate. Halve the area and you double the speed. That's what happens when you put your thumb over a garden hose — the same flow rate is forced through a smaller opening, and the water shoots out faster. It's what happens in every narrowed artery: blood accelerates through the constriction, a fact whose pressure implications we'll reach shortly.

For the cardiovascular system, the continuity equation has a striking consequence. The aorta has a cross-sectional area of about $4 \text{ cm}^2$. The total cross-section of all capillaries combined is about $4{,}500 \text{ cm}^2$ — a thousand times larger. So blood in the capillaries moves about a thousand times slower than blood in the aorta: roughly $0.03 \text{ cm/s}$ compared to $30 \text{ cm/s}$. That's not a design compromise. It's the point. Slow blood in capillaries gives time for oxygen and nutrient exchange across the capillary walls. The cardiovascular system is engineered, by evolution, so that the geometry produces the right flow speed at the right location.

![Schematic of vessel branching from aorta through arteries, arterioles, capillaries. As cross-sectional area grows by orders of magnitude, blood velocity drops proportionally (continuity equation A·v = const). Capillary v ≈ 1 mm/s.](../images/12-fluid-dynamics-and-its-biological-and-medical-applications-fig-01.png)
*Figure 12.1 — Cardiovascular Cascade — A·v = Constant Across Branches*

<!-- → [FIGURE: Schematic of cardiovascular cross-section areas. Left: single aorta with A = 4 cm². Right: branching tree leading to capillary bed with total A = 4500 cm². Arrows showing blood velocity v_aorta >> v_capillary. Caption: Continuity applied to the cardiovascular system. Total cross-sectional area increases 1000-fold from aorta to capillary bed, so blood velocity decreases by the same factor. The slow capillary flow is essential for gas exchange.] -->

![Constriction in a pipe. Wide section: slow flow, high pressure (tall manometer column). Narrow section: fast flow, low pressure (short column). Bernoulli: P + ½ρv² + ρgh = constant along a streamline.](../images/12-fluid-dynamics-and-its-biological-and-medical-applications-fig-02.png)
*Figure 12.2 — Venturi Pipe — Faster Flow, Lower Pressure*

**A worked example.** A Venturi meter — a pipe with a deliberate narrowing used to measure flow rates — has cross-section $A_1 = 4.0 \text{ cm}^2$ in the wide section and $A_2 = 1.0 \text{ cm}^2$ in the narrow throat. Water flows through at $v_1 = 0.50 \text{ m/s}$ in the wide section.

Speed in the throat: $v_2 = v_1(A_1/A_2) = 0.50 \times 4 = 2.0 \text{ m/s}$.

Volume flow rate: $Q = A_1 v_1 = (4.0 \times 10^{-4})(0.50) = 2.0 \times 10^{-4} \text{ m}^3/\text{s} = 0.20 \text{ L/s}$.

The same flow rate holds everywhere in the pipe — the Venturi doesn't add or remove fluid; it just measures it. The measurement trick is that the *speed change produces a pressure change*, and that pressure change is measurable. Which brings us to Bernoulli.

<!-- → [FIGURE: Venturi meter diagram. Horizontal pipe, wide on left and right, narrowed in middle throat. Labels: A₁ = 4 cm², v₁ = 0.5 m/s (wide); A₂ = 1 cm², v₂ = 2.0 m/s (throat). Manometer tubes showing higher pressure in wide section and lower pressure in throat. Caption: The Venturi meter uses continuity (speed increases in throat) and Bernoulli (higher speed → lower pressure) together. Measuring the pressure difference between the wide and narrow sections gives the flow rate.] -->

---

## Energy conservation: Bernoulli's equation

The pressure in a moving fluid is connected to the fluid's speed. Faster flow, lower pressure. This is Bernoulli's principle, and it follows directly from energy conservation.

Consider a small parcel of fluid moving along a streamline — a path that the fluid follows. The parcel has kinetic energy (from its motion), gravitational potential energy (from its height), and "pressure energy" (from the work done by the pressure field pushing it along). In frictionless, steady, incompressible flow, the total energy per unit volume is constant along the streamline:

$$P + \tfrac{1}{2}\rho v^2 + \rho g h = \text{constant}.$$

This is **Bernoulli's equation**. Three terms: the static pressure $P$, the kinetic energy per unit volume $\tfrac{1}{2}\rho v^2$, and the gravitational potential energy per unit volume $\rho g h$. Their sum doesn't change as the fluid moves along its path.

<!-- → [TABLE: Bernoulli's equation terms. Columns: term, physical meaning, units. Rows: P (static pressure, Pa), ½ρv² (kinetic energy per unit volume / dynamic pressure, Pa), ρgh (gravitational potential energy per unit volume, Pa), sum = constant (total mechanical energy per unit volume, Pa). Caption: Bernoulli's equation is the energy ledger for a fluid parcel along a streamline. All three terms have units of Pa (= J/m³ = energy per unit volume).] -->

The implications fall out immediately. If the height doesn't change ($h = \text{const}$), then when speed goes up, pressure goes down. The fluid has traded pressure energy for kinetic energy. When the pipe widens and the fluid slows down, pressure increases — the kinetic energy converts back to pressure energy.

**Torricelli's theorem** is a special case. For water draining from a large reservoir through a hole at depth $h$ below the surface, the surface is approximately stationary ($v_{\text{surface}} \approx 0$), and both the surface and the outlet are at atmospheric pressure. Bernoulli reduces to:

$$P_{\text{atm}} + 0 + \rho g h = P_{\text{atm}} + \tfrac{1}{2}\rho v^2 + 0 \implies v = \sqrt{2gh}.$$

The exit speed equals that of a free-falling object dropped from height $h$. This is not a coincidence — both are just energy conservation, one for a fluid, one for a solid.

<!-- → [FIGURE: Reservoir with hole at depth h below surface. Bernoulli terms labeled at both points: surface (P_atm, v≈0, height h) and outlet (P_atm, v = √2gh, height 0). Caption: Torricelli's theorem is Bernoulli's equation for a drain. The exit speed equals the speed of a free-falling object from the same height — both are energy conservation.] -->

The Venturi meter from the previous section now has a completion. The speed in the throat is higher, so by Bernoulli the pressure there is lower. Measure the pressure difference between the wide section and the throat, and you know the flow rate. No moving parts. No sensors in the flow path. Just geometry and energy conservation.

**A more realistic application: the fire hose.** Water in a fire hose has gauge pressure $2.0 \times 10^5 \text{ Pa}$ and speed $5.0 \text{ m/s}$ in the large hose section. The nozzle narrows the area by a factor of 4, accelerating water to $20 \text{ m/s}$, and exits at atmospheric pressure. Apply Bernoulli (same height throughout):

$$P_{\text{hose}} + \tfrac{1}{2}\rho v_{\text{hose}}^2 = P_{\text{atm}} + \tfrac{1}{2}\rho v_{\text{nozzle}}^2.$$

Left side: $(P_{\text{atm}} + 2.0 \times 10^5) + \tfrac{1}{2}(1000)(5.0)^2 = P_{\text{atm}} + 212{,}500$.

Right side: $P_{\text{atm}} + \tfrac{1}{2}(1000)(20)^2 = P_{\text{atm}} + 200{,}000$.

These don't quite balance — the discrepancy of $12{,}500 \text{ Pa}$ is real, and it's friction losses in the hose that Bernoulli's frictionless idealization ignores. The agreement is about $94\%$. For a rough estimate, Bernoulli works. For precise engineering, viscosity can't be neglected.

### What Bernoulli does not explain

Bernoulli is powerful, but popular accounts overextend it. The most-cited overextension is airplane lift. The standard explanation goes: the curved upper surface of a wing is longer, air takes longer to travel over the top, so it goes faster, so the pressure is lower on top than the bottom, so there's lift. The first step — curved surface is longer — is true. The conclusion — lower pressure on top — is also true. The middle reasoning — air must "meet up" with air that went below — is false. There's no requirement that air takes the same time to traverse both sides of the wing, and experiments confirm it doesn't.

The correct picture combines Bernoulli with Newton. A wing is angled so that it deflects air downward. By Newton's third law, the air pushes the wing upward. This downward momentum given to the air per unit time is also the lift. Simultaneously, the curved geometry creates faster flow over the top and lower pressure there, consistent with Bernoulli. Both descriptions are correct; they're complementary views of the same physics, not competing explanations.

<!-- → [FIGURE: Wing cross-section (airfoil). Streamlines shown: faster, more curved flow over the top surface; slower flow beneath. Pressure arrows: low pressure above (pointing up toward wing), higher pressure below (pointing up into wing). Separate arrow showing downwash — air deflected downward behind wing. Two labels: "Bernoulli: faster flow → lower pressure (lift)" and "Newton: wing pushes air down → air pushes wing up (lift)." Caption: Both Bernoulli and Newton explain the same lift. They're complementary descriptions, not competing ones. The equal-transit-time argument (faster flow because surface is longer) is false — air does not wait for its partner.] -->

---

## Real fluids: viscosity, Poiseuille, and the Reynolds number

Everything so far has assumed frictionless flow. Real fluids aren't frictionless. Molecules in a fluid interact with each other and with the pipe walls, and faster-moving layers drag on slower-moving layers. This internal friction is **viscosity**, measured in $\text{Pa·s}$.

Some representative values: water at $20°\text{C}$ has $\eta \approx 10^{-3} \text{ Pa·s}$. Air has $\eta \approx 1.8 \times 10^{-5} \text{ Pa·s}$ — far lower. Blood is about three to four times more viscous than water, $\eta \approx 4 \times 10^{-3} \text{ Pa·s}$. Honey is about ten thousand times more viscous than water.

<!-- → [TABLE: Viscosity values for common fluids. Columns: fluid, temperature (°C), viscosity η (Pa·s). Rows: air (20°C, 1.8×10⁻⁵), water (20°C, 1.0×10⁻³), blood (37°C, 3–4×10⁻³), olive oil (20°C, ~0.08), honey (20°C, ~10), glass (room temp, ~10¹²). Caption: Viscosities span fifteen orders of magnitude. Glass is technically a very high-viscosity fluid — it flows, but on geological timescales.] -->

For steady, smooth (**laminar**) flow through a cylindrical pipe of radius $r$ and length $L$ with pressure difference $\Delta P$ driving the flow, the volume flow rate is given by **Poiseuille's law**:

$$Q = \frac{\pi r^4 \Delta P}{8 \eta L}.$$

![Cross-section showing parabolic velocity profile in laminar pipe flow: v(r) = v_max(1 − r²/R²). Maximum at center, zero at wall. Total flow rate Q ∝ R⁴ (Poiseuille's law) — small radius changes have outsized effects.](../images/12-fluid-dynamics-and-its-biological-and-medical-applications-fig-03.png)
*Figure 12.3 — Parabolic Velocity Profile — Laminar Pipe Flow and Poiseuille's r⁴ Law*

The $r^4$ is the critical feature. Flow scales as the fourth power of radius. The physical reason: a pipe has cross-sectional area proportional to $r^2$, and the velocity profile in laminar flow is parabolic — the fluid near the center moves faster than near the walls, and integrating a parabolic profile over a circular cross-section introduces another factor of $r^2$. Area × velocity profile = $r^2 \times r^2 = r^4$.

<!-- → [FIGURE: Pipe cross-section showing parabolic velocity profile in laminar flow. Horizontal arrows of varying lengths: longest at center, tapering to zero at pipe wall. Labeled: v_max = 2v_avg at center, v = 0 at wall (no-slip condition). Caption: The Poiseuille velocity profile is parabolic. The no-slip condition (v = 0 at the wall) and maximum velocity at the center produce the parabola. Integrating this profile over the cross-section gives the r⁴ scaling.] -->

Now the opening number becomes clear. A $30\%$ reduction in arterial radius: $r_{\text{new}} = 0.70 r_{\text{old}}$. New flow rate at the same pressure:

$$Q_{\text{new}} = Q_{\text{old}} \times (0.70)^4 = Q_{\text{old}} \times 0.24.$$

Twenty-four percent of the original. To maintain the same flow, the heart must increase the pressure driving force by a factor of $1/0.24 \approx 4$. It does this by pumping harder — which strains the heart muscle — or it accepts reduced flow, which starves downstream tissue. The $r^4$ scaling is not merely a mathematical curiosity. It's the physical mechanism that makes moderate arterial narrowing medically serious.

<!-- → [CHART: Bar chart showing Q/Q_original vs. fraction of original radius, from r = 1.0 down to r = 0.5, using Q ∝ r⁴. Bars at r = 1.0 (Q = 100%), 0.9 (66%), 0.8 (41%), 0.7 (24%), 0.6 (13%), 0.5 (6%). Caption: Poiseuille's r⁴ scaling makes arterial narrowing asymmetrically dangerous. A 30% reduction in radius cuts flow to 24% of normal. A 50% reduction leaves only 6%.] -->

### Laminar and turbulent flow: the Reynolds number

![Two panels. Laminar (Re < 2000): smooth parallel streamlines, predictable layered flow. Turbulent (Re > 3000): chaotic eddies and vortices, irregular mixing. Reynolds number Re = ρvD/η determines regime.](../images/12-fluid-dynamics-and-its-biological-and-medical-applications-fig-04.png)
*Figure 12.4 — Laminar vs Turbulent — A Reynolds Number Crosses ~ 2,000*

Poiseuille's law applies only to laminar flow — smooth, orderly layers of fluid sliding past one another with minimal mixing. The other regime is **turbulent** flow: chaotic, with eddies and vortices and complex velocity patterns. Turbulent flow has higher resistance than laminar flow and generates more noise and more energy dissipation.

Which regime applies depends on a dimensionless quantity called the **Reynolds number**:

$$\text{Re} = \frac{\rho v L}{\eta},$$

where $\rho$ is fluid density, $v$ is a characteristic flow speed, $L$ is a characteristic length (usually pipe diameter), and $\eta$ is viscosity. The Reynolds number is physically a ratio of inertial forces to viscous forces. Large Re: inertia dominates, flow tends to be turbulent. Small Re: viscosity dominates, flow tends to be laminar.

For pipe flow, the rough thresholds are: Re $< 2{,}000$, laminar; Re $> 3{,}000$, turbulent; in between, transitional. These are empirical boundaries, not derived from theory — turbulence is one of the genuinely hard unsolved problems of classical physics.

**A worked example: blood in a healthy artery.** Artery radius $r = 2.0 \text{ mm}$, length $L = 0.10 \text{ m}$, pressure drop $\Delta P = 100 \text{ Pa}$, blood viscosity $\eta = 4 \times 10^{-3} \text{ Pa·s}$.

Poiseuille flow rate:

$$Q = \frac{\pi (2.0 \times 10^{-3})^4 (100)}{8 (4 \times 10^{-3})(0.10)} \approx 1.6 \times 10^{-6} \text{ m}^3/\text{s} = 1.6 \text{ mL/s}.$$

Average flow speed: $v = Q / (\pi r^2) = 1.6 \times 10^{-6} / (\pi \times 4 \times 10^{-6}) \approx 0.13 \text{ m/s}$.

Reynolds number (using diameter $L = 4.0 \text{ mm}$, blood density $\rho = 1{,}060 \text{ kg/m}^3$):

$$\text{Re} = \frac{(1060)(0.13)(4.0 \times 10^{-3})}{4 \times 10^{-3}} \approx 137.$$

Re $\approx 137$, well below the laminar threshold. Flow is smoothly laminar. Poiseuille's law applies. Healthy arteries run laminar.

Now consider a stenosis — a narrowing that reduces the artery's cross-section to $1/4$ of normal, halving the radius. The same cardiac output must push through the constriction. By continuity, flow speed through the narrowing is four times higher. Reynolds number in the constriction:

$$\text{Re}_{\text{stenosis}} \approx 4 \times 137 \times \frac{r_{\text{old}}^2}{r_{\text{new}}^2} = 4 \times 137 \times 4 \approx 2{,}200.$$

![As cuff pressure deflates from above-systolic, three regimes appear: no flow (silent), turbulent intermittent flow (Korotkoff sounds — systolic to diastolic), and continuous laminar flow (silent again). Sounds bracket the two...](../images/12-fluid-dynamics-and-its-biological-and-medical-applications-fig-05.png)
*Figure 12.5 — Blood Pressure Measurement — Three Flow Regimes Across Cuff Pressure*

Now we're in the transitional regime, near turbulence. The turbulent flow makes a sound — an audible murmur. Physicians listen for exactly these sounds to diagnose arterial stenosis. The blood-pressure measurement described in the chapter's opening works on the same principle: turbulent Korotkoff sounds appear when cuff pressure is near systolic, because the artery is partially occluded, the constriction drives the Reynolds number into the turbulent range, and the turbulence is audible.

<!-- → [FIGURE: Cross-section of artery at healthy radius vs. stenosed radius (50% narrower). Velocity profile shown in each: broad parabolic Poiseuille profile in healthy artery (Re ~ 137, labeled "laminar"), narrower flattened profile in stenosed section (Re ~ 2200, labeled "transitional / turbulent"). Caption: Arterial stenosis drives up both flow speed and Reynolds number. The transition to turbulence produces audible sounds that clinicians use to diagnose blockages.] -->

---

## The three pieces, working together

Continuity, Bernoulli, and viscous flow each answer a different question.

**Continuity** answers: given the geometry, what happens to speed? The fluid speeds up when the pipe narrows, slows when it widens, and the product $Av$ stays constant.

**Bernoulli** answers: given the speed, what happens to pressure? Faster flow, lower pressure. The three energy terms — static pressure, kinetic energy density, gravitational energy density — sum to a constant along a streamline.

**Poiseuille and Reynolds** answer: does viscosity matter here, and is the flow smooth or chaotic? For slow, small-scale, viscous flows (blood in capillaries, lubrication films), Poiseuille applies. For fast, large-scale, inertia-dominated flows (household pipes, arteries at stenoses), the Reynolds number predicts turbulence and Bernoulli's frictionless picture applies better.

The scale shift is dramatic. A bacterium $1 \text{ μm}$ in radius swimming at $30 \text{ μm/s}$ through water has Reynolds number:

$$\text{Re} = \frac{(10^3)(3 \times 10^{-5})(2 \times 10^{-6})}{10^{-3}} \approx 6 \times 10^{-5}.$$

At Re $\approx 10^{-5}$, viscosity completely dominates inertia. The bacterium lives in a world where there is no coasting — stop swimming and you stop instantly. The inertia of the fluid is irrelevant; every stroke fights viscosity directly. This is why bacteria use rotating helical flagella rather than oar-like strokes: in low-Re flows, reciprocal motion (back and forth) produces no net displacement — a result called the *scallop theorem*. The physics of locomotion at the microscale is entirely different from the physics at the human scale.

A jumbo jet in cruise has Re $\approx 10^8$, twelve orders of magnitude away from the bacterium. Same equation, same physics, completely different regime. The Reynolds number tells you which.

<!-- → [CHART: Log-scale line showing Reynolds number for a range of real systems. Left to right: bacterium swimming (Re ~ 10⁻⁵), blood in capillary (Re ~ 10⁻³), blood in aorta (Re ~ 10³), kitchen faucet (Re ~ 10⁴), swimmer (Re ~ 10⁶), jumbo jet (Re ~ 10⁸). Vertical dashed lines at Re = 2000 (laminar → transitional) and 3000 (transitional → turbulent). Caption: Reynolds number spans fifteen orders of magnitude from swimming bacteria to aircraft. The same dimensionless ratio determines flow regime at every scale.] -->

---

## Exercises

### Warm-up

**12.1** *(LO 1)* Water flows through a $5.0 \text{ cm}$ diameter pipe at $2.0 \text{ m/s}$. (a) Cross-sectional area? (b) Volume flow rate in $\text{m}^3/\text{s}$ and L/min?

**12.2** *(LO 1)* A river $50 \text{ m}$ wide and $2.0 \text{ m}$ deep flows at $0.50 \text{ m/s}$. Volume flow rate?

**12.3** *(LO 2)* Water flows horizontally at $3.0 \text{ m/s}$ at gauge pressure $50 \text{ kPa}$. The pipe narrows, accelerating flow to $9.0 \text{ m/s}$. New gauge pressure?

**12.4** *(LO 4)* Water at $20°\text{C}$ flows through a $1.0 \text{ cm}$ diameter pipe at $0.50 \text{ m/s}$. Compute Re. Laminar or turbulent?

### Application

**12.5** *(LO 1, 2)* Water drains from a hole at depth $3.0 \text{ m}$ in a large reservoir. (a) Exit speed from Torricelli ($v = \sqrt{2gh}$). (b) Volume flow rate if the hole has area $5.0 \text{ cm}^2$.

**12.6** *(LO 3)* Volume flow rate through a horizontal pipe, radius $1.0 \text{ cm}$, length $5.0 \text{ m}$, $\eta = 10^{-3} \text{ Pa·s}$, pressure drop $200 \text{ Pa}$.

**12.7** *(LO 5)* Cardiac output is $5 \text{ L/min}$. Aortic radius is about $1.0 \text{ cm}$. (a) Average blood velocity in the aorta. (b) Reynolds number. Laminar or turbulent?

**12.8** *(LO 2)* Air ($\rho = 1.21 \text{ kg/m}^3$) flows at $100 \text{ m/s}$ over a wing's upper surface and $80 \text{ m/s}$ under the lower surface. What is the pressure difference between bottom and top?

### Synthesis

**12.9** *(LO 1, 2, 3)* A garden hose (inner diameter $1.5 \text{ cm}$) carries $5 \text{ L/min}$ over $20 \text{ m}$, supply pressure $250 \text{ kPa}$ above atmospheric. (a) Speed in hose. (b) Bernoulli pressure drop from speed alone. (c) Poiseuille pressure drop from viscosity. (d) Which dominates?

**12.10** *(LO 3, 5)* Atherosclerosis reduces an artery's radius by $25\%$. (a) By what factor does flow rate decrease at the same pressure? (b) By what factor must pressure increase to maintain the same flow rate?

**12.11** *(LO 4)* A swimmer moves at $1 \text{ m/s}$, characteristic body length $1.5 \text{ m}$, through water. Compute Re. Laminar or turbulent wake?

### Challenge

**12.12** *(LO 5, beyond chapter)* An aortic stenosis reduces the valve cross-section to $1/4$ normal. Cardiac output remains $5 \text{ L/min}$. (a) Velocity through the stenosed valve. (b) Reynolds number — turbulent? (c) Pressure drop across the stenosis using Bernoulli (ignore viscosity). Express in mmHg.

**12.13** *(beyond chapter)* A bacterium of radius $1 \text{ μm}$ swims through water at $30 \text{ μm/s}$. Compute Re. Explain what this means for how it must swim.

---

## LLM Exercise — Chapter 12: Fluid Dynamics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A flow-rate, pressure, or Reynolds-number analysis of one moving fluid in your anchor phenomenon.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics with LLMs. My anchor phenomenon is [paste 1-sentence description].

For Chapter 12, I want to apply fluid dynamics — continuity, Bernoulli, viscosity — to one flowing fluid in my phenomenon. Please:

1. Identify ONE moving fluid in my phenomenon. Examples:
   - Bike commute: air flowing around the body at riding speed (drag); blood flow in the rider during exertion.
   - Coffee maker: water flowing through coffee grounds during brewing; steam through wand.
   - Basketball: airflow around the spinning ball (Magnus effect).
   - Marathon: airflow around the runner; sweat evaporation.
   - Espresso: water at 9 bar through the coffee puck during extraction (this is the central flow event).

2. Identify the relevant equation: continuity (Av = const), Bernoulli (P + ½ρv² + ρgh = const), or Poiseuille (Q = πr⁴ΔP / 8ηL).

3. Compute the relevant quantities. Report with units, sig figs, uncertainty.

4. Compute the Reynolds number to determine flow regime (laminar, turbulent, transitional).

5. Sanity check with one Fermi estimate.

6. Identify which assumption (incompressible, frictionless, steady-state, ignored viscosity) is most likely to bite.

7. One sentence on how this connects to Chapter 13 (gas laws) — flowing gases involve compressibility that liquids don't.

Save the output as logbook/chapter-12-fluid-dynamics.md.
```

### What this produces

A twelfth Logbook entry: a fluid-flow analysis of one moving fluid in your phenomenon, often revealing the regime (laminar vs. turbulent) that governs which equations apply.

### How to adapt this prompt

- *For phenomena with mostly slow flow* (a coffee drip): use Stokes / low-Re analysis.
- *For phenomena with high-speed flow* (a basketball through air): apply turbulent drag from Ch. 5.
- *For ChatGPT or Gemini:* identical with substitutions.
- *For Claude Code:* if you have flow data (water-meter readings, blood-pressure log), paste it.

### Connection to previous chapters

Builds directly on Chapter 11 (pressure, density, fluid statics). Builds on Chapter 7 (Bernoulli is energy conservation for fluids). Builds on Chapter 5 (drag — Reynolds number connects).

### Preview of next chapter

Chapter 13 introduces temperature and the kinetic theory of gases. Gases are compressible and their behavior couples to temperature. Many fluid-dynamic phenomena in gases (lift, sound, weather) involve both fluid dynamics and gas-law thermodynamics together.

---

**Tags:** fluid-dynamics, Bernoulli, continuity, Poiseuille, Reynolds-number
