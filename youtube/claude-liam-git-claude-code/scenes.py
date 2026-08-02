"""
scenes.py — claude-liam-git-claude-code
Manim fragments for four data-driven beats. All data verified from real repo.

Render command (from books/):
  ART_PALETTE=teardown manim -qh --fps 24 -r 1920,1080 \
    anthropics/youtube/claude-liam-git-claude-code/manim/scenes.py \
    B04_StructureMap

  Then: cp media/videos/.../B04_StructureMap.mp4 \
    anthropics/youtube/claude-liam-git-claude-code/manim/B04.mp4

VERIFIED DATA (all from git clone 2026-08-01):
  File counts: find . -type f | grep -v .git | sed 's/.*\\.//' | sort | uniq -c | sort -rn
    106 md, 27 json, 21 sh, 21 py, 8 tf, 5 ts
  Top-level dirs: find . -maxdepth 1 | grep -v .git | sort
  TypeScript files: find . -name '*.ts' | grep -v .git
    scripts/{auto-close-duplicates,backfill-duplicate-comments,
             issue-lifecycle,lifecycle-comment,sweep}.ts
  CHANGELOG versions: grep '^## [0-9]' CHANGELOG.md | wc -l = 353
    oldest: 0.2.21, newest: 2.1.220
  Commits: git log --oneline | wc -l = 222 (--depth=200 clone)
  Bot commits: 176 (chore: Update CHANGELOG.md = 103, + feed.xml = 73)
  Human commits: 46
  Monthly breakdown (git log --pretty=format:'%ad %s' --date=format:'%Y-%m'):
    2026-02: 50 total, 32 bot, 18 human
    2026-03: 31 total, 26 bot,  5 human
    2026-04: 35 total, 30 bot,  5 human
    2026-05: 42 total, 32 bot, 10 human
    2026-06: 37 total, 31 bot,  6 human
    2026-07: 27 total, 25 bot,  2 human
"""

from manim import *

# Claude brand palette (matches claude.ts tokens)
GROUND = "#FAF9F5"   # cream canvas
INK    = "#3D3929"   # warm dark ink
TERRA  = "#D97757"   # terracotta accent
SLATE  = "#8A7E72"   # structure / secondary text
RED    = "#C8102E"   # error / missing
DIM    = "#8A7E72"   # dim annotations
SERIF  = "EB Garamond"

config.background_color = GROUND


# ---------------------------------------------------------------------------
# B04 — StructureMap
# Horizontal bar chart of file counts by extension.
# 6 rows; .md bar terracotta (dominant 106); all others ink.
# ---------------------------------------------------------------------------

class B04_StructureMap(Scene):
    def construct(self):
        # All bars in INK; .md row gets full opacity to mark dominance (TERRA fails WCAG on cream)
        data = [
            (".md",   106, INK, 0.9),
            (".json",  27, INK, 0.35),
            (".sh",    21, INK, 0.35),
            (".py",    21, INK, 0.35),
            (".tf",     8, INK, 0.35),
            (".ts",     5, INK, 0.35),
        ]
        max_count = 106
        bar_width  = 7.5   # shorter bars keep count labels inside safe-x ±6.3
        bar_height = 0.55
        row_gap    = 0.22
        y_start    = 2.2
        x_start    = -4.2

        title = Text(
            "anthropics/claude-code — 210 files",
            font=SERIF, font_size=38, color=INK,
        ).to_edge(UP, buff=0.75)
        self.play(FadeIn(title, run_time=0.5))
        self.wait(0.2)

        bars = []
        for i, (ext, count, color, opacity) in enumerate(data):
            y = y_start - i * (bar_height + row_gap)
            w = bar_width * count / max_count

            ext_label = Text(ext, font=SERIF, font_size=28, color=INK).move_to(
                [x_start - 0.7, y, 0]
            )
            bar = Rectangle(
                width=w, height=bar_height,
                fill_color=color, fill_opacity=opacity,
                stroke_width=0,
            ).move_to([x_start + w / 2, y, 0])
            count_label = Text(
                str(count), font=SERIF, font_size=26, color=INK
            ).next_to(bar, RIGHT, buff=0.15)

            bars.append((ext_label, bar, count_label))

        for ext_label, bar, count_label in bars:
            bar_zero = bar.copy().stretch_to_fit_width(0.01).align_to(
                bar, LEFT
            )
            self.play(
                FadeIn(ext_label, run_time=0.25),
                GrowFromEdge(bar, LEFT, run_time=0.6),
                FadeIn(count_label, run_time=0.3),
                lag_ratio=0.0,
            )
            self.wait(0.05)

        self.wait(0.5)

        # Red annotation — no .js, no dist/
        note = Text(
            "Zero .js files — Zero dist/ — Zero compiled output",
            font=SERIF, font_size=30, color=RED,
        ).to_edge(DOWN, buff=0.6)
        self.play(Write(note, run_time=1.0))
        self.wait(1.0)


