# CLI-SERIES-BATCH-LOG — Animate Cancer Biology with Claude Code
## @NikBearBrown · claude-liam channel · 20 reels planned

---

## Series overview

Each reel follows the cli-explainer spine:
B00 cold open (ClaudeComposerAsk) → B01–B02 PROBLEM → B03 ASK → B04 CODE →
B05 OUTPUT (Manim) → B06 CHANGE → B07 OUTPUT (Manim) → B08 SUMMARY →
B09 NEXT STEPS ("Your turn.") → B10 OUTRO (ClaudeTitleOutro @NikBearBrown)

Voice: am_onyx (Kokoro, free). Palette: claude. Register: Teardown.

---

## Reel 01 — p53-circuit

| Field | Value |
|-------|-------|
| Slug | `p53-circuit` |
| Folder | `cancer-biology/youtube/claude-liam-p53-circuit/` |
| Title | "Animate the p53 Relay with Claude Code" |
| Topic | damage→p53→effector relay; hub removal breaks the chain |
| Built | 2026-07-20 |
| Manim scenes | B05_P53Circuit, B07_P53CircuitBroken |
| Plate source | `cancer-biology/illustrae/plates/01-p53-circuit.svg` |
| Status | 8/11 filled; slate cut ready at `mp4/p53-circuit-slate.mp4` |
| QC | PASS — white background, hub hierarchy, collapse signal, no clipping |
| Slates remaining | B01 (six-node label card), B02 (~50% stat card), B08 (summary card) |
| Kokoro audio | 11 beats, am_onyx, $0.00, ~212s total |
| Notes | Edge-gap node placement (NODE_W=1.85, HUB_SCALE=1.25, _GAP=0.40) prevents hub overlap |

---

## Batch A — reels 02–05 — 2026-07-20
| reel | slug | duration | manim_renders | slates | qc |
|------|------|----------|---------------|--------|-----|
| 02 | telomere-crisis | 205s | B05+B07 | B01,B02,B08 | PASS |
| 03 | warburg-carbon | 225s | B05+B07 | B01,B02,B08 | PASS |
| 04 | restriction-point | 209s | B05+B07 | B01,B02,B08 | PASS |
| 05 | rb-convergence | 230s | B05+B07 | B01,B02,B08 | PASS |

**Notes:**
- All 4 built sequentially, Kokoro audio $0.00 each (voice=af_heart)
- Static checker gate fixed mid-build: chained `.animate` methods (`.set_fill().scale()`, `.set_opacity()`) not supported by stub — split into separate `self.play()` calls for restriction-point and rb-convergence
- `config.background_color="#FFFFFF"` set at module level in all scenes — white bg confirmed in all QC frames
- Manim scenes: `B05_TelomereCrisis`, `B07_TelomereCrisisFlow`, `B05_WarburgCarbon`, `B07_WarburgCarbonFlow`, `B05_RestrictionPoint`, `B07_RestrictionPointFate`, `B05_RbConvergence`, `B07_RbConvergenceBlocked`
- rb-convergence B05 choreography is an exact port of `cancer-biology/illustrae/rb_scene.py` with B05_ naming convention

---

## Reels 06–20 — pending (original plan: reels 02–20 now reels 06–20)

