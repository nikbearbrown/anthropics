# Show-tell conversion

Source: `books/claude-cowork-plugins/youtube/claude-liam-legal-finance/beat_sheet.json`

Structural checks passed. Narration, scenes, rendering, fact-checking, visual/audio QC and Bear review are still pending. No approval is implied.

**Object cast (consistent across all 14 body beats):** Two sealed cardboard boxes labeled 'legal' and 'finance' are the cast anchor, established in B00 and held in background for B12. Contract pages enter the legal box (B02, B03). Scan line and three flag dots (ghost-grey, dim, terracotta) on clause positions (B02). Five small page objects for legal input types (B03). Hours/minutes bars with threshold line (B04). Four dark-kraft caution-marker blocks, each corner of a box (B05, B10 — mirrored pattern reinforces that both plugins share the same limits structure). Isometric fork with contract page, human-figure block (B06, B11). Cash bar draining inside finance box, runway counter (B07). Five analysis objects around finance box (B08). Three ink curves toward break-even line (B09). Bar-chart object on conveyor to human-figure block (B11). Calendar block, terracotta flag marker, folder stack (B12). Rising cost curve with two position markers (B13).

**Card choices:** Zero ShowTellCard beats in the body. Every beat was tested against all three card-test questions. The triage fork (B06), depletion curve (B07), three-scenario curves (B09), and cost-of-delay curve (B13) are all richer as drawings of the film's own cast than as any ShowTellCard kind (paths, chart, or dashboard). No beat passed question 3 ('does it beat a drawing of the film's own cast?'). A film with zero cards is a normal, complete show-tell film.

**Open fact checks to resolve before render:** (a) Color-coded flag output (green/yellow/red with 'standard / attention / concern' labels) should be verified against the legal plugin's actual interface; source is ch11 chapter text, not the plugin UI directly. (b) 'Fractional CFO' as a characterization of the finance plugin's output is from the source chapter — verify this is Anthropic's own framing before it ships on screen. (c) All illustrative examples (price raise, contractor hire in B09) are deliberately generic, following source B18's own note that 15% and the hire were illustrative assumptions. (d) No numeric claims requiring attribution remain in this beat sheet; the 110× MCP growth figure belongs to the plugin-portal episode and does not appear here. (e) BDEFS term definitions should be spot-checked against published plugin documentation once public.

**BIDEA guard:** lead_silence_s: 0.8 set. triggerWords 'handle the work so you don't have to' appears verbatim in props.text and ends without punctuation. replacementWords 'screen the risk — the call stays with you' also ends without punctuation. Both verified against the component contract.

**BDEFS guard:** 'plugin' (6 chars), 'screening' (9), 'scenario model' (14), 'triage' (6) — all within the 17-character ClaudeDefinitions display limit.

**Removed source beats:** Six segment cards (C01–C06) removed per show-tell style (no act labels between body beats). Two mid-body ClaudeComposerAsk beats (B06, B15) removed per show-tell law (no composer beats between BDEFS and BHTF). V01 verdict artifact and BVDT verdict bookend removed per bookend_exempt: ['cold-open', 'bvdt']. Their content is distributed into BHTF's prompt and check lines.

**Timing note:** All estimated_duration_s values are word-count ÷ 2.5 words/second. Rewrite actual_duration_s from ffprobe after audio is generated with generate_audio_kokoro.py. BOUT tail_silence_s: 1.0 is padded after voice generation using the --only flag; do not rerun the full audio job for BOUT alone or the pad is dropped.
