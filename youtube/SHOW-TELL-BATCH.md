# SHOW-TELL BATCH — brief for every film in show-tell-ideas.md

**What this is.** The standing instructions each build agent follows for the eight show-tell films Bear ordered on 2026-09-26 ("build them all in order"). **Why.** One brief keeps the eight films consistent with the first show-tell film, which Bear called "perfect" and which is published at youtu.be/TEHsl6rlfuI. **Result.** Each film ends as a gated 4K master in its reel folder. Nothing is staged or published.

## Read first, in full
1. `brutalist.art/skills/make/show-tell/SKILL.md`: the doctrine (laws, drawing laws, gate traps, spine, workflow).
2. The worked example, `anthropics/youtube/show-tell-claude-plugin-portal/`: `make_sheet.py`, `scenes.py` (the ISO KIT is pasted at the top), `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `BUILD-LOG.md`, `build_srt.py`. Copy their shape, not their text.
3. Your film's card in `anthropics/youtube/show-tell-ideas.md`, and the SOURCE it names. Read the source itself; don't work from the card.

All paths are relative to `/Users/bear/Documents/CoWork/bear-textbooks/books/`. Run every command from there.

## The spine (fixed)
BIDEA `BrutalistHesitantWriter` (a world-language greeting, "This is Liam, in for Bear.", and the naive question corrected into the real one) → BDEFS `ClaudeDefinitions` (2–4 terms) → B00…Bn body beats (as many as the topic needs, no more; one image per beat, drawn in Manim by default, a `ShowTellCard` only when it passes the SKILL.md card test; labels only; the voice explains) → BHTF `ClaudeComposerAsk` (Your Turn: a concrete prompt read in full, then two checks) → BOUT `ClaudeTitleOutro` (spoken: "<Title>. At Nik Bear Brown.", 1.0 s tail). `bookend_exempt: ["cold-open","bvdt"]`. Liam, Kokoro `am_onyx`. No length cap or target (Bear, 2026-09-27): as long as it needs to be, to the point, no filler — see SKILL.md law 9.

## Rules
- Build into `anthropics/youtube/<slug>/` (slug given in your task). Touch no other reel.
- **Never stage, post, or publish.** Stop at the master: `./brutalist.art/art final <reel> --height 2160 --out <reel>/exports/landscape`.
- Don't edit anything under `brutalist.art/` (the kit, skills, runtime). If the kit lacks a primitive, write it in your own `scenes.py`. If a toolkit script is broken, work around it in the reel and report it; don't patch it.
- Fact-check every claim against the named source (`FACTCHECK.md` rows: PASS / CORRECTED / EXEMPT). No number or claim the source doesn't support. A claim from a secondary place is attributed aloud and on screen. Illustrations that aren't data get an EXEMPT row.
- Bookloop law does NOT apply here: naming the Anthropic article or repo is fine.
- Pre-audit from a scratch copy before any 4K render: `runtime/qc/static_scene_check.py scenes.py --class <C>` (Gate A) and `runtime/qc/manim_layout_audit.py scenes.py --class <C> --curve-strict`, for every scene.
- Look at the frames yourself (low-res stills first, then the qc-sheet, then late frames of the master). Fix anything that reads wrong. Every gate must PASS: Gate A, B, W, V, GATE T, Gate F, and bookend.
- Delete nothing: superseded audio, renders or masters go to `<reel>/_superseded/`. No scratch scripts at the `books/` root; use the session scratchpad or the reel folder.
- Don't commit or push.
- Write the paperwork: FACTCHECK, SOURCES, SHOTLIST, PROMPTS, README (executive summary first), BUILD-PROMPT, and BUILD-LOG (dated; what broke and how it was fixed). Also write `build_srt.py` (copy it) so the reel is ready for staging later.

## Report back (short)
The master path, sha256, duration, and resolution; each gate's result; the facts that were CORRECTED, EXEMPT, or attributed; anything you couldn't do; the path of a contact sheet (late frame of each beat); and any toolkit bug you worked around.

## Batch 2 (overnight, 2026-09-27): extra rules
- Bear, 2026-09-27: "Over night run find the next 25 best candidates and do as many as you can ... list the candidates first." The cards are #10–#34 under "Batch 2 candidates" in `show-tell-ideas.md`; the queue and status are in `SHOW-TELL-BATCH2-QUEUE.md`.
- Two builders may run at once, and **they share the session scratchpad**. Put every scratch file and render ONLY under `<scratchpad>/st<card#>/` (e.g. `st12/`), or inside your own reel folder. Never write to the scratchpad root, never use generic names there, and never `rm -rf` anything outside your own `st<card#>/`. Give every manim render its own `--media_dir` inside that folder.
- Greetings that Kokoro says cleanly: Hallo, Bonjour, Hola, Ciao, Konnichiwa, Namaste, Salaam. Use the one your task names, and whisper-check it anyway.
- Source cautions from the scout (apply the one for your card):
  - #10: the course notebook's line that Claude "does not have access to any built-in server-side tools" is out of date; don't repeat it.
  - #11: ">2x" latency and "up to 90%" cost, quoted as the notebook states them. The cache lifetime isn't in the notebook (only `launch-your-agent/cma-primitives.md` says 5 minutes); leave it out or cite that file.
  - #13: two Ralph copies differ (`claude-code/plugins/ralph-wiggum` and `claude-plugins-official/plugins/ralph-loop`). Pick one, and check the command names against it.
  - #14: Managed Agents is in beta, and the doc says "live docs win"; say beta. Dreams is a research preview.
  - #15: the notebook's model list is out of date; name no supported models.
  - #16: 35% is "averaged across all data sources" (the top-20-chunk retrieval failure rate); quote it exactly or leave it out.
  - #17: the 50% saving, from the notebook, attributed.
  - #20: "~100 tools" and "90%+", from the notebook, attributed.
  - #21: stress the VM/sandbox warning.
  - #22: the README says the compiler is not validated for correctness. Credit no person; nothing here names one.
  - #23: the repo README is one line, so use the paper PDF (`claude-cookbooks/misc/data/Constitutional AI.pdf`).
  - #27: say the output is a draft for attorney review, not legal advice.
  - #28: ROI pricing may be stale; use no prices.
  - #31: the README says only "scores 0–100, filters below 80"; don't say scores are averaged.
  - #33: the 417 tasks, attributed.
  - #34: the thinnest source. Fetch arXiv 2401.05566 to confirm the persistence claim, or limit claims to the title and the trigger data.
- Casting: #29 and #31 share the pull-request setting with the published security-review film, so use a different cast. #20 sits next to "How a Skill Loads", so don't reuse the filing cabinet.
- Fact-check against the RAW source page, not a WebFetch summary. A summary of the hooks docs wrongly said PreCompact can't block (found by the #25 builder). Where a toolkit or plugin SKILL copy disagrees with live docs, the live docs win.
