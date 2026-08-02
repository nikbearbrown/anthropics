"""
scenes.py — claude-liam-git-claude-code/short
Portrait-native Manim scenes (1080 × 1920, 60fps) for the 9:16 Short.

Data identical to parent reel (all verified from real repo 2026-08-01):
  File counts: 106 md, 27 json, 21 sh, 21 py, 8 tf, 5 ts
  Top-level dirs: CHANGELOG.md (5248 lines), README.md (72 lines), examples/,
                  plugins/, scripts/, .claude/, .devcontainer/, SECURITY.md
  TypeScript files: scripts/{auto-close-duplicates,backfill-duplicate-comments,
                             issue-lifecycle,lifecycle-comment,sweep}.ts
  CHANGELOG versions: 353 total, v0.2.21 → v2.1.220
  Commits: 222 total (--depth=200 clone)
  Bot: 176, Human: 46
  Monthly: Feb 50/32/18, Mar 31/26/5, Apr 35/30/5, May 42/32/10, Jun 37/31/6, Jul 27/25/2

Render command (from books/):
  cd anthropics/youtube/claude-liam-git-claude-code/short
  manim -qk scenes.py B04_Portrait B05_Portrait B05b_Portrait B07_Portrait B10_Portrait
  mv media/videos/scenes/2160p60/B04_Portrait.mp4 manim/B04.mp4
  mv media/videos/scenes/2160p60/B05_Portrait.mp4 manim/B05.mp4
  mv media/videos/scenes/2160p60/B05b_Portrait.mp4 manim/B05b.mp4
  mv media/videos/scenes/2160p60/B07_Portrait.mp4 manim/B07.mp4
  mv media/videos/scenes/2160p60/B10_Portrait.mp4 manim/B10.mp4
  cd /Users/bear/Documents/CoWork/bear-textbooks/books
"""

from manim import *

# Portrait config: 1080 × 1920 @ 60fps
config.pixel_width  = 1080
config.pixel_height = 1920
config.frame_rate   = 60

# Claude brand palette
GROUND = "#FAF9F5"   # cream canvas
INK    = "#3D3929"   # warm dark ink
TERRA  = "#D97757"   # terracotta accent
SLATE  = "#8A7E72"   # secondary / muted text
RED    = "#C8102E"   # error / missing
DIM    = "#8A7E72"   # dim annotations
SERIF  = "EB Garamond"

config.background_color = GROUND


# ---------------------------------------------------------------------------
# B04_Portrait — StructureMap (portrait)
# Horizontal bar chart of file counts by extension.
# 6 rows; .md bar dominant (INK full opacity); all others dimmed ink.
# Portrait layout: title at top, bars fill the middle third.
# ---------------------------------------------------------------------------

class B04_Portrait(Scene):
    def construct(self):
        # Target: ~17s to avoid extreme slow-mo. Pad waits generously.
        data = [
            (".md",   106, INK, 0.90),   # dominant — full opacity
            (".json",  27, INK, 0.35),
            (".sh",    21, INK, 0.35),
            (".py",    21, INK, 0.35),
            (".tf",     8, INK, 0.35),
            (".ts",     5, INK, 0.35),
        ]
        max_count = 106

        # Portrait frame: ±6.0 wide, ±10.67 tall (1080×1920 → frame 12×21.33)
        # Place title in upper area, bars in center.
        title = Text(
            "anthropics/claude-code",
            font=SERIF, font_size=44, color=INK,
        ).move_to([0, 7.8, 0])
        subtitle = Text(
            "210 files",
            font=SERIF, font_size=60, color=INK,
        ).move_to([0, 6.8, 0])
        self.play(FadeIn(title, run_time=0.6))
        self.play(FadeIn(subtitle, run_time=0.5))
        self.wait(0.5)

        # Bar chart: bars grow left to right from x_start
        bar_width_max = 9.0   # max bar spans ≈9 units
        bar_height    = 0.70
        row_gap       = 0.35
        y_start       = 4.5   # center the 6 rows vertically around y=3
        x_start       = -4.0  # left edge of bars (after extension labels)

        bars = []
        for i, (ext, count, color, opacity) in enumerate(data):
            y   = y_start - i * (bar_height + row_gap)
            w   = bar_width_max * count / max_count

            ext_label = Text(
                ext, font=SERIF, font_size=34, color=INK,
            ).move_to([x_start - 0.85, y, 0])

            bar = Rectangle(
                width=w, height=bar_height,
                fill_color=color, fill_opacity=opacity,
                stroke_width=0,
            ).move_to([x_start + w / 2, y, 0])

            count_label = Text(
                str(count), font=SERIF, font_size=32, color=INK,
            ).next_to(bar, RIGHT, buff=0.18)

            bars.append((ext_label, bar, count_label))

        for ext_label, bar, count_label in bars:
            self.play(
                FadeIn(ext_label, run_time=0.30),
                GrowFromEdge(bar, LEFT, run_time=0.80),
                FadeIn(count_label, run_time=0.35),
                lag_ratio=0.0,
            )
            self.wait(0.20)

        self.wait(0.8)

        # Red annotation — no .js, no dist/
        note_line1 = Text(
            "Zero .js files",
            font=SERIF, font_size=36, color=RED,
        ).move_to([0, -1.8, 0])
        note_line2 = Text(
            "Zero dist/  —  Zero compiled output",
            font=SERIF, font_size=32, color=RED,
        ).move_to([0, -2.55, 0])
        self.play(Write(note_line1, run_time=1.0))
        self.play(Write(note_line2, run_time=1.0))
        self.wait(1.5)


