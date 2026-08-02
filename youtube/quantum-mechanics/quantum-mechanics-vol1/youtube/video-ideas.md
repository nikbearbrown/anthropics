# Bear's Doodles — Quantum Mechanics Vol. 1 Video Ideas

## Candidate 01 — Why the Wave Crests Move Twice as Fast as the Packet
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Production mode: Manim visualization
- Hook: Watch a quantum wave packet travel, and the ripples inside it race forward at twice the speed of the blob they're inside — crests keep being born at the back and dying at the front.
- Core idea: The individual crests move at the phase velocity (p/2m) while the envelope — the actual particle — moves at the group velocity (p/m), so the wiggles slide through the packet from behind and vanish at the leading edge.
- Visual object: A traveling Gaussian envelope with internal crests visibly overtaking it and passing through
- Manim move: trace
- Short-form fit: Strong
- Prerequisites: wave, wavelength, a moving pulse, the idea of a superposition
- Exclusions: no Taylor expansion of ω(k), no Fourier-integral derivation, no dispersion-spreading math (that's Candidate 12)
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-wave-crests/vox-wave-crests-review.mp4`

## Candidate 02 — Why a Particle in a Box Cannot Sit Still
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Production mode: Manim visualization
- Hook: A classical marble in a box can rest on the floor with zero energy. The quantum particle in the same box can't — its lowest energy is stubbornly above zero.
- Core idea: The wavefunction must vanish at both walls, so the least it can do is a single standing half-wave; that curvature is momentum, and momentum is kinetic energy, so the ground state floor is E₁ = π²ℏ²/2mL² > 0.
- Visual object: A standing half-wave fitted between two hard walls, its curvature highlighted
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: standing wave, boundary condition, kinetic energy
- Exclusions: no eight-step boundary-value derivation, no normalization constant, no n² spectrum table
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-box-ground-state/vox-box-ground-state-review.mp4`

## Candidate 03 — Why a Particle Can Walk Through a Wall
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Production mode: Manim visualization
- Hook: A classical ball thrown at a wall it can't climb bounces back every time. A quantum particle sometimes just appears on the far side — with no energy borrowed and none repaid.
- Core idea: Inside a barrier the wavefunction doesn't stop, it decays exponentially; if the barrier is thin enough, a small amplitude survives to the other side and launches a transmitted wave, with T falling off like e^(−2κL).
- Visual object: A wave striking a barrier, decaying to a thin surviving tail that emerges on the far side and grows as the barrier thins
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: wavefunction, classically forbidden region, exponential decay
- Exclusions: no sinh² exact formula, no four-region matching algebra, no "borrowed energy" framing except to debunk it in one line
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-quantum-tunneling/vox-quantum-tunneling-review.mp4`

## Candidate 04 — Why One Electron Builds an Interference Pattern by Itself
- Source: `quantum-mechanics-vol1/chapters/02-matter-waves.md`
- Production mode: Manim visualization
- Hook: Send electrons through a double slit one at a time — never two in the machine at once — and a wave-interference pattern still assembles itself, dot by dot.
- Core idea: Each electron lands as a single localized dot, but its wave function passes through both slits and interferes with itself; the accumulated dots trace out |ψ|² — matter has a wavelength λ = h/p.
- Visual object: A detector screen filling with single dots that resolve into bright and dark fringes
- Manim move: accumulate
- Short-form fit: Strong
- Prerequisites: wave interference, de Broglie wavelength, probability
- Exclusions: no Bragg/Davisson–Germer angle calculation, no which-path/decoherence tangent, no biprism optics
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-double-slit-self/vox-double-slit-self-review.mp4`

## Candidate 05 — Why a "Stationary" State Is Secretly Spinning
- Source: `quantum-mechanics-vol1/chapters/04-the-schrodinger-equation.md`
- Production mode: Manim visualization
- Hook: A stationary state is called stationary because nothing you can measure about it changes — yet the wave function underneath is spinning the whole time.
- Core idea: An energy eigenstate carries a phase e^(−iEt/ℏ) that rotates in the complex plane; the magnitude |ψ|² is the shadow it casts and the shadow holds still, so the state is a spinning clock whose shadow on the floor never moves.
- Visual object: A clock hand rotating in the complex plane beside its flat, unmoving shadow (|ψ|²)
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: wavefunction, phase, probability density, energy eigenstate
- Exclusions: no separation-of-variables derivation, no superposition beat term (that's Candidate 10), no eigenvalue formalism
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-spinning-phase/vox-spinning-phase-review.mp4`

## Candidate 06 — Why the Wave Function Has to Be Complex
- Source: `quantum-mechanics-vol1/chapters/03-the-wave-function.md`
- Production mode: Manim visualization
- Hook: Take a wave packet moving right and one moving left — their probability clouds are identical. The thing that tells them apart is hiding in the imaginary part.
- Core idea: |ψ|² is the same for both directions, so the direction of motion lives entirely in the phase — the relationship between the real and imaginary parts; strip out the imaginary part and a moving particle can't be represented at all.
- Visual object: Two identical |ψ|² humps whose hidden Re/Im parts wind in opposite directions, revealing left vs right travel
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: probability density, phase, a wave that moves
- Exclusions: no Schrödinger-equation consistency proof, no momentum-operator Fourier argument, no continuity equation
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-complex-wavefunction/vox-complex-wavefunction-review.mp4`

## Candidate 07 — Why a Particle Bounces Off a Cliff It Could Easily Clear
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Production mode: Manim visualization
- Hook: Roll a ball off a downhill step and it always keeps going. Send a quantum particle at a step it has more than enough energy to clear, and part of it reflects anyway.
- Core idea: What causes reflection is not whether the particle has the energy but how abruptly its wavelength changes at the boundary; any sudden change in k reflects part of the wave, exactly like an impedance mismatch on a transmission line — even a step downward.
- Visual object: An incoming wave hitting a step where the wavelength abruptly changes, splitting into a transmitted and a reflected wave
- Manim move: split
- Short-form fit: Medium
- Prerequisites: wave, wavelength, reflection, kinetic energy vs potential
- Exclusions: no probability-current bookkeeping, no R/T amplitude algebra, no evanescent-case detour
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-step-reflection/vox-step-reflection-review.mp4`

## Candidate 08 — Why a Barrier Can Suddenly Turn Invisible
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Production mode: Manim visualization
- Hook: Tune a particle's energy just right and a solid barrier becomes perfectly transparent — the particle sails through as if it weren't there.
- Core idea: When the barrier width is exactly a whole number of half-wavelengths of the wave inside it, the internal reflections cancel by interference and transmission jumps to 100% — a resonance, the same trick as an anti-reflection coating on a lens.
- Visual object: A wave inside a barrier whose width is swept until it fits an integer of half-wavelengths and the reflected wave vanishes
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: wave, wavelength, reflection and transmission, interference
- Exclusions: no full above-barrier transmission formula, no Fabry–Pérot phase algebra, no resonant-tunneling-diode engineering
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-ramsauer-resonance/vox-ramsauer-resonance-review.mp4`

## Candidate 09 — Why Measuring Sideways Erases What You Knew
- Source: `quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md`
- Production mode: Manim visualization
- Hook: Sort atoms so every one is spin-up. Measure their spin sideways, then measure up-down again — and half of your certain spin-ups are now spin-down.
- Core idea: A spin-up state is an equal superposition of spin-left and spin-right, so a sideways measurement collapses it and destroys the up-down information; because the operators don't commute, the second measurement can't preserve the first.
- Visual object: A beam of "up" arrows passing through three Stern–Gerlach magnets (Z→X→Z), splitting 50/50 at the final stage
- Manim move: split
- Short-form fit: Medium
- Prerequisites: spin up/down, superposition, measurement collapse
- Exclusions: no Pauli-matrix commutator algebra, no Bloch-sphere formalism, no Born-rule projection proof
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-stern-gerlach-erase/vox-stern-gerlach-erase-review.mp4`

## Candidate 10 — Why Two Frozen States Make a Sloshing One
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Production mode: Manim visualization
- Hook: Each energy state in a box sits perfectly still. Add two of them together and suddenly the probability sloshes wall to wall — a hundred times faster than a heartbeat.
- Core idea: Two eigenstates rotate at different phase rates, so the angle between them grows and their interference term beats at the Bohr frequency (E₂−E₁)/ℏ; the average position swings back and forth while the total energy stays fixed.
- Visual object: Two still probability humps combining into one cloud that rocks left-to-right at the beat frequency
- Manim move: slosh
- Short-form fit: Medium
- Prerequisites: energy eigenstate, superposition, phase, probability density
- Exclusions: no ⟨x⟩(t) cross-integral, no product-to-sum trig, no femtosecond numerics
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-superposition-slosh/vox-superposition-slosh-review.mp4`

## Candidate 11 — Why a Warm Box Doesn't Glow With Infinite Energy
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Production mode: Manim visualization
- Hook: Classical physics says a hot oven should blast you with infinite ultraviolet light. Open one and it plainly doesn't — and fixing that started quantum mechanics.
- Core idea: Giving every wave mode an equal share of energy makes the predicted curve climb forever (the ultraviolet catastrophe); forcing energy into discrete packets hν starves the high-frequency modes and bends the curve back down to the measured hump.
- Visual object: The rising-to-infinity Rayleigh–Jeans curve overlaid with the Planck curve that peaks and falls
- Manim move: compare
- Short-form fit: Medium
- Prerequisites: wavelength/frequency, energy, the idea of counting wave modes
- Exclusions: no geometric-series average-energy derivation, no Wien's-law algebra, no photoelectric detour
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-ultraviolet-catastrophe/vox-ultraviolet-catastrophe-review.mp4`

## Candidate 12 — Why a Quantum Particle Spreads Out on Its Own
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Production mode: Manim visualization
- Hook: A baseball thrown in a straight line keeps its shape. A quantum particle released as a tidy packet inevitably smears wider — and the tighter you pin it, the faster it blurs.
- Core idea: A localized packet is a bundle of momenta, and because energy goes as k² the faster components outrun the slower ones, so the packet disperses; the doubling time scales as σ₀², so tighter confinement means faster spreading.
- Visual object: A Gaussian packet gliding forward while visibly broadening, its component waves fanning apart
- Manim move: spread
- Short-form fit: Medium
- Prerequisites: wave packet, superposition of momenta, the idea of different speeds
- Exclusions: no Gaussian-integral derivation, no chirp/complex-width algebra, no phase-vs-group recap (that's Candidate 01)
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-packet-spreading/vox-packet-spreading-review.mp4`

## Candidate 13 — Why the Energy Ladder Climbs in Equal Steps
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Production mode: Manim visualization
- Hook: One clever operator lets you climb a quantum system's energy levels like a ladder — and the exact same trick later creates and destroys particles in quantum field theory.
- Core idea: The raising and lowering operators shift the oscillator's state up or down by exactly ℏω; the ladder must have a bottom rung because energy can't go negative, and that lowest rung sits at ℏω/2, not zero.
- Visual object: An evenly spaced energy ladder with a token hopping rung to rung, blocked by a floor at ℏω/2
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: energy levels, harmonic oscillator, operators acting on a state
- Exclusions: no commutator derivation [a₋,a₊]=1, no Hermite-polynomial route, no field-theory formalism beyond a closing nod
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-energy-ladder/vox-energy-ladder-review.mp4`

## Candidate 14 — Why Uncertainty Isn't About Bumping the Particle
- Source: `quantum-mechanics-vol1/chapters/09-operators-and-uncertainty.md`
- Production mode: Manim visualization
- Hook: The famous story says you blur a particle's momentum by hitting it with a photon to see it. But you can measure position and momentum on separate copies that were never touched — and the limit is still there.
- Core idea: The Kennard/Robertson inequality is a property of the prepared state, coming from the non-commuting algebra of position and momentum; squeezing the position spread forces the momentum spread to widen, with no measurement and no kick involved.
- Visual object: Two coupled width-gauges for x and p; squeezing one visibly stretches the other, no photon ever entering
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: standard deviation/spread, position and momentum, wavefunction
- Exclusions: no Cauchy–Schwarz proof, no commutator algebra, no Ozawa measurement-disturbance relation beyond one contrast line
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-uncertainty-intrinsic/vox-uncertainty-intrinsic-review.mp4`

## Candidate 15 — Why an Electron Needs Two Full Turns to Come Back
- Source: `quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md`
- Production mode: Manim visualization
- Hook: Rotate an electron's state all the way around — 360° — and it comes back as the negative of itself. It only truly returns after 720°.
- Core idea: A qubit state carries the angle θ/2, so a full 2π turn of the Bloch vector flips the state's sign; that minus sign is invisible in expectation values but shows up in interference, and neutron interferometry has measured it.
- Visual object: A state arrow whose sign flag flips at 360° and resets only at 720°, beside a normal vector that resets at 360°
- Manim move: rotate
- Short-form fit: Medium
- Prerequisites: rotation, qubit/spin state, interference
- Exclusions: no SU(2)/SO(3) group theory, no Pauli-exponential derivation, no full interferometer optics
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-spinor-720/vox-spinor-720-review.mp4`

## Candidate 16 — Why You Don't Diffract Walking Through a Doorway
- Source: `quantum-mechanics-vol1/chapters/02-matter-waves.md`
- Production mode: Doodle
- Hook: Electrons diffract through crystals like waves — so why doesn't a person walking through a doorway spread into fringes?
- Core idea: Every object has a de Broglie wavelength λ = h/p, but for anything massive and everyday it's absurdly tiny — a walking human comes out around 10⁻³⁵ m, twenty-odd orders below a proton — so no slit in the universe could reveal the wave; quantum mechanics is exact for us, just invisibly so.
- Visual object: A shrinking wavelength scale bar sliding from an electron down to a human, past a "smallest possible slit" marker
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: de Broglie wavelength, momentum = mass × speed, diffraction needs comparable slit size
- Exclusions: no Davisson–Germer numbers, no correspondence-principle formalism, no relativistic momentum
- Score: 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-de-broglie-human/vox-de-broglie-human-review.mp4`

## Candidate 17 — Why Every Qubit Lives on a Globe
- Source: `quantum-mechanics-vol1/chapters/10-measurement-and-the-qubit.md`
- Production mode: Manim visualization
- Hook: Every possible state of a quantum bit — the raw material of a quantum computer — is a single point on the surface of one sphere.
- Core idea: A qubit's two complex amplitudes reduce, after normalization and dropping an unobservable global phase, to two angles; those angles place the state on the Bloch sphere, with the poles the definite 0 and 1 and the equator the equal superpositions.
- Visual object: The Bloch sphere with a state arrow sweeping from pole (|0⟩) through the equator (superpositions) to the other pole (|1⟩)
- Manim move: rotate
- Short-form fit: Medium
- Prerequisites: qubit as α|0⟩+β|1⟩, superposition, normalization
- Exclusions: no expectation-value derivation of the Bloch vector, no gate operations, no θ/2 double-cover subtlety (that's Candidate 15)
- Score: 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-bloch-sphere/vox-bloch-sphere-review.mp4`

## Candidate 18 — Why a Microscope Can Feel a Single Atom
- Source: `quantum-mechanics-vol1/chapters/06-finite-wells-steps-and-barriers.md`
- Production mode: Manim visualization
- Hook: A scanning tunneling microscope images individual atoms — and its secret is that moving the tip one atom's-width closer changes the current by a factor of ten.
- Core idea: Tunneling current falls off exponentially with gap distance (I ∝ e^(−2κd)), so a single ångström of extra gap cuts the current by roughly a factor of seven to ten; that exponential steepness means the current is dominated by the one closest atom on the tip.
- Visual object: An STM tip over a bumpy atomic surface with a current meter swinging wildly as the sub-ångström gap changes
- Manim move: decay
- Short-form fit: Medium
- Prerequisites: tunneling (see Candidate 03), exponential decay, electric current
- Exclusions: no work-function derivation of κ, no feedback-electronics detail, no barrier-matching algebra
- Score: 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-stm-tunneling/vox-stm-tunneling-review.mp4`

## Candidate 19 — Why One Quantum Packet Can Slosh Without Spreading
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Production mode: Manim visualization
- Hook: A free quantum particle always smears out as it moves. But drop one into a spring-like well and a special packet can swing back and forth forever, keeping its exact shape.
- Core idea: A coherent state is a Gaussian packet whose center oscillates at the classical frequency ω while its width stays locked at the minimum-uncertainty value; the restoring potential exactly cancels the dispersion that spreads a free packet, which is why ideal laser light behaves this way.
- Visual object: A compact Gaussian packet oscillating side to side in a parabolic bowl, never broadening, next to a free packet that smears
- Manim move: slosh
- Short-form fit: Medium
- Prerequisites: wave packet, harmonic-oscillator potential, packet spreading (Candidate 12)
- Exclusions: no coherent-state expansion in |n⟩, no Poisson photon statistics, no ladder-operator eigenvalue algebra
- Score: 7/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-coherent-state/vox-coherent-state-review.mp4`

slate cut 

## Candidate 20 — Why a Blinding Red Lamp Releases Fewer Electrons Than a Dim UV Torch
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Topic: QUANTUM MECHANICS
- Hook: A million-watt red spotlight aimed at sodium metal releases exactly zero electrons, while a pocket UV penlight releases them instantly.
- Key case: Millikan's sodium surface in vacuum under green light at 546 nm — photon energy 2.27 eV, work function 2.28 eV — no electrons, not one, from any lamp at any intensity.
- The Question: Classical wave theory predicts that enough intensity should always supply enough energy to free an electron. Here no intensity suffices below a frequency threshold. Why?
- Core idea: Light arrives as single photons each carrying exactly hν; a photon below the threshold simply cannot free one electron no matter how many photons land per second, because one photon acts alone and its energy is non-negotiable.
- Visual object: A threshold frequency line on a photon-energy axis; photons below it bounce off, photons above it each eject one electron
- Manim move: compare
- Example seed: A UV penlight at 300 nm (photon energy 4.13 eV) strikes a sodium surface (work function 2.28 eV); three electrons per second emerge each with 1.85 eV of kinetic energy. Switch to a green laser at 546 nm (photon energy 2.27 eV) cranked to 1 kW: zero electrons, forever.
- Length band: 2–3 min
- Still lanes: geo (threshold-line diagram), c2v (penlight and spotlight objects)
- Prerequisites: frequency, energy, the idea of a work function as an escape energy
- Exclusions: no stopping-potential voltage algebra, no Einstein-equation derivation, no Compton scattering, no history of Millikan's personal disbelief beyond a single spoken line
- Score: 9/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-photoelectric/vox-photoelectric-review.mp4`

slate cut 

## Candidate 21 — Why Liquid Helium Refuses to Freeze Even at Absolute Zero
- Source: `quantum-mechanics-vol1/chapters/07-the-harmonic-oscillator.md`
- Topic: QUANTUM MECHANICS
- Hook: Every other element solidifies when cooled enough — but helium stays liquid all the way down to absolute zero unless you squeeze it hard.
- Key case: Helium at 1 kelvin under atmospheric pressure: still sloshing as a liquid, while neon at the same temperature is a solid crystal.
- The Question: Cooling removes thermal energy; at 0 K there should be nothing left to keep atoms moving. Helium's atoms should settle into a lattice. They don't. Why?
- Core idea: Quantum zero-point motion — the irreducible kinetic energy ℏω/2 that confinement forces on any oscillator — gives helium atoms enough energy to escape their neighbors' gravitational grip; because helium is so light and its binding so weak, the zero-point energy exceeds the lattice binding energy at any pressure below ~25 atm.
- Visual object: Atoms in a would-be lattice site, jittering with zero-point amplitude larger than their nearest-neighbor spacing, unable to lock in place
- Manim move: slosh
- Example seed: A thought-experiment lattice of 12 helium atoms at 0 K: each confined to a 3 Å sphere by its neighbors, giving a zero-point kinetic energy of ~10 meV; the van der Waals binding per atom is only ~1 meV; the atoms cannot stay put.
- Length band: 2–3 min
- Still lanes: geo (lattice-site jitter diagram), c2v (liquid helium container object)
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-liquid-helium/vox-liquid-helium-review.mp4`
- Prerequisites: absolute zero, lattice/crystal structure, kinetic energy, the idea that quantum ground states carry nonzero energy
- Exclusions: no Casimir-force calculation, no superfluid transition physics, no harmonic-oscillator algebra, no helium-4 vs helium-3 isotope distinction
- Score: 9/10

slate cut 

## Candidate 22 — Why 48 Iron Atoms Make Quantum Ripples Nobody Placed There
- Source: `quantum-mechanics-vol1/chapters/05-the-infinite-square-well.md`
- Topic: QUANTUM MECHANICS
- Hook: IBM physicists placed 48 iron atoms in a ring on a copper surface and found concentric wave patterns inside the ring that nobody put there.
- Key case: The 1993 Crommie–Lutz–Eigler quantum corral: an STM image showing standing-wave rings of electron density inside the ring — not where the iron atoms are, but between them, filling the enclosed space.
- The Question: Classical electrons in a confined region should distribute smoothly. The image shows sharp rings at fixed radii. Where do the rings come from and why are they at those exact positions?
- Core idea: Confinement forces the electron wave function to vanish at the boundary; only wavelengths that fit the ring as standing waves survive; those surviving modes are discrete, and their squared amplitudes form the concentric rings — quantization derived purely from the boundary condition, not assumed.
- Visual object: A circular ring boundary with standing-wave modes fitting inside it, ring nodes appearing at fixed radii set by the circumference
- Manim move: accumulate
- Example seed: A circular corral of radius 7 nm: the ground-state de Broglie wavelength that fits is ~14 nm; the first excited mode fits a full wavelength, ~7 nm; the STM image shows exactly these two ring spacings as bright and dark bands.
- Length band: 2–3 min
- Still lanes: geo (standing-wave modes in a circle), raster (STM image of the actual corral as a single cold-open still)
- Prerequisites: standing wave, boundary condition, wavelength, the idea that only certain waves fit a bounded space
- Exclusions: no Schrödinger-equation derivation, no Bessel-function radial eigenstates, no STM tip-mechanics, no comparison to infinite square well energies
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-quantum-corral/vox-quantum-corral-review.mp4`

slate cut 

## Candidate 23 — Why X-Rays Change Color When They Bounce Off Electrons
- Source: `quantum-mechanics-vol1/chapters/01-why-classical-physics-failed.md`
- Topic: QUANTUM MECHANICS
- Hook: Shine X-rays at a target and the scattered X-rays come back longer — they lost energy to the electrons they hit, exactly as if the photon were a billiard ball.
- Key case: Compton's 1923 experiment: X-rays at 0.071 nm scattered from graphite at 90° emerge at 0.073 nm — 2.4 pm longer, matching the Compton wavelength of the electron to four significant figures; classical wave theory predicts zero shift.
- The Question: A wave scattering off electrons should come back at the same frequency — it wiggles the electron and the electron radiates at the same frequency. Here the frequency drops. Why?
- Core idea: The photon carries momentum p = h/λ; when it collides elastically with a nearly-free electron, relativistic energy-momentum conservation forces the photon to give up some energy to the recoiling electron, stretching its wavelength by Δλ = (h/mₑc)(1 − cosθ).
- Visual object: A photon-ball colliding with an electron-ball at angle θ, the photon emerging with a visibly longer wavelength arrow and the electron recoiling
- Manim move: compare
- Example seed: A photon at 0.071 nm (17.5 keV) hits a stationary electron. At θ = 90°, it transfers 0.24 keV to the electron and emerges at 0.073 nm — you can read the shift on a wavelength ruler.
- Length band: 2–3 min
- Still lanes: geo (collision diagram with momentum arrows), c2v (X-ray tube and graphite target object)
- Prerequisites: wavelength, frequency, momentum, elastic collision, the idea that light carries momentum
- Exclusions: no relativistic-kinematics algebra, no Thomson scattering cross-section, no photoelectric effect recap, no Compton wavelength derivation
- Score: 8/10
- Watch: `open /Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol1/youtube/vox-compton-scatter/vox-compton-scatter-review.mp4`

## Candidate 24 — Why Position and Momentum Cannot Commute — and Why That's Everything
- Source: `quantum-mechanics-vol1/chapters/09-operators-and-uncertainty.md`
- Topic: QUANTUM MECHANICS
- Hook: In classical mechanics, it doesn't matter whether you multiply x by p or p by x — you get the same number. In quantum mechanics you get a different answer, and that one-line difference is where all of uncertainty comes from.
- Key case: Acting with x̂ then p̂ on a wave function ψ versus p̂ then x̂: the first measures position then applies momentum, the second applies momentum then measures position; the product rule forces an extra term iℏψ that cannot be cancelled.
- The Question: Position and momentum are both real, measurable quantities — their product should commute just as ordinary numbers do. The calculation shows they don't, leaving a residual iℏ. Why does this remainder exist, and what does it cost?
- Core idea: Momentum in quantum mechanics is a derivative operator; differentiation obeys the product rule, which generates an extra term when position (multiplication by x) is applied before differentiation — that extra term is iℏ, and it is the algebraic root of every uncertainty relation.
- Visual object: Two arrows in the complex plane showing x̂p̂ψ and p̂x̂ψ pointing in different directions, their difference being a single residual arrow labeled iℏ
- Manim move: compare
- Example seed: Take ψ(x) = e^(−x²/2) (a Gaussian). Compute p̂(x̂ψ) = −iℏ∂ₓ(xe^(−x²/2)) = −iℏ(e^(−x²/2) − x²e^(−x²/2)); compute x̂(p̂ψ) = x·(−iℏ)(−x)e^(−x²/2) = iℏx²e^(−x²/2). Subtract: the residual is exactly −iℏe^(−x²/2) = −iℏψ. The iℏ appears from the product rule alone.
- Length band: 2–3 min
- Still lanes: geo (operator order diagram), geo (complex-plane residual arrow)
- Prerequisites: what an operator is, the product rule from calculus, the idea of a commutator
- Exclusions: no Robertson/Kennard proof, no Cauchy-Schwarz algebra, no measurement-disturbance confusion (that's Candidate 14), no Dirac bracket formalism
- Score: 8/10

slate cut 

## Candidate 25 — Why a Probability Density Can Be Greater Than One
- Source: `quantum-mechanics-vol1/chapters/03-the-wave-function.md`
- Topic: QUANTUM MECHANICS
- Hook: A quantum textbook shows |ψ|² = 2 at a point, and a student flags it as impossible — probabilities can't exceed one. The student is wrong, and the confusion costs them every calculation they make.
- Key case: The normalized wave function ψ(x) = (1/√a)e^(−|x|/a) for a = 0.5 nm has |ψ(0)|² = 2 nm⁻¹ at the origin — a number greater than one — yet the probability of finding the particle anywhere is exactly 1.
- The Question: Probabilities must lie between 0 and 1. The Born rule says |ψ|² gives the probability. Here |ψ|² equals 2 at a point. Contradiction?
- Core idea: |ψ(x)|² is a probability density — a probability per unit length — not a probability; to get a dimensionless probability between 0 and 1 you must integrate over an interval; a density of 2 nm⁻¹ over a 0.1 nm region is a probability of 0.2, which is perfectly valid.
- Visual object: A probability density bell curve with a y-axis labeled "per nm," a highlighted narrow strip whose area equals a small valid probability, and a comparison to a population density map where the number of people per km² can far exceed 1
- Manim move: accumulate
- Example seed: ψ(x) = (1/√a)e^(−|x|/a) with a = 0.5 nm; the peak density is 2 nm⁻¹; the probability of finding the particle within ±0.1 nm of the origin is ∫₋₀.₁^0.1 2e^(−2|x|/0.5) dx ≈ 0.33 — sensible, between 0 and 1.
- Length band: ~1 min
- Still lanes: geo (density-curve with strip area), c2v (city population density map analogy object)
- Prerequisites: the idea of a probability between 0 and 1, the concept of a density (e.g. grams per cubic centimeter), integration as area
- Exclusions: no normalization calculation, no Born-rule derivation, no momentum-space counterpart, no continuity-equation digression
- Score: 7/10

slate cut 

## Candidate 26 — Why a Quantum Packet Becomes Chirped as It Spreads
- Source: `quantum-mechanics-vol1/chapters/08-the-free-particle-and-wave-packets.md`
- Topic: QUANTUM MECHANICS
- Hook: After a quantum wave packet travels for a while, its front edge has a shorter wavelength than its back edge — the packet becomes a frequency gradient in space, even though it started uniform.
- Key case: A Gaussian electron packet released from a 2 nm quantum dot: after 70 fs its spatial width has doubled and its front half oscillates visibly faster than its rear half — the leading edge has higher local momentum than the trailing edge.
- The Question: The packet started with a uniform central momentum k₀ and a symmetric spread of momenta around it. After spreading, the high-momentum components should be at the front and low-momentum components at the rear. But the packet was supposed to keep its mean momentum everywhere. Why does it acquire a spatial momentum gradient?
- Core idea: Higher-k Fourier components travel faster (group velocity ∝ k); as time passes they outrun the lower-k components; the front of the packet is progressively enriched in high-k and the rear in low-k, so the local wavenumber varies continuously from back to front — this is chirp, the same phenomenon as a frequency-swept radar pulse.
- Visual object: A wave packet at two times; in the later panel, visible wavelength compression at the front and stretching at the rear, with a local-wavelength ruler overlaid
- Manim move: spread
- Example seed: An electron packet with k₀ = 5 nm⁻¹ and Δk = 1 nm⁻¹; after 100 fs the front (x = v_g t + 2σ) has local k ≈ 5.8 nm⁻¹ and the rear (x = v_g t − 2σ) has local k ≈ 4.2 nm⁻¹ — a 16% difference in local momentum visible in the wavelength.
- Length band: 2–3 min
- Still lanes: geo (two-time packet with wavelength ruler), geo (Fourier component speed diagram)
- Prerequisites: wave packet, Fourier components, group velocity, packet spreading (Candidate 12)
- Exclusions: no complex-width Gaussian algebra, no quadratic-phase derivation, no radar/sonar technology tangent, no chirped-pulse amplification
- Score: 7/10
