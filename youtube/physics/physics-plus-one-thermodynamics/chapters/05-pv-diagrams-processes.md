# Chapter 5 — Thermodynamic Processes and PV Diagrams

*Four canonical paths, the area under the curve, and the first thermodynamic cycle.*

---

## The Pressure-Volume Diagram

I want to start with something that sounds almost too simple to bother with.

A gas has a pressure. It has a volume. If we write those two numbers down — $P$ on one axis, $V$ on the other — we get a point. That point is the *state* of the gas. Everything about the gas's macroscopic condition is captured in that dot on the diagram (given that we also know $n$, because $T$ follows from $PV = nRT$).

Now suppose we change the gas slowly — compress it, heat it, let it expand. The point moves. It traces a *curve*. That curve is a *process*. And if we run the gas through a sequence of processes that brings it back to where it started, the curve closes on itself. That closed curve is a *cycle*.

This is the PV diagram. It's a map. Every quasi-static process the gas can undergo is a path on this map; every state is a point; every cycle is a closed loop. Once you learn to read it, you can analyze any heat engine in the world without doing anything more complicated than identifying curves and measuring areas.

The reason we care about areas is this. The work done *by* the gas during any quasi-static process — any process slow enough that the gas remains in equilibrium throughout — is:

$$W = \int_{V_i}^{V_f} P\,dV$$

That's the area under the $P(V)$ curve, between the initial and final volumes. If the gas expands (moves right on the diagram), it does positive work. If it's compressed (moves left), work is done *on* the gas and $W$ is negative. For a complete cycle, the net work is the *enclosed* area.

<!-- → [DIAGRAM: PV axes (P vertical, V horizontal) with a single smooth process curve from state A (left) to state B (right); the region between the curve and the V-axis shaded in a single color — caption: "The shaded area IS the work; this is not a metaphor, it is the definition. Expansion rightward = positive; compression leftward = negative."] -->

This is not an approximation. It's exact, for quasi-static processes. It follows directly from the definition of work: force times displacement. In a cylinder, the force the gas exerts on a piston is $F = PA$; the displacement of the piston is $dL$; the volume change is $dV = A\,dL$. So $F\,dL = P\,dV$. That's it. The integral over the process gives you the work.

---

## The Four Processes

There are four processes worth knowing by name. Each one holds something constant, and each one has a distinctive shape on the PV diagram.

**Isothermal** — temperature constant. From $PV = nRT$, if $T$ is constant then $PV = \text{constant}$. On the PV diagram, that's a hyperbola — curves that sweep down and to the right, one hyperbola per temperature. Hotter gas sits on a higher hyperbola; cooler gas on a lower one. The work is:

$$W_{\text{iso}} = nRT\ln\!\left(\frac{V_f}{V_i}\right)$$

For an ideal gas, internal energy depends only on temperature: $\Delta U = nC_V\Delta T = 0$ during an isothermal. So all the work the gas does comes straight from heat absorbed: $Q = W$.

**Isochoric** — volume constant. Vertical line on the PV diagram. The gas can't move the piston, so $W = 0$. All the heat goes into changing the internal energy: $Q = \Delta U = nC_V\Delta T$.

**Isobaric** — pressure constant. Horizontal line. Work is simply $W = P\Delta V$. Heat goes partly into work, partly into raising the internal energy: $Q = nC_P\Delta T$, where $C_P > C_V$ by exactly $R$ per mole (because at constant pressure, some of the heat must do the work of expansion).

**Adiabatic** — no heat exchange, $Q = 0$. This one has the richest shape, and I want to spend a moment on why. If the gas can't exchange heat with anything, then all the work it does comes out of its internal energy: $dU = -P\,dV$. Combined with $dU = nC_V\,dT$ and the ideal-gas law, this gives the adiabatic constraint:

$$PV^\gamma = \text{constant}$$

where $\gamma = C_P/C_V$ is the ratio of heat capacities. For a monatomic gas like helium, $\gamma = 5/3 \approx 1.67$. For a diatomic gas like the nitrogen and oxygen in air, at moderate temperatures, $\gamma = 7/5 = 1.40$.

