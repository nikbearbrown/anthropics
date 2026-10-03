# FACTCHECK.md — hai-simple-whats-prompt-really

Checked: 2026-08-27

---

## Claims checked

| Beat | Claim | Verdict | Notes |
|---|---|---|---|
| B01 | "'Write a better prompt' is good advice." | PASS | Framed as a premise; immediately recontextualized by showing the advice depends on understanding what a prompt is. |
| B03 | "The natural reading: those three words are the prompt." | PASS | Framed as a common misconception, not asserted as true. Immediately broken at B04. |
| B04 | "Claude doesn't forget what you said last turn the moment you start a new message." | PASS | Accurate. Conversation history is included in the context window across turns. |
| B05 | "A prompt is the entire block of text assembled and handed to the model before it produces a single word — not just your message, everything the model can see." | PASS | Accurate and canonical. Claude's API documentation confirms the prompt is the full input context, including system prompt and conversation history. |
| B06 | "It has three parts: system instructions — usually invisible, set by whoever built the interface you're using. The conversation history — every prior exchange, written out in order. And your new message." | PASS | Accurate. The three-part structure (system / messages array / new user turn) matches the Claude Messages API format. |
| B07 | "All three get assembled, in that order, into one long block. The model reads it from the top, then generates what comes next." | PASS | Accurate. The model processes the full context from beginning to end before generating the response. "Reads from the top" is a useful simplification of the attention mechanism's forward pass. |
| B08 | "In a clean session, the model receives any system instructions — possibly empty — then your three words. It reads the whole block before writing the first word of its reply." | PASS | Accurate. A fresh session with no system prompt contains only the user message. The model generates after the full forward pass over the input. |
| B09 | "There's a hard limit on how much the model can hold at once — the context window. When a conversation hits that limit, the oldest messages are quietly dropped from the block." | PASS | Accurate. Context windows are finite. In practice, API consumers and Claude.ai handle long conversations by truncation or summarization; the claim that oldest messages are dropped is the standard default behavior. |
| B10 | "A longer conversation doesn't mean the model remembers more. Hit the context limit and the oldest part of the conversation drops — automatically, without notice." | PASS | Accurate. No persistent memory beyond the context window exists in base Claude. Truncation is silent from the model's perspective. |
| B11 | "A short message doesn't mean a small context. A developer might have loaded the interface with a long set of instructions. Those arrive silently at the top of every block, before your first word." | PASS | Accurate. System prompts can be arbitrarily long and are invisible to the user in most interfaces; they prepend every turn. |
| BCRY | "A prompt is everything the model can see — not just what you typed, but the whole conversation and any instructions that were set before you arrived." | PASS | Accurate carry-out. |

---

## Simplifications noted (honest, appropriate for audience)

- B07: "The model reads it from the top" — technically the transformer processes all tokens in parallel via self-attention, but the conceptual model of "read then respond" is accurate at the input/output level and appropriate for a plain-register explainer.
- B09: "quietly dropped from the block" — specific handling varies by interface (hard truncation vs. summarization vs. sliding window). The claim is accurate for the common default case and uses the qualifier "quietly" to acknowledge the silent nature.

---

## Datable claims

None. No version numbers, model names, specific token counts, or time-sensitive figures are named.

---

## External names

None. No third-party tools, companies, authors, or products are named in narration or on-screen text. NO EXTERNAL NAMES rule satisfied.

---

## Verdict

**FACTCHECK: PASS** — All stated claims are accurate. Simplifications are appropriate for a plain-register general-audience explainer. No stale or version-specific claims.
