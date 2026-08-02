# Runbook — post the 6 Quantum Vol. 1 NotebookLM videos to @MedhavyAI

The skill is installed at `bear-textbooks/skills/notebooklm-youtube/`. Run everything
below **on your Mac** (it needs network for Whisper/ElevenLabs/YouTube and the Remotion
`node_modules`), from inside the notebooklm folder:
`books/quantum-mechanics-vol1/notebooklm/`.

## Proposed playlist order (chapter order)

The matcher confirms each of these automatically when you run it; this is the expected result.

| # | NotebookLM file | Chapter |
|---|-----------------|---------|
| 1 | `The_Forensic_Escalation__How_Physics_Broke.mp4` | Ch 1 — Why Classical Physics Failed |
| 2 | `The_Photoelectric_Effect___The_Photon.mp4` | Ch 1 — (photoelectric / the photon) |
| 3 | `The_Matter_Wave_Proof__Deconstructing_Quantum_Reality.mp4` | Ch 2 — Matter Waves |
| 4 | `Deriving_the_Quantum_Engine__From_the_TDSE_to_Stationary_States.mp4` | Ch 4 — The Schrödinger Equation |
| 5 | `Deriving_the_Infinite_Square_Well.mp4` | Ch 5 — The Infinite Square Well |
| 6 | `Building_the_Physical_Free_Particle__Superposition_and_Dispersi.mp4` | Ch 8 — The Free Particle & Wave Packets |

Two videos map to Ch 1 — that's fine, they sit adjacent.

## One-time setup

Install deps and set your keys:

```bash
pip install faster-whisper mutagen requests google-api-python-client google-auth-oauthlib google-auth-httplib2
export ELEVENLABS_API_KEY=sk_...your_key...
```

Then set up YouTube OAuth for @MedhavyAI following
`skills/notebooklm-youtube/references/youtube-setup.md`, and drop `client_secret.json`
into the notebooklm folder.

## Build all six (per video)

```bash
S=../../../skills/notebooklm-youtube/scripts
python "$S/pipeline.py" ./The_Forensic_Escalation__How_Physics_Broke.mp4 --chapters ../chapters
python "$S/pipeline.py" ./The_Photoelectric_Effect___The_Photon.mp4 --chapters ../chapters
python "$S/pipeline.py" ./The_Matter_Wave_Proof__Deconstructing_Quantum_Reality.mp4 --chapters ../chapters
python "$S/pipeline.py" ./Deriving_the_Quantum_Engine__From_the_TDSE_to_Stationary_States.mp4 --chapters ../chapters
python "$S/pipeline.py" ./Deriving_the_Infinite_Square_Well.mp4 --chapters ../chapters
python "$S/pipeline.py" ./Building_the_Physical_Free_Particle__Superposition_and_Dispersi.mp4 --chapters ../chapters
```

Each writes a `<slug>/` folder with the finished `mp4/<slug>.mp4`, `chapters.json`, and a
`<slug>-youtube.md` description draft. Check the chapter the matcher printed for each; if
one is wrong, re-run that line with `--chapter ../chapters/NN-*.md`.

## Refine each description, then flatten

Edit each `<slug>/<slug>-youtube.md` — rewrite the hook, the "What you'll learn" line,
"The physics" (keep the real numbers/equations), and every `<rewrite me>` chapter label —
then:

```bash
python "$S/build_description.py" ./<slug> --refresh
```

## Publish in chapter order

```bash
# preview — confirms auth + prints the order, uploads nothing:
python "$S/publish_playlist.py" --root . --dry-run

# real — uploads + adds to "Quantum Mechanics Volume 1 (NotebookLM)" in chapter order:
python "$S/publish_playlist.py" --root .
```

Videos post as **unlisted** by default (a fresh API project can't publish public until
Google's audit). Flip to `--privacy public` after the audit, or make them public in Studio.
The `publish_ledger.json` means re-running is safe — it skips anything already uploaded.
