# Chapter 16 — Disease and Epidemiology

*A pandemic is a single disease wearing the same face in millions of bodies.*

## The question before the answer

In August 1854, a London neighborhood called Soho saw cholera cases erupt in concentrated numbers. People got sick within hours of exposure, lost liters of fluid to diarrhea, and died of dehydration within a day or two. By the time the outbreak ended, more than 600 people had died within a few blocks.

The cause was unknown. The dominant theory was miasma — bad air. Most cases occurred near reeking sewers and stagnant water, which fit the miasma theory perfectly.

John Snow, a London physician, was suspicious. He had argued for years that cholera was waterborne, not airborne. So he did something simple and radical: he mapped the deaths. He took a paper map of Soho and put a black bar at each address where someone had died. The pattern that emerged was not random. The deaths clustered around a specific water pump on Broad Street.

Snow walked to the parish board and asked them to remove the handle from the Broad Street pump. They did. The outbreak ended within days. [^1]

This was the founding event of epidemiology. Snow had no microscope good enough to see *Vibrio cholerae*. He had no germ theory that would have been accepted by the medical establishment. He had a map, a hypothesis about how cholera spread, and the discipline to test it with the simplest possible intervention. The point of this chapter is to understand how that mode of reasoning — patterns in populations, sources traced, transmission interrupted — became the basis for managing infectious disease at the scale of communities, countries, and the world.

↳ **Dig Deeper — The Snow map as data visualization**

*The Broad Street map is one of the most reproduced images in epidemiology. Looking carefully at the actual map, rather than the schematic textbook version, is worth doing.*

**Prompt:**
> Find and describe John Snow's actual 1854 map of cholera deaths in Soho. What features does the map include that the simplified textbook versions usually omit? How does Snow indicate the location of the Broad Street pump and the other neighborhood pumps? What does the cluster pattern look like in detail (note: it is not a perfect circle around the pump)? Then discuss the analytical decisions Snow made: the natural-experiment comparisons with brewery workers (who drank only beer), the Lambeth vs. Southwark and Vauxhall water comparison. What does the map teach us about data visualization that modern epidemiology has internalized?

**What to do with the output:** The Snow map is the founding visual document of epidemiology. Knowing it well rather than knowing it by reputation is worth the time. Pair with Florence Nightingale's coxcomb diagrams for a deeper sense of Victorian data viz.

## Learning objectives

By the end of this chapter, you will be able to:

1. Distinguish prevalence from incidence and calculate each from raw data.
2. Distinguish sporadic, endemic, epidemic, and pandemic disease patterns.
3. Identify the major types of epidemiological study (descriptive, analytical, experimental) and what each can establish.
4. Describe disease reservoirs and the major modes of transmission (contact, vector, vehicle).
5. Describe the role of WHO and CDC in surveillance and response.
6. Distinguish emerging from reemerging infectious diseases and identify the major factors driving emergence.

Prerequisites: Chapters 1–15.

## Counting disease

**Prevalence** is the fraction of a population that has a particular disease at a given time. If 1 in 1,000 adults in a city has tuberculosis on January 1, the TB prevalence is 0.001 or 100 per 100,000.

**Incidence** is the rate at which new cases develop. If 50 new TB cases are diagnosed in that city over a year, in a population of 1 million, the annual TB incidence is 5 per 100,000 per year.

The two metrics measure different things and can move in opposite directions. A disease can have high prevalence but low incidence if it is chronic (HIV before effective antiretroviral therapy: high prevalence, modest incidence). A disease can have high incidence but low prevalence if it is short-lived (acute viral gastroenteritis: most cases resolve in days).

For public health planning, you need both. Prevalence tells you how many people currently need care. Incidence tells you whether the problem is growing, stable, or shrinking. A high prevalence with declining incidence means the existing case load is large but new infections are slowing; the system is winning. A low prevalence with rising incidence means a new threat is gaining; the system needs to act.

## Patterns of disease in populations

