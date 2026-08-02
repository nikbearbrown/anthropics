# Chapter 2 — Units and Measurement

## Three suggested titles

- **The Billion-Dollar Typo: Why Units Matter**
- **How to Measure the Universe (And Not Lose $325 Million)**
- **Seven Numbers That Describe Everything**

---

## TL;DR

The Mars Climate Orbiter burned up in the Martian atmosphere in 1999 because one piece of software reported forces in pound-seconds while another expected newton-seconds. The machinery of measurement rests on seven base quantities — length, mass, time, temperature, electrical current, amount of substance, luminous intensity — each now defined by a physical constant that will never change. Everything else — area, volume, density, speed — derives from those seven. Get the units right, or lose a spacecraft.

---

## Chapter opening — A spacecraft's last moments

It is September 23, 1999. The *Mars Climate Orbiter*, a spacecraft the size of a small car, has been hurtling toward Mars for nine months. NASA's Jet Propulsion Laboratory in Pasadena has spent those months calculating its trajectory with extraordinary precision — accounting for gravitational effects from Jupiter and the Sun, charting a course through space so delicate that the spacecraft needed to be on target to within a few kilometers of the intended insertion point into Martian orbit.

All the calculations are done. The spacecraft is about to fire its engines to slow down, to let Mars's gravity catch it, to settle it into orbit where its instruments can begin mapping the planet's atmosphere and climate.

Then the signal arrives at JPL. The spacecraft is not where it should be. It is about 100 kilometers too low. NASA engineers realize what will happen: in a few minutes, the spacecraft will enter the Martian atmosphere at too steep an angle. It will not slow down in time. It will burn up.

The investigation that followed revealed a tragicomic culprit. A piece of software called *SM_FORCES* — "small forces" — was recording thruster performance data. It was recording the data in pound-force-seconds (lbf·s), a unit of momentum using pound-force as the measure of force. This is a perfectly sensible unit. The problem was that the rest of the spacecraft's navigation software expected the data in newton-seconds (N·s), the SI unit. No one had caught the mismatch. The spacecraft had been flying a different trajectory from the one the navigators thought they were commanding.

One conversion factor's worth of attention — multiply by 4.45 to convert from lbf·s to N·s — would have saved $325 million.

This chapter is about why that conversion factor matters, why we need agreed-upon units in the first place, and what the machinery of measurement actually looks like underneath. It turns out that measurement is not just about picking a ruler and reading a number. It is about building a system where seven base quantities — carefully defined, globally agreed upon, anchored to physical constants that will never change — combine to describe every magnitude the universe can present. And it is about understanding exactly how precise your measurements are, so you know when you have a problem and when you are good.

### Learning objectives

By the end of this chapter you will be able to:

- **Identify** the seven SI base units and explain how each is defined, including the post-2019 shift from physical artifacts to physical constants.
- **Apply** unit conversion factors to translate between unit systems and **use dimensional analysis to check whether an equation makes physical sense.**
- **Distinguish** accuracy from precision, **calculate** percent uncertainty, and **apply** significant-figure rules to determine how many digits an answer should carry.

### Prerequisites

Comfort with powers of 10 and scientific notation ($2.5 \times 10^{3}$ should not make you flinch). Basic algebra — multiplication, division, fractions. The idea that units obey the rules of algebra (if you can cancel letters in an equation, you can cancel units).

### Why this chapter matters

Every number you will encounter in physics is a *measured quantity* — it comes with a unit attached. The moment you forget what unit you are working in, you are lost. Your car's speedometer tells you a number; that number means nothing until you know whether it is kilometers per hour or miles per hour. A physics problem tells you a mass; you need to know whether it is in grams, kilograms, or pounds. The difference is not academic. It is the difference between a spacecraft in orbit and a spacecraft burning up.

Beyond this chapter, you will use SI units throughout. Vectors, forces, energy, momentum — every one carries units. If an equation does not have consistent units on both sides, it cannot be correct. If your final answer has the wrong units, you have made an error somewhere, and dimensional analysis is your tool for finding it. And when you report a measurement — the length of a table, the mass of a molecule, the speed of a car — you must carry forward the uncertainty in that measurement. Knowing your precision is knowing the limits of what you actually know.

---

## Concept 1 — The SI system: Seven base units, now defined by physical constants

We live in a world of customary units that feel natural because we grew up with them. A car travels at 65 miles per hour. A person is 5 feet 10 inches tall. A gallon of milk weighs about 8.6 pounds. These units are parochial — they live in countries once ruled by the British Empire and a few others. The rest of the world, and the entirety of science, uses SI units: the *Système International d'Unités*, or metric system. In physics, there is no choice. SI units are the language.

The SI system rests on seven base quantities. These are the only quantities we define directly through a measurement process. Everything else — area, volume, density, force, energy — is built from these seven.

**The second** is the SI unit of time. For a long time, a second was defined as 1/86,400 of a mean solar day — a human fraction. That was not good enough. The Earth's rotation is slowing down (the Moon's tidal drag keeps stealing angular momentum). In 1967, physicists switched to something that does not slow down: the cesium atom.

