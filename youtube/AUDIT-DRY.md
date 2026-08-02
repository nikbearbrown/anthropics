# AUDIT-DRY — anthropics/youtube/

**Date:** 2026-07-28  
**Reels audited:** 768  
**Errors (bad JSON or unreadable):** 0

## Aggregate Counts

| Metric | Count |
|--------|-------|
| Total reels | 768 |
| Schema v1 | 0 |
| Schema v2 | 768 |
| Reels with any banned card | 34 |
| Total banned card instances | 148 |
| — BC-1 (SlateCard) | 83 |
| — BC-2 (ClaudeWindow+artifact in body) | 19 |
| — BC-3 (eyebrow/kicker/headline in non-exempt) | 46 |
| — BC-4 (OutroSeries/OutroCTA) | 0 |
| Reels with FormBCard | 43 |
| — FormBCard with empty items[] | 0 |
| Reels with open bookend OK (ClaudeComposerAsk) | 336 / 768 |
| Reels with close bookend OK (ClaudeTitleOutro) | 670 / 768 |
| Reels with BOTH bookends OK | 336 / 768 |
| Reels with voice OK (am_onyx/kokoro) | 768 / 768 |
| Reels with unrendered Remotion boxes | 732 |
| Total unrendered Remotion boxes | 2654 |

## Summary Table

> Columns: schema, banned_count, has_formb, bookend_ok, voice_ok, remotion_box_count

