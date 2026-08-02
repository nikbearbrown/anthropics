# Chapter 7 — Entropy

*Clausius defined it as $dS = \delta Q/T$. Boltzmann defined it as $S = k_B \ln \Omega$. They are the same quantity.*

---

## The cream never comes back

Pour cream into hot coffee. Stir once. The cream mixes throughout. Now wait — an hour, a day, a year. The cream never unmixes. It never spontaneously separates itself back into a layer at the top.

This seems obvious. But here is the thing: nothing in Newton's laws forbids it.

Newton's laws are time-symmetric. If you filmed the mixing at the molecular level and played the film backwards, every single particle would follow a perfectly valid Newtonian trajectory. The reverse motion is physically allowed. No conservation law is violated. No force is pointing the wrong way. The unmixing would be, from a mechanical standpoint, completely legitimate.

And yet it never happens.

The reason is not mechanical. It is statistical. There are vastly more arrangements of cream molecules and coffee molecules that look "mixed" than arrangements that look "cream on top." For a real cup of coffee — somewhere around $10^{23}$ molecules — the ratio of mixed microstates to separated microstates is a number so large it doesn't fit comfortably in any notation we have. Something like $10^{10^{20}}$, give or take. When the system evolves randomly, it wanders through microstates. Essentially all of them look mixed. The probability of spontaneously landing in one of the vanishingly few unmixed microstates is not zero — it is just so small that the universe is not old enough, by many orders of magnitude, to make it worth expecting.

This is entropy. Not a law that says "thou shalt not unmix." A statistical observation that says "of all the accessible microstates, the overwhelming majority look mixed, so that's what you see." The second law of thermodynamics is the statement that systems evolve toward states with more microstates. Entropy is the logarithm of the count of those microstates. And the reason the cream doesn't come back is the same reason that if you shuffle a deck of cards, you never get them in order: not because order is forbidden, but because there are so few ordered arrangements compared to disordered ones that you'd have to wait longer than the age of the universe.

<!-- → [INFOGRAPHIC: Two-panel illustration — left panel: coffee cup with cream layered on top (few microstates, labeled Ω_separated ≈ 1); right panel: same cup with cream fully mixed (astronomically many microstates, labeled Ω_mixed ≈ 10^(10^20)). Arrow from left to right labeled "spontaneous"; crossed arrow from right to left labeled "never observed." Caption: "The second law is a counting argument. There are vastly more mixed microstates than separated ones. The system wanders randomly; it almost always looks mixed."] -->

---

## Two definitions, one quantity

Entropy was defined twice, by two different people, using two completely different approaches. That they give the same answer is one of the deepest results in physics.

Rudolf Clausius, working in the 1850s and 1860s, approached entropy from the macroscopic side — from the thermodynamics of heat engines. He noticed that for any reversible process, the ratio $\delta Q / T$ behaves like the change in a state function. He defined entropy by it:

$$dS = \frac{\delta Q_\text{rev}}{T}.$$

The subscript matters: this is the heat exchanged in a *reversible* process, divided by the temperature at which it's exchanged. Entropy is measured in joules per kelvin.

Ludwig Boltzmann, working in the 1870s and 1880s, approached entropy from the microscopic side — from the statistical mechanics of atoms. He asked: given that a gas is in a particular macroscopic state (a particular temperature, pressure, volume), how many microscopic arrangements of atoms are consistent with that state? He called that number $\Omega$, and defined:

$$S = k_B \ln \Omega.$$

$k_B$ is Boltzmann's constant, $1.38 \times 10^{-23}$ J/K — the conversion factor between the microscopic world of individual molecules and the macroscopic world of joules and kelvins. Boltzmann was so proud of this equation that he asked to have it carved on his tombstone in Vienna. It is there today. The inscription reads $S = k \ln W$.

These two definitions agree. For any process you can name, $\int \delta Q_\text{rev}/T$ and $k_B \Delta \ln \Omega$ give the same number. That agreement is the bridge between classical thermodynamics and statistical mechanics — and the proof that heat, at bottom, is just the disordered kinetic energy of atoms.

---

## What the Clausius definition is actually saying

The Clausius definition is subtle in a way that trips almost everyone on first encounter.

