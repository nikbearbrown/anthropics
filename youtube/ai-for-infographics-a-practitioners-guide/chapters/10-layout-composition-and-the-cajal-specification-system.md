# Chapter 10 — Layout, Composition, and the CAJAL Specification System

## Opening: A vague brief, twelve minutes, one specification

The brief arrives the way briefs always arrive. A platform-reliability lead drops a message: *"Can you make a figure showing the relationship between our deploy frequency and our incident rate? For the all-hands."* That is the entire instruction. It is, as briefs go, completely typical and completely unbuildable. It names two variables and a vibe.

Watch what happens when that brief goes through the CAJAL intake instead of straight to a tool. The instructor takes it live, on a whiteboard, and in about twelve minutes the vague request becomes a defensible specification. *What is the figure actually claiming?* Not "deploys and incidents are related" — the lead, pressed, means **"more frequent, smaller deploys correlate with fewer severe incidents."** That is a claim. It can be true or false; it can be defended or attacked. *Who reads it, and where?* A mixed all-hands audience, projected, ten-second comprehension budget — so a single panel, not a six-panel dashboard. *What gets left out?* Deploy *size*, even though the lead cares about it, because the data don't cleanly separate small from large deploys and including a third variable would overload a projected figure. *What relationship is it?* Correlation over time — which, from the FT Visual Vocabulary of Chapter 6, points at a connected scatter or a dual-line time series, not a pie and not a bar.

By the end of the twelve minutes there is no SVG. There is something more valuable: a **complete design specification** — a claim, an audience, a layout type, a relationship, an encoding plan, and, above all, an *exclusion list*. The concept is now defensible. Someone could attack it, and you could answer. That document is the deliverable of this chapter and the input to the entire Act Three pipeline. The SVG is downstream; the judgment is here.

This is the chapter where the book's spine is most exposed. Everything in Act Three — Claude Code, D3, Illustrator, the PNG conversion — executes *against* this specification. If the specification is wrong, the tool will faithfully produce a wrong figure with great polish. The design intelligence layer is populated *here*, by a human, before a line of code exists. CAJAL is the name for that intelligence made into a process.

## Core content

### Three layout types and the medium that picks them

Before composition, classify the figure into one of three layout types. The type is chosen by *communication purpose and delivery medium*, not by how much you have to say [High].

- **Singular.** One figure, one claim, one visual. The all-hands deploy-vs-incident chart is singular. Singular layouts suit projected slides, social cards, and any context with a short comprehension budget. The discipline of singular is *one claim* — if you find yourself wanting a second panel, you probably have a second figure.
- **Composite.** Several coordinated panels arranged to be read together — a small-multiples grid, a figure with an inset, a main chart plus a breakdown. Composite suits a report page or a poster where the reader has time and the panels genuinely belong to one argument. The risk is that "composite" becomes "dashboard": a pile of unrelated charts sharing a border.
- **Long-form.** A vertical scroll or multi-section document infographic that walks the reader through a sequence — the explainer, the annual-report spread. Long-form suits web and print where the reader commits to a journey. The risk is length without structure.

Reading order is part of layout. In a left-to-right, top-to-bottom reading culture, the top-left is where the eye lands first; that is where the claim or the entry point belongs, not a logo or a legend. Composition in the Brutalist system rides on the 8px spacing grid from Chapter 5: margins, gutters, and panel sizes are multiples of 8, so alignment is structural rather than eyeballed. Exposed grid, honest alignment — the layout is itself a Brutalist commitment.

### The 6–8 component limit and the split decision

Cognitive load theory (Sweller, Chapter 2) makes a quantitative prediction the layout must honor: working memory holds a small number of elements at once, and an infographic that asks the reader to integrate more than roughly **6–8 components** at a time will fail comprehension regardless of how beautifully it is composed [High — consistent with working-memory limits; the 6–8 figure is a practitioner heuristic, not a precise constant]. A "component" here is a thing the reader must hold to understand the figure: a data series, a panel, a reference line, an annotation block.

