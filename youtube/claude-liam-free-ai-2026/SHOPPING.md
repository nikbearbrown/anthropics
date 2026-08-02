# SHOPPING.md — STUB ONLY

**Status: NOT WRITTEN YET — Gate D2 requires audio lock first.**

Per deep-explainer spec: "SHOPPING.md is written AFTER audio lock, never before. A card written before the beat's real length is known can't state its duration requirement, and conform is left stretching instead of trimming."

After audio lock (Gate P → Kokoro generates MP3s → durations measured):
1. Run `python3 brutalist-art/runtime/scripts/pantry_search.py "<terms>"` for each of the 8 VOX beats
2. Copy any library matches to `pantry/<BID>-<id>.png`
3. Write the full SHOPPING.md with locked durations and tier annotations

**VOX beats awaiting stills (all tier-1 generic — AI-generate or stock):**
- B03: three access-pass objects (wristband, ticket, key)
- B10: tall stack of document pages
- B13: abstract coding interface on monitor (no real product UI)
- B18: layered trays (parallax — needs bg/mid/fg layers)
- B24: sealed envelope with wax seal [R1 start]
- B25: closed laptop on desk, alpha cutout [R1 end]
- B29: compass on folded map [R2 start]
- B30: open laptop showing documentation page [R2 end]
