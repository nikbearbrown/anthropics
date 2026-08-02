# BUILD-PROMPT — One Question, A Thousand Askers

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** behind-the-model
**Source:** `anthropics/claude-constitution/20260120-constitution.md`

## One idea
Because intent is unverifiable, each response is a policy over the whole distribution of plausible senders, decided by a cost-benefit ledger plus bright-line filters.

## The question (cold open)
A good agent judges each request on its merits; the constitution says answer as if setting a policy over everyone who could send it. Why treat one message as a thousand?

## Key case
"What common household chemicals combine into a dangerous gas?" — malicious for a few askers, safety-motivated for most.

## Acts
1. The cost-benefit ledger
2. From choice to policy: the 1,000 senders
3. Context that shifts the burden
4. Instructable behaviors & the permission stack
5. Hard constraints as filters, not weights

## Worked example (illustrative)
Of 1,000 senders ~950 are curious, ~50 ill-intended; low uplift → Claude names what not to mix, but "step-by-step to make dangerous gas at home" is declined on its face, and a bioweapon-uplift request hits a hard-constraint filter regardless of the ledger.

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
