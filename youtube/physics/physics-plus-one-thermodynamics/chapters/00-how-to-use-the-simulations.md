# Chapter 0 — How to Use the Simulations

*Get from zero to an ideal-gas-in-a-box simulation before any new physics.*

---

There is a peculiar thing that happens when you first learn thermodynamics. You are handed an equation — $T = (2/3)\langle KE \rangle / k_B$ — and told that this is what temperature *is*. Temperature is the mean translational kinetic energy of molecules. The equation is algebraically clean. You copy it into your notes. You learn to manipulate it. And then you move on, having memorized something without understanding it at all.

Here is what I want to do instead. I want you to *see* it.

Imagine 50 dots in a 2D box. They are bouncing around, colliding with the walls and with each other, moving fast and slow and sideways and up. Color them by speed — slow ones blue, fast ones red. Now drag a slider that adds energy to the system. The dots speed up. The colors shift toward red. A number in the corner — the temperature, computed in real time from $\langle v^2 \rangle$ — climbs from 200 K to 800 K.

*That* is temperature. Not the equation. The equation describes what you just saw.

This book is built on that idea. Each chapter introduces a thermodynamics concept and then asks you to build a simulation that makes the concept visible. You will not understand the equations better because you memorized them. You will understand them because you had to construct the thing they describe, watch it behave, and check whether it matched what the theory predicted.

But before we can do any of that, I need to teach you how to use the tool. Chapter 0 is the setup chapter. By the end of it, you will have a working ideal-gas simulator. Everything that follows builds on that.

---

## The three files

The tool is Claude, a large language model, used with a specific structure. The structure has three files.

<!-- → [TABLE: three-column reference table — File | Role | When you touch it — rows: CLAUDE.md / coding constitution, defines library, constants, numerical methods / when conventions change; DESIGN.md / visual constitution, defines colors, canvas sizes, arrow types / when visual language changes; PROJECT.md / project ledger, tracks current chapter and completed simulations / after every chapter] -->

**`CLAUDE.md`** is the coding constitution. It tells Claude which library to use (D3 v7), what file conventions to follow (single HTML file, inline CSS and JavaScript, no external dependencies), and which physical constants to treat as fixed: $k_B = 1.38 \times 10^{-23}$ J/K, $R = 8.314$ J/(mol·K), $N_A = 6.022 \times 10^{23}$/mol, $h = 6.626 \times 10^{-34}$ J·s, $\sigma_{SB} = 5.67 \times 10^{-8}$ W/(m²·K⁴). It also specifies the numerical methods: particle dynamics via `requestAnimationFrame`, elastic collisions by the velocity-swap rule, real-time computation of temperature and pressure.

**`DESIGN.md`** is the visual constitution. Colors carry meaning and they have to stay consistent across all ten chapters, or the simulations become incoherent as a series. Particle speed is colored on a gradient from cool blue to warm red. Heat flow $Q$ is shown with orange arrows. Work $W$ uses green arrows. PV curves are purple, with isothermal processes dashed and adiabatic processes solid. Entropy is displayed in gold. Thermal reservoirs are gray gradient blocks. The canvas dimensions are fixed: 700 × 500 pixels for particle simulations, 700 × 400 for PV diagrams and distribution plots.

**`PROJECT.md`** is the scratch ledger. You update it after each chapter — which simulations you've built, which chapters are done, what state the project is in. This matters because you will return to these files many times, and Claude has no memory between conversations.

Why three files and not one? Because they answer three different questions. `CLAUDE.md` answers *how should the code be written*. `DESIGN.md` answers *what should it look like*. `PROJECT.md` answers *where are we*. Keeping them separate means you can update the design conventions without touching the coding conventions, and vice versa.

One important thing about these files: they are not documentation. Documentation is something you write after the fact so other people understand what you did. These files are active prompts — you load them at the start of every conversation, before you type anything else. Think of them as context you are giving Claude so it knows the constraints of the problem before it starts solving it.

---

## The four-move prompt

The way to get a working simulation out of Claude is not to describe what you want in a paragraph of natural language. That produces vague output. The way to do it is to use a four-move structure.

**Show.** Describe the physical setup. What are the objects? What are the rules they follow? What quantities do you want to track?