When a concept exceeds the limit, you face the **split decision**: divide one overloaded figure into two figures (or into a composite of clearly separated panels), each under the limit. The split decision is a layout decision and an editorial one. It is also where AI tools fail predictably — asked to "show everything," a generator will cheerfully cram twelve series into one chart, because nothing in the prompt told it the reader has a working-memory ceiling. The ceiling is yours to enforce.

### CAJAL and the SCOPE framework

**CAJAL** is the book's figure-intelligence system — the process by which a concept description becomes a complete design specification document. (The name honors Santiago Ramón y Cajal, whose neuroanatomical drawings are the AI Wayback figure for this chapter; the connection is in the box below.) CAJAL runs an intake that produces a structured specification under the acronym **SCOPE**: **S**pecification, **C**ontent, **O**rganization, **P**resentation, **E**xclusions [High — SCOPE is this book's designed framework; the five-part structure is fixed, individual field formats are presented as the book's system. *Verify — system specifics* against the live CAJAL prompt.]

| Block | Question it answers | What it contains |
|---|---|---|
| **S — Specification** | What is this figure, and what does it claim? | One-sentence claim; figure purpose; audience; delivery medium; layout type; comprehension budget |
| **C — Content** | What is in it? | The data or concept; the relationship type (FT Visual Vocabulary); the marks and channels (Chapter 6); the data sources |
| **O — Organization** | How is it arranged spatially? | Layout type; reading order; panel/grid structure; what occupies the top-left; the 8px-grid placement of major elements |
| **P — Presentation** | How does it look? | Color tokens by role (Chapter 8); typography roles; annotation plan (the four jobs, Chapter 9); stroke conventions |
| **E — Exclusions** | What is deliberately left out? | Every variable, comparison, embellishment, and convenience the figure does *not* include — and one line of justification each |

SCOPE is deliberately ordered. You cannot specify Content until you have a claim (Specification). You cannot organize what you have not selected. You cannot present what you have not organized. And Exclusions come last because you can only know what to exclude once you know everything the figure could have been. The framework is a forcing function: it makes you populate the design intelligence layer in dependency order, the same order Act Three's phase gate will later enforce on the code.

### The exclusion list is the highest-leverage parameter

Here is the claim this chapter most wants you to leave with: **the exclusion list (E) is more important than everything in C, O, and P combined** [High — follows directly from the cognitive-load and prompt-to-code arguments].

Two reasons. First, perceptual: every element you include competes for the reader's limited attention, so what you *exclude* is what gives the included elements room to be read. A figure is defined by its negative space as much as a sculpture is. Second, and increasingly, operational: prompt-to-code and prompt-to-image generators *default toward clutter.* Ask a coding agent for "a figure showing deploy frequency and incidents" and it will add gridlines you didn't want, a legend you don't need, a third axis for a variable you meant to exclude, a gradient, a drop shadow. The generator's default is *more*. The exclusion list is the instrument that says *less*, explicitly, in a form the tool must honor.

This is why a CAJAL specification with a rich Exclusions block produces a clean figure on the first generation, and a specification without one produces the eleven-error mess you will meet in Chapter 13. The exclusion list is where human judgment most directly constrains the machine. "Exclude deploy size — data don't separate cleanly and a third variable overloads a projected figure" is a sentence no model would write for you, and it is the sentence that saves the figure.

### From specification to DESIGN.md and the Claude Code prompt

The CAJAL SCOPE specification is not yet the file Act Three consumes. It is the human-readable design document. **DESIGN.md** is its operational form: the same decisions written as a constitution the tool obeys — the seven color tokens with their roles, the typography stack, the layout type, the annotation plan, and the exclusion list rendered as explicit prohibitions ("no gradients; no legend; do not encode deploy size; no third axis"). The relationship is direct: **SCOPE is the thinking; DESIGN.md is the instruction; the Claude Code prompt references DESIGN.md so the design intelligence travels with every generation request.** A reader who has done the SCOPE work can write DESIGN.md mechanically. A reader who skipped it has nothing to write.

![A vague brief feeding the five SCOPE blocks — Specification, Content, Organization, Presentation, and Exclusions in red — which become DESIGN.md before any SVG exists](images/10-layout-composition-and-the-cajal-specification-system-fig-01.png)

