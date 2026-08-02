# Chapter 2 — No Clear Hierarchy


## TL;DR

- When the eye doesn't know where to land first, the slide has already failed — what is it that makes hierarchy visible, and what destroys it?
- The chapter moves through What the eye is actually doing, Size: the ratio that actually works, Weight: the one-emphasis rule, Proximity: the grouping the eye trusts, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*When the eye doesn't know where to land first, the slide has already failed — what is it that makes hierarchy visible, and what destroys it?*

---

Here is a thing that happens to almost everyone who makes slides for the first time.

You put a title at the top. You put some bullets underneath. The title is a little bigger than the bullets — you can see that it's bigger, if you look carefully. Then you add a callout box on the right because there's a fact you want to highlight. You bold the callout heading so it stands out. You color two of the bullets because the colors feel right and the slide looks a little plain without them.

You look at the finished slide. It seems fine. Everything is on there.

Then you show it to someone and watch their eyes. They glance at the callout. Then the colored bullets. Then — eventually — they read the title. They have toured your slide in the wrong order, and they have left with the wrong thing in their head.

The troubling part is that nothing was an accident. Every element was placed with intention. The hierarchy was there. It was just *the wrong hierarchy.*

That's the puzzle. Not *does hierarchy matter* — it obviously does — but *what, exactly, produces it?* Because there are really only three forces doing the work, and once you see them you can diagnose any slide failure in about ten seconds.

---

## What the eye is actually doing

When you look at a slide for the first time, you are not reading. You are scanning.

The visual system is extraordinarily fast at certain things and extraordinarily slow at others. It is fast at detecting contrast — differences in size, weight, brightness. It is slow at parsing meaning. Reading a sentence takes hundreds of milliseconds per word. Detecting that one element is bigger than another takes around fifty milliseconds total.

This is not a metaphor. The magnocellular pathway in the visual cortex handles coarse spatial information fast; the parvocellular pathway handles fine detail and color more slowly. The practical consequence is that the first thing the eye does on a slide is not find the title — it finds the highest-contrast element, whatever that is. If the highest-contrast element is your "Did you know?" callout box, that's where the eye goes first. The title can be labeled *title* in your mind all it wants. The visual system doesn't read labels.

![Simplified schematic of the visual pathway from retina](images/02-no-clear-hierarchy-fig-01.png)
*Figure 2.1 — Simplified schematic of the visual pathway from retina*

So hierarchy on a slide is not what you intend. It is what the contrast gradients say.

Three forces produce contrast gradients: **size**, **weight**, and **proximity**. Size and weight work on individual elements — they make one thing look more important than another. Proximity works on groups — it makes things that belong together look like they belong together. Everything else is downstream of these three. You can do a lot of visual damage with color, but you cannot fix a broken hierarchy with it.

![Strip showing the same five slide elements arranged](images/02-no-clear-hierarchy-fig-02.png)
*Figure 2.2 — Strip showing the same five slide elements arranged*

---

## Size: the ratio that actually works

Size is the most intuitive of the three. Bigger means more important. This is correct, but incomplete. The relevant question is not *is the title bigger* but *how much bigger*, and at what distance.

Here is a fact that surprises most people: a title at 32 points above body text at 28 points is not a visible hierarchy at projection distance. The ratio — 32 to 28, roughly 1.14 — is below the threshold at which the visual system reads two elements as belonging to different levels. In normal reading conditions you might perceive the difference. In a lecture hall at fifteen feet, under variable lighting, the two elements read as one block. The slide has a hierarchy in the file. It does not have a hierarchy in the room.

The ratio that reliably works at projection distance is around 2:1. A title at 44 points and body text at 22 points. This feels extreme when you look at it on your laptop at arm's length. It feels correct to the person in the back row.

Robert Bringhurst, thinking carefully about typography, organizes his analysis around *modular scales* — sequences of sizes related by a consistent ratio. The useful ones run from 1.125 up to 2.0. The small ones — 1.125, 1.2 — are for book typography, where the reader is close and contrast accumulates across a full page. The large ones are for display typography, where contrast has to survive distance and angle and imperfect conditions. A projected slide is display typography. Use the large ratios.

| Ratio | Context | example sizes (body at 22pt) |
| --- | --- | --- |
| Bringhurst's modular scale ratios | two | Use the chapter example as the concrete test case. |

