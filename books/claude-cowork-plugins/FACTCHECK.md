# FACTCHECK — *Claude Cowork Plugins* (rev. & expanded, Spring 2026, "John Collins")

**Source file:** `claude-cowork-plugins.md` (≈15,400-word audiobook transcript)
**Checked:** 23 July 2026 · **Method:** every number and named claim verified against Anthropic's own repositories and current reporting.
**Bottom line:** The book's *conceptual* spine is sound — Cowork is real, plugins are real, they turn a generalist into domain specialists, and they require a paid plan. But three factual claims are wrong or stale as of July 2026, one is internally inconsistent with the book's own chapters, and the delivered transcript is riddled with speech-to-text errors (including "Cloud" for "Claude" throughout). None of the errors sink the book; all of them should be corrected before this text is used as a script.

---

## 1. Claim-by-claim verdict

| # | Claim (as stated in the book) | Verdict | Correct as of July 2026 | Source |
|---|---|---|---|---|
| 1 | "Claude Cowork launched in January 2026." | ✅ **Holds** | Cowork shipped as a desktop app in Jan 2026. | TechCrunch, 7 Jul 2026 |
| 2 | Cowork is "available on both Mac and Windows through the Claude Desktop application." | ⚠️ **Stale / incomplete** | True at time of writing, but on **7 July 2026** Cowork expanded to **web and mobile** (Max subscribers). "Mac and Windows only" is no longer accurate. | TechCrunch / 9to5Mac, 7 Jul 2026 |
| 3 | "Plugins require a paid plan… The free tier doesn't support plugins." | ✅ **Holds** | Cowork + plugins are excluded from Free; included in every paid tier. | suprmind pricing hub |
| 4 | Pricing: "Pro $20/month. Max $100/month. Teams or enterprise." | ⚠️ **Incomplete** | Pro **$20** ✅. But **Max has two tiers — $100 (5×) and $200 (20×)**; the book names only $100. Team ≈ $25/$125 per seat; Enterprise custom. | suprmind pricing hub |
| 5 | "There are 11 official plugins covering productivity, marketing, sales, research, data analysis, enterprise search, product management, customer support, legal, finance, and **recruiting**." | ❌ **Inaccurate** | See §2 — the count has grown past 11, "recruiting" is **not** a standalone plugin, and a generic "research" plugin doesn't exist (the official one is **bio-research**, life-sciences-specific). | anthropics/knowledge-work-plugins (GitHub) |
| 6 | Legal and Finance are two of the eleven plugins. | ✅ **Holds** (but see note) | They **are** two separate official plugins — yet the book's body merges them into one "Legal and Finance" chapter, which undercuts its own "one chapter per plugin" promise. | GitHub repo |
| 7 | Plugins connect to your *existing* tools (CRM, database, analytics) rather than replacing them; examples include Salesforce, HubSpot, Notion, Stripe, QuickBooks, Mixpanel, PostHog, Amplitude, Zendesk, Intercom. | ✅ **Holds** | Accurate description of how plugins use connectors; all named products are real. These are exactly the kind of names that **date** — see §4. | GitHub repo / plugin READMEs |
| 8 | "If you can install an app on your phone, you can install a Cowork plugin" / setup needs no coding. | ✅ **Holds** | Install is a guided, no-code flow. | claude.com/plugins |
| 9 | Percentage figures in domain chapters (80% first-draft, 40%/60% client-revenue, "raise prices by 15%," etc.). | ✅ **Holds** (illustrative) | These are hypothetical *examples*, not empirical claims — nothing to verify, but keep them framed as examples in any script. | n/a |

---

## 2. The "11 plugins" problem (the book's biggest factual issue)

The book's headline roster is **partly wrong and already out of date**:

- **"Recruiting" is not an official plugin.** Recruiting lives as a *skill* (`recruiting-pipeline`) inside the **Human Resources** plugin. The book lists it as one of the eleven *plugins* — and then never gives it a chapter. That's both a factual error and an internal inconsistency.
- **A generic "research" plugin doesn't exist.** The official research plugin is **`bio-research`**, scoped to life sciences (single-cell RNA analysis, bioinformatics). The book's Chapter 6 describes *market* research, which the bio-research plugin does not do. The market-research workflows the book teaches are real Cowork capabilities, but they aren't a dedicated "Research plugin."
- **The count has grown past eleven.** Anthropic's official `knowledge-work-plugins` repo now carries domain plugins the book never mentions — **engineering, design, operations, human-resources, bio-research** — plus **cowork-plugin-management**. Current third-party guides variously report "11" and "15." "Eleven" was plausibly right in Spring 2026; it isn't a stable number.

**What's verifiably real (Anthropic's own repo, July 2026):** productivity, marketing, sales, data, enterprise-search, product-management, customer-support, legal, finance, human-resources, engineering, design, operations, bio-research, plus plugin-management. The book covers ten of these well; it misnames one, invents one, and omits several newer ones.

---

## 3. Transcription artifacts in the delivered file (fix before scripting)

The `.md`/`.txt` is a raw speech-to-text pass and carries systematic errors that are **not** the author's — but they will read as errors if narrated as-is:

- **"Cloud" → "Claude"** everywhere ("Cloud Co-Work," "Cloud.com/download," "a Cloud subscription"). Pervasive.
- **"Co-Work" / "co-works"** → the product is **Cowork** (one word).
- **"general list"** → **"generalist."**
- **"outside council"** → **"outside counsel."**
- **"the plug-and-s is"** → **"the plugin is."**
- **"mix panel" / "post-hog"** → **Mixpanel / PostHog.**
- **"unglamerous"** → **"unglamorous."**
- **"a 50% sales team"** → almost certainly **"a SaaS sales team."**
- **"How a T works"** (Ch. 13) → likely **"how a stack works"** — verify against the audio.
- Title page: **"## untitled"** and a stray "untitled" — no real front matter.

None change meaning, but a clean pass is required before this becomes narration.

---

## 4. "Datable" flags for the explainers (DOUBLE-CHECK LAW)

Per the deep-explainer doctrine, the following will age the videos and should be **compressed to generic mechanisms, not stated as fixed facts**, in every reel:

- **The plugin count and exact roster** ("11 official plugins," the specific list). It's already moved. Say "a growing catalog of domain plugins," not a number.
- **Platform list** ("Mac and Windows"). Now also web + mobile. Say "wherever you run Claude."
- **Prices** ("$20," "$100"). Say "a paid plan" unless a price is the point of the beat.
- **Named third-party tools** (Salesforce, Mixpanel, etc.). Fine as fleeting examples; never as the beat's subject.
- **Any "as of [month]" framing.** Strip it.

---

## 5. Net assessment

The book is a **conceptually accurate, practically useful** guide whose *evergreen* content — what plugins are, why a generalist-plus-specialists model changes the math for small operators, how to install and customize, how the domain workflows feel — holds up cleanly and is exactly what the explainers should carry. Its *specifics* — the plugin count, the "recruiting" plugin, "Mac and Windows only," "$100 Max" — are wrong or stale and must be corrected here and stripped from the videos. Treat the book as a **strong source for structure and intuition, and an unreliable source for current specifics** — which, fittingly, is the exact caution the book raises about itself in its "A note on timing" section.

---

### Sources
- [Claude Cowork expands to mobile and web — TechCrunch (7 Jul 2026)](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)
- [Anthropic expanding Claude Cowork to mobile and web — 9to5Mac (7 Jul 2026)](https://9to5mac.com/2026/07/07/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/)
- [anthropics/knowledge-work-plugins — official plugin repository (GitHub)](https://github.com/anthropics/knowledge-work-plugins)
- [Human Resources plugin (recruiting-pipeline skill) — GitHub](https://github.com/anthropics/knowledge-work-plugins/tree/main/human-resources)
- [Claude subscription plans & pricing 2026 — suprmind](https://suprmind.ai/hub/claude/pricing/)
- [Plugins for Claude — claude.com/plugins](https://claude.com/plugins)
- [Anthropic knowledge-work plugins overview — ClaudeWorld](https://claude-world.com/articles/anthropic-knowledge-work-plugins-overview/)
