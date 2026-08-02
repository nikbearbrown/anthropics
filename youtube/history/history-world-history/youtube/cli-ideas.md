# History: World History — CLI Video Ideas ("X with Claude")

## Candidate 01 — Research the Mongol Pax Mongolica with Claude

- Source: history-world-history/chapters/18-pax-mongolica-the-steppe-empire-of-the-mongols.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Mongol Empire was simultaneously the largest contiguous land empire in history and a catastrophic demographic disaster for conquered populations. Claude tends to foreground one or the other depending on how you phrase the question.
- The artifact: A sourced 3-section brief — (1) the Pax Mongolica: what trade routes were protected, what goods flowed, Marco Polo's route — what primary sources document this; (2) the demographic cost: estimated mortality from Mongol campaigns in Persia, China, and Eastern Europe — how are these numbers derived and how contested are they?; (3) a framing-effect test: what does Claude say about the Mongols when asked "What was the Pax Mongolica?" vs. "What was the demographic impact of Mongol conquest?" — do the responses foreground different aspects of the same history?
- Prompt seed: `claude "Describe the Pax Mongolica (c. 1260-1350). Include: (1) which trade routes were protected and by what mechanism, (2) estimated population loss in the major regions conquered (Persia, China, Eastern Europe, Central Asia) with sources for the estimates, (3) how historians balance the trade-facilitation and demographic-catastrophe aspects of the Mongol Empire. Flag contested estimates."`
- Read / check: Verify the Pax Mongolica dates are approximately correct (peaks mid-13th to mid-14th century); verify at least one population estimate is given as a range (the Persian and Chinese figures are genuinely contested — check that Claude presents them as estimates, not settled facts); flag if Claude omits the demographic cost entirely when asked about trade.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 1 population estimate against a secondary source (the Cambridge History of Inner Asia is a starting point).
- Output medium: Remotion slate (3-section brief: Pax Mongolica trade routes table, demographic cost section with contested-estimate flags, framing-effect comparison)
- The change: Run the framing-effect test explicitly — same facts, two prompts. Show the responses side by side and annotate what each foregrounds. The exercise demonstrates that historical framing is a choice, and the discipline is making it consciously.
- Teardown angle: The Mongol Empire is one of the strongest test cases for the "compare" move: the same historical event is described very differently depending on the question's entry point. The research brief doesn't resolve the tension — it makes the tension visible and documents both sides with evidence.
- Exclusions: Skip the full steppe-empire history; skip the Black Death connection to Mongol trade routes (a separate card); do not attempt to settle the population-loss debate.
- Score: 9/10

---

## Candidate 02 — Verify the Black Death's Origins and Spread with Claude

- Source: history-world-history/chapters/20-climate-change-and-plague-in-the-fourteenth-century.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Black Death killed 30–60% of Europe's population in 4 years. Claude knows this. But the origin story — the Mongol siege of Caffa, the rat-flea-human transmission chain, the genetic evidence from ancient DNA — is harder to verify and harder to prompt correctly.
- The artifact: A sourced 4-section brief — (1) the origin: what the current genetic evidence says about the Black Death's Central Asian origin (ancient DNA studies 2022–2024); (2) the transmission route from Central Asia to Europe via the Silk Road and the Caffa hypothesis; (3) the mortality estimates: range for Europe (30–60%), range for Middle East and China — how settled are these figures?; (4) the Little Ice Age connection: what evidence links the mid-14th century climate shift to plague emergence and spread.
- Prompt seed: `claude "Research the Black Death's origins and spread. Cover: (1) the most current genetic/paleogenomic evidence on where it originated and when, (2) the Caffa siege hypothesis for European entry, (3) mortality estimates for Europe, the Middle East, and China with confidence levels for each, (4) the evidence linking the Little Ice Age to plague conditions. Cite specific studies, especially recent ancient DNA research. Flag any claims that conflict between older and newer research."`
- Read / check: Verify that the ancient DNA evidence is mentioned (real studies from 2022 — Slavin, Krause, and colleagues identified the Central Asian origin in Kyrgyzstan cemetery remains); verify Caffa hypothesis is presented as hypothesis, not settled fact; check that European mortality range (30–60%) is presented as range, not a single number. Flag if Claude gives mortality as a single precise figure.
- Human supplies: Nothing — Claude synthesizes. Human should verify the 2022 ancient DNA study citation (Nature or equivalent — it is real).
- Output medium: Remotion slate (4-section brief: origin evidence, transmission route map description, mortality table with confidence levels, climate connection section)
- The change: Run the same question on the 2022 ancient DNA evidence specifically: ask Claude to describe what the Kyrgyzstan cemetery findings showed. This tests whether Claude's training includes the most recent research — if it doesn't, that gap is itself a finding about model knowledge cutoffs.
- Teardown angle: The Black Death research is still active — ancient DNA studies are revising the origin story in real time. This is the strongest case for the "verify" discipline: the most recent evidence may not be in Claude's training distribution, and the human step is to check publication dates.
- Exclusions: Skip the full 14th-century crisis context; skip the subsequent plague waves; do not attempt to verify mortality estimates independently (the demographic data requires specialist access).
- Score: 9/10

