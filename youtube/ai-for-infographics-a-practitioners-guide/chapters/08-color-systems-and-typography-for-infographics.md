# Chapter 8 — Color Systems and Typography for Infographics

## Opening: The figure that passed design review and failed everyone

The file came back from review with a green checkmark. A public-health team had built an infographic on county-level vaccination coverage: a choropleth-style panel of bars, one per county, with a soft gradient running from pale yellow at the low end to a confident teal at the high end, and a single coral bar pulled out to mark the county under discussion. It was, by any aesthetic standard, a handsome figure. The reviewer who approved it said it "looked clean and modern." It went into the slide deck.

Then a second reviewer ran it through a contrast checker — the same WCAG check you will run in this chapter — and two things happened. First, the pale-yellow labels against the white canvas measured a contrast ratio of about 1.9:1, well under the WCAG 2.2 minimum of 4.5:1 for normal text [High]. A reader with low vision could not read the low-coverage counties at all — which is to say, the figure hid exactly the counties a public-health audience most needed to see. Second, when the figure was printed in grayscale for a briefing packet, the yellow-to-teal gradient collapsed into a nearly uniform mid-gray. The encoding that carried the entire quantitative message disappeared the moment color was removed.

Neither failure was visible on the screen of the person who approved it. Both were structural. And both trace to the same mistake: color and typography were treated as *decoration applied to a finished figure* rather than as *the channels that carry the figure's meaning*. This chapter is about refusing that mistake. You will learn to deploy color as a semantic system governed by seven tokens, and typography as hierarchy rather than style — and to verify both with checks that do not depend on your own eyesight or taste.

The spine of the book runs straight through here. Whether a yellow is "pretty" is not a judgment any tool can make wrong; whether a yellow *encodes* low vaccination coverage in a way a colorblind reader on a grayscale printout can still decode is a perceptual-accuracy decision, and it is irreducibly human. AI will write the `fill="#C8860E"`. It will not tell you that ochre must never carry data.

## Core content

### Color is a channel, not a coat of paint

In Chapter 6 you learned Cleveland and McGill's channel hierarchy and the two-data-encoding-color limit. This chapter operationalizes it. The governing idea, which you should be able to defend in a review, is that **color in an infographic is a perceptual channel that encodes meaning, and every use of color either carries information or competes with it.** There is no neutral third category. A color that does not encode anything is not "neutral background interest"; it is noise that the reader's pre-attentive visual system must process and discard.

This is why the Brutalist system constrains color so aggressively. The constraint is not an aesthetic preference for restraint — it is a direct consequence of the perceptual science from Chapter 2. The visual system is exquisitely fast at detecting a single salient hue against a uniform field (pre-attentive pop-out) and progressively worse at separating many hues at once. Every additional data-encoding color you introduce degrades the reader's ability to use any of them. The Brutalist commitment to exposed structure and functional marks translates, in the color layer, to a hard rule: **two data-encoding colors maximum before you switch to a secondary encoding** (pattern, direct label, or figure decomposition) [High, per the design system].

### The seven-token system, deployed by role

The Brutalist design system you built in Chapter 5 specifies exactly seven color tokens. In production they live in DESIGN.md and are never hardcoded as loose hex values scattered through a file. The discipline matters: when color is a named token with a stated role, a reviewer can audit a figure by asking "is this token being used for its role?" rather than "do I like this shade of red?"

| Token | Hex | Role | Allowed use | Prohibited use |
|---|---|---|---|---|
| `--color-white` | `#FFFFFF` | Canvas | SVG background | Chart plot region (use fill instead) |
| `--color-ink` | `#2a1a0e` | Primary text & structure | Headings, axes, body, structural strokes, secondary data category | Decorative fills |
| `--color-red` | `#C8102E` | Primary accent | The one highlighted data category; brand emphasis | More than one data category in a figure; encoding "danger" or negative values |
| `--color-secondary` | `#545454` | Supporting text | Captions, axis labels, source lines | Primary headings; data encoding |
| `--color-border` | `#D4D4D4` | Hairlines | Grid lines, dividers, box borders | Text; data encoding |
| `--color-ochre` | `#C8860E` | Decorative accent | Callout borders, figure-label accents | **Any data encoding, ever** |
| `--color-fill` | `#F5F5F5` | Chart area | Plot-region background | Text; data encoding |