| topic | reel | schema | banned | has_formb | bookend_ok | voice_ok | remotion_boxes |
|-------|------|--------|--------|-----------|-----------|---------|----------------|
| claude-cowork | nbb-vox-modal-upgrade | v2 | 28 | N | OK | OK | 6 |
| claude-cowork | vox-modal-upgrade | v2 | 28 | N | FAIL | OK | 4 |
| claude-cowork | claude-liam-vox-modal-upgrade | v2 | 24 | N | FAIL | OK | 2 |
| claude-plugins | claude-liam-installing-plugins | v2 | 5 | N | OK | OK | 5 |
| claude-cowork | claude-liam-access-ladder-explained | v2 | 4 | N | OK | OK | 7 |
| claude-cowork | claude-liam-productivity | v2 | 4 | N | OK | OK | 6 |
| claude-cowork | nbb-vox-format-credibility | v2 | 4 | N | OK | OK | 6 |
| claude-cowork | claude-liam-support | v2 | 4 | N | OK | OK | 5 |
| claude-plugins | claude-liam-combining-plugins | v2 | 4 | N | OK | OK | 4 |
| claude-cowork | vox-format-credibility | v2 | 4 | N | FAIL | OK | 4 |
| claude-plugins | claude-liam-building-plugins | v2 | 3 | N | OK | OK | 6 |
| claude-cowork | claude-liam-troubleshooting | v2 | 3 | N | OK | OK | 5 |
| claude-research | claude-liam-research | v2 | 3 | N | OK | OK | 5 |
| claude-cowork | claude-liam-data | v2 | 2 | N | OK | OK | 7 |
| claude-cowork | claude-liam-enterprise-search | v2 | 2 | N | OK | OK | 7 |
| claude-cowork | claude-liam-one-hour-on-cowork | v2 | 2 | N | OK | OK | 7 |
| claude-code | claude-api-one-endpoint-ladder | v2 | 2 | N | OK | OK | 6 |
| claude-cowork | claude-liam-marketing | v2 | 2 | N | OK | OK | 5 |
| claude-cowork | claude-liam-product | v2 | 2 | N | OK | OK | 5 |
| claude-cowork | claude-liam-sales | v2 | 2 | N | OK | OK | 5 |
| claude-plugins | claude-liam-what-plugins-are | v2 | 2 | N | OK | OK | 5 |
| claude-prompting | claude-liam-different-kind-of-wrong | v2 | 2 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-legal-finance | v2 | 1 | N | OK | OK | 6 |
| claude-prompting | claude-liam-agentic-approval-gate | v2 | 1 | N | OK | OK | 5 |
| behind-the-model | what-is-behind-the-model | v2 | 1 | N | OK | OK | 4 |
| claude-agent-skills | what-is-claude-agent-skills | v2 | 1 | N | OK | OK | 4 |
| claude-basics | what-is-claude-basics | v2 | 1 | N | OK | OK | 4 |
| claude-for-education | what-is-claude-for-education | v2 | 1 | N | OK | OK | 4 |
| claude-mcp-connectors | what-is-claude-mcp-connectors | v2 | 1 | N | OK | OK | 4 |
| claude-plugins | what-is-claude-plugins | v2 | 1 | N | OK | OK | 4 |
| claude-prompting | what-is-claude-prompting | v2 | 1 | N | OK | OK | 4 |
| claude-research | what-is-claude-research | v2 | 1 | N | OK | OK | 4 |
| claude-skills | what-is-claude-skills | v2 | 1 | N | OK | OK | 4 |
| claude-youtube | what-is-claude-youtube | v2 | 1 | N | OK | OK | 4 |
| behind-the-model | nbb-risk-tiered-verification | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-self-check-vs-independent-verification | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-solve-verify-asymmetry | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-supervision-calibration-logger | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-three-level-supervision-classifier | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-type-iii-error-detector | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | rogue-deploy-eval-deception | v2 | 0 | N | OK | OK | 8 |
| claude-basics | browser-coordinate-scaling | v2 | 0 | N | OK | OK | 8 |
| claude-basics | feature-list-checkpoint-persistence | v2 | 0 | N | OK | OK | 8 |
| claude-basics | macos-computer-use-coordinate-roundtrip | v2 | 0 | N | OK | OK | 8 |
| claude-basics | screenshot-prompt-caching | v2 | 0 | N | OK | OK | 8 |
| claude-basics | stable-element-refs | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-boondoggle-score | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-build-chapter-mapping | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-claudemd-constitution | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-dangerous-middle-activity | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-dangerous-middle-detection | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-engineering-partner-loop | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-five-supervisory-capacities | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-fluency-correctness-gap | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-grading-skill-definition | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-handoff-condition-protocol | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-package-hallucination-scanner | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-pattern-analysis-subagent | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-post-build-document | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-pretooluse-grade-blocker | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-software-design-document | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-solve-verify-asymmetry | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-spec-prompt-audit | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-spec-prompt-template | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-three-check-deployment | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-three-file-system-simulator | v2 | 0 | N | OK | OK | 8 |
| claude-code | nbb-three-pass-verification | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-cowork-task-packet-audit | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-file-rename-dry-run | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-human-approval-gates | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-map-the-agentic-loop | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-non-delegation-audit | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-plan-approval-gate | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-privacy-classification-scanner | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-receipt-extraction-pipeline | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-research-packet-traceability | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-routing-matrix | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-task-brief-validator | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-weekly-operations-packet | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-workflow-canvas | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-workflow-card-generator | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-workflow-handoff-documenter | v2 | 0 | N | OK | OK | 8 |
| claude-cowork | nbb-workspace-access-audit | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-ai-feedback-evidence-review | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-ai-policy-classifier | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-assessment-vulnerability-map | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-backward-design-lesson | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-cognitive-labor-audit | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-feedback-type-classifier | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-instructional-brief-generator | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-lesson-ai-integration-audit | v2 | 0 | N | OK | OK | 8 |
| claude-for-education | nbb-rubric-adjective-detector | v2 | 0 | N | OK | OK | 8 |
| claude-mcp-connectors | nbb-evaluate-mcp-server | v2 | 0 | N | OK | OK | 8 |
| claude-prompting | nbb-six-component-spec | v2 | 0 | N | OK | OK | 8 |
| behind-the-model | nbb-legitimacy-auditor | v2 | 0 | Y | FAIL | OK | 8 |
| claude-prompting | prompt-tutorial-lesson-06-precognition | v2 | 0 | N | OK | OK | 7 |
| claude-prompting | prompt-tutorial-lesson-07-few-shot-prompting | v2 | 0 | N | OK | OK | 7 |
| behind-the-model | risk-tiered-verification | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | self-check-vs-independent-verification | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | solve-verify-asymmetry | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | supervision-calibration-logger | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | three-level-supervision-classifier | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | type-iii-error-detector | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | boondoggle-score | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | dangerous-middle-detection | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | engineering-partner-loop | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | five-supervisory-capacities | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | fluency-correctness-gap | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | handoff-condition-protocol | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | package-hallucination-scanner | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | software-design-document | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | solve-verify-asymmetry | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | spec-prompt-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-code | three-pass-verification | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | ai-use-log | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-ai-use-log | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-cowork-task-packet-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-human-approval-gates | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-map-the-agentic-loop | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-privacy-classification-scanner | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-workflow-canvas | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | claude-liam-workflow-handoff-documenter | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | cowork-task-packet-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | human-approval-gates | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | map-the-agentic-loop | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | privacy-classification-scanner | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | workflow-canvas | v2 | 0 | N | FAIL | OK | 6 |
| claude-cowork | workflow-handoff-documenter | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | ai-feedback-evidence-review | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | ai-policy-classifier | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | assessment-vulnerability-map | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | backward-design-lesson | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-ai-feedback-evidence-review | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-ai-policy-classifier | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-assessment-vulnerability-map | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-backward-design-lesson | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-cognitive-labor-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-feedback-type-classifier | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-instructional-brief-generator | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-lesson-ai-integration-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | claude-liam-rubric-adjective-detector | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | cognitive-labor-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | feedback-type-classifier | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | instructional-brief-generator | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | lesson-ai-integration-audit | v2 | 0 | N | FAIL | OK | 6 |
| claude-for-education | rubric-adjective-detector | v2 | 0 | N | FAIL | OK | 6 |
| claude-mcp-connectors | claude-liam-evaluate-mcp-server | v2 | 0 | N | FAIL | OK | 6 |
| claude-mcp-connectors | evaluate-mcp-server | v2 | 0 | N | FAIL | OK | 6 |
| claude-prompting | claude-liam-six-component-spec | v2 | 0 | N | FAIL | OK | 6 |
| claude-prompting | six-component-spec | v2 | 0 | N | FAIL | OK | 6 |
| behind-the-model | sleeper-agents-safety-training-fails | v2 | 0 | N | OK | OK | 5 |
| behind-the-model | sycophancy-to-subterfuge | v2 | 0 | N | OK | OK | 5 |
| claude-basics | anthropic-retrieval-demo-wrapping-same-text-xml-changes | v2 | 0 | N | OK | OK | 5 |
| claude-cowork | claude-liam-vercel-refactor | v2 | 0 | N | OK | OK | 5 |
| claude-for-education | access-scaffolding-text-substitution | v2 | 0 | N | OK | OK | 5 |
| claude-for-education | cra-progression-scaffold | v2 | 0 | N | OK | OK | 5 |
| claude-for-education | fluency-prerequisite-comprehension | v2 | 0 | N | OK | OK | 5 |
| claude-for-education | preserve-cognitive-demand-differentiation | v2 | 0 | N | OK | OK | 5 |
| claude-code | build-chapter-mapping | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-boondoggle-score | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-dangerous-middle-detection | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-engineering-partner-loop | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-five-supervisory-capacities | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-fluency-correctness-gap | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-handoff-condition-protocol | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-package-hallucination-scanner | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-software-design-document | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-solve-verify-asymmetry | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-spec-prompt-audit | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claude-liam-three-pass-verification | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | claudemd-constitution | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | dangerous-middle-activity | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | grading-skill-definition | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | pattern-analysis-subagent | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | post-build-document | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | pretooluse-grade-blocker | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | spec-prompt-template | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | three-check-deployment | v2 | 0 | N | FAIL | OK | 5 |
| claude-code | three-file-system-simulator | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-file-rename-dry-run | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-non-delegation-audit | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-plan-approval-gate | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-receipt-extraction-pipeline | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-research-packet-traceability | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-routing-matrix | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-task-brief-validator | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-weekly-operations-packet | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-workflow-card-generator | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | claude-liam-workspace-access-audit | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | file-rename-dry-run | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | non-delegation-audit | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | plan-approval-gate | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | receipt-extraction-pipeline | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | research-packet-traceability | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | routing-matrix | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | task-brief-validator | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | weekly-operations-packet | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | workflow-card-generator | v2 | 0 | N | FAIL | OK | 5 |
| claude-cowork | workspace-access-audit | v2 | 0 | N | FAIL | OK | 5 |
| behind-the-model | nbb-material-plan-change | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-silent-omission-signal | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-verification-matrix | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-vox-bainbridge-irony | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-vox-code-oracle | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-vox-self-check-loop | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-vox-silent-omission | v2 | 0 | N | OK | OK | 4 |
| behind-the-model | nbb-vox-team-fence-gap | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | agent-decomposition-skills-vs-tools | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | agents-that-remember-memory-store | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | claude-code-claude-liam-agent-development | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | claude-plugins-official-claude-liam-agent-development | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | dispatch-analysts-parallel-orchestration | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | eval-driven-six-agent-variants | v2 | 0 | N | OK | OK | 4 |
| claude-agent-skills | rightmodel-pareto-frontier | v2 | 0 | N | OK | OK | 4 |
| claude-code | claude-liam-command-development | v2 | 0 | N | OK | OK | 4 |
| claude-code | claude-liam-hook-development | v2 | 0 | N | OK | OK | 4 |
| claude-code | claude-liam-writing-rules | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-agentic-loop-not-chatgpt | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-ai-creative-work-belongs-to-nobody | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-ai-homework-fluency-trap | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-boondoggle-score-anatomy | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-brutalist-three-file | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-clear-vs-compact | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-code-runs-ships-wrong | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-conducting-not-prompting | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-five-questions-before-code | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-fluency-trap-danger-zone | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-gru-slash-v0-gate | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-hook-advisory-vs-deterministic | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-intent-layer-authorship | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-one-sentence-problem-statement | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-pagination-bug-dangerous-middle | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-plan-mode-interruption | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-prompt-is-a-wish-spec-is-a-contract | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-rewind-not-fix-forward | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-skill-build-once | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-slash-context-window-check | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-slopsquatting-hallucinated-package | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-spec-vs-prompt-live | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-spec-writing-is-cs-ed | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-string-similarity-semantic-gap | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-tests-pass-user-fails | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-agentic-loop | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-ai-feedback-bias | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-buildlog-assessment | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-claudemd-length | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-handoff-conditions | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-hook-enforcement | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-rewind-respec | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-simulation-ownership | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-spec-saves-time | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-vox-subagent-context | v2 | 0 | N | OK | OK | 4 |
| claude-code | nbb-writer-reviewer-pattern | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | claude-liam-vercel-mcp | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-access-ladder-explained | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-cowork-access-ladder | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-cowork-task-packet | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-extraction-schema-first | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-nondelegation-checklist | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-plan-review-checklist | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-report-claim-tracing | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-seven-field-brief | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-synthesis-vs-deciding | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-batch-propagation | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-coherent-unsafe | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-compression-caveats | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-exposure-gate | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-instruction-channel | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-same-prescription | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-vox-scope-gap | v2 | 0 | N | OK | OK | 4 |
| claude-cowork | nbb-workflow-card-builder | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | claude-liam-math-olympiad | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-advising-privacy-gate | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-ai-ban-design-failure | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-artifact-vs-learning | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-assessment-by-design | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-assignment-stress-test | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-capstone-unit-builder | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-cognitive-friction-loop | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-data-minimization-prompt | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-differentiation-audit | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-faculty-literature-lead | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-feedback-that-replaces | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-instructional-brief-eight-fields | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-manuscript-reviewer-response | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-outcome-before-topic | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-receiving-vs-producing | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-rubric-adjective-trap | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-udl-choice-board | v2 | 0 | N | OK | OK | 4 |
| claude-for-education | nbb-vox-phase-gate | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-code-claude-liam-mcp-integration | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-liam-build-mcp-app | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-liam-build-mcp-server | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-liam-build-mcpb | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-liam-mcp-builder | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-liam-mcp-integration | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | claude-plugins-official-claude-liam-mcp-integration | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | nbb-mcp-resource-vs-tool | v2 | 0 | N | OK | OK | 4 |
| claude-mcp-connectors | nbb-vox-mcp-blast-radius | v2 | 0 | N | OK | OK | 4 |
| claude-news | claude-liam-claude-opus-4-5-migration | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-code-claude-liam-plugin-settings | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-code-claude-liam-plugin-structure | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-access | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-agent-development | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-asana-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-bigquery-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-cardputer-buddy | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-claude-automation-recommender | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-claude-md-improver | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-command-development | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-config-guide | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-configure | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-confluence-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-datadog-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-debug-plugins | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-enterprise-search | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-example-command | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-google-drive-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-grafana-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-graphing | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-hook-development | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-hubspot-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-jira-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-linear-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-m5-onboard | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-notion-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-pagerduty-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-playground | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-plugin-settings | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-plugin-structure | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-project-artifact | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-redshift-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-salesforce-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-liam-sentry-api | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-plugins-official-claude-liam-plugin-settings | v2 | 0 | N | OK | OK | 4 |
| claude-plugins | claude-plugins-official-claude-liam-plugin-structure | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-agentic-approval-gate | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-agentic-handoff-auditor | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-constraint-builder | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-constraint-extractor | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-context-hygiene-demo | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-criteria-first-generator | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-criteria-first-habit | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-data-gigo-detector | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-examples-annotate | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-failure-criterion-generator | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-fluency-trap-correction | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-prompt-anatomy-auditor | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-prompt-card-builder | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-prompt-card-library | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-revision-change-log | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-scope-stack-setup | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-self-critique-loop | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-six-component-prompt | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-six-slot-anatomy | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-three-pass-refinement-demo | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-agentic-irreversible | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-citation-surface-format | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-context-priority-weight | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-criteria-before-output | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-examples-teach-more | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-prompt-injection | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-prompt-library-lost | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-prompt-six-slots | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-prompt-spec | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-self-review-sieve | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-surface-routing | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-vague-revision-spreads | v2 | 0 | N | OK | OK | 4 |
| claude-prompting | nbb-vox-writing-claim-invention | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-brand-guidelines | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-canvas-design | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-claude-api | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-doc-coauthoring | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-docx | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-example-skill | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-frontend-design | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-internal-comms | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-pdf | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-pptx | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-skill-creator | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-skill-development | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-slack-gif-creator | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-web-artifacts-builder | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-webapp-testing | v2 | 0 | N | OK | OK | 4 |
| claude-skills | claude-liam-xlsx | v2 | 0 | N | OK | OK | 4 |
| claude-code | claude-liam-build-chapter-mapping | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-claudemd-constitution | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-dangerous-middle-activity | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-grading-skill-definition | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-pattern-analysis-subagent | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-post-build-document | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-pretooluse-grade-blocker | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-spec-prompt-template | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-three-check-deployment | v2 | 0 | N | FAIL | OK | 4 |
| claude-code | claude-liam-three-file-system-simulator | v2 | 0 | N | FAIL | OK | 4 |
| behind-the-model | silent-omission-signal | v2 | 0 | N | OK | OK | 3 |
| behind-the-model | verification-matrix | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-be-good-at-claude | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-chatgpt-vs-claude | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-101 | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-code | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-connectors | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-cowork | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-design | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-fable-5 | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-for-excel | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-for-your-team | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-linkedin | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-skills | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-claude-to-sound-like-you | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-five-claudes-explained | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-how-to-prompt | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-nine-prompt-writing-skills | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-six-claude-formulas | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-stop-hitting-claude-limits | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-stop-prompting-claude | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | claude-liam-stop-writing-like-ai | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | earnings-preview-verbatim-gate | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | equity-research-initiating-coverage-gate | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | financial-dcf-live-formula | v2 | 0 | N | OK | OK | 3 |
| claude-cowork | managed-agents-two-object-split | v2 | 0 | N | OK | OK | 3 |
| behind-the-model | claude-constitution-honesty-standard | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | claude-constitution-many-hands | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | claude-constitution-operator-floor | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | claude-constitution-stable-identity | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | claude-constitution-thousand-senders | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | jacobian-lens-reading-ahead | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | model-written-evals-inverse-scaling | v2 | 0 | Y | FAIL | OK | 3 |
| behind-the-model | political-neutrality-eval-two-graders-rank-every-topic | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | scone-bench-benchmark-score-may-memorization-score | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | sleeper-agents-paper-ai-s-hidden-scratchpad-blind | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | vox-bainbridge-irony | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | vox-fluency-trap | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | vox-self-check-loop | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | vox-silent-omission | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | vox-team-fence-gap | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | agent-sdk-workshop-adding-one-capability-time-changes | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | agent-sdk-workshop-agent-s-memory-guardrail-one | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | agent-sdk-workshop-parallelism-prompt-problem-code-prob | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | anthropic-tools-channel-returns-tool-results-also | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | claude-agent-sdk-demos-interleaved-parallel-tool-logs-s | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | claude-agent-sdk-typescript-sending-full-list-beats-sen | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | claude-cookbooks-cheap-worker-crew-reads-9 | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | claude-for-legal-one-context-flag-flips-every | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | claude-quickstarts-waiting-each-result-before-next | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | cwc-long-running-agents-agent-will-mark-feature-done | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | cwc-workshops-cutting-402-line-agent-prompt | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | financial-services-untrusted-document-s-hidden-instruct | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | healthcare-no-family-history-pe-needs | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | healthcare-prior-auth-ai-structurally-cannot | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | healthcare-swapping-fast-model-made-whole | v2 | 0 | N | FAIL | OK | 2 |
| claude-agent-skills | launch-your-agent-autonomous-agent-freeze-mid-run | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | anthropic-sdk-php-server-hands-back-encrypted-context | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | anthropic-sdk-typescript-partial-json-valid-object-befo | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claude-constitution-one-narrow-safety-rule-make | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claude-cookbooks-splitting-chunk-from-document-makes | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claude-quickstarts-50-turn-agent-pays-same | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claude-quickstarts-claude-s-click-lands-wrong | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claudeforfoundationmodels-same-api-key-shipped-prototyp | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | claudeforfoundationmodels-web-search-never-runs-code | v2 | 0 | N | FAIL | OK | 2 |
| claude-basics | evals-model-says-i-have-no | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | agentic-loop-not-chatgpt | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | boondoggle-score-anatomy | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | brutalist-three-file | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-action-natural-trigger-review-counting-chec | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-base-action-turn-budget-stops-runaway-agent | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-coding-assistant-deliberately-refuses-write | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-four-agents-scoring-same-bug | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-monitoring-guide-doubling-claude-code-sessi | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-monitoring-guide-typing-one-word-multiply-a | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-code-security-review-same-eval-real-bug-one | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-agentic-loop-not-chatgpt | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-ai-homework-fluency-trap | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-boondoggle-score-anatomy | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-brutalist-three-file | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-clear-vs-compact | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-conducting-not-prompting | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-five-questions-before-code | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-gru-slash-v0-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-hook-advisory-vs-deterministic | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-intent-layer-authorship | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-one-sentence-problem-statement | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-plan-mode-interruption | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-prompt-is-a-wish-spec-is-a-contract | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-rewind-not-fix-forward | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-skill-build-once | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-slash-context-window-check | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-spec-vs-prompt-live | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-spec-writing-is-cs-ed | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-vox-buildlog-assessment | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-vox-subagent-context | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claude-liam-writer-reviewer-pattern | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | claudes-c-compiler-assembly-shrinks-through-13-sequenti | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | clear-vs-compact | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | conducting-not-prompting | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | defending-code-reference-harness-count-field-checked-on | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | defending-code-reference-harness-pipeline-runs-same-cra | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | five-questions-before-code | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | gru-slash-v0-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | hook-advisory-vs-deterministic | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | intent-layer-authorship | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | one-sentence-problem-statement | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | plan-mode-interruption | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | rewind-not-fix-forward | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | riv2025-long-horizon-coding-agent-demo-backend-test-pas | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | riv2025-long-horizon-coding-agent-demo-wildcard-coverin | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | skill-build-once | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | slash-context-window-check | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | spec-vs-prompt-live | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | spec-writing-is-cs-ed | v2 | 0 | N | FAIL | OK | 2 |
| claude-code | writer-reviewer-pattern | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | access-ladder-explained | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-cowork-access-ladder | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-cowork-task-packet | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-extraction-schema-first | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-nondelegation-checklist | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-plan-review-checklist | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-report-claim-tracing | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-seven-field-brief | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-synthesis-vs-deciding | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-batch-propagation | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-coherent-unsafe | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-compression-caveats | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-exposure-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-format-credibility | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-instruction-channel | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-same-prescription | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-vox-scope-gap | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | claude-liam-workflow-card-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | cowork-access-ladder | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | cowork-task-packet | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | extraction-schema-first | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | nondelegation-checklist | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | plan-review-checklist | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | report-claim-tracing | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | seven-field-brief | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | synthesis-vs-deciding | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-batch-propagation | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-coherent-unsafe | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-compression-caveats | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-exposure-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-instruction-channel | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-same-prescription | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | vox-scope-gap | v2 | 0 | N | FAIL | OK | 2 |
| claude-cowork | workflow-card-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | advising-privacy-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | assignment-stress-test | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | capstone-unit-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-advising-privacy-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-assignment-stress-test | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-capstone-unit-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-data-minimization-prompt | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-differentiation-audit | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-faculty-literature-lead | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-instructional-brief-eight-fields | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-manuscript-reviewer-response | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | claude-liam-udl-choice-board | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | data-minimization-prompt | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | differentiation-audit | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | faculty-literature-lead | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | instructional-brief-eight-fields | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | k12-teacher-skills-missing-math-prerequisite-t-scaffold | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | manuscript-reviewer-response | v2 | 0 | N | FAIL | OK | 2 |
| claude-for-education | udl-choice-board | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | claude-liam-mcp-resource-vs-tool | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | claude-liam-vox-mcp-blast-radius | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | github-mcp-server-giving-model-tools-makes-choose | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | github-mcp-server-one-generic-cli-drive-api | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | mcp-resource-vs-tool | v2 | 0 | N | FAIL | OK | 2 |
| claude-mcp-connectors | vox-mcp-blast-radius | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-code-plugin-seven-surfaces | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-plugins-community-copyright-restrictions-mean-th | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-plugins-community-image-model-s-burned-captions | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-plugins-official-enabling-sms-breaks-access-cont | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-plugins-official-live-bot-hands-pairing-codes | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | claude-plugins-official-same-assistant-code-runs-discor | v2 | 0 | N | FAIL | OK | 2 |
| claude-plugins | knowledge-work-plugins-responding-webhook-after-process | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | agentic-approval-gate | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | agentic-handoff-auditor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | anthropic-sdk-python-tool-calling-loop-stops-model | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | anthropic-sdk-typescript-schema-enters-types-travels-te | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-agentic-handoff-auditor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-constraint-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-constraint-extractor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-context-hygiene-demo | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-criteria-first-generator | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-criteria-first-habit | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-data-gigo-detector | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-examples-annotate | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-failure-criterion-generator | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-fluency-trap-correction | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-prompt-anatomy-auditor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-prompt-card-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-prompt-card-library | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-revision-change-log | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-scope-stack-setup | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-self-critique-loop | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-six-component-prompt | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-six-slot-anatomy | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-three-pass-refinement-demo | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-agentic-irreversible | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-citation-surface-format | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-context-priority-weight | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-criteria-before-output | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-examples-teach-more | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-prompt-injection | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-prompt-library-lost | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-prompt-six-slots | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-prompt-spec | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-self-review-sieve | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-surface-routing | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-vague-revision-spreads | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-liam-vox-writing-claim-invention | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | claude-quickstarts-agent-fresh-memory-every-session | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | constraint-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | constraint-extractor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | context-hygiene-demo | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | courses-asking-claude-json-gives-prose | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | courses-claude-handed-ten-tools-one | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | courses-three-graders-read-same-answer | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | criteria-first-generator | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | criteria-first-habit | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | data-gigo-detector | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | examples-annotate | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | failure-criterion-generator | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | fluency-trap-correction | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-anatomy-auditor | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-card-builder | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-card-library | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-eng-interactive-tutorial-claude-t-think-silently | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-eng-interactive-tutorial-helpful-claude-invents- | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-eng-interactive-tutorial-swapping-order-two-argu | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-eng-interactive-tutorial-telling-claude-logic-bo | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | prompt-eng-interactive-tutorial-wrapping-one-email-tags | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | revision-change-log | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | scope-stack-setup | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | self-critique-loop | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | six-component-prompt | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | six-slot-anatomy | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | three-pass-refinement-demo | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-agentic-irreversible | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-citation-surface-format | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-context-priority-weight | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-criteria-before-output | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-examples-teach-more | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-prompt-injection | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-prompt-library-lost | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-prompt-six-slots | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-prompt-spec | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-self-review-sieve | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-surface-routing | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-vague-revision-spreads | v2 | 0 | N | FAIL | OK | 2 |
| claude-prompting | vox-writing-claim-invention | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | attribution-graphs-frontend-language-model-adds-two-num | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | claude-liam-context-dreaming | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | constitutionalharmlessnesspaper-safe-answer-one-argues- | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | decompositionfaithfulnesspaper-answering-sub-questions- | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | hh-rlhf-safer-training-objective-gets-fewest | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | original-performance-takehome-ai-told-speed-up-program | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | sycophancy-to-subterfuge-paper-safety-test-passes-safet | v2 | 0 | N | FAIL | OK | 2 |
| claude-research | toy-models-of-superposition-crowded-features-arrange-th | v2 | 0 | N | FAIL | OK | 2 |
| claude-skills | skills-50-round-agent-survives-past | v2 | 0 | N | FAIL | OK | 2 |
| claude-skills | skills-claude-spends-5000-thinking-tokens | v2 | 0 | N | FAIL | OK | 2 |
| claude-skills | skills-claude-write-right-spreadsheet-formula | v2 | 0 | N | FAIL | OK | 2 |
| claude-skills | skills-number-s-color-financial-model | v2 | 0 | N | FAIL | OK | 2 |
| behind-the-model | political-neutrality-eval-paired-prompts | v2 | 0 | N | OK | OK | 1 |
| claude-basics | computer-use-best-practices | v2 | 0 | N | OK | OK | 1 |
| claude-code | claudes-c-compiler | v2 | 0 | N | OK | OK | 1 |
| claude-code | cwc-how-we-claude-code | v2 | 0 | N | OK | OK | 1 |
| claude-code | cwc-workshop-agent-battle-minecraft | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | cookbooks-metaprompt | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | courses-real-world-prompting-medical | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-avoiding-hallucinations | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-engineering-precognition | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-separating-data | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-tutorial-lesson-02-clear-and-direct | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-tutorial-lesson-03-role-prompting | v2 | 0 | N | OK | OK | 1 |
| claude-prompting | prompt-tutorial-lesson-05-formatting-output | v2 | 0 | N | OK | OK | 1 |
| claude-code | ai-creative-work-belongs-to-nobody | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | ai-homework-fluency-trap | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-ai-creative-work-belongs-to-nobody | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-code-runs-ships-wrong | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-fluency-trap-danger-zone | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-pagination-bug-dangerous-middle | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-slopsquatting-hallucinated-package | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-string-similarity-semantic-gap | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-tests-pass-user-fails | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-agentic-loop | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-ai-feedback-bias | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-claudemd-length | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-code-oracle | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-handoff-conditions | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-hook-enforcement | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-rewind-respec | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-simulation-ownership | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | claude-liam-vox-spec-saves-time | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | code-runs-ships-wrong | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | fluency-trap-danger-zone | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | pagination-bug-dangerous-middle | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | prompt-is-a-wish-spec-is-a-contract | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | slopsquatting-hallucinated-package | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | string-similarity-semantic-gap | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | tests-pass-user-fails | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-agentic-loop | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-ai-feedback-bias | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-buildlog-assessment | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-claudemd-length | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-code-oracle | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-handoff-conditions | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-hook-enforcement | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-rewind-respec | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-simulation-ownership | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-spec-saves-time | v2 | 0 | N | FAIL | OK | 1 |
| claude-code | vox-subagent-context | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | ai-ban-design-failure | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | artifact-vs-learning | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | assessment-by-design | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-ai-ban-design-failure | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-artifact-vs-learning | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-assessment-by-design | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-cognitive-friction-loop | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-feedback-that-replaces | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-outcome-before-topic | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-receiving-vs-producing | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-rubric-adjective-trap | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | claude-liam-vox-phase-gate | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | cognitive-friction-loop | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | feedback-that-replaces | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | outcome-before-topic | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | receiving-vs-producing | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | rubric-adjective-trap | v2 | 0 | N | FAIL | OK | 1 |
| claude-for-education | vox-phase-gate | v2 | 0 | N | FAIL | OK | 1 |
| behind-the-model | claude-constitution-corrigibility-dial | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-constitution-three-principals | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-liam-irreversible-action-gate | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-liam-material-plan-change | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-liam-silent-omission-signal | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-liam-verification-matrix | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | constitutional-ai-self-critique | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | hh-rlhf-preference-data-structure | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | irreversible-action-gate | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | material-plan-change | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | model-written-evals-sycophancy | v2 | 0 | Y | OK | OK | 0 |
| behind-the-model | claude-liam-correlated-failure-research | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-independent-verification-protocol | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-legitimacy-auditor | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-risk-tiered-verification | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-self-check-vs-independent-verification | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-solve-verify-asymmetry | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-supervision-calibration-logger | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-three-level-supervision-classifier | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-type-iii-error-detector | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-vox-bainbridge-irony | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-vox-fluency-trap | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-vox-self-check-loop | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-vox-silent-omission | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | claude-liam-vox-team-fence-gap | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | correlated-failure-research | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | evals-same-question-gets-different-answer | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | headvis-one-always-present-token-secretly | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | independent-verification-protocol | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | jacobian-lens-model-spells-word-right-inside | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | legitimacy-auditor | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | model-cards-re-reading-own-order-back | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | nbb-correlated-failure-research | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | nbb-independent-verification-protocol | v2 | 0 | Y | FAIL | OK | 0 |
| behind-the-model | nbb-irreversible-action-gate | v2 | 0 | Y | FAIL | OK | 0 |
| claude-agent-skills | claude-skills-progressive-disclosure | v2 | 0 | N | FAIL | OK | 0 |

