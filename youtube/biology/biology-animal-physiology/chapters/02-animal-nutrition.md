# Chapter 02 — Animal Nutrition


## TL;DR

- A hummingbird, a sailor, and a cat walk into a problem.
- The chapter moves through Learning objectives, Three stories, one puzzle, What "essential" actually means, What food actually supplies, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

*A hummingbird, a sailor, and a cat walk into a problem. The problem is the same.*

---

## Learning objectives

By the end of this chapter, you should be able to:

1. **Define** what makes a nutrient "essential" for a given species and **predict**, given two species, which essential nutrients differ between them.
2. **Distinguish** macronutrients from micronutrients by what they supply and **compute** the caloric content of a mixed meal from its macronutrient composition.
3. **Compare** the nutritional strategies of herbivores, carnivores, and omnivores, naming the trade-off each strategy makes between food quality and food quantity.
4. **Calculate** daily energy and protein requirements for three species at the same body mass and **explain** why caloric needs scale with mass but protein needs scale with feeding strategy.
5. **Diagnose** a classical deficiency disease (scurvy, rickets, beriberi, pellagra, taurine deficiency cardiomyopathy) by tracing the failure from missing molecule to broken tissue or pathway.
6. **Build and use** a nutritional-requirements calculator that compares dietary needs across species and **interpret** what happens to its outputs when one essential nutrient is set to zero.

Prerequisites: Chapter 00 (how to use the simulations); Chapter 01 (body plans, scaling, mass-specific metabolic rate — small animals burn energy faster per gram than large ones).

---

## Three stories, one puzzle

A male Anna's hummingbird weighs about 4 grams — the mass of two pennies. During the day it visits hundreds of flowers, drinking nectar that is mostly sucrose dissolved in water. On a busy day it consumes something close to its own body weight in nectar. At night it cannot feed. If it kept its daytime body temperature and metabolic rate through the night, it would exhaust its fuel reserves in about six hours and die before dawn. The solution: the hummingbird drops its body temperature into torpor — a controlled, reversible hypothermia — so it can stop spending energy it cannot replace. The arithmetic of this animal is unforgiving. A hummingbird is always a few hours from starvation.

In 1747 a British naval surgeon named James Lind ran what is usually called the first controlled clinical trial. He had twelve sailors with scurvy — bleeding gums, loose teeth, old wounds reopening, skin that bruised at a touch. He divided them into six pairs and gave each pair a different treatment: cider, sulfuric acid, vinegar, seawater, a paste of garlic and mustard seed, or two oranges and a lemon a day. Six days later the citrus pair were the only ones well enough to nurse the others. The molecule responsible was eventually isolated in the 1930s and named ascorbic acid — vitamin C. The interesting fact is not that citrus cured scurvy. It is this: most mammals do not get scurvy and would never need Lind's oranges. A rat synthesizes its own vitamin C from glucose. A dog does. A horse does. Humans, the other great apes, guinea pigs, capybaras, and most fruit-eating bats cannot. We lost the last enzyme in the synthesis pathway — gulonolactone oxidase — sometime between 40 and 60 million years ago in a primate ancestor. The gene is still in our genome, but it is broken. Vitamin C is essential for us not because of anything peculiar to the molecule, but because of something peculiar to our biochemistry.

In the late 1970s, veterinarians began seeing healthy cats develop dilated cardiomyopathy — heart muscle stretched, contractions weakened, blood pressure falling. The cats had one thing in common: they had been fed dog food or vegetarian alternatives, often by well-meaning owners. By 1987 Paul Pion and colleagues had identified the cause: taurine deficiency. Add taurine back and the heart muscle recovered. Most mammals — including dogs — synthesize all the taurine they need from the amino acid cysteine. Cats cannot make enough; they have lost the synthetic capacity almost entirely and must eat taurine. Taurine is found in animal muscle and viscera. Plants contain almost none. A cat fed an all-plant diet is a cat starving for a molecule it cannot make and cannot find in its food.

