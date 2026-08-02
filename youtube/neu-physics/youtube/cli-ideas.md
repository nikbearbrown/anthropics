# NEU Physics — CLI Video Ideas ("X with Claude")

> Scout date: 2026-07-12
> Note: Chapter content is scaffold placeholders only. Cards are derived from the book title/scope (Northeastern Physics course) and standard introductory physics curriculum. Approve after content is written.

---

## Candidate 01 — "Build a Projectile Motion Simulator with Claude"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: Every physics student draws the parabola, but almost no one plots what happens when you change launch angle in real time. The optimum angle isn't always 45° once air drag enters.
- The artifact: An animated Manim scene showing a family of parabolic trajectories for launch angles 15°–75° in 15° steps, with the range plotted as a bar chart that grows beside the simulation; optimal angle highlighted.
- Prompt seed: `claude "Write a Python script that simulates projectile motion for launch angles 15 to 75 degrees in 15-degree steps, no air resistance, v0=20 m/s. Output a table of angle vs range, and a Manim scene that animates each trajectory sequentially and plots the range bar chart."`
- Read / check: Verify range formula R = v²sin(2θ)/g in the table. Check that the Manim scene draws trajectories in order and the bar chart updates after each flight.
- Human supplies: Nothing — fully synthetic. A follow-up with real measured projectile data (e.g., a ball launcher) would require a hardware capture, but the synthetic version is authentic for the lesson.
- Output medium: Manim (animated trajectory family + growing bar chart)
- The change: Add quadratic air drag (fd = -bv) and re-run; show how drag shifts the optimal angle below 45° and shrinks the range envelope.
- Teardown angle: The "always 45° for max range" rule is an idealization. The moment drag enters, the optimum drops — and understanding *why* requires seeing the energy dissipation, not just reciting the formula.
- Exclusions: Magnus effect, 3D trajectory, wind; derivation of equations of motion from Newton's second law.
- Score: 8/10

---

## Candidate 02 — "Measure Free-Fall Acceleration with Claude Code"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: g = 9.8 m/s² is printed in every textbook. But if you drop a ball and time it yourself, how close do you actually get — and where does your error come from?
- The artifact: A Manim-animated scatter plot of measured drop-time vs height data, with a best-fit parabola overlaid, the extracted g value annotated, and a residual plot showing systematic vs random error.
- Prompt seed: `claude "Given drop heights [0.5, 1.0, 1.5, 2.0] m and measured times [0.319, 0.452, 0.553, 0.639] s (with ±0.01 s uncertainty), fit h = 0.5*g*t^2 using scipy.optimize, extract g, compute 95% CI, and animate the fit curve being drawn over the data points in Manim."`
- Read / check: Verify the scipy fit returns g near 9.8 m/s². Check that confidence intervals are computed correctly (not just parameter SE). Confirm Manim draws data points before the fit curve.
- Human supplies: Ideally a real drop-time dataset from a phone slow-motion camera or timing gate — more authentic than the synthetic values. The video can note: "we used these numbers; try yours." Synthetic stand-in is acceptable for demonstration.
- Output medium: Manim (animated scatter + parabola fit reveal)
- The change: Add a systematic error to one timing point (simulate reaction-time bias) and show how it skews g; then use a robust fit (median-based) and compare.
- Teardown angle: Measurement uncertainty is structured, not random. The residual plot is where the lesson lives — it reveals whether your error model is correct, not just how close you got.
- Exclusions: Air resistance on falling sphere, vacuum comparison, derivation of kinematic equations.
- Score: 8/10

---

## Candidate 03 — "Simulate Simple Harmonic Motion with Claude"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: A spring oscillates forever in the equation, but add even a tiny damping term and it decays — in a very specific, predictable way. Claude can plot the envelope and find the damping coefficient from noisy data.
- The artifact: An animated Manim scene showing three side-by-side oscillators (underdamped, critically damped, overdamped), with their x(t) curves drawing in real time and the decay envelope overlaid on the underdamped case.
- Prompt seed: `claude "Simulate a spring-mass system (m=1 kg, k=4 N/m) for three damping values: b=0.5 (underdamped), b=4 (critically damped), b=10 (overdamped). Solve the ODE with scipy.integrate.solve_ivp, plot x(t) for each, and create a Manim scene with three labeled panels animating the motion simultaneously."`
- Read / check: Verify the discriminant condition (b² vs 4mk) classifies each case correctly. Check that the Manim panels are labeled and the underdamped envelope follows exp(-bt/2m).
- Human supplies: Nothing — fully synthetic. A real pendulum with video tracking would be ideal but is not required for the lesson.
- Output medium: Manim (three-panel synchronized animation)
- The change: Extract the damping coefficient from synthetic noisy sensor data (add Gaussian noise to position) using curve fitting; compare fitted b to the true value.
- Teardown angle: Critical damping is the engineering optimum — door closers and shock absorbers target it. Seeing all three cases simultaneously makes the design judgment legible.
- Exclusions: Driven oscillations, resonance frequency sweeps, coupled oscillators.
- Score: 7/10

