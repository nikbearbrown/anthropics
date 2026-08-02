# Chapter 5 — The Brutalist Design System

## Opening: A figure that explains itself

On the studio wall there is a single infographic — a demographic chart showing the shift in median first-marriage age across five decades — and around its edges, in a thin hand, every decision is annotated with the rule that produced it. An arrow from the headline reads *EB Garamond, 14pt, ink #2a1a0e*. An arrow from the one red line reads *the only accent; one data category per figure*. An arrow from the gray plot field reads *fill #F5F5F5, never white — bounds the data space from the canvas*. An arrow from a faint dashed horizontal reads *border #D4D4D4, 0.75 stroke, reference line*.

A student looks at it and says the thing the wall is designed to provoke: "So none of this is taste."

Correct. Almost none of it. That is the entire claim of the Brutalist design system. A Brutalist building exposes its structure — the concrete is the wall *and* the statement that this is concrete. A Brutalist infographic does the same: every visible mark either encodes data or carries structure, and nothing is present merely to be pretty. The system you are about to learn is not a mood board. It is a small set of named constraints, each with an allowed use, a prohibited use, and a verification check — so that the question "is this right?" has an answer that survives a skeptical review instead of dissolving into "I liked it better the other way." [High]

The payoff is concrete and immediate: by the end of this chapter you can paste the whole specification into a `DESIGN.md` file and hand it to Claude Code as the visual constitution for everything you generate. The design intelligence stays human; the execution becomes mechanical. That division is the spine of the book, and here it gets its first fully operational form.

## Why constraints, and why these

A design token is a named value with a job. `--color-red` is not "that nice crimson"; it is "the one accent, the primary data series, brand emphasis — and nothing else." Naming a value and fixing its role does two things at once. It makes production *consistent*: every figure in a deck uses the same red for the same reason. And it makes production *auditable*: a reviewer — or a verification script, or you in six months — can check whether a mark is doing the job its token allows, instead of relitigating the aesthetics each time. [High]

There is a real failure mode to name, because the research file flags it and the chapter would be dishonest without it: **token systems can ossify.** A rule that is right for ninety figures can be wrong for the ninety-first, where the domain meaning, the accessibility requirement, or the publication's house style genuinely demands an exception. The system is a default, not a cage. The discipline is that you *break a rule on purpose and say why* — that exception is exactly the kind of human-judgment decision the AI Use Disclosure exists to capture — rather than drifting away from the system because you forgot it was there. [Medium]

## The seven color tokens

Seven tokens. Memorize the roles, not just the hex values, because the role is what gets enforced. Write the hex values directly into SVG attributes — static SVG does not reliably resolve CSS custom properties across the export boundary, so the production file carries literal hex. [High]

![A spec board showing the seven color-token swatches with hex and role (red marked the single accent, ochre marked never-data), the three-font type stack, and an 8px spacing grid — the figure rendered in the very system it documents.](images/05-the-brutalist-design-system-fig-01.png)

*Figure 5.1 — The seven-token spec board: the system shown as its own legend, with red marked as the single permitted accent and ochre marked as decorative-only, never data.*

