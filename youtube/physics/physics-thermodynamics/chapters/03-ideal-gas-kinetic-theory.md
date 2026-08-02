# Chapter 3 — The Ideal Gas and Kinetic Theory


## TL;DR

- Deriving $PV = NkT$ from molecular collisions, and the Maxwell-Boltzmann distribution.
- The chapter moves through The molecular derivation of $PV = NkT$, The model and its assumptions, The Maxwell-Boltzmann distribution, How temperature and mass shift the distribution, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Deriving $PV = NkT$ from molecular collisions, and the Maxwell-Boltzmann distribution.*

---

Mars is losing its atmosphere. Not quickly — not on any timescale a human would notice — but over billions of years, the lighter molecules in the Martian atmosphere have been slowly leaking away into space. Hydrogen is essentially gone. Helium is gone. The atmosphere today is 95% carbon dioxide at a pressure of about 6 millibars — less than one percent of Earth's.

The reason is a tail.

The escape velocity from Mars is about 5 km/s. The root-mean-square speed of a hydrogen molecule at 200 K — the temperature of the Martian upper atmosphere — is about 1.6 km/s. Far below escape velocity. So hydrogen should stay, right? It doesn't. Because the rms speed is an average, and molecules are not all moving at the average. The Maxwell-Boltzmann distribution — the curve that describes how molecular speeds are spread out — has a long tail extending to high speeds. A small fraction of hydrogen molecules, at any given moment, are moving much faster than the average. Fast enough to escape.

That fraction is small. Maybe one in a thousand. But "one in a thousand escapes per unit time" compounded over four billion years empties an atmosphere. The tail is the story.

This chapter derives that distribution. Along the way it also derives the ideal gas law — not as a postulate, but as a consequence of molecular mechanics. The big move is from the microscopic to the macroscopic: from molecules bouncing off walls to pressure, temperature, and volume as the things we can measure.

---

## The molecular derivation of $PV = NkT$

Imagine a box of side length $L$, volume $V = L^3$, containing $N$ molecules each of mass $m$. Pick one molecule moving in the $+x$ direction with speed $v_x$. When it hits the right wall and bounces back elastically, the momentum transferred to the wall is $\Delta p = 2mv_x$. The time between successive collisions with the same wall is $2L/v_x$ — the molecule has to travel to the far wall and come back. So the average force that molecule exerts on the right wall is:

$$F = \frac{\Delta p}{\Delta t} = \frac{2mv_x}{2L/v_x} = \frac{mv_x^2}{L}$$

Now sum over all $N$ molecules. Not all of them are moving in the $x$ direction, of course. In a gas in equilibrium, molecular motion is isotropic — no direction is preferred. So $\langle v_x^2 \rangle = \langle v_y^2 \rangle = \langle v_z^2 \rangle = \langle v^2 \rangle / 3$. The total force on the right wall is:

$$F_{\text{total}} = \frac{Nm\langle v_x^2 \rangle}{L} = \frac{Nm\langle v^2 \rangle}{3L}$$

Pressure is force per area. The wall has area $L^2$:

$$P = \frac{F_{\text{total}}}{L^2} = \frac{Nm\langle v^2 \rangle}{3L^3} = \frac{Nm\langle v^2 \rangle}{3V}$$

Now recall from Chapter 2 that temperature is defined by $T = m\langle v^2 \rangle / (3k_B)$, which means $m\langle v^2 \rangle = 3k_BT$. Substitute:

$$P = \frac{N \cdot 3k_BT}{3V} = \frac{Nk_BT}{V}$$

$$\boxed{PV = Nk_BT}$$

That is the ideal gas law — not postulated, but derived from Newton's second law applied to bouncing molecules plus the molecular definition of temperature. In terms of moles, where $N = nN_A$ and $R = N_A k_B = 8.314$ J/(mol·K):

$$PV = nRT$$

The ideal gas law is not a fundamental law of nature. It is a consequence of a model: point particles, no intermolecular forces, elastic collisions. When those assumptions hold — low density, moderate temperature, far from any phase transition — the law works with remarkable accuracy. When they fail, we need corrections.

---

## The model and its assumptions

The ideal gas model makes four claims about the molecules:

They are point particles with no internal structure. They move randomly, with speeds distributed according to the Maxwell-Boltzmann distribution. They collide elastically with each other and the container walls — no energy is lost to vibration of the wall or to internal molecular modes. And they exert no forces on each other except during collisions — no attraction at distance, no repulsion until contact.

None of these is exactly true for any real gas. Real molecules have finite size. They attract each other weakly at intermediate distances and repel strongly at short distances. Collisions with walls are not perfectly elastic — walls heat up. But at low density and moderate temperature, the corrections are small. The ideal gas model is the right starting point, and real-gas behavior is a perturbation on top of it.

There is a useful way to think about when the model breaks down. The corrections matter when (a) the volume of the molecules themselves is not negligible compared to the container volume, or (b) when the average kinetic energy per molecule is comparable to the intermolecular potential energy. Both conditions are met at high pressure or low temperature — near liquefaction. The correction that addresses both is the van der Waals equation, which I will return to at the end of this chapter.

---

## The Maxwell-Boltzmann distribution

The ideal gas law tells us about averages. But the atmosphere-escape story requires knowing not just the average molecular speed, but how the speeds are *distributed* — specifically, how much probability sits in the tail.

The distribution of molecular speeds in an ideal gas at temperature $T$ is:

$$f(v) = 4\pi \left(\frac{m}{2\pi k_B T}\right)^{3/2} v^2 \, e^{-mv^2/(2k_BT)}$$

This is the Maxwell-Boltzmann speed distribution. Maxwell derived it in 1860 by a statistical argument; Boltzmann later gave it a more rigorous foundation in statistical mechanics. We will rederive it properly in Chapter 9 using the Boltzmann distribution. For now, let me explain what each piece means and why the distribution has the shape it does.

The factor $e^{-mv^2/(2k_BT)}$ is the Boltzmann factor. It says that the probability of a molecule having kinetic energy $E = \frac{1}{2}mv^2$ is proportional to $e^{-E/k_BT}$. High-energy states are exponentially suppressed. This factor alone would give a distribution that decreases monotonically from zero speed — but that is not what we observe, because at exactly $v = 0$ the probability also goes to zero.

The reason is the $v^2$ factor in front. Speed is a magnitude — it is always positive. In three dimensions, the number of ways to have speed between $v$ and $v + dv$ is proportional to the surface area of a sphere of radius $v$ in velocity space, which is $4\pi v^2$. There are many more ways to have speed 400 m/s than speed 1 m/s, just from geometry. The $v^2$ factor multiplied by the decaying exponential produces a distribution that starts at zero, rises to a peak, then falls off exponentially.

The peak — the most probable speed — is where $d(v^2 e^{-mv^2/2k_BT})/dv = 0$. Working it out:

$$v_{mp} = \sqrt{\frac{2k_BT}{m}}$$

The mean speed, found by computing $\int_0^\infty v f(v) \, dv$, is:

$$v_{avg} = \sqrt{\frac{8k_BT}{\pi m}}$$

The root-mean-square speed, found from $\sqrt{\langle v^2 \rangle} = \sqrt{\int_0^\infty v^2 f(v) \, dv}$, is:

$$v_{rms} = \sqrt{\frac{3k_BT}{m}}$$

These three speeds are related by fixed numerical factors: $v_{mp} : v_{avg} : v_{rms} = 1 : \sqrt{4/\pi} : \sqrt{3/2} \approx 1 : 1.128 : 1.225$. They are always in this order. The distribution is asymmetric — skewed right — because the Boltzmann exponential cuts off the high-speed tail steeply, but the $v^2$ factor suppresses the low-speed end even more steeply.

Let me compute all three for oxygen (O₂, molar mass $M = 32$ g/mol) at room temperature ($T = 300$ K). The molecular mass is $m = 0.032/6.022 \times 10^{23} = 5.31 \times 10^{-26}$ kg.

$$v_{mp} = \sqrt{\frac{2 \times 1.38 \times 10^{-23} \times 300}{5.31 \times 10^{-26}}} = \sqrt{1.56 \times 10^5} \approx 395 \text{ m/s}$$

$$v_{avg} = \sqrt{\frac{8}{\pi}} \times \sqrt{\frac{k_BT}{m}} = \sqrt{\frac{8}{\pi}} \times \sqrt{7.8 \times 10^4} \approx 446 \text{ m/s}$$

