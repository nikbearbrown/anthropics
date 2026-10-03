# Pay Once for the Long Part

**What this is.** A 154-second show-tell explainer of prompt caching, from Anthropic's cookbook notebook `claude-cookbooks/misc/prompt_caching.ipynb`. A novel and a question ride a belt into Claude (a dark reader station). Caching is drawn as a bookmark clipped at the end of the prompt and a shelf where a copy of the read prompt waits, and a time meter shows the difference. Labels only; Liam's voice does the explaining. **Why.** Card #11 of the overnight batch 2 (`../show-tell-ideas.md`, "Batch 2 candidates"). Bear asked to "find the next 25 best candidates and do as many as you can" (2026-09-27). **Found.** Every claim matches the notebook, and current behaviour was confirmed against Anthropic's prompt-caching docs:
- Without caching, all ~187k tokens of *Pride and Prejudice* are processed on every call: 4.89 s in the notebook's run.
- Adding one top-level `cache_control` field puts the breakpoint on the last block. The first call still reads everything and writes it to the cache (4.28 s). The identical second call reads it from the cache (1.48 s, 3.3× faster in that run).
- In a conversation the breakpoint moves forward on its own, and after turn one nearly all input comes from the cache.
- Cache writes cost 1.25× the input price. Reads cost 0.1× in the notebook, and less on some newer models per the docs. That is the one CORRECTED claim.
- The start must match exactly, so a timestamp in front means a miss every call. The cache lives 5 minutes by default, refreshed on each hit; the notebook states this, contrary to the scout's note.
- You can place up to four explicit breakpoints yourself, but the notebook advises starting with automatic.

All numbers are attributed aloud to the notebook, and no model is named.

- The beats: the novel and question on the belt (B00); no cache, everything read, 4.89 s (B01); `cache_control`, the bookmark, the first write to the shelf, 4.28 s (B02); the same request again, off the shelf, 1.48 s and 3.3× (B03); a conversation, the bookmark moving forward (B04); the price columns: normal, write, read (B05); two rules: an exact start and a five-minute hourglass (B06); explicit bookmarks placed by hand, up to four (B07). Your turn: have Claude Code add top-level caching to calls that resend the same long context, keep that part first and unchanged, move anything that changes after it, and log the two cache usage fields. Then check that a second run shows cache reads, and that nothing changing sits before the long part.
- Built with the `show-tell` skill (`brutalist.art/skills/make/show-tell/`). `scenes.py` carries the pasted ISO KIT and the midpoint guard. "Bonjour" needed no re-voice.
- Master: `exports/landscape/show-tell-pay-once-for-the-long-part.mp4`, 3840×2160, 24 fps, 153.71 s, sha256 3de8f488…90efb358. All gates PASS (A, B, W, V, GATE T, F, bookend).
- Status: **built, not staged, not published.** Staging (`art post`) and publishing wait for Bear's word.