# ---------------------------------------------------------------------------
# B05_Portrait — FolderTree (portrait)
# Real top-level directory listing with missing src/ and dist/ marked.
# Portrait layout: monospace tree centered, red annotations below.
# ---------------------------------------------------------------------------

class B05_Portrait(Scene):
    def construct(self):
        # Target: ~17.6s. Slow each entry and hold on missing entries.
        title = Text(
            "anthropics/claude-code/",
            font="Courier New", font_size=38, color=INK,
        ).move_to([0, 8.5, 0])
        self.play(FadeIn(title, run_time=0.6))
        self.wait(0.4)

        # Verified via: find . -maxdepth 1 | grep -v .git | sort
        # CHANGELOG.md is load-bearing (5,248 lines) — flag it prominently
        items = [
            ("├── CHANGELOG.md", "(5,248 lines)",  TERRA),
            ("├── README.md",    "(72 lines)",      DIM),
            ("├── examples/",    "",               INK),
            ("├── plugins/",     "",               INK),
            ("├── scripts/",     "",               INK),
            ("├── .claude/",     "",               INK),
            ("├── .devcontainer/","",              INK),
            ("└── SECURITY.md",  "",               INK),
        ]

        y = 6.8
        for tree_str, note, note_color in items:
            tree_t = Text(tree_str, font="Courier New", font_size=28, color=INK)
            if note:
                note_t = Text(note, font=SERIF, font_size=26, color=note_color)
                row = VGroup(tree_t, note_t).arrange(RIGHT, buff=0.28)
            else:
                row = tree_t
            row.move_to([0, y, 0])
            self.play(FadeIn(row, shift=RIGHT * 0.12, run_time=0.45))
            self.wait(0.15)
            y -= 0.75

        self.wait(0.5)

        # Missing entries — red cross marks; hold on each
        missing = [
            "  ✗  src/    (NOT FOUND)",
            "  ✗  dist/   (NOT FOUND)",
        ]
        for m in missing:
            row = Text(m, font="Courier New", font_size=32, color=RED).move_to([0, y, 0])
            self.play(FadeIn(row, run_time=0.7))
            self.wait(0.5)
            y -= 0.75

        self.wait(2.0)


# ---------------------------------------------------------------------------
# B05b_Portrait — ScriptFiles (portrait)
# The 5 TypeScript files in scripts/ with plain-language descriptions.
# Portrait layout: title + two-column-style list centered.
# ---------------------------------------------------------------------------