$$v_{rms} = \sqrt{\frac{3 \times 1.38 \times 10^{-23} \times 300}{5.31 \times 10^{-26}}} = \sqrt{2.34 \times 10^5} \approx 484 \text{ m/s}$$

Ordering confirmed: $395 < 446 < 484$. Oxygen molecules at room temperature are moving at about 400–500 m/s — comparable to the speed of sound in air, which is not a coincidence. Sound is a pressure wave propagated by molecular collisions; its speed is bounded by how fast the molecules themselves move.

---

## How temperature and mass shift the distribution

Two parameters control the shape of the Maxwell-Boltzmann distribution: temperature and molecular mass.

Temperature: all three characteristic speeds scale as $\sqrt{T}$. Double the temperature and the speeds increase by $\sqrt{2} \approx 1.41$. The distribution shifts right and broadens. What was the far tail at low temperature moves into the body of the distribution at high temperature.

Molecular mass: all three speeds scale as $1/\sqrt{m}$. Heavier molecules at the same temperature are slower. Hydrogen ($m \approx 2$ amu) at 300 K has $v_{rms} \approx 1930$ m/s. Nitrogen ($m \approx 28$ amu) at 300 K has $v_{rms} \approx 515$ m/s. Argon ($m \approx 40$ amu) at 300 K has $v_{rms} \approx 431$ m/s. The speed ratio scales as $\sqrt{m_N/m_H} = \sqrt{14} \approx 3.7$, and indeed hydrogen moves about 3.7 times faster than nitrogen at the same temperature.

This mass dependence is the physics of atmospheric escape. Earth's escape velocity is 11.2 km/s — far above the rms speed of any significant atmospheric component at normal temperatures. Even hydrogen at 300 K has $v_{rms} = 1930$ m/s, roughly six times below escape velocity. But the tail of the Maxwell-Boltzmann distribution reaches arbitrarily high speeds. The fraction of hydrogen molecules above 11.2 km/s is about $10^{-50}$ — essentially zero. Earth keeps its hydrogen.

For Mars, with escape velocity 5.0 km/s and upper-atmosphere temperatures around 200 K, the tail fraction for hydrogen is about $10^{-3}$. One in a thousand hydrogen molecules is moving fast enough to escape at any moment. That rate, sustained over four billion years, is enough to strip the atmosphere. Nitrogen ($m = 28$) at the same conditions has an escape fraction closer to $10^{-100}$ — so Mars has kept its nitrogen and CO₂ while losing its hydrogen. The composition of a planetary atmosphere is a long integral of this distribution over geological time.

---

## The equipartition theorem

There is a simpler way to read the ideal gas law. It says $PV = Nk_BT$, and the pressure derivation shows that this equals $(2/3)N \times \langle KE \rangle_{\text{translational}}$. The average translational kinetic energy per molecule is therefore $\frac{3}{2}k_BT$ — three halves, one half for each spatial dimension.

This is the equipartition theorem in its simplest form: each translational degree of freedom carries average energy $\frac{1}{2}k_BT$. "Degree of freedom" means an independent quadratic term in the energy — a mode that stores energy as the square of some coordinate or velocity component.

Translation in $x$, $y$, $z$: three terms, $(1/2)mv_x^2 + (1/2)mv_y^2 + (1/2)mv_z^2$. Total translational energy per molecule: $\frac{3}{2}k_BT$.

For a diatomic molecule — N₂, O₂, CO — there are also rotational modes. A dumbbell-shaped molecule can rotate about two axes perpendicular to the molecular bond; rotation about the bond axis itself contributes negligible energy (the moment of inertia about that axis is nearly zero for pointlike atoms). So two rotational degrees of freedom: $\frac{1}{2}I_1\omega_1^2 + \frac{1}{2}I_2\omega_2^2$. Total energy per molecule at moderate temperatures: $(3/2 + 2/2)k_BT = \frac{5}{2}k_BT$.

At very high temperatures, vibrational modes activate. A diatomic molecule can vibrate along its bond, storing energy as both kinetic and potential energy — two quadratic terms per vibrational mode. When vibration is fully excited, total energy per molecule is $\frac{7}{2}k_BT$.