A hummingbird a few hours from starvation. A sailor whose collagen is falling apart. A cat whose heart is stopping. Three stories. One puzzle: an animal is not a generic eater of food. It is a specific chemical factory, with a specific list of inputs it cannot manufacture, running at a rate it cannot sustain without inputs at that rate. Nutrition is the matching problem — the matching of what an animal needs with what its environment supplies. To do nutrition seriously, you have to ask, for each animal: what does it need, and why can it not make it itself?

---

## What "essential" actually means

Pick vitamin C. Ask: is vitamin C an essential nutrient?

Honest answer: for whom?

An **essential nutrient** is a molecule that an animal's cells require for normal function but that the animal cannot synthesize from other things in its diet. Two halves to the definition. The first half — required for normal function — is mostly conserved across animals. Every animal needs the twenty standard amino acids. Every animal needs fuel it can burn for ATP. The second half — cannot be synthesized — is a fact about that animal's enzyme repertoire, and it is wildly variable across species.

A rat needs vitamin C; the rat's liver makes it from glucose via a four-step pathway whose last enzyme is gulonolactone oxidase. Vitamin C is not essential for the rat. Our gulonolactone oxidase gene is broken, so we have to eat the molecule. Same chemistry, different enzyme, different definition of essential.

The move worth holding onto: **"essential" is a property of the relationship between an animal and a molecule, not a property of the molecule alone.** A nutritionist who labels vitamin C "essential" without naming the species is doing incomplete work. The same is true for taurine — essential for cats, non-essential for dogs, same molecule, different biochemistry.

Once you see this, a pattern in animal nutrition makes sense. Carnivores tend to have *more* essential nutrients than herbivores. Why? Because eating meat is reliable supply. If your ancestors always ate arginine, every meal, for a hundred million generations, losing the arginine-synthesis pathway costs you nothing as long as the meal keeps arriving. Mutations that knock out the pathway accumulate. Cats have lost the ability to synthesize taurine, arachidonic acid, vitamin A from beta-carotene, and niacin from tryptophan, among others. Their enzymes for glucose handling have shifted toward near-constant gluconeogenesis from amino acids, because in the wild a cat almost never eats a carbohydrate-rich meal. A cat is not a small dog. It is a different chemical economy, built by a different evolutionary history of what was always available in the food.

---

## What food actually supplies

**Macronutrients** are the bulk constituents of food, eaten in tens to hundreds of grams a day.

**Carbohydrates** are chains of sugar units — usually glucose. Starch is glucose linked one way (digestible by mammalian enzymes); cellulose is glucose linked the other way (not digestible by mammalian enzymes). Carbohydrates supply roughly 4 kilocalories per gram.

**Proteins** are chains of amino acids and supply roughly 4 kilocalories per gram when used as fuel — but they are used primarily as building material. Of the twenty amino acids, animals can synthesize most. The rest are essential. For an adult human, the essential amino acids are eight: lysine, leucine, isoleucine, valine, threonine, methionine, phenylalanine, and tryptophan. For a cat the list is longer. For a sheep the practical list is shorter, because the microbes in its rumen synthesize amino acids the sheep then absorbs.

**Fats** supply roughly 9 kilocalories per gram — more than twice either carbohydrate or protein. They also supply two essential fatty acids that no animal synthesizes: linoleic acid (omega-6) and alpha-linolenic acid (omega-3). Animals can lengthen and desaturate these into longer-chain forms — arachidonic acid, EPA, DHA — but the starting molecules must come from food. Cats cannot do the lengthening of linoleic acid efficiently, so arachidonic acid itself becomes essential for them. They get it from animal tissue.

The caloric ledger: carbohydrate 4 kcal/g, protein 4 kcal/g, fat 9 kcal/g. Fat is dense. This single fact controls almost everything about how an animal stores energy and how predators choose prey.

**Micronutrients** are molecules and ions eaten in milligrams or micrograms a day, not used as fuel, but required as cofactors for enzymes or as structural components in specific tissues. They split into vitamins and minerals.