*Figure 10.1 — The CAJAL intake turns a vague brief into the five SCOPE blocks in dependency order, with Exclusions (red) as the highest-leverage block, then operationalizes them as DESIGN.md before any SVG is generated.*

## Worked example: the deploy-frequency figure, fully specified

**Problem statement.** The vague brief from the opening: deploy frequency vs. incident rate, for an all-hands.

**First attempt (specification-less AI output).** Prompted with the raw brief, a coding agent produced a dual-axis chart: deploy count as bars, incident count as a line on a second y-axis, a legend, gridlines on both axes, twelve months of labels, a title "Deploys vs. Incidents," and a faint gradient behind the plot. Dual axes invite the classic correlation illusion (you can make any two series appear to track by scaling the axes), there is no stated claim, deploy *size* is silently absent without acknowledgment, and the figure carries nine-plus components onto a projected slide.

**The CAJAL SCOPE specification (the corrected design intelligence):**

```
[S — SPECIFICATION]
Claim: "Months with more frequent deploys had fewer severe incidents."
Purpose: persuade an all-hands that deploy frequency is not a risk.
Audience: mixed engineering + non-engineering, projected.
Medium: single projected slide. Comprehension budget: ~10 seconds.
Layout type: SINGULAR.

[C — CONTENT]
Data: 12 months. Per month: deploy count; count of SEV1/SEV2 incidents.
Relationship (FT Vocabulary): CORRELATION (with time as context).
Mark/channel: connected scatter — x = deploys/month, y = severe incidents/month,
  points connected in time order. Position on common scales (strongest channel).
Source: internal deploy log + incident tracker, 2025.

[O — ORGANIZATION]
Singular panel. Reading order: top-left title (the claim) → scatter → endpoint labels.
8px grid: 32px margins; plot region on grid; Jan and Dec points labeled.
Top-left holds the CLAIM, not a logo.

[P — PRESENTATION]
Color: all points/line in --color-ink; the most recent quarter highlighted in
  --color-red (the single accent). --color-fill plot region. NO ochre on data.
Type: title EB Garamond; axis ticks JetBrains Mono; labels Inter.
Annotation (four jobs): INTERPRETATION sentence beside the low-incident cluster
  ("High-deploy months cluster at low incidents"); ORIENTATION via direct
  endpoint labels (no legend); CAVEAT in small secondary-gray text.

[E — EXCLUSIONS]
- Deploy SIZE: excluded — data don't separate small/large; third variable
  overloads a projected figure.
- Dual axes: excluded — invite a scale-driven correlation illusion.
- Legend: excluded — direct labels instead (spatial proximity).
- Gridlines beyond two light references: excluded — clutter on projection.
- Gradient / shadow: excluded — Brutalist commitment.
- Causal language ("deploys CAUSE fewer incidents"): excluded — data are
  correlational; claim is worded as correlation, with a caveat.
```

**The lesson.** The vague brief asked for *deploys and incidents*; the specification decided it claims *frequent deploys correlate with fewer severe incidents*, chose a connected scatter over a misleading dual-axis chart, and — most consequentially — excluded deploy size and causal language in writing. The figure is correct before it exists.

**The limit.** A tool can render this specification into clean SVG in seconds. It cannot decide that the claim is correlational not causal, that deploy size must be excluded for honesty and load reasons, or that a connected scatter beats the dual-axis chart it would have defaulted to. Those are the human-judgment decisions, and the Exclusions block is where most of them live.

## AI Wayback Machine: Santiago Ramón y Cajal and the specification that precedes the drawing

The system is named for **Santiago Ramón y Cajal**, the Spanish neuroanatomist whose drawings of neurons, made around the turn of the twentieth century, remain in use as teaching figures more than a hundred years later [High]. (He shared the 1906 Nobel Prize in Physiology or Medicine with Camillo Golgi; Wayback target: Wikipedia "Santiago Ramón y Cajal.") What makes Cajal the right patron for a *specification* system is not that he drew beautifully. It is *how* he decided what to draw.

