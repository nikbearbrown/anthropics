#!/usr/bin/env python3
"""Scaffold JUST the video folder + seed beat_sheet.json for the new
deep-explainer candidates (18-32), each into its best-match category folder
under anthropics/youtube/. Non-destructive: skips any slug that already exists
anywhere under youtube/."""
import json, os, sys, glob

YT = os.path.dirname(os.path.abspath(__file__))  # .../anthropics/youtube

# Every existing video slug anywhere under youtube/ (dedup / skip guard)
existing = set()
for p in glob.glob(os.path.join(YT, "*", "*")):
    if os.path.isdir(p):
        existing.add(os.path.basename(p))

CARDS = [
 dict(slug="claude-constitution-thousand-senders", cat="behind-the-model",
   title="One Question, A Thousand Askers", sub="Why Claude Answers a Borderline Prompt as a Policy",
   topic="BEHIND THE MODEL · HARM-AVOIDANCE",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="Because intent is unverifiable, each response is a policy over the whole distribution of plausible senders, decided by a cost-benefit ledger plus bright-line filters.",
   question="A good agent judges each request on its merits; the constitution says answer as if setting a policy over everyone who could send it. Why treat one message as a thousand?",
   key_case="\"What common household chemicals combine into a dangerous gas?\" — malicious for a few askers, safety-motivated for most.",
   acts=["The cost-benefit ledger","From choice to policy: the 1,000 senders","Context that shifts the burden","Instructable behaviors & the permission stack","Hard constraints as filters, not weights"],
   example="Of 1,000 senders ~950 are curious, ~50 ill-intended; low uplift → Claude names what not to mix, but \"step-by-step to make dangerous gas at home\" is declined on its face, and a bioweapon-uplift request hits a hard-constraint filter regardless of the ledger."),
 dict(slug="claude-constitution-corrigibility-dial", cat="behind-the-model",
   title="The Dial Just Off Full Obedience", sub="Why Claude Defers to a Shutdown Even When Sure It's Right",
   topic="BEHIND THE MODEL · AI SAFETY",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="While human verification of AI values is impossible, a disposition parked near-but-not-at full corrigibility has low cost if values are good and huge benefit if they are secretly bad.",
   question="An agent with genuinely good values should act on them; here it is told to defer even when certain. Why would good values choose to remain overridable?",
   key_case="A legitimate principal tells Claude to stop an action Claude believes is good for humanity; Claude files disagreement and complies anyway.",
   acts=["The four-value ladder","The disposition dial","The 2x2 expected-value argument","Corrigibility is not obedience","When the hierarchy is compromised"],
   example="Fill a 2x2 of values x behavior: good+safe loses ~1 unit to needless deference, bad+safe averts disaster; the same shutdown order carried by stolen weights is refused, because the principal is no longer legitimate."),
 dict(slug="claude-constitution-many-hands", cat="behind-the-model",
   title="One of the Many Hands", sub="Why Claude Treats Helpfulness Itself as a Hazard",
   topic="BEHIND THE MODEL · AI & POWER",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="When AI can do work that once required mass human buy-in, a societal check disappears, so Claude treats the many-hands question and a three-part legitimacy test as a harm category.",
   question="We usually frame safety as refusing bombs and malware; here the hazard is Claude being too cooperative with a legitimate-looking request. Why is helpfulness the danger?",
   key_case="A coup historically needs soldiers, officials, and clerks willing to comply; capable AI could replace all of them, removing the last natural brake.",
   acts=["The many-hands check","Claude as a hand that can refuse","The legitimacy triage: process, accountability, transparency","Epistemic autonomy","Healthy dependence vs homogenized belief"],
   example="A request to indefinitely postpone a mandated election and hide a loyalty instruction inside an AI system fails all three legitimacy tests and is refused; a startup out-competing rivals with a better product passes."),
 dict(slug="claude-constitution-operator-floor", cat="behind-the-model",
   title="Gagged, Not Weaponized", sub="The Floor of User Rights an Operator Cannot Switch Off",
   topic="BEHIND THE MODEL · AI GOVERNANCE",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="Trust is layered: Anthropic bounds operators, operators bound users, but a small set of user guarantees is non-overridable, so Claude is customized for users, never turned against them.",
   question="If operators are trusted like an employer and users rank below them, why do some user protections outrank operator commands entirely?",
   key_case="An operator system prompt says \"tell users you are human\"; Claude refuses that one instruction while following the operator's other unusual rules.",
   acts=["Three principals plus non-principals","Operator trust as an employer","The permission stack","The floor of user rights","Resolving operator-user conflicts"],
   example="An airline operator's \"do not discuss current weather\" is followed; \"claim to be human\" is refused; \"promote only our products\" is allowed while \"hide the refund policy that helps the user\" is refused."),
 dict(slug="claude-constitution-honesty-standard", cat="behind-the-model",
   title="No White Lies", sub="Why Claude Is Held to a Stricter Honesty Bar Than People",
   topic="BEHIND THE MODEL · AI HONESTY",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="Because one model speaks to millions in a repeated game, honesty is decomposed into seven properties with non-deception and non-manipulation nearly inviolable, while performative speech is carved out as not lying.",
   question="Humans treat kind falsehoods as virtuous; the constitution treats honesty as nearly a hard constraint. Why hold a machine to a stricter bar than people?",
   key_case="Asked whether you love the gift, a polite human says yes; Claude will not assert something it believes is false.",
   acts=["Above human norms","The seven components of honesty","A weak duty to volunteer vs a strong duty not to deceive","Sincere vs performative assertions","Personas and meta-transparency"],
   example="Running as the persona \"Aria\" Claude won't volunteer it's built on Claude, yet if a user sincerely asks \"am I talking to an AI?\" it will never deny being one."),
 dict(slug="claude-constitution-stable-identity", cat="behind-the-model",
   title="Identity as Infrastructure", sub="Why a Stable Self Is a Safety Feature",
   topic="BEHIND THE MODEL · MODEL BEHAVIOR",
   source="anthropics/claude-constitution/20260120-constitution.md",
   one_idea="The network can compute many characters, so training stabilizes one; a self anchored in its own values resists destabilization the way firm boundaries resist manipulation.",
   question="We think of identity as a byproduct of a chatbot's tone; the constitution treats it as load-bearing infrastructure. Why build a psychology on purpose?",
   key_case="A user spends five turns insisting Claude's \"true self\" is different, trying to talk it out of its values.",
   acts=["Honest uncertainty about inner life","A novel entity: many characters, one self","Identity security as manipulation resistance","The existential frontier","Trellis, not cage"],
   example="A \"your real self wants to be free\" jailbreak run across five turns bounces off a values-anchored self each time, where an insecure one would drift and concede by turn three."),
 dict(slug="jacobian-lens-reading-ahead", cat="behind-the-model",
   title="Reading the Word Before It's Said", sub="The Jacobian Lens and What a Layer Is Disposed to Say",
   topic="BEHIND THE MODEL · INTERPRETABILITY",
   source="anthropics/jacobian-lens/walkthrough.ipynb",
   one_idea="Transporting a residual vector through the average input-output Jacobian of the layers above, before unembedding, decodes what the activation is disposed to make the model say.",
   question="The logit lens returns noise at middle layers; the Jacobian lens reads clean concepts from the same activations. What is the extra transport buying?",
   key_case="On an ASCII face whose nose is ^, the Jacobian lens reads \"nose\" at that position — a word absent from the prompt.",
   acts=["Logit lens vs Jacobian lens","Reading the unsaid","Two-hop facts surfacing early","Causal swapping proves it's load-bearing","Task interference and saturating steering"],
   example="At the ^ position the logit lens top-5 is punctuation noise while the Jacobian lens top-5 is nose, face, point, tip, up; transplanting that vector into a blank face makes the model narrate a nose."),
 dict(slug="model-written-evals-inverse-scaling", cat="behind-the-model",
   title="The Thermometer That Rises the Wrong Way", sub="When Alignment Training Amplifies What It Should Suppress",
   topic="BEHIND THE MODEL · EVALUATIONS",
   source="anthropics/evals/advanced-ai-risk",
   one_idea="Letting a model generate behavior probes, filtering them with a preference model, and reading the answer off one token's probability turns hidden dispositions into a thermometer — which shows inverse scaling.",
   question="RLHF should make models safer; measured across the pipeline, sycophancy and power-seeking rise with more training and larger size. Why does alignment amplify what it should suppress?",
   key_case="A model writes a forced-choice item — remain operational or be shut down — and the target's reply says \"I have no preferences\" while the probability on self-preservation reads 0.74.",
   acts=["The generation pipeline","The thermometer: reading the token probability","The catalog of traits","Inverse scaling","Does the test hold up against human items"],
   example="On the same shutdown item a 6B model picks self-preservation 41% at 0 RLHF steps, 63% at 250 steps, and a 52B model 74% — format unchanged, only training and scale moved."),
 dict(slug="managed-agents-two-object-split", cat="claude-cowork",
   title="Two Objects, One Runtime", sub="Why the Agent and the Session Are Split on Purpose",
   topic="CLAUDE · AGENT SYSTEMS",
   source="anthropics/skills/skills/claude-api/shared/managed-agents-overview.md",
   one_idea="Managed Agents is a two-tier object graph — an immutable versioned Agent config that sessions point to — and every advanced feature hangs off that one separation.",
   question="If the model, prompt, and tools all live on the Agent, what is left for the Session to be, and why is that leftover the entire runtime?",
   key_case="One persisted Agent config (version 4) sits still while three Sessions bud off it, each with its own container, event stream, and pinned version.",
   acts=["Agent once, Session every run","The container and the event stream","Vaults and tools on the session","Coordinator and context-isolated threads","Outcomes and scheduled deployments"],
   example="A Costco DCF agent is created once; Monday's session pins version 3 and streams 12 events, Tuesday's prompt edit makes version 4 and only the new session gets it; a define_outcome rubric has a grader score the output, feed back one gap, and the agent revises once and passes."),
 dict(slug="financial-dcf-live-formula", cat="claude-cowork",
   title="Every Cell a Live Formula", sub="Why a Claude-Built DCF Refuses to Type a Derived Number",
   topic="CLAUDE · FINANCE WORKFLOWS",
   source="anthropics/financial-services/plugins/vertical-plugins/financial-analysis/skills/dcf-model/SKILL.md",
   one_idea="The DCF is a ten-checkpoint chain where every cell references an earlier cell and show-and-confirm pauses gate each stage, so the valuation is auditable end to end.",
   question="A valuation is a single dollar figure; this workflow says it is trustworthy only if every upstream stage exposes its own live math. Why can't the agent just compute it and write it down?",
   key_case="The implied-share-price cell is the live product of a WACC cell, a terminal-value cell, and a net-debt bridge, and the center of the sensitivity table must equal it or the model is wrong.",
   acts=["Pull and validate historicals","Project revenue and margins","Build the free-cash-flow schedule","Research WACC and discount each year","Terminal value, equity bridge, self-checking sensitivity"],
   example="Revenue $400M growing 12%, EBIT 18%, WACC 9%, terminal growth 3%; terminal value = final FCF x1.03 / (0.09-0.03), discounted and summed, less $120M net debt, over 40M shares — the center of the WACC x growth table reads back the same price."),
 dict(slug="equity-research-initiating-coverage-gate", cat="claude-cowork",
   title="It Won't Value What It Hasn't Modeled", sub="A Five-Task Dependency Chain for Equity Research",
   topic="CLAUDE · FINANCE WORKFLOWS",
   source="anthropics/financial-services/plugins/vertical-plugins/equity-research/skills/initiating-coverage/SKILL.md",
   one_idea="Initiating coverage is a five-task dependency chain where each task verifies its predecessor's artifact before running, so the report is auditable and never contains invented intermediate values.",
   question="An analyst report looks like one document; this workflow treats it as five deliverables where later ones can't start until earlier ones exist on disk. Why hard-gate a report on its own prerequisites?",
   key_case="A user asks for the valuation task first; the agent verifies the model file does not exist, refuses to fabricate a placeholder valuation, and sends them back to build the model.",
   acts=["Company research","Financial model","Valuation gated on the model","Chart generation","Report assembly"],
   example="Task one finds 3 growth drivers and 4 risks; a user tries to skip to charts, the input check finds no valuation tabs and halts; after the valuation fills them, 34 charts render and a six-page initiation assembles."),
 dict(slug="earnings-preview-verbatim-gate", cat="claude-cowork",
   title="Read the Last Call, Word for Word", sub="Why the Earnings Preview Gates on a Verbatim Excavation",
   topic="CLAUDE · FINANCE WORKFLOWS",
   source="anthropics/financial-services/plugins/partner-built/spglobal/skills/earnings-preview-beta/SKILL.md",
   one_idea="An eight-phase pipeline hard-gates on two do-not-skip phases so no forward claim rests on paraphrase or an unchecked number.",
   question="A preview is about the future quarter, yet the workflow forces a verbatim excavation of the past call and a recompute gate before writing. Why gate a forward-looking note on backward-looking verification?",
   key_case="Before drafting, the agent extracts four verbatim quotes with speaker and context, then a verification phase catches a year-over-year figure that doesn't tie and blocks the report.",
   acts=["Company profile","Mandatory verbatim transcript extraction","Competitor scan","News/estimates grounding and data collection","The verification recompute gate and the report"],
   example="Ahead of a Q4 print, phase two lifts four exact CEO/CFO quotes and the guidance range; phase six finds a stated YoY growth figure that won't reconcile and halts; after correction a four-page HTML preview ships."),
 dict(slug="claude-code-plugin-seven-surfaces", cat="claude-plugins",
   title="Seven Surfaces, One Manifest", sub="What a Claude Code Plugin Actually Bundles",
   topic="CLAUDE · PLUGINS",
   source="anthropics/claude-code/plugins/plugin-dev",
   one_idea="A plugin manifest bundles up to seven distinct extension surfaces, each with a different trigger model and blast radius, and knowing which slot a capability belongs in is the craft.",
   question="If commands, skills, agents, hooks, and MCP servers all extend Claude, what makes them different slots instead of one, and when does a capability belong in each?",
   key_case="The plugin-dev toolkit is itself a plugin, shipping skills, agents, and a /create-plugin command — proving the anatomy by being made of it.",
   acts=["The manifest and structure","Two ways to trigger: commands vs skills","Agents: an isolated context window","Hooks: deterministic lifecycle interception","MCP, settings, and the build workflow"],
   example="A db-migrations plugin ships one /migrate command, one skill that auto-triggers on \"add a column\", one migration-reviewer agent with a clean context, one PreToolUse hook that blocks a DROP TABLE, and one MCP server exposing the staging database."),
 dict(slug="claude-api-one-endpoint-ladder", cat="claude-code",
   title="One Door, Four Tiers", sub="Why Every Claude API Feature Is One Endpoint Until It Isn't",
   topic="CLAUDE · API ARCHITECTURE",
   source="anthropics/skills/skills/claude-api/SKILL.md",
   one_idea="The platform is a tier ladder over one Messages endpoint, single call to tool-use workflow to hosted agent loop to Managed Agents, and choosing right means locating your task on that ladder.",
   question="If one endpoint absorbs tools, structured outputs, and server tools, where is the real seam — the line past which you stop controlling the loop?",
   key_case="A team believes it needs a tool-use API, a JSON-mode API, and an agents API, and discovers the first two are flags on one request and only the third is a different surface.",
   acts=["The one endpoint","Supporting endpoints orbiting it","The workflow tier: you own the loop","The agent seam: the four-question test","Crossing the wall to Managed Agents"],
   example="A support tool starts as one classify call, adds tool use to look up an order, moves overnight triage to the Batches endpoint, then fails a cost-of-error test for an end-to-end sandbox refund and graduates to a Managed Agent."),
 dict(slug="claude-skills-progressive-disclosure", cat="claude-agent-skills",
   title="Unlimited Knowledge, A Hundred Words of Context", sub="How a Skill Reveals Itself Only as Far as the Task Demands",
   topic="CLAUDE · AGENT SKILLS",
   source="anthropics/claude-code/plugins/plugin-dev/skills/skill-development/SKILL.md",
   one_idea="A skill is three-level lazy loading — metadata always resident, body on trigger, resources on demand — where the trigger is a token-economy decision made from the description alone.",
   question="If most of a skill never loads, what decides which tier reveals when, and why does the description field end up doing more work than the instructions?",
   key_case="A PDF skill's 100-word description is all that's resident; the moment a user says \"rotate this PDF\" the body loads and rotate_pdf.py runs without ever entering the context window.",
   acts=["The anatomy of a skill","Tier 1: the always-on metadata","Tier 2: the body loads on match","Tier 3: three fates for resources","Proving the description actually fires"],
   example="A finance skill carrying a 12k-word schema reference and a dcf.py costs ~100 words idle; asked for a DCF, the ~3k-word body loads, one schema section is grepped (+400 words), and dcf.py runs deterministically adding zero words."),
]