**Vitamins** are small organic molecules. Fat-soluble vitamins — A, D, E, K — dissolve in fats, are stored in liver and fatty tissues, and can accumulate to toxic levels. Too much vitamin A damages the liver; too much vitamin D raises blood calcium until soft tissues calcify. Water-soluble vitamins — the B-complex and vitamin C — dissolve in water, are excreted when intake exceeds need, and are not stored well. This is why the classical deficiency diseases live in the water-soluble category: you run out of them fast.

**Minerals** are inorganic ions — calcium and phosphorus for bone; iron at the center of hemoglobin; iodine in thyroid hormone; selenium activating glutathione peroxidase. Tiny amounts, specific jobs, predictable failure when absent.

The classical deficiencies are useful to learn as a set because each is a single missing molecule producing a single broken system.

**Scurvy** — vitamin C absent. Vitamin C is the cofactor for the enzymes that hydroxylate proline and lysine in collagen. Without those hydroxylations, the collagen triple helix does not stabilize. New collagen is weak. Old collagen, slowly replaced, fails. Gums bleed; wounds reopen; capillaries burst under their own pressure. Lind's sailors were dying because their connective tissue was unraveling, one uncrosslinked collagen triple helix at a time.

**Rickets** — vitamin D absent. Vitamin D drives intestinal calcium absorption. Without it, blood calcium falls; the parathyroid pulls calcium out of bone; growing bones soften and bow. The classical picture is bowed legs in a child raised indoors in a sunless city.

**Beriberi** — thiamine (B1) absent. Thiamine is the cofactor for pyruvate dehydrogenase, the enzyme that moves glucose-derived carbons into the TCA cycle. Without it, pyruvate piles up and ATP production from carbohydrate stalls. High-energy-demand tissues — heart muscle, peripheral nerves — fail first. Common in 19th-century East Asia after the introduction of milled white rice, which strips off the thiamine-rich bran.

**Pellagra** — niacin absent. Niacin is a precursor of NAD+, the electron carrier used everywhere energy is moved. Symptoms are the four Ds: dermatitis, diarrhea, dementia, death. Common in the early-20th-century American South when corn was the dietary staple — the niacin in corn is bound in a form the gut cannot absorb.

**Taurine cardiomyopathy** — taurine absent, in cats. Taurine plays a structural role in heart muscle that remains incompletely understood. What is established is that without it, in cats, the muscle fails.

Notice the shape of every explanation. Each disease is a machine missing a part. "Scurvy" is not the name of a disease — it is the name of a symptom set. The disease is: one enzyme cannot work because its cofactor is absent. Once you see it that way, a deficiency disease stops being a list to memorize and becomes a pattern to apply.

---

## How much an animal needs

Animals burn energy whether or not they are doing anything visible. The minimum rate at which an awake, resting, fasted mammal expends energy is its **basal metabolic rate** — BMR. The Kleiber rule, which we met in Chapter 01, says BMR scales as roughly the ¾ power of body mass:

$$\text{BMR (kcal/day)} \approx 70 \times M^{0.75}$$

where M is body mass in kilograms. The number 70 is a fitted average across mammals; species differ from it by roughly 20% in either direction.

The per-gram implication is worth deriving once. Divide both sides by M:

$$\frac{\text{BMR}}{M} \approx 70 \times M^{-0.25}$$

Mass-specific metabolic rate falls as the quarter-power of body mass. A 4-gram hummingbird has a per-gram rate roughly 25 times higher than a 70-kg human's. A 5,000-kg elephant's is lower still. The smaller the animal, the more energy it burns per gram, and the less time it can go without food. The hummingbird story is not a curiosity — it is the Kleiber rule made visible.

Total daily energy expenditure is BMR multiplied by an activity factor. A sedentary human uses a factor of about 1.2 to 1.4; moderate activity runs 1.5 to 1.7; an Iditarod sled dog in cold weather can reach 4 or above.

