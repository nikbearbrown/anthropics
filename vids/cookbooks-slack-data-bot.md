## cookbooks-slack-data-bot

- **Source path:** claude-cookbooks/managed_agents/slack_data_bot.ipynb
- **Teachable claim:** A Slack bot that accepts CSV uploads and returns a narrative analysis report — built with Bolt for Python and a Claude Managed Agent session — handles the Slack 3-second ack rule by firing the slow CMA work on a background thread and streaming the result back to the thread.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** medium (5–7 min)

### Visual beats
1. The 3-second ack rule: Slack retries any unacknowledged event; show `ack()` called immediately, then `threading.Thread(target=start_analysis)` spun off — the handler returns in milliseconds
2. CSV upload flow: user @mentions bot with a CSV attachment; bot uploads the file to CMA Files API; creates a session with the file resource attached; sends `user.define_outcome` with "analyze and explain the key trends"
3. Streaming back to Slack: as the CMA session streams events, the bot appends to the thread message using `slack.chat.update`; the reply builds in the thread in near-real-time
4. Console trace: open the Console Sessions view to show the full agent trace behind the Slack reply — the CSV read, the pandas analysis, the chart generation

### Score
- Teachability: 5/5 — the Slack 3-second ack + background thread + streaming update pattern is reusable for any slow-computation bot
- Visual: 4/5 — live Slack thread building up as the analysis streams is inherently demonstrable
- Pull: 4/5 — Slack + data analysis is a very common enterprise workflow
- Freshness: 4/5 — Slack bots exist but the CMA + streaming update pattern is new
- **Total: 17/20**
