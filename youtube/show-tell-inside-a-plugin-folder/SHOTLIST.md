# SHOTLIST — show-tell-inside-a-plugin-folder

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explains. Measured narration total: 158.3 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "How do I install / a Claude plugin?", then corrects "install" to "look inside". Konnichiwa greeting spoken over it. | 8.9 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": manifest, hook, MCP server. | 14.0 |
| B00 | manim | `B00_Folder` | The portal film's sealed kraft box drops in ("plugin"); a folder tab stands up on its back edge ("folder"); the lid lifts off and the parts peek out: a dark MCP block, the helper crate, a page. | 7.8 |
| B01 | manim | `B01_Label` | A white shipping label slaps onto the box's right face; an enlarged copy slides out ("plugin.json") inside a kraft folder (".claude-plugin"); its three lines draw on name / description / version; the name line turns thick ink with a terracotta dot on "Only the name is required". | 11.6 |
| B02 | manim | `B02_Commands` | The box steps left; a command page rises out ("commands"); a Claude Code window's prompt bar types "/commit"; the page drops into the window and three steps tick off. | 9.6 |
| B03 | manim | `B03_SubAgent` | A small kraft helper crate rises out ("sub-agent"); it rides to a stack of task pages ("task"), takes them one by one, and rides back with a report card on top. | 10.4 |
| B04 | manim | `B04_Skills` | Three skill pages rise and fan out ("skills"); each page's top line inks in as Claude reads it; a task card slides in ("task"); a dashed line links it to the matching page, which lifts while the others fade. | 9.9 |
| B05 | manim | `B05_Hooks` | An event belt with a hook gate ("hook"), a dark command slab ("command"), "on edit" at the start; an edit slab, a turn-end cube and another edit ride past the gate, and each time the gate light and the slab lights flash terracotta. | 13.1 |
| B06 | manim | `B06_MCP` | A dark MCP block rises out of the box ("MCP"); a server stack slides in and a cable draws to it; its lights come on; "GitHub"; an ink key (the access token) rides the cable. | 13.9 |
| B07 | manim | `B07_OnlyWhatItNeeds` | Two open boxes with labels on their faces: three slash-marked command cards drop into "commit-commands"; one tall MCP block drops into "github". | 9.3 |
| B08 | manim | `B08_Marketplace` | A kraft shelf of small plugin boxes ("marketplace"); a counter climbs to 255 ("per marketplace.json"); one box slides off the shelf; a magnifier glides over it ("trust it first"). | 13.6 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the look-inside-before-you-install prompt types in full, then two check lines. | 31.6 |
| BOUT | bookend | `ClaudeTitleOutro` | Title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 4.6 |

Audio-first: the measured Kokoro mp3s are the clock. Scenes wait for their spoken phrases (`until`), hold every animation off the clip midpoint (`ST`/`guard`), and end 0.05 s under their audio (`done`).