| Token | Hex | Role | Allowed use | Prohibited use |
|---|---|---|---|---|
| `--color-white` | `#FFFFFF` | Canvas | SVG background | Plot-region fill (use `--color-fill`) |
| `--color-ink` | `#2a1a0e` | Primary text / dark anchor | Headings, axes, structural strokes, body copy; a second neutral data category | — |
| `--color-red` | `#C8102E` | Primary accent | The one highlighted data series; brand emphasis | More than one data category per figure; encoding danger/negative states |
| `--color-secondary` | `#545454` | Supporting text | Captions, axis labels, source lines | Encoding a data category |
| `--color-border` | `#D4D4D4` | Hairlines | Grid lines, dividers, box borders | Encoding a data category |
| `--color-ochre` | `#C8860E` | Decorative accent | Callout borders, pull-quote rules, figure-label accents | **Any** data encoding; body text |
| `--color-fill` | `#F5F5F5` | Chart area | Plot-region background | The canvas (that is white's job) |

Three rules carry most of the weight:

- **Red is the only active color, and it carries at most one data category per figure.** When a second category is unavoidable, the partner is ink (`#2a1a0e`) or a neutral gray (`#787878`, `#ADADAD`) — never a second hue. Two data-encoding colors is the ceiling; beyond that you reach for a *secondary encoding* (pattern, direct labels, figure decomposition) rather than a third color. That ceiling is not arbitrary — it is Cleveland and McGill's channel hierarchy operationalized, which Chapter 6 develops in full: hue is a low-accuracy channel, so the system rations it. [High]
- **Ochre is never a data-encoding color.** It is the one warm decorative note — a callout border, a figure-label flourish. The instant ochre encodes a value, the system is broken, because a reader cannot tell "decorative warm" from "meaningful warm" and the figure has started lying with color. [High]
- **Red does not mean danger.** This trips up everyone with a web-dashboard reflex. In this system red is brand and primary series only; it does not encode negative values, alerts, or stop-states. A falling line is not red because it is falling. [High]

### The luminance ladder and the grayscale test

Color that survives only in color is not a design decision; it is a gamble on the reader's monitor, eyesight, and printer. The Brutalist commitment to *honest material* shows up here as a test you can run on any figure: convert it to grayscale and confirm every data-encoding mark still separates.

The tokens are spaced deliberately along the lightness (L\*) axis so they ladder cleanly in gray:

| Token | Hex | Approx. L\* | Role |
|---|---|---|---|
| `--color-ink` | `#2a1a0e` | ~11 | Dark anchor / primary text |
| `--color-secondary` | `#545454` | ~36 | Label text |
| `--color-red` | `#C8102E` | ~43 | Primary data accent |
| `--color-ochre` | `#C8860E` | ~61 | Decorative only |
| `--color-border` | `#D4D4D4` | ~85 | Hairlines |
| `--color-fill` | `#F5F5F5` | ~97 | Near-white field |
| `--color-white` | `#FFFFFF` | ~100 | Canvas |

Notice that red sits at L\* ≈ 43 and ink at L\* ≈ 11 — a gap of roughly thirty points, more than enough that a red series and an ink series stay distinct in grayscale. If two data colors ever land in the same luminance band, the grayscale test fails and you add a secondary encoding *before* proceeding. Ink (≈16.8:1 against white) clears WCAG's strictest AAA bar (7:1) with room to spare; the contrast math is Chapter 8's subject, but the ladder is where it starts. [Medium — L\* values are approximate; verify against a measured conversion if precise reproduction matters]

## The typography stack

Three families, each with one job. Hierarchy comes from *role and weight*, not from a drawer full of fonts. Always write the full fallback chain — never a bare `Arial` or `system-ui`, because the fallback is what renders when the primary face is missing, and an unspecified fallback is an uncontrolled variable.

| Role | Font family | Size | Weight | Fill |
|---|---|---|---|---|
| Figure title / display heading | `'EB Garamond', 'Garamond', Georgia, serif` | 14 | 400 | `#2a1a0e` |
| Body / item label | `'Inter', -apple-system, 'Helvetica Neue', sans-serif` | 12 | 400 | `#2a1a0e` |
| Caption / sub-label | `'Inter', -apple-system, 'Helvetica Neue', sans-serif` | 11 | 400 | `#545454` |
| Axis tick labels | `'JetBrains Mono', 'Fira Code', 'Courier New', monospace` | 11 | 400 | `#545454` |
| Source / ALL-CAPS identifier | `'Inter', -apple-system, 'Helvetica Neue', sans-serif` | 10 | 400 | `#545454` |

The discipline behind the table:

- **EB Garamond is display only** — chart titles and section labels inside a figure. It is never an axis tick, a body label, or a caption. A serif on an axis is the most common token violation in AI-generated figures, because generators reach for "elegant" without role. [High]
- **Inter is the workhorse** — every label, caption, legend entry, and annotation. When you need a heavier header inside a component, you bump Inter to 600–700 rather than switching families. Weight is the hierarchy lever; family is not.
- **JetBrains Mono is for numbers on axes** — its monospacing keeps tick labels vertically aligned, which is the whole point. It is never a display heading.
- **ALL-CAPS source lines** get `letter-spacing="0.08em"` so the caps breathe.

## The spacing grid and stroke conventions

The layout grid is **8px**. Margins, label baselines, and box edges land on multiples of 8. A figure has a **32px margin on all sides**; default chart margins inside that are top 48 / right 40 / bottom 56 / left 64, widening the left to 160 when labels are long. The plot region is filled with `#F5F5F5`, not white, so the data space is visibly bounded from the canvas — a small move that does real perceptual work, separating "where the data lives" from "the page."

Strokes are specified, not improvised:

- Box borders: `stroke="#D4D4D4"` `stroke-width="1"` `fill="#FFFFFF"`
- Chart-area border: `stroke="#D4D4D4"` `stroke-width="0.75"` `fill="#F5F5F5"`
- Arrows: `stroke="#2a1a0e"` `stroke-width="1.5"` `fill="none"`, with a `marker-end` defined once in `<defs>`
- Reference lines: `stroke-dasharray="5 4"` for primary (mean, median, baseline), `stroke-dasharray="2 4"` for secondary
- No shadows. No gradients. No rounded corners (`rx="0"`). No glassmorphism.

The arrowhead is defined once and referenced, which is both efficient and a structural-honesty move — one definition, many uses:

```svg
<defs>
  <marker id="arrow" markerWidth="8" markerHeight="6"
          refX="7" refY="3" orient="auto">
    <polygon points="0 0, 8 3, 0 6" fill="#2a1a0e"/>
  </marker>
</defs>
```

The prohibitions are the Brutalist commitments in operational form. No shadows, no gradients, no rounded corners — because each of those is a non-encoding visual mark, decoration that adds ink without adding meaning. The aesthetic *is* the cognitive-science argument from Chapter 3, written as a list of things you do not do.

## Worked example: the DESIGN.md block

Here is the failure-first contrast the research calls for. Give a coding agent the brief *"make a clean chart of first-marriage age over time"* with no system prompt, and you get a plausible figure that fails on inspection: a gradient fill behind the bars (prohibited), a teal-and-orange two-hue palette (red is the only accent), Times on the axis ticks (monospace only), a pure-white plot region (should be `#F5F5F5`), and rounded bar corners (`rx="0"` required). Five token violations, none visible as *wrong* to an eye that has not internalized the system — which is exactly why surface polish cannot be trusted.

Now the same concept, generated against a specification. This is the block you paste into `DESIGN.md`:

```markdown
## Color tokens (write hex directly into SVG)
--color-white   #FFFFFF  canvas / svg background
--color-ink     #2a1a0e  text, axes, structural strokes; neutral data cat. 2
--color-red     #C8102E  the one accent; ONE data category per figure
--color-secondary #545454 captions, axis labels, source lines (never data)
--color-border  #D4D4D4  grid lines, dividers, hairlines (never data)
--color-ochre   #C8860E  decorative accent ONLY — never data encoding
--color-fill    #F5F5F5  plot-region background (never the canvas)
Max two data-encoding colors (red + neutral gray); else secondary encoding.
Grayscale test required: every data mark must separate without color.

## Typography (full fallback chains; role = hierarchy)
Display title  'EB Garamond','Garamond',Georgia,serif        14 / 400 / #2a1a0e
Body label     'Inter',-apple-system,'Helvetica Neue',sans   12 / 400 / #2a1a0e
Caption        'Inter',-apple-system,'Helvetica Neue',sans   11 / 400 / #545454
Axis ticks     'JetBrains Mono','Fira Code',monospace        11 / 400 / #545454
Source / CAPS  'Inter',-apple-system,sans                    10 / 400 / #545454  ls 0.08em
EB Garamond = display only. JetBrains Mono = ticks only.

## Spacing & strokes
8px grid. 32px outer margin. Chart margins 48/40/56/64 (wide-label left 160).
Plot fill #F5F5F5. Borders #D4D4D4. Arrows ink 1.5, marker-end from <defs>.
rx="0". No shadows, gradients, rounded corners.
```

| Rule / token | Role | Allowed use | Prohibited use | Verification check |
|---|---|---|---|---|
| `--color-red` | Primary accent | One data series; emphasis | A second category; danger coding | Count hues encoding data ≤ 1 red |
| `--color-ochre` | Decorative | Callout borders | Any data value | Confirm ochre touches no datum |
| `--color-fill` | Plot field | Plot background | The canvas | Plot region is `#F5F5F5`, not white |
| EB Garamond | Display | Titles | Axis ticks, body | No serif on ticks/labels |
| 8px grid | Layout | Margins, baselines | Off-grid placement | Snap-check baselines to multiples of 8 |
| Grayscale | Color safety | All figures | — | Desaturate; data marks still separate |

The lesson, in one sentence: **a design system is the difference between a figure you like and a figure you can defend.** [High]

The limit, in one sentence: the system tells you *how* red behaves once you have decided red belongs here — but the decision that *this* series is the one worth the accent, and that the ninety-first figure earns its documented exception, is judgment the tokens cannot make for you.

## Assessment — Reading Response #3 (30 points)

**Title: "Roles, Not Colors."**

Write a 600–900-word response that does three things:

1. Explain the role of each of the seven color tokens, and argue in your own words why ochre is barred from data encoding while red is barred from carrying more than one data category. Connect at least one of these rules to a perceptual claim from Chapter 2 (the rationing of hue is the obvious candidate). [Understand → Analyze]
2. Take a candidate figure — yours or a provided one — and run the grayscale test in prose: name each data-encoding mark, give its token and approximate luminance band, and state whether the figure passes or where it collapses. [Apply → Evaluate]
3. Identify one place where you would *break* a system rule for a real domain or publication reason, and justify the exception in language that would survive a skeptical review.

Close with an **AI Use Disclosure** naming at least two judgment decisions you made that an AI could not have made for you — for instance, choosing which series deserved the red accent, or deciding that a specific exception was warranted.

Deliverable: a 600–900-word response with the grayscale walk-through and a completed AI Use Disclosure. (30 points)

## AI Wayback Machine — Ellen Lupton

> **Why a typographer anchors a chapter about tokens.** Ellen Lupton's *Thinking with Type* made an argument that this whole chapter rests on: that typography is not decoration applied to content but a *system of roles* — a hierarchy of function in which a heading, a caption, and a footnote each do a distinct job, and the job determines the form. Lupton taught a generation of designers to ask "what is this text *doing*?" before asking "what should it look like?"
>
> That is exactly the move the token table makes. EB Garamond is not "the pretty one"; it is the display role, and the role forbids it from the axis. Inter is not "the plain one"; it is the workhorse role, and weight — not family — carries its internal hierarchy. Lupton's lesson, transposed from type to color and spacing, *is* the design-token discipline.
>
> Try this prompt with an AI assistant: *"Explain how Ellen Lupton's idea of typographic hierarchy as a system of roles helps an engineer build a design-token specification that an AI can execute but cannot author."* The model will likely reconstruct the role-before-form principle; the part it cannot supply is the judgment that *your* figure's title earns the display role and *your* source line does not. [Verify Lupton's exact Wikipedia page title before the final Wayback pass.]

