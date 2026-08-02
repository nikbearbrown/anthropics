# Bear's Doodles — Quantum Mechanics: A Companion Guide Video Ideas

## Candidate 01 — Why a Particle in a Box Cannot Sit Still
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Production mode: Manim visualization
- Hook: The bottom rung of the energy ladder is never on the floor — a trapped particle can't be brought to rest, no matter how you cool it.
- Core idea: Confinement forces the wavefunction to fit as a standing half-wave between the walls; fitting means curvature, curvature means kinetic energy, so the ground state sits above zero.
- Visual object: A single standing half-wave trapped between two walls, its curvature highlighted as the box narrows
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: wave, standing wave, boundary condition, kinetic energy
- Exclusions: no full boundary-value derivation, no normalization constant, no n² spectrum table, no uncertainty-principle algebra beyond one plain sentence
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-pib-zero-point/vox-pib-zero-point-review.mp4`

## Candidate 02 — Why a Stationary State Isn't Standing Still
- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Production mode: Manim visualization
- Hook: A "stationary" quantum state secretly spins — and when two of them spin together, you get every color of light an atom ever emits.
- Core idea: One energy eigenstate's phase rotates invisibly (|ψ|² is flat), but superpose two energies and the phases beat at the Bohr frequency, making the probability cloud rock back and forth — that beat is a spectral line.
- Visual object: One phasor rotating invisibly beside two phasors beating into a sloshing probability cloud
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: wavefunction, phase, energy level, probability density
- Exclusions: no time-evolution operator formalism, no ⟨x⟩(t) integral, no Fourier expansion, no discussion of interpretations
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-stationary-phase/vox-stationary-phase-review.mp4`

## Candidate 03 — Why an Electron Needs Two Full Turns to Come Back
- Source: `quantum-mechanics-a-companion-guide/chapters/07-angular-momentum.md`
- Production mode: Manim visualization
- Hook: Turn an electron all the way around — 360° — and it comes back as the negative of itself. It only truly returns after 720°.
- Core idea: A spin-½ state rotates through the factor θ/2, so a 2π rotation gives −1; this isn't math bookkeeping — neutron interferometry measured the minus sign as a real phase shift.
- Visual object: A spinor arrow whose "sign flag" flips at 360° and only resets at 720°, shown against a normal vector that resets at 360°
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: rotation, vector, spin as intrinsic angular momentum, interference
- Exclusions: no SU(2)/SO(3) group theory, no Pauli-matrix exponential derivation, no full neutron-interferometer optics
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-spinor-720/vox-spinor-720-review.mp4`

## Candidate 04 — Why One Electron Interferes With Itself
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Production mode: Manim visualization
- Hook: Fire electrons one at a time, so there's never a second electron in the machine — and a wave-interference pattern still builds up, dot by dot.
- Core idea: Each electron arrives as a single point, but the pattern of many points is the interference of its own probability amplitude passing through both slits — matter has a wavelength λ = h/p.
- Visual object: A detector screen accumulating single dots that slowly resolve into bright and dark fringes
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: wave interference, de Broglie wavelength, probability
- Exclusions: no complex-amplitude algebra (that's Candidate 17), no path-integral language, no which-path/decoherence tangent
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-double-slit-self/vox-double-slit-self-review.mp4`

## Candidate 05 — Why a Particle Can Walk Through a Wall
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Production mode: Manim visualization
- Hook: Throw a classical ball at a wall it can't climb and it always bounces back. A quantum particle sometimes just appears on the other side.
- Core idea: The wavefunction doesn't stop at a barrier — it decays exponentially inside it, and if the barrier is thin enough some amplitude survives to the far side; halving the width multiplies the transmission by orders of magnitude.
- Visual object: A wave hitting a barrier, decaying to a thin surviving tail on the far side that grows dramatically as the barrier narrows
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: wavefunction, classically forbidden region, exponential decay
- Exclusions: no transmission-coefficient derivation, no WKB integral, no sinh² exact formula, no tunneling-time controversy
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-tunneling-wall/vox-tunneling-wall-review.mp4`

## Candidate 06 — Why the Electron Has No Orbit, Only a Cloud
- Source: `quantum-mechanics-a-companion-guide/chapters/06-the-hydrogen-atom.md`
- Production mode: Manim visualization
- Hook: Bohr's atom has the electron on a circle at one radius. But the electron's most likely radius and its average radius are different numbers — and a circle can't do that.
- Core idea: The radial probability P(r) peaks at the Bohr radius a₀ but has a long tail outward, so the mean (3/2·a₀) sits past the peak; two different "typical radii" is the mathematical fingerprint of a distribution, not an orbit.
- Visual object: The P(r) curve with two markers — peak at a₀, mean at 1.5a₀ — that refuse to coincide because of the tail
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: probability distribution, mean vs mode, hydrogen ground state as a cloud
- Exclusions: no radial Schrödinger derivation, no ansatz/normalization algebra, no SO(4) symmetry, no spherical-harmonic machinery
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-hydrogen-cloud/vox-hydrogen-cloud-review.mp4`