**Nitrogen balance** is the protein equivalent of the energy ledger — the difference between nitrogen eaten and nitrogen excreted. A growing animal is in positive nitrogen balance: eating more nitrogen than it excretes because it is building structure. A healthy maintenance adult is in zero balance. An animal starving or eating insufficient protein is in negative balance: breaking down its own muscle to supply amino acids for essential proteins it cannot do without. Nitrogen balance is how the body keeps the protein books.

---

## Three feeding strategies — and what each costs

Animals eat in different ways, and the difference is not cosmetic. The bodies are built around the strategy.

A **herbivore** eats plants. Plants are abundant — there is more plant biomass than animal biomass on Earth by orders of magnitude — but plant tissue is hard to process. Cell walls are cellulose, which mammalian enzymes cannot cut. Protein content is often low and unbalanced; water content is high; energy density per gram is low. A herbivore has solved this with two features. First, an enormous gut — long, often with elaborate chambers — to give food time to be extracted. Second, a microbial fermentation chamber housing bacteria and protists that do the cellulose chemistry the animal cannot do itself. The microbes ferment cellulose into short-chain fatty acids (acetate, propionate, butyrate) that the host absorbs; they also synthesize amino acids and B vitamins.

Two fermentation architectures dominate. **Foregut fermenters** — ruminants, cows, sheep, deer — have the fermentation chamber before the stomach. The food is fermented first, regurgitated and re-chewed (cud), then passed to the true stomach for acid digestion. **Hindgut fermenters** — horses, rabbits, elephants — have fermentation after the stomach and small intestine, in an enlarged cecum or colon. The trade-off is sharp: foregut fermenters extract more per mouthful but eat more slowly; hindgut fermenters process bulk volume fast but lose more nutrients in feces. Rabbits compensate by re-ingesting their soft feces — caecotrophy — a second digestive pass.

A **carnivore** eats other animals. Prey is dense: high in protein and fat, low in fiber, compositionally similar to the predator's own tissue. The gut can be short, simple, and fast. No fermentation chamber needed; the prey already synthesized the amino acids. Carnivores have lost synthesis pathways their herbivore relatives kept, because the lost pathways' products were always in the meal. Cats are the extreme case — **obligate carnivores**, animals biochemically committed to meat because they have lost so many synthesis pathways that animal tissue is not optional. They cannot synthesize taurine. Cannot synthesize arachidonic acid from linoleic. Cannot convert beta-carotene to vitamin A — they need pre-formed retinol. Cannot synthesize niacin from tryptophan at sufficient rate. Their glucose-handling enzymes run toward continuous gluconeogenesis from amino acids, because in the wild a carbohydrate-rich meal almost never arrives.

An **omnivore** eats both. Gut length is intermediate; dentition is **heterodont** — teeth of multiple kinds in one jaw, specialized for different jobs. Humans, pigs, bears, most monkeys. The strategy is flexibility: an omnivore can switch when one food type runs out. The cost is efficiency — a pig grinds leaves more slowly than a sheep; a pig hunts prey less effectively than a wolf. But the ability to switch is sometimes worth more than either specialist's edge.

Beyond these three:

**Filter feeders** strain small food particles from large volumes of water. Baleen whales lunge through krill swarms with mouths open, trapping crustaceans against keratinized baleen plates. Clams and oysters draw water across gills that double as sieves. Flamingos invert their heads and filter small crustaceans from shallow water. The strategy works wherever food is suspended at low concentration in a fluid the animal can move through.

**Fluid feeders** drink components of another organism. Mosquitoes, leeches, and ticks drink blood — dense in protein and iron, but iron-toxic in excess; blood feeders have specialized excretory machinery to dump the iron surplus. Hummingbirds and nectar bats drink nectar — energy-rich but protein-poor, so they supplement with small insects and pollen.

**Deposit feeders** swallow sediment and digest the organic material in it. Earthworms run soil through their gut, absorbing bacteria, fungi, and decomposing matter mixed with mineral particles. Sea cucumbers do the same on the ocean floor.