## Bridge

You now hold the visual vocabulary: seven tokens, three faces, an 8px grid, and a set of strokes — a specification concrete enough to paste into DESIGN.md and hand to a code generator. But a vocabulary does not tell you *which word to use*. Knowing that red carries one data category does not tell you whether this variable should be encoded as a bar's length, a dot's position, or a region's area — and that choice, not the color, is where most infographics are won or lost. Chapter 6 introduces marks and channels: Bertin's visual variables, the grammar of graphics, and Cleveland and McGill's hard evidence that some channels are simply more accurate than others.

## Sources

- Lupton, E. *Thinking with Type*, 2nd ed. Princeton Architectural Press, 2010. — Typography as a system of functional roles; the conceptual root of the typographic token table.
- Ware, C. *Information Visualization: Perception for Design*, 4th ed. Morgan Kaufmann, 2020. — Bridges perceptual science and applied design; supports the luminance-ladder and attention claims.
- Wong, D. M. *The Wall Street Journal Guide to Information Graphics.* W. W. Norton, 2010. — Editorial-graphics reference for hierarchy and publication constraints.
- W3C WAI. *Web Content Accessibility Guidelines (WCAG) 2.2.* W3C Recommendation, 2023. — Contrast requirements behind the ink-on-white AAA claim. [accessed during drafting]
- Brewer, C. *ColorBrewer 2.0.* Penn State. — Categorical, sequential, and diverging palette reference; supports the rationing-of-hue principle.