The subtlety is this: $\Delta S$ is a state function. It depends only on the initial and final states of the system, not on the path taken between them. But the integral $\int \delta Q/T$ is only well-defined along a *reversible* path. So if you want to compute the entropy change for an irreversible process — a free expansion, a mixing event, a fast compression — you cannot just integrate $\delta Q/T$ along the actual path. You have to find a reversible path connecting the same two endpoints and integrate along that instead.

This is not a cheat. It is a feature. Because entropy is a state function, you are allowed to compute $\Delta S$ by any path you like, as long as it goes between the same initial and final states. The actual process might be irreversible and messy. The entropy change is still a well-defined number, and you find it by computing the reversible alternative.

The integral for common processes comes out cleanly.

For an **isothermal** process at temperature $T$, all the heat is exchanged at one temperature, so $\Delta S = Q/T$.

For **isochoric heating** from $T_i$ to $T_f$ (constant volume, ideal gas), $\delta Q = nC_V \, dT$, so:

$$\Delta S = \int_{T_i}^{T_f} \frac{nC_V \, dT}{T} = nC_V \ln \frac{T_f}{T_i}.$$

For **isobaric heating**, the same calculation with $C_P$ in place of $C_V$.

For a **reversible adiabatic** process, $\delta Q = 0$ at every point, so $\Delta S = 0$. Reversible adiabatic processes are also called *isentropic* — constant entropy — and the adiabatic curves on a PV diagram are also called isentropes.

Now here is the case that makes everything click into place.

<!-- → [TABLE: Entropy changes for standard ideal-gas processes — columns: process, constraint, ΔS formula, sign of ΔS, physical meaning. Rows: isothermal (Q/T, positive for expansion), isochoric (nCv ln Tf/Ti, positive for heating), isobaric (nCp ln Tf/Ti, positive for heating), reversible adiabatic (0, isentropic), free expansion (nR ln Vf/Vi, always positive). Caption: "For every process except reversible adiabatic, entropy increases or can increase. The isentrope is the only process that leaves the universe's entropy unchanged."] -->

---

## Free expansion: the irreversible case

Take one mole of ideal gas in a container of volume $V$. Open a partition to let it expand into an adjacent evacuated chamber of the same volume. The gas doubles its volume. There is no piston, so no work is done: $W = 0$. There is no heat exchange with the surroundings: $Q = 0$. For an ideal gas, internal energy depends only on temperature, so $\Delta U = 0$ and $T$ does not change.

So: $Q = 0$, $W = 0$, $\Delta T = 0$. Does entropy change?

It does. The gas has gone from occupying volume $V$ to occupying $2V$. Each molecule now has access to twice as much space. The number of accessible microstates has increased — dramatically. Entropy has increased. But the Clausius formula $\Delta S = \int \delta Q/T$ seems to give zero, because $\delta Q = 0$ throughout.

The resolution is that you must not compute $\int \delta Q/T$ along the actual (irreversible) path. You must find a reversible path connecting the same endpoints: a gas at temperature $T$ in volume $V$, ending at a gas at temperature $T$ in volume $2V$. That reversible path is an isothermal expansion. For an isothermal expansion:

$$Q_\text{rev} = nRT \ln \frac{2V}{V} = nRT \ln 2.$$

So:

$$\Delta S = \frac{Q_\text{rev}}{T} = nR \ln 2 = R \ln 2 \approx 5.76 \text{ J/K}.$$

Now check this with Boltzmann. The free expansion doubles the volume available to each of the $N_A$ molecules. For each molecule, the number of accessible microstates doubles (twice as many positions available). For $N_A$ molecules, $\Omega$ multiplies by $2^{N_A}$. So:

$$\Delta S = k_B \ln \frac{\Omega_f}{\Omega_i} = k_B \ln 2^{N_A} = N_A k_B \ln 2 = R \ln 2 \approx 5.76 \text{ J/K}.$$

Same answer. The Clausius and Boltzmann definitions agree, even for an irreversible process, even when the actual $\delta Q$ along the process is zero.

This is the deepest demonstration that entropy is a state function. The number of microstates of the final state versus the initial state is what changed. The path between them is irrelevant to the answer.

<!-- → [FIGURE: Two-panel diagram of free expansion — left panel: gas molecules crowded into volume V, partition closed, vacuum on right side; right panel: same molecules spread over 2V after partition opens. Labels: W=0, Q=0, ΔU=0, but ΔS = R ln 2 > 0. Arrow showing the reversible isothermal path used to compute ΔS even though the actual process followed a different path. Caption: "Free expansion: nothing flows, temperature is unchanged, yet entropy increases. The calculation requires a reversible detour to the same endpoints."] -->

