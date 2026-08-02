# Chapter 12 — The Digestive System and Metabolism

*Suggested titles:*
1. The Factory and the Ledger — How a Tube Disassembles a Sandwich and a Body Decides What to Do With the Pieces
2. From Mouth to Mitochondrion — Digestion, Absorption, and the Fed-Fasted Switch
3. One Tube, Two Ledgers — The Digestive System and the Hormone Pair That Spends or Saves Every Calorie

---

## TL;DR

The digestive system is a single tube whose chemistry, motility, and architecture change at every step so that complex food molecules — too large to cross any cell membrane — get cleaved into monomers small enough to absorb. Once absorbed, those monomers run into a second system, the insulin-glucagon switch, that decides whether to spend them for ATP right now or store them as glycogen and fat — and almost every clinical disease of digestion and metabolism, from celiac to Type 2 diabetes, is one specific machine in that two-stage pipeline failing in a specific, diagnosable way.

---

## Learning objectives

By the end of this chapter, you will be able to:

1. **Trace** a mixed meal — carbohydrate, protein, fat — from mouth to bloodstream, naming the enzyme, the secretion, and the segment of the tube that handles each macronutrient at each step.
2. **Explain** why glucose and amino acids enter the portal circulation while dietary fat enters the lymphatic system, and **predict** the clinical consequence of that routing difference after a high-fat versus a high-carbohydrate meal.
3. **Diagram** the structural amplification of intestinal surface area (circular folds → villi → microvilli) and **predict** the absorptive consequence of villus blunting in celiac disease.
4. **Distinguish** the absorptive (fed) state from the postabsorptive (fasted) state at the level of dominant hormone, dominant pathway in the liver, and direction of glucose flux.
5. **Localize** the lesion in a malabsorption syndrome (cystic fibrosis, celiac, cirrhosis, lactase deficiency) by reading which step in the digest-absorb-store pipeline has failed.
6. **Build and run** a nutrient-absorption simulator and **interpret** its outputs against the clinical states of celiac, pancreatic insufficiency, and metabolic syndrome.

Prerequisites: the insulin/glucagon section of Chapter 8 (you should know what beta cells and alpha cells do, and that insulin and glucagon oppose each other); the cell-membrane and transporter logic from Chapter 2 (you should be comfortable with active transport and the Na⁺/K⁺ ATPase); the muscle-fuel concepts from Chapter 5 (glucose vs. fatty acids for ATP).

---

## A genuine puzzle to start with

It is June 12, 1984. A 32-year-old physician in Perth, Western Australia, walks into his laboratory on a weekday morning, picks up a Petri dish containing a slurry of bacteria he has cultured from a patient's stomach biopsy, swirls it in beef broth to make it palatable, and drinks it. He has not told the hospital ethics board. He has not told his wife. He gets a baseline endoscopy first, just to be honest about it. The bacteria's name — at that point — is *Campylobacter pyloridis*. The world will eventually call them *Helicobacter pylori*.

For sixty years before this morning, the orthodoxy in gastroenterology was that peptic ulcer disease was caused by stress and acid. Stomachs were too acidic, the textbook said, for any bacterium to survive there. Patients with ulcers were treated with antacids, sometimes with vagotomies — surgical severing of the nerve that drives gastric acid secretion — and were told to eat blandly and worry less. Many of them still suffered. Some of them died from perforated ulcers eating through the stomach wall.

Barry Marshall and his pathologist colleague Robin Warren had been arguing, since 1982, that bacteria were causing the ulcers — bacteria they had repeatedly cultured from the stomach lining of ulcer patients and almost never from healthy controls. Nobody believed them. The reviewers at major journals rejected their papers. So Marshall did what scientists who have run out of patience occasionally do: he made himself the experimental subject.

By day five he had developed gastritis on the lab bench. By day ten his breath smelled of putrid milk and his wife noticed he was vomiting clear fluid in the mornings. A repeat endoscopy showed extensive inflammation of the gastric mucosa and bacterial colonization. He treated himself with antibiotics, the gastritis resolved, and he and Warren had — finally — direct evidence that a bacterium could colonize the human stomach and cause disease. Twenty-one years later, in 2005, they shared the Nobel Prize in Medicine.[^marshall-nobel]