The organizing principle: feeding strategy determines the quality and quantity of food the animal must process, and the gut and teeth are the body's engineering answer to that processing problem. A carnivore's gut is short because its food is dense. A ruminant's gut is a four-chambered processing plant because its food is not. You can almost read a diet off a cross-section of the intestine.

---

## A worked example — three 70-kilogram animals

Three animals: a 70-kg human, a 70-kg large dog, a 70-kg sheep. Healthy adults, moderate activity. How much energy and protein does each need per day?

**Caloric requirements.** Using BMR = 70 × M^0.75 with M = 70 kg:

$$M^{0.75} = 70^{0.75} \approx 24.2 \qquad \Rightarrow \qquad \text{BMR} \approx 70 \times 24.2 \approx 1{,}700 \text{ kcal/day}$$

Now multiply by an activity factor:

- Human at moderate activity (factor 1.5): 1,700 × 1.5 = **2,550 kcal/day**
- Dog at moderate activity (factor 2.0 — dogs at this size are bigger movers): 1,700 × 2.0 = **3,400 kcal/day**
- Sheep grazing (factor 1.3): 1,700 × 1.3 ≈ **2,200 kcal/day**

Caloric requirements are within about 50% of each other. They are driven by body mass and activity — both roughly comparable here. This is the scale-driven part of nutrition.

**Protein requirements.** Here the species split shows up.

- Human: the established maintenance requirement is roughly 0.8 g of protein per kilogram of body weight per day. For 70 kg: **56 g/day**.
- Dog: roughly 2.5 to 3 g/kg/day of high-quality protein — about three times the human ratio. For 70 kg: **~200 g/day**. Why so much more? Carnivores run a chronic high rate of gluconeogenesis — they continuously manufacture glucose from amino acids, because in the ancestral diet carbohydrate-rich meals were rare. The amino acids burned for glucose are not recycled into protein; they are spent. The diet has to replace them.
- Sheep: roughly 1.3 g/kg/day of digestible protein, about **90 g/day**. But the sheep does not need to eat 90 g of high-quality protein. The microbes in its rumen synthesize amino acids from any nitrogen source — including non-protein nitrogen — and the sheep absorbs microbial protein in its small intestine. The sheep is eating low-quality plant protein at the front and absorbing high-quality microbial protein at the back. The microbes have done the quality upgrade.

The lesson: caloric requirements scale with mass. Protein requirements scale with feeding strategy. At the same body mass, the carnivore needs roughly three times the protein of the omnivore. The herbivore needs slightly more than the omnivore in absolute terms — but the herbivore's rumen microbes manufacture amino acids the carnivore has to eat pre-formed.

The limit of this calculation: these are population averages from feeding trials and metabolic chamber studies. Individuals vary by 20–30%. Growing animals, lactating ones, working sled dogs at −40°C, a sheep pregnant with twins — every life-stage adjustment shifts the numbers. These are maintenance values for healthy adults at moderate activity in temperate conditions. They are the right shape for comparison. They are not diets for individual animals.

---

## Common misconceptions

**"All animals need vitamin C in their diet."** Almost no animals need dietary vitamin C. Most mammals synthesize their own. Humans, great apes, guinea pigs, capybaras, and certain bats are the exceptions because they lost the synthesis enzyme. Scurvy is a human disease — and a guinea pig disease — precisely because it is not a universal mammal disease. The list of species that need to eat vitamin C is the list of species that lost the enzyme.

**"Plant protein is incomplete — you have to combine foods."** Partially right and mostly oversold. Some individual plant foods are lower in certain essential amino acids: grains tend to run low on lysine, legumes on methionine. But almost no real diet is a single plant food. A diet that includes grains, legumes, vegetables, and seeds eaten across a day supplies all eight essential amino acids comfortably for most adults. The strict "combine rice and beans at each meal" advice from 1971 was later walked back by its own author, Frances Moore Lappé, who noted the body's amino acid pool turns over slowly enough that within-day combining barely matters for adults on a mixed plant diet.