## Detail — Reels With Issues

(757 reels have at least one issue)

### `claude-cowork/nbb-vox-modal-upgrade`

- **BC-1 (SlateCard):** B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13, B14
- **BC-3 (eyebrow/kicker/headline):** B01(eyebrow,headline), B02(eyebrow,headline), B03(eyebrow,headline), B04(eyebrow,headline), B05(eyebrow,headline), B06(eyebrow,headline), B07(eyebrow,headline), B08(eyebrow,headline), B09(eyebrow,headline), B10(eyebrow,headline), B11(eyebrow,headline), B12(eyebrow,headline), B13(eyebrow,headline), B14(eyebrow,headline)
- **Unrendered Remotion boxes (6):** NBB00, B02, B11, NBB01, NBB02, NBB03

### `claude-cowork/vox-modal-upgrade`

- **BC-1 (SlateCard):** B01, B02, B03, B04, B05, B06, B07, B08, B09, B10, B11, B12, B13, B14
- **BC-3 (eyebrow/kicker/headline):** B01(eyebrow,headline), B02(eyebrow,headline), B03(eyebrow,headline), B04(eyebrow,headline), B05(eyebrow,headline), B06(eyebrow,headline), B07(eyebrow,headline), B08(eyebrow,headline), B09(eyebrow,headline), B10(eyebrow,headline), B11(eyebrow,headline), B12(eyebrow,headline), B13(eyebrow,headline), B14(eyebrow,headline)
- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (4):** B02, B11, YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-modal-upgrade`

- **BC-1 (SlateCard):** B01, B03, B04, B05, B06, B07, B08, B09, B10, B12, B13, B14
- **BC-3 (eyebrow/kicker/headline):** B01(eyebrow,headline), B03(eyebrow,headline), B04(eyebrow,headline), B05(eyebrow,headline), B06(eyebrow,headline), B07(eyebrow,headline), B08(eyebrow,headline), B09(eyebrow,headline), B10(eyebrow,headline), B12(eyebrow,headline), B13(eyebrow,headline), B14(eyebrow,headline)
- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-liam-installing-plugins`

