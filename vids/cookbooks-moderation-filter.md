## cookbooks-moderation-filter

- **Source path:** claude-cookbooks/misc/building_moderation_filter.ipynb
- **Teachable claim:** A content moderation filter built with Claude is just a prompt — you define ALLOW and BLOCK categories with descriptions, insert the user text, and Claude returns one word; this works better than most ML classifiers for subjective categories because you can update the rules in natural language.
- **Suggested builder:** terminal-screencast
- **Suggested channel:** claude-liam
- **Runtime estimate:** short (2–3 min)

### Visual beats
1. The minimal prompt structure: BLOCK/ALLOW categories as text, `{USER_TEXT}` slot, "respond with one word"
2. Live moderation: various edge cases submitted — Claude's one-word classifications appearing
3. Rule update demo: adding a new BLOCK subcategory in natural language → behavior changes immediately, no retraining
4. Cost comparison: Claude moderation at scale vs. fine-tuning a classifier

### Score
- Teachability: 4/5 — "moderation as a prompt" is a useful mental model shift
- Visual: 3/5 — mostly terminal with classification outputs
- Pull: 4/5 — content moderation is a universal requirement for consumer AI products
- Freshness: 2/5 — LLM-based moderation is established
- **Total: 13/20**
