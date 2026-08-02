## prompt-tutorial-lesson-03-role-prompting

- **Source path:** prompt-eng-interactive-tutorial/Anthropic 1P/03_Assigning_Roles_Role_Prompting.ipynb
- **Teachable claim:** Telling Claude it is a "senior software engineer" or a "pediatric nurse" activates domain vocabulary and calibrated caution — role assignment is the cheapest way to change the register, depth, and audience-appropriateness of every response.
- **Suggested builder:** claude-explainer
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–3 min)

### Visual beats
1. Same question, three roles: "explain TCP/IP" with no role vs. "explain as a networking professor" vs. "explain as if I'm 10" — output comparison
2. Caution calibration: nurse role adds safety caveats that the plain-assistant role skips
3. System prompt placement: where the role goes (system vs. user message) and why system is preferred
4. Limits: role prompting doesn't grant capabilities the model lacks — what it changes vs. what it can't

### Score
- Teachability: 4/5 — role prompting is underused by beginners and the calibration effect is surprising
- Visual: 3/5 — three-way output comparison is readable
- Pull: 3/5 — widely applicable; clear benefit for anyone building with Claude
- Freshness: 2/5 — established technique
- **Total: 12/20**
