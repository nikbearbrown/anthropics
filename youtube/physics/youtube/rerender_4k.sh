#!/usr/bin/env bash
# Batch 4K Manim re-render for 4 physics reels.
# Renders each affected scene class at -qk (3840x2160), moves output to manim/<bid>.mp4.
set -uo pipefail
BOOKS="/Users/bear/Documents/CoWork/bear-textbooks/books"
LOG="$BOOKS/physics/youtube/rerender_4k.log"
: > "$LOG"

render_beat() {
    local reel="$1"
    local bid="$2"
    local cls="$3"
    local reel_dir="$BOOKS/$reel"
    echo "$(date '+%H:%M:%S') RENDER $reel $bid $cls" | tee -a "$LOG"
    cd "$reel_dir"
    rm -f "manim/$bid.mp4"
    manim -qk scenes.py "$cls" --progress_bar none 2>&1 | tee -a "$LOG" | tail -3
    # locate the rendered file
    local out
    out=$(find media/videos -name "${cls}.mp4" 2>/dev/null | head -1)
    if [ -z "$out" ]; then
        # fallback: any recent mp4 matching class name pattern
        out=$(find media/videos -name "*.mp4" -newer scenes.py 2>/dev/null | grep -v partial | tail -1)
    fi
    if [ -z "$out" ]; then
        echo "ERROR: no output found for $cls" | tee -a "$LOG"
        return 1
    fi
    cp "$out" "manim/$bid.mp4"
    local res
    res=$(ffprobe -v error -show_entries stream=width,height -of csv=p=0 "manim/$bid.mp4" 2>/dev/null)
    echo "$(date '+%H:%M:%S') OK $bid: $res" | tee -a "$LOG"
    cd "$BOOKS"
}

echo "=== PHASE 1: position-momentum-uncertainty (4 scenes) ===" | tee -a "$LOG"
render_beat physics/youtube/position-momentum-uncertainty H01 H01_Pinning
render_beat physics/youtube/position-momentum-uncertainty H02 H02_ShakingHead
render_beat physics/youtube/position-momentum-uncertainty A07 A07_Seesaw
render_beat physics/youtube/position-momentum-uncertainty A08 A08_BakedIntoWave

echo "=== PHASE 2: one-atom-farther-cuts-current-tenfold (10 scenes) ===" | tee -a "$LOG"
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold H01 H01_TipAndAtom
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold H02 H02_TipLifts
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A01 A01_TipAboveSurface
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A02 A02_TunnelLink
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A03 A03_ExponentialLadder
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A04 A04_TipTracing
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A05 A05_NeedleSwings
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A06 A06_TinyHeightBigSwing
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A07 A07_CurrentPeaksMapAtoms
render_beat physics/youtube/one-atom-farther-cuts-current-tenfold A08 A08_OneAtomCloserTenTimes

echo "=== PHASE 3: wave-leaks-into-forbidden-wall (4 scenes) ===" | tee -a "$LOG"
render_beat physics/youtube/wave-leaks-into-forbidden-wall H01 H01_BallRollsBack
render_beat physics/youtube/wave-leaks-into-forbidden-wall H02 H02_WaveGlows
render_beat physics/youtube/wave-leaks-into-forbidden-wall A05 A05_EvanescentTail
render_beat physics/youtube/wave-leaks-into-forbidden-wall A08 A08_WaveLeaksLabel

echo "=== PHASE 4: two-spots-not-a-smear-bb (24 scenes) ===" | tee -a "$LOG"
render_beat physics/youtube/two-spots-not-a-smear-bb INTRO INTRO_Title
render_beat physics/youtube/two-spots-not-a-smear-bb H01 H01_Apparatus
render_beat physics/youtube/two-spots-not-a-smear-bb H02 H02_OrientationFan
render_beat physics/youtube/two-spots-not-a-smear-bb H03 H03_ClassicalStreak
render_beat physics/youtube/two-spots-not-a-smear-bb H04 H04_TwoSpotsReveal
render_beat physics/youtube/two-spots-not-a-smear-bb H05 H05_TwoSpotsHold
render_beat physics/youtube/two-spots-not-a-smear-bb W01 W01_TiltAndPush
render_beat physics/youtube/two-spots-not-a-smear-bb W02 W02_ContinuousStreak
render_beat physics/youtube/two-spots-not-a-smear-bb W03 W03_TwoAllowedTilts
render_beat physics/youtube/two-spots-not-a-smear-bb W04 W04_TwoAnswerCard
render_beat physics/youtube/two-spots-not-a-smear-bb W05 W05_BornRuleHold
render_beat physics/youtube/two-spots-not-a-smear-bb S01 S01_TwoBoxesInSeries
render_beat physics/youtube/two-spots-not-a-smear-bb S02 S02_SelectUpBeam
render_beat physics/youtube/two-spots-not-a-smear-bb S03 S03_CertaintyUp
render_beat physics/youtube/two-spots-not-a-smear-bb S04 S04_SwitchToX
render_beat physics/youtube/two-spots-not-a-smear-bb S05 S05_FiftyCoinFlip
render_beat physics/youtube/two-spots-not-a-smear-bb S06 S06_CertainUncertain
render_beat physics/youtube/two-spots-not-a-smear-bb S07 S07_ChainExtendedZXZ
render_beat physics/youtube/two-spots-not-a-smear-bb S08 S08_XErasesZ
render_beat physics/youtube/two-spots-not-a-smear-bb S09 S09_MeasurementChain
render_beat physics/youtube/two-spots-not-a-smear-bb P01 P01_ClumsyAppStruckOut
render_beat physics/youtube/two-spots-not-a-smear-bb P02 P02_IncompatibilityCard
render_beat physics/youtube/two-spots-not-a-smear-bb P03 P03_SpotsReturn
render_beat physics/youtube/two-spots-not-a-smear-bb OUTRO OUTRO_Final

echo "=== ALL RENDERS DONE ===" | tee -a "$LOG"
echo "Check $LOG for details."
