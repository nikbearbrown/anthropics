# Pharma Marketing with AI — CLI Video Ideas ("X with Claude")

> Note: As of scouting (2026-07-12), the book's chapters are placeholders — the frontmatter, introduction, chapter 1, and back matter all contain `[PLACEHOLDER]` blocks with no substantive content. Cards below are drawn from the book's title, stated scope (pharma marketing + AI tools), and the structural signals visible in the scaffolding (a Cowork enrichment pass that generates D3 figures per chapter, a planned LLM-exercise track). When the chapters are written, these cards should be revisited and grounded in chapter specifics.

---

## Candidate 01 — Research the Sunshine Act: Map Open Payments Data with Claude
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; chapter currently placeholder)
- Lane: RESEARCH (Claude assistant)
- Hook: The Sunshine Act has published 15+ years of physician payment records — but nobody outside compliance circles knows what patterns are actually hiding in the public data. What does AI-assisted research reveal about the landscape?
- The artifact: a sourced 2-page brief with an annotated bar chart (Manim animated reveal) showing total Open Payments by payment category (meals, speaker fees, consulting, research) for 2023, cross-referenced with top therapeutic areas and flagged regulatory findings from ProPublica Dollars for Docs.
- Prompt seed: `claude "Research the CMS Open Payments database for 2023. Summarize: (1) total payments by category, (2) top 5 therapeutic areas by physician payment volume, (3) one documented regulatory action citing Open Payments data. Output a sourced brief and flag claims you cannot verify."`
- Read / check: Verify payment totals against CMS Open Payments dashboard (openpaymentsdata.cms.gov). Confirm therapeutic-area ranking against published analyses (JAMA, Health Affairs). Check that no figures are hallucinated — every dollar figure must cite the CMS data download directly.
- Human supplies: Download the 2023 CMS Open Payments CSV from openpaymentsdata.cms.gov — the file is public but large (~1 GB); Claude cannot fetch it directly. A pre-filtered subset by therapeutic area is acceptable for the video.
- Output medium: Manim (animated bar chart with category breakdown, bars growing left-to-right, final frame highlighting the regulatory-flag category in red)
- The change: Re-run the research prompt restricted to a single therapeutic area (e.g., oncology) and compare the category mix — does oncology skew more toward speaking fees than the average?
- Teardown angle: The data has been public for a decade. The gap between what the data shows and what pharma marketing practices actually look like is the story — and Claude can surface it in minutes that previously took journalists weeks.
- Exclusions: HIPAA details, specific physician names, any data not in the public CMS download.
- Score: 7/10

---

