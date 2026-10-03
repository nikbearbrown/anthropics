# REBUILD-LOG — nbb-ai-creative-work-belongs-to-nobody

**Rebuild pass:** 2026-09-01
**Snapshot preserved:** `beat_sheet.pre-rebuild.json` (byte-exact of prior sheet)

## Envelope

- kokoro / am_onyx confirmed (pre-existing on sheet; no change).
- No ElevenLabs-era fields to drop (`voice_id`, `voice_env`, ElevenLabs `clock` prose all absent).
- `folderLabel: "@NikBearBrown"` kept.

## Beats dropped

Four empty-envelope bookend duplicates deleted from the beats array — the four canonical patterns are already carried by NBB00/NBB01/NBB02/NBB03:

- `B00`  (ClaudeComposerAsk, empty narration; duplicate of NBB00)
- `BVDT` (ClaudeVerdictArtifact, `Key finding one/two/three` placeholder; duplicate of NBB01)
- `BHTF` (ClaudeComposerAsk, `Take what you learned from [X]…` template placeholder; duplicate of NBB02)
- `BOUT` (ClaudeTitleOutro, empty narration; duplicate of NBB03)

Amendment: "BVDT may be legitimately ABSENT if a previous pass stripped a placeholder verdict — absent is legal, present-and-empty is not." Same treatment applied to the other three envelopes. Matches the shape used on `nbb-handoff-condition-protocol` (2026-09-01).

## Narration edits

Every body beat (B01–B10) is unchanged — the locked script from the source reel is carried over verbatim.

The following bookend narrations changed. Each entry: **beat_id** — old → new — why.

- **NBB00** — "The Jason Allen ruling unsettles me - 624 iterations, 80 hours, and the Copyright Office still called the human authorship de minimis because the model's aesthetic defaults went uncontested. I want to understand what would have flipped it. Help me: (1) name the specific expressive choices Allen would have had to fix in writing to pass the authorship test, (2) explain why picking from eight options like Marcus did does not count as authoring the blue palette or the centered layout, and (3) show what contesting the defaults in writing concretely looks like for an image project so the work stops belonging to nobody." → **"Shalom, Liam — in for Bear. Why does 80 hours of AI-assisted work belong to nobody? Can you explain it, Bear?"**
  Reason: later automation had swapped a 110-word ask into NBB00 while `actual_duration_s` still read 3.861s (measured against the earlier 15-word line). The sibling `beat_sheet.nbb.json` carries the short form ("Shalom, Liam — in for Bear. Why? Can you explain it, Bear?"). Restored the pattern; the middle question is expanded from "Why?" to a legible one-line question that matches the reel's actual subject. Same defect and fix as `nbb-handoff-condition-protocol` (2026-09-01, `FILMLOOP-LOG.md`).

- **NBB00 `props.command`** — "The Jason Allen ruling unsettles me — [same long ask]" → **"Why does 80 hours of AI-assisted work belong to nobody?"** (same reason).

- **NBB00 `props.greeting`** — "Your turn." → **"Shalom, Liam"** (SPARK-LINE LAW / COLD OPEN LAW — `Your turn.` is reserved for the handoff; the cold open takes `<hello>, Liam`. Hebrew "Shalom" carried over from the sibling `beat_sheet.nbb.json`; not repeated by adjacent nbb reels in this run — `Hallå` (Swedish) already used on `nbb-brutalist-three-file`, `Merhaba` (Turkish) already used on `nbb-handoff-condition-protocol`).

- **NBB01** (verdict) — "Let's recap with Claude. Here's what the body just demonstrated. Seth built a game design agent two ways. …" (long body-verbatim recap) → **"Here is what the body just demonstrated. Nicholas describes the void underneath polished AI work: fluent form, absent author. Authorship requires decisions — not iterations on a model's proposals. Seth's two builds prove it. One prompt with no files: Claude's defaults inflect the persona. Three files first — technical, design, intent — same Claude, different agent, every decision traceable to Seth. AI handles technical execution. You keep creative judgment. The work is yours when the decisions are written down before the build starts."**
  Reason: the verdict narration is one of the two locations `rebuild/SKILL.md` authorizes new writing ("close narration is NEW writing, built from the sheet's own sparkLines/verdict content"). Old narration re-quoted B08/B10 verbatim; the new narration compresses to a real verdict aligned with the on-artifact lines.