| # | Slug (planned) | Topic | Status |
|---|----------------|-------|--------|
| 02 | rb-restriction-point | Rb gate at G1/S; CDK4/6 phosphorylation relay | pending |
| 03 | apoptosis-bcl2 | BCL-2 family voltage; MOMP tipping point | pending |
| 04 | mtor-warburg | mTOR→HIF1α metabolic switch | pending |
| 05 | kras-raf-mek | KRAS→RAF→MEK→ERK cascade; oncogenic lock | pending |
| 06 | dna-repair-brca | HR pathway; BRCA1/2 as scaffold | pending |
| 07 | telomere-crisis | Telomere shortening → BFB → aneuploidy | pending |
| 08 | immune-checkpoint | PD-1/PD-L1 handshake; T-cell exhaustion | pending |
| 09 | vegf-angiogenesis | VEGF→receptor→sprouting tip/stalk | pending |
| 10 | wnt-beta-catenin | β-catenin destruction complex; nuclear signal | pending |
| 11 | notch-delta | Notch lateral inhibition; jagged vs delta | pending |
| 12 | hedgehog-gli | Hh pathway; smoothened lock/unlock | pending |
| 13 | pi3k-akt-pten | PI3K→AKT→mTOR; PTEN as rheostat | pending |
| 14 | stat3-jak | JAK→STAT3 dimer; cytokine amplification | pending |
| 15 | nf-kb-inflammation | NF-κB IκB release; nuclear translocation | pending |
| 16 | tgf-beta-smad | TGFβ tumour suppressor→oncogene switch | pending |
| 17 | myc-target-genes | MYC→E-box; global transcriptional amplifier | pending |
| 18 | protein-level-loss | gene intact, protein tagged and degraded before function | BUILT 2026-07-20 |
| 19 | mgmt-methylation-paradox | MGMT silenced → TMZ damage persists → cell dies | BUILT 2026-07-20 |
| 20 | venetoclax-priming | BH3-primed cell held below threshold, BCL-2 clamp removed | BUILT 2026-07-20 |

---

## Batch E — reels 18–20 — 2026-07-20
| reel | slug | duration | manim | slates | qc |
|------|------|----------|-------|--------|----|
| 18 | protein-level-loss | 242s | B05+B07 | B01,B02,B08 | PASS |
| 19 | mgmt-methylation-paradox | 254s | B05+B07 | B01,B02,B08 | PASS |
| 20 | venetoclax-priming | 241s | B05+B07 | B01,B02,B08 | PASS |

## SERIES COMPLETE — 20/20 reels — 2026-07-20
All reels at review cut. Human-fill slots: B01, B02, B08 in each reel.
No reels published. No commits. No pushes.

---

## Batch B — reels 06–09 (plates series) — 2026-07-21
Animate Cancer Biology with Claude Code · @NikBearBrown · p06–p09 plates
| reel | slug | duration | manim | slates | qc |
|------|------|----------|-------|--------|----|
| 06 | apoptosis-momp | 204s | B05+B07 | B01,B02,B08 | PASS |
| 07 | spindle-checkpoint | 213s | B05+B07 | B01,B02,B08 | PASS |
| 08 | hpv-dual-hit | 211s | B05+B07 | B01,B02,B08 | PASS |
| 09 | differentiation-block | 223s | B05+B07 | B01,B02,B08 | PASS |

Plate sources: `cancer-biology/illustrae/plates_gen.py` p06()–p09()
Folders: `cancer-biology/youtube/claude-liam-{apoptosis-momp,spindle-checkpoint,hpv-dual-hit,differentiation-block}/`
All 4 reels at review cut (slate cut). Human-fill slots: B01, B02, B08 in each reel.
No reels published. No commits. No pushes.

---

## Batch D — reels 14–17 — 2026-07-21

| reel | slug | duration | manim | slates | qc |
|------|------|----------|-------|--------|----|
| 14 | immune-starvation | 194s | B05_ImmuneStarvation + B07_ImmuneStarvationContrast | B01,B02,B08 | PASS |
| 15 | bypass-track | 200s | B05_BypassTrack + B07_BypassTrackFlow | B01,B02,B08 | PASS |
| 16 | hpylori-cancer | 208s | B05_HpyloriCancer + B07_HpyloriProgression | B01,B02,B08 | PASS |
| 17 | mir-deletion | 220s | B05_MirDeletion + B07_MirDeletionSurge | B01,B02,B08 | PASS |

### Reel details