A cesium-133 atom, when undisturbed, vibrates in a highly regular way. Not metaphorically — its electronic states oscillate. You can set up apparatus to count these oscillations. The second is now defined as exactly 9,192,631,770 oscillations of a cesium-133 atom. Not 9 billion and some. Exactly this number. An atomic clock does not measure time in the old sense of counting revolutions of an astronomical body. It counts atoms oscillating, the same way a digital clock counts electronic pulses.

**The meter** is the SI unit of length. It too has been redefined multiple times, each time growing more precise. In 1791, when the French revolutionaries wanted to replace the tangled heap of royal measures with a rational system, they defined the meter as 1/10,000,000 of the distance from the equator to the North Pole. Reasonable, but hard to verify anywhere else. In 1889, they built a platinum-iridium bar and said: the meter is the distance between these two engraved lines. The bar was kept near Paris (it is still there, in a vault at the International Bureau of Weights and Measures). But bars get scratched. They expand and contract with temperature. In 1960, physicists replaced it with the wavelength of light: a meter was defined as 1,650,763.73 wavelengths of orange light emitted by a heated krypton-86 atom. But in 1983, the definition shifted again — this time to something even more fundamental. A meter is now defined as the distance light travels in a vacuum in exactly 1/299,792,458 of a second. The speed of light is fixed at exactly 299,792,458 m/s by international agreement. The meter follows from the second.

Why does this matter? Because light's speed is invariant — it does not change from place to place or time to time, as far as we know. The meter is no longer tied to a physical artifact that can degrade. It is tied to a constant of nature.

**The kilogram** — the SI unit of mass — is the most recent convert to this philosophy. For 223 years, from 1795 to 2018, a kilogram was defined by a cylindrical chunk of platinum-iridium kept in a vault near Paris. The "Grand K," as physicists called it. The problem: the cylinder has been slowly losing mass — about 50 micrograms per century. No one knows why. The air in the vault, microscopic contamination, something in the metal itself. Because the Grand K *was* the kilogram by definition, those 50 micrograms meant that the kilogram was changing. That is unacceptable in a unit system.

In May 2019, the definition changed. A kilogram is now defined by Planck's constant, a number from quantum mechanics that describes the energy of a photon at a given frequency. Planck's constant is approximately $6.62607 \times 10^{-34}$ joule-seconds, but it is now defined to be *exactly* this value for all time. To measure a kilogram, you use an instrument called a Kibble balance. You place a weight on one side of the balance. An electrical current on the other side creates a magnetic force. You adjust the current until the balance is level. That electrical current is proportional to Planck's constant. Since Planck's constant is now defined, the balance tells you the exact mass.

This shift — from physical artifact to physical constant — happened to all seven base units by 2019. Length is defined by the speed of light (a constant). Mass is defined by Planck's constant. Time is defined by the cesium oscillation frequency (a constant). Temperature is defined by the Boltzmann constant. Electrical current is defined by the elementary charge. The mole is defined by Avogadro's number. Luminous intensity is defined by the luminous efficacy of monochromatic radiation.

The machinery is now pure. Each base unit is anchored to something in the fundamental nature of the universe, something that will never change because it is not a thing you keep in a vault — it is a ratio built into the laws of physics.

### Etymology — Where the words come from

The word *meter* comes from the Greek *metron*, meaning "to measure." The *kilogram* comes from Greek *khilioi* (thousand) and *grama* (small weight) — a thousand grams. The *second* comes from Latin *secunda*, meaning "second division" of an hour (the first division being the minute). The *kelvin* is named for William Thomson, Lord Kelvin, who did early work in thermodynamics; it is the only SI base unit named for a person. The *ampere* is named for André-Marie Ampère, a physicist who studied electromagnetism. The *mole* comes from the Latin *moles*, meaning "mass" or "heap" — the mass of atoms in a heap. The *candela* comes from Latin for "candle" — it originally meant the light output of a candle, then was standardized.

### Trade-offs and limits

The virtue of the post-2019 SI system is also its deepest limitation: it is an *abstraction*. A kilogram is no longer a physical object you can hold. It is a number in a quantum equation. To actually measure a kilogram, you need a Kibble balance — a machine that costs hundreds of thousands of dollars and requires expertise to operate. For most of the world's laboratories and engineers, a kilogram is still the *old* kilogram, calibrated to the Grand K before it changed. Traceability — proving that your scale is accurate — requires meticulous chains of certification and comparison.

Conversely, the old system had the opposite problem: it was too concrete. You could hold the meter bar in your hand. But you could not verify it anywhere else. You had to trust that the one in Paris was accurate. And you had to hope no one bumped it.

The SI system is universal — it is used everywhere scientists work. But that universality came at a price. Countries that had used the imperial system (feet, pounds, miles) have had to maintain dual systems for decades. The United States still measures road speeds in miles per hour, even though SI units are the standard. This cost — the friction of switching measurement systems — is real. It is one of the few cases where an inferior standard wins because it is entrenched.

### Scale shift — From cesium oscillations to the age of the universe

One second is defined as 9,192,631,770 cesium oscillations. That is about 9 billion ticks. A human heartbeat is roughly one tick per second. A year is about $3.2 \times 10^7$ seconds — roughly 30 million seconds. The age of the universe is about $4 \times 10^{17}$ seconds — 400 quadrillion seconds.

