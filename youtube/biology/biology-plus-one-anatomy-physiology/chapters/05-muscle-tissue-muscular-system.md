# Chapter 05 — Muscle Tissue and the Muscular System

*What a dead man's locked arm can teach you about every movement you will ever make.*

---

## Learning objectives

By the end of this chapter, you should be able to:

1. **Describe** the nested anatomy of skeletal muscle from whole muscle to sarcomere and **identify** the bands of a sarcomere by what is changing inside them.
2. **Trace** the cross-bridge cycle step by step and **predict** what happens when ATP, calcium, or acetylcholine is missing.
3. **Explain** excitation-contraction coupling — the chain from a motor neuron firing to thin filaments sliding — and **locate** where each step physically happens in the muscle fiber.
4. **Apply** the size principle to predict which motor units fire when you lift a teacup versus a couch, and **predict** the force output of a fiber given a stimulation frequency (twitch, summation, tetanus).
5. **Distinguish** Type I, Type IIa, and Type IIx fibers by their energy strategy and **predict** which fiber type dominates a given athletic task.
6. **Compare** skeletal, cardiac, and smooth muscle by control signal, action potential duration, and calcium source — and **explain** why the heart cannot be tetanized.
7. **Build and run** a sliding filament simulator and **interpret** its force-time output against the underlying calcium and ATP availability.

Prerequisites: Chapter 2 (membrane transport, ATP, ion channels); Chapter 3 (muscle tissue overview); Chapter 4 (origins, insertions, leverage).

---

## The locked arm

A retired pathologist in a teaching hospital invites a medical student into the autopsy suite. On the table is a man in his sixties, six hours dead. The pathologist asks the student to lift the man's right arm. The student takes the wrist and pulls. The arm does not move. It resists him as though the dead man is straining against it.

The pathologist nods. *That is rigor mortis. Before we cut, tell me what is holding his arm down. Not the tendons. Not the joints. What, at the molecular level, is locking this man's muscles in place?*

Sit with that question. The man is dead. No nerve is firing. No calcium is being released on cue. Every active process has ended. And yet his muscles are clamped hard enough that two people struggle to move a limb. Something is gripping. Something is refusing to let go.

That something is the cross-bridge between myosin and actin — the molecular handshake that produces every contraction your body will ever make. In a living person, the handshake breaks every few milliseconds, when ATP arrives, binds the myosin head, and pries it loose. In a corpse, ATP production has stopped. The handshake never breaks. The grip persists until the proteins themselves begin to decay, twelve to thirty-six hours later.

Now run the clock the other way. A few hours earlier the same man might have been lifting a cup of coffee. The same molecular machinery, the same handshake — but now it is being made and broken twenty times per second per myosin head, hundreds of millions of heads at once, gated by a calcium signal that arrives milliseconds after his motor cortex decides to lift. The difference between life and rigor is not the mechanism. The mechanism is identical. The difference is the energy and the signal.

This chapter is about that mechanism — what it is, how it is controlled, how it is amplified from a few nanometers per myosin head into the visible motion of a body, and how the same engine is repurposed for the heart and the gut. By the end, when you watch someone walk across a room, you should see roughly a hundred trillion myosin heads, all rowing.

<!-- → [IMAGE: single myosin head in the rigor state — bound to actin, no ATP present — labeled to show the head gripping actin tightly, the thick filament it is anchored to, and the thin filament it is holding. A second panel shows the same head with ATP bound, beginning to detach. Caption: "rigor mortis in two frames: left panel is every myosin head in a corpse; right panel is the first millisecond of the cycle restarting when ATP arrives."] -->

---

## The anatomical zoom

Before we touch the chemistry, we need to know where it happens. The first thing to understand about muscle is that the word does different jobs at different scales. The biceps you see in a mirror is a muscle. So is each rope-like bundle inside it. So is each cell within those bundles. So is each thread inside each cell. Force is generated at the smallest scale and transmitted upward through every larger scale, like a tug-of-war team where every individual is also pulling on a smaller team behind them.

A **whole muscle** — biceps brachii, gastrocnemius, rectus abdominis — is wrapped in a tough sheath called the **epimysium**, which blends into the tendon at each end and transmits force to bone.

Inside the epimysium, the muscle divides into bundles called **fascicles**, each wrapped in **perimysium**. The visible grain in a cut of cooked meat — the dark threads between lighter strands — is perimysium between fascicles.

Inside each fascicle are **muscle fibers** — single cells, sometimes thirty centimeters long, packed with hundreds of nuclei. Each fiber is wrapped in **endomysium** and bounded by a cell membrane called the **sarcolemma** (sarco-, flesh). The "sarc-" prefix will keep appearing; it always means muscle.

Inside each fiber are cylindrical bundles called **myofibrils**, running the fiber's full length. Around them sits the cell's calcium reservoir, the **sarcoplasmic reticulum**, with tubes called **T-tubules** tunneling inward from the sarcolemma.

Each myofibril divides lengthwise into repeating units called **sarcomeres**. The sarcomere is the contractile unit. It is where chemistry becomes motion. Everything outside it exists to feed it, signal to it, hold it in place, or carry its force outward.

<!-- → [DIAGRAM: nested zoom — whole muscle (epimysium) → fascicles (perimysium) → muscle fibers (endomysium, sarcolemma) → myofibrils → sarcomeres. Each level labeled with its connective tissue wrapping. Arrows show how force generated at the sarcomere is transmitted outward through each layer to the tendon. Caption: "force is made at the smallest scale and passed outward; the connective tissue layers are the rigging that turns molecular work into bone motion."] -->