On the PV diagram, an adiabat looks like a hyperbola — but it's *steeper* than the isothermal at the same point. The slope of an isotherm at any point is $-P/V$. The slope of an adiabat is $-\gamma P/V$. Since $\gamma > 1$, the adiabat always slopes more steeply.

This has a physical interpretation. When a gas expands isothermally, it stays warm by absorbing heat from outside — so pressure doesn't fall as fast. When it expands adiabatically, it gets no heat from anywhere, so the temperature drops as the gas does work, and the pressure falls faster. The adiabat curves away beneath the isotherm.

Work along an adiabat:

$$W_{\text{ad}} = \frac{P_i V_i - P_f V_f}{\gamma - 1} = -\Delta U = -nC_V\Delta T$$

<!-- → [DIAGRAM: Single PV diagram showing all four process types originating from the same point — isothermal hyperbola (label: "isothermal, T = const"), adiabat (steeper, label: "adiabatic, Q = 0"), horizontal line (label: "isobaric, P = const"), vertical line (label: "isochoric, V = const"); the isothermal and adiabat should diverge visibly from each other to make the steepness comparison unmistakable; γ annotation at the divergence point] -->

---

## A Worked Example

Let me work through a specific case so you can see the machinery in action.

A gas at $P_i = 3$ atm $= 3.04 \times 10^5$ Pa occupies $V_i = 2$ L $= 2 \times 10^{-3}$ m³. It expands adiabatically ($\gamma = 1.4$) to $V_f = 6$ L.

First, find the final pressure using $PV^\gamma = \text{const}$:

$$P_f = P_i\left(\frac{V_i}{V_f}\right)^\gamma = 3.04 \times 10^5 \cdot \left(\frac{2}{6}\right)^{1.4}$$

$(2/6)^{1.4} = (0.333)^{1.4}$. Now, $0.333 = 3^{-1}$, so this is $3^{-1.4} \approx 0.209$. Therefore $P_f \approx 3.04 \times 10^5 \times 0.209 = 6.35 \times 10^4$ Pa.

Work done by the gas:

$$W = \frac{P_i V_i - P_f V_f}{\gamma - 1} = \frac{(3.04 \times 10^5)(2 \times 10^{-3}) - (6.35 \times 10^4)(6 \times 10^{-3})}{0.4}$$

$$= \frac{608 - 381}{0.4} = \frac{227}{0.4} = 567 \text{ J}$$

Since $Q = 0$, $\Delta U = -567$ J. The gas cooled. You can verify: $\Delta U = nC_V\Delta T$, and the temperature dropped from $T_i = P_i V_i/(nR)$ to a lower value.

Compare this to the same expansion done isothermally, at temperature $T_i = P_i V_i/(nR)$. Work done isothermally: $W = nRT_i \ln(V_f/V_i)$. We don't need $n$ separately — note that $nRT_i = P_i V_i = 608$ J, so:

$$W_{\text{iso}} = 608 \cdot \ln(3) = 608 \cdot 1.099 = 668 \text{ J}$$

The isothermal process does *more* work than the adiabatic for the same volume change, starting from the same state. That's the area difference between the two curves on the PV diagram — the isotherm sits higher (warmer gas, maintained by heat input), so more area lies under it.

<!-- → [DIAGRAM: Two curves on the same PV diagram, both starting from the same point (P_i, V_i) and ending at the same V_f — isothermal hyperbola above, adiabat below; both shaded areas under the curves to the V-axis; the isothermal shaded region visibly larger; difference region between the two curves highlighted; caption: "The gap between the curves is the gap in work: the isotherm gets heat from outside, so it stays warmer and pushes harder all the way to V_f."] -->

---

## Cycles and the Engine

Now for the really useful idea.

Suppose we run a gas through a sequence of processes that brings it back to its starting state. The gas returns to the same $P$, $V$, and $T$ it started with — meaning $\Delta U = 0$ for the whole cycle. From the first law:

$$\Delta U = Q_{\text{net}} - W_{\text{net}} = 0 \implies Q_{\text{net}} = W_{\text{net}}$$

All the net heat absorbed by the gas over the cycle equals the net work done by the gas. That work is the area enclosed by the closed curve on the PV diagram.

The direction matters. A cycle traversed *clockwise* — expanding at high pressure, compressing at low pressure — does net positive work. It's a *heat engine*: it absorbs heat from a hot reservoir and converts some of it to work, dumping the rest as exhaust. A cycle traversed *counterclockwise* requires net work input. That's a *refrigerator*.

The simplest engine worth analyzing is the **Otto cycle** — the idealized model of the four-stroke gasoline engine in your car.

The Otto cycle has four steps:

**1→2. Adiabatic compression.** The air-fuel mixture is compressed quickly. No heat exchanges (the stroke is too fast for significant heat transfer to cylinder walls). The gas goes from the large volume $V_1$ to the small volume $V_2 = V_1/r$, where $r$ is the *compression ratio* — typically 8 to 12 in modern gasoline engines. On the PV diagram: steep curve upward to the left.

**2→3. Isochoric heat addition.** The spark plug fires. Combustion adds heat $Q_H$ to the gas at essentially constant volume (the explosion is fast compared to piston motion). Pressure jumps. Vertical line upward.

**3→4. Adiabatic expansion.** The hot, high-pressure gas drives the piston down. Another steep adiabatic curve, now to the lower right. This is the power stroke.

**4→1. Isochoric heat rejection.** The exhaust valve opens; hot exhaust gas is replaced by cool fresh mixture. Modeled as cooling at constant volume. Pressure drops. Vertical line downward.

The cycle is now closed. The enclosed area is the net work per cycle.

<!-- → [DIAGRAM: Full Otto cycle on a PV diagram — four labeled states (1, 2, 3, 4); two steep adiabatic curves (1→2 compression, 3→4 expansion) in one color; two vertical isochoric lines (2→3 heat addition, 4→1 heat rejection) in another color; enclosed area shaded and labeled "net work per cycle W"; arrows showing direction of traversal (clockwise); V_1 and V_2 marked on V-axis with compression ratio r = V_1/V_2 annotated; this should be the primary reference figure for the Otto cycle derivation that follows] -->

To find the efficiency — the fraction of $Q_H$ that comes out as work — we apply the first law to each leg.

The isochoric legs (2→3 and 4→1) are the only ones involving heat. For an ideal gas with $n$ moles:

$$Q_H = nC_V(T_3 - T_2) \qquad Q_C = nC_V(T_4 - T_1)$$

Net work: $W = Q_H - Q_C$. Efficiency:

$$\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H} = 1 - \frac{T_4 - T_1}{T_3 - T_2}$$

Now I use the adiabatic constraint on the two adiabatic legs. For 1→2: $T_1 V_1^{\gamma-1} = T_2 V_2^{\gamma-1}$, giving $T_2 = T_1 r^{\gamma-1}$. For 3→4: $T_3 V_2^{\gamma-1} = T_4 V_1^{\gamma-1}$, giving $T_4 = T_3 / r^{\gamma-1}$.

Notice: $T_2/T_1 = T_3/T_4 = r^{\gamma-1}$. This means $T_4 - T_1 = (T_3 - T_2)/r^{\gamma-1}$. Plugging in:

$$\boxed{\eta_{\text{Otto}} = 1 - \frac{1}{r^{\gamma-1}}}$$

That's a clean result. Efficiency depends only on the compression ratio $r$ and $\gamma$. For $r = 10$, $\gamma = 1.4$:

$$\eta = 1 - 10^{-0.4} = 1 - 0.398 = 60.2\%$$

Real gasoline engines achieve 25–35%. The gap comes from heat losses to the cylinder walls, finite combustion time, friction, pumping losses in the intake and exhaust strokes, and the fact that the working fluid isn't actually an ideal gas — combustion products have different $\gamma$ than fresh air. The Otto cycle is not a target; it's an upper bound on what the thermodynamics alone permits.

