# Chapter 11 — Owning Your DESIGN.md


## TL;DR

- Is the design system a tool you direct, or a set of defaults you inherited?
- The chapter moves through What design tokens actually are, What an unowned DESIGN.md looks like, What an owned DESIGN.md looks like, Why the model cares about your comments, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*Is the design system a tool you direct, or a set of defaults you inherited?*

---

There is a thing that happens when you use a system long enough without examining it. The system starts to speak for you.

I want to describe the feeling precisely, because it is easy to dismiss as aesthetic dissatisfaction — which is not what it is. After a semester using the Brutalist system faithfully, your slides are correct. The headlines assert. The color encodes. The visual channel is doing work. You run the diagnostics from the first ten chapters and nothing fails.

And the slides feel like someone else made them.

Show the deck to a colleague who teaches a different course in a completely different register, and their deck looks like your deck. Same red. Same hierarchy. Same one-claim-per-slide rhythm. Same typeface, same density, same template feel. Your seminar on intellectual history and their sophomore data structures lecture are not the same thing. The decks do not know that.

The slides are not wrong. They are correct the way a freshman essay can be correct — no grammatical errors, no factual mistakes, nothing clearly broken — and still not the writing of someone who has something to say. The defaults are doing the talking. You are not.

This is not a problem you can fix at the slide level. Changing individual slides does not change the system that generates them. The problem is upstream: the DESIGN.md has never been examined. It is a collection of inherited defaults, and it feels generic because it is generic — it was tuned for someone else's context, and you adopted it without checking.

The deeper structural point is this. The DESIGN.md is the boundary between the work the AI tool does and the decisions you have made. When the file is unowned, that boundary has been crossed silently — the tool is making your design decisions because the file you handed it does not actually contain yours. The cost is invisible until the slides start to look like a generic version of themselves, which is exactly what they are.

The fix is to own the file.

---

## What design tokens actually are

Before examining the file, it helps to understand what kind of artifact a DESIGN.md is.

A design token is a named variable that stores a single visual decision: a color, a font size, a spacing unit. The term was popularized by Salesforce's Lightning Design System team around 2014, and the underlying idea is older — CSS custom properties, print style guides, the *Chicago Manual of Style*, any system that makes a decision once and applies it consistently rather than re-deciding it on every artifact. The structural argument is not aesthetic. It is cognitive: a decision made once and stored is a decision you no longer have to make. Consistency is a byproduct; the primary product is the elimination of repeated work.

![The cognitive argument for design tokens is not consistency. It is the elimination of repeated decisions. Consistency is what you notice. Reduced decision load is what you gain.](images/11-owning-your-design-md-fig-01.png)
*Figure 11.1 — Two-row comparison *

What is distinctive in the AI-mediated workflow is that the DESIGN.md is also a *prompt*. The system reads the file as part of its context every time it generates a slide. Your design decisions are not just stored — they are instructions to a model. This dual nature, specification and instruction simultaneously, is not fully named in any peer-reviewed design-systems treatment I can find, and I want to flag that honestly: the framing is original to this book, and I do not yet have empirical evidence that it produces better outcomes than ad-hoc prompting. The structural argument is strong. The empirical argument is not yet.

But the implication follows from the structure. If the DESIGN.md is what the model reads, then a DESIGN.md full of inherited defaults is a file instructing the model to produce whoever's defaults those are. The model is faithfully executing the reference instance's design philosophy, not yours. The slides feel generic because you have handed the model someone else's rules and asked it to generate your course.

Ownership means something precise here. It does not mean changing most of the variables — many Brutalist defaults are good defaults, and the right answer for plenty of variables is "this one I endorse." Ownership means examining each variable against your context and arriving at a decision you can defend. The decision may be to keep the default. But it has to be a *decision*, not an inheritance.

![Ownership is not the value. Ownership is the comment.](images/11-owning-your-design-md-fig-02.png)
*Figure 11.2 — Two-state diagram of the same DESIGN*

---

## What an unowned DESIGN.md looks like

Consider a specific case. A faculty member teaches an intellectual-history graduate seminar — twelve students, primary-source reading, sustained discussion of Foucault and Arendt. They have been using the Brutalist system for a year. The DESIGN.md is the file as it shipped: no modifications, no comments added, no variables examined.

