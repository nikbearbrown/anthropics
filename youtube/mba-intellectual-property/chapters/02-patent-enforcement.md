# Chapter 2 — Patent Enforcement


## TL;DR

- In 1976, Eastman Kodak introduced an instant camera.
- The chapter moves through 1 Opening: Polaroid v. Kodak, 2 What infringement is, 3 Claim construction: the linguistic core of patent law, 4 The defenses, and related ideas.
- Read it for the main argument, the vocabulary it introduces, and the practical judgment it asks you to develop.

## 2.1 Opening: Polaroid v. Kodak

In 1976, Eastman Kodak introduced an instant camera. The PR-10 produced a photo in less than a minute, retailing for under \$40 — a direct competitor to Polaroid, which had pioneered the instant-camera category two decades earlier and held a thicket of patents on the chemistry, mechanics, and electronics that made instant photography work. Edwin Land, Polaroid's founder and the inventor behind most of those patents, watched the Kodak introduction and concluded that Kodak had infringed.

Polaroid sued. The case went to the U.S. District Court for the District of Massachusetts. The litigation spanned fourteen years. The trial alone lasted three months. The judge issued a ruling 158 pages long. The trial court found that Kodak had infringed seven Polaroid patents. The Federal Circuit Court of Appeals affirmed in 1986. Damages were assessed in a separate proceeding that ran another two years. In 1990 — fourteen years after Kodak introduced the PR-10 — Kodak was ordered to pay Polaroid approximately \$925 million, the largest patent infringement damages award in U.S. history at the time. Kodak shut down its instant-camera business permanently. The factory in Rochester that had built PR-10s was closed; the inventory was destroyed; the technology was scrapped.

The Polaroid case is unusual only in scale. The structure — a patent holder discovers an alleged infringer; the patent holder sues; the case moves through claim construction, infringement analysis, validity defenses, expert testimony, jury or judge ruling, damages assessment, and possibly appeal — is the structure of every patent enforcement action. Patent rights from Chapter 1 are paper rights until enforced. Enforcement is what makes the rights real, and the enforcement machinery is what this chapter covers.

By the end of this chapter, you should be able to:

- *Distinguish* literal infringement from infringement under the doctrine of equivalents.
- *Explain* the role of *claim construction* — what a patent's claims mean — in any infringement analysis.
- *Identify* the major defenses to patent infringement: invalidity, non-infringement, inequitable conduct, prosecution-history estoppel, exhaustion.
- *Distinguish* the two main forums for patent enforcement: federal district court and the Patent Trial and Appeal Board (PTAB).
- *Compute* the basic damages framework — reasonable royalty vs. lost profits — and recognize when injunctive relief is available.
- *Recognize* the role of *patent assertion entities* (sometimes called "patent trolls") in the modern enforcement landscape, and the policy debates surrounding them.

You walk in with the patent grant from Chapter 1. You walk out with the litigation machinery that turns the grant into protection.

## 2.2 What infringement is

Patent infringement is *making, using, offering for sale, selling, or importing* a patented invention without the patent holder's permission, during the patent's term, in the country where the patent is enforceable. The list is exhaustive — any of those acts, on a product or process within the patent's claims, infringes.

Two flavors of infringement.

*Literal infringement* — the accused product or process matches the patent's claims literally, element-for-element. Every element recited in a claim is present in the accused embodiment. This is the simpler case.

*Infringement under the doctrine of equivalents* — the accused product or process does not literally match the claims, but performs substantially the same function in substantially the same way to achieve substantially the same result. Doctrine of equivalents prevents an infringer from making trivial design changes that escape the literal claim language while preserving the inventive contribution. The doctrine is bounded by *prosecution-history estoppel* (next section): if during patent prosecution the inventor narrowed the claims to overcome a rejection, the inventor cannot later use doctrine of equivalents to recapture the surrendered scope.

A third concept: *induced infringement* and *contributory infringement*. A party who actively induces another to infringe (by, say, selling a kit explicitly designed to be assembled into a patented product) is liable as an inducer. A party who supplies a component "especially made or especially adapted for use in an infringement" with knowledge of the patent is a contributory infringer. Both extend infringement liability beyond the direct infringer to upstream parties who knowingly enabled the infringement.