- **BC-1 (SlateCard):** B01, B06, B09, B14, B19
- **Unrendered Remotion boxes (5):** B00, B22, V01, H01, O01

### `claude-cowork/claude-liam-access-ladder-explained`

- **BC-2 (ClaudeWindow+artifact body):** B01, B02, B03, B04
- **Unrendered Remotion boxes (7):** B00, B01, B02, B03, B04, YOURTURN, B06

### `claude-cowork/claude-liam-productivity`

- **BC-1 (SlateCard):** B03, B05, B08, B10
- **Unrendered Remotion boxes (6):** B00, B12, B20, V01, H01, O01

### `claude-cowork/nbb-vox-format-credibility`

- **BC-1 (SlateCard):** B02, B10
- **BC-3 (eyebrow/kicker/headline):** B02(eyebrow,headline), B10(eyebrow,headline)
- **Unrendered Remotion boxes (6):** NBB00, B02, B10, NBB01, NBB02, NBB03

### `claude-cowork/claude-liam-support`

- **BC-1 (SlateCard):** B05, B07, B09, B10
- **Unrendered Remotion boxes (5):** B00, B11, V01, H01, O01

### `claude-plugins/claude-liam-combining-plugins`

- **BC-1 (SlateCard):** B09, B13, B17, B22
- **Unrendered Remotion boxes (4):** B00, V01, H01, O01

