#!/usr/bin/env python3
"""
build_batch.py — Build all ruben-substack articles as claude-liam reels.

Phases (run all by default, or pick one with --phase):
  beats  — generate beat_sheet.json via Claude API
  audio  — run kokoro am_onyx for each reel
  tsx    — write timing JSON + TSX + public symlink
  root   — update Root.tsx + tsc check
  render — render all compositions to final-cut.mp4

Usage (from any dir):
  python3 build_batch.py [--phase {all,beats,audio,tsx,root,render}] [--slug <slug>] [--force-beats]
"""
import argparse
import json
import math
import os
import re
import subprocess
import sys
from pathlib import Path

BOOK     = Path(__file__).resolve().parent
YOUTUBE  = BOOK / "youtube"
REMOTION = BOOK.parent / "brutalist-art" / "runtime" / "remotion"
SCRIPTS  = REMOTION.parent / "scripts"
MANIFEST = BOOK / "manifest.json"
YOUTUBE.mkdir(exist_ok=True)

GREETINGS = [
    "Hola", "Olá", "Bonjour", "Ciao", "Hallo", "Hej", "Annyeong",
    "Namaste", "Merhaba", "Shalom", "Salaam", "Jambo", "Sawadee",
    "Halo", "Konnichiwa", "Vanakkam", "Aloha", "Yassou", "Privet",
    "Talofa", "Bula", "Kumusta", "Selam",
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def slug_to_component(slug: str) -> str:
    return "".join(w.capitalize() for w in re.split(r"[-_]", slug))

def frames(duration_s: float) -> int:
    return math.ceil((duration_s + 0.4) * 30)

def bt(s) -> str:
    """Wrap a value in a JS backtick template literal (safe for JSX prop values)."""
    s = str(s)
    s = s.replace("\\", "\\\\")
    s = s.replace("`", "\\`")
    s = s.replace("${", "\\${")
    s = s.replace("\n", "\\n")
    s = s.replace("\r", "")
    return f"`{s}`"

def extract_text(local_file: str) -> str:
    from bs4 import BeautifulSoup
    p = BOOK / local_file
    if not p.exists():
        return ""
    soup = BeautifulSoup(p.read_text(), "html.parser")
    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)[:6000]

# ── Beat-sheet generation ─────────────────────────────────────────────────────

BEAT_SYSTEM = """You author beat sheets for "claude-liam" explainer reels in Brutalist video format.
Brand: Claude desktop app skin (cream #FAF9F5 page, terracotta #D97757 spark, EB Garamond serif).
Narrator: Liam (kokoro am_onyx), stand-in for Bear on @NikBearBrown. Register: Teardown (Feynman x MKBHD).

LAWS:
• COLD OPEN LAW: B00 = ClaudeComposerAsk. Narration opens: "this is Liam, in for Bear." then hooks with the article's core tension. greeting = "<hello>, Liam"
• ILLUSTRATE LAW: Claude UI only where UI is the subject. Inner beats ILLUSTRATE with ClaudeWindow (breakdowns/verdicts), SlateBeat/DOCUMENT (screenshot slots), ClaudeCodeBeat (actual code/configs/prompts).
• SPARK-LINE LAW: every beat has a sparkLine — 4 words max, the beat's key sentence distilled.
• HANDOFF LAW: second-to-last = ClaudeComposerAsk, greeting "Your turn.", command = a specific ready-to-paste prompt, runningText "paste this into Claude..."
• OUTRO LAW: last beat = ClaudeTitleOutro. Title restates article title.

BEAT COUNT: 8 beats (B00-B07) for <2000w; 9 beats (B00-B08) for 2000-3500w; 10 beats (B00-B09) for >3500w.

PATTERNS + required props:
• ClaudeComposerAsk: greeting, topic, segment, command, runningText, folderLabel="@NikBearBrown"
• ClaudeWindow: view="artifact", artifactTitle, artifactHeading, artifactLines (array of 3-4 strings), sparkLine
• ClaudeCodeBeat: title (a filename like "skill.md" or "prompt.txt"), code (raw text, use \\n for newlines), sparkLine
• SlateBeat DOCUMENT: shot.type="DOCUMENT", shot.source="own", shot.slot="media/B0X.png", shot.sparkLine, shot.slotNote="SLOT — fill media/B0X.png (what to screenshot)"

NARRATION: 80-150 words per beat (8-15 seconds). Faithful to source; honest about trade-offs. No filler.

OUTPUT: Respond with ONLY a valid JSON object. No markdown fences, no explanation.

Schema:
{
  "metadata": {
    "title": "...",
    "slug": "...",
    "topic": "RUBEN · SHORT_TOPIC",
    "brand": "claude-liam",
    "persona": "Liam",
    "voice": "Liam",
    "engine": "kokoro",
    "voice_kokoro": "am_onyx",
    "in_for_bear": true,
    "greeting": "..., Liam",
    "folderLabel": "@NikBearBrown",
    "register": "Teardown"
  },
  "beats": [
    {
      "beat_id": "B00",
      "act": "COLD-OPEN",
      "narration_text": "this is Liam, in for Bear. ...",
      "shot": {
        "type": "GRAPHIC",
        "source": "remotion",
        "remotion": {
          "pattern": "ClaudeComposerAsk",
          "props": { "greeting": "..., Liam", "topic": "RUBEN · ...", "segment": "...", "command": "...", "runningText": "...", "folderLabel": "@NikBearBrown" }
        }
      }
    }
  ]
}"""


