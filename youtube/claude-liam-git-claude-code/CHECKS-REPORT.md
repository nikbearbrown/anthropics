# CHECKS-REPORT.md — claude-liam-git-claude-code
# Written BEFORE first slate compile (per deep-explainer PROOF GATE requirement)

## Beat classification (body beats B02–B14, 15 total)

| Beat | Lane | Classification | Notes |
|---|---|---|---|
| B02 | CARD | CARD | Segment marker, no factual claim |
| B03 | REMOTION | SHOW | GitHubRepoHero shows real repo; tagline "210 files · 47k lines · 0 src/" verified |
| B04 | MANIM | SHOW | B04_StructureMap; all 6 bar values verified from find+uniq-c |
| B05 | MANIM | SHOW | B05_FolderTree; real dir list; "✗ src/ NOT FOUND" verified |
| B05b | MANIM | SHOW | B05b_ScriptFiles; 5 TS filenames verified from find *.ts |
| B06 | CARD | CARD | Segment marker |
| B07 | MANIM | SHOW | B07_VelocityChart; 353 verified; ~2/day labeled as estimate with ~ |
| B08 | REMOTION | SHOW | GitHubCodeViewer; real CHANGELOG.md lines, v2.1.219, verbatim |
| B09 | CARD | CARD | Segment marker |
| B10 | MANIM | SHOW | B10_ChurnChart; verified monthly breakdown in REPO-VERIFY.md |
| B11 | REMOTION | SHOW | FormACard with verified 222/176/46 counters |
| B11b | REMOTION | SHOW | FormACard listing real human commit subjects (verified from git log) |
| B12 | CARD | CARD | Segment marker |
| B13 | REMOTION | SHOW | GitHubCodeViewer; real stop-hook.sh, first 18 lines verbatim |
| B14 | REMOTION | SHOW | GitHubCodeDiff; commit 843297f verified via git show |

**Total body beats:** 15  
**SHOW:** 11  
**justified-HOLD:** 0  
**CARD:** 4  
**PUNT-flagged:** 0

---

## Teaching arc

| Criterion | Status | Evidence |
|---|---|---|
| FRAMEWORK beat before examples | ✓ | B01 BLUF establishes "compiled binary / public surface" frame before any detail |
| WORKED EXAMPLE | ✓ | B13 (real code) + B14 (real diff) are concrete worked examples |
| FALSIFIABILITY | ✓ | B04/B05 — "no src/" claim is testable: clone the repo and run `find . -maxdepth 1` |
| SCAFFOLDED VIEWER TASK | ✓ | B16 YOUR TURN gives the exact shell commands to replicate on another repo |
| BOOKENDS | ✓ | B00 cold open, B15 verdict, B16 handoff, B17 outro |
| NO-SOURCE-NO-VERDICT | ✓ | Every number cites REPO-VERIFY.md; ~2 releases/day labeled as estimate |

**Teaching arc:** ALL ✓ — sheet is DONE

---

## Beat-mix histogram (body beats only)

| Lane | Count | Share | Target | Status |
|---|---|---|---|---|
| REMOTION | 6 | 40% | 30–45% | ✓ |
| MANIM | 5 | 33% | 25–40% | ✓ |
| CARD | 4 | 27% | remainder | ✓ |
| VOX | 0 | 0% | 20–25% | WARN — see BUILD-LOG.md |

VOX quota deviation: for a code-repo git-explainer with no archival stills needed,
the GitHub skin Remotion components (RepoHero, CodeViewer, CodeDiff) serve the
documentary-texture function that pantry stills serve in a historical doc.
Flagged and justified in BUILD-LOG.md.

---

## GATE P status

GATE P (narration review on animated slate) — **PENDING** — human must review
before any audio spend. Kokoro am_onyx is free and goes into the slate by default.
