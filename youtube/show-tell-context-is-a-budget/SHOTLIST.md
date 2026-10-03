# SHOTLIST — show-tell-context-is-a-budget

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explaining. One tray cast for the whole film: a kraft tray (the context window, the same tray that was "context" in show-tell-how-a-skill-loads), blocks that land in it (white instruction page, dark tools, kraft messages, white results, a taped data box), a needle card, a data crate, a press, a notebook, and sub-agent crates. Measured narration total: 157.3 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "How do I give my agent / more context?", then corrects "more context" to "the right context". "Ciao. This is Liam, in for Bear." is spoken over it. | 10.2 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": context window, context rot, context engineering. | 15.6 |
| B00 | manim | `B00_Tray` | A kraft tray slides in ("context window"). One drop per phrase: a white instruction page, two dark tool blocks, three kraft message blocks, a taped data box. | 9.2 |
| B01 | manim | `B01_Rot` | A small card with a terracotta dot (the fact that matters) lands; two waves of message blocks and white result slabs pile in on top; then every block pales and the card's dot fades to grey; "context rot". | 12.7 |
| B02 | manim | `B02_Budget` | The tray shrinks to the lower right. Four token dots link every pair; "n²"; four more dots pop in and the web redraws with many more links, which thin out. | 9.0 |
| B03 | manim | `B03_Curate` | The tray returns. The pale extra blocks lift out and slide away; the prompt page and the needle regain colour; one of three tools leaves and the other two get dots; a tall stack of thin edge-case slips leaves and three example cards drop in; "high signal". | 10.8 |
| B04 | manim | `B04_JustInTime` | The data box lifts out of the tray and becomes a stack of crates outside it ("data"). A reference tag lands in the tray, tied to the crate by a dashed line ("file path"); one slice slides in; on "head and tail" the top and bottom crates light and only two thin slips come in. | 12.7 |
| B05 | manim | `B05_Compaction` | The crate leaves; the tray fills past its rim. A dark press arrives ("compaction"); two blocks get dots (decisions, bugs); the white result slabs fly out; the press comes down and squeezes the rest into one summary block, then lifts away ("summary"). | 15.0 |
| B06 | manim | `B06_Notes` | The tray steps left; a notebook sits outside it. Slips fly from the tray into the notebook, to-do rows and lines draw ("NOTES.md"), one row is checked; the tray empties (reset); one note card flies back in, with a terracotta check. | 9.7 |
| B07 | manim | `B07_SubAgents` | The notebook leaves; a plan page drops into the tray. Three small crates slide in ("sub-agents") on dashed lines; each fills with many small blocks; each sends one dotted summary card back to the tray. | 13.8 |
| B08 | manim | `B08_Rule` | The crates leave; the tray re-centres with the plan, the note and three summary cards. A small press ("compaction"), a notebook ("notes") and a crate ("sub-agents") arrive around it; a terracotta check lands on the tray. | 8.3 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the context-audit prompt types in full, then two check lines. | 26.1 |
| BOUT | bookend | `ClaudeTitleOutro` | The title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 4.2 |

Audio-first: the measured Kokoro mp3s are the clock. Scenes wait for their spoken phrases (`until`) and hold to 0.05 s under the audio. No animation spans a clip's midpoint (the `ST` guard in `scenes.py`), so the GATE T / Gate V sample frame is always a still. No verdict card; Your Turn is the Claude.ai composer; the spoken outro stays.