<!-- → [CHART: Line chart of η_Otto = 1 − 1/r^(γ−1) vs. compression ratio r from 1 to 20, for γ = 1.4 (diatomic air); mark the typical gasoline range r = 9–12 with a shaded band; mark the diesel range r = 15–22 with a second band; add a horizontal dashed line at η = 1.0 labeled "impossible limit"; add a horizontal band at η = 0.25–0.35 labeled "real gasoline engines" and a band at η = 0.40–0.45 labeled "real diesel engines" — student should see immediately why diesel beats gasoline (higher r) and why real engines fall short of the theoretical curve] -->

Diesel engines reach 40–45% efficiency. The reason is compression ratio: diesel engines compress to $r \approx 15$–22 (versus 9–12 for gasoline). You can't compress gasoline-air mixture that aggressively without pre-ignition — the mixture ignites spontaneously from the heat of compression ("knock"), which is destructive. Diesel fuel is much less volatile and doesn't pre-ignite. Higher $r$ means higher efficiency. The diesel also uses a *different cycle* (isobaric heat addition rather than isochoric), but the dominant factor is $r$.

---

## What the PV Diagram Tells You — and What It Doesn't

The PV diagram is a tool for quasi-static processes. That word "quasi-static" means the process happens slowly enough that the gas is in equilibrium at every instant — effectively a sequence of equilibrium states connected in a smooth path. For quasi-static processes, the curves we've been drawing are exact representations of what happens.

For non-quasi-static processes — a gas rushing through a broken membrane into vacuum, or an explosion — the formula $W = \int P\,dV$ isn't directly applicable, because the gas isn't in a well-defined pressure state during the process. (For free expansion into vacuum specifically, $W = 0$ regardless: there's no force on any piston, so no work is done, and the integral isn't meaningful.) The first law $\Delta U = Q - W$ still holds — it always holds — but you have to compute $W$ from external constraints rather than reading it off the diagram.

There's something deeper the PV diagram doesn't tell you: *direction*. Given two states on the diagram, the PV diagram will show you both a path from A to B and a path from B to A, and it says nothing about which direction is *spontaneous*. A gas can expand isothermally and do work. Can it un-expand — spontaneously compress and generate cold? The first law doesn't forbid it; it just says energy must be conserved. But it doesn't happen. The reason it doesn't happen is the second law, which is where we're going next.

The PV diagram encodes the *mechanics* of thermodynamics. What it leaves out is the *arrow of time* — the direction in which real processes proceed. That's Chapter 6.

---

## Common Misconceptions

*"Adiabatic and isothermal curves look the same."* They do look qualitatively similar — both sweep down and to the right. The difference is steepness. At any point, the adiabat is steeper than the isotherm passing through that same point by a factor of $\gamma$. Draw them through the same starting point and they diverge immediately: the adiabat drops faster.

*"The area enclosed by a cycle is the heat added."* No — it's the net *work*. The heat added and heat rejected are properties of specific legs; the area is the difference between them. It equals net heat only because $\Delta U = 0$ for a complete cycle.

*"Otto cycle efficiency is what real engines achieve."* It's the *upper bound*. Real engines fall well short because the Otto cycle assumes ideal-gas behavior, perfectly instantaneous combustion, zero friction, and no heat transfer through the walls. Real efficiencies are roughly half the Otto value.

*"A cycle must go clockwise."* A clockwise cycle is an engine. A counterclockwise cycle is a refrigerator. The same shape, traversed in opposite directions, has the same enclosed area but opposite sign of net work.

---

## What Would Change My Mind

None of this is contested. The PV diagram follows from the ideal-gas law and the definition of work; the process formulas follow from applying the first law to each constrained case; the Otto efficiency formula is a straightforward derivation. Experiments on ideal-gas systems confirm all of it.

What's genuinely open isn't the PV diagram — it's what happens *between* states during non-quasi-static processes. The diagram describes idealized paths. Real compressions and expansions happen fast, generate turbulence, and produce entropy that the PV diagram doesn't show. The PV diagram is a useful, accurate idealization. Knowing when the idealization breaks down is what separates a physicist from a textbook follower.