# ---------------------------------------------------------------------------
# B05 — FolderTree
# Real top-level directory listing with missing src/ and dist/ marked.
# ---------------------------------------------------------------------------

class B05_FolderTree(Scene):
    def construct(self):
        title = Text(
            "anthropics/claude-code/",
            font="Courier New", font_size=36, color=INK,
        ).to_edge(UP, buff=0.6)
        self.play(FadeIn(title, run_time=0.4))

        # Real top-level items (verified via find . -maxdepth 1)
        items = [
            ("├── CHANGELOG.md", "(5,248 lines)", INK),
            ("├── README.md",    "(72 lines)",    INK),
            ("├── examples/",    "",              INK),
            ("├── plugins/",     "",              INK),
            ("├── scripts/",     "",              INK),
            ("├── .claude/",     "",              INK),
            ("├── .devcontainer/","",             INK),
            ("└── SECURITY.md",  "",              INK),
        ]

        y = 2.0
        x_left = -5.5
        for tree_str, note, color in items:
            row = VGroup(
                Text(tree_str, font="Courier New", font_size=28, color=color).move_to([x_left + 2.0, y, 0]),
                Text(note, font=SERIF, font_size=24, color=DIM).move_to([x_left + 5.5, y, 0]),
            ).arrange(RIGHT, buff=0.3).move_to([0, y, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.1, run_time=0.3))
            y -= 0.52

        self.wait(0.3)

        # Missing entries — red
        missing = [
            "  ✗  src/    (NOT FOUND)",
            "  ✗  dist/   (NOT FOUND)",
        ]
        for m in missing:
            row = Text(m, font="Courier New", font_size=30, color=RED).move_to([0, y, 0])
            self.play(FadeIn(row, run_time=0.5))
            y -= 0.55

        self.wait(1.5)


# ---------------------------------------------------------------------------
# B05b — ScriptFiles
# The 5 TypeScript files in scripts/ with plain-language descriptions.
# ---------------------------------------------------------------------------

class B05b_ScriptFiles(Scene):
    def construct(self):
        title = Text(
            "scripts/*.ts — the 5 TypeScript files",
            font=SERIF, font_size=36, color=INK,
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, run_time=0.4))

        # Verified via: find . -name '*.ts' | grep -v .git
        files = [
            ("auto-close-duplicates.ts",      "→  close duplicate GitHub issues"),
            ("backfill-duplicate-comments.ts", "→  comment management on dupes"),
            ("issue-lifecycle.ts",             "→  label and triage automation"),
            ("lifecycle-comment.ts",           "→  automated notifications"),
            ("sweep.ts",                       "→  periodic repo housekeeping"),
        ]

        y = 1.8
        for fname, desc in files:
            row = VGroup(
                Text(fname, font="Courier New", font_size=26, color=INK),
                Text(desc, font=SERIF, font_size=24, color=SLATE),
            ).arrange(RIGHT, buff=0.4).move_to([0, y, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.08, run_time=0.35))
            y -= 0.58

        self.wait(0.3)

        note = Text(
            "Purpose: GitHub issue management — not the tool.",
            font=SERIF, font_size=30, color=TERRA,
        ).move_to([0, y - 0.2, 0])
        self.play(Write(note, run_time=0.8))
        self.wait(1.2)


# ---------------------------------------------------------------------------
# B07 — VelocityChart
# Counter from 0 to 353; timeline annotation; ~2 releases/day label.
# ---------------------------------------------------------------------------