Three rules in that table do the heavy editorial lifting. First, **ochre is never a data-encoding color.** It exists to mark the apparatus of the figure — a callout border, a label tab — not the data. The moment ochre encodes a value, the reader loses the ability to tell structure from signal. Second, **red is the single accent.** A Brutalist figure highlights *one* thing in red; if two categories are both red, neither is emphasized. Third, **red does not mean danger.** It is the primary brand accent and the primary data series. Using it to flag negative or alarming values smuggles an editorial judgment into what looks like a neutral color choice — exactly the kind of "true data, misleading structure" failure from Chapter 1.

![Seven color tokens listed with their roles, ochre flagged structure-never-data, beside a luminance ladder showing red as a distinct dark step](images/08-color-systems-and-typography-for-infographics-fig-01.png)

*Figure 8.1 — The seven tokens deployed by role, with ochre flagged "structure, never data" and a luminance ladder showing the single red accent survives grayscale conversion as a distinct dark step.*

### Categorical, sequential, emphasis: matching color type to data type

When you reach for color, first classify what you are encoding [High]:

- **Categorical** (distinct, unordered groups — county A vs. county B): use *position and direct labels first*; reserve color for the single category you are highlighting. The seven-token system gives you red for the highlight and ink/neutral grays for the rest. If you have more than two categories that genuinely need to be distinguished by color, the figure is over-loaded — split it or use a secondary encoding.
- **Sequential** (ordered magnitude — low to high coverage): a single-hue luminance ramp reads as ordered because the visual system reads *luminance* as quantity reliably, while it reads *hue* as category. The vaccination figure failed precisely because it ramped *hue* (yellow→teal) instead of luminance. A defensible sequential encoding within this system uses luminance steps of a single token, verified on the luminance ladder.
- **Emphasis** (one element matters more than the rest): this is what red is for. One red mark on a field of ink and gray.

The discipline here is that you select the color *type* from the structure of the data, not from a palette you find attractive. This is the FT Visual Vocabulary principle from Chapter 6 applied to color: start from the relationship, not the form.

### The grayscale test and the luminance ladder

The single most useful color check you can run costs nothing and requires no tool beyond desaturation: **convert the figure to grayscale and ask whether the encoding survives.** If two data categories collapse into the same gray, they were distinguished only by hue, and any reader who is colorblind, printing in monochrome, or viewing on a bad projector cannot decode them [High].

The luminance ladder is the proactive version of the same idea. Before you assign colors, lay your data-encoding colors out by luminance value and confirm they form distinguishable steps in grayscale. The seven tokens are designed so that ink (`#2a1a0e`, very dark), the neutral grays (`#787878`, `#ADADAD`), and the chart fill (`#F5F5F5`, very light) form a clean luminance ladder even before any hue is involved. Red (`#C8102E`) sits at a mid-dark luminance that reads as distinct from ink — which is why a single red accent survives grayscale conversion as "the dark one that isn't quite black."

### Opacity does not stack the way you think

A production failure that AI code generators reproduce constantly: opacity compounds. If you set `opacity="0.5"` on a group and then `fill-opacity="0.5"` on a rectangle inside it, the rectangle does not render at 50% — it renders at 25%, because the two multiply (0.5 × 0.5) [High]. A label you intended to soften becomes invisible. The Brutalist rule is to **avoid opacity for encoding entirely.** If you need a lighter mark, use a lighter token (`#ADADAD` instead of ink at 0.5 opacity). Tokens are auditable and grayscale-stable; opacity is neither, and it stacks silently through the SVG group hierarchy.

### Typography is hierarchy, not style

Typography in an infographic is not "which font looks nice." It is the mechanism by which a reader knows, before reading a single word, what to read first. The three-font stack from Chapter 5 assigns each font family a *role*, and the role — not the designer's taste — determines what is set in what.

| Role | Font family | Size | Weight | Fill |
|---|---|---|---|---|
| Figure title / display | `'EB Garamond', Georgia, serif` | 14 | 400 | `#2a1a0e` |
| Body / item label | `'Inter', -apple-system, sans-serif` | 12 | 400 | `#2a1a0e` |
| Caption / sub-label | `'Inter', -apple-system, sans-serif` | 11 | 400 | `#545454` |
| Axis tick labels | `'JetBrains Mono', monospace` | 11 | 400 | `#545454` |
| Source / ALL CAPS identifier | `'Inter', -apple-system, sans-serif` | 10 | 400 | `#545454` |