## Candidate 02 — Build an AI Ad-Copy Classifier with Claude
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; placeholder)
- Lane: BUILD (Claude Code)
- Hook: FDA requires every pharma ad to balance efficacy and risk claims — but nobody has a fast way to audit whether a draft ad actually passes that balance test before it goes to the regulatory review queue.
- The artifact: a Python script (~35 lines) that takes a pharma ad text as input, prompts Claude to classify each sentence as "efficacy claim," "risk disclosure," "benefit-risk balanced," or "promotional only," and outputs a colored terminal table plus a balance ratio (efficacy sentences / risk sentences). Animated screen-recording shows the script running on two real FDA-cited example ads.
- Prompt seed: `claude "Write a Python script that reads a pharma ad text from stdin and calls the Claude API to classify each sentence as: efficacy_claim | risk_disclosure | balanced | promotional_only. Print a color-coded table with sentence, label, and confidence. Compute the efficacy:risk ratio at the end."`
- Read / check: Verify that the generated Python correctly imports `anthropic`, handles the API call, and parses structured output. Spot-check classification on 5 known FDA-cited ads (FDA's Bad Ad Program examples are public) — does the ratio flag the ones FDA cited for imbalance?
- Human supplies: Three real FDA "bad ad" examples — downloadable from FDA's Bad Ad Program website (public). Nothing proprietary needed; synthetic stand-in acceptable for the video demo.
- Output medium: screen-recording mp4 (terminal running the classifier, colored output visible, ratio displayed)
- The change: Add a second pass where Claude suggests a rewrite of the lowest-scoring sentence to improve the balance ratio — one revision loop visible in the recording.
- Teardown angle: Regulatory review of pharma copy is expensive and slow. A Claude-powered pre-screen doesn't replace the reviewer, but it surfaces the worst imbalances before the clock starts — the same 10-minute analysis that currently takes a compliance team a day.
- Exclusions: Actual FDA submission workflows, specific drug approval status, any proprietary brand copy.
- Score: 8/10

---

## Candidate 03 — Research AI Tools Actually Used in Pharma Marketing: A 2025 Landscape
- Source: pharma-marketing-with-ai/chapters/01-introduction.md (anticipated scope; placeholder)
- Lane: RESEARCH (Claude assistant)
- Hook: Everyone says "pharma is adopting AI," but the specific tools, vendors, and use cases are scattered across white papers and press releases. What does a Claude-powered landscape synthesis actually reveal?
- The artifact: a sourced comparison table (6 tools × 5 criteria: use case, regulatory clearance status, data-privacy posture, claimed ROI metric, one documented case study) formatted as a Manim-animated slide-reveal, one row appearing per beat.
- Prompt seed: `claude "Research the current (2024-2025) AI tool landscape for pharmaceutical marketing. Identify 6 specific tools or vendors with documented pharma marketing use cases. For each: state the use case, whether FDA/regulatory guidance applies, their data-privacy approach, their claimed ROI metric, and one citable case study. Flag any claim you cannot verify from a public source."`
- Read / check: Each tool name must be verifiable (company website or press release). ROI claims must cite a named source. Any flagged unverifiable claims stay flagged in the output — do not paper over them.
- Human supplies: Nothing — fully synthetic from public sources. The human should skim the output for vendor claims that sound too good to be true and cross-check 2-3 against the source URLs Claude cites.
- Output medium: Manim (table reveal, one row per beat, with a "VERIFY" flag icon appearing next to unverified claims)
- The change: Ask Claude to rank the 6 tools by regulatory risk exposure and explain the ranking — which tools are closest to patient data and therefore most exposed to FDA oversight?
- Teardown angle: The landscape is noisy and vendor-driven. A systematic Claude research pass surfaces the tools with actual documented use cases versus those running on press releases — and the regulatory risk map changes the ranking entirely.
- Exclusions: Any claims about specific drug performance, clinical data, or FDA submissions. No proprietary vendor agreements.
- Score: 7/10

---

## Candidate 04 — Build a Pharma HCP Segmentation Script with Claude Code
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; Cowork enrichment pass hints at D3 figure generation per chapter)
- Lane: BUILD (Claude Code)
- Hook: Pharma marketing teams segment physicians by specialty and volume — but the segmentation logic is usually buried in a spreadsheet with no documentation. What if Claude could write the segmentation script from a plain-English spec?
- The artifact: a Python script (~40 lines) that reads a synthetic physician CSV (NPI, specialty, TRx volume, state) and outputs four segments (High-Volume Specialist, Mid-Volume Specialist, Low-Volume GP, Non-Prescriber) with counts and a summary table. Manim animates the segment-flow diagram (four labeled boxes with arrow sizes proportional to physician count).
- Prompt seed: `claude "Write a Python script that reads a CSV with columns: NPI, specialty, TRx_volume, state. Segment physicians into: High-Volume Specialist (TRx>500, specialty in [oncology, cardiology, endocrinology]), Mid-Volume Specialist (TRx 100-500, same specialties), Low-Volume GP (TRx<100 or specialty=GP), Non-Prescriber (TRx=0). Print a summary table with counts and percentages. Use only the standard library and pandas."`
- Read / check: Verify segment boundaries match the prompt. Run on a synthetic 100-row CSV and confirm no physician is double-counted or dropped. Check edge cases: TRx exactly 500, specialty not in the list.
- Human supplies: A synthetic 100-row physician CSV — Claude can generate it. Real NPI data from CMS is public but optional; the video uses the synthetic CSV throughout.
- Output medium: Manim (sankey/flow diagram showing physicians routing into four segment boxes, animated arrows, final frame showing count labels)
- The change: Add a fifth segment — "Sleeping Dog" (TRx>200 but historically non-responsive to detailing) — and ask Claude to explain how you'd operationally identify them without access to actual rep-visit data.
- Teardown angle: The segmentation logic is trivially expressible in 10 lines of English. The real value Claude adds is the edge-case handling — the TRx=500 boundary, the specialty mapping — which is where the spreadsheet usually silently gets it wrong.
- Exclusions: Any real physician NPI data, any actual prescribing records, IQVIA/Symphony data.
- Score: 7/10

