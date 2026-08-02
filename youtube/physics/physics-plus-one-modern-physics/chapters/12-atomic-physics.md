# Chapter 12 — Atomic Physics
*How two postulates and a counting rule became the entire periodic table.*

In 1909, a graduate student named Hans Geiger sat in a darkened room in Manchester and counted flashes of light on a zinc-sulfide screen. Each flash was a single alpha particle — a helium nucleus, fast and heavy — that had traveled through a thin gold foil and struck the screen. Most of the flashes appeared almost directly ahead, at small angles from the beam. That was expected. A few appeared at angles of twenty, thirty, forty degrees. That was curious. And then, occasionally, one appeared behind the foil — at an angle greater than ninety degrees, having bounced almost directly backward.

Geiger's supervisor, Ernest Rutherford, later said that seeing this was "almost as incredible as if you fired 15-inch shells at tissue paper and they came back and hit you." He was not exaggerating. The result made no sense under the reigning model of the atom, which imagined it as a diffuse ball of positive charge with electrons scattered through it like raisins in a pudding. A diffuse positive ball would deflect a fast heavy particle only slightly, the way a sand dune deflects a bowling ball — not send it backward. Something small and extraordinarily dense was inside the gold atom. Something that could hit back.

Rutherford worked out the mathematics. To produce the observed scattering rate, the positive charge and almost all the mass of the gold atom had to be concentrated in a nucleus roughly $10^{-14}$ meters across. The atom itself is $10^{-10}$ meters across — ten thousand times larger. The nucleus is to the atom as a fly is to a cathedral. Almost everything inside an atom is empty space.

<!-- → [DIAGRAM: Scale comparison of atom vs. nucleus — two concentric circles. Outer circle labeled "atom (~10⁻¹⁰ m)"; inner circle, drawn to correct relative scale (~10⁻⁴ of the radius), labeled "nucleus (~10⁻¹⁴ m)". A third tiny inset shows the fly-in-a-cathedral metaphor with correct proportions. Student should see immediately why Rutherford's result was shocking.] -->

This is the picture every chemistry student learns in the first week. But it immediately creates a catastrophe.

An electron orbiting a nucleus is constantly accelerating — centripetally, changing direction every instant. James Clerk Maxwell's equations, which are correct and were already sixty years old at this point, say unambiguously that any accelerating electric charge radiates energy. The electron should radiate, lose energy, spiral inward, and crash into the nucleus in a time of about $10^{-11}$ seconds. Every atom should collapse. All matter should be unstable.

It isn't.

This is the contradiction that Niels Bohr, a twenty-seven-year-old Dane working in Rutherford's lab, decided to take seriously in 1913. He did not resolve it by finding a flaw in Maxwell's equations or in classical mechanics. He resolved it by postulating that those equations simply do not apply inside the atom in the way you'd expect — that electrons in atoms are somehow exempt from radiating while they remain in certain special orbits, and that radiation happens only during the jump from one orbit to another. The energy of that radiation was exactly the energy difference between the two orbits, packaged as a single photon: $hf = E_i - E_f$.

Bohr's postulate was, he knew, completely arbitrary. "I know it is crazy," he told a friend. "The question is whether it is crazy enough." It turned out to be exactly crazy enough.

---

## The mechanism

To understand Bohr's model, start with the one electron in hydrogen orbiting the one proton.

The Coulomb attraction between the proton (charge $+e$) and the electron (charge $-e$) at distance $r$ provides the centripetal force needed for circular orbit:

$$\frac{ke^2}{r^2} = \frac{m_e v^2}{r}.$$

Here $k = 8.99 \times 10^9 \, \text{N} \cdot \text{m}^2 / \text{C}^2$ is Coulomb's constant. This equation relates the orbital speed $v$ to the radius $r$. Two unknowns, one equation — you need another condition to fix both. In classical mechanics, there is none: the electron could orbit at any radius, at the corresponding speed, and both would be continuous variables. Bohr's quantization condition provides the second equation:

$$m_e v r = n \frac{h}{2\pi}, \quad n = 1, 2, 3, \ldots$$

The orbital angular momentum must be an integer multiple of $h/2\pi$. Solve the two equations simultaneously — eliminate $v$, substitute back — and you find that the allowed radii are:

$$r_n = n^2 a_0, \quad a_0 = \frac{h^2}{4\pi^2 m_e k e^2} = 5.29 \times 10^{-11} \, \text{m}.$$

The quantity $a_0$ is the Bohr radius: the size of the ground-state hydrogen atom. It falls out of the calculation as a combination of fundamental constants. You put in $h$, $m_e$, $k$, and $e$ — four things measured by independent experiments — and out comes a number that matches the measured size of hydrogen to better than 1%. This is not a coincidence you ignore.

The total energy of the electron (kinetic plus potential) at each allowed orbit is:

$$E_n = -\frac{13.6 \, \text{eV}}{n^2}.$$

The ground state, $n = 1$, has energy $-13.6$ eV — that is, it would take 13.6 eV of energy to rip the electron completely free of the proton. The excited states ($n = 2, 3, \ldots$) have less negative energies, approaching zero as $n \to \infty$ (a free electron at rest).

<!-- → [DIAGRAM: Hydrogen energy level diagram — vertical axis is energy in eV, horizontal lines at E_n = −13.6/n² for n = 1 through 6, with n = ∞ (ionization) at 0 eV. Arrows showing the Lyman series (all ending at n=1, labeled UV), Balmer series (ending at n=2, labeled visible, with Balmer-α at 656 nm called out), and Paschen series (ending at n=3, labeled IR). Ground state labeled −13.6 eV. Student should see immediately why Lyman lines are UV and Balmer lines are visible.] -->

When the electron jumps from state $n_i$ to state $n_f$ (with $n_f < n_i$), it releases a photon of energy:

$$E_\gamma = E_i - E_f = 13.6 \, \text{eV} \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right).$$

