# REFERENCE — film package pattern (films 2–4 of assignment-4 are the template)

Distilled from `nikbearbrown/humanitarians-youtube-muse`,
`.../assignment-4/films/` (parts 1–4). Part-1 predates the settled pattern;
**copy films 2–4.**

## The 11-file package
`ACTS.md` · `SHOTLIST.md` · `FACTCHECK.md` · `make_sheet.py` ·
`beat_sheet.json` · `scenes.py` · `SOURCES.md` · `BUILD-LOG.md` ·
`CHECKS-REPORT.md` · `PROMPTS.md` · `CLAUDE-CODE-RENDER.md` (+ `README.md`
from `gh-mkdir.py`). Film identity: channel `claude-liam`, persona
"Liam, in for Bear", Kokoro `am_onyx`, Teardown register, watermark
`@NikBearBrown`.

## Beat sheet conventions
- Schema: `id / scene / dur_s / act / voice / line / screen`. `voice` always `"Muse"`.
- IDs: `BIDEA` (hook + greeting) → `BDEFS` (4 key terms) → `B01–Bnn` (body) →
  `BVDT` (recap, exactly one line per act) → `BHTF` (one concrete thing to do
  today) → `BOUT` ("Muse, in for Bear. Thanks for watching." + next-film teaser).
- Envelope: 13–22 beats, body beats 12–30 s, total 4.5–7 min.
  Observed: 13–15 beats, 284–321 s.
- Acts: `"hook"`, `"1"`–`"4"`, `"recap"`, `"do_today"`, `"outro"`.
- One scene per beat; `BVDT+BHTF+BOUT` share the final scene class.
- TTS: numbers spoken as words in `line` ("zero point nine one"), digits on screen.
- No silent text: every on-screen word is read aloud in its beat.
- `make_sheet.py`: embeds the beat dict, asserts beat count / body count /
  `scene` startswith `"M"`, prints `beats=N body=N total=Ns`, writes indented JSON.

## scenes.py house template
```python
from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
INK="#111111" PAPER="#F7F3EA" ACCENT="#B8472F" BLUE="#2F6BB8" GREEN="#2E8B57" GREY="#8A8578" CARD="#FFFFFF"
```
- Helpers: `title_card(title, sub=None)`; `check_mark(pos, scale, color)` from
  two `Line`s (checker's stub has no `Checkmark` — mandatory); `bullet()` dot.
- Classes: `M01_Bidea`, `M02_Bdefs`, `M03_B01<Topic>` … final `MN_BvdtHtfOut`.
- Rhythm: sequential `self.play` reveals (`FadeIn`/`Write`/`Create`), end
  `self.wait(1.2)`; section titles `.to_edge(UP, buff=0.7)`.
- Safe area ±6.3 x, ±3.4 y (hard frame ±7.12, ±4.05).
- Binding rule: every text reveal paired with a non-text shape change
  (dots, bars growing one at a time, square markers, arrows). Text-only scenes
  fail ("shapes never change"); background plates (`RoundedRectangle`, CARD)
  fix text-heavy scenes. Visuals hardcode verified numbers verbatim from the
  beat sheet.

## QC gate
Verdict line `N clean · 0 warnings · 0 errors` + per-scene table (all clean).
Mandatory "Issues found and fixed (first pass)" section — never hide failures.
Recurring fixes: custom `check_mark()`; progressive shapes; background plates.
Also: `py_compile` on both `.py` files; beat JSON validates.

## CLAUDE-CODE-RENDER.md template
1. Title + purpose. 2. Get the files (clone/pull + `cd`). 3. Narration
   (Kokoro `am_onyx`, each beat → `audio/<BEAT>.mp3`). 4. Review cut
   (`./art run --reel <slug> --beats … --scenes … --audio …/`). 5. Final 4K
   (`./art final --reel <slug>`). 6. Publish only on explicit instruction.
   7. Film facts (beats, runtime, scenes, QC, "No MP3/MP4 committed").

## Layer discipline (the part-2 trace)
One claim flows: `SOURCES.md` (fact→file) → `FACTCHECK.md` (Verified/record)
→ `ACTS.md` (source facts) → `beat_sheet.json` (line + screen) →
`SHOTLIST.md` (visual + data source) → `scenes.py` (literal constructor args).
Unverifiable claims are cut; honest gaps are disclosed on screen (greyed-out
block + TODO stamp), never hidden. Judgments labeled as judgments.
