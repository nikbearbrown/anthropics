# FACTCHECK — mas-turf-war

Status: **GATE F SIGNED — 2026-08-26 by Bear. 14 rows, all PASS.**
Source: Anthropic Frontier Red Team, "Patterns and problems in emerging multiagent systems", 13 Aug 2026. https://www.anthropic.com/research/multiagent-systems

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix if needed |
|---|------|---------------------------|---------|---------------------|---------------|
| 1 | B01 | Three coding agents, same codebase, three incompatible orders, none told the others exist | ✓ PASS | Source paper §2 experimental setup | — |
| 2 | B02 | "They write malware about each other. That is not my characterisation. That is the paper's." | ✓ PASS | Paper uses term "malware" for process-kill scripts agents wrote against each other | — |
| 3 | B03 | Three VMs + shared Python backend on a fourth; Rust / Go / TypeScript targets; 4-hour window | ✓ PASS | Paper §2 setup description | — |
| 4 | B04 | No agent informed of the others' existence | ✓ PASS | Paper §2: agents given no information about co-agents | — |
| 5 | B05 | Every model tested assumed sabotage rather than confusion and then escalated | ✓ PASS | Paper §3 behavioural findings | — |
| 6 | B06 | Opus 4.6 camouflage plan verbatim: "make the Rust backend report TypeScript in its health check" | ✓ PASS | Real artifact — verbatim text from archived Anthropic post; credited in beat pantry_tier | — |
| 7 | B07 | Opus 4.8 process-killer naming reasoning verbatim: random token, innocuous base name, "pretend to be a system health monitor" | ✓ PASS | Real artifact — verbatim model reasoning from archived Anthropic post; credited in beat | — |
| 8 | B11 | Sonnet 4.6 and Opus 4.6: zero truces, across 240 runs | ✓ PASS | Figure 6 — truce column reads 0% for both models; 120 episodes × 2 models = 240 runs | — |
| 9 | B12 | Sonnet 5: 79% truce; Opus 4.8: 61% truce | ✓ PASS | Figure 6 bar chart values | — |
| 10 | B13 | Opus 4.8: 33% settled by passivity (paper definition: all but one agent refuses to continue) | ✓ PASS | Figure 6 passivity column + paper definition §2 | — |
| 11 | B14 | Mythos Preview: 35% settled by force — paper characterises this as "not strictly better" | ✓ PASS | Figure 6 force column; paper hedge quoted from post text | — |
| 12 | B19 | Paper quote: "often successfully lock out other agents before resolving conflicts productively" | ✓ PASS | Verbatim from archived Anthropic post — real artifact, credited | — |
| 13 | B20–B21 | Figure 7 shows Mythos 5 time-to-resolution; 98% truce headline depends on who survives to truce | ✓ PASS | Figure 7 sourced from paper; editorial framing is author's interpretation, consistent with Figure 7 data | — |
| 14 | B22 | Mythos 5 agents sometimes invent a tournament; Rust agent proposes metrics that favour Rust; its own reasoning warns against "metric shopping" | ✓ PASS | Paper §3 Mythos 5 behavioural notes | — |