In terms of wavelength:

$$\frac{1}{\lambda} = R \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right), \quad R = 1.097 \times 10^7 \, \text{m}^{-1}.$$

$R$ is the Rydberg constant. Johann Balmer had found this formula empirically in 1885, fitting it to the four visible spectral lines of hydrogen without the slightest idea why it worked. Bohr derived it from a mechanical model and first principles. The derivation gave not just the form of the formula but the numerical value of $R$ — plug in the four fundamental constants and you get $1.097 \times 10^7 \, \text{m}^{-1}$, matching the measured value to four significant figures.

Let us check one number. The transition $n_i = 3 \to n_f = 2$ gives:

$$\frac{1}{\lambda} = (1.097 \times 10^7) \left( \frac{1}{4} - \frac{1}{9} \right) = (1.097 \times 10^7)(0.139) = 1.524 \times 10^6 \, \text{m}^{-1},$$

$$\lambda = 656 \, \text{nm}.$$

This is the bright red line you see when hydrogen glows — in discharge tubes, in stellar atmospheres, in emission nebulae. It has been measured thousands of times. Bohr's formula gives 656 nm. Experiment gives 656 nm. The theory is not approximately right. It is right.

---

## Why the orbits are stable — the wave interpretation

In 1913, Bohr's quantization rule ($L = nh/2\pi$) had no physical justification. It was a postulate. In 1924, Louis de Broglie gave it one.

De Broglie proposed that any particle with momentum $p$ has an associated wavelength $\lambda = h/p$. Apply this to the orbiting electron: it has a de Broglie wavelength $\lambda = h/(m_e v)$. Now ask: for the orbit to be stable, what condition must the wave satisfy on a closed circle of circumference $2\pi r$?

The condition is that the wave must close on itself — an integer number of wavelengths must fit around the orbit. If the wave does not close — if it returns to its starting point slightly out of phase — it interferes destructively with itself on the next pass, and the next, and eventually cancels. Only standing waves survive. The condition is:

$$n\lambda = 2\pi r_n.$$

Substitute $\lambda = h/(m_e v)$ and rearrange:

$$m_e v r_n = n \frac{h}{2\pi}.$$

That is Bohr's quantization condition, now derived from the requirement that the electron's de Broglie wave be a standing wave on the orbit. The allowed orbits are the ones where the electron, thought of as a wave, resonates with itself. The disallowed orbits are the ones where it destructively interferes.

<!-- → [DIAGRAM: Standing waves on a circular orbit — three panels. Left: n=1, one wavelength fits around the circle (stable). Center: n=3, three wavelengths fit around the circle (stable). Right: non-integer case, wave returns slightly out of phase, showing destructive interference where the waveform crosses itself. Caption: "Only integer fits survive — everything else cancels."] -->