def generate_beat_sheet(client, post: dict, greeting: str, text: str) -> dict:
    import anthropic
    user_msg = (
        f"Article slug: {post['slug']}\n"
        f"Title: {post['title']}\n"
        f"Subtitle: {post.get('subtitle', '')}\n"
        f"Word count: {post.get('wordcount', 0)}\n"
        f"Greeting for B00: {greeting}, Liam\n\n"
        f"Article text:\n{text}"
    )
    resp = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        system=BEAT_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )
    raw = resp.content[0].text.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw.strip())
    return json.loads(raw)

# ── TSX generator ─────────────────────────────────────────────────────────────

def beat_to_case(beat: dict) -> str:
    bid = beat["beat_id"]
    shot = beat.get("shot", {})

    if shot.get("type") == "DOCUMENT":
        narr = beat.get("narration_text", "")
        note = shot.get("slotNote", f"fill media/{bid}.png")
        spark = shot.get("sparkLine", "")
        return (
            f"      case '{bid}':\n"
            f"        content = (\n"
            f"          <SlateBeat\n"
            f"            beatId={{{bt(bid)}}}\n"
            f"            narration={{{bt(narr)}}}\n"
            f"            slotNote={{{bt(note)}}}\n"
            f"            sparkLine={{{bt(spark)}}}\n"
            f"          />\n"
            f"        );\n"
            f"        break;\n"
        )

    rem = shot.get("remotion", {})
    pattern = rem.get("pattern", "")
    props = rem.get("props", {})

    if pattern == "ClaudeComposerAsk":
        return (
            f"      case '{bid}':\n"
            f"        content = (\n"
            f"          <ClaudeComposerAsk {{...claudeComposerAskSchema.parse({{\n"
            f"            greeting: {bt(props.get('greeting',''))},\n"
            f"            topic: {bt(props.get('topic',''))},\n"
            f"            segment: {bt(props.get('segment',''))},\n"
            f"            command: {bt(props.get('command',''))},\n"
            f"            runningText: {bt(props.get('runningText',''))},\n"
            f"            folderLabel: {bt(props.get('folderLabel','@NikBearBrown'))},\n"
            f"          }})}} />\n"
            f"        );\n"
            f"        break;\n"
        )

    if pattern == "ClaudeWindow":
        lines = props.get("artifactLines", [])
        lines_str = ",\n              ".join(bt(l) for l in lines)
        return (
            f"      case '{bid}':\n"
            f"        content = (\n"
            f"          <ClaudeWindow {{...claudeWindowSchema.parse({{\n"
            f"            view: {bt(props.get('view','artifact'))},\n"
            f"            artifactTitle: {bt(props.get('artifactTitle',''))},\n"
            f"            artifactHeading: {bt(props.get('artifactHeading',''))},\n"
            f"            artifactLines: [{lines_str}],\n"
            f"            sparkLine: {bt(props.get('sparkLine',''))},\n"
            f"          }})}} />\n"
            f"        );\n"
            f"        break;\n"
        )

    if pattern == "ClaudeCodeBeat":
        return (
            f"      case '{bid}':\n"
            f"        content = (\n"
            f"          <ClaudeCodeBeat {{...claudeCodeBeatSchema.parse({{\n"
            f"            title: {bt(props.get('title','script.py'))},\n"
            f"            code: {bt(props.get('code',''))},\n"
            f"            sparkLine: {bt(props.get('sparkLine',''))},\n"
            f"          }})}} />\n"
            f"        );\n"
            f"        break;\n"
        )

    if pattern == "ClaudeTitleOutro":
        return (
            f"      case '{bid}':\n"
            f"        content = (\n"
            f"          <ClaudeTitleOutro {{...claudeTitleOutroSchema.parse({{\n"
            f"            title: {bt(props.get('title',''))},\n"
            f"            handle: {bt(props.get('handle','@NikBearBrown'))},\n"
            f"            subline: {bt(props.get('subline',''))},\n"
            f"          }})}} />\n"
            f"        );\n"
            f"        break;\n"
        )

    return (
        f"      case '{bid}':\n"
        f"        content = <AbsoluteFill style={{{{ background: CLAUDE.PAGE }}}} />;\n"
        f"        break;\n"
    )