---

## Still Puzzling

*Why $PV^\gamma = \text{const}$ for an adiabat?* It falls out of the math cleanly enough — first law applied to an adiabatic process, combined with the ideal-gas law — but the *physical* content is worth pausing on. The exponent $\gamma$ encodes how energy distributes among a molecule's degrees of freedom. A monatomic gas stores energy only in translational motion (3 degrees), giving $\gamma = 5/3$. A diatomic gas also stores energy in rotation (2 more degrees at moderate temperatures), giving $\gamma = 7/5$. A more "floppy" molecule with more degrees of freedom has lower $\gamma$, meaning less steep adiabats, meaning the molecule's internal complexity lets it absorb more of the compression energy internally rather than returning it to pressure. The structure of the molecule is literally written into the shape of the adiabat.

*What happens at the corners of a cycle?* The Otto cycle has sharp corners on the PV diagram — for instance, the instantaneous transition from adiabatic expansion to isochoric cooling. Real engines don't make instantaneous transitions; every corner is rounded by finite-time effects. The idealized cycle is a useful approximation, but the corners are where the approximation is least accurate.

---

## Exercises

**Warm-up 1** *(Apply — isobaric work)*. A gas at $P = 2.5$ atm expands isobarically from $V_i = 3$ L to $V_f = 7$ L. Compute the work done by the gas in joules. What is $\Delta U$ if no heat is added? What does that tell you?

**Warm-up 2** *(Apply — isothermal work)*. One mole of ideal gas at $T = 350$ K expands isothermally to twice its initial volume. Find $W$, $Q$, and $\Delta U$. Verify that your result is consistent with the first law.

**Warm-up 3** *(Apply — adiabatic process)*. A monatomic ideal gas ($\gamma = 5/3$) at $P_i = 4$ atm, $V_i = 1$ L is compressed adiabatically to $V_f = 0.25$ L. Find $P_f$, $T_f/T_i$, and the work done *on* the gas.

**Application 1** *(Apply — identifying steepness)*. At a given point on the PV diagram, a gas has $P = 3 \times 10^5$ Pa and $V = 2 \times 10^{-3}$ m³, with $\gamma = 1.4$. Compute the slope of the isothermal curve passing through this point and the slope of the adiabatic curve. By what factor do they differ, and why?

**Application 2** *(Apply — rectangular cycle)*. A cycle traces a rectangle on the PV diagram: corners at $(V_1, P_1) = (1\ \text{L},\ 1\ \text{atm})$, $(V_2, P_1) = (4\ \text{L},\ 1\ \text{atm})$, $(V_2, P_2) = (4\ \text{L},\ 3\ \text{atm})$, $(V_1, P_2) = (1\ \text{L},\ 3\ \text{atm})$. Traversed clockwise: find $W_{\text{net}}$. Then traverse it counterclockwise and interpret the sign of $W_{\text{net}}$.

**Application 3** *(Apply — Otto cycle states)*. An Otto cycle: $\gamma = 1.4$, $r = 8$, $T_1 = 300$ K, $Q_H = 1200$ J per cycle, $n = 0.05$ mol. Find $T_2$, $T_3$, $T_4$, $\eta_{\text{Otto}}$, and $W_{\text{net}}$.

**Synthesis 1** *(Analyze — comparing cycles)*. Two cycles start from the same state $(P_1, V_1)$ and both end at $(P_1, 3V_1)$. Cycle A: isothermal expansion, then isochoric cooling back to $P_1$, then isobaric compression back to $V_1$. Cycle B: adiabatic expansion to the same final $V$, then isochoric heating to $P_1$, then isobaric compression back. Which cycle encloses more area? Which does more net work? What does this tell you about the relative efficiency of using isothermal vs. adiabatic expansion in a cycle?

