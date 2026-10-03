# SHOTLIST — show-tell-five-ways-to-wire-an-agent

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explaining. One conveyor cast for the whole film: a kraft crate with terracotta tape (the work), dark stations (one LLM call each; the light turns terracotta when the call runs), pale belts (paths written in code), ink gates. Measured narration total: 150.0 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "How do I build / the smartest agent?", then corrects "the smartest agent?" to "the simplest one that works?". "Bonjour. This is Liam, in for Bear." is spoken over it. | 13.5 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": augmented LLM, workflow, agent. | 13.7 |
| B00 | manim | `B00_Station` | One dark station by a belt. A magnifier ("retrieval"), a connector block ("tools") and a page stack ("memory") drop in and cable to it; a crate rides in and the light comes on. | 11.1 |
| B01 | manim | `B01_Chain` | "1 prompt chaining": three stations behind one belt, an ink "gate" after the first. The crate gains a tick at each station; at the gate a terracotta check lands and the gate turns terracotta. | 10.5 |
| B02 | manim | `B02_Route` | "2 routing": one belt into a track switch that fans to three lines. The lever swings: a kraft crate to "refunds", a dark crate to "tech support", a small crate to the small station. | 10.6 |
| B03 | manim | `B03_Parallel` | "3 parallelization": the belt splits into three lanes and merges. Sectioning: the crate breaks into a block, a page and a small crate, which ride the lanes and rejoin. Voting: three identical crates ride, get two checks and a cross, and the two that agree merge. | 13.4 |
| B04 | manim | `B04_Foreman` | "4 orchestrator-workers": a tall foreman station takes the crate; four "workers" pop up only once it decides; crates fly out along dashed paths and back; on "Unlike parallelization" a fifth worker appears. | 13.1 |
| B05 | manim | `B05_Inspector` | "5 evaluator-optimizer": a maker station and an inspector booth on a loop of belts. The crate is crossed at the booth and rides back along "feedback" to the maker, gains a tick, returns, and on "until it passes" gets a terracotta check. | 9.7 |
| B06 | manim | `B06_Agent` | The belt drops out of frame ("take the rails away"). "agent": the crate hops between loose tool stations on dashed arcs it draws itself; each landing lights a result and fills a step pip; a stop marker sits at the end of the "max steps" row. | 12.4 |
| B07 | manim | `B07_Simplest` | A six-step staircase. The crate lands on the bottom step beside one station ("start here", a check); cost stacks grow on the higher steps; a "measure" gauge rises past its line, and only then does the crate climb one step. | 11.1 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the pattern-picking prompt types in full, then two check lines. | 26.2 |
| BOUT | bookend | `ClaudeTitleOutro` | The title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 4.7 |

Audio-first: the measured Kokoro mp3s are the clock. Scenes wait for their spoken phrases (`until`) and hold to the end (`finish`). No verdict card; Your Turn is the Claude.ai composer; the spoken outro stays.