---

## The second law in entropy language

The first law says energy is conserved. The second law says entropy of the universe never decreases.

For any process — reversible or not:

$$\Delta S_\text{universe} = \Delta S_\text{system} + \Delta S_\text{surroundings} \geq 0.$$

Equality holds for reversible processes. The strict inequality holds for irreversible ones. There are no exceptions.

This is worth unpacking with a concrete case. Heat $Q$ flows from a hot reservoir at temperature $T_H$ to a cold reservoir at temperature $T_C$, with $T_H > T_C$. The hot reservoir loses entropy: $\Delta S_H = -Q/T_H$. The cold reservoir gains entropy: $\Delta S_C = +Q/T_C$. The net change in the entropy of the universe:

$$\Delta S_\text{universe} = Q\left(\frac{1}{T_C} - \frac{1}{T_H}\right).$$

Since $T_H > T_C$, the quantity in parentheses is positive, and $\Delta S_\text{universe} > 0$. The process is spontaneous and irreversible.

Now ask: what if heat tried to flow the other way, from cold to hot? Then $Q$ would be negative in the formula above (heat flowing out of the cold reservoir), and $\Delta S_\text{universe}$ would be negative. The second law says $\Delta S_\text{universe} \geq 0$, so this cannot happen spontaneously. The second law, in entropy form, is the statement that heat flows from hot to cold and not the reverse.

What this does not say is that local entropy can never decrease. A refrigerator decreases the entropy of its contents. A living cell builds ordered structures from disordered precursors. Ice crystals grow from liquid water. In every case, the local entropy decrease is paid for by a larger entropy increase somewhere else — the heat exhausted by the refrigerator, the metabolic heat released by the cell, the entropy increase in the cooling water. The universe's total entropy always wins.

---

## The microstate picture in detail

The Boltzmann formula becomes concrete when you work a small example.

Imagine $N$ gas molecules distributed between two halves of a box. Each molecule is in the left half or the right half — two possible states per molecule. The total number of microstates is $\Omega_\text{total} = 2^N$. The macrostate with exactly $n$ molecules in the left half contains:

$$\Omega(n) = \binom{N}{n} = \frac{N!}{n!(N-n)!}$$

microstates.

For $N = 100$, the most likely macrostate is $n = 50$ (half in each side). Its count is $\Omega(50) = \binom{100}{50} \approx 10^{29}$. The macrostate with all 100 molecules on the left has $\Omega(100) = 1$. The ratio is $10^{29}$. You would have to make $10^{29}$ random observations of the system to expect to see all molecules on one side even once.

For one mole of gas, $N = N_A \approx 6 \times 10^{23}$. The ratio $\Omega(N_A/2) / \Omega(N_A)$ is of order $e^{N_A \ln 2}$ — a number whose exponent itself has twenty-three digits. The probability of observing all the gas on one side of a box, spontaneously, is not merely small. It is so far below any probability we have language for that "impossible" is a reasonable practical description, even though "forbidden" is technically incorrect.

The second law is not a prohibition. It is a statistical statement, and its statistical nature is visible at small $N$. With four molecules, you will regularly see all four on one side — it happens with probability $1/2^4 = 1/16$. With twenty molecules, you would expect to wait about a million observations. With a hundred, you are waiting longer than the age of the universe. With $10^{23}$, the waiting time exceeds any reasonable cosmological scale.

This is why entropy fluctuations matter in nanotechnology and biophysics — at scales where $N$ is a few hundred or a few thousand, the second law is not a reliable guide. At macroscopic scales, it is as reliable as any law in physics.

<!-- → [CHART: Bell-curve histogram of Ω(n) vs. n for N = 100 — x-axis from 0 to 100 (number of molecules on left), y-axis log scale showing Ω. Peak at n = 50 labeled Ω ≈ 10^29; tails at n = 0 and n = 100 labeled Ω = 1. Caption: "The probability distribution of macrostates for 100 molecules. The overwhelming weight is near n = 50. The 'all on one side' macrostate at the tails has Ω = 1 — a single microstate against 10^29."] -->

---

## The third law

As temperature approaches absolute zero, entropy approaches zero.