class B05b_Portrait(Scene):
    def construct(self):
        # Target: ~14.3s. Each file entry takes longer; hold on verdict.
        title = Text(
            "scripts/*.ts",
            font=SERIF, font_size=56, color=INK,
        ).move_to([0, 8.5, 0])
        subtitle = Text(
            "the 5 TypeScript files",
            font=SERIF, font_size=38, color=SLATE,
        ).move_to([0, 7.5, 0])
        self.play(FadeIn(title, run_time=0.6))
        self.play(FadeIn(subtitle, run_time=0.5))
        self.wait(0.4)

        # Verified via: find . -name '*.ts' | grep -v .git
        files = [
            ("auto-close-duplicates.ts",       "close duplicate issues"),
            ("backfill-duplicate-comments.ts", "comment management"),
            ("issue-lifecycle.ts",             "label + triage automation"),
            ("lifecycle-comment.ts",           "automated notifications"),
            ("sweep.ts",                       "periodic repo housekeeping"),
        ]

        y = 5.6
        for fname, desc in files:
            fname_t = Text(fname, font="Courier New", font_size=27, color=INK)
            arrow_t = Text("→", font=SERIF, font_size=32, color=TERRA)
            desc_t  = Text(desc, font=SERIF, font_size=28, color=SLATE)
            row = VGroup(fname_t, arrow_t, desc_t).arrange(RIGHT, buff=0.25)
            row.move_to([0, y, 0])
            # Scale if too wide for portrait frame (±5.4 usable width)
            if row.width > 10.0:
                row.scale(10.0 / row.width)
            self.play(FadeIn(row, shift=RIGHT * 0.08, run_time=0.50))
            self.wait(0.25)
            y -= 1.1

        self.wait(0.5)

        # Terracotta verdict label
        note = Text(
            "Purpose: GitHub issue management\n— not the tool.",
            font=SERIF, font_size=34, color=TERRA,
            line_spacing=1.2,
        ).move_to([0, y - 0.3, 0])
        self.play(Write(note, run_time=1.2))
        self.wait(2.0)


# ---------------------------------------------------------------------------
# B07_Portrait — VelocityChart (portrait)
# Large counter 0→353; timeline annotation; ~2 releases/day label.
# Portrait layout: counter centered in upper half, annotations stack below.
# ---------------------------------------------------------------------------

class B07_Portrait(Scene):
    def construct(self):
        # Target: ~17.7s. Counter runs 3.5s, then generous holds on each element.
        count_label = Text("0", font=SERIF, font_size=220, color=INK).move_to([0, 4.0, 0])

        def update_count(obj, alpha):
            val = int(alpha * 353)
            obj.become(Text(str(val), font=SERIF, font_size=220, color=INK).move_to([0, 4.0, 0]))

        sub = Text(
            "releases documented\nin CHANGELOG.md",
            font=SERIF, font_size=36, color=DIM,
            line_spacing=1.3,
        ).move_to([0, 1.2, 0])

        self.play(FadeIn(count_label, run_time=0.4))
        self.play(
            UpdateFromAlphaFunc(count_label, update_count, run_time=3.5, rate_func=smooth),
        )
        self.wait(0.5)
        self.play(FadeIn(sub, run_time=0.8))
        self.wait(0.8)

        # Timeline: v0.2.21 ─── v2.1.220
        oldest_t  = Text("v0.2.21", font="Courier New", font_size=28, color=DIM)
        line_mob  = Line(LEFT * 3.2, RIGHT * 3.2, color=SLATE, stroke_width=3)
        newest_t  = Text("v2.1.220", font="Courier New", font_size=28, color=INK)
        timeline  = VGroup(oldest_t, line_mob, newest_t).arrange(RIGHT, buff=0.25)
        timeline.move_to([0, -1.0, 0])
        self.play(FadeIn(timeline, run_time=1.0))
        self.wait(0.7)

        # Velocity annotation box — centered below timeline
        vel_rect = RoundedRectangle(
            corner_radius=0.14, width=5.8, height=1.1,
            fill_color=TERRA, fill_opacity=0.92, stroke_width=0,
        ).move_to([0, -2.5, 0])
        vel_text = Text(
            "~2 releases / day", font=SERIF, font_size=38, color=GROUND,
        ).move_to(vel_rect.get_center())
        vel_box = VGroup(vel_rect, vel_text)
        self.play(FadeIn(vel_box, run_time=0.8))
        self.wait(2.5)