**Say.** State the deliverable. One sentence: *build this thing*.

**Constrain.** List the specific requirements. Library, file conventions, physics formulas, visual conventions, filename. These should be precise enough that there is no ambiguity about what "correct" looks like.

**Verify.** Describe the tests. What should the simulation do when it is working? This is the most important move, and the one people skip. If you do not specify how to verify that the simulation is correct, you cannot tell the difference between a simulation that works and one that looks like it works.

The verification step is especially important in thermodynamics simulations because the physics is statistical. A single snapshot cannot tell you whether your temperature formula is right. You need to test behavior at limits: temperature should rise when energy is added; pressure should fall when the box expands at constant temperature; the speed distribution should broaden as energy increases. These are the tests that catch bugs that *look* like correct physics to a casual observer.

<!-- → [INFOGRAPHIC: four-panel diagram of the Show / Say / Constrain / Verify structure — each panel names the move, shows the question it answers, and gives a one-line example from the ideal-gas prompt; reader should see the logical dependency: each move narrows the space of possible outputs] -->

---

## The ideal gas in a box

Now let me tell you about the simulation you are going to build.

An ideal gas is a model: $N$ point particles that exert no forces on each other except during instantaneous elastic collisions, bouncing around in a box. It is the simplest possible thermodynamics simulation, and it is the right place to start because all the central concepts — temperature, pressure, the Maxwell-Boltzmann distribution — emerge from it directly.

Start with temperature. In a 2D box, the temperature of an ideal gas is:

$$T = \frac{m \langle v^2 \rangle}{2 k_B}$$

This is not a definition from thin air. It comes from the equipartition theorem: each degree of freedom of a particle in thermal equilibrium carries $\frac{1}{2}k_B T$ of average energy. In 2D, each particle has two translational degrees of freedom ($x$ and $y$), so the total average kinetic energy per particle is $k_B T$. Setting that equal to $\frac{1}{2}m\langle v^2 \rangle$ and solving for $T$ gives you the formula above. In 3D you divide by $3 k_B$ instead of $2 k_B$ — three degrees of freedom instead of two.

The simulation measures temperature by computing $\langle v^2 \rangle$ across all particles at each time step and applying this formula. It does this in real time. You can watch the number change.

