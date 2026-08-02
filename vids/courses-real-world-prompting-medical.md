## courses-real-world-prompting-medical

- **Source path:** courses/real_world_prompting/02_medical_prompt.ipynb
- **Teachable claim:** A medical prompt is the hardest single prompt to write correctly — it requires role definition, uncertainty language calibration, safety escalation triggers, and explicit "do not diagnose" guardrails — and getting any one wrong has real consequences.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (4–5 min)

### Visual beats
1. The bad medical prompt: missing safety language → Claude gives a confident answer to a dangerous question
2. The good prompt: each guardrail element labeled — role, uncertainty, escalation trigger, disclaimer
3. Uncertainty calibration: "likely", "possible", "you should see a doctor" — the language ladder
4. Escalation trigger: the prompt conditions that make Claude redirect to emergency services

### Score
- Teachability: 5/5 — medical prompting is where stakes make the lesson memorable
- Visual: 4/5 — annotated prompt comparison is readable and impactful
- Pull: 4/5 — anyone building health AI needs this; everyone else finds it compelling as a stakes example
- Freshness: 3/5 — medical AI prompting is an active area with ongoing guidance updates
- **Total: 16/20**