In the other direction: the cesium oscillation period (the time for one cycle) is about $1.09 \times 10^{-10}$ seconds — a tenth of a nanosecond. An atomic nucleus oscillates in nuclear time scales of $10^{-21}$ seconds — a zeptosecond. A Planck time, the smallest meaningful time interval in physics, is $5.4 \times 10^{-44}$ seconds — a yoctosecond.

One meter is the distance light travels in $1/299,792,458$ second. That is about 3.3 nanoseconds. In three nanoseconds, light travels from one end of a meter to the other. A human is about 1.7 meters tall — light crosses a human body in about 5.7 nanoseconds. The Earth's diameter is about $1.3 \times 10^7$ meters. Light takes about 0.04 seconds to cross it — the kind of delay you used to hear on satellite phone calls. The observable universe is about $8.8 \times 10^{26}$ meters across — light takes about 93 billion years to cross it, and we see only what was emitted when the universe was younger.

A kilogram of water, in standard conditions, is one liter — one cubic decimeter. A grain of sand might weigh $10^{-5}$ kilograms (10 milligrams). An electron weighs $9.1 \times 10^{-31}$ kilograms. A proton weighs $1.7 \times 10^{-27}$ kilograms. The Earth weighs $6 \times 10^{24}$ kilograms. The Sun weighs about $2 \times 10^{30}$ kilograms — roughly 330,000 times more than Earth.

All of this variety — from the unimaginably small to the unimaginably large — is measured on a common scale. That is the power of the SI system and its base units.

### Worked example — Metric prefixes and the Kibble balance measurement

Suppose a Kibble balance measures a weight and reports the result as $1.34 \times 10^{-24}$ kg. Express this mass using an appropriate metric prefix.

The metric system uses prefixes to scale units by powers of 10. The common prefixes are:

- **Kilo** ($k$) = $10^3$
- **Mega** ($M$) = $10^6$
- **Micro** ($\mu$) = $10^{-6}$
- **Nano** ($n$) = $10^{-9}$
- **Pico** ($p$) = $10^{-12}$
- **Femto** ($f$) = $10^{-15}$
- **Atto** ($a$) = $10^{-18}$
- **Zepto** ($z$) = $10^{-21}$
- **Yocto** ($y$) = $10^{-24}$

Our mass is $1.34 \times 10^{-24}$ kg. We want to find a prefix such that the numerical coefficient is between 1 and 1000. Since the exponent is $-24$, the "yocto" prefix (which represents $10^{-24}$) is perfect:

$$1.34 \times 10^{-24} \text{ kg} = 1.34 \text{ yg (yoctograms)}$$

This is a tiny mass — a yoctogram is about the mass of a single proton. The Kibble balance is sensitive enough to operate in this range, which is why modern physics can measure individual particles.

### Common misconceptions

**Misconception 1:** "A kilogram is still defined by the Grand K in Paris."

Fact: As of May 2019, the kilogram is defined by Planck's constant. The Grand K is no longer the standard. It is now just a calibration artifact, no different from any other precisely machined weight.

**Misconception 2:** "SI units are metric units, and metric units are based on powers of 10."

Fact: SI units are metric, and the prefixes follow powers of 10, but the base SI unit for mass is the *kilogram*, not the gram. This creates a peculiar rule: you cannot "double up" prefixes. For example, to express $10^6$ grams, you write it as a megagram (Mg), not a kilokilo. Similarly, $10^9$ grams is a gigagram (Gg), and so on. This is because the base unit already contains a "kilo" prefix.

**Misconception 3:** "You need very expensive equipment to measure a kilogram."

Fact: For everyday use, a standard mechanical balance or electronic scale is perfectly adequate. These scales are calibrated to standard weights, which are themselves calibrated to a traceability chain leading back to national standards laboratories. The Kibble balance is a tool for *defining* the kilogram at the highest precision; it is not a tool for every measurement. Most laboratories and most of the world uses scales that are far simpler and rely on comparison to a certified reference weight.

---

## Concept 2 — Unit conversion and dimensional analysis: Tools for checking if your work makes sense

Measurements come in different units. The United States uses miles per hour; Europe uses kilometers per hour. A baker in the US measures flour in cups; a baker in the UK measures in grams. A physicist in Beijing and a physicist in Boston must speak the same language, which is SI units. Unit conversion is the mechanical move: multiply by the right fraction to transform one unit into another. Dimensional analysis is the strategic move: check whether an equation could possibly be correct by seeing whether the dimensions on both sides match.

**Unit conversion using conversion factors**

A conversion factor is a ratio stating how many of one unit equal another. There are 1000 meters in 1 kilometer. There are 1609 meters in 1 mile. There are 3600 seconds in 1 hour. You write a conversion factor as a fraction:

$$\frac{1 \text{ km}}{1000 \text{ m}} \quad \text{or} \quad \frac{1 \text{ mile}}{1609 \text{ m}}$$

To convert a quantity from one unit to another, you multiply by the conversion factor (or its reciprocal) such that the unwanted units cancel out, leaving only the units you want.

Suppose you want to convert 80 meters to kilometers. You have meters; you want kilometers. You need a conversion factor that has meters in the denominator and kilometers in the numerator:

$$80 \text{ m} \times \frac{1 \text{ km}}{1000 \text{ m}} = \frac{80}{1000} \text{ km} = 0.080 \text{ km}$$