class B07_VelocityChart(Scene):
    def construct(self):
        # Large counter
        count_label = Text("0", font=SERIF, font_size=160, color=INK).move_to([0, 0.8, 0])

        def update_count(obj, alpha):
            val = int(alpha * 353)
            obj.become(Text(str(val), font=SERIF, font_size=160, color=INK).move_to([0, 0.8, 0]))

        sub = Text(
            "releases documented in CHANGELOG.md",
            font=SERIF, font_size=32, color=DIM,
        ).next_to(count_label, DOWN, buff=0.3)

        self.play(FadeIn(count_label, run_time=0.3))
        self.play(
            UpdateFromAlphaFunc(count_label, update_count, run_time=2.0, rate_func=smooth),
        )
        self.wait(0.2)
        self.play(FadeIn(sub, run_time=0.5))
        self.wait(0.3)

        # Timeline: v0.2.21 ─── v2.1.220
        timeline = VGroup(
            Text("v0.2.21", font="Courier New", font_size=26, color=DIM),
            Line(LEFT * 2.5, RIGHT * 2.5, color=SLATE, stroke_width=3),
            Text("v2.1.220", font="Courier New", font_size=26, color=INK),
        ).arrange(RIGHT, buff=0.3).move_to([0, -0.8, 0])
        self.play(FadeIn(timeline, run_time=0.8))
        self.wait(0.3)

        # Velocity annotation
        vel_box = VGroup(
            RoundedRectangle(corner_radius=0.12, width=3.0, height=0.7,
                             fill_color=TERRA, fill_opacity=0.9, stroke_width=0),
            Text("~2 releases/day", font=SERIF, font_size=28, color=GROUND),
        )
        vel_box[1].move_to(vel_box[0].get_center())
        vel_box.move_to([3.8, 0.8, 0])
        self.play(FadeIn(vel_box, run_time=0.6))
        self.wait(1.5)


# ---------------------------------------------------------------------------
# B10 — ChurnChart
# Grouped bar chart: total vs bot commits per month (Feb–Jul 2026).
# Verified data from: git log --pretty=format:'%ad %s' --date=format:'%Y-%m'
# ---------------------------------------------------------------------------

class B10_ChurnChart(Scene):
    def construct(self):
        # Verified monthly data
        months = ["Feb", "Mar", "Apr", "May", "Jun", "Jul"]
        totals = [50,    31,    35,    42,    37,    27]
        bots   = [32,    26,    30,    32,    31,    25]
        humans = [18,     5,     5,    10,     6,     2]

        title = Text(
            "anthropics/claude-code — 222 commits (Feb–Jul 2026)",
            font=SERIF, font_size=30, color=INK,
        ).to_edge(UP, buff=0.75)
        self.play(FadeIn(title, run_time=0.5))

        max_val   = 55
        bar_w     = 0.75
        x_start   = -5.0
        step      = 2.0      # 6 groups × 2.0 = 10.0 total span; fits in ±7.1
        y_floor   = -2.0
        bar_h_max = 4.2

        def bar_h(val):
            return val / max_val * bar_h_max

        total_bars = []
        bot_bars   = []
        human_lbls = []
        mon_lbls   = []

        for i, (mon, tot, bot, hum) in enumerate(zip(months, totals, bots, humans)):
            x_center = x_start + i * step

            # Total bar (ink, transparent)
            th = bar_h(tot)
            t_bar = Rectangle(
                width=bar_w * 1.6, height=th,
                fill_color=INK, fill_opacity=0.25, stroke_width=1,
                stroke_color=INK,
            ).move_to([x_center, y_floor + th / 2, 0])

            # Bot bar (terracotta, opaque, inside total)
            bh = bar_h(bot)
            b_bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=TERRA, fill_opacity=0.85, stroke_width=0,
            ).move_to([x_center, y_floor + bh / 2, 0])

            # Human count label above bot bar
            h_lbl = Text(
                str(hum), font=SERIF, font_size=22, color=TERRA,
            ).move_to([x_center, y_floor + th + 0.25, 0])

            # Month label below
            m_lbl = Text(
                mon, font=SERIF, font_size=26, color=INK,
            ).move_to([x_center, y_floor - 0.4, 0])

            total_bars.append(t_bar)
            bot_bars.append(b_bar)
            human_lbls.append(h_lbl)
            mon_lbls.append(m_lbl)

        # Animate all bars up simultaneously
        self.play(*[FadeIn(m, run_time=0.4) for m in mon_lbls])
        self.play(
            *[GrowFromEdge(t, DOWN, run_time=1.0) for t in total_bars],
        )
        self.play(
            *[GrowFromEdge(b, DOWN, run_time=0.8) for b in bot_bars],
        )
        self.play(*[FadeIn(h, run_time=0.4) for h in human_lbls])
        self.wait(0.3)

        # Annotation: 176 / 222 = 79% bot — placed below month labels
        ann = Text(
            "Bot: 176 / 222 = 79%",
            font=SERIF, font_size=26, color=TERRA,
        ).move_to([0, -3.1, 0])
        self.play(FadeIn(ann, run_time=0.5))
        self.wait(1.5)