**"Carnivores need more food than herbivores."** Wrong, and almost backward. Per gram of body mass, a carnivore typically eats *less* than a herbivore, because meat is far more energy-dense than plant tissue. A lion eats 5 to 8 kg of meat after a kill and then rests for two or three days. A 500-kg horse on pasture consumes 10 to 12 kg of dry plant matter every single day, all day. The lion's daily intake is lower in absolute terms despite the larger body. Meat is dense fuel; grass is dilute fuel.

**"The essential nutrients are a fixed list."** They are species-specific and life-stage-specific. Vitamin C is essential for humans, not for rats. Taurine is essential for cats, not for dogs. Arachidonic acid is essential for cats, not for most mammals. Choline was reclassified as essential for humans in 1998 after decades of being considered non-essential. The list is a living scientific judgment, not a fixed truth.

---

## What would change my mind

If a controlled feeding study showed that a 70-kg adult dog on a maintenance ration of 50 g/day of high-quality protein maintained nitrogen balance and lean body mass over six months, I would revise my claim that carnivore protein requirements are roughly three times those of omnivores at the same body mass — at least for domestic dogs.

## Still puzzling

Why cats specifically have lost so many synthesis pathways while other carnivores — dogs, ferrets, mustelids — have kept more. The standard answer is "their ancestors ate enough meat that the pathways became neutral and drifted to loss." That is consistent with the data. It does not explain why the felid lineage drifted further than the canid lineage, given that wolves are also nearly exclusive carnivores. Why one carnivore family went obligate and the other stayed flexible is an open evolutionary question.

A second puzzle: how many other molecules currently classified as "non-essential" are, on closer examination, essential for specific subpopulations under specific conditions? Choline was non-essential for decades and then reclassified. The answer is almost certainly more than zero and almost certainly not yet fully cataloged.

---

## LLM Exercises

The simulation you will build for this chapter is **02-nutritional-requirements.html**. It compares dietary needs across species, with a species selector (human, cow, cat, rabbit, blue whale, hummingbird), an activity slider, and a body mass input. It displays daily energy requirement using allometric scaling, the macronutrient breakdown appropriate for that species, an essential nutrient requirements chart, a feeding-strategy diagram showing gut morphology type, the deficiency consequences when a nutrient is removed, and a comparison mode for energy density of different diets and the quantity of each that would be needed for the same caloric load.

These exercises use Claude Code or another capable coding LLM to help you build, explore, and extend the simulation. Each exercise uses a Show / Say / Constrain / Verify pattern. **Show** = paste source text and starter files. **Say** = give the precise build instruction. **Constrain** = name boundaries the LLM should not cross. **Verify** = check specific outputs against ground truth.

**Exercise 1 — Build the calculator**

*Show:* Paste this chapter and the worked example into the Claude Code context. Add the chapter's table of caloric densities (carbs 4 kcal/g, protein 4 kcal/g, fat 9 kcal/g) and the BMR formula (BMR = 70 × M^0.75 kcal/day).

*Say:* "Build a single-file HTML+JavaScript simulation called 02-nutritional-requirements.html. It must include a species dropdown (human, cow, cat, rabbit, blue whale, hummingbird), a body mass input in kilograms with a sensible default for each species, and an activity slider from 1.0 (basal) to 4.0 (extreme). On any change, display: (a) daily energy requirement using the allometric BMR formula multiplied by activity, (b) the macronutrient breakdown in grams per day for that species, (c) a list of essential nutrients with daily requirements, (d) a small SVG sketch of the gut morphology type (carnivore short / omnivore intermediate / hindgut / ruminant / filter / nectar), and (e) a 'remove nutrient' button next to each essential nutrient that, when pressed, displays the deficiency disease and timeline. Plain HTML/CSS/JS, no frameworks."

*Constrain:* No fabricated numbers — every species' macronutrient and essential-nutrient requirement must be cited inline as a code comment with the reference (use the NRC publications cited in this chapter as the default). If a number is uncertain, use a `[verify]` placeholder in the displayed UI rather than inventing a value. Do not invent gut anatomy — restrict the gut-morphology diagrams to the five strategies described in the chapter plus filter-feeder.