TSX_TEMPLATE = """\
import React from 'react';
import {{ AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, spring }} from 'remotion';
import TIMING from './{slug}-timing.json';
import {{ ClaudeComposerAsk, claudeComposerAskSchema }} from './scenes/ClaudeComposerAsk';
import {{ ClaudeCodeBeat, claudeCodeBeatSchema }} from './scenes/ClaudeCodeBeat';
import {{ ClaudeWindow, claudeWindowSchema }} from './scenes/ClaudeWindow';
import {{ ClaudeTitleOutro, claudeTitleOutroSchema }} from './scenes/ClaudeTitleOutro';
import {{ CLAUDE, CLAUDE_FONT }} from './tokens/claude';

const SERIF = CLAUDE_FONT.serif;
const SANS  = CLAUDE_FONT.ui;

const SlateBeat: React.FC<{{
  beatId: string; narration: string; slotNote: string; sparkLine: string;
}}> = ({{ beatId, narration, slotNote, sparkLine }}) => {{
  const frame = useCurrentFrame();
  const fps = 30;
  const cardIn = spring({{ frame, fps, config: {{ damping: 28, stiffness: 140, mass: 0.8 }} }});
  const sparkIn = spring({{ frame: frame - 20, fps, config: {{ damping: 28, stiffness: 140, mass: 0.8 }} }});
  const cl = (v: number, a: number, b: number) => Math.min(b, Math.max(a, v));
  return (
    <AbsoluteFill style={{{{
      background: '#2F2A26', alignItems: 'center', justifyContent: 'center',
      flexDirection: 'column', padding: '0 10%',
    }}}}>
      <div style={{{{ fontFamily: SANS, fontSize: 14, fontWeight: 700, letterSpacing: 3,
        textTransform: 'uppercase' as const, color: CLAUDE.SPARK,
        opacity: cl(cardIn, 0, 1), marginBottom: 24 }}}}>
        SLOT — {{beatId}} · production media pending
      </div>
      <div style={{{{ fontFamily: SERIF, fontSize: 108, fontWeight: 700, color: '#F3EBDD',
        letterSpacing: '-0.03em', lineHeight: 1,
        opacity: cl(cardIn, 0, 1), transform: `scale(${{cl(cardIn, 0, 1)}})` }}}}>
        {{beatId}}
      </div>
      <div style={{{{ fontFamily: SERIF, fontSize: 22, color: '#F3EBDD', textAlign: 'center',
        lineHeight: 1.5, marginTop: 28, maxWidth: 780, opacity: cl(cardIn * 0.9, 0, 1) }}}}>
        {{narration}}
      </div>
      <div style={{{{ fontFamily: SANS, fontSize: 15, color: CLAUDE.SPARK, marginTop: 20,
        textAlign: 'center', maxWidth: 680, opacity: cl(cardIn * 0.8, 0, 1) }}}}>
        PIPELINE → {{slotNote}}
      </div>
      <div style={{{{ position: 'absolute', bottom: '6%', left: 0, right: 0,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        gap: 10, opacity: cl(sparkIn, 0, 1) }}}}>
        <svg width={{18}} height={{18}} viewBox="0 0 24 24" style={{{{ flexShrink: 0 }}}}>
          {{Array.from({{ length: 8 }}, (_, i) => (
            <line key={{i}} x1={{12}} y1={{12}}
              x2={{12 + 10 * Math.cos((i * Math.PI) / 4 + 0.2)}}
              y2={{12 + 10 * Math.sin((i * Math.PI) / 4 + 0.2)}}
              stroke={{CLAUDE.SPARK}} strokeWidth={{3.2}} strokeLinecap="round" />
          ))}}
        </svg>
        <span style={{{{ fontFamily: SERIF, fontSize: 22, fontStyle: 'italic', color: '#F3EBDD' }}}}>
          {{sparkLine}}
        </span>
      </div>
    </AbsoluteFill>
  );
}};

const TIMED = TIMING.map((t) => ({{ ...t }}));
export const TOTAL_FRAMES = TIMED.reduce((a, b) => a + b.frames, 0);

export const {component}: React.FC = () => {{
  let at = 0;
  const seqs = TIMED.map((t) => {{
    const from = at;
    at += t.frames;
    let content: React.ReactNode = null;
    switch (t.id) {{
{cases}      default:
        content = <AbsoluteFill style={{{{ background: CLAUDE.PAGE }}}} />;
    }}
    return (
      <Sequence key={{t.id}} from={{from}} durationInFrames={{t.frames}}>
        {{content}}
        <Audio src={{staticFile(t.audio)}} />
      </Sequence>
    );
  }});
  return <AbsoluteFill style={{{{ background: CLAUDE.PAGE }}}}>{{seqs}}</AbsoluteFill>;
}};
"""