$$\lim_{T \to 0} S = 0.$$

The reason is quantum mechanical: at absolute zero, a system settles into its ground state. If the ground state is unique — if there is only one lowest-energy configuration — then $\Omega = 1$ and $S = k_B \ln 1 = 0$. The ground state has exactly one microstate, so the entropy is exactly zero.

This is the third law of thermodynamics, established empirically by Nernst around 1906 and understood microscopically once quantum mechanics arrived. Its practical consequence: absolute entropy is well-defined. You can compute $S(T)$ by integrating $\delta Q_\text{rev}/T'$ from zero up to $T$, starting from the known baseline $S(0) = 0$.

The third law also implies that absolute zero is unreachable in finite steps. To cool a system toward $T = 0$, you remove entropy from it. But the further you cool, the less entropy remains to remove, and each step reduces the temperature by a smaller fraction. You can approach zero kelvin arbitrarily closely; you cannot reach it. Nernst's theorem is not just a technical limitation — it reflects the mathematical structure of entropy near the ground state.

---

## Entropy and the arrow of time

The second law is the only fundamental law in classical physics that distinguishes the past from the future.

Newton's laws, Maxwell's equations, even quantum mechanics — all are time-symmetric. If you filmed a billiard-ball collision and played it backwards, both versions would look physically valid. If you filmed the operation of a perfect hydrogen atom and played it backwards, you could not tell which direction was forward.

But film a glass of water shattering on a floor, and no one has any difficulty identifying which version is forward in time. Not because the reverse violates Newton's laws — it doesn't — but because the reverse requires a spontaneous decrease in entropy, and that essentially never happens.

The asymmetry of time — the fact that the past is different from the future, that there is a direction to causation, that you can remember yesterday but not tomorrow — is encoded in the second law. And the second law, as we've seen, is not a fundamental prohibition. It's a statistical fact about initial conditions. The universe started in a state of extremely low entropy. We do not fully understand why. That initial condition, combined with the statistical mechanics of microstate counting, produces the arrow of time we experience.

This is one of the genuinely deep open problems in physics. Penrose has argued that the low initial entropy of the universe requires an explanation as fundamental as any dynamical law. The question sits at the intersection of thermodynamics, cosmology, and the interpretation of quantum mechanics. Nobody has settled it.

---

## A note on "disorder"

Every popular account of entropy describes it as "disorder." This is a useful first approximation and a misleading final answer.

A liquid crystal is a state of matter that looks, to casual inspection, quite ordered — its molecules align along preferred directions. Yet certain liquid crystal phases have *higher* entropy than their disordered liquid counterparts, because the orientational alignment frees up more translational degrees of freedom than it constrains. The system is "more ordered" in one sense and has "more entropy" in another.

Entropy is $k_B \ln \Omega$ — the logarithm of the number of accessible microstates. What increases is the count of microstates, not a subjective quality called disorder. "Disorder" is a metaphor that captures something real but fails at the edges. The precise version is: entropy increases because there are more ways to be in a high-entropy state than in a low-entropy state, and a randomly-evolving system will almost always be found in a high-count macrostate.

---

## Still puzzling

*Why did the universe start in a low-entropy state?* The second law says entropy increases. So in the past, entropy was lower. Keep going back: the early universe had extraordinarily low entropy for its energy content. The hot, dense early universe, naively, should have had many accessible microstates. Roger Penrose has estimated that the entropy of the early universe was about $10^{10^{123}}$ times smaller than the maximum possible entropy for its mass-energy. Why? We don't know. The low initial entropy is one of the most profound unexplained facts in physics.

*What is entropy for systems far from equilibrium?* The Clausius and Boltzmann definitions work cleanly for systems in or near thermodynamic equilibrium. For systems far from equilibrium — a turbulent fluid, a living cell, the global economy — entropy is harder to define. Non-equilibrium thermodynamics is an active research area. Concepts like entropy production rate (how fast irreversibility is generated) are well-defined in some regimes but not universally.

*Can entropy decrease in a quantum system?* Quantum mechanics allows phenomena like Loschmidt echoes, where a quantum system's evolution is time-reversed and the system returns to its initial state. In principle, this appears to violate the second law. In practice, the time-reversal operation becomes exponentially more precise as the system gets larger, making macroscopic reversals as unlikely as classical fluctuations. The relationship between quantum mechanics and the second law is subtle and not fully resolved.