### `claude-cowork/vox-format-credibility`

- **BC-1 (SlateCard):** B02, B10
- **BC-3 (eyebrow/kicker/headline):** B02(eyebrow,headline), B10(eyebrow,headline)
- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (4):** B02, B10, YOURTURN, OUTRO

### `claude-plugins/claude-liam-building-plugins`

- **BC-1 (SlateCard):** B01, B12, B25
- **Unrendered Remotion boxes (6):** B00, B07, B09, V01, H01, O01

### `claude-cowork/claude-liam-troubleshooting`

- **BC-1 (SlateCard):** B01, B04, B09
- **Unrendered Remotion boxes (5):** B00, B08, V01, H01, O01

### `claude-research/claude-liam-research`

- **BC-1 (SlateCard):** B06, B10, B14
- **Unrendered Remotion boxes (5):** B00, B12, V01, H01, O01

### `claude-cowork/claude-liam-data`

- **BC-1 (SlateCard):** B01, B12
- **Unrendered Remotion boxes (7):** B00, B05, B14, B18, V01, H01, O01

### `claude-cowork/claude-liam-enterprise-search`

- **BC-1 (SlateCard):** B05, B09
- **Unrendered Remotion boxes (7):** B00, B07, B12, B15, V01, H01, O01

### `claude-cowork/claude-liam-one-hour-on-cowork`

- **BC-2 (ClaudeWindow+artifact body):** B07, B11
- **Unrendered Remotion boxes (7):** B00, B03, B07, B11, B13, YOURTURN, B16

### `claude-code/claude-api-one-endpoint-ladder`

- **BC-2 (ClaudeWindow+artifact body):** A21, A51
- **Unrendered Remotion boxes (6):** B00, A21, A51, VERDICT, YOURTURN, OUTRO

### `claude-cowork/claude-liam-marketing`

- **BC-1 (SlateCard):** B05, B14
- **Unrendered Remotion boxes (5):** B00, B12, V01, H01, O01

### `claude-cowork/claude-liam-product`

- **BC-1 (SlateCard):** B04, B19
- **Unrendered Remotion boxes (5):** B00, B10, V01, H01, O01

### `claude-cowork/claude-liam-sales`

- **BC-1 (SlateCard):** B07, B17
- **Unrendered Remotion boxes (5):** B00, B10, V01, H01, O01

### `claude-plugins/claude-liam-what-plugins-are`

- **BC-1 (SlateCard):** B04, B13
- **Unrendered Remotion boxes (5):** B00, B06, V01, H01, O01

### `claude-prompting/claude-liam-different-kind-of-wrong`

- **BC-3 (eyebrow/kicker/headline):** B15(kicker), B24(kicker)
- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-legal-finance`

- **BC-1 (SlateCard):** B22
- **Unrendered Remotion boxes (6):** B00, B06, B15, V01, H01, O01

### `claude-prompting/claude-liam-agentic-approval-gate`

- **BC-2 (ClaudeWindow+artifact body):** B02
- **Unrendered Remotion boxes (5):** B00, B02, B04, YOURTURN, B06

### `behind-the-model/what-is-behind-the-model`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-agent-skills/what-is-claude-agent-skills`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-basics/what-is-claude-basics`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, YOURTURN, B07

### `claude-for-education/what-is-claude-for-education`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-mcp-connectors/what-is-claude-mcp-connectors`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-plugins/what-is-claude-plugins`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-prompting/what-is-claude-prompting`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, YOURTURN, B07

### `claude-research/what-is-claude-research`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, YOURTURN, B07

### `claude-skills/what-is-claude-skills`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `claude-youtube/what-is-claude-youtube`

- **BC-2 (ClaudeWindow+artifact body):** B05
- **Unrendered Remotion boxes (4):** B00, B05, B06, B07

### `behind-the-model/nbb-risk-tiered-verification`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-self-check-vs-independent-verification`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-solve-verify-asymmetry`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-supervision-calibration-logger`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-three-level-supervision-classifier`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-type-iii-error-detector`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/rogue-deploy-eval-deception`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B06

### `claude-basics/browser-coordinate-scaling`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B07

### `claude-basics/feature-list-checkpoint-persistence`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B07

### `claude-basics/macos-computer-use-coordinate-roundtrip`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B07

### `claude-basics/screenshot-prompt-caching`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B07

### `claude-basics/stable-element-refs`

- **Unrendered Remotion boxes (8):** B00, B01, B02, B03, B04, B05, YOURTURN, B07

### `claude-code/nbb-boondoggle-score`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-build-chapter-mapping`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-claudemd-constitution`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-dangerous-middle-activity`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-dangerous-middle-detection`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-engineering-partner-loop`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-five-supervisory-capacities`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-fluency-correctness-gap`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-grading-skill-definition`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-handoff-condition-protocol`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-package-hallucination-scanner`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-pattern-analysis-subagent`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-post-build-document`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-pretooluse-grade-blocker`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-software-design-document`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-solve-verify-asymmetry`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-spec-prompt-audit`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-code/nbb-spec-prompt-template`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-three-check-deployment`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-three-file-system-simulator`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-code/nbb-three-pass-verification`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-cowork-task-packet-audit`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-file-rename-dry-run`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-human-approval-gates`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-map-the-agentic-loop`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-non-delegation-audit`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-plan-approval-gate`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-privacy-classification-scanner`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-receipt-extraction-pipeline`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-research-packet-traceability`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-routing-matrix`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-task-brief-validator`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-weekly-operations-packet`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-workflow-canvas`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-workflow-card-generator`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-cowork/nbb-workflow-handoff-documenter`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-cowork/nbb-workspace-access-audit`

- **Unrendered Remotion boxes (8):** NBB00, B02, B03, B05, B09, NBB01, NBB02, NBB03

### `claude-for-education/nbb-ai-feedback-evidence-review`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-ai-policy-classifier`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-assessment-vulnerability-map`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-backward-design-lesson`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-cognitive-labor-audit`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-feedback-type-classifier`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-instructional-brief-generator`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-lesson-ai-integration-audit`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-for-education/nbb-rubric-adjective-detector`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-mcp-connectors/nbb-evaluate-mcp-server`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-prompting/nbb-six-component-spec`

- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `behind-the-model/nbb-legitimacy-auditor`

- **Open bookend:** NBB00: present but pattern='FormBCard'
- **Unrendered Remotion boxes (8):** NBB00, B00, B02, B03, B05, NBB01, NBB02, NBB03

### `claude-prompting/prompt-tutorial-lesson-06-precognition`

- **Unrendered Remotion boxes (7):** B00, B01, B02, B03, B04, YOURTURN, B06

### `claude-prompting/prompt-tutorial-lesson-07-few-shot-prompting`