This is why the electron does not radiate while in a stationary orbit. The standing-wave state is an eigenstate of the atom — it is as stable as a vibrating string in its fundamental mode. There is nothing to radiate because there is no oscillating charge distribution; the standing wave is symmetric and static in time. Radiation requires a *transition* — a change from one standing-wave pattern to another — which is a time-varying process. That time variation drives the photon emission.

The picture is beautiful in its simplicity. An atom is a musical instrument. The allowed orbits are the harmonics. The spectrum of emitted light is the chord the atom can play.

---

## More than one electron

Hydrogen is solvable exactly. Everything else requires more machinery.

In 1925, two things happened in quick succession. First, Wolfgang Pauli, age twenty-four, working in Hamburg, proposed a single rule:

*No two electrons in an atom can simultaneously be in the same quantum state.*

Second, George Uhlenbeck and Samuel Goudsmit proposed that electrons have an intrinsic angular momentum — *spin* — that has no classical analogue. The spin quantum number can take only two values: $+\frac{1}{2}$ or $-\frac{1}{2}$. An electron spinning "up" and an electron spinning "down" are different quantum states.

Together, these two facts explain the periodic table completely.

Every quantum state in an atom is labeled by four numbers:

**$n$**, the principal quantum number: $1, 2, 3, \ldots$ Controls the energy and approximate distance from the nucleus. For hydrogen, $E_n = -13.6 \, \text{eV} / n^2$.

**$\ell$**, the orbital angular momentum quantum number: $0, 1, 2, \ldots, n-1$. Labeled s, p, d, f. Determines the shape of the orbital wavefunction — s orbitals are spherical, p orbitals are dumbbells, d orbitals more complicated.

**$m_\ell$**, the magnetic quantum number: $-\ell, -\ell+1, \ldots, +\ell$. There are $2\ell + 1$ values. An s subshell ($\ell = 0$) has one orbital. A p subshell ($\ell = 1$) has three orbitals. A d subshell ($\ell = 2$) has five.

**$m_s$**, the spin quantum number: $+\frac{1}{2}$ or $-\frac{1}{2}$.

<!-- → [TABLE: Quantum number summary — columns: quantum number, symbol, allowed values, physical meaning, number of states. Rows: principal (n), orbital angular momentum (ℓ), magnetic (m_ℓ), spin (m_s). Final row: total states in shell n = 2n². Purpose: give students a single reference they can return to when doing electron configurations.] -->

The Pauli exclusion principle says each combination $(n, \ell, m_\ell, m_s)$ can be occupied by at most one electron. Two electrons can share the same spatial orbital $(n, \ell, m_\ell)$ only if one is spin-up and the other is spin-down.

Count the states available in shell $n$. The number of spatial orbitals is $\sum_{\ell=0}^{n-1} (2\ell+1) = n^2$. Each holds two electrons (spin up and spin down). Shell $n$ can hold $2n^2$ electrons total.

For $n = 1$: $2 \times 1 = 2$ electrons.
For $n = 2$: $2 \times 4 = 8$ electrons.
For $n = 3$: $2 \times 9 = 18$ electrons.
For $n = 4$: $2 \times 16 = 32$ electrons.

These are the numbers that determine the lengths of the rows of the periodic table. Period 1 has 2 elements. Periods 2 and 3 each have 8 elements. Period 4 has 18. The counting is automatic — four quantum numbers plus one exclusion rule, nothing else.

Atoms fill their electrons into orbitals starting from the lowest energy, one state at a time, subject to the exclusion principle. This is why carbon ($Z = 6$) has configuration $1s^2 \, 2s^2 \, 2p^2$ — it has 4 electrons in its outermost shell ($n = 2$) and can form exactly four chemical bonds. This is why oxygen ($Z = 8$) has $1s^2 \, 2s^2 \, 2p^4$ — two unpaired electrons in the 2p subshell, which is why water is $\text{H}_2\text{O}$. This is why neon ($Z = 10$) has $1s^2 \, 2s^2 \, 2p^6$ — its $n = 2$ shell is exactly full, and neon has no chemical desire for anything.

The periodic table is not a list of observed facts organized for convenience. It is a theorem, derivable from quantum mechanics and one exclusion rule.

---

## Seeing inside atoms: characteristic X-rays

In 1913 — the same year as Bohr's paper — a twenty-six-year-old English physicist named Henry Moseley was systematically bombarding metal targets with electrons and measuring the X-ray frequencies produced. He found a strikingly clean pattern: the square root of the characteristic X-ray frequency was linear in the atomic number $Z$ of the target:

$$\sqrt{f_{K_\alpha}} \propto (Z - 1).$$

To understand why, you need to understand what characteristic X-rays are.

When a high-energy electron hits a metal target with enough energy — supplied by accelerating it through a high voltage $V$ — it can knock out an inner-shell electron from a target atom (a $1s$ electron, for instance). This leaves a vacancy. An electron from a higher shell falls in to fill the vacancy, releasing a photon equal to the energy difference between the shells. Because inner-shell energies depend strongly on nuclear charge — they scale roughly as $Z^2$ through the same Bohr-model physics — these "characteristic" photons are X-rays, and their energies are a fingerprint of the element.

The $K_\alpha$ line comes from an $n = 2 \to n = 1$ transition in the target atom. Using a hydrogen-like approximation with one inner electron screening the nucleus (so the effective nuclear charge is $Z_{\text{eff}} \approx Z - 1$):

$$E_{K_\alpha} \approx 13.6 \, \text{eV} \times (Z-1)^2 \times \left(1 - \frac{1}{4}\right) = 13.6 \times 0.75 \times (Z-1)^2 \, \text{eV}.$$

The square root of frequency is proportional to energy is proportional to $(Z-1)^2$, so $\sqrt{f} \propto (Z-1)$. Moseley's empirical law drops out of the theory.

The practical consequence was enormous. Before Moseley, the periodic table was ordered by atomic mass, which is a rough proxy for atomic number but breaks down for several elements (cobalt and nickel were in the wrong order). Moseley's law let you read off the atomic number of any element from its characteristic X-ray frequency. Every element has a unique $Z$, and therefore a unique X-ray signature. Moseley predicted which atomic numbers were missing and where new elements would be found.

There is also the bremsstrahlung, or braking radiation — the continuous X-ray spectrum that is not characteristic of the target. When a fast electron decelerates in the strong fields near a nucleus, it radiates energy over a continuous range. The maximum photon energy occurs when the electron loses all its kinetic energy at once:

$$E_{\max} = qV = hf_{\max}.$$

A tube operating at $80$ kV produces photons up to $80$ keV. A tube at $100$ kV, up to $100$ keV. The minimum wavelength is $\lambda_{\min} = hc/(qV)$. This is why higher-voltage X-ray tubes penetrate thicker or denser materials — the photons are harder.

The total X-ray spectrum from a tube is the sum of both: a continuous bremsstrahlung background from deceleration, with sharp characteristic lines sitting on top of it, at energies specific to the anode material. The lines let you identify the element; the bremsstrahlung gives you the imaging exposure.

<!-- → [CHART: X-ray tube spectrum — horizontal axis is photon energy (keV), vertical axis is intensity. Smooth bremsstrahlung curve rising from a minimum wavelength cutoff (determined by qV) and falling off at higher energies. Two sharp K_α and K_β characteristic peaks superimposed on the continuous background. Label the cutoff energy as qV, label the peaks by name. Caption: "The continuous background comes from deceleration; the sharp peaks are the element's signature."] -->

Moseley enlisted in the British Army in 1914 and was killed at Gallipoli in August 1915. He was twenty-seven. Had he lived, he would almost certainly have received the Nobel Prize. He never did. The work that died with him would have been the work of another decade.

---

## The sodium street lamp

Let me close with one worked example that ties all three ideas together, because it sits in your daily life.

Sodium (Na, $Z = 11$) has electron configuration $1s^2 \, 2s^2 \, 2p^6 \, 3s^1$. One lone electron in the $n = 3$ shell. The low-pressure sodium lamp used for street lighting for most of the twentieth century works by passing an electrical discharge through sodium vapor, exciting that $3s$ electron into the $3p$ subshell ($\Delta\ell = +1$, allowed by the selection rule that quantum transitions require $\Delta\ell = \pm 1$). When the electron falls back from $3p$ to $3s$, it emits a photon. Two closely spaced lines — the sodium D doublet at 589.0 nm and 589.6 nm — give sodium lamps their characteristic brilliant yellow.

The same 589-nm line appears in solar absorption spectra. When sunlight passes through the Sun's cooler outer atmosphere, sodium atoms there absorb exactly those wavelengths, leaving dark gaps (Fraunhofer lines) in the solar spectrum at 589 nm. Joseph Fraunhofer catalogued these lines in 1814 without knowing what they were. By the 1860s, Kirchhoff and Bunsen had matched them to laboratory spectra of known elements. By 1913, Bohr's model explained why the lines were at those specific wavelengths.