Now zoom into one sarcomere. Under a light microscope, skeletal and cardiac muscle look striped because adjacent myofibrils' sarcomeres line up, and the internal structure alternates dense and light regions — *striated* muscle. The stripes are not decoration. They are the readout of the machinery.

A sarcomere is bounded at each end by a **Z disc**. Two Z discs define one sarcomere — about two micrometers at rest. Anchored at each Z disc and pointing inward are **thin filaments**: actin polymers coated with **tropomyosin** (a rope-like protein lying along the actin chain) and **troponin** (a small regulatory complex attached to tropomyosin at intervals). In the middle, suspended between the inward thin filaments, are **thick filaments** made of **myosin** — a large protein with two heads on long flexible necks, several hundred per filament. The heads are the engines.

Learn the bands. They are how the field talks about what is happening inside the sarcomere.

The **A band** is the full length of the thick filament, including its overlap with thin filaments at each end. Dark. *Anisotropic* — hence A. The A band does not change length when the muscle contracts. That single fact is the key to everything.

The **I band** is the region containing only thin filaments — no thick filament. Light. *Isotropic* — hence I. It contains the Z disc at its center.

The **H zone** is the central part of the A band where only thick filaments exist — no thin filament overlap yet.

The **M line** is the dark cross-link at the center of the H zone where thick filaments are anchored to each other.

<!-- → [DIAGRAM: a single sarcomere at rest, with Z discs at each end, thin filaments extending inward from each Z, thick filaments in the middle with M line, and labeled bands — A band (full thick filament length), I band (thin-only region flanking the Z disc), H zone (center, thick only). Second sarcomere beside it in contraction: Z discs closer, I band shrunken, H zone shrunken, A band unchanged. Caption: "the bands tell you what is happening. A band constant means thick filament length constant. I and H shrinking means overlap is increasing — the filaments are sliding past each other, not getting shorter."] -->

When a muscle contracts, the thick filaments do not shorten. The thin filaments do not shorten. **The filaments slide past each other.** Thin filaments are pulled inward toward the M line, dragging the Z discs with them. The sarcomere shortens. The A band stays the same length — the thick filament has not changed. The I band shrinks — the thin filaments are being pulled into the thick-filament zone, reducing the thin-only region. The H zone shrinks — thin filaments now invade what was thick-only territory. Stretch the muscle and the I and H zones widen; the A band still does not change.