**Sporadic**: occasional cases, no regular pattern. Tetanus in the developed world is sporadic — a few cases each year, scattered geographically.

**Endemic**: present at a consistent baseline level in a population or region. Malaria is endemic in sub-Saharan Africa and parts of Southeast Asia. Lyme disease is endemic in parts of the northeastern US.

**Epidemic**: a sudden increase in cases above the endemic baseline. The 1854 Broad Street cholera outbreak was an epidemic. So was the 2014 Ebola outbreak in West Africa.

**Pandemic**: an epidemic across multiple countries or continents. Influenza pandemics in 1918, 1957, 1968, 2009. HIV/AIDS from the 1980s onward. COVID-19 from 2020.

The boundaries between these categories are not precise. A disease that is endemic in one region can be epidemic when it appears somewhere new. Outbreak investigations begin with surveillance: case counts compared against baseline expectations, geographic clustering, temporal patterns.

## Modes of transmission

Pathogens spread between hosts in characteristic ways. Understanding the mode of transmission is the basis for breaking transmission chains.

### Contact transmission

**Direct contact**: physical touch between an infected and uninfected person. Sexually transmitted infections, MRSA on skin, herpes from kissing.

**Indirect contact**: through an intermediate object (a fomite — a surface or item that carries the pathogen). Norovirus on a doorknob. Influenza on a phone. The pathogen has to survive on the fomite long enough to transfer.

**Droplet transmission**: large respiratory droplets that fall within a meter or so of the source. Influenza, pertussis, meningococcal disease. Masks and distance reduce transmission.

### Vehicle transmission

The pathogen is carried by a non-living medium that delivers it to many people simultaneously.

**Foodborne**: *Salmonella* in undercooked eggs, *Listeria* in soft cheeses, *E. coli* O157:H7 in undercooked ground beef.

**Waterborne**: *Vibrio cholerae* in contaminated drinking water, *Cryptosporidium* in pool water, *Legionella* in cooling tower mist.

**Airborne**: pathogens that travel as small particles (aerosols) over longer distances. Measles, tuberculosis, varicella, COVID-19 (which has both droplet and airborne components). Airborne transmission is harder to control than droplet because the particles travel further and stay in the air longer.

### Vector transmission

A living organism (usually an arthropod) carries the pathogen.

**Mechanical vectors** transmit pathogens passively on their bodies. A fly that lands on feces and then on food can transfer pathogens to the food.

**Biological vectors** harbor the pathogen and often serve as part of its life cycle. Anopheles mosquitoes carry *Plasmodium* through specific developmental stages. Aedes mosquitoes carry dengue, yellow fever, Zika, chikungunya. Ixodes ticks carry *Borrelia burgdorferi* (Lyme). The flea *Xenopsylla cheopis* carries *Yersinia pestis*.

The vector is often essential — *Plasmodium falciparum* must complete part of its life cycle in mosquitoes; the parasite cannot transmit directly from human to human. Vector control (insecticides, breeding-site elimination, bed nets) is therefore central to controlling vector-borne disease.

## Reservoirs and carriers

A **reservoir** is the natural habitat in which a pathogen lives and multiplies. Some are obvious (humans for HIV, mosquitoes-and-humans for malaria). Some are non-obvious. *Yersinia pestis* lives in wild rodents, with humans as occasional hosts. *Histoplasma capsulatum* lives in soil enriched with bird or bat guano. *Legionella* lives in warm freshwater and biofilms.

A **carrier** is a person (or animal) who harbors and can transmit a pathogen without showing symptoms. *Salmonella* Typhi can be carried for life by a small fraction of recovered patients — Mary Mallon ("Typhoid Mary") was a chronic carrier who worked as a cook in early 1900s New York, infecting at least 51 people. *N. meningitidis* is carried in the throat by 5–25% of healthy people. HIV can be transmitted by carriers who do not yet know they are infected.