*Verify:* Open the file in a browser. Select "human, 70 kg, activity 1.5." The calorie display should land near 2,550 kcal/day (within 10%) and the protein display should land near 56 g/day. Now select "dog, 70 kg, activity 2.0" — calories should land near 3,400 kcal/day and protein near 200 g/day. If either is off by more than 20%, ask the LLM to show you the calculation it used and correct the constant.

**Exercise 2 — Explore the comparative space**

*Show:* Use the simulation you built in Exercise 1.

*Say:* "Set up a sequence of four side-by-side scenarios: (a) 4-g hummingbird at activity 3.0; (b) 70-kg human at activity 1.5; (c) 500-kg horse at activity 1.5; (d) 100,000-kg blue whale at activity 1.5. Record the daily caloric requirement and the kcal-per-gram-of-body-mass for each. Now ask Claude to explain why the per-gram rate scales the way it does and what the mathematical relationship is between body mass and per-gram metabolic rate."

*Constrain:* When Claude offers an explanation, ask it to derive the scaling from BMR = 70 × M^0.75 by dividing both sides by M. The relationship per-gram rate ∝ M^(−0.25) should fall out algebraically. Reject any explanation that asserts the relationship without showing this step.

*Verify:* Plot the per-gram rates on log axes against body mass on log axes. The slope should be approximately −0.25. If it is not, either the simulation's BMR formula is wrong or the model is computing something other than what you asked. Diagnose which.

**Exercise 3 — Compare three LLMs on a comparative question**

*Show:* Paste this prompt into Claude, ChatGPT, and Gemini separately:

> "I have three 70-kg mammals: a human, a dog, and a sheep. All are healthy adults at moderate activity. Calculate the daily caloric and protein requirements for each. Then explain in mechanistic terms why the protein requirements differ even though the caloric requirements are similar. Do not paper over the difference by saying 'metabolism varies.' Name the specific biochemical pathway that causes the carnivore to need more protein."

*Say:* Compare the three responses on three axes: (a) numerical accuracy against the worked example in this chapter, (b) whether the model names *gluconeogenesis from amino acids* as the carnivore's high-protein driver, (c) whether the model correctly identifies the sheep's *rumen microbial protein synthesis* as the herbivore's quality-upgrade trick.

*Constrain:* Score each model on those three axes only. Ignore stylistic polish. Ignore length. Ignore confidence of tone.

*Verify:* The right answer to (b) is gluconeogenesis — carnivores burn amino acids for glucose because their ancestral diet was glucose-poor. The right answer to (c) is microbial protein synthesis in the rumen. A model that gets the numbers right but misses the mechanisms is doing arithmetic, not physiology.

**Exercise 4 — Extend to Chapter 03**

*Show:* The bridge to Chapter 03 is the digestive system itself. Each feeding strategy implies a gut design.

*Say:* "Take the gut-morphology diagram from your simulation in Exercise 1. Add a 'gut length' display (in meters) and a 'transit time' display (in hours) for each species. The relationships are: carnivore short gut (~3 m), fast transit (~10 h); omnivore medium gut (~6–8 m), medium transit (~24 h); ruminant long with multiple chambers, very slow transit (~36–72 h); hindgut fermenter long with enlarged cecum, slow transit (~24–48 h)."

*Constrain:* Use the ranges as ranges, not single numbers. The animal-to-animal variation is real and important.

*Verify:* The transit times you display should approximately predict the consequences of toxic food. A carnivore that eats spoiled meat usually expels it within hours via vomiting or diarrhea; a ruminant cannot do this — once material is in the rumen it must work through several chambers, and the animal is committed. Check that the simulation's transit times make this physiological constraint visible to the student.

---

*Byline: Nik Bear Brown*

*Tags:* essential-nutrients, feeding-strategies, comparative-nutrition, allometric-scaling, vitamin-deficiency-diseases