---

## Exercises

### Warm-up

**W1.** One mole of ideal gas expands isothermally and reversibly at $T = 400$ K, doubling its volume. Find $\Delta S$ for the gas, for the surroundings, and for the universe. State whether the process is reversible or irreversible and explain how the $\Delta S_\text{universe}$ result confirms your answer.

*Tests: isothermal entropy formula and the $\Delta S_\text{universe} = 0$ signature of a reversible process. Difficulty: low.*

**W2.** 200 J of heat flows irreversibly from a reservoir at 800 K to a reservoir at 400 K. Compute $\Delta S_H$, $\Delta S_C$, and $\Delta S_\text{universe}$. Now suppose the same 200 J flowed from the 400 K reservoir to the 800 K reservoir. What does the second law say about this direction?

*Tests: $\Delta S = Q/T$ for a reservoir, $\Delta S_\text{universe} \geq 0$ as a direction test. Difficulty: low.*

**W3.** Two moles of diatomic ideal gas ($C_V = \tfrac{5}{2}R$) are heated at constant volume from $T_1 = 300$ K to $T_2 = 600$ K. Find $\Delta S$ for the gas.

*Tests: isochoric entropy formula with integration producing a logarithm. Difficulty: low.*

**W4.** One mole of monatomic ideal gas undergoes free expansion, tripling its volume. The temperature is unchanged. Find $\Delta S$ using the Clausius approach (reversible isothermal path). Then verify the answer using the Boltzmann approach: each molecule now has access to three times the volume, so $\Omega_f = 3^{N_A} \Omega_i$.

*Tests: free expansion as the central example of computing ΔS for an irreversible process via a reversible detour; verifying agreement between the two definitions. Difficulty: medium.*

---

### Application

**A1.** 0.50 kg of water at 0°C is mixed with 0.50 kg of water at 100°C in an insulated container. Find the equilibrium temperature and the total entropy change of the combined system. Use $c_w = 4186$ J/(kg·K) and the approximation $\Delta S \approx mc\ln(T_f/T_i)$ for each portion. Is $\Delta S_\text{universe}$ positive? Should it be?

*Tests: calorimetry combined with entropy calculation; confirms the second law for an irreversible mixing process. Difficulty: medium.*

**A2.** A Carnot engine operates between $T_H = 600$ K and $T_C = 300$ K, absorbing $Q_H = 1200$ J per cycle. (a) How much heat $Q_C$ is rejected? (b) How much work $W$ is done? (c) Compute $\Delta S_\text{universe}$ per cycle. (d) Now suppose the engine is irreversible and rejects $Q_C = 700$ J instead of the Carnot value. Recompute $\Delta S_\text{universe}$. What changed?

*Tests: Carnot cycle as the ideal ($\Delta S_\text{universe} = 0$) case; comparing to an irreversible engine shows why irreversibility always costs entropy. Difficulty: medium.*

**A3.** A box contains $N = 20$ molecules. All start on the left side. (a) What is $\Omega$ for the initial macrostate? What is $S/k_B$? (b) What is $\Omega$ for the equilibrium macrostate (10 on each side)? What is $S/k_B$? (c) Compute $\Delta S/k_B$ for the spontaneous evolution from all-left to equilibrium. (d) If $N = 40$, by what factor does the equilibrium $\Omega$ exceed the all-left $\Omega$?

*Tests: Boltzmann entropy via microstate counting with small $N$; builds intuition for why the second law strengthens with larger $N$. Difficulty: medium.*

---

### Synthesis

**S1.** One mole of ideal monatomic gas undergoes the following cycle: (1) isothermal expansion at $T = 500$ K from $V$ to $2V$; (2) isochoric cooling from 500 K to 250 K; (3) isothermal compression at 250 K from $2V$ back to $V$; (4) isochoric heating from 250 K to 500 K. Compute $\Delta S$ for the gas in each step and sum them. What is $\Delta S_\text{gas}$ for the complete cycle? Should it be zero? Explain why using the state-function property of entropy.

*Tests: entropy calculations for four different processes chained in a cycle; the key result that ΔS_system = 0 for a complete cycle confirms entropy is a state function. Difficulty: high.*