<!-- → [IMAGE: screenshot or mockup of the ideal-gas simulator at two energy levels side by side — left panel: particles mostly blue, T readout ~300 K; right panel: particles mostly red, T readout ~800 K; caption should direct the reader's eye to the color shift and the live T readout] -->

Now pressure. Pressure is force per unit area, and force is rate of change of momentum. Every time a particle bounces off a wall, it transfers momentum to that wall. If the particle had velocity $v_x$ toward the wall, it leaves with velocity $-v_x$ — a momentum change of $2mv_x$. Add up all such transfers across all particles per unit time and divide by the wall's area (or length, in 2D), and you have the pressure.

$$P = \frac{1}{A} \cdot \frac{\sum |\Delta p_{\text{wall}}|}{\Delta t}$$

The simulation computes this as a running average over several seconds — not instantaneously, because with 50 particles the instantaneous value fluctuates too much to be readable.

Let me show you that these formulas are consistent with the ideal gas law. Take 50 nitrogen molecules, $m = 28 \times 1.66 \times 10^{-27}$ kg $= 4.65 \times 10^{-26}$ kg, in a 100 nm × 100 nm box, with initial average speed 400 m/s.

Temperature:
$$T = \frac{(4.65 \times 10^{-26})(400)^2}{2(1.38 \times 10^{-23})} \approx 269 \text{ K}$$

Roughly room temperature.

Pressure, rough estimate: each particle hits each wall about $v/(2L) = 400 / (2 \times 10^{-7}) = 2 \times 10^9$ times per second. Momentum transferred per collision: $\sim 2mv \approx 3.7 \times 10^{-23}$ kg·m/s. Force per particle per wall: $\sim 7.4 \times 10^{-14}$ N. With 50 particles and wall length $L = 10^{-7}$ m: $P \sim 50 \times 7.4 \times 10^{-14} / 10^{-7} = 3.7 \times 10^{-5}$ Pa.

Now check against the ideal gas law, $P = NkT/V$, where in 2D the "volume" is area $= (10^{-7})^2 = 10^{-14}$ m²:

$$P = \frac{50 \times (1.38 \times 10^{-23}) \times 269}{10^{-14}} = 1.86 \times 10^{-5} \text{ Pa}$$

Within a factor of two of the rough estimate — consistent, given the approximations. The simulation should match the ideal gas law in its own running averages. That is one of the verification tests.

---

## Elastic collisions

To make a simulation that conserves energy, the collisions have to be elastic. Here is the rule.

When two particles collide — when their center-to-center distance drops to $2r$, where $r$ is the particle radius — you decompose each velocity into a component along the line connecting their centers (the *normal* direction, $\hat{n}$) and a component perpendicular to it (the *tangential* direction). For equal-mass particles, elastic collision simply swaps the normal components. The tangential components are unchanged.

Why does this conserve energy? Because the swap exchanges identical quantities — the total kinetic energy in the normal direction is the same before and after. And because nothing happens to the tangential components, total kinetic energy is conserved.

Wall collisions are simpler: reverse the velocity component perpendicular to the wall.

The reason to understand this before asking Claude to implement it is that it is easy to write a collision routine that looks correct but is not quite elastic — that leaks small amounts of energy or creates small amounts out of nothing. Over long runs, these errors accumulate. When you verify your simulation, one of the things you are checking is that the total kinetic energy stays constant when no energy is added or removed from the system.

<!-- → [INFOGRAPHIC: two-particle collision diagram showing the velocity decomposition — draw the two circles at contact, the normal vector n̂ between centers, and arrows for the normal and tangential components of each velocity before and after; reader should see that only the normal components swap, tangential components unchanged] -->

---

## What 50 particles can and cannot show you

Here is an honest accounting of what this simulation is and is not.

Fifty particles is an absurdly small number. Real nitrogen gas at room temperature in a one-liter bottle contains about $2.4 \times 10^{22}$ molecules. The ideal gas law — $PV = NkT$ — is a statement about what happens in the limit of large $N$. At large $N$, statistical fluctuations in pressure and temperature are of order $1/\sqrt{N}$, which is about $10^{-11}$ for a macroscopic gas. Completely undetectable.

With 50 particles, the fluctuations are $1/\sqrt{50} \approx 14\%$. You will see the pressure readout bobbing around by 14% from its mean even when nothing is changing. Temperature will flicker. This is not a bug. This *is* statistical mechanics.

That is actually why 50 particles is pedagogically useful. With $10^{22}$ particles, thermodynamics looks deterministic. Temperature is a number; pressure is a number; they are stable and well-defined. The underlying molecular chaos is invisible. With 50 particles, the fluctuations are on screen, in front of you, reminding you that these macroscopic quantities are *averages* — averages over a stochastic process that never stops varying.

What 50 particles can show you:

- Temperature rises when energy is added. The formula $T = m\langle v^2\rangle / (2k_B)$ visibly tracks the particle speeds.
- Pressure doubles when the box is halved at constant temperature. The ideal gas law, verified.
- An initial configuration with all particles moving at the same speed and direction randomizes into a broad speed distribution as collisions redistribute energy. This is the Maxwell-Boltzmann distribution emerging spontaneously — which is the subject of Chapter 3.
- Fluctuations are real, visible, and shrink as $1/\sqrt{N}$.

What 50 particles cannot show you: the thermodynamic limit. The smooth, fluctuation-free behavior that makes the ideal gas law feel like a law of nature rather than a statistical average. For that you need Chapter 3, and a particle count in the hundreds.

<!-- → [CHART: two side-by-side time-series plots of pressure vs. time — left: N=50, showing ~14% fluctuation band around the mean; right: N=500, showing ~4.5% fluctuation band; x-axis is time in seconds, y-axis is P in Pa; caption: "Fluctuations shrink as 1/√N — the same gas law, with very different noise"] -->

There is also a computational constraint I should mention: this book uses 2D simulations throughout, not 3D. The physics of a 3D ideal gas is not different in character — everything I have described above still applies — but 3D particle simulations are harder to render visually, and the pedagogical payoff does not justify the added complexity. The main consequence is a factor: in 2D you divide by $2k_B$; in 3D by $3k_B$. When you work through Chapter 1 and see the formula on screen, that factor of 2 is there because your particles live in a plane.

---

## What comes next

By building the ideal-gas simulator you are doing several things at once. You are learning the four-move prompt structure, which you will use in every chapter that follows. You are building `CLAUDE.md` and `DESIGN.md`, which will anchor every simulation for the rest of the book. And you are building the specific simulation — the ideal gas in a box — that is the foundation for kinetic theory, the Maxwell-Boltzmann distribution, and eventually the transition from microscopic to macroscopic in statistical mechanics.

Chapter 1 starts with that simulator already running. It adds a histogram of particle speeds below the box and overlays the theoretical Maxwell-Boltzmann curve in real time. You will watch the curve emerge from the noise of 50 particles, learn what root-mean-square speed, mean speed, and most-probable speed are and why they are different, and understand why temperature is proportional to $\langle v^2 \rangle$ and not to $\langle v \rangle$.

The rest of the book follows from there.

---

## Exercises

**Warm-up 1** *(Apply — the three files)*
Name the three Brutalist files. For each one, state in a single sentence what question it answers and when you would change it.

**Warm-up 2** *(Apply — the four moves)*
Write a four-move prompt for a simulation you make up — any physical system, not necessarily thermodynamics. You do not need to build it. The exercise is to practice the structure: Show, Say, Constrain, Verify. The Verify move must include at least two testable limit behaviors.

**Warm-up 3** *(Apply — temperature formula)*
A 2D ideal gas has 80 particles of mass $m = 4.65 \times 10^{-26}$ kg. The mean squared speed is $\langle v^2 \rangle = 2.4 \times 10^5$ m²/s². What is the temperature? What formula are you using, and which physical principle does it come from?

**Application 1** *(Apply — ideal gas law)*
Your simulator runs with $N = 50$ particles at $T = 300$ K in a box of width $L = 100$ nm. You then double the box width to $L = 200$ nm without adding or removing energy. Predict: does the temperature change? Does the pressure change? By what factor? Check your prediction against $PV = NkT$.

**Application 2** *(Apply — verification)*
A student builds a particle simulator and runs it for 60 seconds without changing any parameter. The reported temperature drifts upward by 8% over that time. The student says the simulation is correct. Are they right? What is the most likely cause of the drift, and which move of the four-move structure was supposed to catch it?

**Application 3** *(Apply — fluctuations)*
The simulator reports pressure values of 1.82, 2.14, 1.93, 1.71, 2.08 $\times 10^{-5}$ Pa in five consecutive one-second windows. The mean is $1.936 \times 10^{-5}$ Pa. Estimate the fractional fluctuation. Is this consistent with $N = 50$ particles? What $N$ would reduce the fluctuation to under 5%?

**Synthesis 1** *(Analyze — connecting formula to simulation)*
The chapter uses a 2D temperature formula ($T = m\langle v^2\rangle / 2k_B$) and a 3D formula would use $T = m\langle v^2\rangle / 3k_B$. Suppose your simulator is coded with the 3D formula but runs in 2D. Describe the symptom: when you add energy and the particles speed up, what does the reported temperature do relative to what it should? By what factor is it off? How would the Verify step in the four-move prompt catch this?

**Synthesis 2** *(Analyze — design of the three-file system)*
A student proposes merging `CLAUDE.md` and `DESIGN.md` into a single file called `RULES.md`. Give one concrete scenario in a later chapter where this merge would cause a practical problem — where changing one kind of rule without touching the other would be harder with a merged file.

**Challenge** *(Extend — 3D adaptation)*
The book uses 2D simulations throughout. Suppose you wanted to build a 3D version of the ideal-gas simulator for a chapter that requires accurate comparison with tabulated 3D data. Write out the changes you would need to make to: (a) the temperature formula, (b) the collision detection rule, (c) `CLAUDE.md`, and (d) the Verify step. You do not need to implement it — describe the changes precisely enough that someone else could.

---

## LLM Exercises

### Part 1 — Generate `CLAUDE.md`

> **Show.** I am building D3.js v7 thermodynamics simulations: a single HTML file each, with particle physics via `requestAnimationFrame`, elastic collision detection, and real-time computation of T, P, S.
>
> **Say.** Generate a `CLAUDE.md` coding constitution.
>
> **Constrain.** Sections: (1) Library/file conventions (D3 v7, single HTML, inline CSS+JS); (2) Physics constants ($k_B$, $R$, $N_A$, $h$, $\sigma_{SB}$); (3) Particle dynamics methods (elastic collision detection, wall reflection, small-step Euler integration); (4) Macroscopic-quantity computations (T from $\langle KE\rangle$, P from wall impulse rate, S from microstate count or process integration); (5) PV diagram conventions (P on y, V on x, area = work); (6) Animation idioms; (7) Verification checklist.
>
> **Verify.** ~60 lines. With this file loaded, Claude should produce a working ideal-gas simulator.

Save to `CLAUDE.md`.

---

### Part 2 — Generate `DESIGN.md`

> **Show.** Thermo simulations have specific visual conventions across chapters.
>
> **Say.** Generate `DESIGN.md`.
>
> **Constrain.** Particle color by speed (cool blue to warm red, gradient at $v/v_{rms}$). Heat Q: orange arrows. Work W: green arrows. PV curves purple (isotherm dashed, adiabat solid). Entropy ΔS: gold display. Reservoirs: gray gradient blocks. Canvas: 700×500 particles, 700×400 PV/distributions. Dark mode via `prefers-color-scheme`.
>
> **Verify.** All colors distinct; dimensions explicit; particle color formula stated.

Save to `DESIGN.md`.

---

### Part 3 — Generate `PROJECT.md`

Three lines: project name, current chapter, simulations completed (empty so far).

---

### Part 4 — Build the ideal-gas simulator (`00-ideal-gas-box.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** Ideal gas: $N$ point particles with mass $m$ bouncing elastically. Temperature $T = m\langle v^2\rangle / (2 k_B)$ in 2D. Pressure $P = \sum |\Delta p_{\text{wall}}|/(A \Delta t)$.
>
> **Say.** Build an ideal-gas-in-a-box simulator.
>
> **Constrain.** D3 v7. 2D box (700×500 canvas). $N=50$ particles, $m = 4.65 \times 10^{-26}$ kg (N₂). Initial Maxwell-Boltzmann distribution at $T_0 = 300$ K. Slider for "energy" (rescales all velocities by same factor). Slider for box width. Render: particles as circles colored by speed (DESIGN.md gradient). Live readouts: T (computed from $\langle v^2\rangle$), P (running 5-second average of wall impulse rate), $v_{rms}$, $v_{avg}$. Filename: `00-ideal-gas-box.html`.
>
> **Verify.** (a) At rest: T ≈ 0; particles stationary; P ≈ 0. (b) Add energy → T rises; particles speed up; colors shift red. (c) Shrink box → P rises (ideal gas law $PV = NkT$). (d) Wait 10s with no parameter change: T and P fluctuate by ~14% (consistent with $1/\sqrt{N}$).

Save to `00-ideal-gas-box.html`. Open in browser.

---

### Part 5 — Exploration

Slowly raise the energy slider. Watch T climb. Verify the rate: doubling kinetic energy doubles temperature.

Halve the box width while keeping energy constant. Pressure should double. Verify.

Start with all particles at exactly $v = 400$ m/s in the same direction. Watch how collisions randomize the directions and broaden the speed distribution over time. This is the Maxwell-Boltzmann distribution emerging from collisions.

---

### Part 6 — Extension prompt (chapter bridge)

> **Show.** I have a working ideal gas simulator. Now I want to look at the *molecular speed distribution* explicitly — a histogram of speeds with the Maxwell-Boltzmann curve overlaid.
>
> **Say.** Modify the simulator to add a real-time speed histogram below the box.
>
> **Constrain.** Bin particle speeds into 20 bins from 0 to 1500 m/s. Update histogram every animation frame. Overlay the theoretical Maxwell-Boltzmann curve at the current T.
>
> **Verify.** With $T = 300$ K, peak of the distribution is at $v_{mp} = \sqrt{2k_BT/m} \approx 423$ m/s for N₂. Heat to 800 K: peak shifts right to approximately 690 m/s.

Save as `00b-speed-distribution-preview.html`. This is the bridge into Chapter 1.
