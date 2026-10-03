#!/usr/bin/env python3
"""tts_greeting_fix.py — voice BIDEA with the Portuguese greeting said right.

Why: Kokoro's English G2P reads "Olá" as ɑːlˈɑː, which faster-whisper hears as "Allah"; plain "Ola"
comes out as ˈoʊlə ("OH-luh", stress on the wrong syllable). generate_audio_kokoro.py has no per-word
pronunciation override, so this reel-local script (after show-tell-claude-on-your-desk/tts_greeting_fix.py)
voices BIDEA with the SAME engine, voice and mp3 encoder, from the phonemized narration with the first word
swapped to oʊlˈɑː (oh-LAH; faster-whisper hears "Ola" in English and "Olá" in Portuguese).
narration_text stays "Olá." so captions spell the greeting correctly.
Run from books/:  python3 anthropics/youtube/show-tell-one-plugin-per-service/tts_greeting_fix.py
Toolkit is imported read-only; nothing under brutalist.art/ is changed.
"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[2] / "brutalist.art" / "runtime" / "scripts"))
import generate_audio_kokoro as g  # noqa: E402

BID = "BIDEA"
BAD, GOOD = "ɑːlˈɑː", "oʊlˈɑː"
sheet_p = HERE / "beat_sheet.json"
sheet = json.loads(sheet_p.read_text())
beat = next(b for b in sheet["beats"] if b["beat_id"] == BID)
text = beat["narration_text"]
assert text.startswith("Olá."), text
k = g.load_engine()
ph = k.tokenizer.phonemize(g.normalize_for_tts(text), "en-us")
assert ph.startswith(BAD), ph
ph = GOOD + ph[len(BAD):]
samples, sr = k.create(ph, voice=beat.get("voice") or "am_onyx", lang="en-us", is_phonemes=True)
out = HERE / "mp3" / f"beat-{BID}.mp3"
g.write_mp3(samples, sr, out)
dur = round(g.measure(out), 2)
beat["audio_file"] = f"mp3/beat-{BID}.mp3"
beat["actual_duration_s"] = dur
sheet_p.write_text(json.dumps(sheet, indent=2, ensure_ascii=False) + "\n")
tp = HERE / "mp3" / "timings.json"
t = json.loads(tp.read_text()) if tp.exists() else {}
t[BID] = dur
tp.write_text(json.dumps(t, indent=2) + "\n")
print(f"[greeting-fix] {out.name} {dur:.2f}s  phonemes start: {ph[:40]}")