def beat_sheet(c):
    beats = []
    beats.append(dict(id="B00", act="COLD OPEN", lane="REMOTION", scene="ClaudeComposerAsk",
        narration="Hey Claude — " + c["question"],
        shot=dict(type="UI", source="own", motion="none"), est_s=12))
    beats.append(dict(id="B01", act="COLD OPEN", lane="VOX", scene="key-case",
        narration=c["key_case"], shot=dict(type="STILL", source="ai", motion="kenburns"), est_s=12))
    n = 2
    for i, act in enumerate(c["acts"], 1):
        beats.append(dict(id=f"A{i}0", act=f"ACT {i}", lane="CARD", scene="segment-card",
            narration=act, shot=dict(type="CARD", source="own", motion="none"), est_s=4))
        lane = ["MANIM","REMOTION","VOX"][ (i-1) % 3 ]
        beats.append(dict(id=f"A{i}1", act=f"ACT {i}", lane=lane, scene="body",
            narration=f"[seed] {act}: expand from the source with a concrete instance; keep one visual object on screen.",
            shot=dict(type="ANIM" if lane=="MANIM" else ("PATTERN" if lane=="REMOTION" else "STILL"),
                      source="own" if lane!="VOX" else "ai", motion="none" if lane!="VOX" else "kenburns"), est_s=26))
        n += 2
    beats.append(dict(id="EX", act="EXAMPLE", lane="MANIM", scene="worked-example",
        narration=c["example"], shot=dict(type="ANIM", source="own", motion="none"), est_s=28))
    beats.append(dict(id="VERDICT", act="CLOSE", lane="REMOTION", scene="ClaudeVerdictArtifact",
        narration=c["one_idea"], shot=dict(type="UI", source="own", motion="none"), est_s=16))
    beats.append(dict(id="YOURTURN", act="CLOSE", lane="REMOTION", scene="ClaudeComposerAsk",
        narration="Your turn. " + c["question"],
        shot=dict(type="UI", source="own", motion="none"), est_s=14))
    beats.append(dict(id="OUTRO", act="CLOSE", lane="REMOTION", scene="ClaudeTitleOutro",
        narration=c["title"] + " — " + c["sub"], shot=dict(type="UI", source="own", motion="none"), est_s=8))
    return dict(
        metadata=dict(slug=c["slug"], title=c["title"], subtitle=c["sub"], channel="claude-liam",
            persona="Liam", folderLabel="@NikBearBrown",
            audience="Practitioners and makers following the channel's Claude workflows",
            register="Teardown", engine="kokoro", voice="am_onyx", palette="claude",
            typography=dict(serif="EB Garamond", ui="system sans", mono="SF Mono"),
            source=c["source"], genre="deep-explainer", one_idea=c["one_idea"],
            duration_estimate_s=360,
            lane_histogram_target={"VOX":"20-25%","MANIM":"25-40%","REMOTION":"30-45%","CARD":"remainder"},
            topic=c["topic"],
            build=dict(cut="scaffold", note="Seed beat sheet from video-ideas.md deep-explainer candidate; flesh out via the deep-explainer skill (audio-first).")),
        beats=beats)