- **Unrendered Remotion boxes (7):** B00, B01, B02, B03, B04, YOURTURN, B06

### `behind-the-model/risk-tiered-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `behind-the-model/self-check-vs-independent-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `behind-the-model/solve-verify-asymmetry`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `behind-the-model/supervision-calibration-logger`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `behind-the-model/three-level-supervision-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `behind-the-model/type-iii-error-detector`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-code/boondoggle-score`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/dangerous-middle-detection`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/engineering-partner-loop`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/five-supervisory-capacities`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/fluency-correctness-gap`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/handoff-condition-protocol`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/package-hallucination-scanner`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/software-design-document`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/solve-verify-asymmetry`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/spec-prompt-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-code/three-pass-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B07

### `claude-cowork/ai-use-log`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-ai-use-log`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-cowork-task-packet-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-human-approval-gates`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-map-the-agentic-loop`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-privacy-classification-scanner`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-workflow-canvas`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-workflow-handoff-documenter`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/cowork-task-packet-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/human-approval-gates`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/map-the-agentic-loop`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/privacy-classification-scanner`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/workflow-canvas`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/workflow-handoff-documenter`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-for-education/ai-feedback-evidence-review`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/ai-policy-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/assessment-vulnerability-map`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/backward-design-lesson`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-ai-feedback-evidence-review`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-ai-policy-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-assessment-vulnerability-map`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-backward-design-lesson`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-cognitive-labor-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-feedback-type-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-instructional-brief-generator`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-lesson-ai-integration-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/claude-liam-rubric-adjective-detector`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/cognitive-labor-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/feedback-type-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/instructional-brief-generator`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/lesson-ai-integration-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-for-education/rubric-adjective-detector`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-mcp-connectors/claude-liam-evaluate-mcp-server`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-mcp-connectors/evaluate-mcp-server`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, B09

### `claude-prompting/claude-liam-six-component-spec`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `claude-prompting/six-component-spec`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Unrendered Remotion boxes (6):** B00, B02, B03, B05, YOURTURN, OUTRO

### `behind-the-model/sleeper-agents-safety-training-fails`

- **Unrendered Remotion boxes (5):** B00, B04, B05, YOURTURN, B06

### `behind-the-model/sycophancy-to-subterfuge`

- **Unrendered Remotion boxes (5):** B00, B04, B05, YOURTURN, B06

### `claude-basics/anthropic-retrieval-demo-wrapping-same-text-xml-changes`

- **Unrendered Remotion boxes (5):** B00, B04, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-vercel-refactor`

- **Unrendered Remotion boxes (5):** B00, B11, B20, YOURTURN, B22

### `claude-for-education/access-scaffolding-text-substitution`

- **Unrendered Remotion boxes (5):** B00, B02, B03, B04, B05

### `claude-for-education/cra-progression-scaffold`

- **Unrendered Remotion boxes (5):** B00, B02, B03, B04, B05

### `claude-for-education/fluency-prerequisite-comprehension`

- **Unrendered Remotion boxes (5):** B00, B02, B03, B04, B05

### `claude-for-education/preserve-cognitive-demand-differentiation`

- **Unrendered Remotion boxes (5):** B00, B02, B03, B04, B05

### `claude-code/build-chapter-mapping`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/claude-liam-boondoggle-score`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-dangerous-middle-detection`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-engineering-partner-loop`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-five-supervisory-capacities`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-fluency-correctness-gap`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-handoff-condition-protocol`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-package-hallucination-scanner`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-software-design-document`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-solve-verify-asymmetry`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-spec-prompt-audit`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claude-liam-three-pass-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B00, B02, B03, B05, YOURTURN

### `claude-code/claudemd-constitution`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/dangerous-middle-activity`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/grading-skill-definition`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/pattern-analysis-subagent`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/post-build-document`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/pretooluse-grade-blocker`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/spec-prompt-template`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/three-check-deployment`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-code/three-file-system-simulator`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, B07

### `claude-cowork/claude-liam-file-rename-dry-run`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-non-delegation-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-plan-approval-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-receipt-extraction-pipeline`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-research-packet-traceability`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-routing-matrix`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-task-brief-validator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-weekly-operations-packet`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-workflow-card-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/claude-liam-workspace-access-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/file-rename-dry-run`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/non-delegation-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/plan-approval-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/receipt-extraction-pipeline`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/research-packet-traceability`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/routing-matrix`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/task-brief-validator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/weekly-operations-packet`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/workflow-card-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `claude-cowork/workspace-access-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (5):** B02, B03, B05, YOURTURN, OUTRO

### `behind-the-model/nbb-material-plan-change`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-silent-omission-signal`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-verification-matrix`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-vox-bainbridge-irony`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-vox-code-oracle`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-vox-self-check-loop`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-vox-silent-omission`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `behind-the-model/nbb-vox-team-fence-gap`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-agent-skills/agent-decomposition-skills-vs-tools`

- **Unrendered Remotion boxes (4):** B00, B08, B09, B10

### `claude-agent-skills/agents-that-remember-memory-store`

- **Unrendered Remotion boxes (4):** B00, B08, B09, B10

### `claude-agent-skills/claude-code-claude-liam-agent-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-agent-skills/claude-plugins-official-claude-liam-agent-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-agent-skills/dispatch-analysts-parallel-orchestration`

- **Unrendered Remotion boxes (4):** B00, B08, B09, B10

### `claude-agent-skills/eval-driven-six-agent-variants`

- **Unrendered Remotion boxes (4):** B00, B08, B09, B10

### `claude-agent-skills/rightmodel-pareto-frontier`

- **Unrendered Remotion boxes (4):** B00, B08, B09, B10

### `claude-code/claude-liam-command-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-code/claude-liam-hook-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-code/claude-liam-writing-rules`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-code/nbb-agentic-loop-not-chatgpt`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-ai-creative-work-belongs-to-nobody`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-ai-homework-fluency-trap`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-boondoggle-score-anatomy`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-brutalist-three-file`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-clear-vs-compact`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-code-runs-ships-wrong`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-conducting-not-prompting`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-five-questions-before-code`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-fluency-trap-danger-zone`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-gru-slash-v0-gate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-hook-advisory-vs-deterministic`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-intent-layer-authorship`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-one-sentence-problem-statement`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-pagination-bug-dangerous-middle`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-plan-mode-interruption`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-prompt-is-a-wish-spec-is-a-contract`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-rewind-not-fix-forward`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-skill-build-once`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-slash-context-window-check`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-slopsquatting-hallucinated-package`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-spec-vs-prompt-live`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-spec-writing-is-cs-ed`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-string-similarity-semantic-gap`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-tests-pass-user-fails`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-agentic-loop`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-ai-feedback-bias`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-buildlog-assessment`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-claudemd-length`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-handoff-conditions`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-hook-enforcement`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-rewind-respec`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-simulation-ownership`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-spec-saves-time`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-vox-subagent-context`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-code/nbb-writer-reviewer-pattern`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/claude-liam-vercel-mcp`

- **Unrendered Remotion boxes (4):** B00, B18, YOURTURN, B20

### `claude-cowork/nbb-access-ladder-explained`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-cowork-access-ladder`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-cowork-task-packet`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-extraction-schema-first`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-nondelegation-checklist`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-plan-review-checklist`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-report-claim-tracing`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-seven-field-brief`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-synthesis-vs-deciding`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-batch-propagation`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-coherent-unsafe`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-compression-caveats`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-exposure-gate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-instruction-channel`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-same-prescription`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-vox-scope-gap`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-cowork/nbb-workflow-card-builder`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/claude-liam-math-olympiad`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-for-education/nbb-advising-privacy-gate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-ai-ban-design-failure`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-artifact-vs-learning`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-assessment-by-design`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-assignment-stress-test`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-capstone-unit-builder`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-cognitive-friction-loop`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-data-minimization-prompt`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-differentiation-audit`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-faculty-literature-lead`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-feedback-that-replaces`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-instructional-brief-eight-fields`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-manuscript-reviewer-response`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-outcome-before-topic`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-receiving-vs-producing`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-rubric-adjective-trap`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-udl-choice-board`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-for-education/nbb-vox-phase-gate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-mcp-connectors/claude-code-claude-liam-mcp-integration`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-liam-build-mcp-app`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-liam-build-mcp-server`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-liam-build-mcpb`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-liam-mcp-builder`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-liam-mcp-integration`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/claude-plugins-official-claude-liam-mcp-integration`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-mcp-connectors/nbb-mcp-resource-vs-tool`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-mcp-connectors/nbb-vox-mcp-blast-radius`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-news/claude-liam-claude-opus-4-5-migration`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-code-claude-liam-plugin-settings`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-code-claude-liam-plugin-structure`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-access`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-agent-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-asana-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-bigquery-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-cardputer-buddy`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-claude-automation-recommender`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-claude-md-improver`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-command-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-config-guide`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-configure`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-confluence-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-datadog-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-debug-plugins`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-enterprise-search`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-example-command`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-google-drive-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-grafana-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-graphing`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-hook-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-hubspot-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-jira-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-linear-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-m5-onboard`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-notion-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-pagerduty-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-playground`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-plugin-settings`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-plugin-structure`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-project-artifact`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-redshift-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-salesforce-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-liam-sentry-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-plugins-official-claude-liam-plugin-settings`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-plugins/claude-plugins-official-claude-liam-plugin-structure`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-prompting/nbb-agentic-approval-gate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-agentic-handoff-auditor`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-constraint-builder`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-constraint-extractor`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-context-hygiene-demo`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-criteria-first-generator`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-criteria-first-habit`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-data-gigo-detector`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-examples-annotate`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-failure-criterion-generator`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-fluency-trap-correction`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-prompt-anatomy-auditor`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-prompt-card-builder`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-prompt-card-library`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-revision-change-log`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-scope-stack-setup`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-self-critique-loop`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-six-component-prompt`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-six-slot-anatomy`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-three-pass-refinement-demo`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-agentic-irreversible`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-citation-surface-format`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-context-priority-weight`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-criteria-before-output`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-examples-teach-more`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-prompt-injection`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-prompt-library-lost`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-prompt-six-slots`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-prompt-spec`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-self-review-sieve`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-surface-routing`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-vague-revision-spreads`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-prompting/nbb-vox-writing-claim-invention`