The trade-off in defining infringement broadly: it buys *protection against trivial workarounds* (you can't escape a patent by changing one bolt color) at the cost of *expanding what counts as infringement and inviting litigation*. Doctrine of equivalents is the most-litigated doctrine in patent law because it is the inherently fuzzy line between "the same invention" and "a different invention."

## 2.3 Claim construction: the linguistic core of patent law

A patent's *claims* are the numbered sentences at the end of the patent document that define the invention's legal scope. The body of the patent — the description, the figures, the abstract — explains and supports the invention; the claims define what it *is*, in words. Claim construction is the legal process of determining what each word in each claim means.

This is more important than it sounds. Patent infringement turns on whether the accused product is within the claim's scope. If "fastener" in a claim means "any device for joining two surfaces," a screwed connection infringes. If "fastener" means specifically "a threaded device," a glued connection does not. The same patent claim can produce different infringement outcomes depending on how the words are construed.

Claim construction is a question of law decided by the judge, not the jury. The Supreme Court's 1996 *Markman v. Westview Instruments* decision established this rule, and the *Markman hearing* — a pre-trial proceeding where the judge construes disputed claim terms — is now standard in every patent case. The judge's construction governs the rest of the litigation.

Three sources inform claim construction:

*Intrinsic evidence* — the patent itself: the claims, the specification (the body of the patent describing the invention), and the prosecution history (the back-and-forth between the patent applicant and the USPTO during examination). Intrinsic evidence is paramount; courts give it the most weight.

*Extrinsic evidence* — dictionaries, technical treatises, expert testimony. Used to fill gaps when intrinsic evidence is ambiguous. Courts use extrinsic evidence cautiously; it is "secondary" to the intrinsic record.

*The "person having ordinary skill in the art"* (PHOSITA) — claim terms are construed as that hypothetical reader would understand them. Not a layperson; not an expert. The skilled-but-not-extraordinary engineer or scientist in the relevant field at the time of the invention.

The trade-off in claim construction: the formality buys *predictability* (a construed claim has a definite meaning the rest of the litigation operates against) at the cost of *front-loading the dispute* (claim construction is often the most consequential ruling in a patent case, with everything that follows largely determined by it). Skilled patent litigators know that the Markman hearing is often where the case is won or lost.

## 2.4 The defenses

Even when a patent is plausibly infringed, the accused infringer has several defenses available.

*Invalidity*. The accused infringer challenges the patent's validity — argues it should never have issued. Most common grounds: lack of novelty (the invention was anticipated by prior art the USPTO missed), obviousness (the invention was obvious in light of prior art), inadequate disclosure (the patent fails to enable a skilled artisan to practice the invention), indefiniteness (the claims are too vague to be construed). Invalidity is determined by the same patentability requirements from Chapter 1 §1.5; the difference is that the burden is on the challenger to prove invalidity by clear and convincing evidence (a higher bar than the preponderance-of-evidence standard for most civil litigation).

*Non-infringement*. The accused infringer argues that even taking the claims as written and construed, the accused product or process does not infringe. The most common form: the accused product lacks one of the elements recited in the claim (since claims are read element-by-element, and an accused product missing any element does not infringe). Non-infringement and invalidity are independent defenses — both can succeed, both can fail, or one can succeed while the other fails.

*Inequitable conduct*. If the patent applicant deliberately misled the USPTO during prosecution (concealing prior art, misrepresenting test results, etc.), the entire patent can be rendered unenforceable. The Federal Circuit's 2011 *Therasense v. Becton Dickinson* decision substantially raised the bar for proving inequitable conduct — both materiality of the misrepresentation and intent to deceive must be proved by clear and convincing evidence. This made inequitable conduct a less common defense than it had been in the 1990s and 2000s.

*Prosecution-history estoppel*. If during prosecution the inventor surrendered claim scope to overcome a USPTO rejection, the inventor cannot later use doctrine of equivalents to recapture the surrendered scope. This bounds the doctrine of equivalents discussed in §2.2.

*Patent exhaustion*. Once the patent holder has authorized the sale of a patented item, the patent rights in that particular item are *exhausted* — the buyer can use, resell, or modify it without further permission from the patent holder. The 2017 Supreme Court decision *Impression Products v. Lexmark International* applied this even to international sales.

*Inequitable enforcement*. Misuse of the patent — for example, using a patent to control unpatented goods through tying arrangements — can render the patent temporarily unenforceable until the misuse is purged.

The trade-off in this menu of defenses: the multiplicity of defenses makes patent litigation longer and more complex, but it also serves as a check on patents that should never have issued or are being asserted improperly. A patent that survives a thorough invalidity challenge is more credible than one that has never been tested.

## 2.5 The forums: federal court and PTAB

Two main forums hear patent disputes.

*U.S. district court*. Patent litigation falls under federal jurisdiction (28 U.S.C. § 1338). The patent owner files in a district court of proper venue; the case proceeds through pleadings, discovery, claim construction (Markman), summary judgment motions, trial (jury or bench), and post-trial motions. Appeals from district court go to the *Court of Appeals for the Federal Circuit* (CAFC), a specialized appellate court created in 1982 specifically to hear patent appeals nationwide. The CAFC's centralization was intended to bring uniformity to patent law that the prior system of regional appellate courts had failed to deliver.

*Patent Trial and Appeal Board (PTAB)*. Created by the 2011 America Invents Act, the PTAB is a USPTO administrative tribunal that hears patent validity challenges in three formats:

- *Inter partes review (IPR)* — a third party challenges patent validity on novelty or obviousness grounds, based on prior art consisting of patents and printed publications. Most common PTAB proceeding.
- *Post-grant review (PGR)* — broader validity challenge available in the first nine months after a patent issues; can be based on any invalidity ground.
- *Covered business method (CBM) review* — narrower proceedings for business-method patents, sunset in 2020.

The PTAB has become a major venue for patent challengers. It is faster than district court (typical 12-18 months vs. 2-3+ years for district court), uses a lower burden of proof for invalidity (preponderance vs. clear-and-convincing), and uses a specialized panel of administrative patent judges rather than a generalist district judge.

The trade-off in this two-forum system: it buys *specialized validity adjudication* at the cost of *parallel proceedings on the same patent*. A defendant in district court can file a parallel PTAB challenge to invalidate the asserted patent; the district court may stay its proceeding pending the PTAB outcome, or proceed in parallel. Strategic considerations about which forum to use, when to file, and how to coordinate (or not) parallel proceedings is much of what modern patent litigators do.

## 2.6 Damages and injunctive relief

Two categories of remedies for infringement.

*Damages* — money paid to the patent holder. 35 U.S.C. § 284 sets the floor: damages "shall be" no less than a "reasonable royalty" — what a willing licensor and willing licensee would have negotiated at the hypothetical pre-infringement bargaining table.

In practice, two damages theories are common.

*Lost profits*. The patent holder argues that without the infringement, the patent holder would have made the sales the infringer made, at the patent holder's profit margin. Lost profits require proving (a) demand for the patented product, (b) absence of acceptable non-infringing alternatives, (c) the patent holder's manufacturing and marketing capacity to make the additional sales, and (d) the amount of profit the patent holder would have made. The four-factor test from *Panduit Corp. v. Stahlin Bros. Fibre Works* (1978) governs.

*Reasonable royalty*. The patent holder argues for the royalty rate the parties would have agreed on. The court considers factors from *Georgia-Pacific Corp. v. United States Plywood Corp.* (1970) — fifteen factors, including the royalties the patent holder receives from other licensees, the royalty rate paid for comparable patents, the nature and scope of the license, established profitability of the product, and so on.

The Polaroid award in §2.1 — \$925 million — was primarily lost profits, on the theory that Polaroid would have made the sales Kodak made at Polaroid's profit margin. In other cases, where the patent holder is not in a position to manufacture (a university, a research lab, a non-practicing entity), the reasonable royalty theory is the only available one.

*Injunctive relief* — a court order forbidding future infringement. Historically, an injunction was nearly automatic upon finding of infringement. The Supreme Court's 2006 *eBay v. MercExchange* decision changed this: a four-factor test now applies, and injunctions are granted only when (i) the patent holder will suffer irreparable harm without an injunction, (ii) damages are inadequate, (iii) the balance of hardships favors injunction, and (iv) the public interest is not disserved.

The *eBay* decision was particularly consequential for non-practicing entities, who often could not show irreparable harm because they did not produce products that could be displaced by infringement. Post-*eBay*, NPEs typically receive damages but not injunctions; practicing entities — companies that compete with the infringer — more often get both.

## 2.7 Patent assertion entities and the policy debate

A *patent assertion entity* (PAE), sometimes called a "non-practicing entity" (NPE) or "patent troll," is a company whose business is enforcing patents rather than producing the products those patents cover. Some PAEs have legitimate origins — universities, individual inventors, failed startups whose patents survived the company. Others were specifically created to acquire patents for litigation; some are *patent assertion entities* in the narrower sense, structured around litigation as the primary revenue model.

The policy debate is sharp.

*Arguments against PAEs*. They impose costs on operating companies (defense costs, license fees) without making the products their patents cover. They often assert weak patents — patents that would not survive challenge but that companies pay nuisance settlements to avoid the cost of litigation. They congregate in plaintiff-friendly venues (the Eastern District of Texas was historically the dominant patent-litigation venue, until the 2017 *TC Heartland* decision tightened venue rules). They distort innovation incentives by taxing companies that did invent without creating new inventions themselves.

*Arguments for PAEs*. They give individual inventors and small companies a way to monetize patents they cannot themselves commercialize. They are functionally a market for patent rights — the patent law equivalent of any other secondary market. The "troll" pejorative obscures the legitimate role of patent licensing as a business model. The remedies for abusive patent litigation lie in patent quality (better USPTO examination), litigation reform (fee-shifting for frivolous cases, pleading standards), and venue rules — not in restricting patent transferability per se.

The 2011 AIA, the 2014 Supreme Court *Alice Corp. v. CLS Bank* decision (which restricted abstract-idea patents), the 2017 *TC Heartland* venue tightening, and the rise of the PTAB have together substantially reduced the impact of PAE litigation in the late 2010s. The structural debate about how to design a system that serves legitimate inventors without enabling abusive enforcement continues.

## 2.8 Synthesis: the Polaroid case, fully

Return to *Polaroid v. Kodak*. Apply the chapter's full machinery.

*Infringement*. Polaroid asserted seven patents. Kodak's PR-10 was alleged to literally infringe several and to infringe under the doctrine of equivalents on others. The trial court found infringement on multiple counts.

*Claim construction*. The 158-page trial-court opinion devoted substantial pages to construing terms from Polaroid's patents. The construction favored Polaroid on most disputed terms.

*Defenses*. Kodak argued invalidity (asserting prior art that should have anticipated Polaroid's claims) and non-infringement. The trial court rejected most of Kodak's invalidity arguments and most of its non-infringement arguments. The Federal Circuit affirmed.

*Forum*. The case was litigated in district court (D. Mass.). The PTAB did not yet exist (this was 1976-1990, before the AIA created the PTAB in 2011). Validity challenges had to go through the courts.

*Damages*. The \$925 million was primarily lost profits — Polaroid argued, and the court agreed, that without Kodak's infringement Polaroid would have made the instant-camera sales Kodak made. Polaroid's profit margin times Kodak's sales volume produced the bulk of the award.

*Injunction*. Kodak was enjoined from making, using, or selling the infringing PR-10. The injunction was the reason Kodak shut down its instant-camera business permanently. Post-*eBay* (2006), this injunction would still likely have issued because Polaroid was a practicing entity that competed directly with Kodak in instant cameras — irreparable harm was clear, damages alone could not address ongoing competition.

The case is a textbook example of patent enforcement working as designed: a patent holder with a genuine invention, a clear infringer, a thorough adjudication of validity and infringement, substantial damages, and injunctive relief that ended the infringement. It is also unusual in scale and consequence; most patent cases settle long before judgment, with terms that aren't disclosed publicly. The Polaroid case is what patent litigation looks like when it goes the distance.

## 2.9 Exercises

### Warm-up

1. **Define patent infringement** in one sentence, and identify the five infringing acts the statute names.

2. **Distinguish literal infringement from infringement under the doctrine of equivalents.**

3. **Why is claim construction a question of law decided by the judge** rather than a question of fact for the jury?

### Application

4. **An accused product is identical to the patented invention except that one element of the patented claim — say, "a steel bolt" — is replaced with a polymer fastener.** Discuss whether literal infringement applies, whether doctrine of equivalents might apply, and what factors bear on the latter analysis.

5. **A defendant in a patent suit has two independent defenses available: invalidity and non-infringement.** Discuss why a smart defendant typically pursues both.

6. **A patent holder is a university research lab that does not manufacture products.** Discuss what damages theory is available, and what the *eBay* factors say about whether injunctive relief is likely.

### Synthesis

7. **An accused infringer files an inter partes review at the PTAB and is also sued in district court on the same patent.** Discuss the strategic considerations for both parties: when is it advantageous to stay the district court case pending PTAB; when is it not?

8. **A small inventor files a patent and prosecutes it pro se (without a lawyer), submitting an amendment that narrows the claim during prosecution.** Discuss how prosecution-history estoppel might affect later doctrine-of-equivalents arguments if the inventor sues for infringement.

### Challenge

9. **Some commentators argue that PAE litigation is a tax on innovation; others argue that PAEs are a legitimate market for patent rights.** Construct the strongest argument on each side, drawing only on this chapter's framework. Which structural changes (better patent quality, litigation reform, venue rules) most directly address the worst PAE-related abuses without restricting legitimate licensing?

10. **The 2006 *eBay* decision changed injunctive relief from nearly automatic to discretionary, applying a four-factor test.** Discuss how this decision reshaped the PAE business model. Specifically, why are post-*eBay* PAE suits more likely to result in damages than in injunctions, and how does that change settlement dynamics?

## 2.10 Chapter summary

You walked into this chapter with the patent grant. You walk out with the enforcement machinery that turns the grant into protection.

Patent infringement is making, using, selling, offering for sale, or importing a patented invention without permission, during the term, in the country of enforcement. It comes in literal and doctrine-of-equivalents forms; induced and contributory infringement extend liability to enablers.

Claim construction — determining what the words of the claims mean — is a judge-decided legal question that often determines the outcome of a patent case before any infringement analysis happens. The *Markman* hearing is the procedural device.

Defenses include invalidity, non-infringement, inequitable conduct, prosecution-history estoppel, and patent exhaustion. Each is a distinct ground; multiple defenses can be raised in parallel.

Two forums hear patent disputes: federal district court (with appeals to the Federal Circuit) and the PTAB (an administrative tribunal at the USPTO created by the 2011 AIA). Strategic choice between them, and coordination of parallel proceedings, is a major feature of modern patent litigation.

Damages are computed under either lost-profits or reasonable-royalty theories. Injunctive relief, formerly automatic, became discretionary under the 2006 *eBay* decision. The interaction of these remedies with the rise of PAE litigation has reshaped patent enforcement policy in the past two decades.

The single most important idea: patent rights are paper rights until enforced, and enforcement is expensive, slow, and uncertain. The Polaroid case took fourteen years and produced the largest patent damages award of its time. Most patent cases settle for far less than the patent's nominal value would suggest, because both sides recognize the cost and risk of litigation. Patent strategy is as much about the credible threat of enforcement as about actual enforcement.

The common mistake to watch for: assuming that "having a patent" is the same as "being able to stop infringement." It is not. Enforcement requires litigation, which requires money and time and a willingness to accept uncertain outcomes. Patents that the holder cannot or will not enforce are functionally weaker than their nominal scope suggests.

## 2.11 Connections forward

Chapter 3 turns from patents to *copyright* — the parallel intellectual property regime that protects creative expression rather than functional inventions. Books, music, software code, films, paintings, photographs are all copyright subjects. The bargain-and-disclosure logic from Chapter 1 doesn't apply in the same way: copyright protection is automatic on creation, lasts for the author's life plus 70 years (usually), and protects expression rather than ideas. Chapter 3 develops the copyright framework and meets the major doctrines — fair use, work-made-for-hire, the DMCA — that govern its application.
---

## LLM Exercise — Chapter 2: Patent Enforcement (IP Strategy for a Startup Project)

**Project:** Build the complete IP-protection strategy for your fictional startup.
**What you're building this chapter:** the patent enforcement plan — what you do when a competitor copies your patented feature.
**Tool:** **Claude Project** (same project as Ch 1 — references your invention spec and claims).

---

**The Prompt:**

```
Chapter 2 of my startup IP-strategy project. Chapter 2 covered:
infringement (literal vs. doctrine of equivalents); claim
construction (Markman 1996 — judges, not juries, decide what
the words mean); the defenses (invalidity, unenforceability,
non-infringement); federal court vs. PTAB; damages (lost
profits vs. reasonable royalty); injunctions after eBay (2006);
patent assertion entities and the policy debate.

Now: a competitor launched a product 18 months after my patent
issued. The competitor's product has a feature that looks like
my Claim 1. Walk through the enforcement analysis.

1. **Infringement analysis on Claim 1.** Take Claim 1 from the
   Ch 1 work. Imagine the competitor's product (define it
   plausibly — similar mechanism but with at least one
   element-language difference from my claim). Run the
   element-by-element analysis:
   - Does every element of Claim 1 read on the competitor's
     product?
   - If one element is missing, is it equivalent under the
     doctrine of equivalents (function-way-result test)?
   - What's my strongest infringement argument?

2. **Claim construction battle.** Identify the 2-3 claim terms
   the competitor will try to construe narrowly to avoid
   infringement. For each:
   - What does the specification say about that term?
   - What does the prosecution history say (file wrapper estoppel)?
   - What's my best argument for a broader construction; what's
     theirs for a narrower one?

3. **The defenses I should expect.**
   - Invalidity by anticipation (102): is there prior art that
     could anticipate?
   - Invalidity by obviousness (103): the KSR multi-reference
     combination attack.
   - Inequitable conduct (Therasense 2011 standard).
   - Non-infringement.
   Charitably reconstruct the competitor's strongest defense.

4. **Forum choice.**
   - Federal district court (where? TC Heartland 2017 limited
     venue to defendant's place of incorporation or where it
     has a regular and established place of business).
   - ITC (if there are imports — fast, no damages, but
     exclusion order).
   - PTAB IPR (cheaper invalidity attack, but the competitor
     might file this against me — adversarially).
   - Pick a forum and defend the choice for my situation.

5. **Damages model.**
   - Lost profits (Panduit factors): can I show I would have
     made the sales the competitor made?
   - Reasonable royalty (Georgia-Pacific factors): hypothetical
     negotiation at the time of first infringement.
   - Which is bigger for my startup? Which is easier to prove?

6. **Injunction analysis (eBay 4-factor).**
   - Irreparable harm — am I a practicing entity competing for
     the same customers?
   - Adequate remedy at law — would damages be enough?
   - Balance of hardships.
   - Public interest.
   - Realistic? Or settle for damages?

End with the **Enforcement Memo** (300 words): file in [forum],
seek [remedy], expected litigation cost vs. expected recovery,
settlement value, and the one fact pattern that would change
my mind about pursuing this case.
```

---

**What this produces:** A complete enforcement strategy memo for your specific patent. The Markman analysis is the linguistic heart of patent enforcement — most cases turn on what 2-3 words mean. The eBay analysis is the realistic injunction check that killed the assumption that patentees automatically get injunctions.

**Adaptation notes:** A solo founder with a shoestring legal budget rarely litigates patents in federal court — typical patent litigation runs $3-7M through trial. The honest enforcement plan for a startup often involves licensing demands, ITC actions (if imports), or settling for a royalty rather than seeking an injunction.

**Connection to previous chapters:** Direct — uses the invention spec and Claim 1 from Ch 1.

**Preview of next chapter:** Chapter 3 — copyright. Your startup has software, marketing materials, manuals, packaging copy, training videos. What's protected, what's not, what's the registration plan, where does fair use cut for or against you?


---

##  AI Wayback Machine
**Edwin Land** was Polaroid founder whose patent enforcement strategy against Kodak (after Kodak infringed instant-photography patents) became a textbook case in patent litigation.

![Edwin Land](../images/edwin-land-7se.png)

*Puppet Art by [Nik Bear Brown](https://www.nikbearbrown.com/).*

**Run this:**

```
Who is Edwin Land, and how does their work connect to patent enforcement we covered in this chapter? Keep it to three paragraphs. End with the single most surprising thing about their career or ideas.
```

→ Search **"Edwin Land"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to apply Edwin Land's framework to a specific IP question.
- Add a constraint: "Answer including criticisms or limits of Edwin Land's framework."

What changes? What gets better? What gets worse?
