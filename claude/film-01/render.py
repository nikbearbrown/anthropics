#!/usr/bin/env python3
"""Standalone render pipeline — Meet Your Three Claudes (Film 1, Claude at Work).

Steps:
  1. Synthesize narration audio for all 16 beats (Kokoro am_onyx → audio/<ID>.mp3)
  2. Render 14 Manim scenes at 4K (manim/<SceneID>.mp4)
  3. Assemble: per-beat clips → review cut → clean master

M14 covers BVDT + BHTF + BOUT as one animation; their audio tracks are
concatenated and the video is freeze-padded to match the combined duration.
"""
import json, os, shutil, struct, subprocess, sys, tempfile, wave
from pathlib import Path

FILM_DIR = Path(__file__).parent.resolve()
BEAT_SHEET = FILM_DIR / "beat_sheet.json"
AUDIO_DIR = FILM_DIR / "audio"
MANIM_DIR = FILM_DIR / "manim"
CLIPS_DIR = FILM_DIR / "clips"
MP4_DIR = FILM_DIR / "mp4"

ART_HOME = Path("/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art")
KOKORO_MODEL = ART_HOME / "runtime/models/kokoro/kokoro-v1.0.onnx"
KOKORO_VOICES = ART_HOME / "runtime/models/kokoro/voices-v1.0.bin"

FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe") or "ffprobe"
SLUG = "claude-film-01-meet-your-three-claudes"

SCENE_CLASS = {
    "M01": "M01_Bidea",
    "M02": "M02_Bdefs",
    "M03": "M03_B01",
    "M04": "M04_B02",
    "M05": "M05_B03",
    "M06": "M06_B04",
    "M07": "M07_B05",
    "M08": "M08_B06",
    "M09": "M09_B07",
    "M10": "M10_B08",
    "M11": "M11_B09",
    "M12": "M12_B10",
    "M13": "M13_B11",
    "M14": "M14_BvdtHtfOut",
}