[^marshall-nobel]: Barry J. Marshall, "Helicobacter Connections" (Nobel Lecture, December 8, 2005). [https://www.nobelprize.org/prizes/medicine/2005/marshall/lecture/](https://www.nobelprize.org/prizes/medicine/2005/marshall/lecture/)

Hold this story in mind. It is doing two pieces of work for us at once. First, it tells you something about the stomach that any textbook of human physiology will repeat: the stomach is acidic enough — pH 1.5 to 3.5, roughly the pH of battery acid — that the conventional wisdom was correct that almost nothing biological can live there. Marshall's bacterium is the exception, not the rule. It survives by burrowing under the mucus layer and secreting urease, an enzyme that splits urea into ammonia and bicarbonate, locally neutralizing the acid around itself. The bacterium does not refute the acid environment of the stomach; it solves the acid environment of the stomach by carrying its own buffer.

Second — and this is the larger point — Marshall's experiment is a reminder of what it means to take a digestive disease seriously as a mechanism rather than as a label. "Peptic ulcer disease" sounds like an entity. It is not. It is the consequence of a specific failure: the protective mucus layer that keeps the stomach from digesting itself has been breached, and the same enzymes and acid that are supposed to be digesting food are now digesting tissue. The breach can come from an infection (most ulcers, *H. pylori*); from chronic suppression of mucus production (chronic NSAID use); from acid hypersecretion (Zollinger-Ellison syndrome, where a tumor secretes gastrin and the stomach goes into hyperdrive). Three different first causes, one downstream pathology, one tube doing what it is built to do on a surface it was not supposed to reach.

Every chapter of clinical gastroenterology works like this. The digestive system is a chemical assembly line; the diseases are the assembly line malfunctioning in specific ways at specific stations. To diagnose anything you have to know what is supposed to happen at each station. So that is where we start.

---

## The problem digestion solves

Your cells do not eat food. They eat *molecules* — glucose, amino acids, fatty acids, glycerol, and ions. What arrives in your mouth is starch, protein, fat, and fiber — long polymers and large aggregates, none of which can cross a cell membrane.

This is the constraint. The intestinal epithelium is a single layer of cells whose apical (luminal) membrane is a lipid bilayer about five nanometers thick. The tight junctions between epithelial cells are sealed — they leak ions and water under controlled conditions but they do not pass large molecules. So anything that is going to be absorbed has to either dissolve in the lipid bilayer (which means hydrophobic and small) or fit through a specific transporter protein (which means small, with a specific shape the transporter recognizes). A whole protein, a chain of dozens to thousands of amino acids, fits neither criterion. A triglyceride, a glob of three long fatty acid chains wrapped around glycerol, fits neither criterion. A starch molecule, hundreds to thousands of glucose units linked together, fits neither criterion.

So digestion is, at its core, a *size reduction problem*. The polymers in food have to be cleaved into their monomers. Starch into glucose. Protein into amino acids. Triglyceride into fatty acids and monoglycerides (a glycerol with one fatty acid still attached). And those monomers have to be liberated in the right place, with the right transporters waiting, with the right blood supply downstream to carry them away.

You might ask: why does the body do this disassembly-then-reassembly cycle? Why not just absorb intact proteins and use them directly? The answer is two-fold. *Selectivity*: by cleaving proteins down to their constituent amino acids, the body decouples itself from the structure of whatever organism it just ate. It does not have to know what a cow's albumin or a peanut's storage protein looks like — it just absorbs the twenty amino acids and rebuilds whatever proteins it needs. And *immunity*: an absorbed foreign protein would be recognized by the immune system as something to attack. Aminoacid-by-aminoacid absorption strips the food of its molecular identity at the customs gate.

That sounds clean. It is not always clean — celiac disease is what happens when a particular fragment of wheat gluten makes it through the gate partially undigested and the immune system finds it. We will come back to celiac. But the design intent is clear: the digestive system reduces food to a generic monomer-soup before it lets anything cross the wall.

The size reduction is achieved by enzymes — *hydrolases*, which break specific chemical bonds with the addition of a water molecule across the bond. Amylase hydrolyzes the bond between two glucose units in starch. Proteases hydrolyze the peptide bonds between amino acids. Lipases hydrolyze the ester bonds linking fatty acids to glycerol. Each enzyme cleaves a specific kind of bond. Each enzyme works best at a specific pH. And different enzymes are released into different segments of the tube at different times. The tube's job is to stage the chemistry — to make sure each enzyme meets its substrate in the right environment.

---

## The tube, modified at each step

The gastrointestinal tract is one continuous tube, mouth to anus, roughly eight meters long in a living adult. The same four-layer wall — mucosa, submucosa, muscularis, serosa — runs the whole length, but the details of each layer change dramatically from segment to segment to match what each segment does.

A quick orientation. The **mucosa** is the innermost layer, facing the lumen — this is where epithelial cells secrete enzymes and absorb nutrients. The **submucosa** is a layer of connective tissue beneath, carrying blood vessels, lymphatics, and one of the two enteric nerve plexuses. The **muscularis** is the smooth muscle layer, in most regions two sublayers (inner circular, outer longitudinal) that together drive peristalsis. The **serosa** is the outer wrapping, a thin layer of connective tissue and squamous epithelium that lets the tube slide against neighboring organs without friction. Embedded between the muscularis and the submucosa is the **enteric nervous system** — roughly 500 million neurons, more than the spinal cord contains — that coordinates contraction, secretion, and local blood flow without input from the brain.[^ens-count] Sometimes called the "second brain," it can produce peristalsis in an isolated segment of gut with all extrinsic nerves cut.

[^ens-count]: Furness, J. B. (2012). "The enteric nervous system and neurogastroenterology." *Nature Reviews Gastroenterology & Hepatology* 9, 286–294. [https://doi.org/10.1038/nrgastro.2012.32](https://doi.org/10.1038/nrgastro.2012.32)

Now walk the length of the tube.

The **mouth** is the first processing step. Teeth crush food into smaller pieces — pure mechanical work, but mechanically critical, because every subsequent chemical step depends on surface area, and chewing increases the surface area of a bite of food by perhaps a hundredfold. Three pairs of salivary glands (parotid, submandibular, sublingual) deliver about 1.5 liters of saliva per day. Saliva is mostly water, with mucus for lubrication, lysozyme for some antibacterial defense, and **salivary amylase** — the first enzyme of digestion, which begins hydrolyzing starch into shorter chains. By the time you swallow, perhaps five percent of the starch has been converted to maltose and other oligosaccharides. Not much, but a head start.

The **esophagus** is transport only. A muscular tube that uses peristalsis — sequential contraction of circular smooth muscle behind the bolus, relaxation ahead of it — to push food from pharynx to stomach in about ten seconds. A *bolus*, in this context, is the soft chewed mass of food a swallow delivers; the word is worth learning because it reappears every time we talk about what is moving through the tube. The lower esophageal sphincter, a thickened ring of muscle at the bottom, keeps stomach contents from refluxing back up. When it fails — through anatomical hernia, alcohol, certain foods that relax the sphincter, or just chronically — acid reaches the esophageal lining, which has no protective mucus layer, and the burning sensation you call heartburn is chemical injury to the epithelium.

The **stomach** is where chemistry begins in earnest. The stomach is a J-shaped muscular sac with three roles: it stores food (you can eat a meal in five minutes but the digestion takes hours, so something has to buffer the rate), it churns food (the muscularis here has an extra oblique layer that allows multi-directional grinding), and it begins protein digestion.

The gastric epithelium is studded with **gastric pits** — little invaginations leading down to gastric glands. The glands contain three specialized cell types, each secreting one thing.

- **Parietal cells** secrete **hydrochloric acid**, bringing the stomach lumen to a pH of 1.5 to 3.5. They do this by pumping protons across their apical membrane using an H⁺/K⁺ ATPase — the same molecular pump that proton pump inhibitor drugs (omeprazole and its relatives) block when they are used to treat ulcers and reflux. Parietal cells also secrete **intrinsic factor**, a glycoprotein that binds vitamin B12 and is required for B12 absorption far downstream in the ileum. Without intrinsic factor, B12 absorption collapses — which is why patients who have had their stomachs partially removed develop B12 deficiency over years.
- **Chief cells** secrete **pepsinogen**, an inactive precursor that the gastric acid cleaves into the active protease **pepsin**. Pepsin is unusual in that it works at the very low pH of the stomach — most proteases need near-neutral conditions. It begins cleaving the peptide bonds of proteins, breaking them into shorter peptide fragments. The release of pepsinogen as a zymogen — an inactive precursor — rather than as active pepsin is the same protective trick the pancreas uses with its proteases: you don't want the enzyme active inside the cell that made it.
- **Mucous cells** secrete a thick, bicarbonate-rich mucus layer that coats the stomach wall and keeps the acid and pepsin from digesting the stomach itself. This is the protective barrier *H. pylori* burrows under. This is the layer chronic NSAID use depletes. When the mucus layer fails, peptic ulcer disease follows in days to weeks.

Two things to notice. First, the stomach does not absorb much. A few things diffuse across — water, alcohol, some drugs like aspirin — but the stomach is built for chemical attack and storage, not absorption. Second, the stomach has barely touched the carbohydrates and almost not at all touched the fats. Salivary amylase, the carb-digesting enzyme from the mouth, is inactivated by acid almost as soon as it hits the stomach (it needs near-neutral pH to function). Fats just sit there in large globules; there is no lipase active in the stomach to speak of in adults. Protein, and only protein, is meaningfully digested in the stomach. The rest is staged for downstream.

The stomach churns and mixes for two to four hours, depending on meal composition. Fatty meals take longest — fat slows gastric emptying through hormonal feedback, because the small intestine needs time to process it. The pyloric sphincter, the muscular valve at the stomach's outlet, opens in small pulses, releasing about 3 mL of **chyme** — the technical name for the soupy, acidic, partially digested mixture leaving the stomach — into the duodenum at a time. The duodenum could not handle a stomach's worth of acid in one go. The pyloric drip-feeds.

---

## The small intestine: where the real work happens

The **small intestine** is six meters of tube, divided into three regions: the **duodenum** (the first 25 centimeters, where pancreatic and biliary secretions enter), the **jejunum** (the next two and a half meters, where most absorption occurs), and the **ileum** (the final three and a half meters, where vitamin B12 and bile salts are reclaimed). This is the workhorse. Essentially every macronutrient you absorb, you absorb here.

The first thing to notice about the small intestine is its astonishing surface area. The inner wall is folded at three nested length scales.

- **Circular folds** (also called plicae circulares) — visible to the naked eye, ring-shaped projections of the entire wall into the lumen, increasing surface area roughly threefold.
- **Villi** (singular: villus, Latin for "shaggy hair") — finger-shaped projections of the mucosa, about 0.5 to 1.5 millimeters tall, increasing the surface another tenfold. Each villus has a core containing a blood capillary network and a single central lymphatic vessel called a **lacteal**. The word *lacteal* comes from *lac*, milk — because after a fatty meal, the lacteals fill with chylomicron-laden lymph that looks white and milky.
- **Microvilli** — submicroscopic projections of the apical membrane of each epithelial cell, packed so densely they form a "brush" appearance under the electron microscope. Increase surface another twenty- to thirty-fold. This is the **brush border** — the technical name for the microvillus-covered apical surface of intestinal enterocytes, and the membrane in which the final-step digestive enzymes are embedded.

Multiply the amplifications: roughly 3 × 10 × 25 ≈ 750-fold. The bare tube would have a surface area of about 0.3 m². The fully folded intestine has a surface area between 200 and 400 m².[^surface-area] That is roughly a tennis court of absorptive surface, packed into a tube three centimeters across folded into your abdomen.

[^surface-area]: Helander, H. F., & Fändriks, L. (2014). "Surface area of the digestive tract – revisited." *Scandinavian Journal of Gastroenterology* 49(6), 681–689. (The "tennis court" figure of 300 m² is widely cited; this paper revises it somewhat downward to around 30–40 m² based on more direct measurements. The order-of-magnitude conclusion — that the small intestine has dramatically more surface area than a bare tube — is unchanged.) [https://doi.org/10.3109/00365521.2014.898326](https://doi.org/10.3109/00365521.2014.898326)

That surface area is the answer to the engineering problem stated at the top of the chapter. You have a few hours to absorb everything from a meal before it passes out of the small intestine. The only way to absorb that much material that fast is to have an enormous contact surface. The only way to fit that much surface inside a living body is to fold it three times over.

This is why celiac disease is so devastating. The autoimmune reaction to gluten flattens the villi — they "blunt," becoming low ridges instead of finger-like projections. The microvilli on the surviving epithelium are also damaged. Total absorptive surface can fall by 80 to 90 percent. The patient eats normally and starves anyway, because the dining table has been disassembled.

### Pancreatic juice — the enzyme cocktail

When chyme arrives in the duodenum, two organs upstream of the gut wall — the pancreas and the liver — deliver their secretions through ducts that converge at the same point in the duodenal wall.

The **pancreas** is a glandular organ tucked behind the stomach. Most of it (the exocrine pancreas) is dedicated to producing digestive enzymes; a small fraction (the endocrine pancreas, the islets of Langerhans you met in Chapter 8) makes insulin and glucagon. The exocrine pancreas releases pancreatic juice — roughly 1.5 liters per day — into the pancreatic duct, which empties into the duodenum.

Pancreatic juice contains two essential components.

First, **bicarbonate** — a wave of alkaline fluid that neutralizes the acidic chyme arriving from the stomach. Without this, the pH of the duodenum would stay around 2, and no pancreatic enzyme would function (they all need near-neutral pH). The bicarbonate raises the duodenal pH from about 2 to about 7 within minutes of chyme arrival.

Second, **the enzyme arsenal**.

- **Pancreatic amylase** — resumes the starch digestion that salivary amylase started and the stomach interrupted. Cleaves starch into shorter oligosaccharides and disaccharides (mostly maltose, a glucose-glucose pair).
- **Pancreatic lipase** — attacks triglycerides, cleaving off two of the three fatty acid chains and leaving a monoglyceride. This is the only meaningful lipase in adult digestion; almost all dietary fat absorption depends on it. Pancreatic insufficiency, as in cystic fibrosis, removes this enzyme and produces *steatorrhea* — fat in the stool. We will come back to that.
- **Pancreatic proteases** — trypsin, chymotrypsin, elastase, and the carboxypeptidases. Each cleaves peptide bonds at specific amino acid sequences, attacking proteins from multiple angles and producing short peptides and free amino acids.

The proteases are released as **zymogens** — inactive precursors — and activated only after they reach the duodenal lumen. Trypsinogen is converted to trypsin by an intestinal brush-border enzyme called enterokinase; trypsin then activates the other zymogens in a cascade. This is the same defensive trick the stomach uses with pepsinogen: if the enzymes were active inside the cell that synthesized them, they would digest the pancreas itself. **Pancreatitis** is what happens when this safety mechanism fails — zymogens get activated prematurely within pancreatic tissue, and the pancreas begins to digest itself. It is exquisitely painful and can be fatal.

The release of pancreatic juice is coordinated by two hormones secreted by enteroendocrine cells in the duodenal wall.

- **Secretin** is released when the duodenum detects acidic chyme. It travels in the bloodstream to the pancreas and triggers the release of bicarbonate. (It also slows gastric emptying — telling the stomach to ease up on acid delivery until the duodenum has caught up.)
- **Cholecystokinin** (abbreviated CCK; the name comes from the Greek for "gallbladder-mover") is released when the duodenum detects fat and protein in chyme. CCK does two things: it contracts the gallbladder, releasing bile into the duodenum, and it triggers the pancreas to release its enzyme cocktail.

So acidic chyme arriving in the duodenum sets off, within seconds, two parallel signals — secretin and CCK — that within minutes have summoned exactly the secretions needed to neutralize the acid, emulsify the fat, and digest the carbohydrates, proteins, and fats. Three hormones, two organs, one coordinated chemical attack.

There is a third hormone you should know about: **gastrin**, released by enteroendocrine cells in the stomach itself when proteins arrive. Gastrin stimulates the parietal cells to make more acid and the chief cells to release more pepsinogen — it's the positive-feedback signal that ramps up gastric digestion when there is food to digest. Zollinger-Ellison syndrome, mentioned earlier, is what happens when a tumor secretes gastrin autonomously: the stomach is in permanent hyperdrive, acid output is massive, and ulcers form aggressively.

### Bile — the lipid emulsifier

The **liver** continuously produces about 0.5 liters of bile per day. Bile is a yellow-green fluid that is mostly water, with bile salts, cholesterol, bilirubin (the breakdown product of hemoglobin), and electrolytes. The bile salts are the functional component. They are *amphipathic* — molecules with a hydrophobic end and a hydrophilic end, like a tiny tadpole — synthesized by the liver from cholesterol.

Between meals, bile drips down the bile duct into the **gallbladder**, a small sac under the liver, where it is concentrated and stored. When CCK arrives (signaling that fat has reached the duodenum), the gallbladder contracts and squirts the concentrated bile into the duodenum through the bile duct, which joins the pancreatic duct just before they enter the duodenum.

In the duodenum, the bile salts do something specific and necessary: they **emulsify** fat. Dietary fat enters the small intestine as large globules — picture droplets of olive oil floating in water. These globules have very little surface area exposed to water-soluble enzymes; pancreatic lipase, which is water-soluble, can only attack the surface of a fat globule. A few large droplets have a tiny total surface. Many tiny droplets have a vast total surface.

The bile salts coat the large fat globules. Their hydrophobic tails embed in the fat; their hydrophilic heads face outward into the watery intestinal fluid. The mechanical agitation of segmentation (the small intestine's mixing motion) breaks the coated globules into smaller and smaller droplets — emulsion droplets a few micrometers across — and the bile salts prevent them from coalescing back together. Surface area increases dramatically. Lipase can now attack from every direction at once.

Emulsification is not chemical digestion. The triglyceride molecules have not been cleaved. But without emulsification, lipase cannot work fast enough to digest a meal's worth of fat in the time available. Bile is the engineering solution to a surface-area problem.

After lipase has worked, the products — fatty acids and monoglycerides — are still hydrophobic and would clump back together if left alone. So the bile salts perform a second trick: they aggregate with the lipase products, phospholipids, and cholesterol into tiny structures called **mixed micelles** — spherical aggregates about 5 nanometers across, with the hydrophobic cargo in the interior and the bile salt heads facing outward. The micelles are stable in water and small enough to diffuse to the brush border, where they deliver their cargo for absorption.

The bile salts themselves are not absorbed with the fat. They are recycled. Bile salts pass through the small intestine doing their detergent job and are absorbed almost completely in the terminal ileum, where they re-enter the portal blood and return to the liver. This is the **enterohepatic circulation** — the bile salt pool is reused five to ten times per meal. A patient who has had their terminal ileum surgically removed loses this recycling and develops fat malabsorption: the bile salts pass out in stool, the liver cannot make them fast enough, and the next meal's fats cannot be properly emulsified.

### Brush border enzymes — the final cleavage

Pancreatic enzymes do most of the work, but they leave their job incomplete on purpose. Pancreatic amylase cleaves starch into disaccharides — pairs of sugars — but cannot cleave the disaccharide bond itself. Pancreatic proteases cleave proteins into short peptides but not all the way to free amino acids.

The final cleavage happens at the brush border. Embedded in the apical membrane of each enterocyte (the absorptive epithelial cell of the small intestine) are specialized enzymes:

- **Maltase** cleaves maltose (glucose-glucose) into two glucoses.
- **Sucrase** cleaves sucrose (glucose-fructose) into glucose and fructose.
- **Lactase** cleaves lactose (glucose-galactose) into glucose and galactose.
- **Peptidases** cleave short peptides into free amino acids and dipeptides.

Lactase is the famous one, because it is the enzyme that most adult humans gradually lose. Lactose intolerance — the world's most common digestive disorder, affecting roughly two-thirds of adult humans globally and a much higher fraction in East Asian and many African populations — is simply the absence of brush-border lactase.[^lactase-prevalence] The lactose in milk passes undigested into the colon, where bacteria ferment it, producing gas and osmotically pulling water into the lumen. Gas, cramping, diarrhea, two hours after a glass of milk. The mechanism is brush-border-level.

[^lactase-prevalence]: Storhaug, C. L., Fosse, S. K., & Fadnes, L. T. (2017). "Country, regional, and global estimates for lactose malabsorption in adults: a systematic review and meta-analysis." *The Lancet Gastroenterology & Hepatology* 2(10), 738–746. [https://doi.org/10.1016/S2468-1253(17)30154-1](https://doi.org/10.1016/S2468-1253(17)30154-1)

The point of the brush border is that final cleavage happens *right at the absorptive surface*. The free monomers are released directly adjacent to the transporters that will pull them into the cell. There is no diffusion gap during which the monomers might be lost back into the lumen. The architecture is exquisite — cleavage and uptake in the same membrane, one or two nanometers apart.

### Absorption — two routes, two destinations

Now the monomers cross the wall. Different nutrients take radically different routes.

**Glucose and amino acids** are water-soluble and cannot diffuse through a lipid bilayer. They cross the apical membrane using specific transporters. Glucose enters via **SGLT1** — the sodium-glucose cotransporter — which binds one glucose and two sodium ions and shuttles all three into the cell simultaneously. The driving force is the sodium gradient: the Na⁺/K⁺ ATPase on the basolateral membrane of the cell pumps sodium out continuously, keeping intracellular sodium low. Sodium's tendency to flow back in down its gradient drags glucose along, even when the glucose concentration outside the cell is lower than inside. This is **secondary active transport** — the energy for glucose uptake comes ultimately from ATP, but indirectly, via the sodium gradient the ATP-pump maintains.

Once glucose is inside the enterocyte, it exits the basolateral membrane by **GLUT2**, a passive transporter that moves glucose down its concentration gradient into the interstitial fluid and then into the blood capillary in the villus core. Amino acids use a similar logic with their own Na⁺-coupled transporters.

The blood capillaries in the villus core drain into venules, which collect into larger veins that feed the **hepatic portal vein** — a special vein that carries blood from the entire gut directly to the liver, bypassing the systemic circulation. *Portal* circulation, in anatomy, means a venous system that runs from one capillary bed to another rather than back to the heart. The hepatic portal vein takes everything absorbed in the gut to the liver first. The liver gets to inspect, process, store, or pass on every absorbed glucose molecule and every absorbed amino acid before they reach the rest of the body. This is the liver's **first-pass effect**, and it is the reason the liver is the master metabolic organ.

**Fats** take a completely different route. Mixed micelles deliver fatty acids and monoglycerides to the brush border. The lipid products diffuse across the apical membrane — they can do this because they are hydrophobic enough to dissolve into the lipid bilayer itself. No transporter required.

Once inside the enterocyte, the fatty acids and monoglycerides are reassembled into triglycerides (the cell has its own enzymes that re-link them), combined with cholesterol, phospholipids, and a specific protein coat called apolipoprotein B-48, and packaged into structures called **chylomicrons** — large lipoprotein particles, 75 to 1200 nanometers across, that carry dietary fat. The word *chylomicron* comes from *chyle* (the milky fluid in lacteals after a fatty meal) and *micron* (small).

Chylomicrons are too large to fit through the wall of a blood capillary. So they are exported across the enterocyte's basolateral membrane by exocytosis and they enter the **lacteal** — the lymphatic vessel in the villus core. They travel through the intestinal lymphatic system, up the thoracic duct (the major lymph vessel of the body), and finally drain into the systemic blood circulation at a vein near the left collarbone. Dietary fat enters the bloodstream *after* the lymphatic detour, bypassing the liver's first-pass inspection.

This routing difference matters clinically. A high-fat meal raises blood lipid levels visibly within hours — you can see the serum turn milky if you draw blood three hours after a fatty meal — because the chylomicrons are circulating systemically before the liver has had a chance to clear them. A high-carbohydrate meal does not produce a comparable visible change, because the liver is intercepting glucose and either storing it or releasing it back into circulation at a regulated rate.

It also matters in disease. A patient with cirrhosis — diffuse liver damage — has trouble processing amino acids and glucose because everything from the gut comes through the damaged liver first. But dietary fat reaches their systemic circulation relatively unimpaired, at least until lipoprotein clearance further downstream becomes a problem.

---

## The large intestine — water recovery and the microbiome

The **large intestine**, also called the colon, is about 1.5 meters long. It receives the residue of digestion from the small intestine — roughly 1.5 liters of watery, indigestible material per day, including fiber, dead epithelial cells, bile pigments, and bacteria. Its primary job is **water and electrolyte reabsorption**. By the time the residue reaches the rectum, it has been concentrated from a watery slurry into a semisolid mass.

A common misconception is that most water absorption happens in the small intestine. The volumes are surprising. Roughly 9 liters of fluid enter the GI tract per day — 1.5 from food and drink, 1.5 from saliva, 2 from gastric secretions, 1.5 from bile, 1.5 from pancreatic juice, and another liter from the small intestine itself. The small intestine absorbs about 7 of those liters; the large intestine absorbs another 1.5. Out of nine liters in, only about 100 milliliters are lost in stool.

The small intestine absorbs more *volume*, yes — but the large intestine performs a different and arguably more delicate job: it concentrates. The colon takes a watery 1.5 liters and converts it to a semisolid 100 milliliters. If colonic water reabsorption fails — as it does in cholera, where a bacterial toxin pulls chloride (and therefore sodium and water) back out of the cells and into the lumen — a patient can lose up to 20 liters of fluid per day. Death from cholera is death from dehydration, not from any digestive failure. The patient's small intestine is fine. Their colon's concentrating function is overwhelmed.

The large intestine also hosts the **gut microbiome** — roughly 10¹³ to 10¹⁴ bacterial cells, weighing about 0.2 kg in total, comprising hundreds of species.[^microbiome-count] The microbiome ferments fiber and other indigestible carbohydrates into **short-chain fatty acids** (acetate, propionate, butyrate) that the colon absorbs and uses for energy — butyrate is the colonocyte's preferred fuel. The microbiome also synthesizes vitamin K and several B vitamins, which we absorb. And it occupies the colonic niche so densely that pathogenic bacteria have trouble establishing themselves — a phenomenon called **colonization resistance**. Wipe out the microbiome with broad-spectrum antibiotics and *Clostridioides difficile*, which is normally suppressed, can overgrow and produce severe colitis.

[^microbiome-count]: Sender, R., Fuchs, S., & Milo, R. (2016). "Revised Estimates for the Number of Human and Bacteria Cells in the Body." *PLOS Biology* 14(8), e1002533. [https://doi.org/10.1371/journal.pbio.1002533](https://doi.org/10.1371/journal.pbio.1002533) (This is the paper that revised the famous "10:1 bacteria-to-human-cell" ratio down to about 1:1 — closer to 3.8 × 10¹³ bacteria vs. 3.0 × 10¹³ human cells.)

The microbiome's connection to systemic disease — obesity, type 2 diabetes, depression, autism — is one of the most active and most overhyped areas of biology right now. There are real correlational findings. There are some genuine mechanistic links (short-chain fatty acids influence host metabolism and immune function). But the causal claims being made in popular press dramatically outrun what has been demonstrated. We will return to this in the "still puzzling" section.

---

## The liver — the metabolic integrator

Almost everything you have just absorbed — except dietary fat — arrives at the **liver** through the hepatic portal vein. The liver is the central metabolic processing organ, and what it does to the absorbed nutrients depends entirely on which metabolic state the body is in.

Before getting to the metabolic state, list what the liver does:

- **Bile production** (continuous, regardless of meal state).
- **Glycogen storage** — packs absorbed glucose into glycogen, a branched polymer; releases glucose back into blood when needed.
- **Gluconeogenesis** — makes new glucose from non-carbohydrate precursors (lactate, glycerol, amino acids) during fasting. *Gluconeogenesis* literally means "making new glucose."
- **Lipid metabolism** — packages excess glucose and amino acids into triglycerides for storage; makes lipoproteins (VLDL, HDL) to transport lipids in the blood; converts fatty acids into ketone bodies during prolonged fasting.
- **Protein synthesis** — manufactures most of the proteins in blood plasma: albumin (the major osmotic regulator), clotting factors (most of them, which is why liver failure causes bleeding disorders), transport proteins.
- **Detoxification** — chemically modifies drugs, alcohol, ammonia (from amino acid breakdown), and other potentially harmful molecules to make them water-soluble for excretion.
- **Vitamin and mineral storage** — vitamin A, D, B12, iron, copper.

The liver is the metabolic switchboard. It can do all of these things simultaneously, but the *direction* of its activity — storage versus release, anabolism versus catabolism — is set by hormones, and the dominant hormones are the ones from Chapter 8: insulin and glucagon.

---

## The fed-fasted switch — two states, two hormone dominances

This is the second half of the chapter, and it picks up exactly where Chapter 8 stopped. Insulin and glucagon are opposing hormones, both secreted by the pancreatic islets, both regulating blood glucose. Insulin says "abundance — store everything." Glucagon says "scarcity — release everything." The ratio of insulin to glucagon — which depends on blood glucose, which depends on whether you have eaten recently — determines whether the body is in the *absorptive (fed) state* or the *postabsorptive (fasted) state*.

### The absorptive (fed) state — insulin dominates

In the hour or two after a mixed meal, blood glucose rises as absorbed glucose pours in through the portal vein. The pancreatic beta cells sense this and release insulin. Insulin levels rise sharply (often fivefold to tenfold over baseline). Glucagon falls.

What insulin tells the body, organ by organ:

- **Liver:** stop making glucose, start storing it. Specifically: activate glycogen synthase (the enzyme that builds glycogen from glucose), inhibit glycogen phosphorylase (the enzyme that breaks glycogen back down), suppress gluconeogenesis. The liver, which was a net glucose *producer* during the fast, switches to being a net glucose *consumer*. Excess glucose beyond what the liver can store as glycogen is converted to fatty acids and packaged as VLDL (very-low-density lipoprotein) for export to adipose tissue.
- **Muscle:** take up glucose. Insulin triggers translocation of **GLUT4** glucose transporters from intracellular vesicles to the muscle cell membrane. Without insulin, muscle is nearly impermeable to glucose. With insulin, glucose floods in. Some of the glucose is used immediately for ATP; most is stored as glycogen.
- **Adipose tissue (fat):** take up glucose, store fat. Adipocytes also have GLUT4, and they also take up glucose under insulin signaling — they use it to make glycerol (the backbone for triglyceride storage) and they take up fatty acids delivered by chylomicrons and VLDL, repackaging them as stored triglyceride.
- **Brain:** no change. The brain uses GLUT1 and GLUT3 transporters that are insulin-independent. The brain takes up glucose whenever blood glucose is available, full stop, regardless of insulin.

Insulin also stimulates amino acid uptake by muscle and protein synthesis throughout the body. Amino acids absorbed from a meal are used to build new proteins; the body is in net anabolism — building everything, breaking down nothing.

The absorptive state lasts about three to four hours after a meal. By then, the gut has finished delivering nutrients, blood glucose returns to baseline, insulin falls, glucagon begins to rise. The body transitions.

### The postabsorptive (fasted) state — glucagon dominates

After about four hours without food, the gut is empty. Blood glucose would fall — except that the body actively defends it. Glucagon rises. Insulin falls. The same liver that was storing everything an hour ago is now releasing everything.

What glucagon tells the liver:

- **Activate glycogen phosphorylase** — break down glycogen, release glucose into blood. This is **glycogenolysis** (literally "glycogen-breaking-with-water"). Liver glycogen is the immediate glucose reserve and sustains blood glucose for the first six to eight hours of fasting.
- **Inhibit glycogen synthase** — don't waste glucose making more glycogen.
- **Activate gluconeogenesis** — make new glucose from amino acids (from muscle protein breakdown), glycerol (from triglyceride breakdown in adipose tissue), and lactate (from anaerobic glycolysis in red blood cells and active muscle). The rate-limiting enzyme is phosphoenolpyruvate carboxykinase (PEPCK), and glucagon increases its activity.

In adipose tissue, glucagon (along with falling insulin and rising stress hormones) activates hormone-sensitive lipase, which breaks down stored triglycerides into glycerol and free fatty acids. Glycerol heads to the liver for gluconeogenesis. Free fatty acids are released into the blood and taken up by muscle and other tissues, which switch from burning glucose to burning fatty acids.

The brain is the constraint the whole system is organized around. The brain needs about 120 grams of glucose per day. It cannot use fatty acids directly. So the body's strategy during the postabsorptive state is to *preserve glucose for the brain* — let muscle and other tissues burn fat, while the liver keeps manufacturing glucose specifically for the brain.

After about twenty-four hours of fasting, liver glycogen is depleted. Gluconeogenesis is now doing all of the glucose production, and it requires amino acid substrate — which means breaking down muscle protein. This cannot continue indefinitely without compromising muscle function. So the liver pulls a final trick: as fat oxidation continues at high rates, acetyl CoA accumulates faster than the Krebs cycle can process it, and the liver converts excess acetyl CoA into **ketone bodies** — acetoacetate and beta-hydroxybutyrate. The brain, over a few days, adapts to use ketone bodies as a primary fuel, reducing its glucose demand by about seventy percent. Muscle protein breakdown slows dramatically. The body can now run for weeks on fat reserves alone.

The hierarchy is worth stating explicitly: glucose for the brain, fat for everything else, muscle protein only as a last resort and only as slowly as possible.

### Basal metabolic rate

Even at complete rest — supine, awake, in a thermoneutral environment, twelve hours fasted — the body uses energy continuously. This baseline is the **basal metabolic rate** (BMR), the energy required to keep the basic life-supporting machinery running: the heart contracting 60 times a minute, the kidneys filtering blood, the liver detoxifying, the brain processing, the body temperature staying at 37°C. For a typical adult, BMR is about 1,400 to 1,800 kilocalories per day — roughly 60 to 75 watts of continuous power output, the same as a household light bulb. BMR varies with body size, lean mass (muscle is metabolically expensive), age (younger faster), thyroid hormone status (the thyroid sets cellular metabolic rate), and genetic background.

Total daily energy expenditure adds the cost of physical activity (highly variable) and the *thermic effect of food* — the small metabolic cost of digesting and processing what you eat, roughly 10% of intake. A sedentary adult typically expends 1,800 to 2,400 kcal/day; an active adult 2,400 to 3,500; an elite endurance athlete in training can sustain 6,000 to 8,000 kcal/day for weeks.

Energy balance is brutally simple in principle and brutally complicated in practice. If intake exceeds expenditure, the excess is stored — first as glycogen (limited capacity, perhaps 400 g total in liver and muscle, about 1,600 kcal worth), then as triglyceride in adipose tissue (capacity is essentially unlimited; an average lean adult carries 100,000 to 200,000 kcal in fat stores). If expenditure exceeds intake, stores are mobilized in the reverse order.

The principle is simple. The hormonal control of where that energy goes, what gets stored versus what gets burned, why some people store fat preferentially and others store muscle, why insulin resistance develops in some people and not others — that is the part of the science that is still being figured out.

---

## Worked example — trace a meal end to end

Run through a concrete meal so the whole chapter comes together in one continuous chain.

A patient eats a 600-calorie meal containing 50 grams of carbohydrate, 50 grams of protein, and 22 grams of fat.

Do the caloric accounting first.
- Carbohydrate: 50 g × 4 kcal/g = **200 kcal**
- Protein: 50 g × 4 kcal/g = **200 kcal**
- Fat: 22 g × 9 kcal/g = **198 kcal**
- Total: **598 kcal**

Now follow the meal.

**Minutes 0–5: Mouth.** The patient chews. Teeth break the food into smaller pieces. Salivary amylase begins hydrolyzing the starch — by the end of chewing, perhaps 5% of the 50 g of carbohydrate is in the form of shorter oligosaccharides. The protein and fat are untouched. The bolus is swallowed.

**Minutes 5–10: Esophagus.** Peristalsis moves the bolus to the stomach in seconds. No chemistry.

**Minutes 10 minutes to 3 hours: Stomach.** Parietal cells secrete HCl, bringing the gastric pH to ~2. Salivary amylase is denatured almost immediately — carbohydrate digestion pauses. Pepsinogen is released by chief cells and converted to pepsin by the acid. Pepsin begins cleaving the protein — by the end of gastric processing, the 50 g of protein has been broken into a mix of shorter peptides and a few free amino acids. The fat is essentially untouched — it sits in large globules because there is no meaningful lipase in the stomach. The mass churns into chyme. The pyloric sphincter opens in pulses, releasing about 3 mL of chyme at a time into the duodenum. A meal of this composition takes about 3 hours to leave the stomach completely; a fattier meal would take longer.

**As chyme arrives in the duodenum:** Enteroendocrine cells detect the low pH and release **secretin**, which travels to the pancreas and triggers bicarbonate release. Within minutes the duodenal pH rises from 2 to 7. They detect fat and partially-digested protein and release **CCK**, which contracts the gallbladder (bile flows in) and triggers the pancreas to release enzymes (amylase, lipase, proteases).

**Minutes 30 to 5 hours: Small intestine.** The real work.

*Carbohydrate.* Pancreatic amylase resumes starch digestion, cleaving it into maltose and other disaccharides. At the brush border, maltase cleaves maltose into two glucose molecules, sucrase cleaves any dietary sucrose, lactase cleaves any dietary lactose. Free glucose is now adjacent to SGLT1 transporters. Each SGLT1 binds one glucose and two sodium ions, shuttling all three into the enterocyte. Glucose exits the basolateral membrane via GLUT2 into the villus capillary network. The capillaries drain into the portal vein. **The 50 g of carbohydrate, now as ~280 millimoles of glucose, fructose, and galactose, flows to the liver.**

*Protein.* Pancreatic proteases (trypsin, chymotrypsin, elastase, carboxypeptidases) continue cleaving the peptides into shorter peptides. Brush border peptidases finish the job, releasing free amino acids and dipeptides. These cross the apical membrane via amino acid transporters (most are Na⁺-coupled, similar in principle to SGLT1). They exit the basolateral membrane and enter the portal blood. **The 50 g of protein, now as ~440 millimoles of free amino acids, flows to the liver.**

*Fat.* Bile salts from the gallbladder emulsify the fat globules into smaller droplets. Pancreatic lipase cleaves the triglycerides into free fatty acids and 2-monoglycerides. These products, along with bile salts and phospholipids, form mixed micelles that deliver the fat to the brush border. The fatty acids and monoglycerides diffuse across the apical membrane. Inside the enterocyte, they are reassembled into triglycerides, combined with cholesterol and apolipoprotein B-48, and packaged into chylomicrons. The chylomicrons are exocytosed across the basolateral membrane and enter the **lacteal** in the villus core. **The 22 g of fat — too large to enter blood capillaries — instead enters the lymphatic system, travels up the thoracic duct, and joins the bloodstream at the left subclavian vein, bypassing the liver's first-pass inspection.**

**Hours 1–3 after meal: The fed state.**

The pancreas senses the rising blood glucose (and the rising amino acids, and the GIP signal from the small intestine that food is being absorbed) and releases insulin. Blood insulin rises perhaps eight-fold above baseline. Glucagon falls.

In the liver: glycogen synthase activates. Of the 280 mmol of glucose arriving via the portal vein, much is taken up by hepatocytes and polymerized into glycogen. The 50 g of carbohydrate would yield enough glucose to refill roughly a third to a half of the liver's glycogen reserve (the liver holds about 100 g of glycogen at full capacity). Excess glucose is converted to fatty acids and packaged as VLDL.

In muscle: GLUT4 transporters move to the cell surface. Glucose floods in. Muscle takes up glucose for immediate ATP and for glycogen storage. Muscle also takes up amino acids and uses them for protein synthesis.

In adipose tissue: GLUT4 transporters mobilize. Adipocytes take up glucose, make glycerol, and take up fatty acids delivered by chylomicrons (lipoprotein lipase, on the capillary endothelium of adipose tissue, cleaves triglycerides from chylomicrons and lets the fatty acids enter the cell). The fat from the meal is stored.

In the brain: glucose uptake continues at the same rate as always, independently of insulin.

**By hour 4: blood glucose returns to baseline. Insulin falls. Glucagon begins to rise. The body has shifted toward the postabsorptive state.**

**Hours 4–12: The postabsorptive state.**

The liver activates glycogen phosphorylase. Glycogen is broken down. Glucose is released into the blood. The liver becomes a net glucose producer again.

Muscle and other tissues are now running on a mix of glucose and fatty acids. Adipose tissue is mobilizing free fatty acids. The brain continues to use glucose, supplied by the liver's glycogenolysis.

**Hours 12–24:** Liver glycogen is becoming depleted. Gluconeogenesis ramps up. The liver starts making new glucose from glycerol (from continuing lipolysis) and from amino acids (some absorbed from the meal, some from a slow trickle of muscle protein breakdown). Blood glucose stays stable.

**Beyond 24 hours:** Glycogen is gone. Ketogenesis ramps up. The brain begins to adapt to ketone bodies. Muscle protein is being broken down at a measured rate to supply gluconeogenic substrate.

That's the whole pipeline. Digestion is a four- to five-hour event. The metabolic ledger that begins with digestion continues for the next twelve to twenty-four hours and only resets when the next meal arrives. The lesson and the limit go together:

*The lesson:* Digestion and metabolism are not two separate systems. They are one continuous pipeline from mouth to mitochondrion, regulated minute-to-minute by the insulin/glucagon balance. Each enzyme, each transporter, each hormone is a specific machine doing a specific job. When all of them work, you do not notice any of them.

*The limit:* In diabetes, this regulation breaks. In Type 1, insulin is absent — glucose absorbed from a meal stays in the blood instead of being stored, and the body behaves as if it were in a permanent fasted state despite plenty of glucose available, breaking down fat and muscle inappropriately. In Type 2, insulin is present but the target cells stop responding properly — the absorptive state cannot fully engage, glucose accumulates in blood, and the long-term consequences accumulate in every blood vessel insulted by chronic hyperglycemia. The hormone's signal is the bridge between digestion and metabolism. Take away the bridge, and the two halves of the pipeline can no longer talk to each other.

---

## Common misconceptions

**Misconception 1: "Stomach acid does most of the digestion."**

This is the misconception most undergraduates arrive with, and it gets the geography wrong. Gastric acid does two things that are critical and one thing it does not. *Critical:* it denatures proteins (unfolds them, exposing peptide bonds for proteases to cleave) and it activates pepsin from its zymogen. *Not critical for digestion:* it does not directly cleave macronutrients. Pepsin does cleave protein in the stomach, but it produces only short peptides — not free amino acids. Salivary amylase, the only carb-digesting enzyme present, is denatured by the acid. There is no lipase active in the adult stomach to speak of.

So the stomach is a *protein-denaturation chamber* with a *partial-protein-digestion sideline*. The real digestion — finishing the protein, doing essentially all the fat, doing essentially all the carbohydrate, and absorbing everything — happens in the small intestine. Surgically remove the stomach (a total gastrectomy, sometimes done for gastric cancer) and patients can still digest most macronutrients reasonably well, provided they eat small, frequent meals and supplement vitamin B12 (which required intrinsic factor from the stomach).

**Misconception 2: "The liver makes glucose from fat."**

This one is widespread because it sounds plausible — fat has lots of energy, surely the body can convert it to glucose during fasting? It cannot, except by a trickle. Here is the mechanism. Fatty acids are oxidized to acetyl CoA via beta-oxidation. Acetyl CoA enters the Krebs cycle. But acetyl CoA cannot be converted *back* to a Krebs cycle intermediate that could feed gluconeogenesis — the relevant reactions are irreversible, and the carbons of acetyl CoA are released as CO₂ during the cycle. Net: fatty acid carbons leave as CO₂, not as glucose.

There are two exceptions. One: the glycerol backbone of triglycerides can be converted to glucose, but a triglyceride has one glycerol per three fatty acids, so the glucose yield from fat is small. Two: in odd-chain fatty acids (rare in human diet, common in some bacteria), the final beta-oxidation step produces propionyl CoA, which can be converted to a Krebs intermediate and feed gluconeogenesis — but this is a tiny fraction of dietary fat.

The body's main gluconeogenic substrates are amino acids (from protein breakdown), lactate (from anaerobic glycolysis), and glycerol (from fat breakdown but limited to the glycerol fraction). During prolonged fasting, gluconeogenesis from amino acids dominates — which is why protein breakdown is unavoidable during sustained fasting and why ketogenesis is the body's strategy for sparing muscle protein.

**Misconception 3: "You absorb most water in the small intestine."**

This one is partially true but misleading. The small intestine does absorb more *volume* of water — roughly 7 liters per day versus 1.5 in the colon. But the *concentrating function* — the conversion of a liquid residue into a semi-solid stool — happens entirely in the colon. If the colon is bypassed (as in an ileostomy patient, who has had their colon removed and their small intestine routed to a stoma on the abdominal wall), the output is liquid and constant, and the patient must consume substantially more fluid and salt to keep up.

This is also why diarrhea is dangerous. In severe diarrhea (cholera, viral gastroenteritis), the colon's reabsorptive function is overwhelmed or actively reversed, and instead of recovering 1.5 liters, the colon may *lose* additional liters. A patient with massive diarrhea can lose ten to twenty percent of their body weight in fluid in a day. Death from diarrhea is death from cardiovascular collapse from volume depletion — a child with severe gastroenteritis can die in twelve hours from dehydration alone, with no other organ failure. This is why oral rehydration therapy — a solution of glucose, sodium, and water in specific proportions — is one of the most important medical interventions of the twentieth century. It exploits the SGLT1 cotransporter we covered earlier: the SGLT1 transporter is unaffected by most diarrheal toxins, so as long as glucose and sodium are present together in the intestinal lumen, they will be co-absorbed, and water will follow osmotically.

**Misconception 4: "Insulin and glucagon are antagonists, so they are never present at the same time."**

They are antagonists in function but they coexist in concentration. Glucagon is never zero. Even at the peak of the fed state, baseline glucagon continues to be released from alpha cells, and what determines metabolic state is the *ratio* of insulin to glucagon, not the absolute level of either one. Insulin/glucagon ratio of 30:1 means deep fed state, full anabolism. Ratio of 0.5:1 means starvation, full catabolism, ketogenesis ramping up. The ratio is what the liver reads.

This matters clinically. In Type 1 diabetes, the absence of insulin is not the only metabolic insult — alpha cells, freed from insulin's local suppression, often release excessive glucagon, *and* the I/G ratio collapses to far below normal levels, driving aggressive glycogenolysis, gluconeogenesis, and ketogenesis. Diabetic ketoacidosis is partly an insulin-deficiency problem and partly a glucagon-excess problem.

---

## Exercises

**Exercise 1 — Predict the metabolic state (Apply).**

A patient eats a meal containing 80 g of carbohydrate, 20 g of protein, and 10 g of fat at 7:00 PM. They eat nothing else and go to sleep at 11:00 PM.

(a) At 9:00 PM (2 hours post-meal), predict the dominant hormone, the dominant liver activity, and the direction of glucose flux (liver releasing glucose? liver storing glucose?).

(b) At 7:00 AM (12 hours post-meal), predict the same three variables.

(c) Explain in two sentences why the *ratio* of insulin to glucagon — rather than the absolute level of either — is what the liver responds to.

**Exercise 2 — Cystic fibrosis and steatorrhea (Apply / Synthesis).**

Cystic fibrosis is a genetic disorder caused by mutations in the CFTR chloride channel. In the pancreas, the defect prevents proper secretion of bicarbonate and digestive enzymes into the pancreatic duct — the duct gets blocked by thick secretions and most pancreatic enzymes never reach the duodenum.

(a) Predict which macronutrient will show the most severe malabsorption in a CF patient and explain why. (Hint: which macronutrient depends most absolutely on pancreatic enzyme delivery?)

(b) Explain why CF patients develop *steatorrhea* — fat in the stool that produces oily, foul-smelling, floating bowel movements.

(c) The standard treatment is **pancreatic enzyme replacement therapy** — capsules of porcine pancreatic enzymes taken with every meal. Why must the capsules be enteric-coated (designed to dissolve only at near-neutral pH, not in the stomach)?

(d) Predict whether a CF patient would have deficient absorption of fat-soluble vitamins (A, D, E, K), water-soluble vitamins (B, C), or both, and explain why.

**Exercise 3 — Cirrhosis and hypoglycemia (Synthesis / Challenge).**

A patient with end-stage liver cirrhosis from chronic alcohol use is hospitalized. Overnight, while NPO (nothing by mouth) for a procedure, their blood glucose falls to 45 mg/dL — symptomatic hypoglycemia. A healthy person can fast for 24 hours without becoming hypoglycemic.

Explain in detail:

(a) Which two specific liver functions covered in this chapter are responsible for maintaining blood glucose during a fast?

(b) In what order would these functions fail as cirrhosis progresses, and why?

(c) Predict whether this patient would be able to mount a normal ketogenic response if the fast were extended to 72 hours. Explain.

(d) Why, in a healthy person, does the brain *not* simply switch to using fatty acids during a fast — and why is the answer to (c) above clinically significant?

**Exercise 4 — Celiac disease and absorption (Apply / Synthesis).**

In celiac disease, an autoimmune reaction to dietary gluten flattens the villi of the small intestine and damages the microvilli. The "tennis-court" surface area can fall by 80%. The damage is reversible if the patient eliminates gluten from their diet.

(a) Quantify the change in absorptive surface area. If a healthy small intestine has 300 m² of absorptive surface, what would a celiac patient have at 80% villus loss?

(b) Predict which would be more severely affected: absorption of glucose, or absorption of fat. Explain your reasoning. (Hint: think about the difference between active transport via SGLT1 versus mixed-micelle-mediated diffusion.)

(c) A common presentation of celiac disease is iron-deficiency anemia. Iron is absorbed primarily in the duodenum. Explain why celiac disease — which affects the entire small intestine but tends to start in the duodenum — disproportionately affects iron status.

(d) A patient with untreated celiac disease often shows brush-border lactase deficiency, even though they previously tolerated milk. Explain mechanistically why villus damage produces secondary lactose intolerance.

---

## What would change my mind

The chapter is built around a clean separation between digestion (a mechanical/enzymatic disassembly problem solved by staged chemistry along the GI tract) and metabolism (a hormonal regulation problem governed by the insulin/glucagon balance). If careful longitudinal studies of the gut microbiome showed that microbial signaling — short-chain fatty acid effects, microbial metabolites acting on enteroendocrine cells, microbial influence on bile acid pools — was a *primary* regulator of the fed/fasted switch in normal physiology, rather than a secondary modulator, then the chapter's two-actor framing (digestive system delivers monomers; insulin/glucagon balance decides what to do with them) would need to be rewritten as a three-actor framing, with the microbiome promoted from "interesting context" to "co-regulator."

## Still puzzling

Why does the small intestine, with its astonishing surface area and rich enzyme repertoire, not display the same kind of mucosal cancer risk as the colon — which has far less surface area but is the site of one of the most common adult cancers? What evolutionary pressure preserves the *enterohepatic circulation of bile salts* so precisely — the system clearly works, but it costs a continuous metabolic investment in the ileal terminal absorption machinery, and the failure modes (bile salt malabsorption after ileal resection) are debilitating; what design constraint forced this rather than continuous bile salt synthesis? And why has the human pancreas been built with such tight coupling between exocrine and endocrine functions (the islets of Langerhans literally embedded in the exocrine tissue) when most other glands maintain that separation — is this proximity functional or vestigial?

The big still-puzzling question, though, is the microbiome. The composition of human gut bacteria correlates with body weight, with metabolic syndrome, with mood, with autism spectrum traits, with response to immunotherapy in cancer — the correlational literature is enormous. The causal interventions that have actually been demonstrated are far narrower: fecal microbiota transplant cures recurrent *C. difficile* infection in humans; specific bacterial species can drive specific metabolic phenotypes in germ-free mice when transplanted from obese human donors. Between those rigorous endpoints and the popular-press claims about "gut bacteria control your mood" lies a vast gap of correlational findings whose causal direction is unclear. The gut microbiome is real, the microbiome's contribution to host physiology is real, and the field is still in the middle of figuring out which of the dozens of claimed associations are causal and in which direction. The chapter you have just read covers digestion and metabolism without resolving this. I think that is the honest current position.

---

## LLM Exercise — Build, explore, extend

The exercise below builds and uses `12-nutrient-absorption.html` — a single-file HTML page that simulates a meal traveling through the GI tract, tracks absorption of each macronutrient at each segment, and visualizes the metabolic fate of absorbed nutrients in the fed-vs-fasted state. As with previous chapters, treat the model's responses as drafts to be critiqued, not as oracles.

### SHOW — get the artifact built

```
You are helping me build a single-file HTML page called 12-nutrient-absorption.html
for an anatomy and physiology textbook. The page must run in a modern browser with
no build step and no external dependencies — just one HTML file with inline CSS
and JS.

The page is a nutrient absorption simulator. It must support the following.

UI:
  - Top: a "meal composition" panel with three sliders, one each for carbohydrate (g),
    protein (g), and fat (g). Total calories should auto-calculate (4 kcal/g for
    carb and protein, 9 kcal/g for fat) and display.
  - A "physiology" panel with sliders for:
      * GI motility (slow / normal / fast) — affects transit time.
      * Pancreatic enzyme activity (0-100%) — affects digestion efficiency.
      * Villus surface area (normal 100% / celiac 20%) — affects absorption efficiency.
  - A "metabolic state" toggle: fed state (insulin dominates) vs. postabsorptive state
    (glucagon dominates).
  - A "Run meal" button that animates the meal through the GI tract.

Animated diagram:
  - A schematic of the GI tract from mouth to large intestine. The meal is shown as
    three colored blobs (carb=yellow, protein=red, fat=blue). As the simulation runs:
      * Salivary amylase shows partial carb digestion in the mouth.
      * Stomach denatures protein (red blob fragments) but leaves carb and fat largely
        intact.
      * Duodenum: bile from gallbladder emulsifies fat (blue blob breaks into droplets);
        pancreatic enzymes act on all three.
      * Small intestine: brush border completes digestion; show absorption rate
        (molecules per second) for each macronutrient at each segment (duodenum,
        jejunum, ileum).
      * Show routing: glucose and amino acids -> portal vein -> liver (route highlighted
        in red). Fat -> lacteals -> lymph -> systemic blood (route highlighted in blue),
        bypassing the liver initially.
      * Large intestine: show water absorption only.

Metabolic display:
  - Below the GI diagram, show a "metabolic destination" panel:
      * In fed state: glucose -> liver glycogen, muscle glycogen, adipose fat synthesis.
      * In postabsorptive state: liver glycogenolysis releases glucose; lipolysis
        releases fatty acids; gluconeogenesis runs.
  - A live "insulin/glucagon ratio" indicator that updates based on metabolic state
    and recent meals.

Pathology modes:
  - Celiac mode: villus surface area set to 20%; absorption rates fall accordingly;
    diagram shows blunted villi.
  - Cystic fibrosis mode: pancreatic enzyme activity set to ~10%; fat digestion
    largely fails; diagram shows fat passing through largely undigested into stool
    (steatorrhea).
  - Type 1 diabetes mode: insulin output set to zero; in fed state, glucose
    accumulates in blood instead of being stored.

Math:
  - Use simple time-step updates. Absorption rate = (surface area factor) ×
    (enzyme activity factor) × (concentration in segment) × (segment-specific
    transporter capacity).
  - Hormone responses (insulin, glucagon) update based on blood glucose level and
    pathology state.

Use plain CSS Grid for layout. Use inline SVG for the diagram and Canvas for the
time-series graphs. No images, no fetch calls, no libraries. Comment the code so a
beginner can read it. Output the complete HTML file.
```

Save the result as `12-nutrient-absorption.html` and open it. Run a normal meal, then run the same meal with celiac mode, then with CF mode. The visceral feel of "the same meal but the patient cannot absorb it" is the point.

### SAY — explore what the artifact teaches you

Pick one of these and run it. Then run a second one.

```
In the simulator, I set the meal to 80 g carb, 20 g protein, 10 g fat. I ran it
in normal mode, then ran the same meal in celiac mode (20% villus surface area).
Compare the absorption rates for glucose vs. fat in the two runs. Explain why the
fat malabsorption in celiac is often less severe (proportionally) than the
carbohydrate malabsorption, even though both are reduced. Tie your answer to the
specific mechanisms of glucose absorption (SGLT1, active transport) versus fat
absorption (mixed micelle diffusion).
```

```
Run the simulator with a 100 g carbohydrate meal in fed-state, normal physiology.
Watch the insulin/glucagon ratio rise. Now run the same meal with Type 1 diabetes
mode (insulin output = 0). The ratio cannot rise. Trace what happens to the
absorbed glucose. Predict what would happen to the patient's free fatty acid level
and ketone level over the next 12 hours, and explain why diabetic ketoacidosis
is paradoxically a *fed-state* disease in which the body acts as if it is starving.
```

```
Run the simulator with a meal containing 40 g of fat in cystic fibrosis mode
(pancreatic enzyme activity = 10%). Trace what happens to the fat through the
small intestine and into the colon. Now consider this: the patient is supplemented
with oral pancreatic enzyme replacements, but the capsules dissolve too early and
the enzymes are denatured in the stomach. Explain why the supplementation fails
and what specific feature of the enzyme replacement capsules must be engineered
to avoid this failure.
```

### CONSTRAIN — narrow the model's freedom

Re-run one of the SAY prompts with this constraint appended. Compare the two responses.

```
Constrain your answer to <= 250 words. For every numerical claim, either cite a
specific source (textbook chapter, primary paper, clinical guideline) or write
"no citation available". When you would normally write "approximately" or "around",
either give the actual range or say "I don't know the exact value". Do not
include any sentence that could appear unchanged in a corporate health blog.
```

Watch what the model gives up when it cannot bluff. The retreat is the lesson.

### VERIFY — check the model's claims against a primary source

Pick one numerical or mechanistic claim in the model's response and verify it. Suggested primary sources:

- *OpenStax Anatomy and Physiology*, Chapters 23 (digestive system) and 24 (metabolism and nutrition). [https://openstax.org/details/books/anatomy-and-physiology](https://openstax.org/details/books/anatomy-and-physiology)
- Helander, H. F., & Fändriks, L. (2014). "Surface area of the digestive tract – revisited." *Scandinavian Journal of Gastroenterology* — for the tennis-court figure and its revision.
- Sender, R., Fuchs, S., & Milo, R. (2016). "Revised Estimates for the Number of Human and Bacteria Cells in the Body." *PLOS Biology* — for microbiome cell counts.
- Marshall, B. J. (2005). "Helicobacter Connections" — Nobel Lecture, for the *H. pylori* story.
- Fasano, A. (2009). "Surprises from celiac disease." *Scientific American*, 301(2), 54–61 — for celiac pathophysiology in the registers a textbook reader can follow.
- Grundy, S. M. et al. (2005). "Diagnosis and Management of the Metabolic Syndrome." *Circulation* 112, 2735–2752 — for metabolic syndrome diagnostic criteria.

Note in your lab notebook: (a) the claim you verified; (b) the source you used; (c) whether the model was right, partially right, or wrong; (d) how you would change the prompt to make the model more reliable. The point is the habit of checking. Build it now, before the stakes are clinical.

### Extend — looking ahead to Chapter 13

Everything the digestive system absorbs is processed by the liver, and everything the body burns produces waste — water, CO₂, nitrogen-containing compounds (urea, principally, from amino acid breakdown), and a long list of fat-soluble and water-soluble metabolites. The CO₂ is exhaled (Chapter 11). The water and most of the rest leave through the kidneys, which is Chapter 13.

Ask your model:

```
Chapter 12 covered digestion and metabolism — the system that breaks food down,
absorbs the nutrients, and processes them into energy or storage. Chapter 13 will
cover the urinary system — the kidneys' job of cleaning the metabolic waste out
of the blood. Trace one specific nitrogen atom from an amino acid in a steak: from
the moment it is absorbed across the duodenal wall, through the portal vein to
the liver, through the urea cycle (which converts toxic ammonia to less toxic
urea), into the systemic blood, to the kidney, through the glomerular filter, and
out in urine. Identify the single step in this path where a clinical failure
(liver failure, kidney failure) would have the most rapid lethal consequence,
and explain why.
```

The answer is your first taste of Chapter 13. The digestive system gave you the nutrients. The urinary system disposes of the waste.

---

**What would change my mind:** If longitudinal microbiome interventions in humans showed that specific bacterial species are *primary* regulators of the fed-fasted hormonal switch — not just secondary modulators — the chapter's two-actor framing would need to be rewritten with the microbiome promoted to a co-regulator of metabolism.

**Still puzzling:** Across the dozens of correlations linking gut microbiome composition to systemic disease (obesity, depression, autism, immune function), which of those are causal in the microbiome → host direction, which are causal in the host → microbiome direction, and which are mediated by an unmeasured confounder — and how do we design human studies that can distinguish these without waiting another two decades?

---

**Tags:** digestive-system, metabolism, insulin-glucagon, malabsorption, celiac-disease