The reservoir framework drives surveillance strategy. To control plague, you monitor wild rodent populations. To control Legionnaires' disease, you test cooling towers. To control influenza, you survey poultry, pigs, and wild birds in addition to humans, because the reservoir is broader than humans alone.

## Three modes of epidemiology

**Descriptive epidemiology** characterizes who gets the disease, where, and when. The shape of the data. Cases by age, sex, occupation, geography. Time trends. This is the foundation for hypothesis generation.

**Analytical epidemiology** tests hypotheses about cause. The two main designs:

- **Case-control studies**: identify people with the disease (cases) and similar people without (controls), then look back to see what exposures differed. Used when the disease is rare. The 1976 Legionnaires' disease outbreak was characterized through case-control investigation.
- **Cohort studies**: identify exposed and unexposed groups and follow them forward to see who develops disease. Stronger causal inference than case-control, but more expensive and slower. The Framingham Heart Study is the classic example for cardiovascular epidemiology.

**Experimental epidemiology** intervenes, often in randomized trials. Randomized vaccine efficacy trials. Cluster-randomized trials of insecticide-treated bed nets for malaria. The intervention is the strongest design for establishing causation but is logistically and ethically limited — you cannot randomize people to acquire a pathogen.

## Establishing the cause of an outbreak

When an outbreak is recognized, the investigation usually follows a stereotyped pattern:

1. **Confirm the outbreak**. Are these cases actually above baseline? Sometimes apparent outbreaks are surveillance artifacts.

2. **Verify the diagnosis**. Are the cases really the same disease? Confirm by laboratory testing.

3. **Define a case**. Establish criteria for what counts as a case in this outbreak. Include symptoms, dates, location.

4. **Find cases**. Active surveillance — calling hospitals, clinics, labs to find all matching cases.

5. **Describe the data**. By person, place, time. Generate hypotheses about cause.

6. **Test hypotheses**. Case-control study of likely exposures, environmental sampling, laboratory work.

7. **Implement control measures**. Remove the pump handle. Close the contaminated facility. Quarantine the exposed.

8. **Communicate findings**. To health authorities, healthcare providers, the public.

The 1976 Legionnaires' disease investigation followed this pattern. Two hundred people who attended a Pennsylvania American Legion convention developed pneumonia; 34 died. The pathogen could not be cultured initially. Investigators eventually identified a previously unknown bacterium (*Legionella pneumophila*) replicating in the convention hotel's cooling tower. The water cooled by the tower was aerosolized; convention attendees inhaled the aerosol and developed pneumonia. *Legionella* is now known to be a common environmental organism and is a leading cause of pneumonia from contaminated water systems. [^2]

## The pioneers

Snow on cholera (1854). Snow is often called the founder of modern epidemiology. The Broad Street pump story is a teaching example because Snow combined careful case mapping, hypothesis testing, and a low-cost intervention that worked.

Ignaz Semmelweis on puerperal fever (1847). We met him in Chapter 3. His handwashing intervention was epidemiological in its logic — he compared mortality rates between two wards, identified a difference, hypothesized a cause, and tested it with an intervention. The fact that he was right and was ignored anyway is part of the history of how slowly evidence sometimes converts into policy.

Florence Nightingale on military hospital mortality (1854–1860). Nightingale's contribution was not new pathogens or new mechanisms but new methods of data visualization. Her "coxcomb diagrams" — polar area charts showing the causes of mortality in British military hospitals during the Crimean War — communicated that more soldiers were dying from infection in hospitals than from battlefield wounds. The data drove policy change in military medical care. Nightingale was elected the first female fellow of the Royal Statistical Society for this work. [^3]

Joseph Lister on antiseptic surgery (1867). Applied Pasteur's germ theory to surgical wound infection. His use of carbolic acid (phenol) for instruments and wound dressing reduced postoperative mortality in his ward dramatically.

Robert Koch on causation in infectious disease. Already discussed in Chapter 1 and Chapter 15.

## Global infrastructure

### WHO