- **Unrendered Remotion boxes (4):** NBB00, NBB01, NBB02, NBB03

### `claude-skills/claude-liam-brand-guidelines`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-canvas-design`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-claude-api`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-doc-coauthoring`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-docx`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-example-skill`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-frontend-design`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-internal-comms`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-pdf`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-pptx`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-skill-creator`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-skill-development`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-slack-gif-creator`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-web-artifacts-builder`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-webapp-testing`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-skills/claude-liam-xlsx`

- **Unrendered Remotion boxes (4):** B00, BVDT, BHTF, BOUT

### `claude-code/claude-liam-build-chapter-mapping`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-claudemd-constitution`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-dangerous-middle-activity`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-grading-skill-definition`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-pattern-analysis-subagent`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-post-build-document`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-pretooluse-grade-blocker`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-spec-prompt-template`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-three-check-deployment`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `claude-code/claude-liam-three-file-system-simulator`

- **Open bookend:** B00: present but pattern=None
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (4):** B02, B03, B05, YOURTURN

### `behind-the-model/silent-omission-signal`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, B07

### `behind-the-model/verification-matrix`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, B06

### `claude-cowork/claude-liam-be-good-at-claude`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-chatgpt-vs-claude`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-101`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-code`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-connectors`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-cowork`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-design`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-fable-5`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-for-excel`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-for-your-team`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-linkedin`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-skills`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-claude-to-sound-like-you`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-five-claudes-explained`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-how-to-prompt`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-nine-prompt-writing-skills`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-six-claude-formulas`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-stop-hitting-claude-limits`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-stop-prompting-claude`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/claude-liam-stop-writing-like-ai`

- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `claude-cowork/earnings-preview-verbatim-gate`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, OUTRO

### `claude-cowork/equity-research-initiating-coverage-gate`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, OUTRO

### `claude-cowork/financial-dcf-live-formula`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, OUTRO

### `claude-cowork/managed-agents-two-object-split`

- **Unrendered Remotion boxes (3):** B00, YOURTURN, OUTRO

### `behind-the-model/claude-constitution-honesty-standard`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `behind-the-model/claude-constitution-many-hands`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `behind-the-model/claude-constitution-operator-floor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `behind-the-model/claude-constitution-stable-identity`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `behind-the-model/claude-constitution-thousand-senders`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** B01, YOURTURN, OUTRO

### `behind-the-model/jacobian-lens-reading-ahead`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** A11, YOURTURN, OUTRO

### `behind-the-model/model-written-evals-inverse-scaling`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (3):** A11, YOURTURN, OUTRO

### `behind-the-model/political-neutrality-eval-two-graders-rank-every-topic`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/scone-bench-benchmark-score-may-memorization-score`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/sleeper-agents-paper-ai-s-hidden-scratchpad-blind`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/vox-bainbridge-irony`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/vox-fluency-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/vox-self-check-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/vox-silent-omission`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/vox-team-fence-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/agent-sdk-workshop-adding-one-capability-time-changes`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/agent-sdk-workshop-agent-s-memory-guardrail-one`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/agent-sdk-workshop-parallelism-prompt-problem-code-problem`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/anthropic-tools-channel-returns-tool-results-also`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/claude-agent-sdk-demos-interleaved-parallel-tool-logs-still`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/claude-agent-sdk-typescript-sending-full-list-beats-sending`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/claude-cookbooks-cheap-worker-crew-reads-9`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/claude-for-legal-one-context-flag-flips-every`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/claude-quickstarts-waiting-each-result-before-next`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/cwc-long-running-agents-agent-will-mark-feature-done`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/cwc-workshops-cutting-402-line-agent-prompt`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/financial-services-untrusted-document-s-hidden-instructions`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/healthcare-no-family-history-pe-needs`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/healthcare-prior-auth-ai-structurally-cannot`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/healthcare-swapping-fast-model-made-whole`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-agent-skills/launch-your-agent-autonomous-agent-freeze-mid-run`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/anthropic-sdk-php-server-hands-back-encrypted-context`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/anthropic-sdk-typescript-partial-json-valid-object-before`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claude-constitution-one-narrow-safety-rule-make`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claude-cookbooks-splitting-chunk-from-document-makes`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claude-quickstarts-50-turn-agent-pays-same`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claude-quickstarts-claude-s-click-lands-wrong`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claudeforfoundationmodels-same-api-key-shipped-prototype`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/claudeforfoundationmodels-web-search-never-runs-code`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-basics/evals-model-says-i-have-no`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/agentic-loop-not-chatgpt`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/boondoggle-score-anatomy`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/brutalist-three-file`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-code-action-natural-trigger-review-counting-check`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-base-action-turn-budget-stops-runaway-agent`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-coding-assistant-deliberately-refuses-write`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-four-agents-scoring-same-bug`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-monitoring-guide-doubling-claude-code-session-time`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-monitoring-guide-typing-one-word-multiply-api`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-code-security-review-same-eval-real-bug-one`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-liam-agentic-loop-not-chatgpt`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-ai-homework-fluency-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-code/claude-liam-boondoggle-score-anatomy`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-brutalist-three-file`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-clear-vs-compact`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-conducting-not-prompting`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-five-questions-before-code`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-gru-slash-v0-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-hook-advisory-vs-deterministic`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-intent-layer-authorship`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-one-sentence-problem-statement`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/claude-liam-plan-mode-interruption`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-prompt-is-a-wish-spec-is-a-contract`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-code/claude-liam-rewind-not-fix-forward`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-skill-build-once`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-slash-context-window-check`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-spec-vs-prompt-live`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-spec-writing-is-cs-ed`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claude-liam-vox-buildlog-assessment`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-code/claude-liam-vox-subagent-context`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-code/claude-liam-writer-reviewer-pattern`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/claudes-c-compiler-assembly-shrinks-through-13-sequential`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/clear-vs-compact`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/conducting-not-prompting`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/defending-code-reference-harness-count-field-checked-one-pass`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/defending-code-reference-harness-pipeline-runs-same-crash-three`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/five-questions-before-code`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/gru-slash-v0-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/hook-advisory-vs-deterministic`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/intent-layer-authorship`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/one-sentence-problem-statement`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/plan-mode-interruption`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/rewind-not-fix-forward`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/riv2025-long-horizon-coding-agent-demo-backend-test-passes-reali`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/riv2025-long-horizon-coding-agent-demo-wildcard-covering-every-a`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-code/skill-build-once`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/slash-context-window-check`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/spec-vs-prompt-live`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/spec-writing-is-cs-ed`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-code/writer-reviewer-pattern`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-cowork/access-ladder-explained`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-cowork-access-ladder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-cowork-task-packet`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-extraction-schema-first`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-nondelegation-checklist`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-plan-review-checklist`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-report-claim-tracing`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-seven-field-brief`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-cowork/claude-liam-synthesis-vs-deciding`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/claude-liam-vox-batch-propagation`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-coherent-unsafe`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-compression-caveats`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-exposure-gate`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-format-credibility`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-instruction-channel`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-same-prescription`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-vox-scope-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/claude-liam-workflow-card-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/cowork-access-ladder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/cowork-task-packet`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/extraction-schema-first`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/nondelegation-checklist`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/plan-review-checklist`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/report-claim-tracing`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/seven-field-brief`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-cowork/synthesis-vs-deciding`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-cowork/vox-batch-propagation`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-coherent-unsafe`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-compression-caveats`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-exposure-gate`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-instruction-channel`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-same-prescription`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/vox-scope-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-cowork/workflow-card-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/advising-privacy-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/assignment-stress-test`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/capstone-unit-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-advising-privacy-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-assignment-stress-test`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-capstone-unit-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-data-minimization-prompt`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-for-education/claude-liam-differentiation-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-faculty-literature-lead`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-instructional-brief-eight-fields`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-manuscript-reviewer-response`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/claude-liam-udl-choice-board`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/data-minimization-prompt`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-for-education/differentiation-audit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/faculty-literature-lead`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/instructional-brief-eight-fields`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/k12-teacher-skills-missing-math-prerequisite-t-scaffolded`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-for-education/manuscript-reviewer-response`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-for-education/udl-choice-board`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-mcp-connectors/claude-liam-mcp-resource-vs-tool`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-mcp-connectors/claude-liam-vox-mcp-blast-radius`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-mcp-connectors/github-mcp-server-giving-model-tools-makes-choose`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-mcp-connectors/github-mcp-server-one-generic-cli-drive-api`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-mcp-connectors/mcp-resource-vs-tool`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** B05, B06