Cajal looked at tissue through a microscope that showed a chaotic tangle, and he made a relentless series of exclusion decisions: which cells to render, which to omit, what to emphasize, what to leave as suggestion. His drawings are not photographs — they are *arguments*, composed to make a structural claim (that neurons are discrete cells, not a continuous net) legible. He populated the design intelligence layer before his pen touched the paper, and the power of the figure came as much from what he left out as from what he put in. That is the exclusion list, a century early.

> **Prompt to try:** "Explain how Santiago Ramón y Cajal's decisions about what to leave out of a neuron drawing parallel the Exclusions block of a CAJAL SCOPE specification — and why the figure's claim depends on the omissions."

The throughline: a great figure is a specified figure, and the most consequential part of the specification is the part that says *not this.* Cajal knew it through a microscope; you will know it through SCOPE.

## Assessment — Design Specification Checkpoint (100 pts)

This is the Act Two capstone and the gateway to Act Three. You will produce a **complete CAJAL SCOPE specification and a DESIGN.md** for your terminal-project infographic — the figure you will actually generate, edit, and defend in the remaining chapters.

Deliverables:

1. **SCOPE specification (50 pts).** All five blocks fully populated. Specification states a one-sentence *claim* (not a topic) and names audience, medium, layout type, and comprehension budget (10). Content names the relationship type from the FT Visual Vocabulary and the mark/channel with justification (10). Organization specifies reading order and 8px-grid placement, and names what occupies the top-left (10). Presentation assigns color tokens *by role* and gives the annotation plan against the four jobs (10). **Exclusions lists at least five deliberate omissions, each with a one-line justification** (10).
2. **DESIGN.md (30 pts).** The SCOPE decisions rendered as an operational constitution: the seven tokens with roles, the typography stack, the layout type, the annotation plan, and the exclusion list written as explicit prohibitions a tool must honor.
3. **Defense paragraph (20 pts).** In 200–300 words, defend the single most consequential exclusion on your list — why leaving it out *improves* the figure — and explain why the exclusion list is more important than the inclusion list for your figure.

Attach an **AI Use Disclosure** naming at least two decisions in the specification that required your judgment and that no AI tool could supply — for example, the choice of *claim* over *topic*, and the most consequential *exclusion*. (Submissions without a completed disclosure receive the standard 15-point deduction.)

## Bridge

Act Two is complete. You hold a design specification: a claim, a layout, an encoding plan, an annotation plan, and an exclusion list, rendered as a DESIGN.md the tool can obey. Act Three now begins. Chapter 11 introduces the governing files of the Brutalist System — CLAUDE.md, DESIGN.md, and PROJECT.md — and the phase gate that forbids generation until the design intelligence layer is fully populated. The specification you just built is about to meet the pipeline that executes it.

## Sources

- Cairo, Alberto. *The Functional Art.* New Riders, 2012. Grounds infographics as explanation and argument rather than mere charts; basis for the claim-first Specification block.
- Lidwell, William, Kritina Holden, and Jill Butler. *Universal Principles of Design.* Rockport, 2010 (and later editions). Layout, hierarchy, proximity, and grouping principles underlying composition.
- Tondreau, Beth. *Layout Essentials.* Rockport, 2009 (and later editions). Practical grid and composition reference for the 8px-grid discipline.
- Sweller, John. "Cognitive Load During Problem Solving: Effects on Learning." *Cognitive Science*, 1988. Working-memory basis for the 6–8 component limit and the split decision.
- Gebru, Timnit, et al. "Datasheets for Datasets." *Communications of the ACM*, 2021. Documentation model adapted in spirit for the specification-as-provenance idea.
- Mitchell, Margaret, et al. "Model Cards for Model Reporting." *FAccT*, 2019. Structured-disclosure model informing the AI Use Disclosure framing.
- Ramón y Cajal, Santiago. Neuroanatomical illustrations (c. 1888–1904); Nobel Prize in Physiology or Medicine, 1906 (shared with Camillo Golgi).
- CAJAL SCOPE framework and Brutalist Design System (this book; `pantry/cajal-svg-generator.md`). [*Verify — system specifics* against the live CAJAL prompt.]