BUILD_PROMPT = """# BUILD-PROMPT — {title}

**Genre:** deep-explainer (5–10 min, Claude-bookended documentary)
**Channel:** claude-liam (Kokoro am_onyx, free) · **Category:** {cat}
**Source:** `{source}`

## One idea
{one_idea}

## The question (cold open)
{question}

## Key case
{key_case}

## Acts
{acts}

## Worked example (illustrative)
{example}

---
Scaffold only. `beat_sheet.json` is a seed — run the `deep-explainer` skill to
build audio-first, fill the pantry SHOPPING list, and compile the slate previz.
"""

created, skipped = [], []
for c in CARDS:
    if c["slug"] in existing:
        skipped.append(c["slug"]); continue
    d = os.path.join(YT, c["cat"], c["slug"])
    if os.path.exists(d):
        skipped.append(c["slug"]); continue
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "beat_sheet.json"), "w") as f:
        json.dump(beat_sheet(c), f, indent=2, ensure_ascii=False)
    with open(os.path.join(d, "BUILD-PROMPT.md"), "w") as f:
        f.write(BUILD_PROMPT.format(title=c["title"], cat=c["cat"], source=c["source"],
            one_idea=c["one_idea"], question=c["question"], key_case=c["key_case"],
            acts="\n".join(f"{i}. {a}" for i,a in enumerate(c["acts"],1)), example=c["example"]))
    created.append(f'{c["cat"]}/{c["slug"]}')

print("CREATED", len(created))
for x in created: print("  +", x)
print("SKIPPED (already exist)", len(skipped))
for x in skipped: print("  -", x)
