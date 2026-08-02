# BUILD-LOG.md — Free AI in 2026: What You Actually Get

**Slug:** claude-liam-free-ai-2026  
**Channel:** claude-liam (@NikBearBrown)  
**Reel folder:** anthropics/youtube/claude-liam-free-ai-2026/

---

## 2026-08-01 — Initial Plan (Gate Plan)

**Source:** `/Users/bear/.codex/attachments/2caf1d80-735d-4a80-8224-f4f2c8f4bd4d/pasted-text.txt`  
Research compilation on free AI tiers; unresolved `<cite>` markers; source warns about SEO content quality.

**Skills:** deep-explainer (on ai-explainer chassis). claude-liam persona, Kokoro am_onyx, @NikBearBrown, Teardown register.

**Authoring decisions:**

1. **Constraint-first editorial angle** — source structured as "which is best?" — reworked to "what is your constraint?" to avoid a fan-war framing and produce durable content.

2. **FRAMEWORK GATE (B04 before examples)** — The five-constraint routing framework was placed in Act I (B04) before the worked examples (Acts II–IV) to satisfy the teaching-arc requirement. B27 (Act V) is the WORKED EXAMPLE that uses the framework on current cases.

3. **Volatile-limits thesis as content** — every specific number in the source is either UNCONFIRMED or contradicted by the source itself. Rather than paper over this, the reel makes volatility a primary thesis: B05 (limits change faster than published), B30 (verify before you build), and the snapshot marker are all structural beats. This is editorially honest AND more durable than a reel that cites specific numbers as facts.

4. **Specific numbers stripped from on-screen evidence** — "14,400 req/day" compresses to "tens of thousands"; "58→112 tok/s" compresses to "roughly doubled"; "32K Gemini context" appears as "smaller ceiling (unconfirmed)"; contradictory Gemini Pro API limits (50/day vs 1,500/day) excluded entirely.

5. **No model version names on screen** — "Sonnet 5", "GPT-5.5 Instant", "GPT-5.6 Terra/Sol", "Ollama 0.19" all stripped. Structural descriptors used: "Sonnet-class model", "capable base model", "recent runtime updates."

6. **VOX beat selection** — 8 VOX beats (27%, WARN but not FAIL) arranged in 2 runs (R1 B24–B25, R2 B29–B30) plus 4 singles. All tier-1 generic; no rights escalation. Selected for emotionally resonant visual anchors: access (B03), scale (B10), coding access (B13), stacking (B18), privacy (B24, B25), routing (B29), verification (B30).

7. **Greeting: "Annyeong"** — Korean informal hello, one word, fits Liam's word budget. Not repeated in recent batch run (verify against recent reel list before audio).

8. **IN-FOR-BEAR LAW compliance** — B00 narration: "this is Liam, in for Bear." B33 narration: "Liam, in for Bear." B00 greeting: "Annyeong, Liam." No Wagwan (Liam never uses it).

**Beat count:** 34 total (B00–B33); 30 body beats.  
**Estimated runtime:** ~7 minutes 22 seconds (at 2.9 words/s; real measured audio will differ).

---

## Gate Status

| Gate | Status | Notes |
|---|---|---|
| GATE F (fact-check) | **PASS** | FACTCHECK.md written; all volatile claims stripped or labeled |
| CHECKS-REPORT | **PASS** | Teaching arc passes; VOX 27% WARN (acceptable) |
| GATE P (narration review) | **PENDING** — Bear must sign | Review narration on animated slate before any audio spend |
| Audio lock | PENDING — after Gate P | Kokoro am_onyx; all 34 beats |
| Gate D2 (SHOPPING.md) | PENDING — after audio lock | Must not be written before measured durations are known |
| Gate D1 (slate previz) | PENDING — after Gate P + audio | `./brutalist-art/art run anthropics/youtube/claude-liam-free-ai-2026` |
| GATE T (type-lock) | PENDING — after first compile | `scripts/type_check.py` |
| GATE SHARPNESS | PENDING — after first compile | Pixel-art Laplacian check |
| VISUAL QC LAW | PENDING — after compile | ffmpeg frame sample + 9-point rubric |
| Final cut | PENDING | `./brutalist-art/art final anthropics/youtube/claude-liam-free-ai-2026` |
| TOPOST staging | PENDING | `art post` skill only; HARD GLOBAL RULE applies |

---

## SHOPPING.md Note

**SHOPPING.md has NOT been written.** Per the deep-explainer spec (Gate D2): the shopping list must be written AFTER audio lock, never before. A list written before real MP3 durations are known cannot correctly state the beat window for each pantry still, and conform is left stretching instead of trimming.

Action: after audio lock, run `python3 runtime/scripts/pantry_search.py "<terms>"` for each of the 8 VOX beats. Copy any library matches; write SHOPPING.md with locked durations for unmatched entries.

---

## MISSING: None at this stage

All beats are authored with named components or pantry entries. No beats require human judgment to unblock at authoring time.