---

## Candidate 04 — "Plot an Electric Field with Claude Code"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: Every physics textbook shows field-line diagrams for point charges, but they're hand-drawn approximations. What does the real superposition of two opposite charges actually look like — and what happens at the midpoint?
- The artifact: A Manim scene showing the electric field vector arrows for a +q/−q dipole on a 20×20 grid, animating as charge separation increases from 0.1 to 1.0 m; the field magnitude along the axis plotted in a side panel.
- Prompt seed: `claude "Compute the electric field vector E = k*q*(r-r0)/|r-r0|^3 for a +1 nC charge at (0.5, 0) m and a -1 nC charge at (-0.5, 0) m on a 20x20 grid from -2 to 2 m. Use matplotlib quiver to show the field, then create a Manim scene that animates the dipole field as charge separation varies from 0.1 to 1.0 m."`
- Read / check: Verify field direction reversal between charges. Check that the on-axis field magnitude at the midpoint equals 2kq/d² (pointing from + to −). Confirm Manim animation varies separation smoothly.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (animated vector field + side panel line plot)
- The change: Add a third charge (quadrupole geometry) and show how the field pattern changes; discuss why multipole fields decay faster with distance.
- Teardown angle: Superposition is the entire field: each contribution is simple; the combination is rich. Animating the buildup makes superposition a thing you see, not a thing you trust.
- Exclusions: Gauss's law derivation, flux integrals, boundary conditions in conductors.
- Score: 7/10

---

## Candidate 05 — "Research the Physics Behind NEU's Lab Experiments with Claude"
- Source: neu-physics/chapters/00-frontmatter.md (book scope)
- Lane: RESEARCH (Claude assistant)
- Hook: Every intro physics lab has a "correct" answer printed in the manual. But what is the actual measurement uncertainty in the Millikan oil-drop experiment — and why did Millikan's original published value differ from the modern value?
- The artifact: A sourced 4-section brief: (1) the measurement principle, (2) Millikan's original systematic error (selection bias on drops), (3) modern accepted value with uncertainty, (4) a comparison table of historically published e values from 1913 to 2019.
- Prompt seed: `claude "Research the Millikan oil-drop experiment: (1) the measurement principle, (2) the systematic bias in Millikan's original data (he suppressed inconvenient drops), (3) the modern NIST value for the elementary charge with uncertainty, (4) a timeline table of published e values from 1913 to 2019. Cite sources."`
- Read / check: Verify NIST CODATA value for e. Check that the selection-bias criticism is cited (Franklin, 1981 is the key source). Confirm the timeline table spans at least 5 distinct published values.
- Human supplies: Nothing — Claude can synthesize from published literature. A human expert in measurement history would improve the quality of the selection-bias analysis.
- Output medium: slate (4-panel sourced brief rendered as a Remotion slide sequence)
- The change: Extend the brief to compare Millikan's situation to modern replication crises — ask Claude to identify a contemporary case where a field-wide systematic bias was later corrected.
- Teardown angle: The "correct" answer in the textbook was wrong for decades, and the person who got it wrong was the one who defined the measurement method. Authority and accuracy are different.
- Exclusions: The details of Stokes' law drag calculation, electrical circuit diagram of the apparatus.
- Score: 7/10

---