**Synthesis 2** *(Analyze — the direction question)*. A gas undergoes a complete clockwise cycle and does net work $W > 0$. The first law for the cycle gives $Q_{\text{net}} = W$. Where did this energy come from? Trace the flow: which leg(s) absorbed heat, which rejected it, and how does the enclosed area connect to the net heat exchange? Now reverse the cycle (counterclockwise). Redo the energy accounting.

**Challenge** *(Analyze + Apply — the diesel cycle)*. The diesel cycle replaces the Otto cycle's isochoric heat addition with *isobaric* heat addition (the fuel burns more slowly, at roughly constant pressure). The four legs are: adiabatic compression ($V_1 \to V_2$), isobaric heat addition ($V_2 \to V_3$), adiabatic expansion ($V_3 \to V_1$), isochoric heat rejection ($V_1$, pressure drops). Define the cutoff ratio $r_c = V_3/V_2$. Derive the diesel cycle efficiency:

$$\eta_{\text{Diesel}} = 1 - \frac{1}{r^{\gamma-1}} \cdot \frac{r_c^\gamma - 1}{\gamma(r_c - 1)}$$

For $r = 18$, $r_c = 2$, $\gamma = 1.4$: compute $\eta_{\text{Diesel}}$ and compare to $\eta_{\text{Otto}}$ at the same $r$. The diesel is lower efficiency at the same compression ratio. Why, then, do diesel engines beat gasoline engines in practice?

---

## LLM Exercises

### Build the PV diagram simulator (`05-pv-diagram.html`)

> **Show.** Four processes: isothermal $PV = \text{const}$, isochoric $V = \text{const}$, isobaric $P = \text{const}$, adiabatic $PV^\gamma = \text{const}$. Work = area under curve.
>
> **Say.** Build an interactive PV-diagram simulator with all four process types and cycle chains.
>
> **Constrain.** D3 v7. PV axes with isothermal hyperbolas drawn as background grid (at several reference temperatures). Initial state controls (sliders for $P_0, V_0, T_0$, and $n$). Process selector (isothermal/isochoric/isobaric/adiabatic). Final-state slider. The process plays as an animated curve on the diagram; work computed as shaded area; $Q, \Delta U$, $W$ displayed numerically. Cycle mode: chain up to 4 processes; show the closed path; net work = enclosed area. Preset: Otto cycle. Filename: `05-pv-diagram.html`.
>
> **Verify.** (a) Isothermal: hyperbola. (b) Adiabatic: steeper than isothermal at any point. (c) Isobaric: horizontal. (d) Isochoric: vertical. (e) Otto cycle enclosed area = work computed analytically.

### Exploration

- Build an Otto cycle. Vary $r$ from 5 to 15. Plot efficiency vs. $r$. Compare to $1 - 1/r^{\gamma-1}$.
- Run two cycles starting from the same state: isothermal expansion then isochoric heating then isobaric compression vs. adiabatic expansion then isochoric heating then isobaric compression. Which produces more net work? Both end at the same final state, but the paths differ.
- Reverse a cycle (go counterclockwise). The same shape, but work is now negative — work is done on the gas. This is a refrigerator.

### Extension prompt (chapter bridge)

> **Show.** I've analyzed thermodynamic cycles that do net work. Now I want to understand the *limit* on how efficient any cycle can be — and why no engine can convert all heat to work.
>
> **Say.** Build a Carnot cycle simulator showing the upper bound on heat-engine efficiency.
>
> **Constrain.** Two isothermals (at $T_H$ and $T_C$) connected by two adiabats. Show the cycle on both PV and TS diagrams. Display Carnot efficiency $\eta_C = 1 - T_C/T_H$. Slider for $T_H$ and $T_C$.
>
> **Verify.** Carnot efficiency $< 1$ for any finite $T_H$. As $T_C/T_H \to 0$, $\eta \to 1$ (impossible to reach). As $T_C/T_H \to 1$, $\eta \to 0$ (no heat differential = no work).

Save as `05b-carnot-preview.html`. Bridge to Chapter 6.

---

**Tags:** PV diagram, isothermal, isochoric, isobaric, adiabatic, thermodynamic cycle, Otto cycle, compression ratio, heat engine, work as area
