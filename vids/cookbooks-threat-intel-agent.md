## cookbooks-threat-intel-agent

- **Source path:** claude-cookbooks/tool_use/threat_intel_enrichment_agent.ipynb
- **Teachable claim:** A Claude tool-use agent replaces the security analyst's manual IOC pivot workflow — given an IP, file hash, or domain, it queries VirusTotal, AbuseIPDB, and MITRE ATT&CK in the right order, decides when enough evidence justifies a verdict, and writes a structured threat report without being told which tools to call.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The analyst's manual workflow: IP → VirusTotal → AbuseIPDB → ATT&CK cross-reference → report; count the 15 manual steps; the agent compresses them to one prompt
2. Tool definitions: four tools with detailed descriptions — the description is what tells Claude when to call each one; show a bad description vs. a good one and how it changes tool selection
3. Live run: paste a known-malicious IP; tool calls scroll in order; Claude decides to stop after AbuseIPDB confirms 87% confidence malicious — it doesn't call ATT&CK for an obvious case
4. Report output: structured INDICATOR / VERDICT / CONFIDENCE / EVIDENCE / MITRE block — show the schema enforced by the prompt, not by structured outputs

### Score
- Teachability: 5/5 — "the tool description is what the model uses to decide when to call it" is immediately applicable
- Visual: 4/5 — tool call sequence + structured report output is concrete and checkable
- Pull: 4/5 — security teams are a serious Claude user segment
- Freshness: 4/5 — threat intel agents exist but the tool-description-as-routing insight is underexplained
- **Total: 17/20**