The molar heat capacity at constant volume is $C_V = \partial U/\partial T = (f/2)Nk_B = (f/2)nR$, where $f$ is the number of active degrees of freedom. For a monatomic gas: $f = 3$, $C_V = \frac{3}{2}R \approx 12.5$ J/(mol·K). For a diatomic gas at moderate temperature: $f = 5$, $C_V = \frac{5}{2}R \approx 20.8$ J/(mol·K). These predictions match experimental data for noble gases and diatomic gases at room temperature with remarkable precision.

But there is a problem. At low temperatures, $C_V$ for a diatomic gas drops toward $\frac{3}{2}R$ — as if the rotational modes have been "frozen out." At room temperature, vibration is also frozen for most diatomic gases. The equipartition theorem does not predict this. It is a classical result, and quantum mechanics breaks it: a mode can only absorb energy in discrete quanta $\hbar\omega$. When $k_BT \ll \hbar\omega$, the mode cannot be excited — it is frozen out. Chapter 9 explains why. For now, the takeaway is that equipartition works beautifully where it works, and its failures point directly toward quantum mechanics.

---

## Real gases: the van der Waals correction

The ideal gas law assumes molecules have zero volume and zero intermolecular forces. Both assumptions fail for real gases. The simplest systematic correction is the van der Waals equation of state:

$$\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT$$

The constant $b$ is the excluded volume per mole — the volume one mole of molecules physically occupies and therefore unavailable to other molecules. Subtracting $nb$ from $V$ gives the effective free volume. For nitrogen: $b = 0.0385$ L/mol.

The constant $a$ corrects for attractive intermolecular forces. When molecules attract each other, those near a wall are pulled slightly backward by their neighbors — reducing the force they exert on the wall. Pressure is therefore slightly less than the ideal prediction. Adding $an^2/V^2$ to the measured pressure recovers the ideal-gas-law quantity. For nitrogen: $a = 1.39$ L²·atm/mol².

At low density (large $V$) and high temperature, $nb \ll V$ and $an^2/V^2 \ll P$, and van der Waals reduces to the ideal gas law. Near a phase transition — where the liquid and gas become indistinguishable at the critical point — the corrections become large and the equation predicts a first-order liquid-vapor transition. The prediction is qualitatively correct and quantitatively approximate; more sophisticated equations of state (Redlich-Kwong, Peng-Robinson) are used in chemical engineering. But van der Waals was the first to show that a simple modification of the ideal gas law could describe both gas and liquid phases in a single equation — a conceptual breakthrough, recognized with the Nobel Prize in 1910.

---

## Dalton's law

One more consequence of the molecular picture: in a mixture of non-reacting ideal gases at the same temperature, the total pressure is the sum of the partial pressures each gas would exert alone.

$$P_{\text{total}} = P_1 + P_2 + \cdots$$

where $P_i = n_i RT/V$. Each species contributes momentum transfer to the walls independently; molecules of different types don't "know about" each other except during collisions, and at low density those collisions are rare. Air is approximately 78% nitrogen and 21% oxygen by mole fraction; at one atmosphere, nitrogen contributes about 0.78 atm and oxygen about 0.21 atm, with minor contributions from argon, CO₂, and water vapor making up the rest.

---

## What comes next

The ideal gas law describes a gas in equilibrium. The Maxwell-Boltzmann distribution describes how energy is partitioned among its molecules. But thermodynamics is ultimately about *processes* — what happens when a gas expands, compresses, absorbs heat, does work. Chapter 5 introduces the first law of thermodynamics: $\Delta U = Q - W$. The tools built here — the relationship between $PV$ and temperature, the internal energy $U = (f/2)NkT$, the heat capacity $C_V$ — become the ingredients for analyzing isothermal, adiabatic, isochoric, and isobaric processes. The ideal gas is the working substance for the first two chapters on thermodynamic cycles.

---

## LLM Exercises

### Build the Maxwell-Boltzmann explorer (`04-maxwell-boltzmann.html`)

