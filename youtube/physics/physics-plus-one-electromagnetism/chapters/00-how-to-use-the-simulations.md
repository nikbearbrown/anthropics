# Chapter 0 — How to Use the Simulations

*Get from zero to a working, modifiable electric-field simulation before you read any new physics.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Generate the three Brutalist governing files — `CLAUDE.md`, `DESIGN.md`, and `PROJECT.md` — and place them in your working directory.
2. **(Apply)** Write a four-move prompt (Show / Say / Constrain / Verify) and use it to ask an LLM to produce a working D3 simulation.
3. **(Analyze)** Verify a simulation against three checks: it opens, the physics is right at obvious limits, and the visualization conventions match `DESIGN.md`.
4. **(Apply)** Modify the point-charge simulation — flip the sign, double the magnitude, add a second charge — and predict what should happen before pressing play.

---

## Opening case: the simulation that runs in your browser at 11 PM

A student is stuck on her electromagnetism homework Wednesday night. Question 4 asks for the field at a point off-axis from two unequal charges. The textbook gives Coulomb's law and one worked example with charges on a line. She can compute the field magnitude algebraically. She can't *see* what the field is doing — whether the field lines bend more steeply near the larger charge, whether there's a point where they cancel exactly, what happens off the symmetry axis. Her professor is asleep. PhET has a simulation, but she can't modify the charges to her exact problem.

She opens a code editor and pastes a four-move prompt to Claude:

> **Show.** [Coulomb's law]. [The picture I want: two charges at chosen positions, vector arrows showing **E** at every point on a 20×20 grid.]
> **Say.** Render the electric field of two point charges as a 2D vector field in a single HTML file using D3 v7.
> **Constrain.** Sliders for q₁, q₂, and positions. Positive charges red, negative blue. Field arrows scaled by log(1+|E|). Length-of-arrow proportional to field strength.
> **Verify.** Field arrows should point away from positive charges and toward negative ones. Arrows should bunch near each charge.

Sixty seconds later she has 90 lines of HTML in her editor. She saves it, opens it in Chrome, and there is her homework problem. She drags one charge closer, watches the field rearrange, finds the null point by eye, and writes down its coordinates. Total elapsed time including writing the prompt: four minutes.

The chapter you are about to read teaches you to be that student. Not the prompt — the prompt is the easy part — but the *habit of mind* that turns Claude into a simulation tool you can trust. By the end of this chapter you will have generated the simulation above. By the end of the book you will have generated eleven more, each visualizing a different piece of electromagnetism.

---

## Core concept: the three files and the four moves

### The Brutalist three-file system

Three files live at the top of your working directory and travel with the project across the whole semester. They are not documentation. They are **prompts you keep loading.**

**`CLAUDE.md` — your coding constitution.** Names the library (D3 v7), file conventions (single HTML file, inline CSS+JS, no external dependencies), physics constants (ε₀ = 8.85 × 10⁻¹² C²/N·m², μ₀ = 4π × 10⁻⁷ T·m/A, k = 8.99 × 10⁹ N·m²/C², c = 2.998 × 10⁸ m/s), numerical methods (RK4 for field-line integration), animation idioms (`requestAnimationFrame`, sliders drive `input` events that re-render in real time), and a verification checklist. You write this file once, in Chapter 0. You revise it across chapters as your taste in code sharpens.

**`DESIGN.md` — your visual constitution.** Names the color conventions you'll keep across every chapter. Positive charges: red. Negative charges: blue. Electric field lines: dark gray. Equipotentials: green, dashed. Magnetic field lines: purple. Current arrows: orange. Canvas sizes: 700×500 for fields, 700×400 for time-series plots. Dark mode: backgrounds shift, lines lighten by 40%. The same conventions across twelve chapters means a student can glance at any simulation and instantly read what's happening.

**`PROJECT.md` — project state.** A live document tracking which simulations you've built, which chapter you're on, what's outstanding. Updated by you after each chapter. Three lines is fine; ten is fine; it's a scratch ledger, not a publication.

**Why three files instead of one?** Because the *instruction budget* — how much context Claude reads on every prompt — grows linearly with the file size. Cramming coding rules and visual rules and project state into one file means every prompt re-reads all of it. Splitting them means each prompt loads only what matters. Coding question? Load `CLAUDE.md`. Restyling? Load `DESIGN.md`. Update the ledger? Load `PROJECT.md`.

### The four-move prompt structure

Every LLM Exercise in this book uses the same prompt scaffold. Four moves in order:

1. **Show.** Paste the reference. The equation, the desired output picture, an annotated diagram. Concrete, not abstract.
2. **Say.** State the task in one sentence. "Render the electric field of a point charge as a 2D vector field."
3. **Constrain.** List the rules. Library, file format, allowed inputs, what to avoid, color conventions, the specific physics formula. Three to ten items.
4. **Verify.** Name the checks you'll perform on the output. Does it open in a browser? Do arrows point outward from a positive charge? Does field magnitude fall as 1/r²?

The fourth move is the one students skip. Without `Verify` in the prompt, the student doesn't know what "working" means and accepts whatever Claude returns. Naming the checks *in the prompt itself* trains the diagnostic habit the rest of the book depends on.

### Worked example: the point charge

The simplest possible E&M object. One charge q at the origin. Field at distance r from the charge:

$$\vec{E}(r) = \frac{kq}{r^2}\,\hat{r}$$

Field lines emerge from a positive charge in straight radial spokes; converge to a negative charge in straight radial spokes. Magnitude falls as 1/r². Field lines never cross. Density of lines correlates with field strength (with a caveat — see Common Misconceptions).

To compute and draw a field line from a chosen starting point near the charge, we integrate the equation d**r**/ds = **E**/|**E**| (unit vector along the field at the current position) numerically. The standard method is the **fourth-order Runge–Kutta** (RK4):

```
At current position p with step size h:
  k₁ = E(p)/|E(p)|
  k₂ = E(p + h·k₁/2)/|E(p + h·k₁/2)|
  k₃ = E(p + h·k₂/2)/|E(p + h·k₂/2)|
  k₄ = E(p + h·k₃)/|E(p + h·k₃)|
  p_new = p + h(k₁ + 2k₂ + 2k₃ + k₄)/6
```

Stop when p exits the canvas, when |E| drops below threshold, or when p enters a small radius around another charge.

**The lesson.** A field line is a *path through the field*, generated by walking along E one small step at a time. Once you can compute a field line, you can compute a field map for any charge configuration.

**The limit.** RK4 fails near singularities (very close to a point charge, |E| → ∞ and the step becomes erratic). The fix is to start your field lines on a small circle of finite radius around each charge — never *at* the charge.

---

## Common misconceptions

**"Field-line density shows field strength."**
Partially true and partially a teaching simplification. In two dimensions with line count proportional to |q|, density gives an approximate quantitative read on |E|. In 3D rendered to a 2D cross-section, density is only qualitative. Chapter 2 returns to this carefully. For Chapter 0, the simplification ("more lines = stronger field") is fine.

**"The simulation is correct if it looks like the textbook picture."**
A simulation that looks right can still be wrong: wrong constants, wrong scaling, wrong direction. The four-move `Verify` step is the antidote. Always check at least one quantitative limit (flip the sign of q and watch arrows reverse; double q and confirm field doubles, not quadruples).

**"Claude knows D3."**
Claude knows D3 v6 *and* v7 syntax, plus older. Without specifying v7 in `Constrain`, you may get hybrid or v6 code with breaking changes. Be explicit.

**"The Brutalist files are documentation."**
They are not. They are *active prompts loaded with every interaction*. A `CLAUDE.md` Claude doesn't read in some prompts isn't doing its job for those prompts. Tell Claude which file to use, every time.

---

## Exercises

**Warm-up (Apply).** Write a one-sentence definition of each of the three Brutalist files. Then write the four moves of the prompt structure in one sentence each, with no formulas.

**Apply.** Open the simulation you generate in this chapter. Flip the sign of the charge using the slider. Predict what the field lines should do *before* you watch the animation. Did your prediction match? Write one sentence on why it did or didn't.

**Apply.** Modify the prompt to render *two* charges instead of one. The two charges should be at (−L/4, 0) and (+L/4, 0). Compare the resulting picture to two textbook diagrams: (a) two opposite charges (a dipole), (b) two like charges. Verify by eye that your simulation matches both.

**Apply + Analyze.** Change one color in `DESIGN.md`: make positive charges magenta instead of red. Re-run the prompt without modifying it. Did the simulation respect the change? If not, what prompt change was needed? (Answer: explicitly tell Claude to re-read `DESIGN.md` before generating.)

---

## LLM Exercises

### Part 1 — Generate `CLAUDE.md`

Paste to Claude:

> **Show.** I am building a series of D3.js v7 simulations for an undergraduate electromagnetism course. Each is a single HTML file with inline CSS and JS, no external dependencies. The simulations use sliders for parameters, RK4 integration for field lines, and `requestAnimationFrame` for animation.
>
> **Say.** Generate a `CLAUDE.md` file I will keep at the top of my project. It is a coding constitution Claude will read with every prompt.
>
> **Constrain.** Include sections: (1) Library and file conventions, (2) Physics constants (ε₀, μ₀, k, c), (3) Numerical methods (RK4 with adaptive step size for field lines, finite differences for gradients), (4) Animation idioms (requestAnimationFrame, sliders on input events), (5) Verification checklist (does it open, does the physics work at limits, do colors match DESIGN.md), (6) No external dependencies beyond D3 v7.
>
> **Verify.** The file should be one markdown document, no longer than 60 lines. When pasted as system context, Claude should be able to produce a working point-charge simulation with no additional prompting beyond "make a point-charge field-line simulator."

Save to `CLAUDE.md`.

### Part 2 — Generate `DESIGN.md`

Paste to Claude:

> **Show.** I am building D3 simulations for E&M. Color conventions matter because students will see twelve of these and need to read them at a glance.
>
> **Say.** Generate a `DESIGN.md` for the project.
>
> **Constrain.** Include: positive charges red (#d62828), negative blue (#1d3557), electric field lines dark gray (#444), equipotentials green (#2a9d8f) dashed, magnetic field lines purple (#7b2d8b), current direction orange (#f4a261). Canvas: 700×500 for field views, 700×400 for time-series. Dark mode via `prefers-color-scheme`. Font: system sans-serif. 1.5px line strokes default.
>
> **Verify.** When pasted alongside `CLAUDE.md`, a simulation generated by Claude should match every color and dimension.

Save to `DESIGN.md`.

### Part 3 — Generate `PROJECT.md`

Three lines is fine: project name, current chapter, simulations completed (empty so far).

### Part 4 — Build the point-charge simulator

With `CLAUDE.md` and `DESIGN.md` in the conversation context:

> **Show.** Coulomb's law: **E** = kq/r² r̂. I want to see the field lines around a single point charge.
>
> **Say.** Build a point-charge field-line visualizer in a single HTML file.
>
> **Constrain.** D3 v7. Charge at canvas center. Slider for q in range [−5, +5] in arbitrary units. Render 16 field lines per charge using RK4 integration from a small circle of radius 10 px. Stop integration when a line exits the canvas. Charge shown as a red circle for positive, blue for negative. Field lines in dark gray. File name: `00-point-charge.html`.
>
> **Verify.** (a) The file opens in Chrome. (b) Positive charge: field lines emerge radially. (c) Negative charge: field lines converge radially. (d) Doubling q does not change the field-line directions, only their density encoding (which we'll add in Chapter 1).

Save to `00-point-charge.html`. Open it.

### Part 5 — Exploration

- Flip the sign. Watch field lines reverse.
- Double the magnitude. (No visible change yet; this is the bug `Verify`-step (d) flagged. Chapter 1 will fix it.)
- Resize the browser window. Does the canvas stay readable?

### Part 6 — Extension prompt (chapter bridge)

> **Show.** I now have a single-charge simulator. Coulomb's law for two charges: total force is the vector sum.
>
> **Say.** Extend the simulator to two charges with independent positions and magnitudes.
>
> **Constrain.** Use the existing file as starting point. Two charges, each with its own slider for q. Drag-and-drop on the canvas to reposition. Render field lines from each, using superposition.
>
> **Verify.** With one positive and one negative charge of equal magnitude: field lines should connect them (a dipole pattern). With two positive charges of equal magnitude: a symmetric pattern with a null point on the midline.

Save to `00b-two-charges.html`. This file is your bridge into Chapter 1.

---

## What would change my mind

The Brutalist three-file system rests on one empirical claim: that splitting the instruction budget across three files produces better LLM output than one consolidated file. If a controlled experiment showed that students using a single consolidated `INSTRUCTIONS.md` produced *better* simulations (correctness, modifiability, transferability across chapters) than students using the three-file split, I would revise this chapter. I have not run that experiment, and I am open to its negative result. The deeper claim — that *some* structured prompt scaffolding beats unstructured prompting — is supported by the prompt-engineering literature (Brown et al., 2020; Wei et al., 2022) and is unlikely to be overturned.

## Still puzzling

- *What is the right granularity for a `CLAUDE.md` file?* Sixty lines is the working answer; I do not have a principled justification beyond "students who write longer ones see less change in Claude's output."
- *Does the four-move prompt generalize to LLMs other than Claude?* It works on ChatGPT and Gemini in my testing, but I have not measured systematically.
- *When does the simulation-build habit stop being a learning aid and start being a substitute for thinking?* I do not have a clean answer. The exercises in subsequent chapters try to keep the labor on the student's side of the line, but I am sure I have not gotten every exercise right.

---

**Tags:** D3, point charge, Coulomb's law, simulation pedagogy, Brutalist, four-move prompt, RK4, field lines, LLM-assisted learning

