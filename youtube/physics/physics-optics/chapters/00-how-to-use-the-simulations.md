# Chapter 0 — How to Use the Simulations

*Get from zero to a working, modifiable ray-tracing simulation before any new optics content.*

---

## Learning objectives

By the end of this chapter you will be able to:

1. **(Apply)** Generate the three Brutalist governing files — `CLAUDE.md`, `DESIGN.md`, `PROJECT.md` — adapted for optics conventions.
2. **(Apply)** Write a four-move prompt (Show / Say / Constrain / Verify) and produce a working D3 simulation of a single ray reflecting off a flat mirror.
3. **(Analyze)** Verify a simulation against three checks: it opens, the physics works at obvious limits (θᵢ = 0 → ray returns; θᵢ = 45° → reflected ray perpendicular to incident), and the visualization conventions match `DESIGN.md`.
4. **(Apply)** Modify the simulation — change angle, flip mirror orientation, add a second ray, label angles — and predict each change's effect before pressing reload.

---

## Opening case: the homework problem at 11 PM

A student is stuck Wednesday night on her optics homework. Problem 4 asks: at what angle of incidence does the reflected ray make a 75° angle with the surface? She has read the textbook section on the law of reflection. She understands that the angle of reflection equals the angle of incidence and both are measured from the normal (not the surface). But she keeps making sign errors, and the angle between reflected ray and surface, measured how exactly, is making her doubt her answer.

She opens her editor and pastes a four-move prompt to Claude:

> **Show.** [Law of reflection: $\theta_r = \theta_i$ from the normal.] [Picture: incident ray hits horizontal mirror, normal is vertical, reflected ray makes the same angle on the other side.]
> **Say.** Build a flat-mirror ray tracer in a single HTML file using D3 v7.
> **Constrain.** Horizontal mirror at $y = 0$. Slider for incident angle (0–89°). Incident ray drawn orange; reflected ray drawn blue. Show the normal as a gray dashed line. Display incident angle, reflected angle, and angle-from-surface as text labels.
> **Verify.** At 0°, both rays are vertical. At 45°, the rays are perpendicular to each other. The reflected angle always equals the incident angle (both measured from the normal).

Sixty seconds later she has 70 lines of HTML. She opens it, drags the slider to where angle-from-surface reads 75°, and reads off the answer: 15° from the normal. She submits the homework.

The chapter ahead teaches you to be that student. The prompt is the easy part. The cognitive habit — write the verify check *into* the prompt, so you know what "working" means — is the lesson.

---

## Core concept

### The Brutalist three-file system, adapted for optics

The three governing files travel with the project across all 10 chapters. They are not documentation. They are **active prompts you load with each interaction**.

**`CLAUDE.md` — coding constitution.** Names the library (D3 v7), file conventions (single HTML, inline CSS+JS, no external dependencies), physics constants (c = 3 × 10⁸ m/s, h = 6.626 × 10⁻³⁴ J·s, common refractive indices like n_air = 1.0003, n_water = 1.33, n_glass = 1.5), numerical methods (trigonometry for ray geometry — no RK4 needed for geometric optics), animation idioms (`requestAnimationFrame`, sliders → `input` events), and a verification checklist.