There is an important corollary. If you have three type sizes on your slide, each of them has to be doing identifiable work — not *slightly different for visual interest*, but *this size means this level of the hierarchy, full stop*. If you cannot name what each size is for, you have too many sizes. Two sizes — title and body, 2:1 ratio — forces the question in a good way.

---

## Weight: the one-emphasis rule

Weight is what bold does. And bold does something specific: it says *this matters more than the surrounding text*.

Emphasis works by contrast. A word in bold in a paragraph of regular text pops forward. A paragraph in bold in a slide of bold text is just... the normal weight. The emphasis has cancelled itself out.

This sounds obvious when stated plainly. But look at almost any AI-generated slide deck and you will find the body text in semibold, the bullet points in semibold, the subheadings in bold, and the title in bold — a slide with four or five elements all fighting for visual primacy with weight, none winning. The slide is uniformly tense. The eye has nowhere to rest and nothing to prioritize.

The rule that fixes this: emphasis appears at most twice on a slide, and only on elements that the slide's main claim specifically names as important. Not twice as a ceiling you should try to reach. Twice as the absolute maximum, and once is usually better.

There is a version of this failure that arrives through color. A slide with three bullets, two of them in accent colors — one purple, one green — is a slide with two emphasis signals and no signal about what the colors *mean*. The eye sees: *these two are different from the third.* It cannot see why, because the slide never said. The color is spending visual bandwidth on nothing.

Compare: a slide with three bullets, one in bold red, whose headline says *the second cause was load-bearing.* Now the color is answering the headline's question. One cue, one purpose, visible at a glance.

![Emphasis works by scarcity. Spend it twice arbitrarily and it means nothing. Spend it once on what the headline names and it does all the pointing.](images/02-no-clear-hierarchy-fig-03.png)
*Figure 2.3 — Slide mockups illustrating the color-encoding failure and fix*

---

## Proximity: the grouping the eye trusts

Size and weight work on how important something looks. Proximity works on what belongs with what.

The perceptual principle was named by the Gestalt psychologists — Max Wertheimer in 1923 — and every vision science textbook since has confirmed it: elements that are spatially close are read as a group, regardless of what they are. The eye does this before meaning is processed. A bulleted list where the bullets sit tightly together reads as one group. A loose collection of text elements scattered across a slide reads as — well, it doesn't read as anything coherent, because grouping by proximity is what makes structure visible in the first place.

The practical consequence is that white space is not decoration. It is syntax. The gap between your title and your body text is asserting a relationship: *these are different groups.* The gap between your bullet group and your callout box is asserting: *these do not belong to the same idea.* If you tighten or loosen those gaps for aesthetic reasons, you are changing the semantic claims the slide is making, whether you mean to or not.

![White space is not padding — it is punctuation. The gap is making a claim about what belongs together.](images/02-no-clear-hierarchy-fig-04.png)
*Figure 2.4 — The same six slide elements shown twice in*

Here is the grouping error that produces the most common hierarchy failure: a callout box on the side of a slide, with its own bold heading and a border, sitting at roughly the same height as the main title. The visual system sees: *the title and the callout heading are both emphasized, both at eye level, both making claims.* It cannot tell which is primary. The callout often wins — because someone bolded it heavily to make it "stand out," and heavier weight beats title size when the size ratio is already thin.

The fix is not to make the callout look less important. The fix is to ask what the callout is actually *for*. If it carries supporting detail the audience doesn't need during the lecture, it belongs in the notes field. If it carries a fact the argument depends on, it belongs in the body, not in a box competing with the claim.

---

## What hierarchy is really for

I want to pause here on something the technical vocabulary can obscure.

The reason hierarchy matters is not aesthetic. It is not that cluttered slides are ugly and minimal slides are beautiful. The reason is that your audience is doing cognitive work while looking at the slide — they are simultaneously reading, listening to you, and trying to connect what they're seeing to what they already know. Working memory is finite. Every time the eye lands in the wrong place, or has to scan twice to find the entry point, or tries to parse a color that doesn't mean anything — that is cognitive work spent on your design instead of your content.

