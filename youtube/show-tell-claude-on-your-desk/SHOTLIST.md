# SHOTLIST — show-tell-claude-on-your-desk

**What this is.** The typed work order, one row per beat. Show-tell style: one drawn isometric image per beat, labels only, Liam's voice explains. Measured narration total: 150.4 s (BOUT includes its 1.0 s tail). No pantry slots, no open requests.

| beat | lane | scene | image | s |
|---|---|---|---|---|
| BIDEA | bookend | `BrutalistHesitantWriter` | Types "How do I buy / a Claude desk buddy?", then corrects "buy" to "build". "Hej" greeting spoken over it. | 9.2 |
| BDEFS | bookend | `ClaudeDefinitions` | "Terms In This Film": BLE, permission prompt, reference repo. | 10.9 |
| B00 | manim | `B00_Desk` | A kraft desk slides up; a laptop drops onto it and its lid rises to a Claude window ("Claude"); a tiny upright device drops in beside it ("device"), its pet asleep; two session windows open; a dashed grey arc draws between them ("Bluetooth"). | 11.3 |
| B01 | manim | `B01_OptIn` | The arc greys out; a toggle on the laptop screen slides on ("developer mode"); the Hardware Buddy panel opens; a cursor clicks its dark Connect key; the device pulses and the arc redraws solid ink with terracotta ends, which pulse. | 12.1 |
| B02 | manim | `B02_Snapshot` | The camera steps in: laptop left, device enlarged right. Snapshot packets ride the arc ("snapshot"); three session panels appear, one with a terracotta "waiting" dot; transcript lines appear on the laptop and, after another packet, on the device's dark screen ("messages"); a new line slides in at the top and the oldest drops off. | 11.7 |
| B03 | manim | `B03_PetWakes` | "ESP32"; the pet breathes with its eyes closed ("asleep"); a new session window pops open on the laptop, a packet rides over, and the pet's eyes open ("awake"). | 8.0 |
| B04 | manim | `B04_Prompt` | A permission prompt card appears in the Claude window ("Bash"); a prompt packet rides to the top of the arc ("prompt"), then on to the device, where a light prompt block replaces the lines; the pet frowns and wiggles; the light on top blinks terracotta. | 11.7 |
| B05 | manim | `B05_Approve` | The front button presses in ("approve"); a reply packet rides back to the laptop and a "once" tag lands; the laptop's prompt gets a check, the light goes out, the lines return; the side button pulses ("deny"); the pet smiles and three hearts float up. | 11.0 |
| B06 | manim | `B06_Pairing` | Packets ride both ways; a grey dongle slides in and a dashed line reaches toward the arc ("dongle"); a passkey tag pops out of the device ("pass key") and a copy is typed into a field in the app; a padlock closes on the arc ("encrypted") as the dongle and its line disappear. | 15.9 |
| B07 | manim | `B07_Blueprint` | The arc and padlock go and the example device shrinks to the top corner; a blueprint sheet unrolls ("REFERENCE.md"); a maker's board rises onto it and draws its own arc to the laptop; one-line slips ride it both ways; a second board rises with its own arc; fork lines branch from the small example device to both boards ("fork"). | 17.6 |
| BHTF | bookend | `ClaudeComposerAsk` | The Claude.ai composer, "Your turn.": the plan-your-own-device prompt types in full, then two check lines. | 27.1 |
| BOUT | bookend | `ClaudeTitleOutro` | Title restates with @NikBearBrown; Liam reads the title, then "At Nik Bear Brown". | 3.9 |

Audio-first: the measured Kokoro mp3s are the clock. Scenes wait for their spoken phrases (`until`), hold every animation off the clip midpoint (`ST`/`guard`), and end 0.05 s under their audio (`done`).