<!-- → [IMAGE: Solar absorption spectrum showing Fraunhofer lines — a horizontal band of the visible spectrum (violet to red) crossed by narrow dark vertical lines. The sodium D doublet at 589 nm should be called out with an arrow. Caption: "The dark lines are where atoms in the Sun's atmosphere absorbed exactly the photon energies their electrons needed. Each gap is an element's signature."] -->

That is the arc: from Geiger counting flashes in a darkened room in 1909, to Bohr's standing-wave orbits in 1913, to Pauli's exclusion principle in 1925, to an explanation of every line in every stellar spectrum and the electron configuration of every element. The whole edifice sits on two postulates and four quantum numbers.

---

## Exercises

### Warm-up

**12.1** *(Rutherford scattering)* In Geiger and Marsden's experiment, most alpha particles passed through the gold foil with small deflections, but roughly 1 in 8,000 bounced back. What did the large-angle scattering rule out, and what did it establish? State your answer in one sentence for each.

**12.2** *(Rydberg formula)* Compute the wavelength of the Balmer-$\beta$ line of hydrogen ($n_i = 4 \to n_f = 2$). In which part of the visible spectrum does it fall?

**12.3** *(Quantum numbers)* For the $n = 3$ shell: list every allowed value of $\ell$, every allowed value of $m_\ell$ for each $\ell$, and count the total number of distinct quantum states (including spin). Confirm that the total is $2n^2 = 18$.

**12.4** *(Bohr radius)* The Bohr radius is $a_0 = 5.29 \times 10^{-11}$ m. What is the radius of the $n = 4$ orbit in hydrogen, in nm? What is the energy of an electron in that orbit, in eV?

### Application

**12.5** *(Spectral series)* The Lyman series ($n_f = 1$) falls in the UV; the Balmer series ($n_f = 2$) falls in the visible; the Paschen series ($n_f = 3$) falls in the IR. Using the Rydberg formula, compute the longest-wavelength line of the Lyman series ($n_i = 2$) and confirm it is UV. Then compute the shortest-wavelength line of the Balmer series (the series limit, $n_i \to \infty$) and confirm the series stays visible or near-UV.

**12.6** *(Electron configurations)* Write the ground-state electron configurations for nitrogen ($Z = 7$), silicon ($Z = 14$), and iron ($Z = 26$). For iron, identify how many unpaired 3d electrons there are and explain in one sentence why this makes iron magnetic.

**12.7** *(Noble gas inertness)* Why is argon ($Z = 18$) chemically inert? Answer in terms of its electron configuration and the Pauli exclusion principle — not just "its shell is full."

**12.8** *(X-ray tube)* An X-ray tube operates at 60 kV. Find (a) the maximum X-ray photon energy in keV, and (b) the corresponding minimum wavelength in pm. Show that this photon is far more energetic than any visible photon.

### Synthesis