Cognitive load theory, developed by John Sweller in the late 1980s, distinguishes between intrinsic load (the complexity of the content itself), extraneous load (the cognitive cost imposed by the presentation design), and germane load (the cognitive work of actually learning). A well-designed slide minimizes extraneous load so the available capacity goes to the content. A hierarchy failure is an extraneous load generator. Every ambiguous emphasis decision, every misused color, every poorly spaced group — each is a small tax on attention that the student pays with capacity that should have gone to understanding.

![A hierarchy failure doesn't make the content harder. It fills the wrong bucket and leaves less capacity for learning.](images/02-no-clear-hierarchy-fig-05.png)
*Figure 2.5 — Three-bucket diagram of Sweller's cognitive load model *

This is why the one-second test matters. Ask someone to glance at your slide for one second and tell you what they read. What they report is what your hierarchy says is most important. If their answer matches your intention, the hierarchy is working. If they report the callout trivia while you intended the main claim, the hierarchy is lying about the content — and students will learn the wrong thing, not because the content was hard, but because the slide sent them to the wrong place first.

![The one-second test is not a polish check — it is a factual audit of what your contrast gradients are actually saying](images/02-no-clear-hierarchy-fig-06.png)
*Figure 2.6 — Two-row "one-second test" scorecard *

---

## A concrete example

The same slide, two configurations. The principle is easier to see than to describe.

The bad version has a title: "Three Causes of the 2008 Financial Crisis." A label, not a claim. The title is 32pt semibold; the bullets are 28pt semibold. Ratio: 1.14×. At projection distance: invisible. One bullet is purple. Another is green. There is a callout box titled "Did you know?" in bold, heavier than the main title. The callout says Lehman Brothers was founded in 1850.

Run the one-second test. The eye finds "Did you know?" first — it is the heaviest element on the slide. The student who glances up for a second leaves knowing something about 1850. The slide's actual subject, which of the three causes was the structural one, is not communicated at all.

Now the good version. Title: "MBS leverage was the load-bearing cause." Full sentence. A claim. At 44pt bold, with body text at 22pt regular — ratio 2:1. Three bullets at 22pt regular, except the middle one: "Mortgage-backed security leverage" in bold with a red accent. One emphasis, on the bullet the headline names. The callout is gone; its 1850 fact is in the notes field.

![Same content. Same facts. The left slide teaches 1850. The right slide teaches which cause was structural.](images/02-no-clear-hierarchy-fig-07.png)
*Figure 2.7 — Side-by-side mockup of the two 2008 financial crisis*

One-second test: the eye finds the title, reads a claim, looks for evidence, finds one emphasized bullet confirming it. The student who glances up for a second has the answer.

The biggest change between the two versions was not the size ratio. It was deciding what the title was *for*. Once the title became a claim rather than a label, the questions answered themselves. Which bullet should be emphasized? The one the claim names. What should the color encode? The same thing. The visual hierarchy followed from the rhetorical hierarchy, because that is what visual hierarchy is — the rhetorical structure made visible at the speed of perception.

---

## The prompt

If you are using an AI slide tool and want to fix a hierarchy problem, here is the prompt that addresses the root cause rather than the symptom:

```
Restructure this slide so the visual hierarchy is unmistakable at a
glance. Requirements:

1. The headline is the entry point. Set it at 44pt bold (or whatever
   produces at least a 2.0x size ratio against body text). Rewrite the
   headline as a full-sentence claim if it is currently a topic label.

2. Body text sits at one weight lighter than the headline (regular,
   not bold) and at body size from DESIGN.md. There should be exactly
   two type sizes on this slide: headline and body. Reject any
   intermediate sizes.

3. Accent color appears at most twice on the slide and only on elements
   the headline's claim points to. If you cannot state in one phrase
   what the accent color encodes on this slide, remove the color.

4. Group elements by proximity. Things that belong together sit
   together with tight spacing; groups are separated by visible
   whitespace at least 1.5x the line-height between groups.

5. Move any callout box, sidebar, or "did you know" element to the
   notes field unless the headline's claim explicitly depends on it.

Return the slide as Brutalist HTML with the .slide and .notes structure
preserved.
```

The second requirement is the one that gets resisted most: *but I need three sizes for nuance.* Three sizes is fine when each size does identifiable work. Three sizes that the eye reads as one band — because the ratios are all below 1.5× — is not three sizes. It is visual noise that looks like structure.

---

## Two honest disagreements

Before leaving this chapter, I want to name where two thoughtful people can read everything above and still disagree.

The first is about how aggressive the contrast should be. Reynolds-style slide design — which is close to what I've described here — uses dramatic ratios, one or two type weights, and generous white space. The argument: hierarchy invisible to the back row is hierarchy that didn't happen. Tufte-style technical typography accepts subtler hierarchy: 1.5× ratios, multiple weights, small caps, indentation as a cue. The argument: dense technical content cannot be flattened to keynote sparseness without lying about the structure. Both are right in their domains. Reynolds' approach is for the lecture hall. Tufte's approach is for the journal page. A projected slide is closer to the lecture hall — which is why this book leans toward 2.0× as the default. But if you are projecting a dense technical diagram to specialists who expect to study it closely, the subtler approach may serve better. The vocabulary to use when making this choice: *what is the contrast ratio between my levels, and does the person in the back row see it?* Not *which aesthetic do I prefer?*

The second is about how many type sizes a slide can carry. I've argued for two. A designed system — light for captions, regular for body, semibold for sub-emphasis, bold for headline — can work if each level does identifiable work and the system is applied consistently across every slide in the deck. The failure mode is not four sizes; it is four sizes used inconsistently, so the eye cannot learn the system and has to re-parse each slide from scratch. If you use four sizes, name what each one means, and hold to it every time.

| Dimension | Reynolds | presentation style | Tufte | technical style |
| --- | --- | --- | --- | --- |
| typical size ratio, number of weights used, white space approach, best context, failure mode when misapplied | The pattern becomes easy to misuse or overlook. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. | A concrete checkpoint for applying the chapter concept. |

---

## The diagnostic questions

Five questions, ten seconds. Run any slide through them before it ships.

Where did your eye land first? If it didn't land on the most important element, the hierarchy is wrong.

How many type sizes are on this slide, and can you name what each one is for? More than three, or any you can't name — those are accidental sizes.

What does the accent color encode? If you can't answer in one phrase, the color is decoration and should come off.

Are elements that belong together physically close? Proximity is making a claim; make sure it's the claim you want.

If you removed all the text and looked only at the shapes and weight, would you still see the structure? Hierarchy that survives that test is doing visible work.

![Run this in ten seconds before any slide ships](images/02-no-clear-hierarchy-fig-08.png)
*Figure 2.8 — Vertical checklist card titled "The five-question audit" *

---

Once the hierarchy is clear, the next problem is different: the slide may have the right structure and still carry too much. Chapter 3 is about that — the decision of what to cut, and what happens to the cut material when it doesn't go in the trash but has somewhere else to go.

---

**What would change my mind:** A controlled study showing that subtle typographic hierarchy (1.2× ratios, multiple weights) produces equivalent recall and comprehension to dramatic hierarchy (2×+ ratios, two weights) for projected lecture slides in actual classroom conditions. The literature supports the Signaling Principle generally but does not finely partition by hierarchy-aggression. If evidence arrives on the subtle-hierarchy side, the default ratio in this chapter should be revised downward.

**Still puzzling:** I do not have a clean rule for when an intermediate type size earns its place. Two sizes plus careful weight variation handles almost every slide I've seen. The case for a third size — a sub-headline, a caption tier — is intuitively real, but the empirical work isolating its value against the cost in visual complexity is, to my reading, thin.

---

### LLM Exercises

**Exercise 1 — Hierarchy audit**
Paste any slide you have built recently into an LLM with this prompt: *"Look at this slide. Without reading its content, describe where my eye would land first, second, and third. Then tell me whether that order matches a coherent hierarchy from most to least important."* Compare the LLM's reading order to your intended reading order. Where they diverge, diagnose which of the three forces — size, weight, or proximity — is producing the mismatch.

**Exercise 2 — The ratio check**
Take a slide where the hierarchy feels weak. Ask an LLM: *"The title of this slide is [N]pt bold. The body text is [M]pt semibold. Given that the slide will be projected in a lecture hall, is this ratio sufficient for the eye to parse title and body as different hierarchy levels? What ratio would you recommend, and why?"* Then apply the recommendation and run the one-second test on a colleague.

**Exercise 3 — Color encoding**
Find a slide in your current deck that uses accent colors on more than one element. Paste it to an LLM with this prompt: *"List every element on this slide that is colored, bolded, or otherwise visually emphasized. For each one, state in a single phrase what the emphasis is encoding — what question it is answering. If you cannot state a purpose, flag it."* Use the flagged items to decide what comes off the slide.

**Exercise 4 — Callout surgery**
Take a slide with a callout box, sidebar, or bordered "did you know" element. Ask an LLM: *"The headline of this slide claims [X]. The callout box contains [Y]. Evaluate: does the callout support the headline's claim directly enough to stay on the live-deck slide, or does it belong in the notes field? Explain the hierarchy fight the callout is creating and what resolves it."*

**Exercise 5 — Rebuild from claim**
Give an LLM a topic-label title and a set of bullets: *"Rewrite this slide so the title is a full-sentence claim that identifies the most important bullet. Then restructure the bullets so the one the title names is visually distinct (bold, accent color, or both) and the others are regular weight. Use a 2:1 size ratio between title and body. Return the result as plain text with formatting described in brackets."* Compare the rebuilt slide against the original and name what changed in the hierarchy and why.

---

## Tier Connection

Hierarchy is the chapter where the **Tier 1 / Tier 4 split** becomes visible at the level of a single slide. The AI renders the size, weight, and proximity contrasts you specify (Tier 1 — pattern execution). It cannot decide *which element is most important* (Tier 4 — interpretive judgment). The model produces a slide where every element looks equally finished because it has no signal for what matters. The instructor supplies the signal.

The **phase gate** sits at the priority decision: before any layout prompt, you decide what the eye should land on first, second, third. The prompt encodes that decision. The system executes against it. A hierarchy that ranks wrong is not a rendering failure — it is a phase-gate failure where the priority decision was implicit and the system filled it in with a default. See *Appendix A — The Fundamental Themes*.

**Tags:** typographic-hierarchy, Mayer-signaling, Gestalt-proximity, Bringhurst-modular-scale, contrast-ratio, cognitive-load

## Prompts

Use these prompts with Claude to generate interactive D3 v7 versions of the
figures in this chapter. Each produces a standalone HTML file you can open
in a browser and modify freely.

**Prerequisites:** Load `brutalist/CLAUDE.md` and `brutalist/DESIGN.md` into
your Claude project context before using these prompts. They define the stack,
naming conventions, color system, and typography the figures use.

---

### Figure 2.1 — Simplified schematic of the visual pathway from retina

Create a standalone D3 v7 HTML file for a left-to-right flow diagram titled "Simplified schematic of the visual pathway from retina". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-01.html`

---

### Figure 2.2 — Strip showing the same five slide elements arranged

Create a standalone D3 v7 HTML file for a concept map titled "Strip showing the same five slide elements arranged". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-02.html`

---

### Figure 2.3 — Slide mockups illustrating the color-encoding failure and fix

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "Slide mockups illustrating the color-encoding failure and fix". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-03.html`

---

### Figure 2.4 — The same six slide elements shown twice in

Create a standalone D3 v7 HTML file for a concept map titled "The same six slide elements shown twice in". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-04.html`

---

### Figure 2.5 — Three-bucket diagram of Sweller's cognitive load model

Create a standalone D3 v7 HTML file for a trajectory or spectrum chart titled "Three-bucket diagram of Sweller's cognitive load model". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-05.html`

---

### Figure 2.6 — Two-row "one-second test" scorecard

Create a standalone D3 v7 HTML file for a ranked or grouped bar chart titled "Two-row "one-second test" scorecard". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-06.html`

---

### Figure 2.7 — Side-by-side mockup of the two 2008 financial crisis

Create a standalone D3 v7 HTML file for a side-by-side comparison diagram titled "Side-by-side mockup of the two 2008 financial crisis". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-07.html`

---

### Figure 2.8 — Vertical checklist card titled "The five-question audit"

Create a standalone D3 v7 HTML file for a checklist card diagram titled "Vertical checklist card titled "The five-question audit"". Use the chapter idea as the data: slide design decision, visual evidence, reader attention, cognitive load, and learning outcome. Encode the primary claim with one red mark and all supporting marks with neutral ink. Include direct labels, a zero baseline if quantitative values are shown, short annotations, accessible SVG title and description, responsive redraw with ResizeObserver, dark-mode CSS variables, and reduced-motion handling. Use the D3 7.9.0 CDN and inline CSS/JS only.

> Reference implementation: `d3/02-no-clear-hierarchy-fig-08.html`