The meters cancel. You are left with kilometers. Simple.

Now suppose you want to convert a speed. A car travels at 60 miles per hour. What is that in meters per second? You have miles per hour. You want meters per second. You need two conversion factors: one to turn miles into meters, and one to turn hours into seconds.

$$60 \frac{\text{mi}}{\text{hr}} \times \frac{1609 \text{ m}}{1 \text{ mi}} \times \frac{1 \text{ hr}}{3600 \text{ s}} = \frac{60 \times 1609}{3600} \frac{\text{m}}{\text{s}} = 26.8 \frac{\text{m}}{\text{s}}$$

The miles cancel. The hours cancel. You are left with meters per second. The answer is 26.8 m/s.

**Dimensional analysis as a reality check**

Dimensional analysis is different. It is not about converting a number from one unit to another. It is about checking whether an equation could possibly be correct.

Every physical quantity has a *dimension*. Dimensions are built from seven base dimensions:

- **Length** — symbol $L$
- **Mass** — symbol $M$
- **Time** — symbol $T$
- **Temperature** — symbol $\Theta$
- **Electrical current** — symbol $I$
- **Amount of substance** — symbol $N$
- **Luminous intensity** — symbol $J$

Area has dimension $L^2$ (length times length). Volume has dimension $L^3$. Speed has dimension $L/T$ (length divided by time). Density has dimension $M/L^3$ (mass divided by volume).

The rule of dimensional consistency is simple: *every term in an equation must have the same dimension, and the dimensions on both sides of the equals sign must match*.

Suppose you have memorized two formulas and forgotten which is which:
- $\text{Circumference} = 2\pi r$
- $\text{Area} = \pi r^2$

One is the circumference of a circle; one is the area. Which is which? Dimensional analysis tells you.

The dimension of circumference is length: $[C] = L$. The dimension of area is $[A] = L^2$.

Now check the dimensions of the formulas. For $2\pi r$:

$$[2\pi r] = [\text{pure number}] \times [r] = 1 \times L = L$$

The dimensions match. This formula has dimension $L$, so it could be the circumference.

For $\pi r^2$:

$$[\pi r^2] = [\text{pure number}] \times [r]^2 = 1 \times L^2 = L^2$$

This formula has dimension $L^2$, so it must be the area.

Here is a more elaborate example. You are checking whether the equation $v^2 = 2as$ is dimensionally consistent. You know that $v$ is velocity (dimension $LT^{-1}$), $a$ is acceleration (dimension $LT^{-2}$), and $s$ is displacement (dimension $L$).

Left side: $[v^2] = (LT^{-1})^2 = L^2T^{-2}$

Right side: $[2as] = [a] \times [s] = LT^{-2} \times L = L^2T^{-2}$

Both sides have dimension $L^2T^{-2}$. The equation is dimensionally consistent. This does not prove it is *correct* — there could be a numerical error, a missed factor of 2, etc. — but it is at least possible that the equation describes a physical law.

If the dimensions do not match, the equation is wrong, period. You do not need to solve it. You can throw it out.

### Etymology — How dimensional analysis works

The technique of dimensional analysis comes from the principle of *homogeneity* in algebra. If you have an equation like $x + y = z$, then $x$, $y$, and $z$ must all have the same "kind" or dimension. You cannot add apples to oranges; they are different kinds of things. The same rule applies in physics. An acceleration (dimension $LT^{-2}$) cannot be added to a velocity (dimension $LT^{-1}$) because they are different kinds of quantities.

The terminology comes from 19th-century mathematicians and physicists who wanted to understand how equations behave under changes of scale. If you measure length in meters instead of feet, how does an equation change? If you measure time in seconds instead of hours? Dimensional analysis is the systematic study of this question.

### Trade-offs and limits

The power of dimensional analysis is its simplicity: you can check an equation without knowing its detailed derivation, and you can often catch errors in algebra or memory. The limit of dimensional analysis is that it cannot find dimensionless errors. If an equation should have a factor of $\pi$ and you forgot it, dimensional analysis will not catch it. Both $2\pi r$ and $2r$ have the same dimension (length), so dimensional analysis alone cannot tell you which is the circumference. You need to know (or derive) the numerical coefficient.

Dimensional analysis also cannot tell you about the sign of an equation. An equation $v = -at$ has the same dimensions as $v = at$, but the first one implies an object is speeding up in the negative direction while the second implies it is speeding up in the positive direction. Dimensions tell you the structure, not the direction.

### Scale shift — From atomic to human to cosmic distances

A hydrogen atom has a radius on the order of $5 \times 10^{-11}$ meters (50 picometers). A human is about 1.7 meters tall. The Earth's radius is about $6.4 \times 10^6$ meters. The distance to the Sun is about $1.5 \times 10^{11}$ meters (150 million kilometers, also called an astronomical unit). The distance to the nearest star (Proxima Centauri) is about $4 \times 10^{16}$ meters (about 4.2 light-years). The observable universe extends to about $8.8 \times 10^{26}$ meters (46 billion light-years, accounting for cosmic expansion).

Each step is a factor of 10,000 or more. The metric system handles all of these with the same base unit — the meter — and simple prefixes. This uniformity is one reason SI units have become universal.

### Worked example — Converting density and checking dimensional consistency

