# BUILD-LOG — show-tell-claude-plugin-portal

**What this is.** The dated record of the build, including what broke and how it was fixed.

## 2026-09-26
- Bear: "claude just launched a portal for plugins. make an explainer video … a new style that I call show-tell … every beat needs an image … minimal text … the voice over explains." He sent 4 reference frames, then "more images" with 5 more. Then: "make show-tell a new skill using drawn isometric illustrations in the Claude palette default to the Liam voice over."
- Sheet: 9 image beats plus the spoken outro. Kokoro `am_onyx` audio measured at 87.0 s.
- Stills review, round 1: B03's parts floated, so they now drop to the floor, with a bigger GitHub tag; B04's cursor covered the word, so it moved; B05's conveyor was enlarged and its status pill moved top-left; B08's check was spaced away from its label.
- Round 2: the GitHub label was touching its leader line, so it moved. The B05 "Submit" label sat below the safe area (−3.47), so the conveyor was lifted 0.15.
- Gate F failed with no paperwork, so FACTCHECK, SOURCES, SHOTLIST and PROMPTS were written. The claims were checked against claude.com/blog/build-plugins-for-claude; 110x appears only in the @ClaudeDevs post and is attributed.
- Gate A failed in two ways. B00 only moved its box ("shapes never change"), so a floor shadow was added in B00 and carried into B01. The static stub also lacks `rate_functions.ease_in_quad`, so a local `ease_in` replaced it.
- The show-tell skill was written from this build: `brutalist.art/skills/make/show-tell/`.
- Gate V, first 4K pass: 21 MAJOR. **Underfill** (19–54%): one object on cream is the show-tell style, so the gate's per-beat `qc.sparse_by_design` waiver was declared with a written reason on B00, B01 and B03–B08 (not B02, which fills on its own). **Low contrast** (0.21–0.27 on B00, B03, B04, B08): real, because pale cardboard averaged too close to the cream. Fixed in the drawing, not by waiver: kraft tones, 4 px ink outlines, and a dark title bar on B04's window. Tested at 0.27–0.33 on final frames.
- B03 "1" and "2" numerals changed from terracotta to ink (GATE T: no terracotta text).
- B00 still measured 0.29 on contrast at its 50% frame, so the floor shadow was deepened to #BFB4A0 and the "plugin" label now lands on "a portal for plugins" (the word, not "So first").
- GATE T (samples each clip at its midpoint), 3 FAILs, all fixed. B02: the half-faded server read as a faint text blob, so it now slides in, fully opaque, before the midpoint. B06: the DIM labels on the card were undetected, so they are now INK. B07: the half-drawn terracotta curve read as accent text, so the curve is now INK and only its end dot is terracotta.
- B04: the shield landed after its words, so the scan sweep went from 1.4 s to 0.9 s.
- **Master:** `exports/landscape/show-tell-claude-plugin-portal.mp4`, 3840×2160, 24 fps, 87.125000 s, sha256 84b701bdafdd27ef2ea6424153cb22430d786a9738aa5025a95734de81fef007, tail max_volume: -84.3 dB. Gates A/B/W/V PASS, GATE T PASS, Gate F PASS. Not staged, not published.

## 2026-09-26 — v2
- Bear, on v1: "add hesitant writer as the first beat and key terms like tldr uses as the second, the 'Your turn' should still mimic the Claude.ai interface like the all do ... otherwise perfect".
- Added BIDEA (`BrutalistHesitantWriter`: "…and how do I build one?" corrected to "get one live"; Liam's greeting moved here), BDEFS (`ClaudeDefinitions`: MCP, skill, plugin), and BHTF (`ClaudeComposerAsk`: the plugin-planning prompt plus two checks). The drawn B08 your-turn scene is gone. B00's line was shortened to "Start with the plugin itself…" and its cues retimed. `bookend_exempt` is now `["cold-open","bvdt"]`. The bookend check passes.
- New Kokoro audio for BIDEA, BDEFS, B00 and BHTF. The v1 B00/B08 audio and renders, and the v1 master (sha 84b701bd…), were kept in `_superseded/`.
- **Master v2:** `exports/landscape/show-tell-claude-plugin-portal.mp4`, 3840×2160, 127.6 s, sha256 f8856ff6…, tail −84.3 dB. Gate V: 0 defects across 24 frames. GATE T PASS (12 beats), Gate F PASS. Not staged, not published.
- **Published 2026-09-26** (Bear: "perfect"): https://youtu.be/TEHsl6rlfuI, unlisted, @NikBearBrown, Claude & Agentic AI at position 0, verified at forced 2160p. The master moved to TOPOST via `art post --no-topaz`.
