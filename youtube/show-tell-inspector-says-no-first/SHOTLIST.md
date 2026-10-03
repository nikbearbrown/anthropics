# SHOTLIST — show-tell-inspector-says-no-first

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explains. Measured narration total: 157.7 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "How do I get my agent / to say it's done?", then corrects "say" to "prove". Namaste greeting spoken over it. | 7.5 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": builder, evaluator, default-FAIL. | 11.2 |
| B00 | manim | `B00_Bench` | A kraft workbench with the dark builder station slides up ("builder"); its light comes on; a part crate rises out of the bench; a unit-test tick flashes; the builder drops its own "PASS" tag on the part; a crack draws across the part. | 12.2 |
| B01 | manim | `B01_DefaultFail` | The bench steps left; a prompt note slides into the station and the PASS tag stays; the tag lifts off and "FAIL" drops on; the results board slides in ("test-results.json"); three rows each draw an ink cross. | 9.7 |
| B02 | manim | `B02_EvidenceGate` | A belt and the hook arch with a drop bar ("hook"); a write slip rides up and stops at the bar; a screenshot of the cracked part flies out and opens large ("evidence"); the hook light turns terracotta, the bar lifts, the slip rides through, row one turns to a check and the tag flips to PASS; the screenshot is used up, the bar drops, a second slip waits. | 10.0 |
| B03 | manim | `B03_Booth` | The board leaves; the builder's reasoning pages land on the bench; a closed kraft booth slides in ("inspector"); a wall rises between them ("fresh context"); the pages grey out; a spec, a diff and the screenshot drop in and slide into the booth's hatch; a pencil appears and is crossed out. | 10.2 |
| B04 | manim | `B04_NeedsWork` | The screenshot comes out of the booth's window and the crack is ringed; the booth's lamp comes on; a "NEEDS_WORK" slip slides out; a findings note ("findings") arcs back over the wall into the builder station; the part's tag flips back to FAIL. | 10.6 |
| B05 | manim | `B05_Handoff` | The booth and wall leave; the bench steps forward; the station's light goes out, it slides away, and a fresh station drops in; a clipboard drops beside the bench ("PROGRESS.md") and fills with lines; a dashed line runs from it to the station; grey commit slabs drop onto a stack ("git log"); the light goes out and a last slab drops. | 11.5 |
| B06 | manim | `B06_Loop` | The loop: a small bench ("build"), a belt, the booth ("inspect"), the board with three crosses; a part rides to the booth and a findings note flies back; the next trips flip rows to checks; a dashed line runs from the booth to the board and the last row checks. | 11.5 |
| B07 | manim | `B07_Operator` | The loop runs; an "AGENT_STOP" file drops in and every light goes grey with the part stopped on the belt; the file lifts away and the lights come back; a "STEER.md" note slides into the builder station, which pulses, and the part moves on. | 10.3 |
| B08 | manim | `B08_GoalVsYours` | The booth steps right; a small dark booth slides in ("/goal") with a one-line condition pill; parts pass it turn by turn on a belt and its lamp blinks each time; a terracotta check lands; the kraft booth pulses ("evaluator.md") and a hook arch rises over its own belt, its light turning terracotta. | 13.0 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the write-the-inspector-first prompt types in full, then two check lines. | 35.4 |
| BOUT | bookend | `ClaudeTitleOutro` | Title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 4.5 |

Audio-first: the measured Kokoro mp3s are the clock. Scenes wait for their spoken phrases (`until`), hold every animation off the clip midpoint (`ST`/`guard`), and end 0.05 s under their audio (`done`).