**S2.** An insulated box is divided in half by a partition. The left side holds 1 mol of nitrogen ($N_2$) at 300 K and 1 atm. The right side holds 1 mol of oxygen ($O_2$) at 300 K and 1 atm. The partition is removed and the gases mix. (a) Does the temperature change? Does the pressure change? (b) Compute the entropy of mixing: $\Delta S_\text{mix} = -nR(x_1 \ln x_1 + x_2 \ln x_2)$ where $x_1 = x_2 = 0.5$ are the mole fractions. (c) Would $\Delta S_\text{mix}$ be the same if both sides had contained identical gases? Explain what this tells you about the physical origin of entropy of mixing.

*Tests: entropy of mixing as a microstate-counting argument; the Gibbs paradox setup (identical gases give zero mixing entropy) makes the statistical interpretation concrete. Difficulty: high.*

---

### Challenge

**C1.** Show from Boltzmann's definition that the entropy of an ideal gas in volume $V$ at temperature $T$ satisfies $\Delta S = nC_V \ln(T_f/T_i) + nR \ln(V_f/V_i)$ for a general process. Do this by noting that the number of accessible microstates scales as $\Omega \propto V^N T^{3N/2}$ for a monatomic gas (the $T^{3N/2}$ factor comes from the number of ways to distribute kinetic energy among $3N$ translational degrees of freedom). Take the logarithm, differentiate, and show that the Clausius and Boltzmann approaches give the same differential $dS$.

*Tests: deriving the general entropy formula from Boltzmann's definition using dimensional reasoning about microstate counting — bridges the two definitions at the level of a derivation rather than a verification. Difficulty: very high.*

---

## LLM Exercises

### Build the entropy / microstate simulator (`07-entropy-microstates.html`)

> **Show.** Boltzmann's $S = k_B \ln \Omega$. For $N$ particles distributed in two halves of a box: $\Omega(n_L) = N!/(n_L!(N-n_L)!)$.
>
> **Say.** Build an entropy-from-microstates simulator.
>
> **Constrain.** D3 v7. A box divided into two halves. $N$ particles (slider, 4 to 100). Each particle, at each time step, hops to the other half with probability 0.5. Count particles in left half ($n_L$). Compute $\Omega(n_L) = \binom{N}{n_L}$ and $S = k_B \ln \Omega$. Display: histogram of $n_L$ over time as the system equilibrates; running maximum entropy; current $S/k_B$. Starting condition: all particles on one side ($n_L = N$, $S = 0$). Animation shows particles spreading; entropy rises and saturates near the maximum at $n_L = N/2$. Filename: `07-entropy-microstates.html`.
>
> **Verify.** (a) Starting with all particles on left, $S$ starts at 0 and rises. (b) Maximum $S$ is achieved when $n_L \approx N/2$. (c) For $N = 20$: max $S/k_B = \ln\binom{20}{10} \approx \ln 184756 \approx 12.13$.

### Exploration

- Watch the system evolve from $n_L = 20$ (all on left) to $n_L \approx 10$. Note: starting with all particles on one side is *not* equilibrium; the system spontaneously evolves to equilibrium.
- The second law is statistical: at $N = 20$, fluctuations are visible. At $N = 200$, fluctuations are smaller. At $N = 10^{20}$, they're invisible.
- Once the system is near equilibrium, count how often $n_L$ deviates by more than 20% from $N/2$. The fluctuation rate decreases dramatically with $N$.

### Extension prompt (chapter bridge)

> **Show.** The microstate counting gives the entropy. The Boltzmann distribution generalizes this: in thermal equilibrium with a reservoir at temperature $T$, the probability of energy $E_i$ is $\propto e^{-E_i/k_BT}$.
>
> **Say.** Build a Boltzmann distribution simulator.
>
> **Constrain.** A system with $N$ energy levels equally spaced by $\Delta E$. Sliders for $T$ and $N$. Display: occupation probability of each level as a bar chart, with $p_i = e^{-E_i/k_BT}/Z$.
>
> **Verify.** At low $T$ ($k_BT \ll \Delta E$): essentially all in ground state. At high $T$ ($k_BT \gg \Delta E$): nearly uniform distribution. Average energy $\langle E\rangle$ rises with $T$.

Save as `07b-boltzmann-preview.html`. Bridge to Chapter 8.

---

**Tags:** entropy, Clausius definition, Boltzmann entropy, microstate counting, second law, irreversibility, free expansion, third law, arrow of time, Maxwell's demon