The accent color is `#C8102E` — Northeastern University red, the brand color of the institution the Brutalist system was originally tuned for. This faculty member teaches at a different institution whose brand red is `#7B0000` and whose style guide reserves red for emergency signage. The slides are projecting another institution's brand color onto a campus where that color reads as a collision. The variable was never opened.

The body text size is 28pt. This is sized for a 200-seat lecture hall with a 1080p projector at 60 feet of viewing distance. The seminar room has twelve seats and a maximum viewing distance of roughly 12 feet. At 28pt, three short bullets fill the entire screen. Every slide reads like a poster at a trade show. The variable passes the last-row test for the context it was calibrated to. It fails the last-row test for the room where it is being used. Nobody checked.

The visual form default is `diagram_over_list`. This is correct for a quantitative course where most content relationships are causal or comparative. This seminar's content is different: primary-source reading, which means the "visual" on most slides is a passage of historical prose set for reading. A diagram-over-list default is applying quantitative course logic to humanistic course material, and the mismatch shows in every slide that tries to turn a Foucault passage into a flowchart.

The headline rule is `headline_must_assert: true`. This is correct for teaching slides. But a seminar deck has slide types the Brutalist defaults do not account for. A citation slide — "Foucault, *Discipline and Punish*, 1975, pp. 217–220" — is not asserting a claim. It is orienting a discussion. The default headline rule produces forced assertion rhetoric on slides that should be reference labels. The file does not name the exception because nobody thought to look.

None of these variables is wrong in the abstract. Every one of them is wrong for this course, in this room, at this institution.

