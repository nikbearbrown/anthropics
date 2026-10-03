# ACTS.md — Muse Can See (Film 3 of 12)

**Exact title:** Muse Can See

**Core promise:** By the end, the viewer knows Muse's two visual superpowers
— transcribing images and building a web page from a reference image — and
the workflow that makes them work: sharp instructions up front, judgment and
iteration after.

**Structure:** hook + key terms + three acts (9 body beats) + recap + your
turn + outro. 14 beats, ~282 s (~4m42s).

- **Hook (BIDEA):** what if the model could look at your screen?
- **Key terms (BDEFS):** Vision · Transcription · Reference image ·
  System instruction.
- **Act 1 — Read it (3 beats):** B01 the NHK screenshot ("transcribe this");
  B02 the result (100%, kanji/kana, tiny furigana); B03 the honest footnote
  (the encoding glitch was the editor's fault, not the model's).
- **Act 2 — Build it (4 beats):** B04 the PHP-Nuke reference image; B05 the
  system instruction (front-end dev, one file, flexbox); B06 the result
  (three columns, modules, shoutbox); B07 judge it, ask for one more pass.
- **Act 3 — Work it (2 beats):** B08 single-shot vs iterate; B09 the
  mobile-friendly check.
- **BVDT:** 3 lines, one per act.
- **BHTF:** screenshot something on your screen; ask it to transcribe it.
- **BOUT:** "Muse, in for Bear. Thanks for watching." + teaser for Film 4
  (Thinking on Canvas).

**Tone:** curious, practitioner-like. The instructor's tests are presented as
his tests ("he grabs a screenshot", "he checks it"), with the honest
footnotes kept in — the film is about what the model can do *and* how to
tell.

**What this film is not:** not the playground setup (Film 2); not
brainstorming/diagrams (Film 4); not search grounding (Film 5).

**Cast:** the screenshot is a browser-window frame (rounded rect + three
dots); the website is a three-column rail sketch (left rail / center /
right rail) reused across B04–B09; the check-mark glyph marks every verified
result; the coin/price motif does not appear (no pricing in this film).

**Source facts:**
- NHK News Easy screenshot fed to the model with the one-word prompt
  "transcribe"; result 100% accurate on kanji, hiragana, katakana; tiny
  furigana readings in parentheses rendered small — the only oddity.
  (transcript §4)
- Replacement characters in the pasted-back output were the author's editor
  mangling the encoding, not model error. (transcript §4)
- PHP-Nuke reference: original template screenshot; concept = social tech
  community for tech professionals (DevOps, cloud, AI, security).
  (transcript §5)
- System instruction: front-end web developer with designer skills; single
  self-contained HTML file; no CSS framework; flexbox; lean markup and CSS;
  mobile-friendly. (transcript §5)
- Result: single-file retro PHP-Nuke concept, three-column flex layout;
  modules (system load, who's online, select your stack, contributors,
  server status, nuke chat shoutbox); feed, docs, submit post, topics, top
  10; sample headline about cutting Kubernetes costs. (transcript §5)
- Judgment: looks right; wants more spacing; plugins skewed to site
  performance vs community engagement → asked for one more pass with
  specific direction. (transcript §5)

**LEFT OUT (with reasons):**
- JLPT grammar-list prompting — that was Film 2's quality-test beat.
- The mermaid mind-map iteration — that's Film 4's whole subject.
- Playground controls (reasoning effort, streaming) — Film 2.
