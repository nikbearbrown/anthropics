# Chapter 13 — The Big Bang

*A persistent hiss in a New Jersey radio antenna in 1965, blamed first on pigeons, that turned out to be the oldest light in the universe — predicted in detail seventeen years before anyone bothered to look.*

---

In May 1965 two radio astronomers at Bell Labs in Holmdel, New Jersey, published a one-page paper titled "A Measurement of Excess Antenna Temperature at 4080 Mc/s." Their 20-foot horn antenna, built to track communications satellites, was picking up 3.5 degrees Kelvin of radiation from every direction at every hour of every season, no matter what they did to the instrument.

Arno Penzias and Robert Wilson had spent the better part of a year trying to make the signal go away. They cooled the receiver. They checked the cabling. They climbed into the antenna throat and scrubbed out a deposit of what they called, in the paper, "white dielectric material" left by nesting pigeons. The pigeons were relocated to a facility in Whippany, New Jersey. The pigeons flew back. Nothing changed the 3.5 K.

![Schematic of the Bell Labs Holmdel horn antenna in 1965. An excess 3.5 K isotropic signal arrived from every direction at every hour. Pigeon dielectric coating was scrubbed; the signal stayed. Gamow, Alpher, and Herma...](../images/13-the-big-bang-fig-01.png)
*Figure 13.1 — Penzias & Wilson's Antenna and the Pigeons*

At Princeton, fifteen miles away, Robert Dicke's group was constructing a receiver to look for exactly this signal. The theory had been worked out in 1948 by Gamow, Alpher, and Herman: if the universe began hot and dense, the radiation left over from that early epoch — stretched and cooled by the expansion of space — should fill the sky today at a few degrees Kelvin. The paper had been published. It had been ignored for seventeen years. When Penzias made a phone call that eventually reached Dicke, Dicke listened for a minute, hung up, and told his team: "Well, boys, we've been scooped."

What Penzias and Wilson had stumbled onto is the oldest light we can see — radiation that last interacted with matter when the universe was 380,000 years old, stretched from infrared into microwaves by the 13.8 billion years of expansion since. It was predicted before it was found. The prediction was quantitative. The measurement confirmed it.

![Logarithmic timeline from 10^-35 seconds to 13.8 billion years. Major epochs marked: inflation, quark-hadron transition, neutrino decoupling, big-bang nucleosynthesis, recombination/CMB, first stars, first galaxies, s...](../images/13-the-big-bang-fig-05.png)
*Figure 13.5 — Cosmic Timeline from 10⁻³⁵ s to Today*

That is the story this chapter is about.

---

## Hubble's law and what it means

Start with something you can verify at a telescope.

In 1929 Edwin Hubble published a short paper showing that the spectral lines of distant galaxies are systematically shifted to longer wavelengths, and that the shift is proportional to distance. Treating the shift as Doppler recession:

$$v = H_0 \, d$$

A galaxy one megaparsec away recedes at $H_0$ km/s. The modern value is roughly 70 km/s per megaparsec — contested, and we will come back to why. A galaxy at 10 Mpc recedes ten times faster. At 1,000 Mpc, 70,000 km/s, close to a quarter of the speed of light.

One note on credit: in 1927 — two years before Hubble — Georges Lemaître, a Belgian priest and physicist, derived this exact relation from Einstein's equations and estimated the constant. He published it in French in a small Belgian journal. When the paper was translated into English in 1931 the relevant paragraphs were absent — dropped by Lemaître, or by editors, historians still argue. Hubble's name attached to the law. The physics belongs to both.