The density of aluminum is given as 2.7 g/cm³. Convert this to kg/m³.

We need to convert grams to kilograms and cubic centimeters to cubic meters. The conversion factors are:
- $1 \text{ kg} = 1000 \text{ g}$
- $1 \text{ m} = 100 \text{ cm}$, so $1 \text{ m}^3 = (100)^3 \text{ cm}^3 = 10^6 \text{ cm}^3$

$$2.7 \frac{\text{g}}{\text{cm}^3} \times \frac{1 \text{ kg}}{1000 \text{ g}} \times \frac{10^6 \text{ cm}^3}{1 \text{ m}^3} = \frac{2.7 \times 10^6}{1000} \frac{\text{kg}}{\text{m}^3} = 2700 \frac{\text{kg}}{\text{m}^3}$$

Dimensional consistency check: The dimensions on the left are $M/L^3$. The dimensions on the right are also $M/L^3$. They match. Good.

### Common misconceptions

**Misconception 1:** "Dimensional analysis tells you whether an equation is correct."

Fact: Dimensional analysis tells you whether an equation *could be* correct. An equation that is not dimensionally consistent is definitely wrong. An equation that *is* dimensionally consistent might still be wrong (wrong numerical factor, wrong sign, wrong physical law). Dimensional analysis is a necessary condition, not a sufficient one.

**Misconception 2:** "You have to use SI units. Other units are not allowed in physics."

Fact: You can use any unit system you want, as long as you are consistent. Some problems are easier in non-SI units. A problem about interplanetary distances might be easier in astronomical units (AU). A problem about atoms might be easier in ångströms (1 Å = $10^{-10}$ m). The key is that you declare your unit system and stick to it. Always — always — include units with every number.

**Misconception 3:** "Unit conversion is just algebra; there is nothing deep here."

Fact: Unit conversion is algebra, but it is algebra that catches errors. Many physics mistakes come from using the wrong units somewhere in a calculation and not noticing. By carefully writing out conversion factors and checking that units cancel, you catch errors before they become disasters. The Mars Climate Orbiter burned up because someone did not do this step.

---

## Concept 3 — Significant figures, accuracy, and precision: The limits of what you know

A measurement is not a pure number. It is a number plus uncertainty. When you measure the length of a table with a ruler, you are not reading off a true value. You are reading off a value that depends on how carefully you look, how good the ruler is, how straight the table is. Your result carries an uncertainty — a range within which the true value probably lies.

**Accuracy and precision**

Scientists distinguish between *accuracy* and *precision*. They sound like the same thing, but they are not.

*Accuracy* is how close a measurement is to the true value. If you measure the length of a piece of standard printer paper and you get 11.0 inches, and the paper actually is 11.0 inches long, then your measurement is accurate.

*Precision* is how close repeated measurements are to each other. If you measure the same piece of paper three times and get 11.1 inches, 11.2 inches, and 10.9 inches, your measurements are precise — they cluster tightly around an average value. If you measure it three times and get 11 inches, 13 inches, and 10 inches, your measurements are not precise — they scatter widely.

You can have accuracy without precision: imagine a broken bathroom scale that you adjust before each use. It might consistently read the correct weight (accurate), but if you stand on it multiple times without resetting it, the readings will scatter (not precise). Conversely, you can have precision without accuracy: imagine a thermometer that is consistently 5 degrees off. It reads 25°C when the true temperature is 20°C, reads 35°C when the true temperature is 30°C. Each individual reading is off by the same amount (precise), but they are systematically wrong (not accurate).

The best situation is both accurate and precise. The worst is neither.

**Reporting uncertainty**

When you report a measurement, you should state your uncertainty. If you measure a length and get 11.1 inches with an uncertainty of 0.15 inches, you write:

$$L = 11.1 \pm 0.15 \text{ inches}$$

This means: the length is somewhere between 10.95 and 11.25 inches, and 11.1 is your best estimate. The uncertainty can be expressed as an absolute amount (± 0.15 inches) or as a percent:

$$\text{Percent uncertainty} = \frac{\text{uncertainty}}{\text{measured value}} \times 100\% = \frac{0.15}{11.1} \times 100\% = 1.4\%$$

**Significant figures**

Significant figures are the digits in a measurement that are meaningful — that reflect the actual precision of the measurement. When you measure something with a ruler that is marked in millimeters, your measurement is precise to about 1 millimeter. An extra digit claiming precision to 0.1 millimeters is not meaningful; it is false precision.

The rule is: count digits starting from the leftmost non-zero digit up to the rightmost digit that reflects your actual precision.

Examples:

- 11.1 inches has 3 significant figures. All three digits are meaningful.
- 0.0025 kg has 2 significant figures. The leading zeros are placeholders; they do not count. Only the 2 and the 5 are significant.
- 1.50 m has 3 significant figures. The zero is meaningful; it is telling you that the measurement is known to the hundredths place.
- 1500 m is ambiguous. It could have 2, 3, or 4 significant figures, depending on whether the trailing zeros are meaningful or just placeholders. In scientific notation, this is unambiguous: $1.5 \times 10^3$ m has 2 significant figures; $1.50 \times 10^3$ m has 3.