## Candidate 06 — "Build a Wave Interference Simulator with Claude"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: Two speakers playing the same frequency create loud and quiet zones in the room. Claude can compute exactly where — and show why the pattern depends on the wavelength-to-separation ratio.
- The artifact: A Manim animated 2D heatmap of the superposed wave amplitude from two point sources, with dark fringes (destructive) and bright fringes (constructive) appearing as the frequency sweeps from 200 Hz to 2000 Hz.
- Prompt seed: `claude "Simulate 2D wave interference from two point sources at (0, 0.5) m and (0, -0.5) m, frequency 500 Hz, v=343 m/s. On a 200x200 grid from -3 to 3 m, compute |sin(kr1-wt) + sin(kr2-wt)| at t=0. Create a Manim animation that sweeps frequency from 200 to 2000 Hz and updates the heatmap."`
- Read / check: Verify the fringe spacing formula Δy = λL/d at the observation plane. Check that destructive interference appears at d·sin(θ) = (n+½)λ. Confirm the heatmap updates smoothly across the frequency sweep.
- Human supplies: Nothing — fully synthetic. A real room acoustic measurement would be more authentic but is optional.
- Output medium: Manim (animated 2D interference heatmap)
- The change: Switch from two sources to a 5-element phased array; show how adjusting phase offsets steers the main lobe (beam-forming).
- Teardown angle: Interference is not a quirk — it's the foundation of every antenna, lens, and noise-cancelling headphone. The pattern is computable; the physics is exact.
- Exclusions: Diffraction grating derivation, quantum double-slit interpretation.
- Score: 7/10

---

## Candidate 07 — "Compute Entropy Change in a Carnot Cycle with Claude"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: Thermodynamics textbooks show the Carnot cycle as a P-V diagram. But the efficiency formula η = 1 − Tc/Th is a consequence of something deeper — and Claude can show why no engine can beat it by computing entropy on each leg.
- The artifact: A Manim animation of the Carnot cycle on both a P-V diagram and a T-S diagram drawn simultaneously, with the net work area and efficiency annotated; then a side-by-side comparison with a "hot engine" (Th = 800 K vs 600 K) showing the efficiency jump.
- Prompt seed: `claude "Plot a Carnot cycle for Th=600 K, Tc=300 K, V1=1 L, compression ratio 4. Compute P-V and T-S coordinates for each of the four legs (isothermal expansion, adiabatic expansion, isothermal compression, adiabatic compression). Create a Manim scene showing both diagrams animating simultaneously, with efficiency and net work annotated."`
- Read / check: Verify efficiency (1 − 300/600 = 50%). Check that entropy change ΔS = 0 for each adiabatic leg and ΔS = Q/T for each isothermal. Confirm the T-S diagram is a rectangle.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (dual P-V and T-S animated diagrams)
- The change: Compare the Carnot efficiency to a realistic Otto cycle (gasoline engine, γ = 1.4, compression ratio 8) and show the gap; discuss why real engines can't close it.
- Teardown angle: The Carnot limit is not an engineering constraint — it is a consequence of entropy being a state function. You cannot exceed it without violating the second law.
- Exclusions: Statistical mechanics derivation of entropy, Maxwell's demon, refrigerator COP derivation.
- Score: 7/10

---

## Candidate 08 — "Simulate a Quantum Particle in a Box with Claude"
- Source: neu-physics/chapters/02-chapter-01.md (placeholder — content pending)
- Lane: BUILD (Claude Code)
- Hook: Quantum mechanics says electrons in a box can only have certain energies. That sounds like a rule someone made up — until you plot the wavefunctions and watch the energy levels appear from the boundary conditions alone.
- The artifact: A Manim animation of the first five particle-in-a-box wavefunctions drawing sequentially, with their probability density |ψ|² overlaid and the energy level ladder annotated on the right (En = n²π²ℏ²/2mL²).
- Prompt seed: `claude "Compute and plot the first 5 wavefunctions and probability densities for a particle in a 1D infinite square well of width L=1 nm, m=electron mass. Use numpy for the computation and create a Manim animation that draws each wavefunction ψn(x) and |ψn(x)|^2 sequentially, with the energy ladder (in eV) annotated."`
- Read / check: Verify E1 = π²ℏ²/(2mL²) ≈ 0.376 eV for L=1 nm. Check that wavefunctions have n nodes (ψ1 has 0 interior nodes, ψ2 has 1, etc.). Confirm |ψ|² integrates to 1 over the box.
- Human supplies: Nothing — fully synthetic.
- Output medium: Manim (sequential wavefunction + probability density animation with energy ladder)
- The change: Add a finite potential well (barrier height 5 eV) and show how wavefunctions tunnel into the classically forbidden region; compare the energy levels to the infinite well.
- Teardown angle: Quantization is not imposed — it emerges from boundary conditions. The boundary conditions are the physics.
- Exclusions: Schrödinger equation derivation, many-body quantum mechanics, hydrogen atom.
- Score: 8/10