![Left: Hubble's 1929 original plot, 24 galaxies with H_0 around 500 km/s/Mpc (wrong by sevenfold). Right: modern Pantheon+ Type Ia data extending to redshift ~0.8 with H_0 around 70 km/s/Mpc. Lemaitre derived the same...](../images/13-the-big-bang-fig-02.png)
*Figure 13.2 — Hubble's Law: Recession Velocity vs Distance*

Now, what does the law mean? The naïve reading is that galaxies are flying outward through space, like shrapnel from an explosion, with us at the center. This is wrong on every count. The general-relativistic reading is that space itself is stretching — the distances between galaxies grow because the metric that defines distance is expanding, not because the galaxies are racing through a static background. The galaxies are mostly sitting still in their local patches of space while those patches are carried apart.

The balloon analogy is imperfect but earns its place. Glue dots onto the surface of an uninflated balloon and blow it up. Each dot sees every other receding, faster if farther. No dot is the center. The recession is not motion across the rubber; it is the rubber growing. The analogy breaks because the balloon is a 2D surface embedded in a 3D space we can step outside of; the universe has no outside vantage point. But the kinematics — everywhere receding, no center, velocity proportional to distance — are right.

<!-- → [IMAGE: Two-panel balloon analogy diagram — left panel: balloon partially inflated with four dots labeled A, B, C, D and arrows showing distances between them; right panel: same balloon more inflated, same dots now farther apart, arrows longer; caption should note that no dot is the center of expansion, every dot sees every other receding, and the dots are not moving across the surface — the surface itself is growing] -->

Running the film backward, $v = H_0 d$ compresses everything to a point at some finite past moment. The crude estimate of when:

$$T_0 \approx \frac{1}{H_0}$$

One megaparsec is $3.086 \times 10^{22}$ m, so $H_0 = 70$ km/s/Mpc converts to $H_0 \approx 2.27 \times 10^{-18}$ s$^{-1}$, giving:

$$\frac{1}{H_0} \approx 4.4 \times 10^{17} \text{ s} \approx 14 \text{ billion years}$$

The careful answer — integrating the expansion history through a period of gravity-dominated deceleration followed by dark-energy-driven acceleration — is 13.8 billion years. The crude estimate is off by about 1.5%, which is a remarkable coincidence: in the universe we happen to live in, with $\Omega_m \approx 0.3$ and $\Omega_\Lambda \approx 0.7$, the two corrections nearly cancel. A universe with very different parameters would have $1/H_0$ off by 50% or more. The lesson is that $1/H_0$ is a useful order-of-magnitude estimate; the near-exact agreement with 13.8 Gyr is a consistency check on the standard model, not a derivation.

---

## The three pillars

The recession alone is suggestive. It tells you the universe had a hot dense past. It does not tell you what conditions were like in that past, or whether the hot-dense-past story is really true. For that you need independent evidence from different physical regimes. There are three pillars.

**Pillar 1: the recession.** Already described. The redshift-distance relation holds from the nearest galaxies out to redshifts beyond 10, measured by JWST. Farther galaxies redshift more. The universe was smaller in the past.

**Pillar 2: the cosmic microwave background.** Gamow, Alpher, and Herman's 1948 prediction: a hot, dense early universe in thermal equilibrium with radiation would leave behind, when the universe cooled enough for neutral atoms to form, a thermal bath of photons at a temperature set by how much the universe has expanded since. Penzias and Wilson found it at 3.5 K in 1965. COBE measured the full spectrum in 1990 and found it to be, within one part in ten thousand, a perfect blackbody at 2.725 K. We will spend serious time on this in the next section.

**Pillar 3: primordial element abundances.** The universe was hot enough for nuclear fusion only in its first few minutes. Starting from a thermal soup of protons and neutrons with a neutron-to-proton ratio set by the weak force as the temperature fell, the physics predicts: roughly 25% helium-4 by mass, 75% hydrogen, deuterium at about 2.5 parts per hundred thousand by number, trace helium-3 and lithium-7. The predictions follow from well-tested nuclear reaction rates, the expansion rate at those temperatures, and the measured baryon density (from the CMB acoustic peaks). Measurements in the oldest, most metal-poor gas clouds in the universe match the helium-4 and deuterium predictions within their uncertainties. Lithium-7 is off by a factor of three — the lithium problem — and remains unresolved. But the two dominant species agree, and they were set by completely different physics (helium by the neutron-to-proton freeze-out ratio, deuterium by the baryon density).

![Primordial mass fractions of H, He, D, and Li-7. BBN predictions follow from the neutron-to-proton ratio frozen at temperature 10^10 K during the first 3 minutes. Hydrogen, helium-4, and deuterium agree with observati...](../images/13-the-big-bang-fig-06.png)
*Figure 13.6 — Primordial Element Abundances: BBN Prediction vs Observation*

Three observations from three physical regimes — galaxy dynamics now, photons released at 380,000 years, isotope ratios fixed in the first three minutes — give a single consistent history. The convergence is the argument. No competing model has explained all three.

<!-- → [TABLE: The three pillars side by side — columns: Observation, Physical regime, Timescale probed, Predicted by Big Bang model, Observed value, Agreement; rows: (1) Galaxy recession / Hubble's law, dynamics of galaxies today, ~13.8 Gyr, v = H₀d, measured for thousands of galaxies, yes; (2) CMB blackbody spectrum, photons decoupled at 380,000 yr, T = 2.725 K, COBE FIRAS 2.725 K, yes to 1 part in 10⁴; (3) He-4 mass fraction, BBN at t < 3 min, ~25%, observed ~24–25% in metal-poor gas, yes; caption should emphasize that agreement across three independent physical regimes is the argument, not any single pillar alone] -->

---

## Why the CMB blackbody spectrum is the smoking gun

Here is where I want to slow down and be precise, because this is the deepest piece of evidence.

A blackbody spectrum (Chapter 3) is the radiation field in thermal equilibrium at temperature $T$. It is a specific mathematical curve — the Planck function — that depends only on $T$ and on two fundamental constants ($h$ and $k_B$). Nothing else. Not the composition of the emitting matter, not the history of how the equilibrium was reached, not the geometry of the system. Any system that has been in thermal equilibrium long enough radiates a Planck spectrum.

Real astrophysical sources are not perfect blackbodies. Stars have absorption lines. Hot gas has emission lines. Dust scatters and reprocesses light. Synchrotron radiation from electrons in magnetic fields follows a power law, not a Planck curve. You can always tell an impure source from a true thermal field if you have good enough instruments, because an impure source matches the Planck curve at some wavelengths and deviates at others.

The CMB is different. COBE's FIRAS instrument measured the CMB spectrum from 0.5 to 5 millimeters — across the full Planck peak and well down both sides — and found a perfect blackbody at $T = 2.725 \pm 0.001$ K. The residuals from the Planck curve were consistent with zero at one part in ten thousand. The error bars on the published figure are smaller than the line width of the plotted curve. John Mather presented the spectrum at an American Astronomical Society meeting in 1990 and received a standing ovation from a room full of astronomers who recognized what they were looking at.

Why is a perfect blackbody the smoking gun? Because there is no way to produce one except from a system that was once in thermal equilibrium. You cannot assemble a perfect Planck spectrum from astrophysical sources without invoking a hot dense past. Starlight integrated over all stars and all history does not make a blackbody — it makes something with structure, lines, power-law tails. Dust emission does not make a blackbody at 2.725 K across three decades of wavelength. Nothing local does. The only known mechanism for producing a perfectly thermal microwave background filling all of space is the one Gamow, Alpher, and Herman described: the universe was once hot, dense, and opaque, with radiation and matter in thermal equilibrium; then it cooled enough for neutral atoms to form; the radiation decoupled and streamed freely; the expansion stretched every wavelength by the same factor, preserving the Planck shape while cooling the temperature from ~3,000 K at decoupling to 2.725 K today.

![Two Planck blackbody curves on a log wavelength axis. Recombination-era at 3,000 K peaks near 970 nm (visible/near-IR). Today's 2.725 K peaks at 1.06 mm in the microwave — exactly where Penzias and Wilson's radio ante...](../images/13-the-big-bang-fig-03.png)
*Figure 13.3 — Wien's Law Applied to CMB: 2.725 K → 1.06 mm Peak*

Let me check the numbers. Wien's law gives the peak wavelength for a blackbody at temperature $T$:

$$\lambda_{\text{peak}} = \frac{b}{T} = \frac{2.9 \times 10^{-3} \text{ m·K}}{2.725 \text{ K}} \approx 1.06 \text{ mm}$$

About a millimeter. That is the microwave band — which is why Penzias and Wilson detected it with a radio antenna designed to track satellites, not with an optical telescope. Their antenna was sensitive to the right wavelength range by a coincidence of engineering, not by design.

At recombination, the universe had expanded by a factor of about 1,100 less than it has today, so the temperature was $2.725 \times 1100 \approx 3,000$ K. Wien's law at 3,000 K:

$$\lambda_{\text{peak}} = \frac{2.9 \times 10^{-3}}{3000} \approx 970 \text{ nm}$$

Near-infrared, just outside the red end of the visible spectrum. At the moment the universe became transparent, it was glowing a dim, deep red. The light we see as the CMB today was that red glow, stretched a thousandfold by 13.4 billion years of expansion.

<!-- → [CHART: The COBE FIRAS CMB spectrum — x-axis: frequency in GHz (or wavelength in mm, from 0.5 to 5 mm); y-axis: specific intensity; plotted curve: theoretical Planck function at T = 2.725 K; plotted points: COBE FIRAS measured data; the two should be visually indistinguishable, with residuals shown in a lower panel confirming zero to one part in 10⁴; caption should note that the error bars on the FIRAS data are smaller than the plotted line, making this the most perfect blackbody spectrum observed in nature] -->

![COBE FIRAS spectrum of the cosmic microwave background, 1990. A single Planck curve at T = 2.725 K with ~30 data points overlaid. Error bars smaller than the line width. Agreement at one part in 10,000. Only thermal e...](../images/13-the-big-bang-fig-04.png)
*Figure 13.4 — COBE FIRAS CMB Blackbody: The Smoking Gun*

The Planck prediction is the riskiest test. A model can fake a thermal signal at one frequency — there are always noise sources and emission mechanisms that could mimic a narrow spike. Matching the Planck curve from 0.5 to 5 mm — across a factor of ten in wavelength — requires the radiation to actually be thermal. The CMB passes this test at one part in ten thousand. That is the smoking gun.

---

## The acceleration and what we do not know

The 1998 supernova measurements changed the picture in a way nobody expected.

Two independent teams — the Supernova Cosmology Project and the High-Z Supernova Search Team — were measuring Type Ia supernovae at redshifts up to $z \approx 0.8$ to measure how fast the expansion was decelerating under gravity. Both teams expected deceleration. Both found acceleration. Supernovae at high redshift were fainter than a decelerating universe would predict — farther than expected. The expansion is speeding up. The 2011 Nobel Prize recognized this result.

Acceleration requires a component with negative pressure — something that acts against gravity rather than with it. The simplest description is Einstein's cosmological constant $\Lambda$, an energy density of empty space that does not dilute as space expands. Combined with the CMB acoustic-peak measurements that constrain geometry and total energy density, the modern accounting is:

$$\Omega_{\text{baryon}} \approx 0.05, \quad \Omega_{\text{dark matter}} \approx 0.27, \quad \Omega_\Lambda \approx 0.68$$

Ordinary matter — every atom in every star, planet, and person — is 5% of the energy budget of the universe. Dark matter is inferred from gravitational effects (galaxy rotation curves, gravitational lensing, cluster dynamics) and has never been directly detected as a particle. Dark energy is the name we have given to whatever is causing the acceleration; "a cosmological constant" is a phenomenological description, not a mechanism. Quantum field theory's estimate of the vacuum energy density — the most obvious candidate for dark energy — is off from the observed value by 120 orders of magnitude. This disagreement is the worst prediction in the history of physics. The honest statement is that we have named the 68% and measured its effect, and we do not know what it is.

<!-- → [CHART: Pie chart showing the composition of the universe's energy budget — three slices: ordinary baryonic matter (5%), dark matter (27%), dark energy / cosmological constant (68%); caption should note that only the 5% baryonic slice is composed of atoms we understand, and that "dark" in both cases means we infer these components from their gravitational effects or from accelerating expansion, not from direct detection] -->

![Left: a pie chart of the cosmic energy budget — 4.9% ordinary matter, 26.8% dark matter, 68.3% dark energy. Right: H_0 measurements with SH0ES at 73.0 km/s/Mpc and Planck at 67.4 km/s/Mpc, in 5-sigma disagreement.](../images/13-the-big-bang-fig-07.png)
*Figure 13.7 — ΛCDM Composition Pie + Hubble Tension*

---

## The Hubble tension

There is one live disagreement in the standard model that I want to name honestly.

The CMB acoustic-peak measurements from Planck give $H_0 = 67.4 \pm 0.5$ km/s/Mpc. The local distance ladder — Cepheids calibrating Type Ia supernovae calibrating the Hubble flow — gives $H_0 = 73.0 \pm 1.0$ km/s/Mpc from the SH0ES team. The disagreement is about 5.7 km/s/Mpc, or roughly 5σ.

These are not two measurements of the same thing by two methods. Planck measures $H_0$ indirectly: it fits the CMB acoustic spectrum to a six-parameter cosmological model and extrapolates that model forward 13.8 billion years to the present expansion rate. The local ladder measures $H_0$ directly from velocities and distances in the nearby universe today. They are measuring the same number, but one measures it now and the other infers it from what the universe looked like when it was 380,000 years old.

The disagreement could mean the local ladder has a systematic error somewhere — in the Cepheid period-luminosity relation, in the Type Ia calibration, in how metallicity or dust is corrected for. It could mean the cosmological model is missing an ingredient that changes the early-universe sound horizon, altering the Planck inference. Or it could mean both are right and something unexpected separates early- and late-universe physics.

As of now, no single systematic has been identified that explains the full 5.7 km/s/Mpc gap. Independent local methods — the Tip of the Red Giant Branch, gravitational-wave standard sirens, megamaser distances — give results scattered between the two values, not decisively resolving the tension. The gravitational-wave method is the most promising long-term discriminator: the waveform of a binary neutron-star merger encodes the luminosity distance directly from general relativity, with no calibration chain. A catalog of tens of events from future LIGO runs would settle whether the siren $H_0$ lands near 67 or near 73. If near 67, the local ladder has a hidden systematic. If near 73, the cosmological model is incomplete. Either result matters.

---

## What would change my mind

The CMB blackbody spectrum is the load-bearing piece. A reproducible departure from the Planck curve at one part in a thousand or larger, after every foreground source is subtracted and confirmed by an independent instrument, would require a fundamental rewrite. Current limits from COBE FIRAS constrain spectral distortions below one part in $10^5$. The proposed PIXIE and LiteBIRD missions aim to push another two orders of magnitude. A second mind-changer: a primordial helium-4 fraction measured at 12% or 38% rather than 25%. A factor-of-two miss from the nucleosynthesis prediction would mean the early thermal history is wrong somewhere fundamental, and the whole framework would need rebuilding. Neither result has appeared. Both would be instantly decisive if they did.

---

## Exercises

**Warm-up.** A galaxy in the Virgo Cluster is approximately 16.5 Mpc away. (a) Using $H_0 = 70$ km/s/Mpc, predict its recession velocity. (b) Using the non-relativistic Doppler formula $\Delta\lambda/\lambda = v/c$, predict how much the hydrogen-alpha line (rest wavelength 656.3 nm) would be shifted in this galaxy. (c) Would this shift be detectable with a modern spectrograph? *(Tests: Hubble's law, Doppler shift, connecting the two.)*

**Warm-up.** The CMB temperature today is $T = 2.725$ K. (a) Use Wien's law to find the peak wavelength of the CMB today, and confirm it falls in the microwave band. (b) At recombination the universe was about 1,100 times smaller; the temperature scales inversely with the scale factor. Compute the CMB temperature at recombination. (c) Use Wien's law again to find the peak wavelength at recombination — in what part of the electromagnetic spectrum does it fall? *(Tests: Wien's law applied twice, temperature-scale-factor scaling.)*

**Application.** Convert $H_0 = 70$ km/s/Mpc to SI units (s$^{-1}$). Then compute $1/H_0$ in seconds and convert to years. Compare to the accepted age of 13.8 Gyr and compute the percentage error of the $1/H_0$ estimate. *(Tests: unit conversion, order-of-magnitude age estimate, quantifying how good the approximation is.)*

**Application.** Big Bang nucleosynthesis predicts that the helium-4 mass fraction in the oldest gas should be about 25%. (a) Why is it important to measure helium in *metal-poor* environments (old dwarf galaxies, metal-poor gas clouds) rather than in the Sun or solar neighborhood? (b) The Sun's current helium fraction is about 28%. Explain in one sentence why this is higher than the primordial 25% — where did the extra helium come from? (c) What would it mean for the Big Bang model if an old gas cloud were measured with a helium fraction of 10%? *(Tests: distinguishing primordial from stellar nucleosynthesis, what constitutes falsifying evidence.)*

**Synthesis.** In 1948 Gamow, Alpher, and Herman predicted a residual thermal radiation background at a few Kelvin. In 1965 Penzias and Wilson found 3.5 K excess emission. In 1990 COBE measured the full spectrum and found a perfect blackbody at 2.725 K. (a) Which of these three results is the most powerful test of the Big Bang model, and why? (b) Explain why finding a thermal signal at *one frequency* (Penzias and Wilson's measurement) is far weaker evidence than finding a Planck spectrum *across a decade of wavelength* (COBE FIRAS). (c) What alternative model could, in principle, produce a thermal-looking signal at one frequency that would fail the FIRAS multi-frequency test? *(Tests: why breadth of wavelength coverage matters, nature of the blackbody test, distinguishing partial from complete evidence.)*

**Synthesis.** The Hubble tension. SH0ES measures $H_0 = 73.0 \pm 1.0$ km/s/Mpc; Planck measures $H_0 = 67.4 \pm 0.5$ km/s/Mpc. (a) Compute the difference and the combined uncertainty (add in quadrature). Express the disagreement in standard deviations. (b) In plain language, explain why these two measurements are *not* measuring the same quantity in the same way. (c) Name one specific change to the local distance ladder that would move the SH0ES value down, and one change to the early-universe model that would move the Planck value up. *(Tests: significance of tension, conceptual distinction between direct and model-extrapolated measurements, identifying where each answer could be wrong.)*

**Challenge.** The universe's energy budget is $\Omega_\text{baryon} \approx 0.05$, $\Omega_\text{DM} \approx 0.27$, $\Omega_\Lambda \approx 0.68$. (a) Quantum field theory predicts the vacuum energy density (the simplest dark energy candidate) to be approximately $\rho_\text{vac} \sim (E_\text{Planck})^4 / (\hbar c)^3$, where $E_\text{Planck} \approx 10^{19}$ GeV. The observed dark energy density is $\rho_\Lambda \approx 10^{-29}$ g/cm³. Without doing the full calculation, explain in order-of-magnitude terms why the ratio $\rho_\text{vac}/\rho_\Lambda$ is famously described as "120 orders of magnitude." (b) Does this disagreement constitute a failure of the Big Bang model? Explain why or why not. (c) What kind of new theoretical framework would be needed to explain why $\rho_\Lambda$ is so much smaller than the QFT estimate — and why does the problem remain unsolved? *(Tests: the cosmological constant problem, distinguishing observational confirmation from theoretical explanation, limits of current physics.)*

---

## LLM Exercises

### Build the Hubble diagram + CMB blackbody simulator (`13-hubble-cmb.html`)

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** A two-panel D3 v7 visualization. Left: a Hubble diagram with recession velocity (km/s) vs. distance (Mpc), populated with real Type Ia supernova data from the Pantheon+ sample, and a slider-controlled best-fit line $v = H_0 d$. Display residual sum of squares so the user can fit by eye. Right: the CMB blackbody spectrum $B_\lambda(T)$ at $T = 2.725$ K from 0.1 to 10 mm, with COBE FIRAS data overlaid and a slider varying $T$ from 1 to 5 K. Annotate the Wien peak dynamically.
>
> **Say.** Use $B_\lambda(T) = (2hc^2/\lambda^5) \cdot 1/(e^{hc/\lambda k_B T} - 1)$. For the Hubble panel, distance moduli convert to Mpc via $d = 10^{(m - M + 5)/5}$ pc. Show $H_0$ and $1/H_0$ (in Gyr) next to the slider.
>
> **Constrain.** D3 v7 only. Filename: `13-hubble-cmb.html`. Sliders update in real time.
>
> **Verify.** (a) $H_0 = 70$ minimizes the Hubble residual. (b) $T = 2.725$ K gives a Wien peak at ~1.06 mm. (c) $T = 2.000$ K moves the peak to ~1.45 mm. (d) $T = 5.000$ K moves it to ~0.58 mm — well outside the FIRAS data.

### Exploration

- Drag $H_0$ from 60 to 80 km/s/Mpc and watch $1/H_0$ change from 16.3 to 12.2 Gyr. The careful answer (13.8 Gyr) sits inside this range — but the spread is the full span of the Hubble tension.
- On the CMB panel, push $T$ to 3 K. The curve overshoots the FIRAS points by many standard deviations. Try 2.726 and 2.724 K — FIRAS constrains $T$ to milliKelvin precision.

### Bridge to Chapter 14

> **Show.** The universe is 13.8 billion years old, expanding, and contains roughly $10^{24}$ stars. Most of those stars host planets. The remaining question is the one Fermi asked at lunch in 1950: *if all this physics is universal, where is everybody?*
>
> **Say.** Add a third panel showing the Drake equation with sliders for each of its seven factors, computing $N$ (the expected number of communicating civilizations in the Milky Way) in real time.

Save as `13b-drake-equation-preview.html`. Lead-in to Chapter 14 — *Life in the Universe*.

---

**Tags:** Big Bang, Hubble's law, cosmic microwave background, Penzias and Wilson, Lemaître, COBE FIRAS, nucleosynthesis, dark energy, Hubble tension, ΛCDM