| variable | default value | correct context | actual context | failure |
| --- | --- | --- | --- | --- |
| accent color (#C8102E | NEU brand, large university | Use the chapter example as the concrete test case. | Use the chapter example as the concrete test case. | The pattern becomes easy to misuse or overlook. |
| body text size (28pt | 200-seat lecture hall, 60ft viewing | Use the chapter example as the concrete test case. | Use the chapter example as the concrete test case. | The pattern becomes easy to misuse or overlook. |
| visual form (diagram_over_list | quantitative causal relationships | Use the chapter example as the concrete test case. | Use the chapter example as the concrete test case. | The pattern becomes easy to misuse or overlook. |
| headline rule (must_assert | teaching slides | Use the chapter example as the concrete test case. | Use the chapter example as the concrete test case. | The pattern becomes easy to misuse or overlook. |

---

## What an owned DESIGN.md looks like

The same faculty member, after the work this chapter describes, produces a different file. Not dramatically different — most variables stay close to the defaults, because the defaults are thoughtful — but a file where every variable has been examined and every departure has a reason.

The accent color becomes a deep brown. The comment: institutional brand considerations, plus aesthetic neutrality for a course on power and surveillance. Not "I like brown better." A traceable decision.

The body font changes from a sans-serif to a serif face. The comment: the slides are thirty percent or more quoted historical prose, set at paragraph length. A serif font aids sustained reading; the sans-serif default was calibrated for bullet-point legibility, not for passage reading.

The body size drops to 22pt. The comment: last-row test passed in the actual seminar room on a specific date. The 28pt default was sized for 200 seats and 60 feet. This room has 12 seats and 12 feet. The test is the same test. The result is different because the room is different.

The density cap departs from the Brutalist 60-character limit. The comment: passage reading is the course's central activity. Author-written prose still caps at 60 characters. Quoted passages from primary sources carry their own density limit — roughly 250 words — because the passage *is* the slide content, not decoration over a claim.

The headline rule becomes a hybrid: assertion headlines on teaching slides, citation labels on reference slides, question fragments on discussion-prompt slides. Three slide types, three headline grammars. The exception has been expanded to fit the course.

What makes the owned version owned is not that the variables differ from the defaults. It is that each variable is now a decision traceable to a principle. The faculty member can point to a specific reason — cognitive, visual, or contextual — for every value in the file.

![Same variables. The comments are not decoration — they are the decisions.](images/11-owning-your-design-md-fig-03.png)
*Figure 11.3 — Of two DESIGN*

---

## Why the model cares about your comments

Here is something that might seem like an implementation detail but is load-bearing.

The DESIGN.md comments — the one-sentence justifications you write for each variable — are not just documentation for yourself. They are part of the context window the model reads. A comment that says `/* 28pt — lecture-hall default, not checked for this room */` instructs the model that this value is provisional. A comment that says `/* 22pt — last-row test passed in 12-seat seminar, 2026-01-15 */` instructs the model that this value has been verified for a specific context. A comment that says `/* accent brown — replaces Brutalist red; no institutional brand overlap; deliberate departure */` tells the model that this is an intentional decision, not an oversight.

The model generates slides against this context. A file full of provisional defaults produces different slides than a file full of examined decisions, because the comments change how confidently the model applies the rules. An unverified variable is a variable the model has to decide how strictly to enforce. A verified variable is a constraint the model enforces without negotiation.

This is the dual-audience property. The comment is legible to you, as a record of your thinking. The comment is legible to the model, as a signal about the variable's authority. Writing the comment is not bureaucratic documentation. It is the act that makes the variable a decision rather than an inheritance.

![The comment has two readers. For the human it is a record. For the model it is an authority signal.](images/11-owning-your-design-md-fig-04.png)
*Figure 11.4 — Dual-reader diagram *

---

## The audit

The prompt that operationalizes this chapter:

```
Audit this DESIGN.md against the courses I teach and my institution.
Report on three dimensions.

1. Palette. For each color variable: does this color encode something
   specific in my course's content, or is it inherited from the Brutalist
   reference instance? Flag any color that has no encoding role for my
   context. Flag any color that creates a brand collision with my
   institution.

2. Typography. For each typography variable: is this sized for my lecture
   room, my content type, and my students' reading conditions? Flag font
   sizes that pass the last-row test in the Brutalist reference space but
   not in my space. Flag font families that fight my content type.

3. Density and headline grammar. For my course shape — lecture, seminar,
   studio, lab — is the default body-text-density cap correct? Is the
   default headline-must-assert rule correct, or does my course have
   reference-slide types that need a different grammar? Name the slide
   types explicitly.

For each flag, propose the DESIGN.md change. Include a one-sentence
rationale in framework vocabulary — cognitive science or visual design.
If you cannot justify the change in framework vocabulary, flag it as
aesthetic preference and ask me to re-examine.
```

Two things to notice. The three dimensions are constrained — palette, typography, density — rather than open-ended. Constraining the question makes the answer usable. An open audit produces a list of suggestions without priority; a three-dimension audit produces actionable flags.

The framework-vocabulary requirement is the discipline. A change you can justify in terms of Mayer's principles, the last-row test, contrast ratios, or the slideument distinction is a design decision. A change you want because "it looks better" is an aesthetic preference, which is valid but should be named as such — because aesthetic preferences drift with mood, and design decisions do not. The prompt forces the distinction.

---

## The reflexive point

The Brutalist DESIGN.md you started with is itself an opinionated file. Somebody examined every variable against a particular context — probably a quantitative course, a large lecture hall, a specific institution — and arrived at the defaults you inherited. Those defaults are not arbitrary. They are decisions, made for someone's context.

Your job, at this point in the book, is the same operation on your context. Examine each variable. Endorse it if it fits. Change it if it doesn't. Write the comment either way. The artifact you produce will look different from the artifact the Brutalist author produced. Both can be fully owned. Ownership is not convergence on the same file. Ownership is the process of examination, applied to your situation.

There is a version of this that is tempting to short-circuit. After running the audit prompt, you will have a list of proposed changes. Some you will accept; some you will reject. It is tempting to accept or reject based on how the change *feels* — does the output look better? — rather than on whether the reason holds. A change that looks better but has no framework justification is an aesthetic preference wearing a decision's clothes. The discipline is to write the one-sentence justification first, before you decide whether to accept the change, and to reject the change if you cannot write the justification.

A DESIGN.md where you cannot write a one-sentence justification for every variable is a DESIGN.md that is still partly inherited. The goal is not a fixed number of departures or a quota of comments. The goal is a file where every line is something you decided. That file will regenerate correctly six months from now, after you have forgotten the reasoning, because the reasoning is in the file. The unowned file will regenerate correctly too — it will just keep generating someone else's course.

![Ownership is the examination axis, not the departure axis. A file that endorses 90% of defaults with documented reasons is fully owned.](images/11-owning-your-design-md-fig-05.png)
*Figure 11.5 — 2x2 matrix *

---

## Two honest disagreements

Two reasonable faculty members can read this chapter and disagree about how far to take the ownership move.

One position: design systems become more useful the more consistently they are applied, even across different contexts. Variation reduces the cognitive payoff — if every instructor customizes the DESIGN.md, the system loses its consistency value and becomes a collection of one-off configurations. The Brutalist defaults represent accumulated judgment; overriding them requires better judgment than most instructors have developed. The recommendation: endorse most defaults, document the endorsement, and depart sparingly.

The other position: a design system that cannot adapt to context is not a system; it is a template. The whole point of named variables is that they can be changed without breaking anything. An instructor who teaches a seminar should not be using lecture-hall defaults. The recommendation: audit fully, change freely, document everything.

Both positions converge on the same discipline: document your decisions, in framework vocabulary, in the file. They disagree about how many departures the documentation should record. The chapter is comfortable with that disagreement, because the documentation requirement is the non-negotiable part. A faculty member who inherits ninety percent of the defaults and documents why each one was endorsed has done the work. A faculty member who departs from fifty percent of the defaults without documentation has not.

There is a second disagreement worth naming: whether the DESIGN.md is a specification or a prompt. The traditional design-systems literature treats it as the former — a normative document a designer applies. The AI-mediated workflow treats it as both specification and model instruction. If you conclude that the prompt framing overstates the case — that the comments are just documentation and the model would behave similarly without them — that disagreement is legitimate and I cannot fully resolve it. My reading is that the comments change how the model enforces the variables. But I am also the person who built this framing, and I should be appropriately skeptical of my own argument.

---

The book now has eleven chapters of diagnostic vocabulary and one DESIGN.md you can defend. What you do not yet have is a way to use that vocabulary on a deck you have never seen before, quickly, without re-reading everything. That artifact is Chapter 12.

---

**What would change my mind:** An empirical study comparing decks generated from heavily specified DESIGN.md files against decks generated from minimally specified files, showing that minimal specification produces equivalent or better outcomes once the author has built diagnostic vocabulary. The claim that specification scales better than per-slide tweaking is structural, not empirical. If expert authors produce better slides with permissive systems, the chapter's prescription weakens for readers past the novice stage.

**Still puzzling:** I do not have a clean rule for how much of a DESIGN.md should be specified versus left for per-slide judgment. The chapter takes a prescriptive position because the audience is developing diagnostic vocabulary, and prescription scaffolds judgment while that vocabulary is forming. After a year of use, some prescriptions should probably relax and others tighten. I cannot predict which ones in advance, because the answer depends on what each reader's eye has actually internalized.

---

## Exercises

**Warm-up**

1. A faculty member teaches a 400-seat introductory physics lecture and has never modified their DESIGN.md from the Brutalist defaults. The body text is 28pt. Is this an owned decision or an inherited default? What single piece of information would you need to determine whether 28pt is correct for their room, and how would you test it? *Tests: ability to distinguish endorsement from inheritance, and to name the test that resolves the question.*

2. The Brutalist default accent color is `#C8102E`. A faculty member at a different institution adopts the system without checking. Their institution's brand style guide reserves red for emergency signage. Name the failure type — is this a cognitive failure, a visual design failure, or a contextual failure? Explain why the slide is not "wrong" in the abstract while still being wrong in use. *Tests: understanding that default-correctness and context-correctness are separable.*

3. A DESIGN.md variable reads: `--font-size-body: 24pt`. The comment reads: `/* default */`. Is this variable owned? What would it take to make it owned without changing the value? Write the comment that would constitute ownership — in framework vocabulary, citing a specific test or principle. *Tests: ability to write a justification that makes inheritance into endorsement.*

**Application**

4. Open your own DESIGN.md (or, if you do not have one, the Brutalist default file). For each color variable, write one sentence answering: does this color encode something specific in my course's content, or is it inherited from the reference instance? Flag any variable for which your answer is "I don't know" or "it was the default." Count the flags. *Tests: ability to run the palette dimension of the audit against one's own file and identify unexamined variables.*

5. The intellectual-history seminar in this chapter has three slide types: teaching slides, citation slides, and discussion-prompt slides. The Brutalist default `headline_must_assert: true` handles one of them correctly. Write the headline rule that handles all three — in YAML-style comments, explaining why each type gets the grammar it gets, in framework vocabulary. *Tests: ability to expand a single-type rule into a multi-type rule with explicit justifications.*

6. A colleague argues: "I just tweak individual slides when something looks wrong. I don't need to update the DESIGN.md." Construct the strongest rebuttal. Name the specific failure mode that per-slide tweaking produces over time, and explain why updating the file is the correct level of intervention rather than the slide. *Tests: ability to explain the difference between a rule and a per-instance fix, and to identify the failure mode that accumulates when the rule layer is skipped.*

**Synthesis**

7. The chapter argues that DESIGN.md comments have two readers — the human author and the model — and that the same comment functions differently for each. Construct the best argument *against* this claim: that comments are just documentation and the model applies the rules identically with or without them. What would you need to observe, in actual generated slides, to falsify the claim in either direction? *Tests: ability to stress-test the chapter's novel dual-audience claim and specify what evidence would resolve it.*

8. You inherit a DESIGN.md from a colleague who has owned it carefully for two years. Every variable has a one-sentence justification. However, your colleague taught large quantitative lectures; you teach small qualitative seminars. Walk through at least four specific variables from the chapter's examples and apply the audit framework to each: which do you expect to endorse, which to revise, and on what basis would you make each decision? *Tests: ability to transfer the ownership move to a new context rather than repeating the worked examples.*

**Challenge**

9. The "what would change my mind" note names a specific missing empirical study: a comparison of heavily specified versus minimally specified DESIGN.md files on slide quality, once the author has built diagnostic vocabulary. Design that study. What is the independent variable, what outcome measures would you use, how would you control for content and instructor effects, and how would you operationalize "diagnostic vocabulary has been built" as an inclusion criterion? What result would constitute evidence that the chapter's prescription weakens for expert users? *Tests: ability to design the study that would resolve the chapter's central empirical gap, including the hardest methodological problem — defining expertise as an entry condition.*

---

## Tier Connection

The `DESIGN.md` is the phase gate made into a file. It is the artifact that holds the boundary between the rendering work the model does and the design decisions the author owns. When the file is unexamined — inherited defaults, no documented justifications, variables you have never read — the gate has been delegated across, even though the file is technically still there. The model is doing your design work, and the work has your name on it.

This is also the chapter where Tier 7 authorship becomes concrete. A `DESIGN.md` you wrote is a record of decisions you can defend. A `DESIGN.md` you inherited is a record of decisions someone else made for a different context. The first is yours. The second is borrowed authority operating under your byline. The audit in this chapter is the move that makes the difference visible. The decision to update is the move that makes the file yours. See *Appendix A — The Fundamental Themes*.

**Tags:** design-tokens, DESIGN.md, ownership, audit, Brutalist-system, specification-vs-prompt, aesthetic-drift

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 11.1 — Two-row comparison

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Two-row comparison". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-owning-your-design-md-fig-01.html`

---

### Figure 11.2 — Two-state diagram of the same DESIGN

Create a standalone D3 v7 HTML file for a concept map titled "Two-state diagram of the same DESIGN". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-owning-your-design-md-fig-02.html`

---

### Figure 11.3 — Of two DESIGN

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Of two DESIGN". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-owning-your-design-md-fig-03.html`

---

### Figure 11.4 — Dual-reader diagram

Create a standalone D3 v7 HTML file for a concept map titled "Dual-reader diagram". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-owning-your-design-md-fig-04.html`

---

### Figure 11.5 — 2x2 matrix

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "2x2 matrix". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/11-owning-your-design-md-fig-05.html`