## Candidate 07 — Why Two Electrons Avoid Each Other With No Force
- Source: `quantum-mechanics-a-companion-guide/chapters/08-identical-particles.md`
- Production mode: Manim visualization
- Hook: Two electrons stay farther apart than random chance — even with every force switched off. Nothing pushes them; the symmetry of the wavefunction does it.
- Core idea: Because electrons are identical fermions, their joint wavefunction must be antisymmetric, which forces a node whenever they'd sit at the same place — so they're statistically separated (bosons, symmetric, huddle closer) with no term in the Hamiltonian.
- Visual object: A 2D joint-probability sheet over (x₁, x₂) with a diagonal node for fermions vs a diagonal ridge for bosons
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: identical particles, symmetric vs antisymmetric, probability density
- Exclusions: no Slater determinant, no helium exchange-integral J/K algebra, no spin-statistics-theorem proof
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-exchange-stats/vox-exchange-stats-review.mp4`

## Candidate 08 — Why Uncertainty Isn't About Bumping the Particle
- Source: `quantum-mechanics-a-companion-guide/chapters/05-quantum-formalism.md`
- Production mode: Manim visualization
- Hook: The famous story says you blur a particle's momentum by hitting it with a photon to see it. That story is wrong about what the uncertainty principle actually is.
- Core idea: Robertson's inequality is a property of the state itself — before any measurement — where sharpening the position width forces the momentum width to widen; no apparatus, no kick, just the algebra of non-commuting operators.
- Visual object: Two coupled width-gauges for x and p; squeezing one visibly stretches the other, with no "photon" ever entering the frame
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: probability spread/standard deviation, position and momentum, wavefunction
- Exclusions: no Cauchy–Schwarz proof, no commutator algebra, no Ozawa measurement-disturbance inequality beyond one contrast sentence
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-uncertainty-state/vox-uncertainty-state-review.mp4`

## Candidate 09 — Why 2 Becomes 2√2 (How Bell Beat Einstein)
- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`
- Production mode: Manim visualization
- Hook: If the world had hidden, pre-set answers, a certain correlation score can never exceed 2. Entangled particles hit 2√2 — and experiments agree.
- Core idea: Any local-hidden-variable theory caps the CHSH combination at 2, but the quantum correlation −cos θ between measurement angles pushes it to 2√2; that 41% gap is measurable and rules out Einstein's pre-set-answer picture.
- Visual object: A number line with three zones (classical ≤2, quantum up to 2√2, no-signalling beyond) and a −cos θ correlation curve crossing the classical bound
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: correlation, entanglement, spin measurement along an axis
- Exclusions: no full CHSH algebraic derivation, no loophole taxonomy, no interpretation debate, no Tsirelson-bound proof
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-chsh-ceiling/vox-chsh-ceiling-review.mp4`

## Candidate 10 — Why One Photon Can Become Two Identical Twins
- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`
- Production mode: Manim visualization
- Hook: A passing photon can tickle an excited atom into emitting a second photon that's a perfect copy — same direction, same phase. Do that in a chain and you get a laser.
- Core idea: Stimulated emission produces a photon coherent with the one that triggered it; with a population inversion (more atoms up than down) each photon spawns copies faster than they're absorbed, and the light avalanches.
- Visual object: One photon entering an excited atom and leaving as two identical photons, cascading into a coherent beam
- Manim move: duplicate
- Short-form fit: Medium
- Prerequisites: atomic energy levels, photon emission/absorption, energy E = hν
- Exclusions: no Einstein A/B coefficient derivation, no cavity/optics engineering, no four-level pumping schematics
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-stimulated-laser/vox-stimulated-laser-review.mp4`