def write_tsx(slug: str, component: str, beats: list):
    cases = "".join(beat_to_case(b) for b in beats)
    tsx = TSX_TEMPLATE.format(slug=slug, component=component, cases=cases)
    path = REMOTION / "src" / f"{component}.tsx"
    path.write_text(tsx)
    print(f"  [tsx] {path.name}")

# ── Root.tsx update ───────────────────────────────────────────────────────────

IMPORT_COMMENT = "// ── ruben-substack batch ──"
COMP_COMMENT   = "      {/* ── ruben-substack batch ── */}"

def update_root_tsx(entries):
    root = REMOTION / "src" / "Root.tsx"
    content = root.read_text()

    # Imports
    if IMPORT_COMMENT not in content:
        import_lines = "\n".join(
            f"import {{{comp}, TOTAL_FRAMES as {comp}_FRAMES}} from './{comp}';"
            for _, comp in entries
        )
        # Insert after cowork-setup import line
        anchor = "import {CoworkSetup, TOTAL_FRAMES as CoworkSetup_FRAMES} from './CoworkSetup';"
        idx = content.find(anchor)
        if idx != -1:
            idx = content.find("\n", idx) + 1
        else:
            # Fallback: after last import block line
            idx = content.rfind("\nimport ")
            idx = content.find("\n", idx + 1) + 1
        content = content[:idx] + f"{IMPORT_COMMENT}\n{import_lines}\n" + content[idx:]

    # Compositions
    if COMP_COMMENT not in content:
        comp_lines = "\n".join(
            f'      <Composition id="{comp}" component={{{comp}}} durationInFrames={{{comp}_FRAMES}} fps={{30}} width={{1280}} height={{720}} />'
            for _, comp in entries
        )
        content = content.replace(
            "    </>",
            f"    {COMP_COMMENT}\n{comp_lines}\n    </>"
        )

    root.write_text(content)
    print(f"  [root] {len(entries)} compositions registered")

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["all","beats","audio","tsx","root","render"], default="all")
    ap.add_argument("--slug")
    ap.add_argument("--force-beats", action="store_true")
    a = ap.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    posts = manifest["posts"]
    if a.slug:
        posts = [p for p in posts if p["slug"] == a.slug]

    # ── BEATS ─────────────────────────────────────────────────────────────────
    if a.phase in ("all", "beats"):
        import anthropic
        client = anthropic.Anthropic()
        for i, post in enumerate(posts):
            slug = post["slug"]
            reel_dir = YOUTUBE / slug
            reel_dir.mkdir(exist_ok=True)
            bs_path = reel_dir / "beat_sheet.json"
            if bs_path.exists() and not a.force_beats:
                print(f"[beats] skip {slug}")
                continue
            print(f"[beats] {slug} ({i+1}/{len(posts)})...")
            text = extract_text(post["local_file"])
            greeting = GREETINGS[i % len(GREETINGS)]
            try:
                bs = generate_beat_sheet(client, post, greeting, text)
                bs_path.write_text(json.dumps(bs, indent=2))
                (reel_dir / "PEDAGOGY.md").write_text(
                    f"# PEDAGOGY — {slug}\n\nVERDICT: PASS\n\n(kokoro — no spend gate)\n"
                )
                print(f"  ok  {len(bs['beats'])} beats")
            except Exception as e:
                print(f"  ERROR: {e}")

    # ── AUDIO ─────────────────────────────────────────────────────────────────
    if a.phase in ("all", "audio"):
        for post in posts:
            slug = post["slug"]
            reel_dir = YOUTUBE / slug
            if (reel_dir / "mp3" / "timings.json").exists():
                print(f"[audio] skip {slug}")
                continue
            if not (reel_dir / "beat_sheet.json").exists():
                print(f"[audio] skip {slug} (no beat sheet)")
                continue
            print(f"[audio] {slug}...")
            try:
                subprocess.run(
                    ["python3", str(SCRIPTS / "generate_audio_kokoro.py"),
                     str(reel_dir), "--no-gate"],
                    check=True
                )
                print(f"  ok")
            except subprocess.CalledProcessError as e:
                print(f"  ERROR: {e}")

    # ── TSX ───────────────────────────────────────────────────────────────────
    if a.phase in ("all", "tsx"):
        for post in posts:
            slug = post["slug"]
            comp = slug_to_component(slug)
            reel_dir = YOUTUBE / slug
            timings_path = reel_dir / "mp3" / "timings.json"
            bs_path = reel_dir / "beat_sheet.json"

            if not timings_path.exists() or not bs_path.exists():
                print(f"[tsx] skip {slug} (missing audio/beat sheet)")
                continue

            print(f"[tsx] {slug} → {comp}")
            bs = json.loads(bs_path.read_text())
            timings = json.loads(timings_path.read_text())
            beats = bs["beats"]

            # Timing JSON
            timing_data = [
                {"id": b["beat_id"],
                 "frames": frames(timings.get(b["beat_id"], 10.0)),
                 "audio": f"{slug}-mp3/beat-{b['beat_id']}.mp3"}
                for b in beats
            ]
            (REMOTION / "src" / f"{slug}-timing.json").write_text(
                json.dumps(timing_data, indent=2)
            )

            # TSX
            write_tsx(slug, comp, beats)

            # Symlink
            sym = REMOTION / "public" / f"{slug}-mp3"
            if not sym.exists():
                sym.symlink_to(reel_dir / "mp3")
                print(f"  [sym] public/{slug}-mp3")

    # ── ROOT ──────────────────────────────────────────────────────────────────
    if a.phase in ("all", "root"):
        entries = []
        for post in posts:
            slug = post["slug"]
            comp = slug_to_component(slug)
            if (REMOTION / "src" / f"{comp}.tsx").exists():
                entries.append((slug, comp))
            else:
                print(f"[root] skip {slug} (no tsx)")
        if entries:
            update_root_tsx(entries)

        print("[tsc] checking...")
        r = subprocess.run(["npx", "tsc", "--noEmit"], cwd=REMOTION,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"[tsc] ERRORS:\n{r.stdout[-2000:]}\n{r.stderr[-1000:]}")
            sys.exit(1)
        else:
            print("[tsc] clean")

    # ── RENDER ────────────────────────────────────────────────────────────────
    if a.phase in ("all", "render"):
        for post in posts:
            slug = post["slug"]
            comp = slug_to_component(slug)
            reel_dir = YOUTUBE / slug
            out = reel_dir / "media" / "final-cut.mp4"
            if out.exists():
                print(f"[render] skip {slug}")
                continue
            if not (REMOTION / "src" / f"{comp}.tsx").exists():
                print(f"[render] skip {slug} (no tsx)")
                continue
            out.parent.mkdir(exist_ok=True)
            print(f"[render] {slug}...")
            r = subprocess.run(
                ["npx", "remotion", "render", "src/index.ts", comp, str(out),
                 "--scale=1.5", "--concurrency=1"],
                cwd=REMOTION, capture_output=True, text=True
            )
            if r.returncode != 0:
                print(f"  ERROR:\n{r.stderr[-600:]}")
            else:
                mb = out.stat().st_size // 1024 // 1024
                print(f"  ok  {mb}MB")


if __name__ == "__main__":
    main()
