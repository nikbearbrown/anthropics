#!/usr/bin/env python3
"""One-shot rewriter for nbb-vox-endosomal-escape/beat_sheet.json.

Migrates old body-locked wrap (B_LIAM/B_BODY/B_VERDICT/B_YOUR_TURN/B_OUTRO plus
placeholder scaffold B00/B01/BVDT/BHTF/BOUT) into the canonical bookend pattern
used by nbb-vox-bystander-effect: B00 + B01-B11 body + BVDT + BHTF + BOUT.
Preserves LOCKED narrations from B_LIAM/B_VERDICT/B_YOUR_TURN verbatim.
Body narrations copied verbatim from source vox-endosomal-escape beat sheet.
"""
import json
from pathlib import Path

REEL = Path(__file__).parent
OLD = REEL / "beat_sheet.pre-rebuild.json"
SRC = REEL.parent / "vox-endosomal-escape" / "beat_sheet.json"
OUT = REEL / "beat_sheet.json"

with OLD.open() as f:
    old = json.load(f)
with SRC.open() as f:
    src = json.load(f)


def find(beats, bid):
    for b in beats:
        if b.get("beat_id") == bid:
            return b
    return None


b_liam = find(old["beats"], "B_LIAM")
b_verdict = find(old["beats"], "B_VERDICT")
b_your_turn = find(old["beats"], "B_YOUR_TURN")
b_outro = find(old["beats"], "B_OUTRO")

TITLE = old["metadata"]["title"]
SHORT = "The pH-Triggered Lock"

# Compressed short labels for FormACard body beats
BODY_LABELS = {
    "B01": "in vitro potent, in vivo inert — the delivery gap",
    "B02": "the wrong diagnosis — cargo swallowed and digested",
    "B03": "how does the ionizable lipid solve the endosomal trap?",
    "B04": "the sealed compartment where most cargo ends its life",
    "B05": "proton pumps acidify — the compartment turns hostile",
    "B06": "the charge flip — amine picks up a proton, goes positive",
    "B07": "positive lipid rips the anionic bilayer — cargo dumps out",
    "B08": "~1–2% escape — RNAi amplification does the rest",
    "B09": "same siRNA, two carriers — 8% vs 84% silencing (illustrative)",
    "B10": "no charge switch → cargo digested, drug fails",
    "B11": "the escape step, opened",
}


def body_beat(src_beat):
    bid = src_beat["beat_id"]
    return {
        "beat_id": bid,
        "act": src_beat.get("act", ""),
        "estimated_duration_s": src_beat.get("estimated_duration_s", 10),
        "narration_text": src_beat["narration_text"],
        "shot": {
            "type": "GRAPHIC",
            "source": "own",
            "motion": "drawon",
            "remotion": {
                "pattern": "FormACard",
                "provenance": "proven-core/FormACard",
                "version": "1",
                "props": {
                    "lines": [BODY_LABELS[bid]],
                    "dark": False,
                },
                "rendered": {"out": f"media/{bid}.mp4", "at": ""},
            },
        },
        "audio_file": f"mp3/beat-{bid}.mp3",
        "engine": "kokoro",
        "voice": "am_onyx",
        "voice_kokoro": "am_onyx",
    }


B00 = {
    "beat_id": "B00",
    "act": "COLD OPEN",
    "lane": "BOOKEND",
    "title": "Liam cold open — ClaudeComposerAsk",
    "engine": "kokoro",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "narration_text": b_liam["narration_text"],
    "shot": {
        "type": "CARD",
        "source": "remotion",
        "motion": "hold",
        "remotion": {
            "pattern": "ClaudeComposerAsk",
            "provenance": "proven-core/ClaudeComposerAsk",
            "version": "1",
            "props": {
                "command": b_liam["narration_text"],
                "topic": "CANCER NANOMEDICINE",
                "segment": "endosomal escape · the pH-triggered charge flip",
                "greeting": "Vanakkam, Liam",
                "runningText": "explaining the endosomal escape mechanism…",
                "output": [
                    "The cell packages the drug into an acidic bubble.",
                    "The ionizable lipid's charge flip breaks the bubble open.",
                    "That pH-triggered switch is what turns a liposome into a drug.",
                ],
                "folderLabel": "@NikBearBrown",
            },
            "rendered": {"out": "media/B00.mp4", "at": ""},
        },
    },
    "estimated_duration_s": 22.0,
    "audio_file": "mp3/beat-B00.mp3",
}