This is the **sliding filament theory**, proposed in two back-to-back 1954 papers in *Nature* — by Hugh Huxley and Jean Hanson, and independently by Andrew Huxley and Rolf Niedergerke ([Huxley & Hanson 1954](https://www.nature.com/articles/173973a0); [Huxley & Niedergerke 1954](https://www.nature.com/articles/173971a0)). They settled a sixty-year argument. The filaments slide. They do not contract.

That leaves the question of *what* slides them.

---

## The cross-bridge cycle

The myosin head is a molecular machine that does five things in sequence, repeatedly, as long as it has fuel. The fuel is ATP. A **cross-bridge** is the physical connection formed when a myosin head binds an actin site. The **cross-bridge cycle** is the sequence from one binding to the next. Here is one head completing one stroke — in a real fiber, hundreds of millions are doing this asynchronously.

**Step 1 — ATP binds; the head releases.** The head begins bound to actin (the rigor state from the previous cycle). ATP arrives and binds. This immediately weakens the head's grip. The head detaches.

**Step 2 — ATP is hydrolyzed; the head is cocked.** Myosin is its own ATPase — it splits the bound ATP into ADP and inorganic phosphate (Pi). The energy released drives a conformational change: the head pivots into a high-energy cocked position, like a spring being wound. ADP and Pi remain bound. The head is ready to grab forward — but only if a binding site on actin is available.

**Step 3 — The cocked head binds a new actin site.** If calcium has uncovered the binding sites (we will explain that gate next), the cocked head latches onto an actin site farther toward the Z disc than its previous binding site.

**Step 4 — The power stroke.** Pi is released, then ADP. As Pi leaves, the head pivots — pulling the thin filament about ten nanometers toward the M line. This is the power stroke. This is where force is produced.

**Step 5 — Rigor state.** With ADP and Pi gone, the head grips actin tightly in the rigor state. It stays there until the next ATP arrives and the cycle begins again.

<!-- → [DIAGRAM: five-frame loop of the cross-bridge cycle. Frame 1: head bound to actin (rigor); ATP arrives. Frame 2: head detached, ATP bound. Frame 3: head cocked, ADP+Pi bound, reaches forward. Frame 4: head binds new actin site; Pi released. Frame 5: power stroke, ADP released, thin filament pulled ~10 nm toward M line. Arrows return to Frame 1. Caption: "ATP binding releases the head. ATP hydrolysis cocks the head. Phosphate release fires the stroke. ADP release locks the grip. Each step is a shape change; together they are a ratchet walking the thin filament toward the center."] -->

Two things to understand about where in the cycle each event happens.

ATP is consumed at Step 2 — the hydrolysis that cocks the head. Force is produced at Step 4 — the power stroke. These are not the same step. The chemical event that costs energy happens *before* the mechanical event that produces force. The energy of ATP hydrolysis is stored in the spring of the cocked head and released later, when calcium opens the gate. Cause and effect are separated by time, by a conformational intermediate that holds the energy until it is needed.

The cycle has one failure mode that defines rigor mortis. If ATP runs out at Step 5, the head cannot detach. It sits on actin, locked, waiting for an ATP that never comes. Multiply this across every myosin head in every muscle, and the entire body stiffens. Rigor is not a contraction — it is a failure to relax, because relaxation requires ATP, and there is none left.

---

## Excitation-contraction coupling

The cross-bridge cycle is the engine. But the engine has a gate, and the gate is calcium. The chain from a thought in your motor cortex to thin filaments sliding in your biceps is called **excitation-contraction coupling** — EC coupling. Here is that chain, each link at a specific place.

**Link 1 — Motor neuron action potential.** A motor neuron's cell body sits in the spinal cord or brainstem. When it fires, an action potential travels down its axon to the terminal sitting on a muscle fiber.

**Link 2 — Acetylcholine release at the neuromuscular junction.** At the **neuromuscular junction** (NMJ), the action potential opens voltage-gated calcium channels in the axon terminal. Calcium flows in. Synaptic vesicles release **acetylcholine** (ACh) into the narrow synaptic cleft.

**Link 3 — Muscle fiber depolarization.** ACh binds nicotinic acetylcholine receptors on the sarcolemma — ligand-gated channels that open and admit sodium. The local depolarization triggers voltage-gated sodium channels, propagating an action potential along the sarcolemma in both directions.

**Link 4 — Action potential down the T-tubules.** The action potential reaches the **T-tubules** — deep infoldings of the sarcolemma that tunnel into the fiber's interior at every Z disc. T-tubules exist because the fiber is too large for a surface electrical signal to penetrate fast enough. They are the antennae that carry the action potential inward so every sarcomere is signaled simultaneously.

**Link 5 — Calcium released from the sarcoplasmic reticulum.** The terminal cisternae of the SR flank each T-tubule; one T-tubule and its two flanking cisternae form a **triad**. Voltage-sensing proteins in the T-tubule membrane (dihydropyridine receptors, DHPR) are physically coupled to calcium-release channels in the SR membrane (ryanodine receptors, RyR). When the action potential changes the T-tubule voltage, the DHPRs mechanically pull open the RyRs. Calcium floods out of the SR into the cytosol. Concentration around the myofibrils jumps roughly a hundredfold in milliseconds.

**Link 6 — Calcium binds troponin; actin sites exposed.** Each troponin complex has a calcium-binding subunit (troponin C). When calcium binds, troponin changes shape and moves the attached tropomyosin sideways along the actin chain, uncovering the myosin-binding sites that tropomyosin had been blocking at rest.

**Link 7 — Cross-bridge cycling.** With sites exposed and ATP available, myosin heads grab and pull. Cycling continues as long as both calcium and ATP are present.

**Link 8 — Relaxation.** When the motor neuron stops firing, ACh release stops; residual ACh is cleaved by acetylcholinesterase. The SR's SERCA pumps (sarcoendoplasmic reticulum calcium ATPase) pull calcium back into the SR, using ATP. Cytosolic calcium falls. Troponin releases calcium, tropomyosin slides back, sites are covered. Cross-bridges that complete their stroke and release cannot re-form. The fiber relaxes.

<!-- → [DIAGRAM: linear flow of EC coupling — motor neuron AP → ACh at NMJ → muscle AP → T-tubule AP → DHPR/RyR coupling → Ca²⁺ release from SR → Ca²⁺ binds troponin → tropomyosin moves → cross-bridge cycling. Each step labeled with location: "at the NMJ," "in the sarcolemma," "at the triad," "on the thin filament." Caption: "every step is a physical event at a specific place. Break any link and contraction fails — and which link is broken determines what the disease looks like."] -->

Notice that every link is a disease. Curare blocks the nicotinic receptors at Link 3. Myasthenia gravis destroys those same receptors by autoimmune attack. Botulinum toxin blocks ACh release at Link 2. Tetanus toxin disinhibits motor neurons upstream of Link 1, causing sustained firing. Malignant hyperthermia is a genetic defect in ryanodine receptors at Link 5 that causes uncontrolled calcium release under volatile anesthetics. The clinical picture of each disease is the signature of the link it breaks.

<!-- → [TABLE: EC coupling disease map — columns: disease/drug, EC coupling link broken, molecular mechanism, direction of failure (flaccid vs. rigid vs. other), clinical presentation. Rows: botulinum toxin (Link 2), curare (Link 3), myasthenia gravis (Link 3), succinylcholine (Link 3), malignant hyperthermia (Link 5), tetanus toxin (upstream of Link 1). Caption: "the same chain, broken in different places. The direction of failure — toward paralysis or toward spasm — tells you where in the chain the break is."] -->

Relaxation is not free. SERCA pumps cost ATP — roughly as much as the contraction itself. Holding a heavy bag at arm's length while standing still is genuinely tiring not because you are visibly moving but because every micro-relaxation is being paid for by SERCA, continuously.

---

## Motor units and graded force

A single muscle fiber follows the **all-or-nothing principle**: it either fires a full action potential and produces a maximal twitch, or it fires nothing. There is no half-fire. So how does the same biceps lift a teacup and a couch?

The answer is the **motor unit** — one motor neuron plus all the muscle fibers it innervates. A small motor unit might be one neuron and ten fibers. A large unit might be one neuron and a thousand. When the neuron fires, every fiber in its unit contracts together. The motor unit is the smallest functional package the nervous system can address.

Fine-control muscles have very small motor units. The muscles that move your eyes have units of just a handful of fibers — that is why you can fixate on a single letter and adjust by tenths of a degree. Gastrocnemius motor units can contain a thousand fibers, because gastrocnemius launches the body upward, not threads a needle.

The nervous system grades force two ways. First, **recruitment** — firing more motor units. Second, **wave summation** — firing the active units more frequently.

Recruitment follows the **size principle**, identified by Elwood Henneman and colleagues in the 1960s. Small motor units have small motor neurons that are easy to depolarize; large units require stronger drive. As demanded force increases, small units fire first — they tend to be fatigue-resistant Type I fibers. Larger, more powerful, more fatigable units come in at higher drive levels. Maximum effort recruits everything.

Wave summation works through calcium. A single motor unit firing once produces a **twitch** — a brief rise and fall in tension over about a hundred milliseconds. If the unit fires again before relaxation is complete, the second twitch builds on top of the first: the unit develops more tension than a single twitch could produce. This stacking is **wave summation**. If you keep firing faster than the fiber can fully relax, twitches fuse into a smooth, sustained, high-tension contraction called **tetanus** — here, physiological tetanus, sustained contraction, not the disease, although the disease is named for it because it produces exactly this.

<!-- → [CHART: force-time output of one motor unit at three stimulation frequencies. Top panel: single twitches at low frequency, complete relaxation between each. Middle panel: unfused tetanus at moderate frequency, peaks and partial relaxations stacking upward. Bottom panel: fused tetanus at high frequency, smooth plateau of high tension. Caption: "the same fiber, the same machinery. What changed is how soon the next action potential arrives — too soon for the calcium to be pumped back, so it accumulates and contraction sustains."] -->

The mechanism lives in the calcium pump. Between twitches, SERCA is pumping calcium back into the SR. If the next action potential arrives before SERCA clears the calcium, cytosolic calcium accumulates rather than declining, more troponin stays activated, more cross-bridges form, more tension develops. Tetanus is the steady state where calcium release outruns SERCA. So when you contract a muscle smoothly and strongly, your nervous system is doing two things simultaneously: recruiting the right motor units and firing them fast enough that each is in tetanus. The result is a graded, smooth, controllable force output — even though every individual fiber is following all-or-nothing rules.

---

## Fiber types

Not all skeletal muscle fibers are the same. Three types coexist in nearly every muscle, in proportions that depend on the muscle's job, on genetics, and on training. The classification rests on two things: how fast the fiber contracts (which depends on how quickly the myosin ATPase can split ATP) and how the fiber generates ATP.

**Type I — slow oxidative.** Slow myosin ATPase. ATP from oxidative phosphorylation in mitochondria. Dense mitochondria, dense capillary supply, high myoglobin content (the oxygen-binding protein that gives slow fibers their dark red color). Fatigue-resistant. Moderate force per fiber. These are the endurance specialists — your postural muscles, soleus, diaphragm. Marathon runners have unusually high Type I percentages, partly trainable, partly genetic.

**Type IIa — fast oxidative-glycolytic.** Fast myosin ATPase. ATP from both oxidative phosphorylation and glycolysis. Moderate mitochondrial density, moderate fatigue resistance. Higher force per fiber than Type I. The middle-distance specialists — strong enough for explosive movement, oxidative enough not to fail immediately. Most athletic movement heavily recruits Type IIa.

**Type IIx — fast glycolytic.** Fastest myosin ATPase. ATP almost entirely from anaerobic glycolysis. Few mitochondria, pale color, high force per fiber. Fast to fatigue — roughly thirty seconds of maximal output before exhaustion. Sprint and power specialists. A 100-meter sprinter or power lifter has unusually high Type IIx in their primary movers.

<!-- → [TABLE: fiber type comparison — columns: fiber type, myosin ATPase speed, primary ATP source, mitochondrial density, fatigue resistance, force per fiber, dominant athletic use. Rows: Type I, Type IIa, Type IIx. Caption: "three specialists sharing one muscle. Recruitment order follows the size principle: I first, IIa next, IIx only at maximum effort."] -->

The size principle connects fiber type to recruitment order. Type I fibers sit in small motor units with low thresholds — they fire first, they handle the constant low-load work. Type IIx fibers sit in large motor units with high thresholds — held in reserve for emergencies. The architecture is efficient: the fatigue-resistant fibers handle routine demand; the powerful but fragile fibers are protected from unnecessary use.

---

## Where the ATP comes from

Three energy systems supply ATP to a contracting muscle at different timescales, and knowing which system dominates tells you what will fail first.

**Immediate — phosphocreatine.** Muscle fibers store creatine phosphate. When ATP is consumed faster than it can be remade, an enzyme transfers a phosphate from creatine phosphate to ADP, regenerating ATP in one step. Fast but finite — sustains maximal effort for about ten seconds. The first ten seconds of a sprint, the moment of a vertical jump: phosphocreatine.

**Short-term — anaerobic glycolysis.** When phosphocreatine is depleted and oxygen delivery hasn't caught up, the fiber breaks glucose (or glycogen) down to pyruvate, producing ATP without oxygen. Pyruvate is reduced to lactate to keep glycolysis running. This system sustains hard effort for roughly thirty seconds to a few minutes.

**Sustained — oxidative phosphorylation.** With adequate oxygen, mitochondria fully oxidize glucose and fats, producing far more ATP per substrate than anaerobic pathways. The only system capable of sustaining effort for hours. Its rate is limited by oxygen delivery — the cardiovascular system, not the muscle.

Muscle fatigue is not one thing. Phosphocreatine depletion caps maximal short efforts. Glycogen depletion hits marathoners around mile 20 — the "wall" — when liver and muscle glycogen are exhausted and the body shifts toward fat oxidation, which is slower. Ion accumulation (extracellular potassium, intracellular inorganic phosphate) disrupts EC coupling and reduces force per cross-bridge. At very high intensities, the SR's calcium handling itself degrades.

Lactate is worth clearing up, because it carries undeserved blame. Lactate is cleared from blood within roughly an hour of exercise. Delayed-onset muscle soreness — DOMS — peaks 24 to 48 hours later and is caused by microscopic damage to fibers, especially during eccentric contractions where the muscle lengthens under load, followed by inflammation and repair. Lactate is a fuel during exercise — the heart and slow-twitch fibers oxidize it readily. It is not a toxin and it is not causing your soreness two days later.

<!-- → [CHART: three-panel time-course of energy system contribution during exercise of increasing duration. X-axis: time from 0 to 120 minutes. Y-axis: % of ATP supply. Panel 1 (0–10 sec): phosphocreatine dominant. Panel 2 (10 sec–2 min): anaerobic glycolysis dominant. Panel 3 (2 min–120 min): oxidative phosphorylation dominant, with fat contribution rising as glycogen depletes. Caption: "the three systems are not sequential switches — they overlap. But each one dominates a window, and the window defines the event."] -->

---

## Cardiac muscle — same engine, different wiring

Everything above describes skeletal muscle. The remarkable fact about cardiac muscle is that it uses the same cross-bridge cycle — actin, myosin, troponin, tropomyosin, calcium gating — all conserved. What changes is the control system.

Cardiac muscle is striated like skeletal muscle because it also has sarcomeres in register. But cardiac fibers are short, branched, and connected end-to-end by **intercalated discs** containing two kinds of junctions: desmosomes that anchor adjacent cells mechanically (so the tissue doesn't tear under pumping stress) and gap junctions that let ions flow between cells. An action potential beginning in one cardiac cell spreads directly through gap junctions to its neighbors without needing a synapse. The myocardium behaves electrically like one giant cell — a **functional syncytium**.

Cardiac muscle is **autorhythmic**. Cells in the sinoatrial node have unstable resting membrane potentials that drift slowly toward threshold and fire spontaneously. The pacemaker fires; the action potential spreads via gap junctions across the atria, through the AV node, and into the ventricles. Your nervous system can speed or slow the pacemaker, but it does not initiate each beat. Cut all cardiac nerves and the heart still beats — at a different rate, but it beats. This is why heart transplants work.

The cardiac action potential lasts 200 to 400 milliseconds — far longer than skeletal's 1 to 2. The plateau phase comes from voltage-gated calcium channels staying open, admitting calcium from outside the cell while the SR also releases its own (calcium-induced calcium release). Cardiac muscle therefore uses both extracellular and SR calcium; skeletal uses almost entirely SR calcium.

The long action potential means the refractory period is nearly as long as the contraction itself. The cell cannot be re-stimulated until it has nearly finished relaxing. **The heart cannot be tetanized.** This is not a limitation — it is a survival mechanism. A next action potential cannot arrive in time to stack on top of the first. If cardiac muscle had skeletal-style action potentials, the heart would tetanize at high heart rates and stop pumping blood.

<!-- → [CHART: side-by-side comparison of action potential duration and force-time curves for skeletal vs. cardiac muscle. Left panel: skeletal — short action potential (~2 ms), long twitch (~100 ms), refractory period ends before twitch peaks, enabling tetanus at higher stimulation frequency. Right panel: cardiac — long action potential (~300 ms), twitch of similar duration, refractory period extending through the contraction, preventing re-stimulation until relaxation is nearly complete. Caption: "the cardiac action potential is a built-in governor. The cell is electrically refractory for as long as it is mechanically contracting — making tetanus structurally impossible at any physiological heart rate."] -->

---

## Smooth muscle — the quiet workforce

Smooth muscle wraps the walls of blood vessels, gut, bladder, airways, uterus, the iris. It is non-striated — actin and myosin are present but arranged less regularly than in sarcomeres — and involuntary, controlled by the autonomic nervous system, hormones, local chemical signals, and stretch.

Two organizational patterns. **Single-unit** smooth muscle (visceral) has cells connected by gap junctions; the whole sheet contracts together — gut, bladder. **Multi-unit** smooth muscle has individually innervated cells allowing fine local control — the iris, piloerector muscles.

Smooth muscle has no troponin. Instead, when calcium enters (from extracellular space or a smaller SR), it binds **calmodulin**, a regulatory protein. The calcium-calmodulin complex activates **myosin light chain kinase**, which phosphorylates myosin. Only phosphorylated myosin can cycle. This gate is slower than the troponin-tropomyosin switch — smooth muscle contracts over seconds rather than milliseconds.

Many smooth muscles generate **slow wave potentials** — slow rhythmic oscillations in membrane potential that periodically bring the cell to threshold. Peristalsis in your intestines runs this way: pacemaker cells (interstitial cells of Cajal) generate slow waves that propagate through the smooth muscle network without moment-to-moment nervous command.

Smooth muscle can also hold tension at very low metabolic cost through **latch bridges** — cross-bridges that remain attached to actin for extended periods without cycling. Blood vessels maintain vascular tone for hours using latched cross-bridges rather than actively cycling ones. If smooth muscle ran the same ATP bill as skeletal muscle, maintaining basal vascular tone would be metabolically unsustainable.

<!-- → [DIAGRAM: two-panel comparison of smooth vs. skeletal muscle calcium regulation. Left panel (skeletal): thin filament with troponin-tropomyosin; Ca²⁺ binds troponin C; tropomyosin shifts; actin site exposed directly. Right panel (smooth): no troponin; Ca²⁺ binds calmodulin; Ca²⁺-calmodulin complex activates MLCK; MLCK phosphorylates myosin regulatory light chain; phosphorylated myosin cycles. Latch state shown as dephosphorylated myosin remaining attached. Caption: "smooth muscle takes a longer route to activation — Ca²⁺ → calmodulin → MLCK → phospho-myosin — and can stall in a low-cost latch state when MLCK is inactivated but cross-bridges have not yet detached."] -->

---

## Three failure modes of the same machine

Let's take the cross-bridge cycle and ask what breaks when three different things go wrong. The setup: a myosin head has just completed its power stroke and is in the rigor state, gripping actin, waiting for ATP. The motor neuron has fired. Calcium is in the cytosol. Tropomyosin has moved. Everything is ready.

**Failure mode 1 — Curare.** Curare blocks the nicotinic ACh receptors at the NMJ (Link 3 of EC coupling). ACh is released by the motor neuron but cannot bind. No depolarization of the sarcolemma. No T-tubule signal. No calcium release from the SR. Troponin never binds calcium. Tropomyosin never moves. Binding sites stay covered. The cross-bridge cycle never starts. The result is **flaccid paralysis** — muscles stay relaxed because they never receive the signal. Curare was the first surgical muscle relaxant for exactly this reason; it stops the muscle without affecting consciousness or the heart (though it stops the diaphragm, requiring ventilation).

**Failure mode 2 — Succinylcholine.** Succinylcholine mimics ACh at the receptor but is not broken down quickly by acetylcholinesterase. The receptor stays bound. The sarcolemma stays depolarized. After a brief initial twitch (the visible fasciculations at induction), voltage-gated sodium channels along the sarcolemma inactivate under the sustained depolarization and cannot re-fire. Result: **flaccid paralysis** by the opposite mechanism. Curare prevents depolarization; succinylcholine causes depolarization that will not stop. Both block contraction; the molecular stories are mirrors of each other.

**Failure mode 3 — Death.** ATP production stops. Existing ATP is consumed within minutes. Myosin heads complete their current power strokes, arrive at Step 5, and grip actin in the rigor state. No new ATP arrives to release them. SERCA pumps also fail; calcium leaks out of the SR permanently, leaving binding sites exposed. More cross-bridges form, lock, and never release. The muscle stiffens. **Rigor mortis.** It begins two to six hours after death and resolves twenty-four to thirty-six hours later as the proteins denature.

The lesson: calcium is the gate; ATP is the fuel. Remove the gate and the fiber relaxes — it was never activated. Remove the fuel and the fiber locks — it cannot release. The same machinery fails in opposite directions depending on which input disappears.

---

## The major muscles — one organizing move

There are roughly 640 named skeletal muscles, and memorizing every one is not the point. The point is to understand the organizing principle well enough that any muscle's name and location lets you predict its action.

The consistent move: *name a muscle, ask what joints it crosses, ask in which direction it can shorten, and you have its action*. The names — Latin compounds for origin, insertion, shape, or action — are usually self-documenting. *Sterno-cleido-mastoid*: sternum to clavicle to mastoid process. Pulls diagonally, rotates and flexes the head. Every name is a description waiting to be read.

**Head and neck.** Facial muscles attach skin-to-skin or bone-to-skin — expression, not joint movement. Chewing muscles (masseter, temporalis) clamp the mandible. Neck muscles (sternocleidomastoid, scalenes, upper trapezius) move the head and resist gravity.

**Trunk anterior.** Pectoralis major and minor on the chest. Rectus abdominis and the obliques on the abdomen. Diaphragm internally — the primary breathing muscle.

**Trunk posterior.** Trapezius and rhomboids anchor the scapula. Erector spinae runs the spine's length, holding posture. Latissimus dorsi spans lower back to humerus, powering pulling.

**Upper limb.** Deltoid lifts the arm. Rotator cuff (supraspinatus, infraspinatus, teres minor, subscapularis) holds the humeral head in its socket. Biceps brachii flexes the elbow; triceps extends it. Forearm muscles control wrist and fingers.

**Lower limb.** Gluteus maximus extends the hip; gluteus medius and minimus stabilize the pelvis in single-leg stance. Quadriceps extend the knee; hamstrings flex it and extend the hip. Gastrocnemius and soleus plantarflex the ankle. Tibialis anterior dorsiflexes it.

<!-- → [INFOGRAPHIC: anterior and posterior body maps with major muscle groups labeled by region. Each muscle labeled with its primary action. Color-coded by region: head/neck, trunk anterior, trunk posterior, upper limb, lower limb. Caption: "a muscle's name is usually a description. Read the Latin and you have the anatomy."] -->

---

## Common misconceptions

**"Muscles push."** They do not. A muscle can only shorten. Every "pushing" motion in the body is a muscle pulling on a bone whose lever geometry translates that pull into the outward movement you feel. When you push a door open, the triceps is pulling the ulna backward, extending the elbow. The hand moves outward because of the lever. The muscle pulled.

**"The all-or-nothing principle means a whole muscle is on or off."** This is about the fiber, not the muscle. A whole muscle is a collection of motor units. The nervous system grades force by recruiting more units and firing them faster. A muscle can produce one percent of its maximum or ninety-nine percent. The individual fibers are all-or-nothing; the muscle is precisely gradable.

**"Lactate causes muscle soreness."** Lactate is cleared from blood within roughly an hour of exercise. The soreness peaking 24 to 48 hours later is delayed-onset muscle soreness from microscopic fiber damage — especially in eccentric contractions — followed by inflammation and repair. Lactate is a fuel during exercise, not a toxin deposited in your tissue.

**"More muscle mass means more strength."** Mass matters, but architecture and neural drive matter as much. A small pennate muscle can outpull a larger parallel one of the same volume. Training increases strength substantially before any visible size change, largely by teaching the nervous system to actually access the high-threshold units. The nervous system's access to the muscle it owns is often the limiting factor.

---

## Exercises

**Warm-up**

1. A sarcomere is 2.0 μm long at rest. When the muscle contracts fully, the A band is still 1.6 μm. What is the new sarcomere length if the H zone has disappeared entirely (thin filaments have just reached the M line)? Which bands changed and which did not? Explain each in one sentence. *(Tests: sliding filament theory; band behavior during contraction)*

2. Define the following in your own words, without using the word you are defining: *cross-bridge*, *power stroke*, *rigor state*, *motor unit*, *wave summation*. If your definition uses jargon you have not also defined, rewrite it. *(Tests: precision of vocabulary; conceptual clarity)*

3. Rank the three energy systems — phosphocreatine, anaerobic glycolysis, oxidative phosphorylation — by (a) speed of ATP delivery and (b) total ATP capacity. Then name the athletic task most dependent on each. *(Tests: energy system hierarchy; application to exercise)*

**Application**

4. ATP synthesis in a muscle fiber stops abruptly. Calcium is still present in the cytosol. Walk through what happens to each step of the cross-bridge cycle. Which step gets permanently stuck? What is the macroscopic consequence — does the muscle relax, contract harder, or lock? Connect your answer mechanistically to rigor mortis and explain why the stiffness resolves after 24–36 hours. *(Tests: cross-bridge cycle; failure modes; protein denaturation)*

5. A patient with myasthenia gravis (autoimmune destruction of nicotinic ACh receptors at the NMJ) is given a drug that inhibits acetylcholinesterase. Predict what happens to her muscle strength, and trace your prediction through the EC coupling chain. Name the specific link the drug is targeting and explain why the intervention helps. *(Tests: EC coupling; NMJ pharmacology; disease mechanism)*

6. A 400-meter runner and a marathon runner both train five days per week, but their leg muscles look and perform very differently. Using fiber type proportions, myosin ATPase speed, and energy system dominance, predict how each runner's vastus lateralis differs — and explain why the size principle means the marathon runner is using her Type IIx fibers far less than the sprinter does, even at race effort. *(Tests: fiber types; recruitment order; size principle)*

**Synthesis**

7. Botulinum toxin cleaves SNARE proteins in motor neuron terminals, preventing synaptic vesicle fusion. Tetanus toxin (from *Clostridium tetani*) blocks inhibitory interneurons in the spinal cord that normally suppress motor neuron firing. Both toxins ultimately affect muscle. Predict (a) the direction of muscle failure for each (flaccid versus rigid), (b) which link in the EC coupling chain each toxin breaks, and (c) why the clinical presentations are opposite despite both toxins targeting the nervous system's control of muscle. *(Tests: EC coupling; inhibitory circuits; clinical reasoning)*

8. During a maximal isometric contraction — holding a weight still without moving — a muscle is generating force but producing no visible work. Yet the muscle fatigues. Explain, using cross-bridge cycling, SERCA pumping, and the energy systems, why a contraction that does no external mechanical work still consumes ATP at a high rate. *(Tests: ATP cost of contraction and relaxation; isometric vs. isotonic; fatigue mechanisms)*

**Challenge**

9. The cardiac action potential plateau (the long depolarization phase driven by slow calcium channels) is sometimes described as the "price the heart pays" to avoid tetanus. Construct the argument in full: starting from the physics of the refractory period, show why a longer action potential extends the refractory period, why that extension prevents tetanus at physiological heart rates, and then calculate — roughly — at what stimulation frequency a heart with a 300 ms refractory period would first be at risk of incomplete relaxation. What is the clinical correlate of this risk? *(Tests: cardiac action potential; refractory period; tetanus; tachyarrhythmia)*

10. A physiologist proposes that smooth muscle's latch-bridge mechanism evolved specifically to allow sustained vascular tone at low metabolic cost. Design two experiments — one in an isolated smooth muscle preparation and one in a whole animal — that could test whether latch bridges really do reduce ATP consumption compared to actively cycling cross-bridges maintaining the same tension. For each, describe (a) what you would measure, (b) what result would support the latch hypothesis, and (c) what result would refute it. *(Tests: latch-bridge mechanism; experimental design; hypothesis testing)*

---

## What would change my mind

If a careful study found that smooth-muscle latch bridges require continuous ATP at rates comparable to skeletal-muscle cross-bridge cycling — that "latch" is a kinetic story rather than a low-energy hold — I would have to revise the claim that smooth muscle maintains vascular tone at near-negligible metabolic cost. The latch-bridge story is well-supported, but the precise energetic cost in vivo is harder to measure than textbooks suggest.

## Still puzzling

How does the nervous system override reciprocal inhibition during deliberate co-contraction? What sets the resting level of fiber-type composition — how much is genetic destiny, how much is trainable, and at what age does plasticity decline? Why does eccentric contraction produce so much more microtrauma per unit of force than concentric — what is structurally vulnerable about the lengthening-while-loaded state? And what exactly makes a single myosin head's 10-nanometer stroke add coherently across a sarcomere when individual heads are firing asynchronously — what dynamic prevents the net pull on the thin filament from averaging out?

---

## LLM Exercise — Build the sliding filament simulator

**Build:** `05-sliding-filament.html`

A single-page interactive that visualizes one sarcomere contracting, with three inputs and three outputs the student can manipulate and read.

**Inputs (controls):**
- A **calcium slider** (0 to "high"): sets cytosolic calcium concentration. When low, tropomyosin covers binding sites and the cross-bridge cycle cannot proceed. When high, sites are exposed and cycling proceeds.
- An **ATP toggle** (present / depleted): controls whether myosin heads can release from actin after the power stroke. When ATP is depleted, heads lock in the rigor state — the simulator should visibly show this.
- A **stimulation frequency slider** (single twitch → low-frequency train → fused tetanus): controls how often the motor neuron is firing. The calcium dynamic and force output should respond.

**Outputs (visualizations):**
- An **animated sarcomere** showing thick and thin filaments, with myosin heads cycling visibly through the five cross-bridge steps when conditions allow. The Z discs should visibly move toward the M line as contraction proceeds; the A band should stay constant; the I and H zones should shrink.
- A **force-output graph** showing tension over time as twitches stack into summation into tetanus.
- A **cytosolic calcium indicator** that rises with each action potential and falls between them (SERCA at work), with the rate of decline matching the set frequency.

**Show / Say / Constrain / Verify**

*Show:* paste the cross-bridge cycle (Step 1 through Step 5 as described above) and the EC coupling chain (Links 1 through 8) into your prompt. Show one or two reference images of a sarcomere with labeled bands. Tell the LLM the simulator must visibly demonstrate the cycle and the band-length rules.

*Say:* tell the LLM exactly what you want — a single-page HTML file with embedded JavaScript and CSS, no external dependencies, three sliders, one toggle, and three visualizations as listed. The animation should run at 30–60 fps. The force graph should scroll left to right and persist a few seconds of history.

*Constrain:* the simulator must enforce the physics — when calcium is low, no cross-bridges form regardless of ATP; when ATP is depleted, cross-bridges that have started must lock in the rigor state and stop cycling; when stimulation frequency exceeds the calcium-pumping rate, calcium accumulates and tetanus develops. The A band must not change length under any condition. The I and H zones must shrink in proportion to contraction.

*Verify:* run three test cases.
1. Calcium low, ATP present, no stimulation: no contraction, no force.
2. Calcium high, ATP suddenly depleted mid-contraction: cross-bridges should freeze, force should plateau at the current level, and the sarcomere should not return to rest. (This is rigor.)
3. Stimulation frequency ramped from low to high while ATP is plentiful: force output should show individual twitches that gradually fuse into unfused tetanus and then smooth fused tetanus.

If any of these fail, push back on the LLM with the specific test that failed. *"When ATP is depleted, your simulator is letting the heads detach. They should be locked. Fix it."* Iterate.

**Exploration**

Once the simulator works, use it to investigate:

- What happens to force output if you keep stimulation frequency high but reduce ATP availability over time? (This simulates fatigue in a glycolytic fiber as substrate runs low.)
- What happens at very high calcium, very high ATP, very high stimulation? Does force keep rising indefinitely, or does it plateau at the maximum the simulated sarcomere can produce? Why?
- Add a "fiber type" toggle that changes the speed of myosin ATPase (slower for Type I, faster for Type IIx) and the rate of SERCA pumping. Run the same stimulation pattern through each. How does the force-time profile differ?

**Extension to Chapter 6 — the nervous system commands the muscle**

The simulator currently treats motor neuron firing pattern as an input slider. Chapter 6 is about how the nervous system generates that pattern. After Chapter 6, come back and add: a model of a motor neuron with a membrane potential, an excitatory input from "higher centers," and a threshold for firing. Then watch what happens when you stimulate the neuron rather than directly setting the muscle's input frequency. The motor neuron's behavior — when it fires, how fast it can re-fire, how recruitment works at the population level — is what the muscle sees as its command signal.

This is the bridge to the next chapter: muscles contract when commanded by the nervous system. We have just shown what the muscle does with the command. Next we have to ask where the command comes from.

---

*Byline: Nik Bear Brown*

*Tags:* sarcomere, cross-bridge-cycle, excitation-contraction-coupling, motor-units, sliding-filament-theory
