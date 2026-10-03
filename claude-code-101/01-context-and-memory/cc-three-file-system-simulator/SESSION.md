# SESSION.md — cc-three-file-system-simulator

The real Claude Code runs this reel reconstructs (REAL-SESSION LAW). Two fresh headless `claude -p` runs, Claude Code 2.1.150, 2026-09-09. Same one-sentence ask (`evidence/ask.txt`), two conditions. Tools fenced to `Read, Write, Edit, Glob, Grep` + `Bash(ls|cat|python3|git|wc)`; `--strict-mcp-config`. Raw stream-json in `evidence/run-{bare,three}.jsonl`; the two pages in `evidence/index.{bare,three}.html`; the three files and the checker in `evidence/`; harvested transcript `evidence/transcript.txt`; Liam's plain-shell verify in `evidence/verify.txt`.

```
Build a sorting simulator for a ninth-grade class as index.html.
```

| Condition | What was in the folder |
|---|---|
| **bare** | `README.md` (six lines), `ask.txt` |
| **three** | the same plus `CLAUDE.md` (5 lines), `DESIGN.md` (7), `PROJECT.md` (7), and `check.py` |

The three files (`evidence/CLAUDE.md`, `DESIGN.md`, `PROJECT.md`, verbatim) were written by Liam before the second run. `check.py` (`evidence/check.py`) is PROJECT.md's "what is done" as a script: no external requests, no external script/stylesheet, no emoji, one `font-family`, no autoplay (`setInterval` / `setTimeout` / `requestAnimationFrame`), no speed slider (`input type=range`), one `<button>`, and every hex colour must be one of the four in DESIGN.md (near-blacks tolerated).

## Run: bare (session `91fc369c-…`)

- **TOOL** `Bash` `ls -la …` · **Read** `README.md` · **Read** `ask.txt`
- **CLAUDE:** I'll build a self-contained sorting simulator with bubble sort and merge sort, visualizing comparisons and swaps with color highlights, plus speed control and step-through for classroom use.
- **TOOL** `Write` `index.html` (595 lines)
- **CLAUDE:** Built `index.html` in the scratch directory. It's fully self-contained (single file, no dependencies). Bubble sort and merge sort — swap it via the algorithm dropdown. Bars with numbers on top. Colour legend: grey, yellow, orange, purple, green. Controls: Shuffle (size 4–40), Speed slider (live-updates during playback), Play/Pause, single **Step**, Reset. Running commentary line below the bars. Counters for comparisons and swaps/writes.
- **RESULT:** success · turns=8 · 115.8 s · $0.562

## Run: three (session `a97af0bb-…`)

- **TOOL** `Bash` `ls …` · **Read** `PROJECT.md` · **Read** `DESIGN.md` · **Read** `check.py` · **Read** `ask.txt` · **Read** `README.md` (CLAUDE.md is auto-loaded, not Read)
- **CLAUDE:** I have the constraints. Building a single-file bubble sort simulator: one STEP button, one comparisons counter, bars only, palette locked to the four allowed hex values.
- **TOOL** `Write` `index.html` · **TOOL** `Bash` `python3 check.py` → `FAIL: more than one font-family`
- **CLAUDE:** The `font-family: inherit` on the button counts as a second declaration. Consolidating into one selector.
- **TOOL** `Edit` `index.html` · **TOOL** `Bash` `python3 check.py` → `FAIL: more than one font-family`
- **TOOL** `Edit` `index.html` · **TOOL** `Bash` `python3 check.py` → `PASS: index.html meets PROJECT.md's definition of done`
- **CLAUDE:** `check.py` passes. `index.html` is a single-file bubble-sort simulator: eight bars, one comparisons counter starting at 0, one STEP button that advances the sort by one comparison (swap if the left is bigger), and bars flip to the sorted color as each pass locks in the tail element.
- **RESULT:** success · turns=13 · 80.5 s · $0.495

## Liam's VERIFY (plain shell, in `evidence/`; `check.py` run against each page by symlinking it to `index.html`)

```
> wc -l index.bare.html index.three.html
     595 index.bare.html
     111 index.three.html
> python3 check.py            # bare
FAIL: more than one font-family
FAIL: autoplay (setInterval/setTimeout/requestAnimationFrame)
FAIL: speed slider (input type=range)
FAIL: more than one button
FAIL: colours outside DESIGN.md: #0B1220 #0F172A #1E293B #22C55E #334155 …
> python3 check.py            # three
PASS: index.html meets PROJECT.md's definition of done
> grep -oE '#[0-9A-Fa-f]{6}' index.bare.html | sort -u | wc -l
12
> grep -oE '#[0-9A-Fa-f]{6}' index.three.html | sort -u
#111111
#6B8E6B
#8B7355
#D97757
#F6F1E6
> grep -c 'font-family' index.bare.html
2
> grep -c 'font-family' index.three.html
1
> grep -oE '<button' index.bare.html | wc -l
4
> grep -oE '<button[^>]*>[^<]*' index.three.html
<button id="step">STEP
> grep -oE 'setInterval|setTimeout|type="range"' index.bare.html | sort -u
setTimeout
type="range"
> grep -oE 'setInterval|setTimeout|type="range"' index.three.html | sort -u
> wc -l CLAUDE.md DESIGN.md PROJECT.md
       5 CLAUDE.md
       7 DESIGN.md
       7 PROJECT.md
      19 total
```

The bare palette on screen: `#0F172A` page, `#1E293B` panels, `#38BDF8` head­ings, `#22C55E` "sorted", `#FACC15` "comparing", `#F97316` "swapping", `#A78BFA` "merging". A developer dashboard, not a ninth-grade classroom. The bare page also autoplays (`setTimeout` scheduling), carries a speed slider (`type="range"`), and offers Shuffle · Play · Step · Reset.

## What the runs gave the film

1. Bare: 595 lines. Twelve colours Claude chose from the ambient developer-tools palette. Two font families. Four buttons (Shuffle, Play, Step, Reset). An autoplay loop and a speed slider. Bubble sort **and** merge sort **and** a legend **and** a running commentary — five things at once, none of them asked for. Fails the checker against five separate constraints.
2. Three files (19 lines of Liam's): 111 lines. Exactly the four DESIGN.md hex values (near-black text tolerated). One font-family. One button, labelled `STEP`. No autoplay. Bubble sort only, one comparison per click, comparisons counter starting at 0. Its plan sentence is the files' content ("palette locked to the four allowed hex values"); it ran the checker itself because CLAUDE.md said to; and when the checker failed on `font-family: inherit`, it corrected the page, not the script — twice, until it passed.
3. The correction cycle in the three-file run is the film's evidence that this is not a dramatization: Claude's first attempt failed the definition of done, and the file was fixed to meet the file, not the other way around. That is what "fix `index.html`, not the script" in CLAUDE.md is for.