When you multiply or divide, the result should have no more significant figures than the least precise measurement you started with. If you multiply 11.1 cm (3 sig figs) by 2.5 cm (2 sig figs), your result should have 2 sig figs:

$$11.1 \text{ cm} \times 2.5 \text{ cm} = 27.75 \text{ cm}^2 \rightarrow 28 \text{ cm}^2 \text{ (2 sig figs)}$$

When you add or subtract, the result should be no more precise than the least precise measurement. If you add 11.1 cm and 2.54 cm, the result is 13.64 cm, but since 11.1 cm is only known to the tenths place, your answer should be 13.6 cm.

$$11.1 \text{ cm} + 2.54 \text{ cm} = 13.64 \text{ cm} \rightarrow 13.6 \text{ cm}$$

### Etymology — Where "significant figures" comes from

The term "significant" here means "meaningful" — the digits that actually convey information about the quantity being measured. A leading zero in 0.025 is not significant because it is just a placeholder. It does not tell you how precisely the measurement was made. The 2 and the 5 are significant because they carry information.

The concept of significant figures emerged in the late 1800s and early 1900s as experimental physicists realized they needed a systematic way to communicate how precisely they had measured something. Before this, scientists often reported more digits than their measurements warranted, creating false precision.

### Trade-offs and limits

The advantage of significant-figure rules is simplicity: you can apply them mechanically without thinking deeply about your measurements. The disadvantage is that they are crude. A measurement known to 1 percent precision and a measurement known to 0.1 percent precision are treated differently by sig fig rules, but both are quite precise. A better approach is to always state your uncertainty explicitly (e.g., "the length is 11.1 ± 0.15 inches") rather than relying on sig figs alone.

Also, sig fig rules work best for multiplication and division. For addition and subtraction, they can be misleading. If you add a very large number to a very small number, significant figures might suggest you should round to match the precision of the large number — but you might be throwing away valuable information about the small number.

### Scale shift — From atomic to engineering measurements

The precision you can achieve varies wildly depending on what you are measuring. An atomic physicist using a scanning tunneling microscope can measure atomic positions to about 1 picometer ($10^{-12}$ m). A carpenter with a tape measure can measure to about 1 millimeter ($10^{-3}$ m). A GPS receiver can locate your position to about 5 meters. These differ by 17 orders of magnitude.

Similarly, precision as a *fraction* of what you are measuring varies. Measuring the width of a human hair (about 75 micrometers) to within 1 micrometer is a precision of about 1 percent. Measuring the Earth's circumference (about 40 million meters) to within 1 kilometer is also a precision of about 0.0025 percent. The absolute precision is wildly different; the relative precision is comparable.

### Worked example — Uncertainty propagation in a calculation

Suppose you measure the diameter of a sphere to be $d = 5.2 \pm 0.1$ cm and you want to calculate its volume. The volume of a sphere is:

$$V = \frac{4}{3} \pi r^3 = \frac{4}{3} \pi \left( \frac{d}{2} \right)^3 = \frac{\pi d^3}{6}$$

With $d = 5.2$ cm, the volume is:

$$V = \frac{\pi (5.2)^3}{6} = \frac{\pi \times 140.608}{6} = 73.6 \text{ cm}^3$$

Now, what is the uncertainty in the volume? For multiplication and division, you can use the method of adding percentages: the percent uncertainty in the result is approximately the sum of the percent uncertainties in the inputs. Here, the percent uncertainty in $d$ is:

$$\frac{0.1}{5.2} \times 100\% = 1.9\%$$

Since volume goes as $d^3$, the percent uncertainty in volume is approximately $3 \times 1.9\% = 5.7\%$. (The factor of 3 comes from the exponent in the formula.) The absolute uncertainty is:

$$\delta V = 0.057 \times 73.6 = 4.2 \text{ cm}^3$$

So you would report: $V = 73.6 \pm 4.2$ cm³, or $V = 73.6 \pm 5.7\%$ cm³.

### Common misconceptions

**Misconception 1:** "If I report 5 significant figures, my measurement is more accurate."

Fact: Reporting more digits does not make a measurement more accurate. If you measure something with a precision of 1 percent, reporting 8 digits is false precision. It misleads anyone reading your result into thinking you know more than you actually do. Report digits that correspond to your actual precision.

**Misconception 2:** "Accuracy and precision are the same thing."

Fact: Accuracy is how close you are to the true value. Precision is how close repeated measurements are to each other. A broken thermometer can be precise (it gives the same reading each time) but not accurate (the reading is wrong by a constant amount).

**Misconception 3:** "Uncertainty in a measurement means I did something wrong."

Fact: Every measurement has uncertainty. It is not a failure; it is a fact about the physical world. The best experimental physicists are those who carefully characterize their uncertainty, because that is how you know what your data actually tells you.

---

## Integration and synthesis — Why this matters for everything that comes next

The Mars Climate Orbiter burned up in 1999 because an engineer or team of engineers did not multiply by a conversion factor. This chapter is really about that: about the infrastructure of agreement that makes science possible. Physics is a language, and like any language, it has grammar. The grammar is units. Speak it carelessly, and your message does not arrive — or it arrives somewhere it was not meant to go, in this case, the Martian atmosphere.