The editorial weight rides on the role assignments. **EB Garamond** carries display authority — the figure title and section headers, nothing else; a serif title signals "this is the editorial voice." **Inter** carries the body and labels — the workaday reading layer. **JetBrains Mono** carries numbers on axes, because a monospace face aligns digits into columns, so `1,204` and `987` line up by place value and the reader can compare them by length, reinforcing the position channel. Using a proportional font for axis ticks breaks that alignment and quietly degrades the reader's ability to compare quantities. The font choice is, again, a perceptual decision wearing the costume of a style decision.

Notice that the fills come straight from the color tokens. Supporting text — captions, axis labels, source lines — is set in `--color-secondary` (`#545454`), not ink. That single luminance step down is doing hierarchy work: it tells the reader "this is apparatus, not the main claim" without a single word of instruction.

![Four type roles stacked by size and weight: a red display title, Inter body, monospace aligned digits, and a grey caption one luminance step down](images/08-color-systems-and-typography-for-infographics-fig-02.png)

*Figure 8.2 — The three-font stack assigned by role: EB Garamond carries the display title (red), Inter the body, JetBrains Mono the aligned axis digits, and the grey caption sits one luminance step down to read as apparatus.*

### Two export bugs that destroy typographic intent

Two failures appear when D3-generated SVG meets Illustrator, and you will meet both in Act Three. They belong here because they are *typographic* failures.

The **`text-anchor` export mismatch**: in SVG, `text-anchor="middle"` centers text on its anchor point, and D3 relies on this for centered labels. When Illustrator imports the file and you save it back out, Illustrator may *bake the alignment into baked coordinates* and drop the `text-anchor` attribute. The text still looks centered in that one export, but the moment anyone edits the label length, it no longer recenters — the semantic alignment is gone, replaced by a frozen position [Medium, verify against current Illustrator behavior — system specifics].

The **`<tspan>` whitespace collapse**: multi-line labels built from `<tspan>` elements can lose their intended spacing when whitespace between tspans is collapsed on import, jamming two lines together or losing a leading space [Medium, verify]. Both bugs share a lesson: typographic intent that is *computed* (centered, spaced) is fragile across the handoff, while typographic intent that is *structural* (the right font family, the right size token) survives. Specify roles, not one-off tweaks.

## Worked example: rebuilding the vaccination figure

**Problem statement.** County-level vaccination coverage, twelve counties, one (Marion County) under discussion. The brief: show how Marion compares and make the low-coverage counties legible.

**First attempt (specification-less AI output).** Prompted with "make an infographic of vaccination coverage by county, make it look modern," a coding agent produced: a yellow→teal sequential gradient across all twelve bars, Marion in coral, county labels in a thin light-gray sans at 10px, a white plot region, and a decorative ochre underline beneath the title that also tinted the highest bar. Plausible. Pretty. Wrong on at least four counts.

**Design diagnosis.**
1. *Hue-ramp for ordered data.* The yellow→teal gradient encodes magnitude in hue, which the visual system reads as category. Violates the sequential-encoding rule; fails the grayscale test (collapses to uniform gray).
2. *Coral highlight is a second red-family accent that is not a token.* Marion should be the single `--color-red` accent; coral is an un-auditable off-palette color.
3. *Ochre tinting a data bar.* The decorative underline bled ochre onto the highest-coverage bar — ochre is encoding "highest," which is prohibited.
4. *Contrast failure.* 10px light-gray county labels on white measured ≈1.9:1; below WCAG 4.5:1.

**Corrected version (specification-driven).** Apply the tokens by role:
- All twelve bars in `--color-ink` (`#2a1a0e`), *except* Marion in `--color-red` (`#C8102E`). One accent, one highlight. Magnitude is read from bar *length* (position on a common scale — the top of Cleveland–McGill), not from color at all. Color now does exactly one job: "this is Marion."
- County labels in `--color-ink` at the Inter body role (12px), not light gray. Axis ticks (coverage %) in JetBrains Mono at `--color-secondary`.
- Plot region `--color-fill` (`#F5F5F5`), canvas white. Title in EB Garamond. Source line in the ALL CAPS Inter role with `letter-spacing="0.08em"`.
- No gradient. No ochre on data. A single ochre callout border may bracket Marion's annotation tab — decorative, structural, not encoding.

**Verification.** Grayscale conversion: bars remain readable by length; Marion remains distinguishable because red's luminance differs from ink's. WCAG check: ink-on-white labels measure well above 4.5:1; secondary-on-white axis text measures above 4.5:1 [verify exact ratios at production].