## Candidate 11 — Why a Hot Box Doesn't Hold Infinite Energy
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Production mode: Manim visualization
- Hook: Classical physics predicts a warm oven glows with infinite energy at short wavelengths. It doesn't — and fixing that broke physics open.
- Core idea: Giving every wave mode an equal share of energy makes the curve climb forever (the ultraviolet catastrophe); forcing energy to come in discrete packets hν starves the high-frequency modes and bends the curve back down to the measured peak.
- Visual object: The rising-to-infinity Rayleigh–Jeans curve overlaid with the capped Planck curve that peaks and falls
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: wavelength/frequency, energy, the idea of counting modes
- Exclusions: no geometric-series average-energy derivation, no mode-counting integral, no historical Planck-vs-Einstein quantization subtlety beyond one line
- Score: 8/10

## Candidate 12 — Why a Quantum Particle Spreads Out Over Time
- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Production mode: Manim visualization
- Hook: A baseball thrown straight keeps its shape. A quantum particle released as a tidy packet inevitably smears wider and wider.
- Core idea: A localized packet is a bundle of momenta, and because energy goes as k² each momentum travels at a different speed, so the fast and slow components pull the packet apart — dispersion with no classical analog.
- Visual object: A Gaussian wave packet moving and visibly broadening, its component waves fanning out at different speeds
- Manim move: spread
- Short-form fit: Medium
- Prerequisites: wave packet, superposition of momenta, phase velocity
- Exclusions: no Fourier-transform algebra, no explicit σ(t) formula, no uncertainty-relation derivation
- Score: 8/10

## Candidate 13 — Why the Energy Ladder Climbs in Equal Steps
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Production mode: Manim visualization
- Hook: One clever operator lets you climb a quantum system's energy levels like rungs — and the same trick later builds and destroys particles in quantum field theory.
- Core idea: The raising and lowering operators shift a harmonic oscillator's state up or down by exactly ℏω; the ladder must have a bottom rung (energy can't go negative), and that lowest rung sits at ℏω/2, not zero.
- Visual object: An energy ladder with a token hopping up/down one rung at a time, stopped by a floor at ℏω/2
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: energy levels, harmonic oscillator, operators acting on states
- Exclusions: no commutator algebra [a₋,a₊]=1, no Hermite-polynomial route, no second-quantization detour beyond a closing nod
- Score: 8/10

## Candidate 14 — Why Your Hand Doesn't Fall Through the Table
- Source: `quantum-mechanics-a-companion-guide/chapters/08-identical-particles.md`
- Production mode: Doodle
- Hook: Solid matter is mostly empty space — so why can't you push your hand through a table?
- Core idea: The Pauli exclusion principle forbids two electrons from occupying the same state, so electrons must stack into higher and higher energy shells instead of all collapsing into the lowest one; that refusal to share is what gives atoms size and matter its solidity.
- Visual object: Electrons as characters forced to take separate "seats" up a stack of energy shells, vs a collapsed pile if sharing were allowed
- Manim move: split
- Short-form fit: Medium
- Prerequisites: electrons, energy shells/orbitals, the idea of a quantum state
- Exclusions: no antisymmetry/determinant proof, no periodic-table filling rules, no degeneracy-pressure astrophysics beyond a one-line tease
- Score: 8/10

## Candidate 15 — Why a Factor-of-Two in Energy Means 10²⁴ in Lifetime
- Source: `quantum-mechanics-a-companion-guide/chapters/04-one-dimensional-problems.md`
- Production mode: Mixed
- Hook: Two radioactive nuclei differ in decay energy by just a factor of two — yet one lives microseconds and the other outlives the Earth by a billion times.
- Core idea: Alpha particles escape by tunneling through a Coulomb barrier, and the escape probability sits inside an exponential; feed a modest change in energy into that exponent and half-lives fan out across 24 orders of magnitude (the Geiger–Nuttall line).
- Visual object: An alpha particle tunneling through a Coulomb hill, with a half-life-vs-energy plot whose points explode across a huge vertical range
- Manim move: decay
- Short-form fit: Medium
- Prerequisites: tunneling (see Candidate 05), exponential scaling, radioactive half-life
- Exclusions: no Gamow-factor integral, no WKB derivation, no closed-form arccos barrier calculation
- Score: 7/10

