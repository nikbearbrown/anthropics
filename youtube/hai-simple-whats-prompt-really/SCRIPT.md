# SCRIPT — What's a prompt, really?

*Reel: hai-simple-whats-prompt-really*
*Register: Plain — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive question using "command," hesitates, crosses it out, replaces with "prompt," lands the real question. Liam reads the corrected version over the typing.)*

**Liam:** "Someone started this question as if it were about commands — crossed out command, and wrote prompt instead. What's a prompt, really? Let's find out."

---

## B01 — Stakes

The phrase "write a better prompt" is everywhere. It's good advice — but most people have never stopped to ask what a prompt actually is. The answer changes what the advice means.

---

## B02 — ANCHOR PLANTED

*(THE ANCHOR. This exact visual returns at B08.)*

Hold on to one picture: you open Claude, type three words — explain DNA — and press Enter. That's the moment we'll come back to.

---

## B03 — Wrong Guess

The natural read is that those three words are the prompt. You typed them, the AI reads them, works from them — the way a search query is exactly what you typed.

---

## B04 — Break It

But if that were true, Claude would forget what you said last turn the moment you started a new message. It doesn't. Something is being carried forward that isn't just your latest words.

---

## B05 — Mechanism: Prompt = Everything

A prompt is the entire block of text assembled and handed to the model before it produces a single word — not just your message, everything the model can see.

---

## B06 — Three Parts

It has three parts: system instructions — usually invisible, set by whoever built the interface you're using. The conversation history — every prior exchange, written out in order. And your new message.

---

## B07 — Assembled

All three get assembled, in that order, into one long block. The model reads it from the top, then generates what comes next.

---

## B08 — ANCHOR PAYOFF

*(THE ANCHOR RETURNS — same "explain DNA" inside the block structure.)*

Back to explain DNA. In a clean session, the model receives any system instructions — possibly empty — then your three words. It reads the whole block before writing the first word of its reply.

---

## B09 — One Flag

One flag: there's a hard limit on how much the model can hold at once — the context window. When a conversation hits that limit, the oldest messages are quietly dropped from the block. The rest still holds.

---

## B10 — Both Directions: A

So a longer conversation doesn't mean the model remembers more. Hit the context limit and the oldest part of the conversation drops — automatically, without notice.

---

## B11 — Both Directions: B

And a short message doesn't mean a small context. A developer might have loaded the interface with a long set of instructions. Those arrive silently at the top of every block, before your first word.

---

## BCRY — Carry-Out (Remotion)

A prompt is everything the model can see — not just what you typed, but the whole conversation and any instructions that were set before you arrived.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me. Ask Claude: before you answer anything else, walk me through what's in your context right now. Everything you can see — any instructions you were given, the conversation so far, my current message. What does the full picture look like from your side? Run that today. You'll see the three parts arrive in the order they were assembled. Liam, in for Bear.

---

## BOUT — Outro (Remotion)

What's a prompt, really? Liam, in for Bear.

---

## Six-Move Audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | B01 | WRONG-GUESS LAW setup |
| 2 wrong guess | B03 (planted at B02), broken at B04 | WRONG-GUESS LAW |
| 3 mechanism | B05, B06, B07 | ONE-FLAG LAW |
| 4 anchor | B02 planted → B08 paid off | ANCHOR LAW |
| 5 both directions | B10 / B11 | BOTH-DIRECTIONS LAW |
| 6 carry-out | BCRY | CARRY-OUT LAW |