> **Show.** Maxwell-Boltzmann speed distribution: $f(v) = 4\pi(m/(2\pi k_BT))^{3/2} v^2 e^{-mv^2/(2k_BT)}$. Three speeds: $v_{mp} = \sqrt{2k_BT/m}$, $v_{avg} = \sqrt{8k_BT/(\pi m)}$, $v_{rms} = \sqrt{3k_BT/m}$.
>
> **Say.** Build a Maxwell-Boltzmann distribution explorer.
>
> **Constrain.** D3 v7. Slider for $T$ (100–2000 K). Dropdown for molecular species: H₂ (M=2), He (4), N₂ (28), O₂ (32), Ar (40), CO₂ (44). Compute and display $f(v)$ as an area chart, with $v_{mp}, v_{avg}, v_{rms}$ marked as vertical lines (color-coded). Numerical readouts of all three speeds. Display the "escape fraction" — fraction of molecules above 11.2 km/s (Earth escape) and above 5.0 km/s (Mars escape). Two-curve overlay mode: compare two temperatures or two species. Filename: `04-maxwell-boltzmann.html`.
>
> **Verify.** (a) At higher $T$, distribution broadens and shifts right. (b) At higher $m$, distribution narrows and shifts left. (c) Always $v_{mp} < v_{avg} < v_{rms}$. (d) Escape fraction for H₂ on Mars at 200 K: about $10^{-3}$.

### Exploration

Compare H₂ at 300 K and N₂ at 300 K. Verify that the lighter molecule has a much faster distribution.

Look at the escape fractions for various atmospheres: H₂ at Mars (200 K) vs N₂ at Earth (288 K). Mars has lost its hydrogen; Earth keeps its nitrogen.

At what temperature does the average speed of nitrogen equal the speed of sound in air (343 m/s)? Around 300 K — instructive.

### Extension prompt (chapter bridge)

> **Show.** I've modeled the gas in equilibrium. Now I want to apply the *first law of thermodynamics* — energy conservation — to processes that change a gas's state.
>
> **Say.** Build a first-law energy-balance visualizer.
>
> **Constrain.** A box with gas at $T_0$, $P_0$, $V_0$. Slider for process type (isothermal, adiabatic, isochoric, isobaric). Slider for final state. Compute $Q$, $W$, $\Delta U$ from the appropriate formulas. Display the energy bar chart showing energy moving in/out.
>
> **Verify.** Isothermal: $\Delta U = 0$ so $Q = W$. Adiabatic: $Q = 0$ so $\Delta U = -W$. Isochoric: $W = 0$ so $Q = \Delta U$. Isobaric: $W = P\Delta V$, $Q = \Delta U + W$.

Save as `04b-first-law-preview.html`. Bridge to Chapter 5.
![A single molecule in a box of side L. Travels right with velocity +v_x, bounces off wall, returns with -v_x. Momentum transfer 2m v_x. Round-trip time 2L/v_x. This builds PV = NkT.](../images/03-ideal-gas-kinetic-theory-fig-01.png)
*Figure 3.1 — Molecular Wall Collision*

![The Maxwell-Boltzmann speed distribution for oxygen at 300 K. Curve rises from zero, peaks at v_mp = 395 m/s, falls with a long tail. Three speeds marked: v_mp = 395, v_avg = 446, v_rms = 484 m/s, always in this order.](../images/03-ideal-gas-kinetic-theory-fig-02.png)
*Figure 3.2 — Maxwell-Boltzmann Distribution*

![Maxwell-Boltzmann distributions on Mars at 200 K for hydrogen H2 and nitrogen N2. Log y-axis shows the tail behavior. Mars escape velocity at 5 km/s. H2 fraction above escape: 10^-3 (visible). N2: 10^-100 (invisible).](../images/03-ideal-gas-kinetic-theory-fig-03.png)
*Figure 3.3 — Atmospheric Escape*

![Three panels. Monatomic atom: 3 translational degrees of freedom, C_V = 3/2 R. Diatomic at moderate T: 3 translation plus 2 rotation = 5, C_V = 5/2 R. Diatomic with vibration: plus 2 vibrational = 7, C_V = 7/2 R.](../images/03-ideal-gas-kinetic-theory-fig-04.png)
*Figure 3.4 — Degrees of Freedom*

![Heat capacity of diatomic gas like H2 versus temperature on log scale. Plateau at 3/2 below ~85 K, rises to 5/2 above the rotational temperature, then to 7/2 above the vibrational temperature ~6000 K. Quantum mechanic...](../images/03-ideal-gas-kinetic-theory-fig-05.png)
*Figure 3.5 — C_V/R vs T*