def sh(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        print(f"[FAIL] {' '.join(str(c) for c in cmd)}")
        print(r.stderr[-1200:])
        sys.exit(1)
    return r


def probe_dur(path):
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    return float(r.stdout.strip())


def probe_wh(path):
    r = subprocess.run(
        [FFPROBE, "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    try:
        w, h = r.stdout.strip().splitlines()[0].split(",")
        return int(w), int(h)
    except Exception:
        return None, None


def write_mp3(samples, sr, out_path):
    ints = [max(-32768, min(32767, int(s * 32767))) for s in samples]
    with tempfile.TemporaryDirectory(prefix=".tts-", dir=AUDIO_DIR) as scratch:
        tmp_wav = Path(scratch) / "audio.wav"
        tmp_mp3 = Path(scratch) / "audio.mp3"
        with wave.open(str(tmp_wav), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes(struct.pack(f"<{len(ints)}h", *ints))
        subprocess.run(
            [FFMPEG, "-y", "-v", "error", "-i", str(tmp_wav),
             "-c:a", "libmp3lame", "-q:a", "2", str(tmp_mp3)],
            check=True,
        )
        os.replace(tmp_mp3, out_path)


# ── Step 1: audio ────────────────────────────────────────────────────────────

def generate_audio(beats):
    AUDIO_DIR.mkdir(exist_ok=True)
    sys.path.insert(0, "/opt/homebrew/lib/python3.14/site-packages")
    from kokoro_onnx import Kokoro
    k = Kokoro(str(KOKORO_MODEL), str(KOKORO_VOICES))

    total_dur = 0.0
    for b in beats:
        bid = b["id"]
        out = AUDIO_DIR / f"{bid}.mp3"
        if out.exists() and out.stat().st_size > 0:
            dur = probe_dur(out)
            print(f"[audio] {bid}.mp3  {dur:.2f}s  (cached)")
            total_dur += dur
            continue
        text = b["line"]
        samples, sr = k.create(text, voice="am_onyx", speed=1.0, lang="en-us")
        write_mp3(samples, sr, out)
        dur = probe_dur(out)
        total_dur += dur
        print(f"[audio] {bid}.mp3  {dur:.2f}s")

    print(f"[audio] {len(beats)} files · total {total_dur:.1f}s ({total_dur/60:.1f}m)")
    return total_dur


# ── Step 2: Manim render ──────────────────────────────────────────────────────

def render_scene(scene_id):
    out = MANIM_DIR / f"{scene_id}.mp4"
    if out.exists() and out.stat().st_size > 0:
        dur = probe_dur(out)
        print(f"[manim] {scene_id}.mp4  {dur:.2f}s  (cached)")
        return out

    class_name = SCENE_CLASS[scene_id]
    print(f"[manim] rendering {scene_id} ({class_name}) at 4K …")

    work_dir = FILM_DIR / "_manim_work"
    work_dir.mkdir(exist_ok=True)
    cmd = [
        "python3", "-m", "manim", "render",
        "-qh",
        "-r", "3840,2160",
        "--media_dir", str(work_dir),
        str(FILM_DIR / "scenes.py"),
        class_name,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=str(FILM_DIR))
    if r.returncode != 0:
        print(f"[manim] FAILED {scene_id}")
        print(r.stderr[-1200:])
        sys.exit(1)

    found = list(work_dir.rglob(f"{class_name}.mp4"))
    if not found:
        print(f"[manim] ERROR: no output for {class_name}\n{r.stdout[-500:]}")
        sys.exit(1)

    shutil.move(str(found[0]), str(out))
    shutil.rmtree(work_dir, ignore_errors=True)

    dur = probe_dur(out)
    print(f"[manim] {scene_id}.mp4  {dur:.2f}s")
    return out


def render_all_scenes(beats):
    MANIM_DIR.mkdir(exist_ok=True)
    seen = set()
    for b in beats:
        sid = b["scene"]
        if sid not in seen:
            render_scene(sid)
            seen.add(sid)


# ── Step 3: clip assembly ─────────────────────────────────────────────────────

def concat_mp3s(paths, out_path):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for p in paths:
            f.write(f"file '{p}'\n")
        list_file = f.name
    try:
        sh([FFMPEG, "-y", "-v", "error",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-c:a", "libmp3lame", "-q:a", "2", str(out_path)])
    finally:
        os.unlink(list_file)


SCALE = "scale=3840:2160:flags=lanczos"  # upscale 1920×1080 → 4K

def mux_clip(video_path, audio_path, out_path):
    """Mux video + audio at 4K, freeze-padding video if shorter than audio."""
    v_dur = probe_dur(video_path)
    a_dur = probe_dur(audio_path)
    gap = a_dur - v_dur

    encode_flags = ["-c:v", "libx264", "-crf", "17", "-preset", "fast",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k"]

    if gap > 0.05:
        # scale first, then freeze-pad last frame to fill audio duration
        filt = f"[0:v]{SCALE},tpad=stop_mode=clone:stop_duration={gap:.3f}[vp]"
        sh([FFMPEG, "-y", "-v", "error",
            "-i", str(video_path), "-i", str(audio_path),
            "-filter_complex", filt,
            "-map", "[vp]", "-map", "1:a:0",
            *encode_flags, "-t", str(a_dur), str(out_path)])
    elif gap < -0.05:
        # scale + trim to audio length
        sh([FFMPEG, "-y", "-v", "error",
            "-i", str(video_path), "-i", str(audio_path),
            "-filter_complex", f"[0:v]{SCALE}[v]",
            "-map", "[v]", "-map", "1:a:0",
            *encode_flags, "-t", str(a_dur), str(out_path)])
    else:
        # scale + mux
        sh([FFMPEG, "-y", "-v", "error",
            "-i", str(video_path), "-i", str(audio_path),
            "-filter_complex", f"[0:v]{SCALE}[v]",
            "-map", "[v]", "-map", "1:a:0",
            *encode_flags, "-shortest", str(out_path)])

    dur = probe_dur(out_path)
    return dur


def assemble(beats):
    CLIPS_DIR.mkdir(exist_ok=True)
    MP4_DIR.mkdir(exist_ok=True)

    m14_beats = [b for b in beats if b["scene"] == "M14"]
    m14_ids = {b["id"] for b in m14_beats}

    ordered_clips = []
    m14_done = False

    for b in beats:
        bid = b["id"]
        if bid in m14_ids:
            if not m14_done:
                # One combined clip for all M14 beats
                combined_audio = CLIPS_DIR / "M14_audio.mp3"
                concat_mp3s([AUDIO_DIR / f"{b2['id']}.mp3" for b2 in m14_beats],
                            combined_audio)
                clip_out = CLIPS_DIR / "M14.mp4"
                dur = mux_clip(MANIM_DIR / "M14.mp4", combined_audio, clip_out)
                print(f"[clip]  M14.mp4  {dur:.2f}s  (BVDT+BHTF+BOUT combined)")
                ordered_clips.append(clip_out)
                m14_done = True
            # else: skip repeated M14 beats (already handled)
        else:
            clip_out = CLIPS_DIR / f"{bid}.mp4"
            dur = mux_clip(MANIM_DIR / f"{b['scene']}.mp4",
                           AUDIO_DIR / f"{bid}.mp3", clip_out)
            print(f"[clip]  {bid}.mp4  {dur:.2f}s")
            ordered_clips.append(clip_out)

    # Concatenate all clips into the master
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        for clip in ordered_clips:
            f.write(f"file '{clip}'\n")
        list_file = f.name

    try:
        master = MP4_DIR / f"{SLUG}.mp4"
        sh([FFMPEG, "-y", "-v", "error",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-c", "copy",
            str(master)])
    finally:
        os.unlink(list_file)

    return master


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    beats = json.loads(BEAT_SHEET.read_text())
    print(f"[render] Meet Your Three Claudes  ·  {len(beats)} beats  ·  "
          f"estimated {sum(b['dur_s'] for b in beats)}s")
    print()

    print("── Step 1: audio ──")
    total_audio = generate_audio(beats)

    print("\n── Step 2: Manim render ──")
    render_all_scenes(beats)

    print("\n── Step 3: assemble ──")
    master = assemble(beats)

    # Verify
    dur = probe_dur(master)
    w, h = probe_wh(master)
    audio_files = sorted(AUDIO_DIR.glob("*.mp3"))

    print(f"""
═══════════════════════════════════════
  RENDER COMPLETE
  beats:       {len(beats)}
  audio files: {len(audio_files)} ({', '.join(f.stem for f in audio_files[:4])}…)
  master:      {master}
  resolution:  {w}×{h}
  runtime:     {dur:.1f}s ({int(dur//60)}m{int(dur%60)}s)
═══════════════════════════════════════""")


if __name__ == "__main__":
    main()