The **World Health Organization** is the United Nations agency for international public health. Founded 1948. Headquartered in Geneva. Mission: directing and coordinating health within the UN system, setting health norms and standards, providing technical support to countries, monitoring health trends, responding to health emergencies.

Some of the WHO's major achievements: smallpox eradication (declared 1980). Polio reduction (from 350,000 cases in 1988 to a few dozen wild-virus cases per year now). Childhood vaccination expansion. The HIV/AIDS response. Tobacco control framework (the first WHO treaty). COVID-19 pandemic response (with mixed reviews, depending on whose). The WHO classifies pandemic and public health emergencies and coordinates international response.

The WHO publishes the **International Classification of Diseases (ICD)**, a standardized system for coding diseases used in health records worldwide. ICD-11, the current revision, was released in 2018.

### CDC

The **Centers for Disease Control and Prevention** is the US federal public health agency. Founded 1946. Headquartered in Atlanta. Mission: protect Americans from health, safety, and security threats, both foreign and in the US.

The CDC operates national surveillance systems (the National Notifiable Diseases Surveillance System), maintains a reference laboratory for unusual pathogens, conducts epidemiological investigations (the Epidemic Intelligence Service is the CDC's outbreak response team), and publishes the **Morbidity and Mortality Weekly Report (MMWR)** — the primary US publication for new outbreak data and recommendations.

Most countries have analogous national agencies — Public Health England (now UKHSA), Robert Koch Institute in Germany, ECDC for the European Union, Chinese CDC, etc. They coordinate with WHO and with each other on cross-border infectious disease issues.

### IHR

The **International Health Regulations** (IHR) are a binding international agreement among WHO member states for reporting, response, and prevention of public health emergencies of international concern (PHEICs). The IHR have been revised several times — most significantly in 2005 — to handle a wider range of threats including chemical and radiological events.

When the WHO Director-General declares a Public Health Emergency of International Concern, member states are obligated under the IHR to share information and coordinate response. Recent PHEIC declarations: 2009 H1N1 pandemic, 2014 Ebola in West Africa, 2014 polio resurgence, 2016 Zika, 2020 COVID-19, 2022 mpox.

## Emerging and reemerging diseases

**Emerging infectious diseases** are diseases that have appeared in a population for the first time or that have been known but are rapidly increasing in incidence or geographic range. The list since 1980 is striking: HIV/AIDS (1981), Lyme disease (1975, though probably ancient), Legionnaires' disease (1976), SARS (2003), MERS (2012), Ebola (more outbreaks since the original 1976 discovery), Zika (Americas 2015–2016), COVID-19 (2019), mpox global outbreak (2022). [^4]

**Reemerging infectious diseases** are those that had been controlled but are returning. Tuberculosis, particularly multi-drug-resistant forms. Pertussis, due to waning vaccination coverage. Measles, due to vaccine refusal. Dengue, due to climate change expanding mosquito ranges. Diphtheria in conflict zones with disrupted vaccination.

The major drivers of emergence and reemergence:

**Ecological change**. Deforestation, expanded agriculture, and urban encroachment bring humans into closer contact with wildlife reservoirs. Many emerging pathogens (Ebola, Nipah, COVID-19 likely, Hendra, Lassa) come from wildlife — bats, primates, rodents, civets — disturbed by human activity.

**Climate change**. Warming temperatures expand the geographic range of vectors and the seasons in which they are active. Lyme disease has moved north as winters have warmed. Dengue has expanded its global range. Malaria is appearing at higher altitudes in Africa than it did 50 years ago.

↳ **Dig Deeper — Climate change and the expanding map of vector-borne disease**

*The vector ranges that determine where dengue, Zika, and chikungunya can occur are moving with climate.*

**Prompt:**
> Describe the documented effects of climate change on infectious disease distribution. Cover *Aedes aegypti* and *Aedes albopictus* range expansion (the vectors of dengue, Zika, chikungunya, yellow fever) into temperate regions including the southern United States and southern Europe; the northward expansion of *Ixodes scapularis* (Lyme disease tick) in the US and Canada; the altitudinal expansion of *Plasmodium* and *Anopheles* in East African highlands; the increasing severity and frequency of *Vibrio* infections in warmer coastal waters. End by predicting which diseases will move into new regions over the next 30 years.

**What to do with the output:** Public health planning over the next decades depends on getting these projections right. Save the answer; carry to clinical chapters where regional disease distributions matter (especially Chapter 25, mosquito-borne infections).

**Globalization of travel and trade**. A pathogen that emerges anywhere can be anywhere within days. SARS spread internationally in weeks. COVID-19 spread globally before most people knew it existed. Food chains stretch across continents, so a contamination in one place can produce illness on another.

**Antimicrobial resistance**. We covered this in Chapter 14. Many old pathogens are returning as resistance erodes treatment options.

**Vaccine refusal**. The decline in measles vaccination has reignited outbreaks in countries that had effectively eliminated the disease. Pertussis outbreaks in undervaccinated communities. The mechanism is mathematical: herd immunity requires high vaccination coverage; when coverage drops, the disease comes back.

**Healthcare-associated transmission**. *C. difficile*, MRSA, CRE (carbapenem-resistant enterobacteriaceae), *Candida auris* — most of these are pathogens that primarily spread in healthcare settings, and their incidence has grown with the complexity of modern medicine.

**Bioterrorism**. Deliberate release of pathogens is the subject of an entire parallel field (biodefense). The 2001 anthrax letters in the US, the Aum Shinrikyo cult's earlier attempts to deploy *Bacillus anthracis* and *Clostridium botulinum*, and concerns about smallpox stocks all illustrate that intentional pathogen release is a real category.

## R₀ and herd immunity

The **basic reproduction number** (R₀) of a pathogen is the average number of secondary infections produced by one infected person in a fully susceptible population. R₀ above 1 means the epidemic grows. R₀ below 1 means it dies out.

R₀ varies by pathogen:

- Measles: 12–18 (extraordinarily contagious)
- Pertussis: 12–17
- Smallpox: 5–7
- SARS-CoV-2 (original): 2–3; later variants higher
- Influenza: 1.5–2
- Ebola: 1.5–2.5

R₀ alone does not tell you the whole picture. It depends on the population's mixing patterns (sexual contacts for STIs, respiratory contacts for airborne pathogens), the duration of infectiousness, and the susceptibility profile. The same pathogen can have different R₀ in different populations.

The threshold for herd immunity — the fraction of the population that must be immune for the epidemic to die out — is approximately 1 − 1/R₀. For measles (R₀ ~15), about 93% of the population must be immune. For influenza (R₀ ~2), about 50%. The high herd immunity threshold for measles is why vaccination rates need to be near-universal to prevent outbreaks; even small drops in coverage permit measles to return.

R₀ is heavily used in early outbreak modeling and pandemic response planning. It is also frequently misused. R₀ is a property of pathogen-and-population, not just pathogen. R₀ in a dense city is different from R₀ in a rural area. R₀ under social distancing is different from R₀ without. Single-number summaries are useful but should not be over-interpreted.

↳ **Dig Deeper — Beyond R₀: superspreading and overdispersion**

*R₀ is an average. The actual distribution of how many people each infected person infects is wildly uneven, and that unevenness matters for control.*

**Prompt:**
> Describe the concept of overdispersion in infectious disease transmission and how it differs from a simple R₀ value. What is the dispersion parameter k, and what does a low k tell you about how transmission actually occurs? Cover specific examples — SARS-CoV-1 (highly overdispersed; few cases responsible for most transmission), measles (less overdispersed), tuberculosis (intermediate). Then discuss what overdispersion implies for control strategies: how does targeting superspreading events differ from blanket population measures? What does this mean for contact tracing?

**What to do with the output:** This is one of the more important pieces of modern epidemiology that R₀-centric reporting tends to miss. The skewed distribution of transmission is the rule, not the exception.

## What the chapter is really about

Epidemiology is the science of patterns in disease populations. It is the layer of microbiology that operates above the individual patient, looking for the structure of how disease moves through groups of people, animals, and environments.

The methods are old but the questions are not. John Snow mapped cholera deaths in 1854 with a paper map and a pencil. Modern epidemiologists use genome sequencing to track outbreaks in real time, mathematical models to predict spread, contact-tracing apps on smartphones to follow individual exposures. The tools have changed; the underlying logic — describe, hypothesize, test, intervene — has not.

For the chapters that follow (21–26), where we will be discussing specific organ-system infections, keep two pieces of epidemiological framing in mind. First: a pathogen and its disease are not the same thing. The same pathogen can produce different syndromes in different hosts; the same syndrome can result from different pathogens. Second: every infection is part of a network of transmission. Asking how it got to this patient, and how it could get to the next one, is part of understanding it.

## Still puzzling

I do not fully understand why some pathogens emerge from a long history of stable host-pathogen coexistence into outbreaks affecting humans. Bats appear to be reservoirs for many emerging viruses (Ebola, Nipah, several coronaviruses including likely SARS-CoV-2). Bat physiology — their immune systems, body temperature, and longevity — appears to make them well-adapted hosts for these viruses. The bat-to-human jump has happened multiple times. The factors that determine which bat-borne pathogen jumps successfully into humans and which doesn't are not fully understood. There is presumably a mix of viral genetics, intermediate host opportunities, human behavior, and chance. The bat reservoir is large; the spillover events are rare; but the rare ones can change history.

## What would change my mind

The standard epidemiological framework treats human populations as well-mixed at relevant scales. Real human mixing is heterogeneous — there are superspreader events, dense clusters, sparse contacts — and modern epidemiology incorporates these to some extent through network-based models. If contact tracing data from recent outbreaks (COVID-19 in particular) substantially revise the picture of how respiratory pathogens propagate (e.g., showing that R₀ is a much less useful summary than the field has treated it), the simple R₀-and-threshold framework will need substantial nuance. `[verify: 2020–2025 literature on network epidemiology and superspreading dynamics]`

## LLM exercises

1. **The Snow analysis.** Tell the LLM you have a list of cholera deaths in 1854 Soho with addresses and dates. Ask it how to analyze the data to identify the source. Compare to what Snow did. The exercise is about the simplicity and power of careful descriptive epidemiology.
2. **Calculating from raw data.** Give the LLM hypothetical disease numbers: in a city of 1 million, 800 people currently have disease X, with 120 new cases over the past year. Ask it to calculate prevalence, annual incidence, and average duration of disease (using the relationship: prevalence ≈ incidence × duration). Verify the calculation.
3. **An outbreak investigation.** Describe an outbreak scenario: 30 attendees at a wedding develop gastrointestinal symptoms 12 hours after the event. Ask the LLM to walk through the investigation step by step. What information do you collect? How do you generate hypotheses? What lab tests confirm? Compare to standard outbreak protocols.
4. **R₀ thinking.** Ask the LLM to explain how R₀ relates to herd immunity threshold for three pathogens of different transmissibility (measles, influenza, COVID-19). Then ask what mitigations affect R₀ in real outbreaks (vaccination, masking, distancing, contact tracing, isolation). Critique the assumption that R₀ is a fixed property of the pathogen.
5. **Emerging disease risk assessment.** Ask the LLM to identify three emerging diseases that should be high on the global pandemic-preparedness watchlist, with reasoning. Then critique the choices — what is the actual risk, what are the likely countermeasures, what would change the risk?

## References

[^1]: Snow, J. *On the Mode of Communication of Cholera*, 2nd ed. London: John Churchill, 1855. Available online at: https://www.ph.ucla.edu/epi/snow/snowbook.html
[^2]: Fraser, D.W. et al. "Legionnaires' disease: description of an epidemic of pneumonia." *New England Journal of Medicine* 297, no. 22 (1977): 1189–1197. doi:10.1056/NEJM197712012972201.
[^3]: McDonald, L. "Florence Nightingale and the early origins of evidence-based nursing." *Evidence-Based Nursing* 4, no. 3 (2001): 68–69. doi:10.1136/ebn.4.3.68.
[^4]: Morens, D.M., Folkers, G.K., Fauci, A.S. "The challenge of emerging and re-emerging infectious diseases." *Nature* 430, no. 6996 (2004): 242–249. doi:10.1038/nature02759.
---

## LLM Exercise — Chapter 16: Disease and Epidemiology (Microbe Profile Database Project)

**Project:** Microbe Profile Database.
**What you're building this chapter:** epidemiology fields — transmission, reservoir, geographic distribution, key outbreaks.
**Tool:** **Cowork**.

---

**The Prompt:**

```
Chapter 16 of my Microbe Database project. Chapter 16 covered
epidemiology — definitions (incidence vs. prevalence; endemic /
epidemic / pandemic; outbreak investigation); transmission routes
(airborne, droplet, contact, fecal-oral, vector-borne, vertical);
reservoirs (humans, animals, environment); R₀ (basic reproduction
number); herd immunity; Koch's postulates revisited (and the
limits — many pathogens fail Koch's standards but are still
pathogens).

Schema additions:
- **Transmission_route**: airborne / droplet / contact (direct or
  indirect) / fecal-oral / vector-borne (specify vector) /
  vertical (mother-to-fetus) / blood-borne / sexual.
- **Reservoir**: human-only / animal (zoonotic, specify animals)
  / environmental (water, soil) / multiple.
- **R0_estimate**: where known (Measles ~12-18, COVID ~3, Flu ~1.5).
- **Geographic_distribution**: global / regional (specify) /
  tropical / etc.
- **Notable_outbreaks**: 1-2 historical outbreaks (Black Death for
  *Y. pestis*; 1854 London for *V. cholerae*; 1976 Philly for
  Legionella; etc.).
- **Reportable_to_CDC**: yes/no.

Backfill for entries. Key examples:
- *V. cholerae*: fecal-oral; water reservoir; pandemic potential;
  Snow's 1854 Broad Street pump map is the founding event of
  epidemiology.
- *Y. pestis*: flea-vector; rodent reservoir; Black Death (50%
  Europe killed); now mostly rural in southwest US.
- *Mycobacterium tuberculosis*: airborne; human-only reservoir;
  global pandemic (1/3 humanity infected — most latent).
- HIV-1: blood-borne + sexual + vertical; began as zoonotic from
  chimps; current global pandemic with regional variation.
- SARS-CoV-2: airborne/droplet; bat reservoir likely; pandemic
  2020-present.
- Influenza A: droplet, sometimes airborne; birds + pigs as
  reservoirs (recombination); seasonal pandemics.

End with: query — "all zoonotic infections" (animal-reservoir).
How does the zoonotic origin shape control strategies (vaccination
of animals; reducing wildlife contact; surveillance)?
```

---

**What this produces:** Epidemiology fields populated. Database becomes useful for public-health reasoning.

**Connection to previous chapters:** Ch 11 (HGT explains how new pathogens emerge) + Ch 15 (virulence) + Ch 16 (transmission + reservoir) describe each pathogen's "outbreak signature."

**Preview of next chapter:** Chapter 17 covers innate immunity. Adds immune-evasion fields (how each microbe evades innate defenses).


---

## AI Wayback Machine

**Florence Nightingale** was reformed military hospitals using meticulous statistical analysis of preventable infectious deaths — and invented data visualization to make the case.

**Run this:**

```
Who is Florence Nightingale, and how does their work connect to disease and epidemiology we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Florence Nightingale"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Florence Nightingale's ideas to a contemporary microbiology problem.
- Add a constraint: "Answer including criticisms or limits of Florence Nightingale's framework."

What changes? What gets better? What gets worse?
