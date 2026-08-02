# Newton's Law of Universal Gravitation

**TL;DR:** Gravity is not a tug of war — it's the geometry of mass bending space. The same force that pulls an apple down pulls the moon in orbit. The machinery is inverse-square: double the distance, and the pull becomes one quarter as strong.

---

## Chapter Opening: The Moon's Defiance

Imagine you are standing in the dark. The moon hangs above you, pulling the ocean. You know this. You have seen the tides. But here is the puzzle: the moon is not touching the water. It is not beneath it, pushing up. It hangs 380,000 kilometers away, visible as a pale disc in the vacuum. Yet the oceans rise and fall on a rhythm written by that distant rock.

For thousands of years, this was maddening. How could something act across empty space? It seemed like magic. Gravity was so puzzling that most people did not even try to explain it — they simply took it as a given, like hunger or breath.

Then in 1666, while Cambridge University was shut by plague, a young Isaac Newton sat in his mother's garden watching an apple fall. He did not invent gravity by watching the apple. What he invented was the thought: *what if the same force that drops the apple also holds the moon in its orbit?*

This was not obvious. The apple falls toward Earth. The moon does not. The apple accelerates. The moon orbits at constant speed. For two centuries before Newton, astronomers had treated these as two entirely different phenomena. Newton asked: what if they are the same force, just at different distances?

He was right. And when he worked out the mathematics, the universe simplified. One law. One force. Everything from dust to planets to the spin of galaxies follows the same rule.

**Learning Objectives.** By the end of this chapter, you will be able to:
- State Newton's law of universal gravitation and identify the role of each term
- Distinguish between mass and weight, and explain why weight changes with gravity while mass does not
- Calculate gravitational force between two objects
- Connect Newton's law to Kepler's three laws of planetary motion
- Explain why Einstein's theory of general relativity extended Newton's insight, and what "bending of space" actually means

**Prerequisites.** Newton's three laws of motion. The concept of force and acceleration. Basic algebra with exponents.

---

## Concept 1: The Inverse-Square Law

Here is Newton's law of universal gravitation in mathematical form:

$$\mathbf{F} = G\frac{mM}{r^{2}}$$

Read this slowly. $\mathbf{F}$ is the gravitational force — the pull between two objects, measured in newtons. The letter $m$ is the mass of one object, $M$ is the mass of the other. The letter $r$ is the distance between their centers of mass. And $G$ — the gravitational constant — is a number that sets the strength of gravity everywhere in the universe: $G = 6.67 \times 10^{-11}$ newton-meters-squared per kilogram-squared.

The equation says: the force is proportional to the product of the masses. Bigger masses pull harder. And the force is *inversely proportional to the square of the distance*. Double the distance, and the pull becomes one quarter as strong. Triple it, and the pull becomes one ninth as strong. The mathematics is brutally simple.

But what does "proportional to the product of the masses" actually mean? It means that if you double one mass, the force doubles. If you double both masses, the force quadruples. A 2-kilogram object and a 3-kilogram object pull on each other with a force six times as strong as two 1-kilogram objects separated by the same distance. The product $mM$ captures this: $2 \times 3 = 6$.

The inverse-square part is trickier. Why the square of the distance? Here is the machinery. Imagine gravity as a thing that spreads out from a mass like light from a lamp. At a distance $r$, the gravitational "signal" is spread over a sphere of surface area $4\pi r^2$. Double the distance, and the surface area of the sphere increases by a factor of four. The same gravitational signal is now spread four times thinner. Hence the inverse square.

This is why gravity gets weak so fast the farther away you go. The moon is 380,000 kilometers from Earth. That is not some arbitrary distance. It is precisely the distance where the moon's orbital speed and the strength of Earth's gravity happen to balance. If the moon were twice as far, Earth's pull would be only one quarter as strong, and the moon would move more slowly — but not so slowly that gravity's weakness would let it escape. The whole system balances on the geometry of the inverse square.

