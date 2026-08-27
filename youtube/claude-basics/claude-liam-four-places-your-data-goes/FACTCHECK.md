# FACTCHECK — claude-liam-four-places-your-data-goes

**Gate:** GATE F · **Date:** 2026-08-13

---

## DOUBLE-CHECK LAW — all three stripped claims confirmed absent

SOURCES.md named three claims that must not survive into this reel:

| # | Stripped claim | Status |
|---|---|---|
| 1 | "When your organization brings in Claude, model training is off by default." | **ABSENT** — not in any beat's narration_text |
| 2 | "At Anthropic, we work to make those choices easy to understand." | **ABSENT** |
| 3 | "Personal data is generally removed from chats before they're used for training." (hardened form) | **REWRITTEN** — B16 reads: *"Personal details are generally stripped out first — generally, and that hedge belongs to them, not to me."* The hedge is intact and explicitly attributed to the source, not to this reel. |

---

## B16 — the "generally" beat (special scrutiny)

> *"Level four is training. Some providers use conversations to improve the next model. Personal details are generally stripped out first — generally, and that hedge belongs to them, not to me."*

- **"generally" hedge is present.** ✓
- **Attribution is explicit.** The hedge is credited to the source, not asserted by this reel. ✓
- **Not hardened into a guarantee.** ✓
- **sparkLine: "Generally. Their word."** — on-screen text matches the narration's attribution posture. ✓

---

## No defaults asserted for any named provider

- **B11:** *"Depending on the product, memory is on by default or waiting to be switched on."*
  The "depending on the product" qualifier covers the real variance across AI products. No universal default is asserted. No provider is named. ✓
- **B19:** *"Where providers train on conversations, most let you opt out."*
  "Most" is hedged, not "all." ✓

---

## Mechanism claims — accuracy check

| Beat | Claim | Verdict |
|---|---|---|
| B05 | "When the window closes, it isn't holding them anywhere, because it wasn't holding them anywhere else to begin with." | ✓ Correct. Context windows are in-memory and cleared on session end. No persistence outside a memory feature. |
| B06 | "Open a fresh chat tomorrow and it starts blank." | ✓ Correct for conversations without memory enabled. |
| B09 | "The model did not remember you. A file on your account did — and that file gets read into the blank chat before you finish typing your first word." | ✓ Accurate mechanism for account-level memory features: user-facing memory is stored as a text document and injected into the context before the conversation begins. |
| B10 | "In most products you can read the file, change a line, clear it, or switch the whole thing off." | ✓ "Most" is appropriately hedged. Accurate across major AI products with memory. |
| B13 | "the period is real, it's usually written down, and it is not yours" | ✓ Retention periods are documented in privacy policies. "Usually" is hedged. |
| B17 | "It becomes a very small adjustment to how likely certain words are to follow other words." | ✓ Simplified but technically correct description of how gradient-descent training adjusts next-token prediction weights. |
| B18 | "You cannot un-train a model on a conversation it has already learned from." | ✓ Correct. Machine unlearning is an active research area but not available as a consumer guarantee. |
| B21 | "Most of what you type never leaves level one." | ✓ Accurate: most conversation content does not reach training. "Most" is hedged. |

---

## Credit attribution (B03)

> *"Anthropic's education team laid these four out and the taxonomy is correct — I'm borrowing it."*

- Names Anthropic as taxonomy source. ✓ (required by PLAN.md and SOURCES.md)
- Does not speak on behalf of Anthropic or assert Anthropic policy. ✓
- The SOURCES card (BVDT area) carries: *"Inspired by Anthropic's education video 'What does AI know about you?'"* per PLAN.md. ✓

---

## No-name check (restricted references)

- **Dante:** Not named anywhere in narration, on screen, in `beat_sheet.json`, in this file. ✓
- **Virgil:** Absent. ✓
- **No Italian, no inscription, no Roman numerals, no "abandon hope."** ✓
- **No tool authors named in narration or props.** ✓

---

## Corrections log

*(empty — no corrections required)*

---

## GATE F VERDICT: PASS

All three DOUBLE-CHECK LAW items confirmed absent or properly hedged. B16 carries the "generally" hedge with attribution intact. No defaults asserted for any provider. No Dante reference anywhere. Narration is factually accurate and correctly hedged throughout.