BVDT = {
    "beat_id": "BVDT",
    "act": "VERDICT",
    "lane": "BOOKEND",
    "engine": "kokoro",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "narration_text": b_verdict["narration_text"],
    "shot": {
        "type": "CARD",
        "source": "remotion",
        "motion": "hold",
        "remotion": {
            "pattern": "ClaudeVerdictArtifact",
            "provenance": "proven-core/ClaudeVerdictArtifact",
            "version": "1",
            "props": {
                "artifactTitle": "Endosomal Escape — the mechanism",
                "artifactHeading": "What the pH-triggered charge flip actually does",
                "artifactLines": b_verdict["shot"]["remotion"]["props"]["artifactLines"],
            },
            "rendered": {"out": "media/BVDT.mp4", "at": ""},
        },
    },
    "estimated_duration_s": 38.0,
    "audio_file": "mp3/beat-BVDT.mp3",
}


BHTF = {
    "beat_id": "BHTF",
    "act": "YOUR TURN",
    "lane": "BOOKEND",
    "engine": "kokoro",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "narration_text": b_your_turn["narration_text"],
    "shot": {
        "type": "CARD",
        "source": "remotion",
        "motion": "hold",
        "remotion": {
            "pattern": "ClaudeComposerAsk",
            "provenance": "proven-core/ClaudeComposerAsk",
            "version": "1",
            "props": {
                "command": b_your_turn["shot"]["remotion"]["props"]["command"],
                "topic": "CANCER NANOMEDICINE",
                "segment": "your turn · endosomal escape",
                "greeting": "Your turn.",
                "runningText": "paste this into Claude and push the escape fraction…",
                "output": [],
                "folderLabel": "@NikBearBrown",
            },
            "rendered": {"out": "media/BHTF.mp4", "at": ""},
        },
    },
    "estimated_duration_s": 7.0,
    "audio_file": "mp3/beat-BHTF.mp3",
}


BOUT = {
    "beat_id": "BOUT",
    "act": "OUTRO",
    "lane": "BOOKEND",
    "engine": "kokoro",
    "voice": "am_onyx",
    "voice_kokoro": "am_onyx",
    "silent": True,
    "silence_s": 5.0,
    "narration_text": TITLE,
    "shot": {
        "type": "CARD",
        "source": "remotion",
        "motion": "hold",
        "remotion": {
            "pattern": "ClaudeTitleOutro",
            "provenance": "proven-core/ClaudeTitleOutro",
            "version": "1",
            "props": {
                "title": TITLE,
                "handle": "@NikBearBrown",
                "subline": "neutral in blood, cationic in the endosome — that charge flip is the drug",
            },
            "rendered": {"out": "media/BOUT.mp4", "at": ""},
        },
    },
    "estimated_duration_s": 5.0,
    "audio_file": "mp3/beat-BOUT.mp3",
}


body = [body_beat(find(src["beats"], bid)) for bid in [f"B{i:02d}" for i in range(1, 12)]]

new = {
    "metadata": {
        "slug": "vox-endosomal-escape",
        "variant": "nbb",
        "nbb_slug": "nbb-vox-endosomal-escape",
        "title": TITLE,
        "short_title": SHORT,
        "topic": "CANCER NANOMEDICINE",
        "audience": "NikBearBrown",
        "channel_title": "@NikBearBrown",
        "folderLabel": "@NikBearBrown",
        "register": "Teardown",
        "palette": "claude",
        "engine": "kokoro",
        "voice": "am_onyx",
        "voice_kokoro": "am_onyx",
        "aspect_ratio": "16:9",
        "width": 1280,
        "height": 720,
        "fps": 24,
        "derived_from": "beat_sheet.pre-rebuild.json",
        "source_reel": "../vox-endosomal-escape",
        "source_beat_sheet": "../vox-endosomal-escape/beat_sheet.json",
        "note": "NBB wrap; canonicalized from the July-16 body-lock wrap (B_LIAM/B_BODY/B_VERDICT/B_YOUR_TURN/B_OUTRO) to the standard bookend pattern used by the sibling nbb-vox-* reels. Liam cold open, body from source vox-endosomal-escape beat narrations, verdict/handoff/outro from the July-16 authored wrap.",
    },
    "beats": [B00] + body + [BVDT, BHTF, BOUT],
}

with OUT.open("w") as f:
    json.dump(new, f, indent=1)

print("wrote", OUT, "beats:", [b["beat_id"] for b in new["beats"]])
