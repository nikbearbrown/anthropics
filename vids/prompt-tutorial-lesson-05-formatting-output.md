## prompt-tutorial-lesson-05-formatting-output

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/05_Formatting_Output_and_Speaking_for_Claude.ipynb
- **Teachable claim:** You can pre-fill Claude's response by providing a partial assistant message — `{"role": "assistant", "content": "The answer is:"}` — which forces Claude to continue from that exact text, enabling precise output format control without post-processing.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (3–4 min)

### Visual beats
1. The prefill technique: messages array ending with a partial assistant turn — shown in code, then the output
2. Format forcing: prefill with `{` forces JSON; prefill with `1.` forces numbered list
3. Limitation note (Claude 4+ change): recent models handle prefill differently — the notebook flags this change explicitly
4. Alternative approach: `stop_sequences` to terminate output at a marker — complementary technique

### Score
- Teachability: 4/5 — prefill is a powerful and non-obvious technique
- Visual: 3/5 — code-focused but the output comparison is clear
- Pull: 3/5 — developers building structured output pipelines need this
- Freshness: 3/5 — prefill behavior changed in Claude 4.6; this lesson is newly relevant
- **Total: 13/20**