# ---------------------------------------------------------------------------
# B10_Portrait — ChurnChart (portrait)
# Grouped bar chart: total (ink) vs bot (terracotta) per month.
# Portrait layout: 6 month groups along x-axis; portrait height used for
# taller bars and stacked annotations.
# ---------------------------------------------------------------------------

class B10_Portrait(Scene):
    def construct(self):
        months = ["Feb", "Mar", "Apr", "May", "Jun", "Jul"]
        totals = [50,    31,    35,    42,    37,    27]
        bots   = [32,    26,    30,    32,    31,    25]
        humans = [18,     5,     5,    10,     6,     2]

        title = Text(
            "anthropics/claude-code",
            font=SERIF, font_size=40, color=INK,
        ).move_to([0, 9.0, 0])
        sub_t = Text(
            "222 commits  ·  Feb–Jul 2026",
            font=SERIF, font_size=32, color=SLATE,
        ).move_to([0, 8.1, 0])
        self.play(FadeIn(title, run_time=0.4))
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(0.2)

        max_val   = 55
        bar_w     = 0.80
        # 6 groups spread across portrait width (±5.0 usable)
        x_positions = [-4.2, -2.5, -0.8, 0.9, 2.6, 4.3]
        y_floor     = -3.0
        bar_h_max   = 8.5   # tall bars use portrait height

        def bar_h(val):
            return val / max_val * bar_h_max

        total_bars = []
        bot_bars   = []
        human_lbls = []
        mon_lbls   = []

        for i, (mon, tot, bot, hum) in enumerate(zip(months, totals, bots, humans)):
            x = x_positions[i]

            # Total bar — ink, semi-opaque outline
            th = bar_h(tot)
            t_bar = Rectangle(
                width=bar_w * 1.5, height=th,
                fill_color=INK, fill_opacity=0.20,
                stroke_width=1.5, stroke_color=INK,
            ).move_to([x, y_floor + th / 2, 0])

            # Bot bar — terracotta, inside total
            bh = bar_h(bot)
            b_bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=TERRA, fill_opacity=0.88, stroke_width=0,
            ).move_to([x, y_floor + bh / 2, 0])

            # Human label above total bar
            h_lbl = Text(
                str(hum), font=SERIF, font_size=24, color=TERRA,
            ).move_to([x, y_floor + th + 0.38, 0])

            # Month label below
            m_lbl = Text(
                mon, font=SERIF, font_size=28, color=INK,
            ).move_to([x, y_floor - 0.55, 0])

            total_bars.append(t_bar)
            bot_bars.append(b_bar)
            human_lbls.append(h_lbl)
            mon_lbls.append(m_lbl)

        # Animate — slower timings to fill ~18s beat
        self.play(*[FadeIn(m, run_time=0.5) for m in mon_lbls])
        self.wait(0.4)
        self.play(*[GrowFromEdge(t, DOWN, run_time=1.5) for t in total_bars])
        self.wait(0.3)
        self.play(*[GrowFromEdge(b, DOWN, run_time=1.2) for b in bot_bars])
        self.wait(0.3)
        self.play(*[FadeIn(h, run_time=0.5) for h in human_lbls])
        self.wait(0.5)

        # Legend
        ink_sq  = Square(0.38, fill_color=INK, fill_opacity=0.25, stroke_width=1.5, stroke_color=INK)
        ink_lbl = Text("total", font=SERIF, font_size=28, color=INK)
        ter_sq  = Square(0.38, fill_color=TERRA, fill_opacity=0.88, stroke_width=0)
        ter_lbl = Text("bot", font=SERIF, font_size=28, color=INK)
        legend  = VGroup(ink_sq, ink_lbl, ter_sq, ter_lbl).arrange(RIGHT, buff=0.22)
        legend.move_to([0, y_floor - 1.4, 0])
        self.play(FadeIn(legend, run_time=0.6))
        self.wait(0.5)

        # Summary annotation — centered, bottom of portrait
        ann = Text(
            "Bot: 176 / 222 = 79%",
            font=SERIF, font_size=36, color=TERRA,
        ).move_to([0, y_floor - 2.5, 0])
        self.play(FadeIn(ann, run_time=0.7))
        self.wait(2.5)