**The lesson.** Move the quantitative message from color (a weak, fragile channel) onto position (the strongest channel), and reserve color for the single editorial emphasis the figure exists to make.

**The limit.** A tool can apply the seven tokens once you tell it the roles. It cannot decide that *Marion* is the county worth one red accent, or that low-coverage legibility is the accessibility constraint that governs this figure. Those are the human-judgment decisions your AI Use Disclosure will name.

## AI Wayback Machine: Cynthia Brewer and the color you can trust

Long before "design tokens" were a phrase, the cartographer **Cynthia Brewer** confronted exactly this chapter's problem: mapmakers were choosing color schemes that looked good and read wrong — sequences that reversed under colorblindness, schemes that collapsed in grayscale, palettes where the eye could not tell which class was "more." Her response was ColorBrewer, a tool that classifies color schemes as sequential, diverging, or qualitative and flags which are colorblind-safe and print-safe [High]. (Wayback targets: Wikipedia "ColorBrewer"; bio "Cynthia Brewer.")

What Brewer institutionalized is the move this chapter asks of you: treat color as a *typed, testable system* rather than an aesthetic free-for-all. Sequential data gets a sequential (luminance-ordered) scheme; categorical data gets a qualitative scheme; and every scheme is checked against the readers who do not see what the designer sees.

> **Prompt to try:** "Explain how Cynthia Brewer's ColorBrewer work helps an engineer avoid a polished but indefensible infographic — specifically, how the sequential/diverging/qualitative distinction maps onto a seven-token Brutalist palette."

The throughline: Brewer's lineage tells you that the discipline of color-as-system is not a Brutalist invention. It is what serious visual communicators have done for decades, because the eye that approves a figure on screen is not the only eye that will read it.

## Assessment — Reading Response #5 (30 pts)

Find a published infographic in a domain you know (public health, climate, finance — your choice) that uses at least three data-encoding colors. In 600–800 words:

1. **Classify** each color use as categorical, sequential, or emphasis, and state whether the color *type* matches the *data type* it encodes (10 pts).
2. **Run the grayscale test** (desaturate a screenshot) and report which encodings survive and which collapse. Run a WCAG contrast check on the two lowest-contrast text elements and report the ratios against the 4.5:1 threshold (12 pts).
3. **Re-specify** the figure under the seven-token system: state which single element earns `--color-red`, why ochre appears nowhere in the data, and how you would move at least one color-borne message onto a stronger channel (8 pts).

Attach an **AI Use Disclosure** naming at least two decisions in your re-specification that required your judgment and that an AI tool could not have supplied (e.g., *which* element deserves the single accent; *which* accessibility constraint governs this audience).

## Bridge

Color and typography carry the figure's *meaning* and its *hierarchy*. But meaning and hierarchy are not the same as *explanation* — the sentence that tells the reader what the highlighted bar actually implies. That explanatory layer is annotation, and annotation is where more infographics are won and lost than anywhere else. Chapter 9 asks the hardest question in the design system: when does a piece of text on a figure earn its place — and when is it just clutter wearing the costume of helpfulness?

## Sources

- W3C Web Accessibility Initiative. *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C Recommendation, 2023. Authoritative source for the 4.5:1 contrast minimum for normal text. [Verify access date at production; version-sensitive.]
- Brewer, Cynthia. *ColorBrewer 2.0.* Pennsylvania State University. Sequential/diverging/qualitative classification and colorblind/print-safe flags. [Verify exact page title before Wayback citation.]
- Stone, Maureen. *A Field Guide to Digital Color.* A K Peters, 2003. Applied reference for luminance, contrast, and display constraints.
- Lupton, Ellen. *Thinking with Type.* Princeton Architectural Press, 2010 (and later editions). Typographic hierarchy, role, and discipline.
- Ware, Colin. *Information Visualization: Perception for Design.* 4th ed. Morgan Kaufmann, 2020. Perceptual basis for luminance-as-quantity and hue-as-category claims.
- Cleveland, William S., and Robert McGill. "Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods." *Journal of the American Statistical Association*, 1984. Channel hierarchy underlying the position-over-color argument.
- Brutalist Design System (this book, Chapter 5; `pantry/cajal-svg-generator.md`). The seven color tokens, three-font stack, and stroke conventions as a production specification.