**Trade-offs:** The inverse-square law is elegant, but it has a cost. It means gravity is never truly zero. Even you and I, sitting across a table, exert a gravitational pull on each other. It is absurdly tiny — about $6.67 \times 10^{-9}$ newtons for two 10-kilogram masses one meter apart. You could not feel it. But mathematically, it is there. Gravity is the weakest of the four fundamental forces in nature. It is so weak that we ignore gravitational interactions between atoms. But because gravity is always attractive and never repels, it dominates on cosmic scales, pulling galaxies together across billions of light-years.

**Worked Example: Weight at Earth's Surface**

What is your gravitational force on Earth?

Take yourself: mass $m = 60$ kilograms. Earth's mass: $M = 5.97 \times 10^{24}$ kilograms. Earth's radius: $r = 6.38 \times 10^6$ meters (the distance from Earth's center to you, standing on the surface). Plug into the equation:

$$\mathbf{F} = \left(6.67 \times 10^{-11}\frac{\text{N} \cdot \text{m}^{2}}{\text{kg}^{2}}\right) \frac{(60\text{ kg})(5.97 \times 10^{24}\text{ kg})}{(6.38 \times 10^{6}\text{ m})^{2}}$$

The denominator: $(6.38 \times 10^{6})^2 = 4.07 \times 10^{13}$ m$^2$.

The numerator: $60 \times 5.97 \times 10^{24} = 3.58 \times 10^{26}$ kg$^2$.

$$\mathbf{F} = (6.67 \times 10^{-11}) \times \frac{3.58 \times 10^{26}}{4.07 \times 10^{13}} = (6.67 \times 10^{-11}) \times (8.79 \times 10^{12}) \approx 586\text{ N}$$

You weigh 586 newtons. Or 60 kilograms times 9.8 m/s$^2$, which gives 588 newtons. The numbers agree to within rounding. This is not a coincidence. It is the machinery of gravity.

**Common Misconception:** "Gravity is a constant." No. The strength of gravity at Earth's surface is about 9.8 m/s$^2$. But the *value changes* if you climb a mountain or move to another planet. What is constant is $G$, the gravitational constant — the number that sets gravity's strength everywhere. On Mars, where the surface gravity is 3.71 m/s$^2$, the same $G$ applies. The reason gravity is weaker there is that Mars is less massive and smaller than Earth, so you are both farther from its center and pulled by a smaller mass.

---

## Concept 2: Mass vs. Weight

Here is a source of endless confusion in physics: the difference between mass and weight.

**Mass** is the amount of stuff in an object. It is measured in kilograms. Mass does not change. A 60-kilogram person is 60 kilograms whether they are on Earth, on the moon, or drifting in deep space.

**Weight** is the gravitational force acting on an object. It is measured in newtons, or sometimes in "kilograms-force." Weight changes depending on where you are.

The distinction matters because they are different things wearing similar names. On Earth, we say "I weigh 60 kilograms," but we are technically lying. We mean our mass is 60 kilograms. Our weight — the pull of Earth's gravity on us — is about 588 newtons.

On the moon, an astronaut with a mass of 60 kilograms still has a mass of 60 kilograms. But the moon is much smaller than Earth and much less massive. The gravitational constant $G$ is the same. But the moon's radius and mass are smaller. Plug them into the equation, and you get $g = 1.62$ m/s$^2$ — about one sixth of Earth's. So the astronaut weighs only 97 newtons on the moon.

The formula that connects them is simple:

$$\mathbf{W} = m\mathbf{g}$$

where $\mathbf{W}$ is weight (in newtons), $m$ is mass (in kilograms), and $\mathbf{g}$ is the local acceleration due to gravity. On Earth, $\mathbf{g} = 9.8$ m/s$^2$. Everywhere else, it is different.

Here is where it gets interesting. We can derive $\mathbf{g}$ itself from Newton's law. Set the weight equal to the gravitational force:

$$m\mathbf{g} = G\frac{mM}{r^{2}}$$

The $m$ cancels:

$$\mathbf{g} = G\frac{M}{r^{2}}$$

This tells you that $\mathbf{g}$ depends only on the mass and size of the body below you, not on your own mass. A feather and a hammer dropped on the moon fall at the same rate. Galileo suspected this. Newton proved it. Air resistance aside, they arrive together.

**Trade-offs:** The advantage of understanding mass and weight separately is clarity. You now know why your mass never changes but your weight does. The disadvantage is that the English language confuses them shamelessly. We colloquially weigh things in kilograms, which is technically a mass. Metric units are clear: kilograms for mass, newtons for weight. But in everyday speech, the boundary blurs. The best practice is to use the terms precisely in physics and forgive the sloppiness in daily life.

**Worked Example: Weight on Mars**

You have a mass of 60 kilograms. You land on Mars. Mars has a mass of $6.39 \times 10^{23}$ kilograms and a radius of $3.39 \times 10^6$ meters. What is your weight on Mars?

Use the formula $\mathbf{g} = G\frac{M}{r^{2}}$:

$$\mathbf{g}_{\text{Mars}} = (6.67 \times 10^{-11}) \frac{6.39 \times 10^{23}}{(3.39 \times 10^{6})^{2}} = (6.67 \times 10^{-11}) \frac{6.39 \times 10^{23}}{1.15 \times 10^{13}} \approx 3.71\text{ m/s}^{2}$$

Now your weight:

$$\mathbf{W}_{\text{Mars}} = (60\text{ kg})(3.71\text{ m/s}^{2}) = 223\text{ N}$$

On Earth, you weigh 588 newtons. On Mars, you weigh 223 newtons. Your mass has not changed. The pulling power of gravity beneath your feet has weakened.

**Common Misconception:** "Objects weigh more near the poles because Earth is fatter at the equator." There is a small truth here. Earth is slightly fatter at the equator than at the poles — it bulges. But the real effect is more subtle. The equation is $\mathbf{g} = G\frac{M}{r^{2}}$. At the equator, you are slightly farther from Earth's center, so $r$ is larger, and $\mathbf{g}$ is slightly smaller. At the pole, you are closer, and $\mathbf{g}$ is slightly larger. This is the primary effect. The rotation of Earth adds a secondary complication — centrifugal effects — but the inverse-square distance change is the main reason.

---

## Concept 3: Gravity and Orbital Motion — Connecting to Kepler

Here is the deepest insight: Kepler's three laws of planetary motion, which describe the observed patterns of orbits, can be derived from Newton's law of universal gravitation.

Kepler's third law states that the square of the orbital period is proportional to the cube of the orbital radius:

$$\frac{T^{2}}{r^{3}} = \frac{4\pi^{2}}{GM}$$

where $T$ is the period (the time to complete one orbit), $r$ is the orbital radius, $M$ is the mass of the central body (the sun, or Earth, or whatever the planet orbits), and $G$ and $4\pi^2$ are constants.

How do we get here from Newton's law? The route is calculus and circular motion, but the logic is physical. An orbiting object experiences a gravitational force pulling it toward the center. This force supplies the centripetal acceleration that keeps the object moving in a circle instead of flying off in a straight line. Set the gravitational force equal to the centripetal force, solve for the period, and you get Kepler's third law.

The payoff is enormous. Kepler observed the patterns — he had no explanation for *why* they worked. Newton showed that gravity itself, the same force that drops an apple, explains all of planetary motion. It is a unification: one force, one equation, everything from dust to galaxies.

Here is a practical consequence. If you know the orbital period of a satellite and the distance it orbits from the center of its parent body, you can calculate the mass of the parent body. Astronomers use this every day. They observe the orbital period of a star's exoplanet and measure how far it orbits. From those two observations alone, they can infer the star's mass. They do not need to go there. They do not need to weigh it. Gravity gives them the answer.

**Trade-offs:** The connection between Kepler's laws and Newton's law shows the power of a unifying principle. But it comes with a cost: Newton's mechanics does not explain gravity itself. It describes the pattern — inverse square, proportional to mass — but not the underlying mechanism. Why does mass curve space? Newton did not ask. He calculated. It took another two centuries and Albert Einstein to answer the mechanism question.

**Worked Example: Finding a Satellite's Orbital Period**

A satellite orbits Earth in 27.3 days at an average distance of $3.84 \times 10^8$ meters (this is the moon). You discover a new satellite orbiting the same planet at a distance of $7.88 \times 10^6$ meters. Using Kepler's third law, what is its orbital period?

Kepler's third law for two satellites orbiting the same body:

$$\frac{T_{1}^{2}}{T_{2}^{2}} = \frac{r_{1}^{3}}{r_{2}^{3}}$$

Let 1 = moon, 2 = new satellite. Solve for $T_2$:

$$T_{2} = T_{1} \left(\frac{r_{2}}{r_{1}}\right)^{3/2}$$

Convert the moon's period to seconds: $27.3 \text{ days} \times 86400 \text{ s/day} = 2.36 \times 10^6$ seconds.

$$T_{2} = (2.36 \times 10^6) \left(\frac{7.88 \times 10^{6}}{3.84 \times 10^{8}}\right)^{3/2}$$

The ratio: $\frac{7.88 \times 10^{6}}{3.84 \times 10^{8}} = 0.0205$.

Raise to the 3/2 power: $(0.0205)^{1.5} = 0.00293$.

$$T_{2} = (2.36 \times 10^6)(0.00293) \approx 6900\text{ seconds} \approx 1.9\text{ hours}$$

A satellite 50 times closer than the moon orbits in only 1.9 hours. The inverse-square relationship is pitiless: closer orbits are much faster.

**Common Misconception:** "The moon doesn't fall because it's far away." False. The moon *is* falling — it is falling toward Earth continuously. The reason it does not crash is that it also has sideways motion. The combination of falling and sideways motion curves its path into an orbit. The moon is always falling; it just keeps missing the Earth because the Earth is round.

---

## Integration: One Force, Many Scales

Stand back and see what we have built.

A single equation — $\mathbf{F} = G\frac{mM}{r^{2}}$ — explains:
- Why you weigh 60 kilograms on Earth and 23 kilograms on Mars
- Why the moon orbits in 27.3 days at 380,000 kilometers away
- Why a satellite 50 times closer must orbit 8 times faster
- Why the tides rise and fall with the moon
- Why planets trace ellipses, not circles
- Why galaxies spin, held together by gravity even across millions of light-years

This is the power of Newton's insight: *the same force that pulls you down pulls the cosmos together*.

There is a catch. Newton's equation works perfectly for everyday objects and for planetary motion. But it has limits. It says gravitational force acts *instantaneously* across any distance. If the sun disappeared, Newton's equation would say Earth would immediately fly away. But in reality, Earth would not "know" the sun had disappeared until light from the event reached us — eight minutes later. Newton's equation ignores this.

Einstein's theory of general relativity fixes this. It says gravity is not a force pulling across space, but rather the geometry of space-time itself bending around mass. Massive objects warp the fabric of space and time around them. Objects move along the curved paths this warping creates. The moon does not orbit because Earth pulls it; the moon orbits because Earth's mass bends the space around it into a "valley," and the moon rolls along the bottom of that valley. Light bends around the sun for the same reason — not because gravity pulls on it (photons have no mass), but because the space it travels through is curved.

For most problems — calculating orbits, weighing things, launching rockets — Newton's equation is precise enough. But for extreme cases — the edge of a black hole, the first moments after the Big Bang — Einstein's geometry is necessary. Both are true. Newton's is the simpler, more practical description. Einstein's is deeper.

---

## Exercises

**Warm-up**

1. Calculate your weight on Earth. (Assume $g = 9.8$ m/s$^2$ and your mass is 70 kg.)

2. The gravitational constant $G = 6.67 \times 10^{-11}$ N⋅m$^2$/kg$^2$. Two 100-kilogram spheres sit 10 meters apart. Calculate the gravitational force between them. (Hint: the answer is tiny.)

3. If you double the distance between two objects, the gravitational force becomes ________ as strong. (Fill in: one-fourth, one-half, two times, four times.)

**Application**

4. Earth's moon has a mass of $7.35 \times 10^{22}$ kg and a radius of $1.74 \times 10^6$ meters. Calculate the surface gravity on the moon. How does it compare to Earth's?

5. Kepler's third law relates orbital period and radius. If a new exoplanet orbits a star every 365 days at an orbital radius twice that of Earth's, what can you infer about the star's mass compared to the sun?

6. The International Space Station orbits Earth at about 400 kilometers altitude. Calculate Earth's surface gravity there. Why does the astronaut "float"?

**Synthesis**

7. You are on a planet with twice Earth's mass and twice Earth's radius. How does your weight compare to your weight on Earth? Explain using the equation for $g$.

8. Einstein's theory of general relativity says gravity curves space-time, not that it is a force pulling objects. How would you test this difference? What observation would distinguish Einstein's view from Newton's?

**Challenge**

9. A satellite falls toward Earth at a rate of about 5 millimeters per second squared (this is the measured centripetal acceleration of the International Space Station). Using $\mathbf{g} = G\frac{M}{r^{2}}$, calculate the altitude of the satellite. (Use Earth's mass: $5.97 \times 10^{24}$ kg, Earth's radius: $6.38 \times 10^6$ m, $G = 6.67 \times 10^{-11}$ N⋅m$^2$/kg$^2$.)

---

## Chapter Summary

Gravity is governed by Newton's law of universal gravitation: every mass attracts every other mass with a force proportional to the product of their masses and inversely proportional to the square of the distance between them.

Mass is the amount of matter; weight is the gravitational force on that matter. Mass is constant everywhere. Weight changes depending on where you are.

The surface gravity $g$ on any body is determined by its mass and radius: $\mathbf{g} = G\frac{M}{r^{2}}$. This is why you weigh less on the moon and why gravity gets weaker farther from Earth.

Kepler's three laws of planetary motion can be derived from Newton's law. This unification — showing that the same force explains both falling apples and orbiting planets — is one of science's greatest achievements.

Einstein's theory of general relativity extended Newton by showing that gravity is not a force but the curvature of space-time itself. For everyday calculations, Newton's equation is precise enough. For extreme cases, Einstein's geometry is necessary.

---

## Connections Forward

In the next chapter, we turn to oscillations and waves — periodic motions that govern everything from vibrating strings to light itself. The same mathematics that describes an orbit — periodicity, resonance, energy transfer — describes a pendulum or a vibrating drum. Gravity will reappear when we study tides and orbital resonances. And when we reach the quantum scale, we will discover that gravity is the odd force out: it resists quantization, and we still do not have a complete quantum theory of gravity. But that is a frontier problem for another day.

---

## Appendix: "What Would Change My Mind"

If observation showed that gravitational force *did not* follow an inverse-square law — if doubling distance produced less than a four-fold decrease in force — Newton's law would need revision. We have measured this to extraordinary precision; the inverse square holds to better than one part in a trillion in the solar system and to remarkable precision even in galaxy clusters. But gravity at the strongest extreme — near black holes and neutron stars — does show deviations. This is not a failure of Newton's law; it is a domain where general relativity, not Newton, is the correct description.

## Appendix: "Still Puzzling"

I do not yet fully understand why the universe is "fine-tuned" so that gravity is weak enough that atoms exist, yet strong enough to build galaxies. If $G$ were only slightly different, either atoms would not form or the universe would have collapsed immediately. Why is gravity so precisely calibrated? The answer might lie in quantum gravity, or in multiverse models, or in a principle we have not yet discovered.

---

## Tags

#gravity #inverse-square-law #Kepler #Newton #orbital-mechanics #mass-and-weight #general-relativity
---

## LLM Exercise — Chapter 7: Newton's Law of Gravitation (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the pendulum-period-measures-g demo.
**Tool:** **Claude Project** for the entry.

---

**The Prompt:**

```
Chapter 7 demo. Notebook in this Claude Project. Chapter 7 taught:
F = Gm₁m₂/r² (universal gravitation); orbital motion as a balance
of gravitational pull and centripetal-force requirement; orbital
velocity v = √(GM/r); g = 9.8 m/s² near Earth's surface as a
direct consequence of GM_Earth / R_Earth².

The Cavendish-style direct measurement of G is hard with household
items. Instead: measure g via the pendulum period, which is the
canonical historical measurement.

**The Demo:** Measure g by timing a pendulum's period.

**The physics:** For small angles, a pendulum's period is
T = 2π√(L/g), where L is the length and g is the gravitational
acceleration. Solving for g: g = 4π²L / T².

**Materials:**
- A long string (1-2 m). Longer = better measurement.
- A small heavy weight: a key, a small lock, a hex nut, a washer.
- A measuring tape.
- A stopwatch (your phone).

**Procedure:**

1. Attach the weight to one end of the string. Tie the other end
   to a fixed point (a ceiling fixture, a doorframe, a tree
   branch). Make sure the pendulum swings freely and the string
   is taut.

2. Measure L: from the pivot to the center of the weight.

3. Pull the pendulum back ~10 degrees from vertical (small-angle
   approximation requires this). Release without push.

4. Time 20 complete swings (back-and-forth = one swing). Record
   total time t. Period T = t / 20. (Timing 20 swings averages
   out the timing error.)

5. Compute g = 4π²L / T². Should be close to 9.8 m/s².

6. Repeat with a different L (e.g., shorter pendulum). Compute g
   again. Should be the same.

**Predicted vs. measured:**
- For L = 1 m: predicted T = 2π√(1/9.8) ≈ 2.01 s.
- For L = 0.5 m: predicted T ≈ 1.42 s.

**Use Claude as a thinking partner:**
- Before: "If I want my computed g to be within 1% of 9.8 m/s²,
  how accurately do I need to measure L and T?"
- After: "I measured L = X m and T = Y s. Computed g = Z m/s².
  Discrepancy from 9.8: D %. Likely sources: timing precision,
  string-stretch, large-angle nonlinearity, air resistance.
  Which is most consequential here?"

**Variation: large-angle pendulum.** Repeat with a 60-degree
release angle. Period should be slightly longer (the small-angle
approximation breaks). The discrepancy is predictable from the
chapter's physics.

**Notebook entry should include:**
- Photo of the pendulum setup.
- Measured L and T (with units and uncertainty).
- Computed g.
- Discrepancy from 9.8 m/s² and likely cause.
- A second measurement at a different L confirming g is constant.

End with: how would you measure g on the moon or on Mars using
the same setup? What would you predict for the period?
```

---

**What this produces:** A measured g value, computed from a pendulum. Most students get within 5% of 9.8 m/s² with reasonable care.

**How to adapt this prompt:**

- *For your own project:* Take 20 swings, not 5 — the precision improvement is significant.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* Optional — for analyzing video to extract period.
- *For a Claude Project:* Append.

**Connection to previous chapters:** Ch 3's free-fall and Ch 4's force concepts both come together — gravity is a force; that force produces acceleration g near Earth's surface; the pendulum period measures that g.

**Preview of next chapter:** Chapter 8 is momentum. You'll do a collision experiment with two equal-mass coins and confirm momentum conservation.


---

## AI Wayback Machine

**Henry Cavendish** measured Newton's gravitational constant G in 1798 — letting physics finally compute the mass of the Earth.

**Run this:**

```
Who is Henry Cavendish, and how does their work connect to Newton's law of gravitation we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Henry Cavendish"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Henry Cavendish's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Henry Cavendish's framework."

What changes? What gets better? What gets worse?
