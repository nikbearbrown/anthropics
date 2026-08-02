# Chapter 2 — Production Tasks: What to Delegate and What to Protect

*The tool can do more than you think. That is exactly the problem.*

---

Here is the thing that puzzles me about the way designers talk about AI productivity: they describe it as though more speed is always better, as though the only question is how many tasks you can hand off before the client notices. Nobody asks the harder question, which is whether the task you handed off was actually yours to give away.

Let me try to make that concrete.

A freelance brand designer has five days to deliver what would normally take three weeks. Moodboards, image directions, social adaptations, deck cleanup, headline alternates, export specs. She uses AI for almost all of it. AI expands the moodboard. AI drafts image prompts. AI suggests copy alternates. AI cleans up the presentation structure. AI helps resize approved assets.

But she does not let AI choose the type system. She does not upload the confidential strategy deck. She does not let AI interpret the client's vague comment that the work should feel "less startup." She does not let AI write the final client rationale.

The project lands in five days. The client says, "This is sharper than the last round."

What changed was not that AI did the design. What changed was that she had already thought through which tasks were genuinely delegable and which ones, if handed off, would quietly transfer the authorship of the work to the tool. She had, in other words, a delegation map. This chapter is about how to build one.

<!-- → [IMAGE: Visual of the delegation map as a horizontal spectrum from "fully delegable" on the left to "protect" on the right, with specific design tasks placed along the spectrum — helps the reader see the shape of the framework before the details] -->

---

## What Makes a Task Safe to Delegate

The first question to ask about any task is whether it is bounded. A bounded task has a clear input, a clear output, and a low risk that the tool will silently make a strategic decision for you while completing it.

"Silently" is the key word. Most AI failures in design workflows are not dramatic. The tool does not refuse to work or produce obvious nonsense. It produces something plausible — something that looks finished — while having slipped a judgment past you. It chose a metaphor. It made an assumption about tone. It treated a creative decision as a production task. The output looks right, so you don't notice that something has moved out of your hands.

Bounded tasks resist this failure mode. When you ask a tool to resize an approved asset to twelve platform dimensions, it cannot slip a strategic judgment past you. The input is specified. The output is checkable. The risk is low. This is a Tier 1 task — safe to delegate after you set the frame.

<!-- → [TABLE: Tier 1 tasks for graphic and brand designers — columns: Task, Why it is delegable, Human check required — rows covering moodboard expansion, copy alternates, presentation cleanup, asset resizing, competitive scan summary] -->

The research that gets cited most often in this conversation — Noy and Zhang's productivity study, Brynjolfsson and colleagues' work on customer support — confirms that bounded work is where acceleration is most plausible. What those studies show is not that AI is universally good at creative tasks. They show that when the task has clear parameters and the output is inspectable, AI assistance reliably compresses time without obviously degrading quality. The inference some people draw — that this must extend to all design work — does not follow. A competitive scan summary is not the same kind of task as final mark selection, even if both involve visual judgment.

The practical rule is this: start with tasks whose failure you can quickly inspect.

---

## The Three Columns

Now here is where I want to push the framework harder, because the real insight is not about Tier 1 at all. Most designers who think about AI delegation reach a binary: things I'll use AI for, things I won't. That binary is too crude. It misses the most important category.

I think about it as three columns.

The first column is delegate. AI can do most of the task after you set the frame. You review the output, but you are checking for errors, not making decisions.

The third column is protect. AI may assist around the edges, but the final decision stays human — not because AI is incapable, but because the decision is where your accountability, your professional judgment, and often your client relationship live.

The second column is the interesting one: explore then decide. AI generates options. You make the decision. This is where most of the real design work lives, and it is the column most designers under-attend.

Consider color selection. AI can generate dozens of palette candidates in minutes. That is genuinely useful. But if you accept the palette because it looked good in the tool's output without asking whether it differentiates this client in their market, whether it holds up in accessibility checks, whether it survives across materials — then you have not explored and decided. You have just delegated to a tool that did not know it was being asked to make a strategic choice.

<!-- → [TABLE: Delegation map for brand identity work — three columns (Delegate / Explore then decide / Protect) with specific tasks sorted into each — this is the core operative tool of the chapter] -->

The middle column forces a question most designers don't ask explicitly: what is the actual decision here, and am I the one making it? When the answer is yes, the middle column is where you do your most productive AI-assisted work. When you stop asking the question, the middle column collapses into the delegate column, and you begin losing authorship without noticing.

---

## The Additive Problem

There is a structural reason why middle-column work is hard with generative tools: they are built to add.

More options. More texture. More adjectives. More visual motifs. More plausible directions. Generative systems are trained to produce candidates. They have no native sense of when the best move is subtraction — when the answer is to take out the impressive part.

Senior design is often exactly that: subtractive. Fewer elements. Clearer hierarchy. Sharper concept. More restraint. The skill is not generating five strong directions; it is recognizing which one is genuinely right and removing everything that competes with it.

Dorst and Cross described creative design as co-evolution between problem space and solution space: the designer's understanding of the problem changes while solutions are being explored. Their research suggests that the moment of highest creative leverage is not when you generate candidates — it is when you refuse a direction that would have been easier to accept. If you accept the first impressive output, you stop that co-evolution prematurely.

<!-- → [INFOGRAPHIC: Diagram showing two passes — generative pass (AI adds options, range, texture) followed by subtractive pass (designer removes, edits, decides) — makes the two-pass workflow visible as a single image] -->

