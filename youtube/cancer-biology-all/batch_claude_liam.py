#!/usr/bin/env python3
"""
batch_claude_liam.py — Claude-Liam retrofit for all 11 cancer-biology-all videos.

For each video (run from books/):
  1. Creates liam/ subfolder with beat_sheet.json (Liam narrations, am_onyx voice)
  2. Runs kokoro audio generation → liam/mp3/
  3. Reads timings → writes <slug>-timing.json to remotion/src/
  4. Writes <ComponentName>.tsx to remotion/src/
  5. Creates public/<slug>-liam-mp3 → video/liam/mp3 symlink
  6. Updates Root.tsx (import + composition)

Usage:
  python3 cancer-biology-all/batch_claude_liam.py
  python3 cancer-biology-all/batch_claude_liam.py --skip-audio
  python3 cancer-biology-all/batch_claude_liam.py --skip-tsx
  python3 cancer-biology-all/batch_claude_liam.py --only cancer-disparities-zip-code
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
BOOKS_DIR   = Path(__file__).resolve().parent.parent
CANCER_DIR  = BOOKS_DIR / "cancer-biology-all" / "youtube"
TOOLKIT_DIR = BOOKS_DIR / "brutalist-art"
REMOTION    = TOOLKIT_DIR / "runtime" / "remotion"
SRC         = REMOTION / "src"
PUBLIC      = REMOTION / "public"
KOKORO_SCRIPT = TOOLKIT_DIR / "runtime" / "scripts" / "generate_audio_kokoro.py"

# ── Per-video data ─────────────────────────────────────────────────────────────
VIDEOS = [
    {
        "slug":      "cancer-disparities-zip-code",
        "component": "CancerDisparitiesZipCode",
        "greeting":  "Salaam, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Cancer Disparities",
        "b01_spark": "40% gap — biology alone doesn’t explain it.",
        "b04_spark": "The causal chain, counted.",
        "b06_spark": "Scaled interventions — what actually works.",
        "b07_artifact_title": "Cancer disparities — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "Biology explains some of the gap but not most of it.",
            "Triple-negative breast cancer is more common in Black women — that is real.",
            "But when researchers control for stage and treatment quality, the biological disadvantage shrinks.",
            "The remaining gap is structural — and addressable: screening access, financial toxicity, trial equity.",
        ],
        "b07_spark": "Structure closes the gap. Biology alone doesn’t.",
    },
    {
        "slug":      "cancer-dormancy-recurrence",
        "component": "CancerDormancyRecurrence",
        "greeting":  "Hola, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Cancer Dormancy",
        "b01_spark": "Disease-free for fifteen years. Then not.",
        "b04_spark": "Mechanisms, evidence, interventions — three panels.",
        "b06_spark": "Actionability rated. Trial evidence added.",
        "b07_artifact_title": "Cancer dormancy — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "The dormancy state is not passive — the cell actively suppresses growth via TGF-β and BMP.",
            "Those pathways are receptor-mediated and drugable.",
            "Blocking reactivation requires knowing WHEN the cell wakes — no reliable clinical marker exists.",
            "The intervention window is real but unmeasured.",
        ],
        "b07_spark": "Drugable pathways. Unmarked window.",
    },
    {
        "slug":      "car-t-solid-tumor-barrier",
        "component": "CarTSolidTumorBarrier",
        "greeting":  "Ciao, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "CAR-T Barriers",
        "b01_spark": "70–90% in leukemia. Near zero in solid tumors.",
        "b04_spark": "Response rates: high in blood, low in solid.",
        "b06_spark": "Solutions called. Phase status listed.",
        "b07_artifact_title": "CAR-T solid tumor barriers — the teardown, one page",
        "b07_artifact_heading": "Five barriers, five open problems",
        "b07_lines": [
            "The five barriers are separate unsolved engineering problems.",
            "A CAR-T that beats antigen heterogeneity still faces exhaustion.",
            "Progress requires solving all five simultaneously.",
            "The field is solving them independently — no single therapy has cleared all five.",
        ],
        "b07_spark": "Five problems. Must solve all five.",
    },
    {
        "slug":      "clonal-resistance-prediction",
        "component": "ClonalResistancePrediction",
        "greeting":  "Hej, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Clonal Resistance",
        "b01_spark": "Resistant cells predate the drug.",
        "b04_spark": "The resistance decision tree — EGFR to C797S.",
        "b06_spark": "ctDNA window: 3–6 months before imaging.",
        "b07_artifact_title": "Clonal resistance prediction — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "The resistance clone is always there first — selected, not created.",
            "ctDNA gives a 3–6 month window before imaging progression.",
            "Three requirements: test ordered, interpreted correctly, next therapy available.",
            "Any one of the three fails the patient.",
        ],
        "b07_spark": "Three requirements. Any one fails the patient.",
    },
    {
        "slug":      "ctdna-mrd-detection",
        "component": "CtdnaMrdDetection",
        "greeting":  "Jambo, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "ctDNA MRD",
        "b01_spark": "Clean scan, positive ctDNA — act now.",
        "b04_spark": "Evidence tier, by cancer type.",
        "b06_spark": "Cost and coverage — added to the matrix.",
        "b07_artifact_title": "ctDNA MRD detection — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "The test works: ctDNA detects MRD months before imaging.",
            "The clinical question: does acting on that detection improve survival?",
            "DYNAMIC said yes for colorectal cancer (Tie et al. 2022, NEJM).",
            "Every other cancer type: pending.",
        ],
        "b07_spark": "Detection solved. Acting on it isn’t.",
    },
    {
        "slug":      "metastatic-cascade-bottleneck",
        "component": "MetastaticCascadeBottleneck",
        "greeting":  "Annyeong, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Metastatic Cascade",
        "b01_spark": "A million shed. Almost none metastasize.",
        "b04_spark": "One million to five — the funnel.",
        "b06_spark": "Every bottleneck, every intervention.",
        "b07_artifact_title": "Metastatic cascade bottlenecks — the teardown, one page",
        "b07_artifact_heading": "Where the math says the opportunity is",
        "b07_lines": [
            "Approved therapies target macrometastasis — the last step.",
            "Earlier bottlenecks already kill most cells — the opportunity is there.",
            "The math: 10⁶ shed per day, ≈5 establish — three steps before clinical detection.",
            "Challenge: building a trial around a step that precedes measurable disease.",
        ],
        "b07_spark": "Approved drugs hit step ten. Step two is open.",
    },
    {
        "slug":      "neoantigen-vaccine-pipeline",
        "component": "NeoantigenaVaccinePipeline",
        "greeting":  "Vanakkam, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Neoantigen Vaccines",
        "b01_spark": "mRNA-4157: teaching immune recognition.",
        "b04_spark": "Biopsy to dose — times and failure rates.",
        "b06_spark": "Pipeline attrition — cumulative loss per stage.",
        "b07_artifact_title": "Neoantigen vaccine pipeline — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "The vaccine works when it reaches the patient.",
            "30% attrition from biopsy to first dose — the real barrier is logistics.",
            "This is not a vaccine failure. It is a pipeline failure.",
            "The biology is solved. The supply chain is not.",
        ],
        "b07_spark": "Attrition, not biology, is the wall.",
    },
    {
        "slug":      "oncolytic-virotherapy",
        "component": "OncolyticVirotherapy",
        "greeting":  "Bonjour, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Oncolytic Virotherapy",
        "b01_spark": "T-VEC: engineered herpes, FDA-approved.",
        "b04_spark": "OPTiM versus systemic delivery — compared.",
        "b06_spark": "Systemic pipeline: virus, target, phase.",
        "b07_artifact_title": "Oncolytic virotherapy — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "T-VEC converts cold tumors to hot — forcing antigen release and immune recruitment in situ.",
            "The effect reaches uninjected distant lesions — the abscopal response.",
            "Ceiling: immune-excluded tumors that block recruitment entirely.",
            "Systemic delivery remains unsolved; intratumoral injection limits reach.",
        ],
        "b07_spark": "Cold → hot → abscopal. The mechanism.",
    },
    {
        "slug":      "pfs-surrogate-endpoint",
        "component": "PfsSurrogateEndpoint",
        "greeting":  "Merhaba, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "PFS Surrogate",
        "b01_spark": "Tumor shrank. Patient didn’t live longer.",
        "b04_spark": "PFS versus OS — the translation gap.",
        "b06_spark": "OS co-primary — positive, negative, untested.",
        "b07_artifact_title": "PFS as surrogate endpoint — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "PFS: tumor shrinks or holds. OS: patient lives longer.",
            "These are not the same question.",
            "Treating PFS as OS proxy requires biological rationale — often absent.",
            "PFS improved, OS unchanged: scan timing extended, not life.",
        ],
        "b07_spark": "Two different questions. Treated as one.",
    },
    {
        "slug":      "pre-metastatic-niche",
        "component": "PreMetastaticNiche",
        "greeting":  "Aloha, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Pre-Metastatic Niche",
        "b01_spark": "The tumor preps the liver before it arrives.",
        "b04_spark": "The exosome address system, mapped.",
        "b06_spark": "Anti-integrin block. Kaplan 2005 evidence.",
        "b07_artifact_title": "Pre-metastatic niche — the teardown, one page",
        "b07_artifact_heading": "What the evidence shows",
        "b07_lines": [
            "Block niche formation before metastatic cells arrive — eliminate the landing zone.",
            "The niche forms before any detectable metastatic lesion.",
            "Therapy must be given to patients who appear disease-free.",
            "Intervention window: widest before the first metastatic cell lands.",
        ],
        "b07_spark": "Eliminate the landing zone. Not the cells.",
    },
    {
        "slug":      "tumor-heterogeneity-tracerx",
        "component": "TumorHeterogeneityTracerx",
        "greeting":  "Yassou, Liam",
        "topic":     "CANCER BIOLOGY",
        "segment":   "Tumor Heterogeneity",
        "b01_spark": "One biopsy. 40% of the tumor, unseen.",
        "b04_spark": "Trunk versus branch — one biopsy captures one branch.",
        "b06_spark": "ctDNA + multi-region. The complete map.",
        "b07_artifact_title": "Tumor heterogeneity — the teardown, one page",
        "b07_artifact_heading": "What TRACERx showed",
        "b07_lines": [
            "The tumor is a population of competing clones, not a single entity.",
            "A single biopsy captures one corner of that population.",
            "TRACERx: trunk mutations present in every cell — better targets than subclonal ones.",
            "Subclonal targets spare the rest. The trunk is the shared weakness.",
        ],
        "b07_spark": "Target the trunk. Miss the branch.",
    },
]

# ── Helpers ────────────────────────────────────────────────────────────────────

def slug_to_public_name(slug):
    return f"{slug}-liam-mp3"

def strip_claude_command(cmd: str) -> str:
    """Strip the 'claude "..."' wrapper from a terminal command string."""
    m = re.match(r'^claude\s+"(.*)"$', cmd, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.match(r"^claude\s+'(.*)'$", cmd, re.DOTALL)
    if m:
        return m.group(1).strip()
    return cmd.strip()

def tsx_str(s: str) -> str:
    """Escape a string for use as a TSX single-quoted prop value."""
    s = s.replace("\\", "\\\\")
    s = s.replace("'", "\\'")
    return f"'{s}'"

def tsx_backtick(s: str) -> str:
    """Escape a string for use as a TSX backtick template literal."""
    s = s.replace("\\", "\\\\")
    s = s.replace("`", "\\`")
    s = s.replace("${", "\\${")
    return f"`{s}`"

def frames_for(duration_s: float) -> int:
    return math.ceil((duration_s + 0.4) * 30)


# ── Step 1: Prepare liam/ folder ───────────────────────────────────────────────

def prepare_liam_folder(video: dict, bs: dict) -> Path:
    slug = video["slug"]
    liam_dir = CANCER_DIR / slug / "liam"
    liam_dir.mkdir(exist_ok=True)
    (liam_dir / "mp3").mkdir(exist_ok=True)

    # Build the claude-liam beat sheet
    liam_bs = json.loads(json.dumps(bs))  # deep copy
    liam_bs["metadata"]["voice"] = "Liam"
    liam_bs["metadata"]["voice_id"] = "am_onyx"
    liam_bs["metadata"]["voice_kokoro"] = "am_onyx"
    liam_bs["metadata"]["style_preset"] = "claude-liam"
    liam_bs["metadata"].pop("voice_kokoro_old", None)

    greeting = video["greeting"]

    for beat in liam_bs["beats"]:
        bid = beat["beat_id"]
        beat["audio_file"] = f"mp3/beat-{bid}.mp3"

        if bid == "B00":
            orig = beat["narration_text"]
            # Strip "Nik Bear Brown." prefix
            hook = re.sub(r'^Nik Bear Brown\.\s*', '', orig).strip()
            beat["narration_text"] = f"{greeting}. This is Liam, in for Bear. {hook}"

        elif bid == "B09":
            beat["narration_text"] = "Liam, in for Bear. Build it, then take it apart."

    liam_bs_path = liam_dir / "beat_sheet.json"
    liam_bs_path.write_text(json.dumps(liam_bs, indent=2, ensure_ascii=False))
    print(f"  [prep] {slug}/liam/beat_sheet.json written")
    return liam_dir


# ── Step 2: Generate kokoro audio ──────────────────────────────────────────────

def run_kokoro(liam_dir: Path):
    cmd = [
        sys.executable, str(KOKORO_SCRIPT),
        str(liam_dir),
        "--no-gate",
    ]
    print(f"  [kokoro] running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False, text=True)
    if result.returncode != 0:
        print(f"  [ERROR] kokoro failed for {liam_dir}", file=sys.stderr)
        return False
    return True


# ── Step 3: Read timings ───────────────────────────────────────────────────────

def read_timings(liam_dir: Path) -> dict:
    timings_path = liam_dir / "mp3" / "timings.json"
    if not timings_path.exists():
        # Fall back: read actual_duration_s from liam beat_sheet.json
        bs = json.loads((liam_dir / "beat_sheet.json").read_text())
        return {b["beat_id"]: b.get("actual_duration_s", 8.0) for b in bs["beats"]}
    return json.loads(timings_path.read_text())


# ── Step 4: Write timing JSON ──────────────────────────────────────────────────

def write_timing_json(video: dict, timings: dict):
    slug = video["slug"]
    public_name = slug_to_public_name(slug)
    beat_ids = ["B00", "B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09"]
    timing_list = []
    for bid in beat_ids:
        dur = timings.get(bid, 8.0)
        timing_list.append({
            "id": bid,
            "frames": frames_for(dur),
            "audio": f"{public_name}/beat-{bid}.mp3",
        })
    out_path = SRC / f"{slug}-timing.json"
    out_path.write_text(json.dumps(timing_list, indent=2))
    print(f"  [timing] {out_path.name} written ({sum(t['frames'] for t in timing_list)} total frames)")
    return timing_list


# ── Step 5: Write TSX composition ─────────────────────────────────────────────

SLATE_BEAT_COMPONENT = '''
// ── Slate for DOCUMENT beats ──────────────────────────────────────────────────
const SlateBeat: React.FC<{
  beatId: string;
  narration: string;
  slotNote: string;
  sparkLine: string;
}> = ({ beatId, narration, slotNote, sparkLine }) => {
  const frame = useCurrentFrame();
  const fps = 30;
  const cardIn = spring({ frame, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const sparkIn = spring({ frame: frame - 20, fps, config: { damping: 28, stiffness: 140, mass: 0.8 } });
  const clamp = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));

  return (
    <AbsoluteFill style={{
      background: '#2F2A26',
      alignItems: 'center',
      justifyContent: 'center',
      flexDirection: 'column',
      padding: '0 10%',
    }}>
      <div style={{
        fontFamily: SANS,
        fontSize: 14,
        fontWeight: 700,
        letterSpacing: 3,
        textTransform: 'uppercase' as const,
        color: CLAUDE.SPARK,
        opacity: clamp(cardIn, 0, 1),
        marginBottom: 24,
      }}>
        SLOT — {beatId} · production media pending
      </div>
      <div style={{
        fontFamily: SERIF,
        fontSize: 108,
        fontWeight: 700,
        color: '#F3EBDD',
        letterSpacing: '-0.03em',
        lineHeight: 1,
        opacity: clamp(cardIn, 0, 1),
        transform: `scale(${clamp(cardIn, 0, 1)})`,
      }}>
        {beatId}
      </div>
      <div style={{
        fontFamily: SERIF,
        fontSize: 22,
        color: '#F3EBDD',
        textAlign: 'center',
        lineHeight: 1.5,
        marginTop: 28,
        maxWidth: 780,
        opacity: clamp(cardIn * 0.9, 0, 1),
      }}>
        {narration}
      </div>
      <div style={{
        fontFamily: SANS,
        fontSize: 15,
        color: CLAUDE.SPARK,
        marginTop: 20,
        textAlign: 'center',
        maxWidth: 680,
        opacity: clamp(cardIn * 0.8, 0, 1),
      }}>
        PIPELINE → {slotNote}
      </div>
      <div style={{
        position: 'absolute',
        bottom: '6%',
        left: 0,
        right: 0,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 10,
        opacity: clamp(sparkIn, 0, 1),
      }}>
        <svg width={18} height={18} viewBox="0 0 24 24" style={{ flexShrink: 0 }}>
          {Array.from({ length: 8 }, (_, i) => (
            <line key={i} x1={12} y1={12}
              x2={12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}
              y2={12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}
              stroke={CLAUDE.SPARK} strokeWidth={3.2} strokeLinecap="round" />
          ))}
        </svg>
        <span style={{
          fontFamily: SERIF,
          fontSize: 22,
          fontStyle: 'italic',
          color: '#F3EBDD',
        }}>
          {sparkLine}
        </span>
      </div>
    </AbsoluteFill>
  );
};
'''

def write_tsx(video: dict, bs: dict, timing_list: list):
    slug       = video["slug"]
    component  = video["component"]
    greeting   = video["greeting"]
    topic      = video["topic"]
    segment    = video["segment"]

    beats = {b["beat_id"]: b for b in bs["beats"]}

    # ── B00 command: topic hook (strip "Nik Bear Brown." prefix)
    b00_orig = beats["B00"]["narration_text"]
    b00_hook = re.sub(r'^Nik Bear Brown\.\s*', '', b00_orig).strip()
    b00_running = "reading the research…"

    # ── B02 command and runningText
    b02_props = beats["B02"].get("shot", {}).get("remotion", {}).get("props", {})
    b02_cmd = strip_claude_command(b02_props.get("command", ""))
    b02_running = b02_props.get("runningText", "researching…")

    # ── B03 filename and code
    b03_props = beats["B03"].get("shot", {}).get("remotion", {}).get("props", {})
    b03_filename = b03_props.get("filename", "script.py")
    b03_code = b03_props.get("code", "# code here")

    # ── B05 command and runningText
    b05_props = beats["B05"].get("shot", {}).get("remotion", {}).get("props", {})
    b05_cmd = strip_claude_command(b05_props.get("command", ""))
    b05_running = b05_props.get("runningText", "revising…")

    # ── B07 artifact data
    b07_title   = video["b07_artifact_title"]
    b07_heading = video["b07_artifact_heading"]
    b07_lines   = video["b07_lines"]
    b07_spark   = video["b07_spark"]

    # ── B08 handoff command
    b08_narration = beats["B08"]["narration_text"]

    # ── B09 ClaudeTitleOutro
    # Derive title from metadata title, take segment name
    title_words = segment  # use segment as the outro title
    b09_title = f"{segment}."

    # ── SlateBeat data
    b01_narration = beats["B01"]["narration_text"]
    b04_narration = beats["B04"]["narration_text"]
    b06_narration = beats["B06"]["narration_text"]

    b01_spark = video["b01_spark"]
    b04_spark = video["b04_spark"]
    b06_spark = video["b06_spark"]

    # Timing JSON filename
    timing_import = f"./{slug}-timing.json"
    public_name = slug_to_public_name(slug)

    lines = []
    lines.append("import React from 'react';")
    lines.append("import { AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, spring } from 'remotion';")
    lines.append(f"import TIMING from {tsx_str(timing_import)};")
    lines.append("import { ClaudeComposerAsk, claudeComposerAskSchema } from './scenes/ClaudeComposerAsk';")
    lines.append("import { ClaudeCodeBeat, claudeCodeBeatSchema } from './scenes/ClaudeCodeBeat';")
    lines.append("import { ClaudeWindow, claudeWindowSchema } from './scenes/ClaudeWindow';")
    lines.append("import { ClaudeTitleOutro, claudeTitleOutroSchema } from './scenes/ClaudeTitleOutro';")
    lines.append("import { CLAUDE, CLAUDE_FONT } from './tokens/claude';")
    lines.append("")
    lines.append("const SERIF = CLAUDE_FONT.serif;")
    lines.append("const SANS  = CLAUDE_FONT.ui;")
    lines.append(f"const TOPIC = {tsx_str(topic)};")
    lines.append(f"const SEGMENT = {tsx_str(segment)};")
    lines.append("const FOLDER = '@NikBearBrown';")
    lines.append("")
    lines.append(SLATE_BEAT_COMPONENT.strip())
    lines.append("")
    lines.append("// ── Timing ────────────────────────────────────────────────────────────────────")
    lines.append("const TIMED = TIMING.map((t) => ({ ...t }));")
    lines.append("export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);")
    lines.append("")
    lines.append("// ── Main composition ──────────────────────────────────────────────────────────")
    lines.append(f"export const {component}: React.FC = () => {{")
    lines.append("  let at = 0;")
    lines.append("")
    lines.append("  const seqs = TIMED.map((t) => {")
    lines.append("    const from = at;")
    lines.append("    at += t.frames;")
    lines.append("    let content: React.ReactNode = null;")
    lines.append("")
    lines.append("    switch (t.id) {")

    # B00 — ClaudeComposerAsk (cold open)
    lines.append("      // ── B00 — cold open ───────────────────────────────────────────────────────")
    lines.append("      case 'B00':")
    lines.append("        content = (")
    lines.append("          <ClaudeComposerAsk {...claudeComposerAskSchema.parse({")
    lines.append(f"            greeting: {tsx_backtick(greeting)},")
    lines.append("            topic: TOPIC,")
    lines.append("            segment: SEGMENT,")
    lines.append(f"            command: {tsx_backtick(b00_hook)},")
    lines.append(f"            runningText: {tsx_backtick(b00_running)},")
    lines.append("            folderLabel: FOLDER,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B01 — SlateBeat (problem)
    lines.append("      // ── B01 — THE-PROBLEM (SLOT) ─────────────────────────────────────────────")
    lines.append("      case 'B01':")
    lines.append("        content = (")
    lines.append("          <SlateBeat")
    lines.append("            beatId='B01'")
    lines.append(f"            narration={{{tsx_backtick(b01_narration)}}}")
    lines.append(f"            slotNote='fill media/B01.png'")
    lines.append(f"            sparkLine={{{tsx_backtick(b01_spark)}}}")
    lines.append("          />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B02 — ClaudeComposerAsk (The ask)
    lines.append("      // ── B02 — THE-ASK ────────────────────────────────────────────────────────")
    lines.append("      case 'B02':")
    lines.append("        content = (")
    lines.append("          <ClaudeComposerAsk {...claudeComposerAskSchema.parse({")
    lines.append("            greeting: 'The ask,',")
    lines.append("            topic: TOPIC,")
    lines.append("            segment: SEGMENT,")
    lines.append(f"            command: {tsx_backtick(b02_cmd)},")
    lines.append(f"            runningText: {tsx_backtick(b02_running)},")
    lines.append("            folderLabel: FOLDER,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B03 — ClaudeCodeBeat
    lines.append("      // ── B03 — THE-SCRIPT (ClaudeCodeBeat) ───────────────────────────────────")
    lines.append("      case 'B03':")
    lines.append("        content = (")
    lines.append("          <ClaudeCodeBeat {...claudeCodeBeatSchema.parse({")
    lines.append(f"            title: {tsx_backtick(b03_filename + ' — the count, not the claim')},")
    lines.append(f"            code: {tsx_backtick(b03_code)},")
    lines.append(f"            sparkLine: `The script does the counting.`,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B04 — SlateBeat (output)
    lines.append("      // ── B04 — THE-OUTPUT (SLOT) ──────────────────────────────────────────────")
    lines.append("      case 'B04':")
    lines.append("        content = (")
    lines.append("          <SlateBeat")
    lines.append("            beatId='B04'")
    lines.append(f"            narration={{{tsx_backtick(b04_narration)}}}")
    lines.append(f"            slotNote='fill media/B04.png'")
    lines.append(f"            sparkLine={{{tsx_backtick(b04_spark)}}}")
    lines.append("          />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B05 — ClaudeComposerAsk (revision ask)
    lines.append("      // ── B05 — THE-REVISION-ASK ───────────────────────────────────────────────")
    lines.append("      case 'B05':")
    lines.append("        content = (")
    lines.append("          <ClaudeComposerAsk {...claudeComposerAskSchema.parse({")
    lines.append("            greeting: 'The ask,',")
    lines.append("            topic: TOPIC,")
    lines.append("            segment: SEGMENT,")
    lines.append(f"            command: {tsx_backtick(b05_cmd)},")
    lines.append(f"            runningText: {tsx_backtick(b05_running)},")
    lines.append("            folderLabel: FOLDER,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B06 — SlateBeat (revised output)
    lines.append("      // ── B06 — THE-REVISED-OUTPUT (SLOT) ─────────────────────────────────────")
    lines.append("      case 'B06':")
    lines.append("        content = (")
    lines.append("          <SlateBeat")
    lines.append("            beatId='B06'")
    lines.append(f"            narration={{{tsx_backtick(b06_narration)}}}")
    lines.append(f"            slotNote='fill media/B06.png'")
    lines.append(f"            sparkLine={{{tsx_backtick(b06_spark)}}}")
    lines.append("          />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B07 — ClaudeWindow artifact (verdict)
    lines.append("      // ── B07 — VERDICT (ClaudeWindow artifact) ────────────────────────────────")
    lines.append("      case 'B07':")
    lines.append("        content = (")
    lines.append("          <ClaudeWindow {...claudeWindowSchema.parse({")
    lines.append("            view: 'artifact',")
    lines.append(f"            artifactTitle: {tsx_backtick(b07_title)},")
    lines.append(f"            artifactHeading: {tsx_backtick(b07_heading)},")
    lines.append("            artifactLines: [")
    for al in b07_lines:
        lines.append(f"              {tsx_backtick(al)},")
    lines.append("            ],")
    lines.append(f"            sparkLine: {tsx_backtick(b07_spark)},")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B08 — ClaudeComposerAsk (Your turn)
    lines.append("      // ── B08 — HANDOFF (Your turn.) ───────────────────────────────────────────")
    lines.append("      case 'B08':")
    lines.append("        content = (")
    lines.append("          <ClaudeComposerAsk {...claudeComposerAskSchema.parse({")
    lines.append("            greeting: 'Your turn.',")
    lines.append("            topic: TOPIC,")
    lines.append("            segment: SEGMENT,")
    lines.append(f"            command: {tsx_backtick(b08_narration)},")
    lines.append("            runningText: `paste this into Claude…`,")
    lines.append("            folderLabel: FOLDER,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    # B09 — ClaudeTitleOutro
    lines.append("      // ── B09 — OUTRO (ClaudeTitleOutro) ──────────────────────────────────────")
    lines.append("      case 'B09':")
    lines.append("        content = (")
    lines.append("          <ClaudeTitleOutro {...claudeTitleOutroSchema.parse({")
    lines.append(f"            title: {tsx_backtick(b09_title)},")
    lines.append("            handle: `@NikBearBrown`,")
    lines.append("            subline: `Liam, in for Bear · build it, then take it apart`,")
    lines.append("          })} />")
    lines.append("        );")
    lines.append("        break;")
    lines.append("")

    lines.append("      default:")
    lines.append("        content = <AbsoluteFill style={{ background: CLAUDE.PAGE }} />;")
    lines.append("    }")
    lines.append("")
    lines.append("    return (")
    lines.append("      <Sequence key={t.id} from={from} durationInFrames={t.frames}>")
    lines.append("        {content}")
    lines.append("        <Audio src={staticFile(t.audio)} />")
    lines.append("      </Sequence>")
    lines.append("    );")
    lines.append("  });")
    lines.append("")
    lines.append("  return (")
    lines.append("    <AbsoluteFill style={{ background: CLAUDE.PAGE }}>")
    lines.append("      {seqs}")
    lines.append("    </AbsoluteFill>")
    lines.append("  );")
    lines.append("};")
    lines.append("")

    tsx_content = "\n".join(lines)
    out_path = SRC / f"{component}.tsx"
    out_path.write_text(tsx_content)
    print(f"  [tsx] {component}.tsx written")


# ── Step 6: Create public symlink ──────────────────────────────────────────────

def create_symlink(video: dict):
    slug = video["slug"]
    PUBLIC.mkdir(exist_ok=True)
    link_name = slug_to_public_name(slug)
    link_path = PUBLIC / link_name
    target = CANCER_DIR / slug / "liam" / "mp3"
    if link_path.exists() or link_path.is_symlink():
        link_path.unlink()
    link_path.symlink_to(target)
    print(f"  [symlink] public/{link_name} → {target}")


# ── Step 7: Update Root.tsx ────────────────────────────────────────────────────

def update_root_tsx(videos_to_add: list):
    root_path = SRC / "Root.tsx"
    content = root_path.read_text()

    # Build import lines to add
    import_lines = []
    import_lines.append("// ── claude-liam — cancer-biology-all batch retrofit ──")
    for v in videos_to_add:
        component = v["component"]
        slug = v["slug"]
        var_frames = f"{component.upper()[:3]}_{component.upper()[-3:]}_FRAMES"
        import_lines.append(
            f"import {{{component}, TOTAL_FRAMES as {component}_FRAMES}} from './{component}';"
        )

    # Build composition JSX to add
    comp_lines = []
    comp_lines.append("      {/* ── claude-liam — cancer-biology-all batch retrofit ── */}")
    for v in videos_to_add:
        component = v["component"]
        comp_lines.append(f"      <Composition")
        comp_lines.append(f"        id={json.dumps(component)}")
        comp_lines.append(f"        component={{{component}}}")
        comp_lines.append(f"        durationInFrames={{{component}_FRAMES}}")
        comp_lines.append(f"        fps={{30}}")
        comp_lines.append(f"        width={{1280}}")
        comp_lines.append(f"        height={{720}}")
        comp_lines.append(f"      />")

    # Insert imports after the AdaptiveTherapyRevolution import line
    atr_import = "import {AdaptiveTherapyRevolution, TOTAL_FRAMES as ATR_TOTAL_FRAMES} from './AdaptiveTherapyRevolution';"
    new_imports = "\n".join(import_lines)

    if "cancer-biology-all batch retrofit" not in content:
        content = content.replace(
            atr_import,
            atr_import + "\n" + new_imports
        )

    # Insert compositions before the closing AdaptiveTherapyRevolution block
    atr_comp_block = """      {/* ── claude-liam — adaptive-therapy-revolution (full 11-beat reel) ── */}
      <Composition
        id="AdaptiveTherapyRevolution"
        component={AdaptiveTherapyRevolution}
        durationInFrames={ATR_TOTAL_FRAMES}
        fps={30}
        width={1280}
        height={720}
      />"""

    new_comps = "\n".join(comp_lines)
    if "cancer-biology-all batch retrofit" not in content:
        content = content.replace(
            atr_comp_block,
            atr_comp_block + "\n" + new_comps
        )

    root_path.write_text(content)
    print(f"  [root] Root.tsx updated with {len(videos_to_add)} compositions")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="restrict to these slugs")
    ap.add_argument("--skip-audio", action="store_true")
    ap.add_argument("--skip-tsx",   action="store_true")
    ap.add_argument("--skip-root",  action="store_true")
    args = ap.parse_args()

    videos = VIDEOS
    if args.only:
        videos = [v for v in videos if v["slug"] in args.only]
    if not videos:
        print("No videos to process (check --only filter)")
        return

    for video in videos:
        slug = video["slug"]
        print(f"\n{'='*60}")
        print(f"  {slug}")
        print(f"{'='*60}")

        bs_path = CANCER_DIR / slug / "beat_sheet.json"
        if not bs_path.exists():
            print(f"  [SKIP] No beat_sheet.json found")
            continue
        bs = json.loads(bs_path.read_text())

        # Step 1: Prepare liam/ folder
        liam_dir = prepare_liam_folder(video, bs)

        # Step 2: Generate audio
        if not args.skip_audio:
            ok = run_kokoro(liam_dir)
            if not ok:
                print(f"  [WARN] Audio generation failed, continuing...")

        # Step 3 & 4: Read timings and write timing JSON
        timings = read_timings(liam_dir)
        timing_list = write_timing_json(video, timings)

        # Step 5: Write TSX
        if not args.skip_tsx:
            write_tsx(video, bs, timing_list)

        # Step 6: Create symlink
        create_symlink(video)

    # Step 7: Update Root.tsx (once for all videos)
    if not args.skip_root:
        update_root_tsx(videos)

    print("\n[batch] Done. Run renders with:")
    for video in videos:
        slug = video["slug"]
        component = video["component"]
        out = CANCER_DIR / slug / "media" / "final-cut.mp4"
        print(f"  cd {REMOTION} && npx remotion render src/index.ts {component} {out} --scale=1.5 --concurrency=1")


if __name__ == "__main__":
    main()
