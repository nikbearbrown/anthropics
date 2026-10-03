# Recursive show-tell beat-sheet loop

`./showtellloop.sh` now discovers existing beat sheets throughout `anthropics`
and converts them using the current `brutalist.art/skills/make/show-tell/SKILL.md`.
Each source gets a fresh Claude context with the full skill, parent skill and
schema example. The model rewrites narration and visual plans; the supervisor
checks the show-tell structure and writes the result. There is no Figma dependency.

```bash
./showtellloop.sh --dry --n 20         # inventory preview, no writes/model calls
./showtellloop.sh --once              # convert one pending sheet
./showtellloop.sh                     # convert the remaining discovered sheets
./showtellloop.sh --only claude-code  # restrict by source path substring
./showtellloop.sh --n 10              # at most ten attempts
./showtellloop.sh --status            # saved counts and worker status
./showtellloop.sh --retry-failed      # retry failed conversions
./showtellloop.sh --rebuild --once    # a new version, preserving previous output
```

An optional positional directory overrides the scan root; the default is the
script's directory, independent of the caller's working directory. Canonical
`beat_sheet.json` / `beat-sheet.json` and named `.json` variants are included.
Backup/pre-edit snapshots, archive directories, symlinks, dependencies and this
loop's own output/state are skipped. `--include-archives` includes archive trees.
Standard `beats` arrays and lecture `segments` arrays are supported. For lectures,
coverage indexes each original segment, retaining its nested beats and visual content.
Sheets already declaring show-tell are skipped. Malformed sheets are reported.
Each invocation takes one discovery snapshot; rerun to discover later additions.

Outputs live in `show-tell-conversions/<relative source folder>/<sheet stem>/<attempt>/`:
`beat_sheet.json`, a source snapshot, `coverage.json` mapping every original beat,
and `CONVERSION.md`. The original files are not modified. Outputs are marked
`sheet-converted-unrendered`: these are authored sheets, not finished films or
fact-checked/approved releases. Scenes, fresh audio, rendering and visual/audio
QC remain production work. Old audio paths, timings and completion stamps cannot
be carried through as evidence of a new build.

Resume state is `.showtell-convert/queue.json`; each attempt keeps its prompt,
raw response and stderr there. Source hashes detect changed inputs; output hashes
detect missing/modified converted sheets. A filesystem lock prevents two workers
on the same root and remains held by an in-flight child after a supervisor crash.
Do not run overlapping scan roots concurrently. Interrupt with Ctrl-C and rerun.
`--timeout` defaults to 1800 seconds per sheet; three consecutive failures halt
the loop. Failed items require `--retry-failed`; interrupted and account-blocked
items can resume with the normal command after the underlying issue is resolved.
Account/authentication errors stop immediately, without an overnight retry storm.

Uses Python 3 and the existing authenticated `claude` CLI/account. Claude usage
limits and any account billing still apply. No paid media API is used. The model
has no tools or MCP servers for this conversion: it returns structured JSON over
stdin/stdout and the supervisor writes only derived files. There is no permission
bypass, publishing, upload or Git push. `SHOWTELL_MODEL` selects the model and
`BRUTALIST_ART` overrides the skill root. `--claude` can select an executable for testing.

The earlier Figma film factory and its prompt remain available with an explicit
first argument `--queue`:

```bash
./showtellloop.sh --queue ../figma-for-educational-ai --once
```

That legacy mode retains its previous behavior and permissions; it is independent
of the new converter. An already running Figma worker is not stopped or relaunched.

Offline checks: `python3 -m unittest -v test_showtell_convert.py`.