- **NBB01 `props.artifactHeading`** — "Why AI Creative Work Is Beautiful and Belongs" (a truncation of the reel title, no verdict) → **"Fluent form, absent author."** (real body-derived summary).

- **NBB01 `props.artifactLines`** —
  1. "Nicholas, the creative contributor to this book, describes what he calls the void." →
     **"Silence is delegation — the model fills every micro-decision the spec leaves open."**
  2. "Authorship requires decisions — not iterations on a model's proposals." →
     **"Authorship = decisions written down before Claude touches the file, not iterations after."**
  3. "AI handles technical execution." →
     **"Intent — who this is for, what it refuses — is the one layer that cannot be delegated."**
  Reason: old lines were body-line quotes, not the reel's compressed claim. New lines state what this reel established, in three parallel sentences the viewer can screenshot. `verdict_audit.py` passes cleanly: no template default, no cross-reel duplicate, would be false of a different video.

- **NBB02** (your-turn) — "Take this prompt, run it on your own — pick any cancer type or clinical scenario you know about and ask how this mechanism applies there." → **"Take a piece of AI-assisted work you shipped this month — a deck, a design, a short essay, a bit of code. For every visible choice — the palette, the tone, the structure, the opening line — write down whether YOU decided it or the model did. Now count the model's decisions. Those are the ones the work belongs to."**
  Reason: check 5c — the placeholder was seeded from a totally unrelated (medical) template; rewritten as a real exercise from the reel's own content and method.

- **NBB02 `props.command`** — "Explain how [Why AI Creative Work Is Beautiful and Belongs to Nobody] applies to a specific cancer type or clinical case you're studying. What proteins are involved…" → **"Pick one AI-assisted piece I shipped this month. For every visible choice — palette, tone, structure, opening line — mark whether I decided it or the model did. Then tell me which decisions I should have written down before the build."** (same reason; on-screen prompt matches the narrated exercise).

- **NBB02 `props.segment`** — "Why AI Creative Work Is Beautiful" → **"Your Turn"** (segment card must reflect the actual beat, not restate the title).

- **NBB03** — unchanged; title outro reads "Why AI Creative Work Is Beautiful and Belongs to Nobody".

- **B01 shot** — `FormBCard.items` were `Key point one/two/three` with empty `sub` (scaffolder placeholders). Rewritten from the beat's own `on_screen` text:
  - `80 hours` — sub: `624 prompt iterations in Midjourney`
  - `First prize` — sub: `Colorado State Fair, fine art`
  - `No author` — sub: `Copyright Office ruled de minimis`
  `title` was the reel title (too long for the card head) → `The Jason Allen ruling` (the actual subject of the FormB card).

## scenes_std.py rewrite

The prior scenes file called `Text(narration[:30])` / `[:60]` on every chart label and caption, producing mid-word truncations ("AI tools have aesthetic defaults - a particular register, pa", "The comma you kept against the rule", etc.). Same class of defect fixed on `nbb-handoff-condition-protocol` (2026-09-01). Rewritten in full:

- `_two_bar(left_label, left_h, right_label, right_h)` — SHORT category-noun labels only. Right bar taller and terracotta when the narration favors it (B02: `80 hours` (82) vs `Authorship` (22, terra); B06: `Iterations` (30) vs `Decisions` (85, terra)).
- `_layer_stack([labels])` — 1–3-word box labels, top box terracotta.
- `_three_lines(l1, l2, l3, accent_line)` — three EB Garamond lines at font_size 54/42/42 (auto-scale only when the line legitimately overflows 12 Manim units), one terracotta spark under the accent line.
- `_caption(text)` — a single COMPLETE sentence at font_size 32, bottom of frame.

No line of narration text is drawn on a chart. Bar heights are drawn to agree with what the narration argues (iteration doesn't equal authorship → iteration bar shorter; decisions are load-bearing → decisions bar taller).

## Renders

- Kokoro audio generated for NBB00–NBB03 (4 beats free, $0.00). B01–B10 audio reuses the source reel's mp3s (locked pointer).
- Remotion: NBB00, B01, NBB01, NBB02, NBB03 rendered via `remotion_scenes.py`.
- Manim: B02–B10 rendered via 9 individual `manim -qm` calls, then copied `Scene_B<NN>_NbbAiCreative.mp4` → `media/B<NN>.mp4`.
- Compile: `compile.py --force`; slot Counter `Counter({'VIDEO': 14})`; GATE AUDIO PASS at −23.8 dB.
