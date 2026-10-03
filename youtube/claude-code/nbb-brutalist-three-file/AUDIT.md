# AUDIT.md — nbb-brutalist-three-file
Checked: 2026-08-31

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Stale renders | PASS | no mp4s existed |
| 2 | Bookends B00/BVDT/BHTF/BOUT canonical patterns | FIXED | duplicate `NBB00/01/02/03` wrappers removed; canonical bookends kept |
| 3 | Spark lines | FIXED | B00 greeting `"Liam"` → `"Hallå, Liam"`; BHTF greeting `"Your turn."`; body sparks preserved (`Received, not made.` / `Three files. Before anything.` / `Intent is authorship.` / `Maximally informed. Minimally autonomous.` / `Paste this.`) |
| 4 | Verdict | FIXED (authored) | BVDT was placeholder `Key finding one/two/three` + empty narration. Body has 5 beats, ~340 words → AUTHOR: four verdict lines drawn from body nouns; narration written to compress the claim |
| 5b | Chart text | FIXED | scenes_std.py rewritten: `Text(narration[:30])` mid-word truncation replaced with 1–3-word category labels + one complete-sentence caption; act header spelled `"THREE  FILES"` / `"INTENT  LAYER"` (doubled space so it does not rasterize as zero-width) |
| 5c | Your-Turn placeholder | FIXED | BHTF was `Take what you learned from [Three Files Before Claude Touches Anything] and apply it to your own work`. AUTHOR: real 3-step exercise (write PROJECT.md, then CLAUDE.md + DESIGN.md, only then ask Claude for the agent) |
| 5 | Card text | FIXED | B01 FormBCard had empty subs + generic labels `Key point one/two/three`. AUTHOR: 3 items (Polished by defaults / Generic by omission / Fails authorship) with real subs |
| 6 | Punt sweep | PASS | zero gen-AI asks, zero unfilled slates, zero DoodleScene, zero `STILL src=archive` for conceptual content. Empty shot blocks on B04 & B05 in pre-rebuild sheet AUTHORED (B04 → FormBCard summarizing the payoff; B05 → ClaudeComposerAsk handoff) |
| 7 | Card-only reel | PASS | B02 and B03 route to Manim (`Scene_B02_NbbBrutalistThree`, `Scene_B03_NbbBrutalistThree`); not a punt-in-a-costume |
| 8 | Lens audit | PASS | Descartes (what falsifies "I authored this?" → whether the expressive choices trace to the human — B01); Popper (states what would count as failing authorship: Copyright Office 2023 test); Plato (artifact vs world: the prompt output is the shadow, the intent-layer answers are the wall) — two moves earned in the body |
| 9 | Brand fields | PASS | `folderLabel: "@NikBearBrown"` (channel handle, not brand key); `engine: kokoro`, `voice: am_onyx` matches persona ("Liam, in for Bear") |
| 10 | Pacing | PASS-LOG | words/estimated_s at ~4.0–4.4 wps for B01–B04. Kokoro will set the real clock via measured audio — will re-check after mp3s |
| 11 | GATE T (type_check.py) | PASS | 0 FAILs; 1 advisory on §8.10 BVDT recites card — narration references the on-screen phrase intentionally, kept |

## Structural changes recorded

- Removed beats `NBB00`, `NBB01`, `NBB02`, `NBB03` (duplicate scaffolder wrappers that shadowed the canonical `B00/BVDT/BHTF/BOUT` bookends).
- Promoted B00's real cold-open `remotion` block (top-level in pre-rebuild) into `shot.remotion.props`; dropped placeholder `command: "What is: Three Files Before Claude Touches Anything?"` in favour of the real ask.
- Dropped dead ElevenLabs-era fields (`modelLabel: "Fable 5"`, `effortLabel: "High"` on NBB00/NBB02) with the removed beats.
- Removed `"locked": true` and `source_clip`/`source_audio` pointers that referenced audio-only from a sibling reel (`../brutalist-three-file/mp3/…`) — this variant now generates its own Kokoro audio, per rebuild contract §5.
