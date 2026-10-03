# Source Details — claude-plugins-official--claude-liam-m5-onboard

Generated: 2026-09-05T11:09:00

## Reel
- Question: m5-onboard
- Family: claude-plugins-official
- Source sheet: /Users/nik/Documents/books/anthropics/claude-plugins-official/youtube/claude-liam-m5-onboard/beat_sheet.json

## Source Skill
- Path: /Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-plugins-official/plugins/cwc-makers/skills/m5-onboard/SKILL.md
- Name: m5-onboard
- Description: End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

## Capabilities To Name On Screen
- End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer
- Cardputer-Adv
- Stick) — detect on USB
- flash UIFlow 2.0 firmware
- and install the Claude Buddy MicroPython app bundle

## Constraints / Failure Modes
- How to invoke this from Claude Code's Bash tool. Do NOT call onboard.py as a foreground Bash command. The Bash tool captures output and does not stream it back to the…
- ### Relaying physical steps to the user (REQUIRED)
- The flash stage cannot proceed without a manual button press on native-USB boards — there is no software path. When the monitored log shows Enter download mode (or the…
- If the device reboots into UIFlow instead of going dark, tell the user G0 was released too early and to try again holding it longer. Do not move on, retry the script, or…
- Flash (flash.py) — esptool write_flash 0x0 <image> at 460800 baud for UART bridges, --no-stub at 115200 baud for native-USB S3 devices. 921600 fails intermittently on…
- ## Critical gotchas (baked into the scripts — do not second-guess)
- Native-USB ESP32-S3 boards (Cardputer, Cardputer-Adv, CoreS3) require a physical BtnG0+BtnRST dance to enter download mode. There is no software path. The chip has no…
- Do not unplug the device during FLASH. Especially on native USB. A mid-flash disconnect leaves the internal flash in an inconsistent state. Mask ROM is usually reachable…

## Procedure / Sequence
- No numbered procedure; treat this as reference guidance rather than a pipeline.

## Supporting Files And Signals
- Referenced: /flash/
- Referenced: cwc-makers
- Referenced: buddy/
- Referenced: /maker-setup
- Referenced: scripts/*.py
- Referenced: onboard/
- Referenced: --apps buddy
- Referenced: buddy/device/
- Referenced: onboard.py --apps buddy
- Referenced: install_apps.py --src buddy
- Signal: code block: bash

## Source Sections
- Where the scripts live
- When to use
- Which variant to assume
- The workflow
- Relaying physical steps to the user (REQUIRED)
- Stages
- Critical gotchas (baked into the scripts — do not second-guess)
- After provisioning (what the user sees on the device)
- Files
- Dependencies

## Batch Log Match
- Row: 53
- Canonical path: anthropics/claude-plugins-official/plugins/cwc-makers/skills/m5-onboard/SKILL.md
- MP4 path: anthropics/claude-plugins-official/youtube/claude-liam-m5-onboard/claude-liam-m5-onboard.mp4

## Redo Note
Use these details to replace generic body beats with concrete capability, constraint, procedure, and source-file beats.