This is why every generative pass needs a subtractive pass. Not as a quality check — as a design act. The subtractive pass is where you reclaim authorship of what the work means.

Here is what that looks like in practice. The AI-generated brand directions for a residential architecture firm include warm concrete textures, elegant floor-plan lines, a roofline symbol, a monogram, and a neutral palette. It looks finished. It is also too much.

Remove the roofline symbol. Too literal — it brands the firm as a company that makes buildings, not as a company that gives clients a sense of order before construction becomes overwhelming. Remove the monogram. Too generic for this market. Keep the floor-plan line idea, but redraw it as a modular grid that can become a layout system. Change the palette from beige-gray to charcoal, clay, and off-white, because the client wants residential warmth without looking like a lifestyle brand.

<!-- → [IMAGE: Before/after showing the AI-generated direction (full, busy, literal) alongside the designer's subtractive edit (grid system, reduced palette, no roofline symbol) — the visual argument for the two-pass workflow] -->

None of those decisions came from the tool. They came from understanding what the client was actually trying to communicate and being willing to discard what was impressive but wrong.

---

## Choosing Platforms by Task Risk

One thing I have noticed is that designers tend to choose AI tools by familiarity rather than by fit. They use what they already know how to use, and they apply it to whatever is in front of them. This is understandable, but it creates risk that is easy to avoid.

The criteria that should govern platform selection are more stable than the specific tools, which change quickly. Before using any platform for a client task, five questions are worth asking:

Does this task involve confidential client material? Some platforms use inputs to improve models by default. Terms vary and change. If you are not certain about data handling, the platform is not appropriate for confidential work.

Will the output appear in a final deliverable? If so, the platform's commercial terms need to permit that use for your specific context.

Does the client need to own or register the output? Copyright questions around AI-generated work are not resolved. If ownership matters — and in brand identity it almost always does — you need to understand what the platform's terms say about output ownership and what the current legal landscape looks like in your jurisdiction.

Does the tool provide usable commercial terms for this context? This requires reading the terms, not assuming.

Can you inspect and revise the result? If you cannot get inside the output and change it, you cannot do the subtractive pass.

Adobe Firefly occupies a particular position in this landscape because Adobe has marketed it around licensed and commercially cleared training data and has offered indemnification options for some enterprise customers. Whether that positioning holds up legally, and what it means for specific use cases, depends on current terms that should be verified before client use — not assumed from this chapter. Midjourney is genuinely useful for exploration but carries more uncertainty around output authorship and commercial use. Stable Diffusion workflows vary widely depending on which model, license, and deployment you are working with.

The practical principle is to pick tools by task risk, not by habit.

<!-- → [TABLE: Platform selection criteria — rows: confidential material, final deliverable, ownership/registration needs, commercial terms, revisability — columns: question to ask, risk if ignored, what to verify] -->

---

## What "Faster" Actually Means

I want to close with the speed question, because I think the framing most designers use is wrong.

"AI made me faster" is not a complete sentence. Faster at what? Faster in a way that protected or weakened the work? Faster in a way that transferred the judgment to the tool or preserved it with you?

The useful version of the speed question looks like a simple audit: for each task, what was the old time, what is the AI-assisted time, was the key human decision protected, and did quality change? That audit does three things. It tells you where the genuine gains are. It tells you where speed came at the cost of something that mattered. And it tells you, over time, which parts of your workflow have genuinely been transformed and which ones just feel faster because you are no longer doing the hard part.

<!-- → [TABLE: Speed audit table — columns: Task, Old time, AI-assisted time, Human decision protected?, Quality change — rows with sample design tasks showing where gains are real vs. where they mask lost judgment] -->

The deeper question — one that does not have a clean answer yet — is what speed gains mean for pricing. If you complete a three-week project in five days, and the quality is equal or better, you have not delivered less value. You have delivered the same value more efficiently. That efficiency belongs to you, not to the client as a discount. But if speed comes from skipping the protected decisions — from letting AI write the rationale, choose the type system, make the conceptual call — then what you have sold the client is not faster design. It is the appearance of design without the substance of it.

The delegation map does not resolve that question. But it gives you the tool to know the difference. Tasks in the delegate column make you faster at production. Tasks in the explore-then-decide column make you faster at exploration while preserving the decision. Tasks in the protect column stay with you, full stop, because they are where the work means something.

That is the map. The next problem is harder: once AI has produced something beautiful, how do you know whether it is actually ready? The audit framework in Chapter 3 gives you the answer.

---

## LLM Exercises

**Exercise 1 — Generate and Examine**
Ask an AI tool to generate three brand direction options for a residential architecture firm. Review the output and identify every decision the tool made that you did not explicitly specify. List them. Which of those decisions would you keep? Which would you change? Which should never have been delegated in the first place?

**Exercise 2 — Apply to Known Context**
Take your most recent client project and sort every task into the three-column delegation map: delegate, explore then decide, protect. Where did your actual workflow match the map? Where did it diverge, and why?

**Exercise 3 — Stress-Test the Speed Claim**
Identify one task in your practice where you believe AI has made you faster. Run the speed audit: old time, new time, human decision protected or not, quality change. Does the productivity gain survive the audit? If not, what did you actually trade away?

**Exercise 4 — Draft a Professional Deliverable**
Write a one-paragraph client-facing rationale for a brand decision you made recently. Now ask an AI tool to write the same rationale based on a description of the project. Compare them. What is in yours that is not in the AI version? What does that difference tell you about which column that task belongs in?