---

## Candidate 05 — Research the Regulatory Line: What AI in Pharma Marketing Requires FDA Attention
- Source: pharma-marketing-with-ai/chapters/01-introduction.md (anticipated scope; placeholder)
- Lane: RESEARCH (Claude assistant)
- Hook: FDA has issued guidance on digital health, social media, and AI — but where exactly does "AI-generated pharma marketing content" sit in the regulatory framework? Most teams don't know.
- The artifact: a sourced 3-section brief: (1) FDA guidance documents that apply to AI-generated marketing content with publication dates, (2) one documented enforcement action involving digital pharma marketing, (3) a yes/no matrix: 8 AI marketing use cases × regulatory-review required (Manim-animated table reveal).
- Prompt seed: `claude "Research FDA regulatory guidance applicable to AI-generated pharmaceutical marketing content as of 2025. List specific guidance documents with dates. Identify one documented FDA enforcement action involving digital or social media pharma marketing. Create a yes/no matrix for these 8 use cases and whether FDA submission or review is likely required: [ad copy generation, email personalization, chatbot HCP interaction, social media targeting, clinical claim generation, rep call planning, medical education content, patient support messaging]. Flag every claim you cannot verify from a public FDA document."`
- Read / check: All cited FDA guidance must have a real FDA.gov URL. The enforcement action must be verifiable from the FDA warning letter database (public). The matrix cells must cite the specific guidance that informs each yes/no — no bare assertions.
- Human supplies: Nothing — fully synthetic from public FDA sources. Human should verify 3-4 matrix cells against the cited guidance documents.
- Output medium: Manim (animated matrix, rows appearing one at a time, red/green cells for yes/no, citation footnotes appearing below)
- The change: Ask Claude to explain which of the 8 use cases has the most legal ambiguity — where the guidance is genuinely unclear — and to cite the gap.
- Teardown angle: The regulatory picture is not as murky as pharma compliance teams claim. The guidance exists; the ambiguity is real but bounded. A Claude research pass surfaces the specific gaps versus the clearly-settled cases — which changes the conversation with legal entirely.
- Exclusions: Any specific drug NDA/sNDA submissions, specific brand enforcement actions, specific company legal strategy.
- Score: 7/10

---

## Candidate 06 — Build a Prompt-Audit Tool: Does Your AI Marketing Prompt Leak PHI Risk?
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; Cowork enrichment pass structure)
- Lane: BUILD (Claude Code)
- Hook: Marketing teams are pasting physician data into AI tools without knowing whether those prompts are creating HIPAA exposure. A 20-line Claude script can flag the risk before it becomes a breach.
- The artifact: a Python script (~25 lines) that reads a draft marketing prompt from stdin and uses Claude to classify it on three axes: (1) contains PII/PHI risk (yes/no + reason), (2) references identifiable physician or patient data (yes/no), (3) recommended data-handling tier (public OK / de-identified only / PHI — do not use AI). Output: a terminal report with color-coded risk flags.
- Prompt seed: `claude "Write a Python script that reads a marketing prompt from stdin and calls the Claude API to assess it on three axes: (1) PII/PHI risk presence (yes/no with one-sentence reason), (2) whether it references identifiable physician or patient data, (3) recommended data-handling tier: public_ok | deidentified_only | phi_do_not_use. Output a color-coded terminal report. Add a disclaimer that this is a screening tool, not legal advice."`
- Read / check: Verify the Python compiles and runs. Test on three prompts: a clearly safe one (generic disease education), a borderline one (aggregate prescribing data), and a clearly risky one (physician name + prescription pattern). Confirm the tiers match the risk level.
- Human supplies: Three test prompts — Claude generates them synthetic. No real PHI needed or appropriate.
- Output medium: screen-recording mp4 (terminal showing three test prompts processed sequentially, color-coded output, clear disclaimer displayed)
- The change: Add a fourth axis — "would this prompt be logged by the AI vendor?" — and ask Claude to explain what the typical AI vendor logging policy implies for pharma data governance.
- Teardown angle: The biggest pharma AI risk isn't a sophisticated attack — it's a marketing manager pasting physician names into ChatGPT. A two-minute screening pass catches the obvious cases before they become compliance problems.
- Exclusions: Actual HIPAA legal advice, specific vendor privacy policies (which change), any real patient or physician data.
- Score: 8/10