### `claude-mcp-connectors/vox-mcp-blast-radius`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-code-plugin-seven-surfaces`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-plugins-community-copyright-restrictions-mean-three-compl`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-plugins-community-image-model-s-burned-captions`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-plugins-official-enabling-sms-breaks-access-control`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-plugins-official-live-bot-hands-pairing-codes`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/claude-plugins-official-same-assistant-code-runs-discord`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-plugins/knowledge-work-plugins-responding-webhook-after-processing-silen`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/agentic-approval-gate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/agentic-handoff-auditor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/anthropic-sdk-python-tool-calling-loop-stops-model`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/anthropic-sdk-typescript-schema-enters-types-travels-text`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-agentic-handoff-auditor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-constraint-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-constraint-extractor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-context-hygiene-demo`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/claude-liam-criteria-first-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-criteria-first-habit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-data-gigo-detector`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-examples-annotate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-failure-criterion-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-fluency-trap-correction`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-prompt-anatomy-auditor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-prompt-card-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-prompt-card-library`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-revision-change-log`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-scope-stack-setup`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/claude-liam-self-critique-loop`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-six-component-prompt`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/claude-liam-six-slot-anatomy`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/claude-liam-three-pass-refinement-demo`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-agentic-irreversible`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-citation-surface-format`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-context-priority-weight`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-criteria-before-output`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-examples-teach-more`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-prompt-injection`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-prompt-library-lost`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-prompt-six-slots`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-prompt-spec`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-self-review-sieve`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-surface-routing`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-vague-revision-spreads`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-liam-vox-writing-claim-invention`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/claude-quickstarts-agent-fresh-memory-every-session`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/constraint-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/constraint-extractor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/context-hygiene-demo`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/courses-asking-claude-json-gives-prose`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/courses-claude-handed-ten-tools-one`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/courses-three-graders-read-same-answer`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/criteria-first-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/criteria-first-habit`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/data-gigo-detector`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/examples-annotate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/failure-criterion-generator`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/fluency-trap-correction`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/prompt-anatomy-auditor`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-card-builder`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/prompt-card-library`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-eng-interactive-tutorial-claude-t-think-silently-reasonin`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-eng-interactive-tutorial-helpful-claude-invents-answer-pe`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-eng-interactive-tutorial-swapping-order-two-arguments-fli`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-eng-interactive-tutorial-telling-claude-logic-bot-turns`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/prompt-eng-interactive-tutorial-wrapping-one-email-tags-stops`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/revision-change-log`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/scope-stack-setup`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B06

### `claude-prompting/self-critique-loop`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/six-component-prompt`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/six-slot-anatomy`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B07

### `claude-prompting/three-pass-refinement-demo`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-agentic-irreversible`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-citation-surface-format`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-context-priority-weight`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-criteria-before-output`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-examples-teach-more`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-prompt-injection`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-prompt-library-lost`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-prompt-six-slots`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-prompt-spec`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-self-review-sieve`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-surface-routing`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-vague-revision-spreads`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-prompting/vox-writing-claim-invention`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/attribution-graphs-frontend-language-model-adds-two-numbers`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/claude-liam-context-dreaming`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, B44

### `claude-research/constitutionalharmlessnesspaper-safe-answer-one-argues-back`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/decompositionfaithfulnesspaper-answering-sub-questions-separate`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/hh-rlhf-safer-training-objective-gets-fewest`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/original-performance-takehome-ai-told-speed-up-program`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/sycophancy-to-subterfuge-paper-safety-test-passes-safety-test`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-research/toy-models-of-superposition-crowded-features-arrange-themselves`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-skills/skills-50-round-agent-survives-past`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-skills/skills-claude-spends-5000-thinking-tokens`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-skills/skills-claude-write-right-spreadsheet-formula`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `claude-skills/skills-number-s-color-financial-model`

- **Open bookend:** B00: present but pattern=None
- **Unrendered Remotion boxes (2):** YOURTURN, OUTRO

### `behind-the-model/political-neutrality-eval-paired-prompts`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-basics/computer-use-best-practices`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claudes-c-compiler`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/cwc-how-we-claude-code`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/cwc-workshop-agent-battle-minecraft`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/cookbooks-metaprompt`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/courses-real-world-prompting-medical`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-avoiding-hallucinations`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-engineering-precognition`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-separating-data`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-tutorial-lesson-02-clear-and-direct`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-tutorial-lesson-03-role-prompting`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-prompting/prompt-tutorial-lesson-05-formatting-output`

- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/ai-creative-work-belongs-to-nobody`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/ai-homework-fluency-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-ai-creative-work-belongs-to-nobody`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-code-runs-ships-wrong`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-fluency-trap-danger-zone`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-pagination-bug-dangerous-middle`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-slopsquatting-hallucinated-package`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-string-similarity-semantic-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-tests-pass-user-fails`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-agentic-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-ai-feedback-bias`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-claudemd-length`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-code-oracle`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-handoff-conditions`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-hook-enforcement`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-rewind-respec`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-simulation-ownership`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/claude-liam-vox-spec-saves-time`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/code-runs-ships-wrong`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/fluency-trap-danger-zone`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/pagination-bug-dangerous-middle`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/prompt-is-a-wish-spec-is-a-contract`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/slopsquatting-hallucinated-package`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/string-similarity-semantic-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/tests-pass-user-fails`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-agentic-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-ai-feedback-bias`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-buildlog-assessment`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-claudemd-length`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-code-oracle`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-handoff-conditions`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-hook-enforcement`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-rewind-respec`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-simulation-ownership`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-spec-saves-time`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-code/vox-subagent-context`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/ai-ban-design-failure`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/artifact-vs-learning`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/assessment-by-design`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-ai-ban-design-failure`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-artifact-vs-learning`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-assessment-by-design`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-cognitive-friction-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-feedback-that-replaces`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-outcome-before-topic`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-receiving-vs-producing`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-rubric-adjective-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/claude-liam-vox-phase-gate`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/cognitive-friction-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/feedback-that-replaces`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/outcome-before-topic`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/receiving-vs-producing`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/rubric-adjective-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `claude-for-education/vox-phase-gate`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)
- **Close bookend:** MISSING (no BOUT/NBB03/OUTRO and last beat is not ClaudeTitleOutro)
- **Unrendered Remotion boxes (1):** YOURTURN

### `behind-the-model/claude-liam-correlated-failure-research`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-independent-verification-protocol`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-legitimacy-auditor`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-risk-tiered-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-self-check-vs-independent-verification`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-solve-verify-asymmetry`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-supervision-calibration-logger`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-three-level-supervision-classifier`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-type-iii-error-detector`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/claude-liam-vox-bainbridge-irony`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)

### `behind-the-model/claude-liam-vox-fluency-trap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)

### `behind-the-model/claude-liam-vox-self-check-loop`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)

### `behind-the-model/claude-liam-vox-silent-omission`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)

### `behind-the-model/claude-liam-vox-team-fence-gap`

- **Open bookend:** MISSING (no B00/NBB00 and first beat is not ClaudeComposerAsk)

### `behind-the-model/correlated-failure-research`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/evals-same-question-gets-different-answer`

- **Open bookend:** B00: present but pattern=None

### `behind-the-model/headvis-one-always-present-token-secretly`

- **Open bookend:** B00: present but pattern=None

### `behind-the-model/independent-verification-protocol`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/jacobian-lens-model-spells-word-right-inside`

- **Open bookend:** B00: present but pattern=None

### `behind-the-model/legitimacy-auditor`

- **Open bookend:** B00: present but pattern='NikBearBrownOpen'

### `behind-the-model/model-cards-re-reading-own-order-back`

- **Open bookend:** B00: present but pattern=None

### `behind-the-model/nbb-correlated-failure-research`

- **Open bookend:** NBB00: present but pattern='FormBCard'

### `behind-the-model/nbb-independent-verification-protocol`

- **Open bookend:** NBB00: present but pattern='FormBCard'

### `behind-the-model/nbb-irreversible-action-gate`

- **Open bookend:** NBB00: present but pattern='FormBCard'

### `claude-agent-skills/claude-skills-progressive-disclosure`

- **Open bookend:** B00: present but pattern=None