## Candidate 16 — Why One Sign Splits the Universe in Two
- Source: `quantum-mechanics-a-companion-guide/chapters/08-identical-particles.md`
- Production mode: Manim visualization
- Hook: The Fermi–Dirac and Bose–Einstein laws differ by a single ± sign in the denominator — and that one sign decides whether particles pile together or refuse to.
- Core idea: A +1 (fermions) caps each state at one occupant, so at low temperature they stack up to a sharp Fermi step; a −1 (bosons) lets a state hold unlimited occupants, so they cascade into the ground state and condense.
- Visual object: Two occupation curves sharing an axis — a sharp fermion step vs a diverging boson pile-up — driven by flipping one sign
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: energy states, temperature, occupation number, fermions vs bosons
- Exclusions: no derivation of the distributions, no chemical-potential subtleties, no BEC/white-dwarf case studies beyond a closing image
- Score: 7/10

## Candidate 17 — Why Quantum Mechanics Can't Be Written Without i
- Source: `quantum-mechanics-a-companion-guide/chapters/02-mathematical-foundations.md`
- Production mode: Mixed
- Hook: You can't get the dark bands of a two-slit pattern with ordinary real numbers — the experiment forces imaginary ones on you.
- Core idea: Getting alternating bright and dark fringes needs contributions that smoothly cancel and revive, which requires a continuously turning phase e^{iφ}; add the two slit amplitudes as complex arrows and the interference falls out, add them as real numbers and the dark bands vanish.
- Visual object: Two rotating phasor arrows from the two slits adding tip-to-tail, canceling and reinforcing as the screen angle sweeps
- Manim move: rotate
- Short-form fit: Medium
- Prerequisites: two-slit interference, adding amplitudes then squaring, basic idea of a phase
- Exclusions: no Euler-formula proof, no Hilbert-space formalism, no Renou real-QM experiment beyond a one-line "this was actually tested"
- Score: 7/10

