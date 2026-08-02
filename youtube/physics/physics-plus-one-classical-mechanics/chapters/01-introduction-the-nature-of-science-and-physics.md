# Chapter 1 — The Nature of Science and Physics

*What it means to say you know something.*

---

## A vault outside Paris

In a temperature-controlled vault at the Bureau International des Poids et Mesures in Sèvres, just outside Paris, there is a small cylinder of platinum-iridium alloy about the size of a golf ball. For 130 years it had one job. It *was* the kilogram. Not represented the kilogram. Not approximated it. *Was* it. If you wanted to know what one kilogram of mass felt like, your reference chain ended at that cylinder. They called it *Le Grand K*, and replicas sat in similarly guarded vaults from Maryland to Tokyo, each calibrated against the original every few decades.

<!-- → [IMAGE: photograph of Le Grand K inside its triple bell-jar enclosure at the BIPM — caption should note the scale (golf-ball sized) and draw attention to the protective layers; reader should feel the absurdity of the world's mass standard being a lump of metal under glass] -->

There was a problem. The cylinder was changing. Not by much — perhaps fifty micrograms over a century, the mass of an eyelash. But the replicas were drifting from it in different directions, and nobody could say which one was right, because the kilogram was *defined* to be the cylinder. The original was, by definition, exactly one kilogram, even if it was gaining or losing mass. Which meant, in a precise and uncomfortable sense, that every object in the universe was also "drifting" — because the ruler they were measured against was drifting.

On May 20, 2019, a vote of the General Conference on Weights and Measures ended this. From that day forward, the kilogram would no longer be the cylinder. It would be derived from a number — a fixed value of Planck's constant, $h = 6.62607015 \times 10^{-34}$ joule-seconds — realized through a precision instrument called a Kibble balance. The cylinder kept its name. It lost its job.

I want you to hold that scene. A lump of metal in a French vault, retired by international vote. A definition that now lives inside a quantum-mechanical equation. This is what physics *is* — not the equations on the chalkboard, but the discipline of pinning down, to within the smallest expressible uncertainty, what each of your words and numbers actually means. Before we can do any physics, we have to understand what it means to measure something, how to express a quantity precisely, and how to know whether an answer is reasonable. That's this chapter.

---

## What the discipline is

Let me tell you something that is easy to miss. Physics doesn't discover the truth about the universe. It discovers the *best available approximation* to the truth, within a specified domain, to a specified precision. These are very different claims, and confusing them causes enormous amounts of unnecessary argument.

When physicists talk about how they organize their knowledge, they use three words that get thoroughly muddled in everyday speech: *model*, *theory*, and *law*. They are not synonyms, and they are not a hierarchy where one "becomes" the other when it's been sufficiently confirmed. They are different kinds of objects.

A **model** is a mental picture you build because the actual thing is too small, too fast, or too abstract to apprehend directly. Bohr's atom — electrons orbiting a nucleus like planets around a sun — is a model. It is wrong in several technical senses. Electrons don't have orbits; they have probability clouds. The picture breaks down badly once you have more than one electron in the system. But it is *useful* because it lets you predict the spectrum of hydrogen with surprising accuracy, and because it gives students something to hold in their heads while they learn quantum mechanics. A model is justified by what it lets you compute, and its claim is deliberately local. When it fails — and every model does, eventually — you replace it with one that works in the regime you've moved into.

A **theory** is bigger. It's a body of explanation, supported by many independent lines of evidence, that accounts for an entire category of phenomena. Newton's theory of gravity explains the fall of an apple, the orbit of the Moon, the tides, the precession of the equinoxes, and the trajectory of a cannonball, all from the same starting idea: every mass attracts every other mass with a force proportional to the product of the masses and inversely proportional to the square of the distance. The claim of a theory is universal within its domain. When experiment contradicts it, the theory is either refined (Einstein's general relativity extended Newton's gravity to the regime of high speeds and strong fields) or, if the contradiction is fundamental, replaced.

A **law** is a concise mathematical statement of a regularity in nature. Newton's second law, $F = ma$. The law of conservation of energy. These are smaller than theories in vocabulary but often larger in reach. The conservation of energy is a constraint every physical situation satisfies, not a description of any particular one. A law doesn't explain *why* the regularity exists — $F = ma$ tells you what force does without telling you what force *is* — but it compresses an enormous range of confirmed experience into a single expression.

The boundaries between these are not perfectly sharp. But the spirit of the distinction is clear enough to be useful. And there's one more thing worth saying, because it comes up constantly: in everyday English, "theory" means guess, hunch, speculation. In science, "theory" means the highest-confidence kind of explanation we have. Evolution is "just a theory" in exactly the same sense that gravity is "just a theory": a body of explanation that has survived every test ever brought against it. When someone says "it's just a theory" to dismiss a scientific claim, they are, very precisely, using the word wrong.

<!-- → [DIAGRAM: three-tier visual showing MODEL / THEORY / LAW as distinct objects with labeled arrows — not a hierarchy/ladder but three parallel boxes showing scope (local → domain-wide → universal constraint), typical lifespan, and one example each; student should see that a law doesn't "graduate" from a theory, they coexist] -->

---

## How a number gets to mean something

In 1967, the international scientific community redefined the second.

Before that, the second had been $\frac{1}{86{,}400}$ of a mean solar day — a bookkeeping convenience that worked until clocks got accurate enough to notice that the solar day itself was not a fixed length. The Earth's rotation is slowing, by tidal friction and by the redistribution of mass after every earthquake. A second defined by the day was a second built on a wobbling foundation.

So they moved the foundation. From 1967 onward, the second has been defined as the time required for an undisturbed cesium-133 atom to complete exactly **9,192,631,770** oscillations between two specific energy states. Cesium atoms vibrate at this frequency anywhere in the universe, in any laboratory, at any time. The standard is portable, reproducible, and as accurate as you can build the apparatus to count.

This is the move physics has been making, systematically, with every fundamental unit for two centuries: pull the standard off something that drifts — a planet, a metal bar, a platinum cylinder — and anchor it to something that doesn't — the speed of light, Planck's constant, the hyperfine transition of an atom. The 2019 kilogram redefinition was the last of the major ones. Every base unit of the SI system now derives from a constant of nature.

The SI system uses seven fundamental units. We'll use four of them constantly:

| Quantity | Unit | Symbol |
|---|---|---|
| Length | meter | m |
| Mass | kilogram | kg |
| Time | second | s |
| Electric current | ampere | A |

Everything else is **derived** — a combination of these four. Speed is length divided by time: m/s. Acceleration is length divided by time squared: m/s². Force is mass times acceleration, so a newton is $1 \text{ N} = 1 \text{ kg} \cdot \text{m/s}^2$. Energy is force times distance, so a joule is $1 \text{ J} = 1 \text{ kg} \cdot \text{m}^2/\text{s}^2$. The derivation isn't a naming convention — it's a physical claim about what the unit means.

<!-- → [INFOGRAPHIC: tree diagram rooted at the four base units (m, kg, s, A) — branches show derived units with their dimensional decompositions: m/s (speed), m/s² (acceleration), kg·m/s² (newton/force), kg·m²/s² (joule/energy), kg·m²/s³ (watt/power); each derived unit labeled with its symbol, its name, and one familiar physical example] -->

This is why dimensional analysis is so powerful. If your answer for an energy comes out with units of $\text{kg} \cdot \text{m/s}$ — that's momentum, not energy — you know, before checking a single number, that you've made a structural error somewhere. The units run as a parallel proof alongside the arithmetic. They can't tell you the arithmetic is right; they can tell you when it's definitely wrong.

**The cancellation method.** Here's the move that makes unit conversion trivial. Treat units as algebraic quantities that obey the rules of multiplication and division. Want to convert 30.0 km/h to m/s? Set up a chain of fractions where each fraction has the unit you want to cancel on the bottom and the unit you want to keep on top:

$$30.0 \frac{\text{km}}{\text{h}} \times \frac{1{,}000 \text{ m}}{1 \text{ km}} \times \frac{1 \text{ h}}{3{,}600 \text{ s}} = 8.33 \frac{\text{m}}{\text{s}}$$

The km cancels. The h cancels. What remains is m/s — which is exactly what you wanted. You don't need to remember a conversion factor. You need to set the fractions up so the unwanted units disappear.

<!-- → [INFOGRAPHIC: step-by-step visual of the unit-cancellation chain for the 30.0 km/h → m/s conversion — show each fraction as a boxed ratio, draw strikethrough lines through the cancelling units (km, h), and circle the surviving units (m, s); the visual should make the algebra feel mechanical and failsafe] -->

A quick sanity check: 30 km/h is about 19 mph — roughly the speed of a casual bicycle ride. Eight or nine meters per second feels about right for that. If the answer had come out 83 m/s or 0.83 m/s, you'd know immediately that you'd inverted something. The order-of-magnitude check is a guard against errors you won't otherwise notice until the next exam.

The metric prefix system adds another layer of leverage. Every SI unit can be scaled by a power of ten using a fixed vocabulary: nanometers ($10^{-9}$ m), megahertz ($10^6$ Hz), femtoseconds ($10^{-15}$ s). The prefixes run from atto ($10^{-18}$) to exa ($10^{18}$) — thirty-six orders of magnitude in one coherent system with no conversion-factor memorization required. Compare this to the U.S. customary system, which requires you to remember that there are 12 inches per foot, 3 feet per yard, 1,760 yards per mile, 16 ounces per pound, and that the U.S. gallon is not the same as the imperial gallon. Each of those conversions is a number you have to look up. Every metric conversion is a count of zeros. For science, the trade is unambiguously worth it.

---

## What every number owes you

Here is the most important thing in this chapter, and it's the one most likely to get skipped.

Every measurement carries an uncertainty. Not just some measurements — *every* measurement. The smallest division on your ruler, the precision of your timing device, the variability in the thing itself — all of these contribute. A measurement reported without its uncertainty is like a sentence without a verb: it's not a complete claim.

This isn't a technicality. It's the whole game. When the kilogram cylinder was drifting by fifty micrograms per century, that drift *mattered* because the people measuring it were trying to achieve parts-per-billion precision. At 1% precision, fifty micrograms over a century is noise. At one part in $10^9$, it's a catastrophe. Whether an uncertainty is acceptable always depends on what the measurement is *for*.

**Accuracy and precision are not the same thing.** Suppose you measure an 11.0-inch stick three times and get 11.1, 11.2, 10.9. You're accurate — clustered around the true value — but not especially precise. Suppose you get 12.0, 12.0, 12.0. You're precise — zero spread — but inaccurate. A systematic error has pushed all three readings to the same wrong value. You want both. In practice, precision is easier to test (just repeat the measurement) and accuracy is harder (you need an independent way to know the true value).

<!-- → [IMAGE: four-quadrant target diagram — top-left: scattered shots centered on bullseye (accurate, not precise); top-right: tight cluster on bullseye (accurate and precise); bottom-left: scattered shots off-center (neither); bottom-right: tight cluster off-center (precise, not accurate); label each quadrant with the student-facing takeaway, not just the terms] -->

**Percent uncertainty** is how you make uncertainties comparable across measurements with different magnitudes:

$$\text{\%unc} = \frac{\delta A}{A} \times 100\%$$

where $A$ is the central value and $\delta A$ is the uncertainty. An uncertainty of $\pm 0.4$ kg on a 5-kg measurement is an 8% uncertainty. The same $\pm 0.4$ kg on a 500-kg measurement is 0.08%. The same absolute uncertainty, completely different stories.

**Propagating uncertainty.** When you multiply or divide measured quantities, uncertainty compounds. The simplest rule, valid when individual uncertainties are a few percent or less: the percent uncertainty in the result equals the sum of the percent uncertainties in the inputs.

Take the area of a floor. You measure the length as $4.00 \text{ m}$ with 2% uncertainty and the width as $3.00 \text{ m}$ with 1% uncertainty. The area is $12.0 \text{ m}^2$. The uncertainty in the area:

$$\text{\%unc} = 2\% + 1\% = 3\%$$

That's $0.03 \times 12.0 = 0.36 \text{ m}^2$, which rounds to $0.4 \text{ m}^2$. You report: $A = 12.0 \pm 0.4 \text{ m}^2$.

The deeper lesson here: uncertainty *grows* when you compound measurements. A calculation built on five measured inputs will have larger uncertainty than any single input. You cannot manufacture precision the inputs don't have. Reporting extra digits suggests precision you don't possess, which is a form of dishonesty — about what you actually measured.

**Significant figures** are shorthand for this. The last digit you write is the first digit that carries any uncertainty. $36.7 \text{ cm}$ has three significant figures because the 7 — the millimeter digit — was estimated. The rules for arithmetic:

For multiplication and division, the result has as many significant figures as the *least precise* input. $\pi \times (1.2 \text{ m})^2 = 4.5238... \text{ m}^2$ rounds to $4.5 \text{ m}^2$ because the input has two significant figures. Reporting 4.52 or 4.524 would be claiming precision the measurement doesn't support.

For addition and subtraction, the result has no more decimal places than the *least precise* input. $7.56 \text{ kg} - 6.052 \text{ kg} + 13.7 \text{ kg} = 15.208 \text{ kg}$ rounds to $15.2 \text{ kg}$ because the least precise input ($13.7$) is precise only to the tenths place.

Zeros are where people get turned around. Leading zeros are not significant: $0.053$ has two sig figs. Zeros between significant digits are significant: $10.053$ has five. Trailing zeros in a number without a decimal point are ambiguous — $1{,}300$ might mean two, three, or four significant figures. Write $1.3 \times 10^3$ or $1.300 \times 10^3$ and the ambiguity disappears.

---

## Estimation

There's a separate skill here that is worth naming explicitly, because it's one of the most useful things physics teaches and one of the least formally taught: the order-of-magnitude estimate, sometimes called a Fermi problem, after Enrico Fermi, who was legendary for them.

The point is to get an answer that is right within a factor of ten — without precise measurement, without a calculator, sometimes on the back of an envelope in the middle of a lecture. You decompose an unknown quantity into factors you can estimate, multiply them together, and read off the order of magnitude. The answer doesn't need to be exact. It needs to be *reasonable*.

Here's an example. How tall is a 39-story building? You don't have a measuring tape. But you know a person is about 2 meters tall, and one story of a building is roughly the height of two people stacked (accounting for floor structure and ceiling height). So:

$$\frac{2 \text{ m}}{1 \text{ person}} \times \frac{2 \text{ persons}}{1 \text{ story}} \times 39 \text{ stories} \approx 160 \text{ m}$$

That's good to within a factor of two, well within a factor of ten. If a precise calculation later tells you the building is 1,600 meters tall, you know immediately — without re-doing the arithmetic — that something has gone badly wrong. The estimate is a guardrail.

<!-- → [INFOGRAPHIC: visual breakdown of the 39-story building Fermi estimate — show the chain: person (2 m) → story (2 persons = 4 m) → 39 stories → ~160 m; lay it out vertically so the stacking is literal; annotate with the "factor of ten guardrail" idea — what range of answers would be reasonable vs. clearly wrong] -->

Fermi estimates work because most quantities we care about — areas, volumes, populations, energies — factor into simpler quantities that are already somewhere in our heads. The skill is knowing which factors to grab and how to chain them together without losing the thread.

One more example, to show the method applied to units at the same time. A tectonic plate moves at about $4.0 \text{ cm/year}$. How far does it move in one second?

$$4.0 \frac{\text{cm}}{\text{yr}} \times \frac{1 \text{ m}}{100 \text{ cm}} \times \frac{1 \text{ yr}}{3.16 \times 10^7 \text{ s}} \approx 1.3 \times 10^{-9} \frac{\text{m}}{\text{s}}$$

That's roughly the diameter of a few atoms. Per second. The same plate, measured over a million years, moves 40 kilometers. The same physical rate looks completely different depending on the units you choose to express it in. The physics hasn't changed; only the bookkeeping has. And notice: the input had two significant figures, so the answer gets two: $1.3 \times 10^{-9}$ m/s, not $1.265823 \times 10^{-9}$.

<!-- → [TABLE: two-column comparison showing the tectonic plate rate expressed in contrasting unit pairs — rows: cm/year vs. m/s, km/My vs. nm/day, etc.; right column adds a "physical feel" annotation (e.g., "~3 atoms per second," "half a marathon per million years"); student should feel how unit choice controls intuition] -->

---

## What these three things have in common

Step back from the details for a moment. This chapter has given you three commitments:

Nature has discoverable order — models, theories, and laws are different kinds of claim about that order, and knowing which one you're dealing with tells you how far to trust it.

Every quantity must be tied to a defensible unit — the SI system anchors each fundamental unit to a constant of nature, and every derived unit is built from those four fundamentals in a way that carries physical meaning.

Every number must carry its honest uncertainty — percent uncertainty, propagation rules, significant figures, and Fermi estimation are all different faces of the same demand: say what you know, and say how well you know it.

These aren't separate topics dressed up as a chapter. They're the same discipline, viewed from three angles. The reason *Le Grand K* had to be retired in 2019 was precisely that the cylinder could no longer support the uncertainty demands modern measurements placed on it. When precision improved by several orders of magnitude, the artifact-based definition became the bottleneck. The move to Planck's constant was the discipline asserting itself: the standard must be as honest as the measurement.

The deepest thing this chapter is trying to install is not a method. It's a habit of mind. Before you write down a number, ask: what are my units, and do they make sense? How well do I actually know this value? Is the answer I computed in the right ballpark? These questions don't slow you down. They are the difference between physics and arithmetic.

There's a question this chapter raises that it doesn't answer, and I want to name it: *why* does the universe cooperate? Why do the same mathematical regularities hold in a lab in Sèvres and in the atmosphere of a star ten billion light-years away? We can demonstrate the cooperation. We can derive some regularities from deeper ones. But the meta-question — why does nature have such order at all — sits at the edge of what physics can address. Eugene Wigner called it "the unreasonable effectiveness of mathematics in the natural sciences" in 1960. The puzzle hasn't gone away.

---

## Exercises

### Warm-up

**1.1** In your own words, distinguish a model from a theory from a law. Give one physics example of each that is not Newton's gravity.

**1.2** Express each of the following in scientific notation with the correct SI prefix substituted: 1,500 meters in km; 0.0042 seconds in ms; 7,300,000,000 hertz in GHz; 0.000000056 meters in nm.

**1.3** Count the significant figures in each: $0.0009$; $15{,}450.0$; $6 \times 10^3$; $87.990$; $30.42$.

**1.4** A highway speed limit is $100 \text{ km/h}$. Use the cancellation method to convert this to m/s. Then convert to miles per hour. ($1 \text{ km} = 0.6214 \text{ mi}$.)

### Application

**1.5** A car speedometer has a 5.0% uncertainty. (a) What is the range of possible true speeds when it reads $90 \text{ km/h}$? (b) Convert this range to miles per hour.

**1.6** You measure the three sides of a small rectangular box: $1.80 \pm 0.01 \text{ cm}$, $2.05 \pm 0.02 \text{ cm}$, and $3.1 \pm 0.1 \text{ cm}$. Calculate the volume and propagate the uncertainty. Report as $V \pm \delta V$ in cm³.

**1.7** Newton's law of gravitation is $F = G \frac{m_1 m_2}{r^2}$. Without computing anything, work out what units $G$ must carry for the equation to be dimensionally consistent — that is, for the right-hand side to come out in newtons. Show your reasoning.

**1.8** A friend claims to have run a marathon (42.188 km) in 2 hours, 30 minutes, and 12 seconds. Before reaching for a calculator, estimate her average speed in m/s. Then compute it precisely. By what percentage did your estimate miss?

### Synthesis

**1.9** You weigh yourself five times on a digital bathroom scale: $72.1$, $72.3$, $72.0$, $72.2$, $72.4 \text{ kg}$. The scale's resolution is $\pm 0.1 \text{ kg}$. Report your weight as $\bar{m} \pm \delta m$. Justify your choice of $\delta m$ — is it the scale's resolution, the spread in your readings, or something else?

**1.10** The chapter argues that classical physics is "essentially exact" within its domain of applicability. What is that domain, in concrete terms? Name two physical scenarios where it breaks down and identify what physical effect each failure points toward. You should be able to construct this argument from the chapter's prose — no outside knowledge required.

**1.11** Estimate the number of heartbeats in a human lifetime. State your input assumptions. Bracket your answer with a plausible upper and lower estimate. Then compare your result to the commonly cited value of $2 \times 10^9$ and comment on whether the agreement is meaningful or coincidental.

### Challenge

**1.12** The kilogram was redefined in 2019 to depend on Planck's constant rather than a physical artifact. Construct an argument — addressing both the practical and philosophical dimensions — for why this change matters. On the practical side: what was actually wrong with the cylinder? On the philosophical side: what does it mean for a unit to be "defined" by an artifact versus by a constant of nature?

**1.13** Estimate the total number of atoms in your body. State every input assumption; show the full chain of estimates; report your answer to one significant figure. (Hint: start from the mass of a person and the mass of an "average" atom — most of the body is hydrogen, oxygen, and carbon, so a rough average atomic mass is somewhere around 7–10 atomic mass units.)

---

## LLM Exercise — Chapter 1: Anchor Quantity for the Reality Check Logbook

**Project:** Physics Reality Check Logbook  
**What you're building this chapter:** Your project's first entry — one anchor quantity, measured or sourced honestly, with units, significant figures, and an explicit uncertainty.  
**Tool:** Claude Project (the same one you set up in Chapter 00).

### The Prompt

```
I'm building a Physics Reality Check Logbook for College Physics with LLMs. Each chapter contributes one entry analyzing a real-world physical phenomenon using that chapter's physics. For Chapter 1, the entry tests my ability to report a measured quantity honestly — with proper units, significant figures, and uncertainty.

I want my anchor phenomenon for this whole logbook to be: [paste a 1-sentence description of the phenomenon you'll track across the book — e.g., "the daily commute by bicycle from my apartment to campus," "the operation of my coffee maker," "the trajectory of a basketball shot from the free-throw line," "the energy budget of running a marathon"].

For Chapter 1, please:

1. Identify ONE quantitative property of this phenomenon that I should measure or source carefully (e.g., for the bike commute: the elevation gain in meters; for the coffee maker: the steady-state operating temperature in Celsius). Explain why this quantity is foundational for the analyses that will follow in later chapters.

2. Tell me where I would source this number from primary references vs. measure myself, and what kind of uncertainty I should expect from each path.

3. Show me how to report it correctly: value ± uncertainty, with proper units and significant figures.

4. Walk through one Fermi-style sanity check I can do mentally to verify the number is in the right order of magnitude.

5. Identify two ways the number could mislead me later (e.g., variability across measurements, dependence on conditions I didn't record).

Be specific to my chosen phenomenon. Don't give me a generic "uncertainty 101" answer.
```

### What this produces

A one-page Logbook entry — your first — that establishes the phenomenon you'll track across the book. The entry includes one carefully sourced number with explicit uncertainty, a Fermi-check, and two named pitfalls for future chapters. Save as `logbook/chapter-01-anchor.md` (or your preferred filename convention).

### How to adapt this prompt

- *For your chosen phenomenon:* Replace the bracketed description with the phenomenon you'll track for the whole book. Picking it well now matters — you'll come back to it 33 more times.
- *For ChatGPT or Gemini:* Works identically. Replace "Claude Project" with "Custom GPT" or "Gemini Gem" for setup, but the prompt itself transfers.
- *For a more code-heavy approach:* If you have measurement data (a fitness tracker recording your bike commute, a thermocouple log from your coffee maker), use Claude Code instead — paste the data and ask Claude to compute the mean and standard deviation, then report properly.

### Connection to previous chapters

Builds on Chapter 00's project setup. The Claude Project you created in Chapter 00 should now hold both the project foundation document and this Chapter 1 anchor entry.

### Preview of next chapter

Chapter 2 introduces kinematics — position, velocity, acceleration. The Chapter 2 LLM Exercise will ask you to extract one kinematic property of your chosen phenomenon (a speed, an acceleration, a stopping distance) using the equations of motion, and add it as the second entry in your Logbook.

---

## AI Wayback Machine

**Ibn al-Haytham** wrote *Kitāb al-Manāẓir* (Book of Optics) around 1021 — establishing experimental method centuries before its European rediscovery. He insisted that light travels in straight lines, enters the eye rather than emanating from it, and that experiment must validate theory.

**Run this:**

```
Who was Ibn al-Haytham, and how does his work connect to the nature of science we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about his career or ideas.
```

→ Search **"Ibn al-Haytham"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to describe one of Ibn al-Haytham's optical experiments in the *Book of Optics*.
- Ask it about how Ibn al-Haytham came to write the book during his decade under house arrest in Cairo.

What changes? What gets better? What gets worse?

---

*Chapter 2 introduces kinematics — position, velocity, acceleration. With the discipline of units and uncertainty installed, you will spend the next chapter making motion precise in exactly the same way this chapter made measurement precise.*