The machinery is invisible once you have internalized it. You will stop thinking about units; they will become automatic. But they are always there. Every calculation you do from here on — force, energy, momentum, electric field — will be a calculation in SI units (or occasionally non-SI units that you explicitly choose). Every answer you write will carry units. Every number will be asked: what is your uncertainty? The habit of attention to units and precision is the foundation of experimental science.

The three concepts in this chapter — defining base units by physical constants, using conversion factors and dimensional analysis to translate between representations, and quantifying uncertainty through precision and significant figures — are the machinery of measurement. They are not exciting. They do not produce insights. But without them, every number you produce is suspect. With them, you can have confidence in your results.

From here forward: always write units. Always check dimensions. Always state your uncertainty. Do this, and you will avoid the largest class of physics mistakes. Do this, and you will be thinking like a physicist.

---

## Graduated exercises

**Warm-up: Recognizing SI base units and converting between them**

1. Identify which of the following are SI base units and which are derived:
   - meter (m)
   - newton (N)
   - kilogram (kg)
   - joule (J)
   - second (s)
   - watt (W)

2. Convert 45 km to meters.

3. Convert 2500 ms to seconds. (Hint: "milli" means $10^{-3}$.)

4. Express $3 \times 10^8$ meters using a metric prefix. (This is the distance light travels in one second.)

**Application: Unit conversion in multi-step problems**

5. A car travels at 65 miles per hour for 2 hours. How far does it travel in meters? (Use 1 mile = 1609 m.)

6. The density of mercury is 13.6 g/cm³. Convert this to kg/m³.

7. A water faucet flows at 2.5 gallons per minute. How many liters per hour is this? (Use 1 gallon = 3.785 L, 1 hour = 60 minutes.)

**Synthesis: Dimensional analysis and checking your work**

8. The period of a pendulum (the time it takes to swing back and forth once) is given by $T = 2\pi\sqrt{L/g}$, where $L$ is the length of the pendulum and $g$ is the acceleration due to gravity (9.8 m/s²). Check whether this equation is dimensionally consistent.

9. Which of the following equations is dimensionally consistent? ($v$ is velocity, $a$ is acceleration, $t$ is time, $s$ is displacement.)
   - $v = at$
   - $s = vt^2 + 0.5at$
   - $v^2 = 2as$

10. You measure the side of a square to be 5.3 ± 0.2 cm. What is the area of the square, and what is the uncertainty in the area?

**Challenge: Estimation and order of magnitude**

11. Estimate the number of seconds in your lifetime. (Use reasonable estimates for your age.)

12. The human body is roughly 60 percent water by mass. Estimate the mass of water in your body, in kilograms.

13. A Fermi estimation: How many piano tuners are there in New York City? Outline your reasoning step by step and state your assumptions explicitly.

---

## Chapter summary

**Base units define everything.** The SI system rests on seven base quantities (length, mass, time, temperature, electrical current, amount of substance, luminous intensity), each now defined by a physical constant. A second is 9,192,631,770 cesium oscillations. A meter is the distance light travels in 1/299,792,458 of a second. A kilogram is defined by Planck's constant. These definitions do not change; they are anchored to the laws of physics.

**Unit conversion requires care.** A conversion factor is a ratio expressing how many of one unit equal another. To convert a quantity from one unit to another, multiply by conversion factors such that unwanted units cancel and desired units remain. The Mars Climate Orbiter burned up because this step was skipped, with $325 million in consequences.

**Dimensional analysis is a reality check.** Every physical quantity has a dimension (built from length, mass, time, temperature, current, amount of substance, and luminous intensity). An equation can only be correct if the dimensions on both sides match. Dimensional analysis cannot prove an equation is correct, but it can quickly prove an equation is wrong.

**Precision and accuracy are not the same.** Accuracy is closeness to the true value; precision is closeness of repeated measurements to each other. Report measurements with explicit uncertainty: $L = 11.1 \pm 0.15$ m. Significant figures are a crude way to communicate precision; when possible, state uncertainty explicitly.

**Always check your units and your precision.** The difference between success and failure in experimental science is often the difference between careful attention to units and careless attention. Make this a habit from the start.

---

## What would change my mind

The redefinition of SI base units by physical constants is the current scientific consensus, but if it were discovered that Planck's constant or the speed of light change over cosmological time scales (which current physics says they do not), the definition of the kilogram and meter would need to be revisited. Similarly, if a dimensionless physical constant (like the fine-structure constant) were discovered to vary with time, the entire foundation of SI units would need recalibration.

---

## Still puzzling

I am uncertain about the practical implications of the 2019 redefinition for non-metrology laboratories and industry. The change from the Grand K to Planck's constant is conceptually elegant — a constant of nature rather than a physical artifact — but in day-to-day practice, most laboratories calibrate their scales by comparison to certified weights. The traceability chain ensures that these scales are as accurate as the Kibble balance, but I have not fully worked out the implications for measurement uncertainty in fields where the physical artifact (the old definition) mattered. How much has uncertainty actually changed at the millimeter and engineering scales?

---

## Tags

#units #measurement #SI-system #dimensional-analysis #significant-figures #Mars-Climate-Orbiter #Planck-constant #cesium-atom #uncertainty #physical-standards


---

## LLM Exercise — Chapter 2: Initialize the Toolkit