## Candidate 18 — Why Entangled Spins Always Disagree, on Every Axis
- Source: `quantum-mechanics-a-companion-guide/chapters/07-angular-momentum.md`
- Production mode: Manim visualization
- Hook: Two particles in a singlet have no spin of their own — yet measure them along any direction you like and they always come out opposite.
- Core idea: The singlet (↑↓−↓↑)/√2 is rotationally invariant, so it looks identical in every measurement basis; that's why the perfect anti-correlation holds not just along z but along x, y, or any axis — the seed of the Bell argument.
- Visual object: A joined two-spin state that keeps its form as the measurement axis rotates, two dials always landing opposite
- Manim move: rotate
- Short-form fit: Medium
- Prerequisites: spin-½ up/down, superposition, measurement collapse
- Exclusions: no Clebsch–Gordan/ladder construction, no triplet comparison algebra, no CHSH derivation (that's Candidate 09)
- Score: 7/10

## Candidate 19 — Why Solids Have Forbidden Energy Gaps
- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`
- Production mode: Manim visualization
- Hook: In a crystal, electrons are allowed some energies and flatly forbidden others — and that gap is the whole difference between a metal, an insulator, and the chip in your phone.
- Core idea: Solving the Schrödinger equation in a repeating potential gives a condition where one side is trapped between ±1; wherever the other side overshoots that range, no real electron wave exists — those windows are the band gaps, with no extra assumption.
- Visual object: A bounded cos(ka) band on the y-axis and an oscillating curve sweeping through it, shading in the "no solution" gaps where it exceeds ±1
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: periodic potential, electron as a wave, allowed vs forbidden energy
- Exclusions: no Bloch-theorem proof, no Kronig–Penney boundary matching, no doping/transistor engineering beyond a closing line
- Score: 7/10

## Candidate 20 — Why the Electron Can't Be a Tiny Spinning Ball
- Source: `quantum-mechanics-a-companion-guide/chapters/06-the-hydrogen-atom.md`
- Production mode: Doodle
- Hook: If the electron's spin were an actual spinning sphere, its surface would have to move about 170 times faster than light.
- Core idea: Set a classical ball's rotational angular momentum equal to the electron's ℏ/2 and its known size, and the required equatorial speed blows past c; spin is real angular momentum, but it's intrinsic — a built-in property, not motion through space.
- Visual object: A cartoon electron-sphere spinning faster and faster, its rim speed-gauge smashing through a "c" redline
- Manim move: rotate
- Short-form fit: Medium
- Prerequisites: angular momentum of a spinning object, speed of light as a limit, electron spin exists
- Exclusions: no Dirac-equation origin of spin, no moment-of-inertia derivation on screen, no g-factor discussion
- Score: 7/10

## Candidate 21 — Why Energy Levels Repel Each Other
- Source: `quantum-mechanics-a-companion-guide/chapters/09-approximation-methods.md`
- Production mode: Manim visualization
- Hook: Nudge a quantum system and its energy levels shove apart — the closer two levels start, the harder they push, and they never cross.
- Core idea: A perturbation lowers the ground state and raises neighbors through the second-order shift, whose size grows as the gap between levels shrinks; the result is "avoided crossings" that shape band structure, molecules, and nuclei.
- Visual object: Two energy lines approaching as a knob turns, then bending away from each other instead of crossing
- Manim move: split
- Short-form fit: Weak
- Prerequisites: energy levels, a small perturbation, the idea of level spacing
- Exclusions: no second-order sum-over-states formula, no degenerate-perturbation matrix diagonalization, no specific Stark/Zeeman worked case
- Score: 6/10

slate cut 

## Candidate 22 — Why the i in Schrödinger's Equation Changes Everything
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-schrodinger-i/vox-schrodinger-i-review.mp4`
- Source: `quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md`
- Topic: QUANTUM MECHANICS
- Hook: Remove one letter from Schrödinger's equation and the quantum world stops being a wave and becomes a spreading stain.
- Key case: A localized electron wave packet is released in free space. Without the i the packet dissolves irreversibly into an ever-wider smear that never returns. With the i it travels and breathes without collapsing.
- The Question: Two equations differ by a single factor of i. One describes a wave, one describes heat flowing away forever. A quantum amplitude should predict where an electron is found next week. The diffusion version cannot do that. Why does one imaginary unit decide whether quantum mechanics is possible at all?
- Core idea: The factor i rotates time-derivative and space-derivative contributions into the complex plane so they interfere constructively as a traveling wave rather than adding their magnitudes monotonically as diffusion does — it is the algebraic switch between "spread irreversibly" and "propagate coherently."
- Visual object: Two initially identical Gaussian packets side by side — one under the real (diffusion) equation that flattens and never bounces back, one under the full Schrödinger equation that travels intact
- Manim move: compare
- Example seed: An electron in a 1 nm pocket is released. Under the diffusion equation its probability cloud hits 10 nm width in 3 femtoseconds and never contracts. Under the Schrödinger equation the same pocket produces a coherent pulse that crosses a 5 nm gap and arrives intact at a detector.
- Length band: 2–3 min
- Still lanes: geo (two side-by-side packet evolution traces)
- Prerequisites: wave packet, probability density, the idea that the Schrödinger equation governs evolution
- Exclusions: no plausibility-argument derivation of the full equation, no Hamiltonian formalism, no i in complex numbers from scratch, no interpretation of what ψ "is"
- Score: 10/10

slate cut 

## Candidate 23 — Why Bright Red Light Ejects No Electrons
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-photoelectric-threshold/vox-photoelectric-threshold-review.mp4`
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Topic: QUANTUM MECHANICS
- Hook: Turn up the power of a red laser shining on copper and not one electron ever leaves — but a single dim violet photon sends electrons flying.
- Key case: Robert Millikan in 1914 doubles the intensity of red light on sodium. The ammeter reads zero. He switches to dim ultraviolet. Electrons eject immediately, each with exactly the same kinetic energy as if the intensity hadn't changed.
- The Question: A brighter wave delivers more energy per second. Classical theory says electrons should accumulate that energy and escape eventually — more power means more electrons and more energy each. Here is sodium under intense red light with zero electrons and a dim UV beam with electrons at a fixed energy. Why?
- Core idea: Light arrives in indivisible packets of energy hν — one photon, one electron; the photon either has enough energy to exceed the binding threshold or it doesn't, no matter how many photons per second arrive; intensity controls the rate of attempts, frequency controls whether each attempt succeeds.
- Visual object: A threshold bar on a frequency axis — photons below the bar bounce off, photons above launch electrons with leftover energy equal to hν minus the bar height
- Manim move: scan
- Example seed: A sodium surface (work function 2.36 eV) is lit by 620 nm red light (photon energy 2.0 eV) at 10 mW — zero electrons. Switch to 400 nm violet (3.1 eV) at 0.1 mW — electrons eject at 0.74 eV each, 100 times fewer per second but every one successful.
- Length band: 2–3 min
- Still lanes: geo (frequency axis with threshold bar and photon-energy arrows)
- Prerequisites: light as waves carrying energy, electrons bound in a metal, energy in eV
- Exclusions: no work-function measurement lab, no stopping-potential circuit, no Millikan's full experimental setup, no Einstein 1905 paper history beyond one sentence
- Score: 9/10

slate cut 

## Candidate 24 — Why Quantum Mechanics Needs ℓ(ℓ+1), Not ℓ²
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-angular-momentum-ell/vox-angular-momentum-ell-review.mp4`
- Source: `quantum-mechanics-a-companion-guide/chapters/07-angular-momentum.md`
- Topic: QUANTUM MECHANICS
- Hook: If the components of angular momentum commuted like ordinary numbers, the eigenvalue formula would be ℓ²ℏ². They don't commute — and that one fact forces the +1 that students memorize without understanding.
- Key case: A student sets up the algebra expecting that the maximum m-value squared equals the total L² eigenvalue, writes λ = ℓ²ℏ², and gets predictions that conflict with spectroscopy everywhere.
- The Question: Angular momentum squared should equal its maximum z-component squared. Every formula for L² says ℓ(ℓ+1)ℏ², not ℓ²ℏ². The +1 cannot be removed. Why does L² give more than the square of L_z?
- Core idea: Expanding L₋L₊ with the commutation relation [L_x, L_y] = iℏL_z produces a cross-term −ℏL_z; this extra term shifts the eigenvalue from ℓ²ℏ² to ℓ(ℓ+1)ℏ², so the +1 is literally the non-commutativity of the components showing up in the eigenvalue.
- Visual object: A ladder of m-values climbing from −ℓ to +ℓ with a gap above the top rung that measures the +1 contribution from the cross-term
- Manim move: accumulate
- Example seed: For ℓ = 2 (a d-orbital), a student expects L² = 4ℏ². The actual measurement gives L² = 6ℏ² (i.e., 2×3). The extra 2ℏ² comes directly from the single commutator cross-term — show it appearing when L₋L₊ is expanded.
- Length band: 2–3 min
- Still lanes: geo (ladder diagram with explicit +1 gap annotation)
- Prerequisites: angular momentum components, commutator, eigenvalue ladder, the idea of a top rung
- Exclusions: no Lie-algebra representation theory, no Clebsch-Gordan addition, no derivation of spherical harmonics, no half-integer spin — orbital only
- Score: 9/10

slate cut 

## Candidate 25 — Why Moving a Tip 1 Å Closer Changes Tunneling Current by 7
- Source: `quantum-mechanics-a-companion-guide/chapters/10-quantum-mechanics-in-the-modern-world.md`
- Topic: QUANTUM MECHANICS
- Hook: A scanning tunneling microscope maps individual atoms by measuring a current that changes by a factor of seven every time the tip moves one ten-billionth of a meter closer.
- Key case: Heinrich Rohrer and Gerd Binnig at IBM Zurich in 1981 hold a sharp metal tip 5 Å above a silicon surface. They lower it 1 Å. The current jumps by a factor of roughly 7 — more than enough to resolve a single atom bump.
- The Question: Moving a tip closer to a surface should gradually increase the current — a smooth, roughly linear increase. Here the current multiplies by 7 for every 1 Å step. Why does a change smaller than an atom's diameter produce such a dramatic response?
- Core idea: Electrons reach the surface by tunneling through vacuum; the tunneling probability falls as e^(−2κd) where d is the gap and κ ≈ 1 Å⁻¹ for typical metals, so each ångström of retraction multiplies the probability by e^2 ≈ 7.4 — the exponential, not the distance, is doing the work.
- Visual object: A tip above a surface with the exponentially decaying wave function tail spanning the gap, and a current-vs-distance plot whose slope on a log scale is a constant −2κ line
- Manim move: decay
- Example seed: With work function φ = 4 eV, κ = 1.02 Å⁻¹. Gap d = 5 Å gives current I₀. Gap d = 6 Å gives I₀/7.4. Gap d = 4 Å gives 7.4·I₀. One atom protruding 1 Å above its neighbors carries 7× more current than the rest — the microscope is reading a single atom.
- Length band: 2–3 min
- Still lanes: geo (decay curve and log-current vs distance plot), c2v (stylized tip-surface cross-section)
- Prerequisites: tunneling (wave function leaking through a barrier), exponential decay, electric current
- Exclusions: no κ derivation from WKB, no STM feedback electronics, no surface reconstruction physics, no scanning-mode details
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-a-companion-guide/youtube/vox-stm-exponential/vox-stm-exponential-review.mp4`

## Candidate 26 — Why X-Rays Come Back Longer After Scattering
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Topic: QUANTUM MECHANICS
- Hook: Shine an X-ray on graphite and the scattered X-ray comes back at a longer wavelength — classical physics says it should come back at the same wavelength, always.
- Key case: Arthur Compton in 1923 fires molybdenum Kα X-rays at a graphite target and measures the scattered beam at 90°. It arrives 2.4 picometers longer than it left — a tiny but perfectly reproducible shift that classical wave theory cannot produce.
- The Question: A wave hitting an electron should set the electron oscillating at the incoming frequency, which then re-radiates at that same frequency. Classical Thomson scattering predicts zero wavelength shift. Compton sees a shift that grows with scattering angle. Why does the scattered X-ray return longer?
- Core idea: A photon carries momentum h/λ; treating the collision as a billiard-ball exchange of energy and momentum between the photon and a nearly free electron, the electron recoils and the photon loses energy, which means it loses frequency and gains wavelength by the amount Δλ = (h/m_e c)(1 − cos θ).
- Visual object: A before-and-after collision: incoming photon arrow and stationary electron, then deflected photon arrow (longer) and recoiling electron arrow, with the angle θ between old and new photon paths labeled
- Manim move: split
- Example seed: At θ = 90° the shift is exactly h/m_e c = 2.43 pm regardless of which element the target is made of. At θ = 180° (head-on bounce) the shift doubles to 4.86 pm. Compton measured 2.23 pm at 90° — within 10% of theory and independent of target material, ruling out any effect of the binding energy.
- Length band: 2–3 min
- Still lanes: geo (collision diagram with before/after momentum arrows and angle label)
- Prerequisites: photons carry energy E = hν, wavelength and frequency, conservation of energy and momentum
- Exclusions: no derivation of the Compton shift formula, no relativistic energy-momentum relation derivation, no Thomson-scattering classical calculation, no Compton's Nobel Prize history
- Score: 8/10

slate cut 

## Candidate 27 — Why Any Guess at the Quantum Ground State Is Too High
- Source: `quantum-mechanics-a-companion-guide/chapters/09-approximation-methods.md`
- Topic: QUANTUM MECHANICS
- Hook: Guess the ground-state energy of any quantum system — any guess at all — and you are guaranteed to be at or above the truth. Wrong but always wrong in the same direction.
- Key case: Egil Hylleraas in 1929 picks a product of two hydrogen-like wave functions with one free parameter — a wrong shape for helium — and minimizes the energy over that parameter. He gets −77.5 eV. The measured value is −79.0 eV. His answer is too high by 2%, exactly as the theorem requires.
- The Question: Helium has no exact closed-form solution. Hylleraas picks an incorrect shape, minimizes one number, and produces an energy that is within 2% of experiment — and the theorem guarantees he cannot overshoot. Why is the energy from a wrong wave function always at or above the true ground-state energy, never below?
- Core idea: Expand any trial state in the exact eigenbasis; the expectation value of the Hamiltonian is a weighted average of the exact eigenvalues with the ground state at the bottom, so the average is always at least as large as the minimum — the variational principle is just the statement that averages exceed their minimum.
- Visual object: An energy axis with the true ground state at the bottom and a sequence of trial-state energies stacked above it, each one sliding down as the trial is improved but never crossing the floor
- Manim move: collapse
- Example seed: For helium, trial effective charge Z* = 2.0 (ignore shielding) gives −74.8 eV. Z* = 1.69 (optimize) gives −77.5 eV. Experiment: −79.0 eV. Both estimates are above the true value; the optimized one is closer but still above, as the theorem requires.
- Length band: 2–3 min
- Still lanes: geo (energy axis with floor and descending trial-energy markers)
- Prerequisites: expectation value, ground state, the idea that any state can be expanded in an energy eigenbasis
- Exclusions: no Cauchy–Schwarz proof steps, no Hartree-Fock machinery, no density-functional theory, no second trial-state parameterization
- Score: 8/10

slate cut 

## Candidate 28 — Why Electrons Can Only Lose Exactly 4.9 eV in Mercury Gas
- Source: `quantum-mechanics-a-companion-guide/chapters/01-why-quantum-mechanics.md`
- Topic: QUANTUM MECHANICS
- Hook: Fire electrons through mercury vapor. The collector current climbs, then drops sharply at 4.9 V, climbs again, drops at 9.8 V, again at 14.7 V — the same gap, over and over, with clockwork precision.
- Key case: James Franck and Gustav Hertz in 1914 watch the electron current drop to near zero every time the accelerating voltage crosses a multiple of 4.9 V. Between those multiples the electrons pass through mercury atoms without losing energy — below the threshold, elastic collisions only.
- The Question: Electrons bouncing off atoms should be able to hand over any fraction of their energy in a soft collision — a slow electron should trickle energy into the atom gradually. Yet a mercury atom takes exactly 4.9 eV or nothing. Why can't an atom absorb less than its fixed quantum of energy?
- Core idea: Mercury atoms have discrete internal energy levels; the first excited level sits exactly 4.9 eV above the ground state, so a collision either has enough energy to raise the atom to that level and does, or the atom stays in the ground state and the electron bounces away with all its energy intact — there is no intermediate option.
- Visual object: Mercury atom energy-level diagram with the 4.9 eV gap, and a current-vs-voltage plot showing periodic dips spaced exactly 4.9 V apart
- Manim move: scan
- Example seed: Electrons accelerated to 7.0 eV pass through mercury vapor. Each electron can trigger exactly one 4.9 eV excitation and arrive at the collector with 2.1 eV to spare. At 9.9 eV each can trigger two successive excitations (9.8 eV) and arrive with 0.1 eV — current drops again at 9.8 V.
- Length band: 2–3 min
- Still lanes: geo (energy level diagram with gap annotation, current-voltage plot)
- Prerequisites: electron kinetic energy in eV, atomic energy levels, the idea of elastic vs inelastic collision
- Exclusions: no spectroscopy of mercury emission lines, no quantum-number assignment for the excited state, no historical context of the experiment vs Bohr model, no detailed apparatus schematic
- Score: 8/10

slate cut 

## Candidate 29 — Why Bohr's Wrong Orbits Got the Right Energies
- Source: `quantum-mechanics-a-companion-guide/chapters/06-the-hydrogen-atom.md`
- Topic: QUANTUM MECHANICS
- Hook: Bohr's electron traces a definite circular orbit at a fixed radius — a picture quantum mechanics says is completely wrong. Yet his energy formula for hydrogen is exactly correct. How does a wrong model give the right numbers?
- Key case: Apply Bohr's circular-orbit quantization condition to helium (one more electron, one more Coulomb term). The prediction misses the measured ionization energy by about 30%. The method that was perfect for hydrogen fails completely for the second atom.
- The Question: Bohr's model predicts hydrogen's energies to all measured decimal places and fails for helium by 30%. The real hydrogen atom has no orbit, no definite radius, and no classical trajectory. Why does a model that is wrong about every physical property of the electron produce the exact correct energy?
- Core idea: The 1/r Coulomb potential has a hidden SO(4) symmetry — beyond ordinary rotational symmetry — that forces all states with the same principal quantum number n to be degenerate regardless of angular momentum; Bohr's rule stumbled onto a consequence of that symmetry without knowing it existed, and the symmetry is unique to 1/r, which is why the accident only works for hydrogen.
- Visual object: Two side-by-side energy diagrams — Bohr's circular orbit with levels labeled by n only, and the quantum atom with the same energy levels but each showing multiple degenerate ℓ sub-levels — both reading the same total energy
- Manim move: compare
- Example seed: Hydrogen n = 2 has four states: 2s (ℓ=0) and three 2p (ℓ=1). All four sit at −3.4 eV. Bohr predicts −3.4 eV for n = 2 from one classical circular orbit. Quantum mechanics recovers the same number from four distinct wave functions that look nothing like an orbit — the SO(4) symmetry links them all.
- Length band: 3–5 min
- Still lanes: geo (two-column energy diagram comparing Bohr and quantum-mechanical degeneracy structure)
- Prerequisites: hydrogen energy levels (E_n = −13.6/n² eV), quantum numbers n and ℓ, the idea of degeneracy
- Exclusions: no SO(4) group theory, no Laplace-Runge-Lenz vector derivation, no Pauli algebraic solution, no helium Schrödinger equation beyond the one-sentence contrast
- Score: 7/10
