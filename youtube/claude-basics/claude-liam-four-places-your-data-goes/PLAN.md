# PLAN — claude-liam-four-places-your-data-goes

**Title:** Three You Can Take Back. One You Can't.
**Skill:** `ai-explainer` (extends `explainer`) · no modifier — not a profile, not a skill-teardown
**Channel:** `claude-liam` — Liam in for Bear, Kokoro `am_onyx`, free · footer chip `@NikBearBrown`
**Reel:** `anthropics/youtube/claude-basics/claude-liam-four-places-your-data-goes/`
**Register:** Teardown — describe the mechanism → judge it → name the constraint
**Source:** Anthropic education video, "What does AI know about you?" (Zoe, Anthropic education team), 4:40. **Inspired by, not adapted from.**
**Estimated runtime:** 3:30–4:00 · 26 beats

**Status: plan gate. No `beat_sheet.json` written.**

---

## The one thing this reel adds

Anthropic's video is good and it is accurate. Its frame is *"the reassuring part is that you have control."* True — and it treats the four uses as one continuum of control when they are not. **They differ in reversibility, and the video never draws that axis.**

| Use | Where it lives | Can you take it back? |
|---|---|---|
| 1 · the conversation | context window, nowhere else | **Yes** — close it and it's gone |
| 2 · product memory | a file on your account the model re-reads | **Yes** — edit, clear, toggle |
| 3 · provider systems | logs, safety review, ops, retention | **Partly** — you can ask; you don't hold the clock |
| 4 · training | the weights | **No** |

Use 4 is the whole reel. The source says it beautifully — *"your detail isn't really your exact words anymore — it's a pattern"* — and presents that as reassurance. It is also the point of no return. **Opt-out is prospective. You can close the door; you cannot un-walk through it.**

The rule that falls out, and the reel's verdict: **price what you share against the least reversible use it could reach, not the most.**

## Act map

| Beats | Act | Carries |
|---|---|---|
| B00 | Cold open · `ClaudeComposerAsk` | The ask lands answered; Liam signs in |
| B01–B04 | **The detail** | One shared detail; the empty four-rung ladder |
| B05–B07 | **Rung 1 · the conversation** | Bounded context; close it, it's gone. Gate: reversible |
| B08–B11 | **Rung 2 · product memory** | *Not the model remembering* — a file re-read into a blank chat. Gate: reversible |
| B12–B15 | **Rung 3 · provider systems** | Logs, safety review, retention. Gate: partial — you can ask, you don't set the clock |
| B16–B19 | **Rung 4 · training** | Words become a pattern. Gate: **no**. The terracotta moment of the reel |
| B20–B22 | **What follows** | Ladder redrawn, all four gates lit; the pricing rule; the placeholder habit |
| B23 | Verdict · `ClaudeVerdictArtifact` | |
| B24 | Handoff · `ClaudeComposerAsk`, `Your turn.` | Prompt read aloud and discussed |
| B25 | Outro · `ClaudeTitleOutro` | Title restate |

## The recurring visual

**The reversibility ladder** — a C3 concept illustration built once at B02 and revisited at every act. Four rungs on the cream stage, the detail (`partner · hiking · near Denver`) descending one rung per act, a gate glyph resolving at each. The only terracotta in the reel that repeats: the gate at rung 4, which never opens. Everything else is warm ink.

Per ILLUSTRATE LAW the Claude UI appears **only** at B00, the one ask micro-beat, B23, B24, B25. Every inner beat illustrates.

## Authoring decisions

- **Greeting: `Sawubona, Liam`** (Zulu, one word — Liam's budget). Chosen deliberately: *sawubona* means "I see you." For a privacy episode that is the joke, and it is never explained on screen. Wagwan is Bear's; Liam never takes it.
- **ASK→RESULT pair at B08–B09** — the composer types *"show me what 'the model remembers me' actually means"*, the next beat is the blank-chat-plus-pasted-memory-card illustration. One pair is enough for a reel this length.
- **One ask→result, one UI cold open, one handoff.** Typing appears in exactly two beats.

## DOUBLE-CHECK LAW — what gets stripped

The source carries three things a @NikBearBrown reel must not repeat as-is:

1. **"When your organization brings in Claude, model training is off by default."** Vendor-specific, current-policy, will date. **Cut.** The reel teaches *go read your provider's toggle*, and asserts no defaults for anyone.
2. **"At Anthropic, we work to make those choices easy to understand."** First-party framing. Cut — we are not Anthropic.
3. **"Personal data is generally removed from chats before they're used for training."** True as a general industry practice, hedged in the source with "generally." Keep the hedge or cut the claim. Do not harden it.

Everything kept is the taxonomy and the mechanism, which are the source's real contribution and are correct.

## Credit

The source is named on screen once, on the SOURCES card near the outro: *Inspired by Anthropic's education video "What does AI know about you?"* — and in the description. Not quoted, not screenshotted (REBUILD LAW), not parroted. The four-use taxonomy is theirs and is credited as theirs.

## Handoff prompt (B24 — read aloud verbatim, then discussed)

> Open the privacy and data settings for the AI tool you use most. Find four specific things: whether it keeps conversation history, whether it has a memory feature and whether it's on, what retention period it states, and whether training on your conversations is on or off. Then tell me which of those four I could reverse tomorrow and which one I couldn't.

Interesting because it makes them go look, and because the last clause is the reel's argument applied to their own account.

## Not a duplicate

`anthropics/youtube/claude-for-education/` already holds `claude-liam-advising-privacy-gate` and `claude-liam-data-minimization-prompt`. Both are prompt-technique reels. Neither teaches the four-use taxonomy or the reversibility axis. No overlap; different series folder.

## Gates

1. Write `beat_sheet.json` — 26 beats, lanes, `show` blocks, the ladder as a reusable C3 component.
2. **GATE P** — narration on an animated slate. No audio spend before signature.
3. Kokoro `am_onyx` → measured mp3s become the clock → align.
4. Slate previz → VISUAL QC LAW frame pass → GATE T → `art final`.

Never publish. Never stage to TOPOST.

---

## Visual grammar — superseded section

The "recurring visual" section above is superseded by **`VISUAL-GRAMMAR.md`** in this folder: the four uses are staged as a Dante-structured descent (ordered named places, narrowing per level, a threshold at each, one-way arch at level 4). The reference is never named on screen, in narration, in the title, or in the description.