**Project:** *Physics Simulation Toolkit* — a Python repository where each of the 17 chapters contributes a clean, tested simulation of that chapter's signature physics, with conservation-law tests and benchmarks that empirically verify what the textbook proves analytically.

**What you're building this chapter:** The scaffolding — repo structure, unit system, dimensional-analysis utilities, and the testing harness every later chapter uses.

**Tool:** Claude Code (file creation, tests, git from one tool).

**The prompt:**

```
I am working through *University Physics — Mechanics, Waves, and the
Mathematics Behind Both* and building a Python simulation toolkit. This
is Chapter 2's setup task — scaffolding only.

Please scaffold a repository called `physics-simulation-toolkit` with
this structure:

- A top-level `README.md` explaining the project: one module per chapter,
  each with implementations, conservation-law tests, and benchmarks. The
  toolkit's purpose is to empirically verify what the textbook proves
  analytically.
- A `chapters/` directory with subdirectories named `ch02_units` through
  `ch19_sound` (skipping ch16, which is a section divider). Use the
  actual content chapter numbers: 02, 03, 04, 05, 06, 07, 08, 09, 10, 11,
  12, 13, 14, 15, 17, 18, 19.
- Each chapter directory: `README.md` (placeholder), `__init__.py`,
  `simulations.py`, `test_simulations.py`, `benchmarks.py`.
- A top-level `pyproject.toml` for Python 3.11+ with `numpy`, `scipy`,
  `matplotlib`, `pytest`, `pytest-benchmark`, `pint` (units library),
  `sympy` (for symbolic verification).
- A `Makefile` with `test`, `bench`, `lint` targets.
- A `.gitignore` for Python.

For Chapter 2 specifically (units and measurement):

1. `chapters/ch02_units/simulations.py` — a `Units` module wrapping
   `pint` with SI base units already configured (kg, m, s, A, K, mol, cd).
   Plus utility functions:
   - `assert_dimensionally_equal(a, b)` — raises ValueError if `a` and
     `b` have different dimensions
   - `to_sig_figs(value, n)` — round to n significant figures (handle
     units)
   - `fermi_estimate(low, high)` — geometric mean of two bounds, used
     for order-of-magnitude estimates

2. `test_simulations.py` — verify:
   - 1 mile + 1 km gives a length (not a TypeError)
   - 1 N + 1 lbf converts cleanly
   - `assert_dimensionally_equal(force, mass * acceleration)` passes
   - The Mars Climate Orbiter unit mismatch (lbf·s vs N·s) is detected
     and raises a clear error

3. `benchmarks.py` — measure unit-conversion overhead. The toolkit will
   carry units through every later simulation; the per-conversion cost
   should be < 100 microseconds.

4. `README.md` — replace the placeholder with a one-paragraph statement
   plus the *Mars Climate Orbiter* case: this is why we wrap units, not
   raw floats.

Initialize git, run `pytest -q` to confirm the scaffold passes,
commit as `ch02: scaffold repo and SI unit system`.

If I'm using a language other than Python (Julia, Rust, MATLAB), ask
before defaulting to Python.
```

**What this produces:** A committed repo with 17 chapter directories, a unit-aware `Units` module, four passing tests, and a benchmark for unit-conversion overhead. The Mars Climate Orbiter is the worked example in `test_simulations.py`.

**How to adapt this prompt:**

- *For your own project:* If your engineering domain uses imperial units routinely, configure `pint` to default to imperial. The dimensional checks survive either way.
- *For ChatGPT / Gemini:* Both can produce the scaffold. Without Claude Code's file-write loop, you'll be copy-pasting; ask for each file with the path commented at top.
- *For Claude Code:* Native fit. Let it run `pytest -q` itself before reporting done.
- *For a Claude Project:* Skip — Claude Code is the right tool.

**Connection to previous chapters:** None — this is the seed.

**Preview of next chapter:** Chapter 3 builds the vector library every later chapter uses — dot product, cross product, 3D vector algebra, with tests that empirically verify the algebraic identities.


---

##  AI Wayback Machine
The physics in this chapter didn't appear from nowhere. **Henrietta Swan Leavitt** was the discovery of the period-luminosity relation for Cepheid variable stars (1912) — the *yardstick of the universe*, the measurement technique that lets astronomers determine distances to galaxies — and despite the substance of the work, the name is far less recognized than it deserves. Here's a prompt to find out more — and then make it better.

**Run this:**

```
Who was Henrietta Swan Leavitt, and how does their work on the period-luminosity relation for Cepheid variables and the calibration of astronomical distances connect to units and measurement, especially the chain of inferences that lets us measure things we cannot directly visit? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Henrietta Swan Leavitt"** on Wikipedia after you run this. See what the model got right, got wrong, or left out.

**Now make the prompt better.** Try one of these:

- Ask it to explain *exactly* how Leavitt's 1912 observation of 25 Cepheids in the Small Magellanic Cloud established the period-luminosity relation, and what assumption made the inference work
- Ask: "Leavitt was deaf, paid $0.30 per hour as a 'human computer' at Harvard, and barred from operating the telescopes whose plates she analyzed. What did she actually do day-to-day, and what credit was withheld from her?"
- Add the framing: "Answer as if you're writing the historical-marker text at the Harvard College Observatory commemorating Leavitt's plates room"

What changes? What gets better? What gets worse?