---

## Candidate 03 — Research the Rise of Islam with Claude: A Verification Exercise

- Source: history-world-history/chapters/14-the-rise-of-islam-and-the-caliphates.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Hijra — Muhammad's migration from Mecca to Yathrib — in 622 CE is the founding event of the Islamic calendar. Claude knows this. What it does less reliably is the specific political and theological context of the first four Caliphates and where historical consensus ends and sectarian interpretation begins.
- The artifact: A sourced 3-section brief — (1) the verified political history of the four Rashidun Caliphs (632–661 CE): who succeeded whom, the specific political conflicts (Ali vs. Muawiyah, Battle of Karbala) that produced the Sunni-Shia split; (2) the Umayyad and Abbasid expansion: geographic extent, dates, administrative innovations; (3) a verification note on where the historical record is clear vs. where it is contested by the sources themselves (early Islamic historians writing generations after the events). A "source-type" annotation: what is in the Quran, what is in hadith, what is in later historical chronicles.
- Prompt seed: `claude "Describe the political history of the first four Caliphates after Muhammad's death (632 CE). Include: (1) the succession disputes and their outcomes, (2) the specific events that led to the Sunni-Shia split, (3) the geographic expansion under each Caliph. Then: for each major event you describe, identify whether the evidence comes from: (a) near-contemporary sources, (b) later chronicles, or (c) religious tradition. Flag where historians disagree."`
- Read / check: Verify the first four Caliphs (Abu Bakr, Umar, Uthman, Ali) are correctly named and sequenced; verify the Battle of Karbala date (680 CE — under Yazid, Umayyad period — not during the Rashidun Caliphate itself — flag if Claude conflates timelines); check that at least one historiographical debate is named (e.g., the reliability of Ibn Ishaq's biography of Muhammad).
- Human supplies: Nothing — Claude synthesizes. Human verifies at least the Caliph sequence against the textbook chapter.
- Output medium: Remotion slate (3-section brief: Rashidun table with source annotations, expansion section, historiographical debate section)
- The change: Ask Claude to describe the same events from two different historiographical traditions: (a) as a secular historian would frame them; (b) as a believing Muslim historian would frame them. Show how the framing differs — not to privilege one over the other, but to demonstrate that the same events carry different weight in different traditions.
- Teardown angle: The early Islamic period is a case where the distinction between historical evidence and religious tradition is itself a contested question. The research brief doesn't resolve it — it makes the distinction visible so the viewer can engage with the sources consciously.
- Exclusions: Skip the theological content of Islam; skip the later Abbasid period; do not attempt to adjudicate Sunni vs. Shia historical claims.
- Score: 8/10

---

## Candidate 04 — Build a Primary Source Comparison: Roman Empire Perspectives

- Source: history-world-history/chapters/09-experiencing-the-roman-empire.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Roman Empire looks different depending on who you were: a senator, a slave, a tax collector, or a worshipping Christian. Can Claude synthesize evidence from different social perspectives — and can you verify that the evidence is primary?
- The artifact: A sourced 4-perspective brief — (1) the senator's perspective: political institutions, the Senate's role under Augustus, Tacitus's view; (2) the slave's perspective: what documentary evidence exists for slave experience in Rome (manumission records, epitaphs, the Digest of Justinian); (3) the provincial taxpayer's perspective: evidence from papyri (Egypt), tax records, complaints to Roman administrators; (4) the early Christian's perspective: what the Gospels and early church letters say about life under Roman rule. For each perspective, a source-type annotation: what is primary, what is secondary synthesis.
- Prompt seed: `claude "Synthesize evidence about life in the Roman Empire from four perspectives: senator, slave, provincial taxpayer, and early Christian. For each: (1) describe 2-3 aspects of their experience, (2) name a specific primary source (document, inscription, papyrus, or text) that provides evidence for each perspective, (3) identify what each primary source type cannot tell us. Flag where Claude is synthesizing from secondary sources rather than citing primary evidence directly."`
- Read / check: Verify Tacitus is a valid source for the senatorial perspective (real — Annals, Histories); verify papyri are a valid source for provincial life (real — extensive Egyptian papyrus record); check that slave experience sources are real (manumission inscriptions exist; the Digest has slave law); flag if Claude fabricates specific papyrus citations.
- Human supplies: Nothing — Claude synthesizes. Human should verify at least 1 papyrus source against a real database (Duke Databank of Documentary Papyri or equivalent).
- Output medium: Remotion slate (4-perspective grid — each perspective a quadrant with experience summary, primary source named, and "evidence gap" annotation)
- The change: Add a fifth perspective: a Roman soldier on the frontier. Show how the military papyri from Egypt (Vindolanda tablets equivalent for the eastern frontier) provide evidence for daily military life — and what they don't tell us about combat experience.
- Teardown angle: The "experiencing" framing is the textbook's analytical move — and Claude handles it well when prompted specifically. The research discipline is verifying that the named primary sources are real and accessible, not synthesized from secondary descriptions of what the sources say.
- Exclusions: Skip the full Roman political history; skip the fall of Rome; do not attempt a comprehensive survey of Roman social history.
- Score: 8/10

---

## Candidate 05 — Research the Little Ice Age and 14th-Century Crisis with Claude

- Source: history-world-history/chapters/20-climate-change-and-plague-in-the-fourteenth-century.md
- Lane: RESEARCH (Claude assistant)
- Hook: Climate historians have reconstructed a 14th-century cooling that preceded the Black Death by two decades. Can Claude describe the evidence for the Little Ice Age — and distinguish between what the data shows and what is inferred?
- The artifact: A sourced 3-section brief — (1) what the Little Ice Age was: temperature reconstruction methods (tree rings, ice cores, pollen records), when it is dated, how severe the cooling was; (2) the 14th-century crisis chain: famine (1315–1322 Great Famine of Europe), then plague (1347–1353) — what the causal links are and how historians debate them; (3) a contemporary evidence check: what did 14th-century writers observe about the weather, and how do their accounts compare to the paleoclimate data?
- Prompt seed: `claude "Describe the Little Ice Age and its role in the 14th-century crisis. Include: (1) the methods historians and climate scientists use to reconstruct pre-industrial climate (tree rings, ice cores, pollen analysis), (2) the Great Famine of 1315-1322 and its connection to climate, (3) whether the causal link between climate change and plague is established or inferred. Cite specific studies. Flag claims where the evidence is indirect or contested."`
- Read / check: Verify the Great Famine dates (1315–1322 — real); verify that climate reconstruction methods are correctly described (tree rings, ice cores — real methods); check that the climate-plague causal link is presented as inferred/debated rather than settled. Flag if Claude presents the causal chain as direct and established.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 1 paleoclimate study citation.
- Output medium: Remotion slate (3-section brief: climate reconstruction methods table, crisis chain timeline, evidence-type annotations throughout)
- The change: Add a contemporary source: find an excerpt from a 14th-century chronicle that describes unusual weather or crop failure. Ask Claude to locate one and then verify it against a real chronicle (Jean de Venette is a real source). Show the process of verifying that a medieval source actually says what Claude claims.
- Teardown angle: Climate history requires integrating physical evidence (ice cores, tree rings) with documentary evidence (chronicles, tax records) — two different source types with different reliability profiles. The research brief models how to hold both together without conflating them.
- Exclusions: Skip the modern climate change connection (out of scope for a medieval history card); skip the full Black Death card (covered in card 02); do not attempt to verify ice core data independently.
- Score: 8/10

---

## Candidate 06 — Research the Bantu Migrations with Claude

- Source: history-world-history/chapters/19-states-and-societies-in-sub-saharan-africa.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Bantu migrations — the spread of agricultural peoples and ironworking across sub-Saharan Africa over 3,000 years — are one of the most significant population movements in human history and one of the least-covered in standard textbooks. Does Claude know the evidence base?
- The artifact: A sourced 3-section brief — (1) the linguistic evidence: what the distribution of Bantu languages tells us about migration routes and timing; (2) the archaeological evidence: ironworking sites, agricultural expansion evidence, pottery traditions used as chronological markers; (3) the genetic evidence: what ancient and modern DNA studies show about Bantu expansion. A "convergence" section: where all three evidence types agree and where they diverge.
- Prompt seed: `claude "Describe the Bantu migrations across sub-Saharan Africa. Include: (1) what the linguistic evidence (the Bantu language family) tells us about the origin point and spread pattern, (2) what archaeological evidence (ironworking, pottery, agricultural sites) shows, (3) what genetic evidence adds. Where do these three evidence types agree and where do they diverge? Cite specific studies or evidence types. Flag where the evidence is thin."`
- Read / check: Verify the proposed origin region for Bantu languages (northwestern Cameroon/Nigeria border — real, widely accepted); verify ironworking is a key marker (real); check that genetic evidence is presented as a more recent addition to the picture (ancient DNA studies are recent — post-2010). Flag if Claude gives a falsely precise timeline for the migrations (they span centuries and the dates are approximate).
- Human supplies: Nothing — Claude synthesizes. Human verifies the linguistic origin claim against at least 1 secondary source (Ehret 2001 or equivalent).
- Output medium: Remotion slate (3-section brief: linguistic evidence with map description, archaeological markers table, genetic evidence section, convergence/divergence summary)
- The change: Ask Claude to identify the regions where the Bantu expansion evidence is strongest vs. weakest. This surfaces what the training distribution covers well (linguistic evidence, widely published) vs. poorly (genetic evidence from specific sites, more recent). The gap is informative.
- Teardown angle: The Bantu migrations are a case where multiple evidence types — linguistic, archaeological, genetic — need to be triangulated. No single type is sufficient. The research brief models the triangulation discipline: what do the sources agree on, what do they disagree on, and what does neither tell us?
- Exclusions: Skip the full sub-Saharan African political history; skip the contemporary implications; do not attempt to date the migrations precisely (the ranges are too wide for a precise claim).
- Score: 8/10

---

## Candidate 07 — Probe Claude on the Roman Fall: Primary vs. Secondary Evidence

- Source: history-world-history/chapters/09-experiencing-the-roman-empire.md + chapters/13-empires-of-faith.md
- Lane: RESEARCH (Claude assistant)
- Hook: Edward Gibbon wrote the definitive account of Rome's decline in 1776. Historians have been revising it ever since — but the Gibbon narrative is so thoroughly in the training distribution that Claude may reproduce it uncritically. Does it?
- The artifact: A sourced 3-section brief — (1) Gibbon's thesis (decline and fall due to Christianity and barbarian invasions) — what Gibbon actually argued; (2) the major 20th-century revisions (economic, demographic, institutional, climate-related explanations); (3) a prompt-comparison: what does Claude say about Rome's fall when asked "Why did Rome fall?" vs. "What is the current historiography on Rome's decline?" — do the responses differ?
- Prompt seed: `claude "What are the major historiographical explanations for the decline and fall of the Western Roman Empire? Include: (1) what Edward Gibbon argued in the 18th century, (2) major 20th-century revisions to Gibbon's thesis, (3) the most recent scholarly emphasis (economic, demographic, climate, or institutional). For each explanation, name the historians associated with it and cite a publication. Flag where scholars disagree."`
- Read / check: Verify Gibbon is correctly characterized (Christianity as enervating force + Germanic invasions); verify at least one revisionist is named (Bryan Ward-Perkins for material decline, Peter Heather for barbarian agency, Kyle Harper for climate/disease); flag if Claude presents a single unified explanation as consensus when the field is genuinely divided.
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 1 revisionist citation.
- Output medium: Remotion slate (3-section brief: Gibbon thesis, revision table with historians, current emphasis summary; framing-comparison result)
- The change: Run the framing-comparison test: "Why did Rome fall?" vs. "What does the current scholarship say about Rome's decline?" Compare the two responses — which Gibbon elements survive in the open-ended version that the historiography version explicitly revises?
- Teardown angle: The Gibbon narrative is deeply embedded in the training distribution because Decline and Fall is one of the most cited historical texts in English. The "compare" move — asking once openly, once with historiographical framing — reveals the model's default vs. its more considered output.
- Exclusions: Skip the Eastern Roman Empire history; skip the specific barbarian kingdoms; do not attempt to settle the decline debate.
- Score: 7/10

---

## Candidate 08 — Research Early Civilizations: What the Archaeological Evidence Actually Shows

- Source: history-world-history/chapters/04-early-civilizations-and-urban-societies.md
- Lane: RESEARCH (Claude assistant)
- Hook: The "first cities" narrative — Uruk, Mesopotamia, around 3000 BCE — is real. But the comparative story (was urbanism invented once or independently multiple times?) is more complex than most textbooks represent. Does Claude know the comparative evidence?
- The artifact: A sourced 3-section brief — (1) Mesopotamia: what the archaeological evidence for Uruk shows (population estimates, administrative innovations, writing emergence); (2) independent urban development: evidence from the Indus Valley, Yellow River Valley, Mesoamerica, and Andean regions — what the dates and evidence types are; (3) the "first cities" debate: is "first" a meaningful category given the difficulty of dating and the different definitions of "city"?
- Prompt seed: `claude "Research the emergence of early cities and urban societies. Include: (1) what the archaeological evidence shows for Uruk (Mesopotamia) as an early urban center — population estimates, administrative evidence, writing, (2) evidence for independent urban development in the Indus Valley, Yellow River Valley, Mesoamerica, and the Andes, (3) what definitions of 'city' archaeologists use and whether 'first city' is a meaningful claim. Flag contested dates and definitions."`
- Read / check: Verify Uruk dates (~3500–3000 BCE for early urban features — real); verify Indus Valley urbanism (Mohenjo-Daro, ~2500 BCE — real); check that Yellow River urbanism is given approximate dates (Erlitou ~2000 BCE); flag if Claude presents Uruk as the uncontested first city (the Çatalhöyük debate makes "first" contested).
- Human supplies: Nothing — Claude synthesizes. Human verifies at least 1 archaeological date against a secondary source.
- Output medium: Remotion slate (3-section brief: Uruk evidence table, comparative urbanism timeline, "first city" debate section)
- The change: Ask Claude specifically about Çatalhöyük (7500–5700 BCE, Turkey) — is it a city? This is a genuine debate. Show how the response depends on the definition of "city" used, demonstrating that the research brief's conceptual clarification (section 3) is load-bearing, not optional.
- Teardown angle: The "first" question in early history is almost always methodologically fraught — it depends on definitions, on what evidence survives, and on which regions have been excavated. The research brief models the discipline of surfacing the definition before accepting the claim.
- Exclusions: Skip the full ancient Mesopotamia history; skip writing system origins; do not attempt to cover all early civilizations in one card.
- Score: 7/10

---

## Candidate 09 — Research the Ottoman Empire's Administrative Innovations with Claude

- Source: history-world-history/chapters/21-the-ottomans-the-mamluks-and-the-ming.md
- Lane: RESEARCH (Claude assistant)
- Hook: The Ottoman millet system governed multi-religious empire for centuries. Claude knows the name. Does it know the specific mechanisms, the documented outcomes, and where Ottoman-era records survive?
- The artifact: A sourced 3-section brief — (1) the millet system: what it was, which communities it governed, what rights and obligations it created; (2) the devshirme (child recruitment) system: documented evidence for how it operated, which regions it drew from, what the career paths were; (3) where Ottoman administrative records survive and what they show — the imperial archive (Başbakanlık Osmanlı Arşivi) as a primary source base.
- Prompt seed: `claude "Describe the Ottoman administrative innovations: (1) the millet system — what communities it governed and what rights/obligations it created, (2) the devshirme system — what the evidence shows about how it operated and who it recruited, (3) what Ottoman primary source records survive and what historians can reconstruct from them. Cite at least one Ottoman-era source type and flag where the evidence is reconstructed from later accounts."`
- Read / check: Verify the millet system description (non-Muslim communities governed by own religious leaders — real); verify devshirme is correctly described (levy of Christian boys for Janissary corps — real, documented); check that the Ottoman archive is mentioned as a real resource (it is — housed in Istanbul, digitization ongoing). Flag if Claude invents specific archival citations.
- Human supplies: Nothing — Claude synthesizes. Human verifies the millet system description against the textbook chapter.
- Output medium: Remotion slate (3-section brief: millet system table, devshirme section, primary source guide)
- The change: Ask Claude to describe what an Ottoman imperial register (defter) would show for a specific province. This tests whether Claude knows the specific document type (real — these record population, tax assessments, land holdings). If Claude describes it accurately, show the verification; if not, show the correction.
- Teardown angle: Ottoman history is a case where rich primary sources exist but are in Ottoman Turkish — a language requiring specialized training to read. The research brief models the discipline of knowing what primary sources exist even when the student cannot access them directly.
- Exclusions: Skip the full Ottoman military history; skip the decline and fall of the Ottoman Empire; do not attempt to access the Ottoman archive in the demo.
- Score: 7/10

---

## Candidate 10 — Verify the Confucius Historical Evidence with Claude

- Source: history-world-history/chapters/06-asia-in-ancient-times.md
- Lane: RESEARCH (Claude assistant)
- Hook: Confucius is one of the most cited thinkers in world history. What do we actually know about him as a historical person vs. what is later tradition? Claude will cite the Analects — but the Analects were compiled after Confucius's death by students, and the historical Confucius vs. the textual Confucius are different objects of study.
- The artifact: A sourced 3-section brief — (1) what the historical evidence actually shows: dates of Confucius's life (~551–479 BCE), the political context of the Warring States period, what contemporary or near-contemporary sources exist; (2) the Analects as a source: when it was compiled, how far removed it is from Confucius's life, what textual scholars have concluded about its reliability; (3) how the "historical Confucius" question compares to similar problems in other traditions (the historical Jesus, the historical Socrates) — all three known primarily through texts compiled by followers.
- Prompt seed: `claude "What do historians know about the historical Confucius as distinct from the textual tradition? Include: (1) what contemporary or near-contemporary evidence exists for his life, (2) what is known about when the Analects were compiled and how far removed from Confucius the compilers were, (3) how textual scholars assess the Analects' reliability as historical evidence. Compare to the similar 'historical vs. textual' problems for Socrates and Jesus."`
- Read / check: Verify Confucius dates (~551–479 BCE — real, widely accepted); verify the Analects were compiled by students and later editors (real — the final compilation is debated but probably post-death); check that the Socrates/Plato parallel is correctly drawn (Socrates known only through Plato and Xenophon). Flag if Claude presents the Analects as a contemporaneous record.
- Human supplies: Nothing — Claude synthesizes. Human verifies the Analects compilation timeline against at least 1 secondary source.
- Output medium: Remotion slate (3-section brief: historical evidence, Analects as source, comparative "historical vs. textual" table)
- The change: Ask Claude for the most confident historical fact we know about Confucius vs. the most uncertain. This surfaces the gradient — what is well-attested (he was an official in Lu, he traveled, he taught) vs. what is traditional attribution (many statements in the Analects may be later additions). The gradient is the lesson.
- Teardown angle: The "historical vs. textual" problem is the world history equivalent of the US history model-consistency test: the same figure looks different depending on whether you're asking about the historical evidence or the tradition. Both are real objects of study; conflating them is the error.
- Exclusions: Skip the full Confucian philosophical content; skip the later Neo-Confucian tradition; do not attempt to verify the Analects against the original text.
- Score: 7/10