---

## Candidate 07 — Research KOL Mapping: What Public Data Can You Build a KOL Network From?
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; placeholder)
- Lane: RESEARCH (Claude assistant)
- Hook: Key Opinion Leader mapping is a multi-million-dollar consulting exercise in pharma. How much of that network can Claude reconstruct from public data alone — PubMed authorship, conference agendas, CMS Open Payments?
- The artifact: a sourced brief describing 4 public data sources for KOL identification (PubMed co-authorship, CMS Open Payments speaking fees, conference speaker lists, FDA advisory committee rosters) with a worked example: Claude traces a hypothetical KOL network in cardiology using only public data, yielding an annotated network graph (Manim animated edge-by-edge construction).
- Prompt seed: `claude "Research and describe 4 public data sources usable for pharmaceutical KOL network mapping in cardiology. For each: state the data source, access method, what KOL signal it provides, and one limitation. Then trace a hypothetical 5-node KOL network using only these public sources — name the nodes by role (e.g., 'senior researcher,' 'journal editor') rather than real names. Describe the edges (co-authorship, co-speaker, payment relationship). Flag all claims with their source."`
- Read / check: Each data source must have a verifiable public URL. The hypothetical network must be clearly synthetic — no real physician names. Confirm PubMed and CMS Open Payments are correctly described (access methods, data freshness).
- Human supplies: Nothing — fully synthetic. Human should verify 2 of the 4 data source descriptions against the actual databases.
- Output medium: Manim (animated network graph: nodes appear labeled by role, edges animate in one by one with edge-type labels, final frame shows full network with legend)
- The change: Ask Claude to identify which edge type (co-authorship, payment, or co-speaker) is the most predictive of actual KOL influence in a documented study — and cite the study.
- Teardown angle: The expensive part of KOL mapping isn't the data — it's the synthesis. Most of the network is recoverable from public sources in an afternoon with Claude. The value-add consultancies are selling is the proprietary supplementation, not the baseline.
- Exclusions: Any real physician names, any non-public commercial databases, any specific brand's KOL program.
- Score: 6/10

---

## Candidate 08 — Build a Content Personalization Prototype: Right Message, Right Specialty
- Source: pharma-marketing-with-ai/chapters/02-chapter-01.md (anticipated scope; placeholder)
- Lane: BUILD (Claude Code)
- Hook: Pharma marketing teams write one message and send it to every physician. A 40-line Claude script can generate specialty-tuned variants from a single master message — demonstrating what "personalization at scale" actually looks like in code.
- The artifact: a Python script (~40 lines) that takes a single pharma educational message as input, a list of 5 physician specialties, and produces one tailored variant per specialty — same clinical claim, different emphasis, vocabulary, and example calibrated to the specialty. Output: a terminal side-by-side comparison table. Screen-recording shows the script running live.
- Prompt seed: `claude "Write a Python script that takes a pharma educational message (drug efficacy claim, safety profile, dosing) and a list of physician specialties and produces one tailored version per specialty. The clinical claim must remain identical; only the framing, emphasis, and example may change. Use the Claude API with a system prompt that enforces: no off-label claims, no superlatives, balanced efficacy/risk framing. Print a side-by-side table of original vs. specialty-tailored message."`
- Read / check: Verify that each variant preserves the original efficacy/safety claim verbatim. Check that no variant introduces a superlative ("best," "most effective") not in the original. Run a diff between original and each variant to confirm the clinical core is unchanged.
- Human supplies: A synthetic example pharma educational message (Claude generates it) and a list of 5 specialties. Nothing proprietary needed.
- Output medium: screen-recording mp4 (terminal showing original message, then 5 variants appearing one by one in a comparison table, diff highlights visible)
- The change: Add a guardrail pass where Claude reviews each variant for FDA balance compliance (efficacy:risk ratio) and flags any variant that drifts from the original's balance.
- Teardown angle: Personalization at scale is not a technology problem — the technology is trivial. It's a governance problem: ensuring the tailored variants don't drift from the approved claim. The guardrail pass is the real product, not the personalization itself.
- Exclusions: Any real drug brand names, any specific FDA-approved labeling, any patient data.
- Score: 7/10