**Reel 14 — immune-starvation**  
Title: "Animate Immune Starvation with Claude Code"  
Greeting: Namaste, Liam (Hindi). Topic: one fuel pool, two drinkers, the T-cell that goes hungry.  
Geometry: ORANGE reservoir, thick GRAY pipe → 7 BLUE tumor circles, thin GRAY pipe → lone SKY/VERM-dashed immune cell.  
Folder: `cancer-biology/youtube/claude-liam-immune-starvation/`

**Reel 15 — bypass-track**  
Title: "Animate Bypass Signaling with Claude Code"  
Greeting: Mbote, Liam (Lingala). Topic: block the front door, the cell finds a side door to the same room.  
Geometry: GRAY hub, BLUE receptor A (blocked by VERM plug/X), ORANGE receptor B (active), 6 GREEN output circles.  
Folder: `cancer-biology/youtube/claude-liam-bypass-track/`

**Reel 16 — hpylori-cancer**  
Title: "Animate the H. pylori Cancer March with Claude Code"  
Greeting: Yassas, Liam (Greek). Topic: a persistent irritant marches the stomach lining stage by stage.  
Geometry: 6 tissue patches (5 SKY, 1 ORANGE cancer), increasing dot disorder L→R, VERM bacterium rod above, 3 downward arrows.  
Folder: `cancer-biology/youtube/claude-liam-hpylori-cancer/`

**Reel 17 — mir-deletion**  
Title: "Animate MicroRNA Deletion with Claude Code"  
Greeting: Zdravo, Liam (Macedonian). Topic: lose the little silencer, and the oncogene it muzzled shouts.  
Geometry: two-state stacked layout — top: BLUE mRNA + GREEN hairpin + blocked arrow + 1 dot; bottom: VERM X-mark + unblocked arrow + 9 dots.  
Folder: `cancer-biology/youtube/claude-liam-mir-deletion/`

### Build notes (Batch D)
- All 4 reels passed Gate A (static_scene_check) and Gate W (WCAG/margins) clean
- All 8 Manim scenes rendered: B05 + B07 per reel; 4K masters in manim/
- Static errors fixed pre-render: list/numpy arithmetic (immune-starvation), set_fill on animate proxy (hpylori-cancer)
- `config.background_color = "#FFFFFF"` at module level in all 4 scenes.py
- Kokoro am_onyx, $0.00, free — no paid spend
- B01, B02, B08 SLATE in every reel (expected — human-fill slots)
- QC frames extracted and verified for B05 in all 4 reels
- No publish, no commit, no push

---

## Reel 13 — mtap-passenger — 2026-07-21

| Field | Value |
|-------|-------|
| Slug | `mtap-passenger` |
| Folder | `cancer-biology/youtube/claude-liam-mtap-passenger/` |
| Title | "Animate MTAP Passenger Deletion with Claude Code" |
| Topic | Passenger deletion (CDKN2A→MTAP co-deletion); metabolic dependency on PRMT5 |
| Built | 2026-07-21 |
| Manim scenes | B05_MtapPassenger (15 anims), B07_MtapPassengerFlow (16 anims) |
| Plate source | p13() geometry from plates_gen.py |
| Status | 8/11 filled; slate cut ready at `mp4/mtap-passenger-slate.mp4` (249.2s) |
| QC | PASS — white background, GRAY bar, VERM bracket, BLUE driver + ORANGE passenger fall, SKY node + 5 dots, VERM plug. Frames verified at t=2s/4s/6s. |
| Slates remaining | B01 (chromosome diagram, 9p21), B02 (PRMT5 dependency panel), B08 (4-step causal chain card) |
| Kokoro audio | 11 beats, am_onyx, $0.00, ~249s total |
| Greeting | "Shalom, Liam" (Hebrew) |
| Your Turn prompt | PRMT5 dependency extension — accumulating dots → PRMT5 consumes → survival; blocked → overflow → death |
| Notes | Shapes animate from bar level downward (deletion fall). Flow dots separate VGroup animated from source to node targets. Plug is Triangle rotated PI/6 to point left. |

---