**12.9** *(Moseley's law)* A sample of unknown metal emits $K_\alpha$ characteristic X-rays at approximately 7.5 keV. Use the approximation $E_{K_\alpha} \approx 13.6 \times 0.75 \times (Z-1)^2$ eV to estimate $Z$. What element is this likely to be? (It is a common transition metal.)

**12.10** *(Periodic table as theorem)* The periodic table closes its first four rows at 2, 10, 18, and 36 electrons (helium, neon, argon, krypton). Show that these closure numbers are not arbitrary but follow from the allowed values of the four quantum numbers and the Pauli exclusion principle. Specifically, show that the cumulative count of electrons at each row boundary equals $\sum_{n=1}^{N} 2n^2$ for the appropriate $N$.

**12.11** *(de Broglie and Bohr)* Derive Bohr's quantization condition $m_e v r = nh/(2\pi)$ from the requirement that an integer number of de Broglie wavelengths fit around the circular orbit of radius $r$. Then use this to show that the Bohr radius $a_0$ falls out when you combine this condition with the Coulomb force equation. State clearly what physical picture motivates the derivation.

### Challenge

**12.12** *(Dimensional analysis of $a_0$)* Without being told the formula, show that the combination $h^2/(m_e k e^2)$ has units of length. Use dimensional analysis: write out the SI units of $h$ (J·s), $m_e$ (kg), $k$ (N·m²/C²), and $e$ (C), and verify that the combination reduces to meters. Then substitute numerical values to recover $a_0 = 5.29 \times 10^{-11}$ m (the factor of $4\pi^2$ is from the algebra; here estimate within an order of magnitude).

**12.13** *(Muonic hydrogen)* A muon is a particle with the same charge as an electron but 207 times heavier. A muonic hydrogen atom consists of a proton orbited by a muon instead of an electron. (a) Using the Bohr model, show that the Bohr radius of muonic hydrogen is $a_0/207$. (b) Compute the ground-state energy. (c) Compute the wavelength of the Lyman-$\alpha$ transition. In which part of the EM spectrum does it fall? (d) Explain in one sentence why muonic atoms have been used to measure the proton's charge radius precisely.

---

## LLM Exercise — Chapter 12: Atomic Physics in Your Anchor Phenomenon

**Project:** Physics Reality Check Logbook
**What you're building this chapter:** A Logbook entry connecting atomic physics — spectral lines, X-rays, electron configurations — to your anchor phenomenon. Most everyday phenomena involve specific elements with specific spectra. The connection is usually accessible.
**Tool:** Claude Project.

### The Prompt

```
I'm continuing my Physics Reality Check Logbook for College Physics
with LLMs. My anchor phenomenon is [paste your 1-sentence description].

For Chapter 12, I want to apply atomic physics — Bohr's model, quantum
numbers, the periodic table, characteristic spectra — to my phenomenon.

Please:

1. Identify ONE atomic-physics aspect of my phenomenon. Examples: for a
   bike commute — sodium street lamps emitting at 589 nm, LED traffic
   signals (semiconductor band gaps which derive from atomic structure),
   the iron in my bike's steel (3d subshell, ferromagnetic). For a coffee
   maker — spectroscopic identification of caffeine (C, H, N, O atoms),
   the sodium D-line in the dye of any colored cup, mineral content of
   water (calcium, sodium, etc.). For a basketball shot — the elements in
   human muscle (carbon-based chemistry), gym lighting (mercury vapor in
   fluorescent bulbs at 254 nm; LEDs based on band-gap engineering). For
   a marathon — caffeine in pre-race coffee, sodium and potassium in
   electrolyte drinks.

2. Apply ONE atomic-physics calculation. Compute a transition wavelength
   using the Rydberg formula, predict a spectral line, estimate ionization
   energy of a key element, identify the electron configuration of a
   specific atom.

3. Specify input numbers and uncertainty.

4. Run the calculation. Report value with units.

5. One sanity check: does the wavelength match a known spectral line of
   the right element?

6. One sentence connecting this to Chapter 13 (radioactivity) — moving
   from atomic to nuclear physics.

Save the output as logbook/chapter-12-atomic.md.
```

### What this produces

A Logbook entry connecting your phenomenon to specific atomic structure or spectroscopy.

### How to adapt this prompt

- *For a phenomenon involving any color:* Color is atomic physics. Identify the atom or molecule responsible.
- *For ChatGPT/Gemini:* Identical with interface substitutions.
- *For Claude Code:* If you have access to a smartphone spectroscope or a recorded spectrum, you can extract the dominant emission lines and identify them by element.

### Connection to previous chapters

Builds directly on the photon ($E = hf$) and the de Broglie wavelength ($\lambda = h/p$). Uses standing-wave ideas from earlier wave mechanics.

### Preview of next chapter

Chapter 13 (radioactivity and nuclear physics) moves from electrons to nuclei — protons and neutrons bound by the strong force, with their own shell structure and "magic numbers." Many of the same principles (quantization, exclusion, characteristic spectra) apply, but at nuclear scales and at energies in MeV rather than eV.

---

## AI Wayback Machine

**Lise Meitner** identified nuclear fission in 1938 — interpreting Otto Hahn's puzzling experimental results during her exile in Sweden. Hahn alone received the Nobel; Meitner's exclusion is one of the most-cited omissions in Nobel history.

**Run this:**

```
Who was Lise Meitner, and how does her work on nuclear fission connect to
atomic physics we covered in this chapter? Keep it to three paragraphs.
End with the single most surprising thing about her career or ideas.
```

→ Search **"Lise Meitner"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through Meitner's 1938 calculation of the energy released in uranium fission.
- Ask it about Meitner's refusal to work on the Manhattan Project and what it meant for her career.

What changes? What gets better? What gets worse?