**`DESIGN.md` — visual constitution.** Optics-specific colors and dimensions:
- Incident rays: **orange** (#e76f51), 2 px stroke
- Reflected rays: **blue** (#457b9d), 2 px stroke
- Refracted (transmitted) rays: **green** (#2a9d8f), 2 px stroke
- Surface normals: gray (#aaa), 1 px dashed
- Optical surfaces (mirrors, lens outlines): black (#222), 2 px
- Wavefronts: purple (#7b2d8b), 1 px dashed
- Object points: filled black circles
- Image points: open circles in the color of the corresponding ray
- Intensity color map (for wave-optics chapters): blue → red (cool to hot)
- Canvas: 800 × 500 for ray diagrams; 700 × 400 for intensity plots
- Dark mode via `prefers-color-scheme`

**`PROJECT.md` — project state.** A scratch ledger: project name, current chapter, simulations built so far, outstanding TODOs. Updated by the student after each chapter.

### The four-move prompt structure

Every LLM Exercise in this book follows the same four moves in order.

1. **Show** — paste the reference. The equation, the geometric setup, the desired output diagram. Concrete.
2. **Say** — name the task in one sentence. "Build a flat-mirror ray tracer."
3. **Constrain** — list the rules. Library, file structure, sliders, formulas, what to avoid, color conventions.
4. **Verify** — name the physics checks you'll perform. At zero angle, what should happen? At a limit, what should match an analytical answer?

The fourth move is the one students skip. Without `Verify` in the prompt, you don't know what "working" means and you accept whatever Claude returns. Naming the verification criteria *in the prompt itself* is the diagnostic habit the book rests on.

### Optics differs from E&M for simulations

In the Electromagnetism volume, every simulation was a vector-field rendering computed by numerical integration (RK4) of field lines. In Optics, simulations are *ray-based*: rays are line segments computed by trigonometry. The math is simpler. RK4 rarely appears. Instead, the operations are:

- **Ray-mirror intersection.** Compute where a parameterized ray crosses a surface.
- **Ray-lens refraction.** Apply Snell's law (Ch 2) at each lens surface, or use the three principal-ray rules for thin lenses (Ch 4).
- **Wave-optics intensity.** Compute $I(\theta)$ as a closed-form expression of the geometry (Chs 5–6).

This means: a student finishing Chapter 0 in 30 minutes has a working simulator. The complexity climbs into wave optics, but geometric optics chapters are computationally cleaner than their E&M counterparts.

---

## Worked example: the flat mirror in code

A horizontal mirror at $y = 0$. An incident ray from a source at $(x_0, y_0)$ makes angle $\theta$ from the normal. The ray hits the mirror at point $(x_0 + y_0 \tan\theta, 0)$. The reflected ray leaves the same hit point at the same angle on the other side of the normal.

**Direction vectors.** If the incident ray heads down-right at angle $\theta$ from the vertical normal, its direction is $\vec{d}_i = (\sin\theta, -\cos\theta)$. After reflection (the $y$ component flips), the reflected direction is $\vec{d}_r = (\sin\theta, +\cos\theta)$.

In JavaScript:
```javascript
const reflect_horizontal_mirror = (dx, dy) => [dx, -dy];
```

To draw the rays as SVG line segments, extend each from the hit point along its direction until it exits the canvas. The math is two lines; the visualization is the rest of the file.

**The lesson.** With the law of reflection ($\theta_r = \theta_i$) and trigonometry, a complete ray-tracing simulation fits in ~70 lines of HTML+CSS+JS.

**The limit.** This treats the mirror as perfectly flat and the ray as a single mathematical line. Real mirrors have surface roughness causing diffuse scattering; real beams have finite width. For intro purposes, both idealizations are excellent. Wave-optics chapters (5–6) return to the cases where they break down.

---

## Common misconceptions

**"The angle of reflection is measured from the surface."** Almost always measured from the *normal*, not the surface. The two add to 90°. Pick a convention and use it consistently throughout your simulation.

**"Field-line density shows field strength in 2D ray pictures."** Different volume — that was the E&M visualization. In optics, ray density doesn't directly correspond to intensity; ray *count* in a beam approximates it, but density on the page is more about diagram readability than physics.

**"Claude will know which D3 version to use."** It defaults to a recent one but may produce v5 or v6 code without explicit `v7` constraints. Be explicit in `CLAUDE.md`.

**"The Brutalist files are documentation."** They are prompts. Tell Claude in each conversation: "Read CLAUDE.md and DESIGN.md before responding."

---

## Exercises

**Warm-up (Apply).** State the four moves of the prompt structure in one sentence each, with no formulas. Then list the three Brutalist files and explain what each is for.

**Apply.** Open your `00-flat-mirror.html` simulation. Set the angle of incidence to 0°. Predict what the reflected ray should do (answer: travel back along the incident ray, vertically). Verify in the simulation.

**Apply.** Set the angle of incidence to 45°. The angle between the incident and reflected rays should be exactly 90°. Verify this both algebraically and in the simulation. Now answer: at what angle of incidence is the angle between incident and reflected rays exactly 60°? (Answer: 30°.)

**Apply + Analyze.** Modify the simulation to add a *second* incident ray from a different source position. Both rays reflect off the same mirror. Predict where each reflected ray ends up before reloading.

**Challenge.** Change the mirror from horizontal to *vertical* (a mirror at $x = 0$, normal pointing in $\pm \hat{x}$). What changes in the code? What's the simplest way to refactor so the code handles any mirror orientation?

---

## LLM Exercises

### Part 1 — Generate `CLAUDE.md`

> **Show.** I am building a series of D3.js v7 simulations for an undergraduate optics course. Geometric optics chapters render ray diagrams using line segments and trigonometry. Wave optics chapters render intensity patterns as line plots.
>
> **Say.** Generate a `CLAUDE.md` for the project — a coding constitution Claude reads with every prompt.
>
> **Constrain.** Sections: (1) Library and file conventions (D3 v7, single HTML file, inline CSS+JS, no external dependencies); (2) Physics constants ($c$, $h$, common $n$ values for air, water, glass); (3) Geometric-optics methods (trigonometry for ray-surface intersection, law of reflection, Snell's law, three principal-ray rules for thin lenses); (4) Wave-optics methods (closed-form intensity formulas; numerical evaluation on a grid; line plots via D3); (5) Animation idioms (`requestAnimationFrame`, sliders on `input` events, pause/play button); (6) Verification checklist (does it open; physics works at limits; matches DESIGN.md colors).
>
> **Verify.** ~60 lines. Pasted as system context, Claude should produce a flat-mirror ray tracer with no further prompting.

Save to `CLAUDE.md`.

### Part 2 — Generate `DESIGN.md`

> **Show.** Optics simulations have specific color conventions I want to maintain across 10 chapters.
>
> **Say.** Generate a `DESIGN.md` for the project.
>
> **Constrain.** Colors: incident rays orange (#e76f51), reflected blue (#457b9d), refracted green (#2a9d8f), surface normals gray (#aaa) dashed, optical surfaces black (#222), wavefronts purple (#7b2d8b) dashed, image points open circles, object points filled black. Canvas: 800×500 for ray diagrams; 700×400 for intensity plots. Intensity color map blue→red. Font: system sans-serif. Stroke widths: 2px for rays, 1px for normals/wavefronts. Dark mode via `prefers-color-scheme`.
>
> **Verify.** All four ray-type colors are distinct and accessible. Dimensions are explicit.

Save to `DESIGN.md`.

### Part 3 — Generate `PROJECT.md`

Three lines of state: project name, current chapter, simulations completed (empty so far).

### Part 4 — Build the flat-mirror ray tracer

With `CLAUDE.md` and `DESIGN.md` loaded:

> **Show.** Law of reflection: $\theta_r = \theta_i$, both measured from the surface normal.
>
> **Say.** Build a flat-mirror ray tracer in a single HTML file.
>
> **Constrain.** D3 v7. Horizontal mirror at $y = 0$ across the canvas. Light source at $(x_s, y_s) = (200, 350)$. Slider for angle of incidence (0–89°). Render incident ray (orange), reflected ray (blue), and normal at the hit point (gray dashed). Display three text labels: incident angle from normal, reflected angle from normal, angle of reflected ray from surface. Filename: `00-flat-mirror.html`.
>
> **Verify.** (a) At 0°, reflected ray returns vertically along the incident ray. (b) At 45°, incident and reflected rays are perpendicular. (c) Reflected angle always equals incident angle.

Save to `00-flat-mirror.html`. Open in your browser.

### Part 5 — Exploration

- Slide to angle of incidence = 0°. Where does the reflected ray go?
- Slide to angle of incidence = 89°. Where does the reflected ray go?
- Resize the browser window. Does the canvas scale correctly?

### Part 6 — Extension prompt (chapter bridge)

> **Show.** I have a single-ray, single-mirror tracer. I want to add a second mirror and see how a ray reflects off both.
>
> **Say.** Extend the simulation to two perpendicular mirrors forming a corner.
>
> **Constrain.** First mirror horizontal at $y = 0$; second mirror vertical at $x = $ some chosen position. Ray reflects off the first, then off the second. Use the existing reflection code; apply it twice.
>
> **Verify.** No matter what angle the incident ray makes with the first mirror, the ray reflecting off both mirrors emerges parallel to the original incident ray, but offset. This is how a *corner reflector* works (used in road signs and bicycle reflectors).

Save as `00b-corner-reflector.html`. This is the bridge into Chapter 1.

---

## What would change my mind

The Brutalist three-file structure rests on the empirical claim that splitting the instruction budget across three files produces better LLM output than one consolidated file. If a controlled study showed students using a single `INSTRUCTIONS.md` produce *better* simulations than students using the three-file split, the framework would need revision. I have not run that study; I am open to its negative result. The deeper claim — that *some* structured prompt scaffolding beats unstructured prompting — is supported by the prompt-engineering literature (Brown et al., 2020; Wei et al., 2022) and is unlikely to be overturned.

## Still puzzling

- *What's the right granularity for `CLAUDE.md`?* Sixty lines is the working answer; I don't have a principled justification.
- *Does the four-move prompt generalize to LLMs other than Claude?* Yes in my testing on ChatGPT and Gemini; I haven't measured systematically.
- *When does the simulation-build habit stop being a learning aid and start being a substitute for thinking?* I do not have a clean answer. The exercises throughout the book try to keep cognitive labor on the student's side of the line, but I am sure I have not gotten every exercise right.

---

**Tags:** D3, flat mirror, law of reflection, Brutalist, four-move prompt, optics simulation, ray tracing, geometric optics

![Four-panel reference diagram showing the recurring prompt structure used in every LLM exercise in the book. Show is the physical setup sketch; Say is the single-sentence imperative; Constrain is the rule list includin...](images/00-how-to-use-the-simulations-fig-01.png)
*Figure 0.1 — Four-Move Prompt*

![Systems diagram showing three context files feeding a central LLM prompt. CLAUDE.md is the coding constitution (behavior). DESIGN.md is the visual constitution (appearance). PROJECT.md is the project state (memory). T...](images/00-how-to-use-the-simulations-fig-02.png)
*Figure 0.2 — The Brutalist Three-File System*

![Geometric diagram of a single light ray hitting a horizontal mirror. Incident ray in orange arrives from upper left at angle theta-i measured from the vertical normal (dashed gray). Reflected ray in blue leaves to upp...](images/00-how-to-use-the-simulations-fig-03.png)
*Figure 0.3 — Flat-Mirror Reflection*

![Geometric diagram of a light ray entering a corner of two perpendicular mirrors. Incident ray in orange enters from the upper right, bounces off the horizontal mirror, reflects to the vertical mirror, and exits to the...](images/00-how-to-use-the-simulations-fig-04.png)
*Figure 0.4 — Corner Reflector*

