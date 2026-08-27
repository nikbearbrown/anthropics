# BATCH-PROMPT — CC/Cowork simulator conversion batch (22 reels)

Run the CC/Cowork simulator conversion batch defined in anthropics/youtube/CC-COWORK-BATCH-WORKLIST.json — all 22 reels, cowork block first, then claude-code block, FULLY AUTONOMOUS.

HARD RULE — NO QUESTIONS. Never stop to ask me anything, ever, for any reason. Every situation has a prescribed action: ambiguity → make the most reasonable call and log it in the report's DECISIONS column; a reel fails to build → mark FAILED with the reason and continue; a reel's narration can't be honestly carried by the kits → mark SKIPPED with the reason and continue; a tool errors twice → FAILED, continue. The run takes as long as it takes. I review each reel's slate cut individually, in its own folder, when the run is done.

The kits are in brutalist-art/runtime/remotion/src/scenes/ — Cowork* scenes (CoworkShell, CoworkComposer, CoworkTaskView, CoworkSideRail, CoworkSettings, CoworkMenu, CoworkFolderTree) and CC* scenes (CCShell, CCPromptBar, CCStatusVerb, CCToolCall, CCDiff, CCPlanCard, CCSession, CCThemePicker, CCWebHome), doctrine in scenes/CC-TEMPLATES.md and scenes/CODEX-TEMPLATES.md. Read both docs and each scene's demo defaultProps before converting anything.

Per reel, in worklist order:

1. Read its beat_sheet.json. NARRATION IS FROZEN — never rewrite a narration line.

2. Convert every slated body beat (build.status != VIDEO) to a kit scene chosen by what the narration DESCRIBES. Cowork reels: task delegated → CoworkComposer (typed ask) then CoworkTaskView (prompt/toolline/cardgrid/review blocks); progress/files → CoworkSideRail; settings/permissions/access levels → CoworkSettings or CoworkMenu (the access-ladder reel is settings + menu beats); checklists → CoworkTaskView review blocks with pass/warn/fail badges. Claude-code reels: session → CCSession (mascot:"auto" allowed); command/tool → CCToolCall; change → CCDiff; plan mode → CCPlanCard; thinking/status → CCStatusVerb; hooks/commands/slash content → CCSession blocks plus code-block (Onda) for real file contents. Derive every prop's content from that beat's own narration — never invent numbers, filenames, or product strings; chrome strings verbatim only. These are claude-code/claude-cowork topic reels: the UI is the subject, so ILLUSTRATE LAW is satisfied.

3. Bookends: keep existing ones untouched. Add any missing standard bookend (ClaudeComposerAsk cold open, ClaudeVerdictArtifact, Your Turn ClaudeComposerAsk, ClaudeTitleOutro) using the reel's existing narration/title only — a bookend with no narration gets the title restated, nothing invented.

4. Build: reuse existing mp3s where present (narration unchanged = audio still valid); generate Kokoro am_onyx for beats without audio; then remotion_scenes.py (foreground, --concurrency=1), compile.py.

5. Cuts — BOTH, kept: (a) the REVIEW CUT with audio and beat-id burn-in markers (./art run --review or the pipeline's review mode) saved as <slug>-review.mp4 in the reel folder — this is what I watch for feedback; (b) the clean master via ./art final.

6. QC, automated, no pauses: sample frames (ffmpeg fps=2 plus per-beat 15/50/85%), READ them against the 9-point rubric. Component-source defects get fixed ONCE in runtime/ and every already-built reel in this batch that used that scene gets re-rendered. Reel-level prop defects get fixed in that reel's sheet. GATE T per reel; TYPECHECK.md written. Log everything, ask nothing.

After both blocks:

7. Write anthropics/youtube/CC-COWORK-BATCH-REPORT.md: one row per reel — status (DONE/FAILED/SKIPPED), beats converted, review-cut path, master path, QC defects found/fixed, DECISIONS made without asking — plus a top section listing any component-source fixes made in runtime/ (those affect brutalist-art). Masters and review cuts stay in their folders. NOTHING staged, NOTHING to TOPOST, NOTHING uploaded.
