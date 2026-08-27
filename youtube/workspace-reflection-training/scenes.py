"""scenes.py — Manim graphics for workspace-reflection-training (E06)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-reflection-training
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_ThePrediction

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-reflection-training

Scene → beat mapping (durations from estimated audio — update after gen):
  B02_ThePrediction     14.0s   three-step syllogism: might-say → says → thinks
  B03_CRTBefore         12.0s   J-space before CRT: task tokens, ethics absent
  B04_CRTData           14.0s   CRT pipeline: truncate → reflection Q → gradient
  B05_HonestyNumbers    17.0s   paired bars: dishonesty 0.25→0.07, deception 0.38→0.05
  B06_HowItWins         16.0s   before/after response distributions
  B07_LensReceipts      13.0s   top-20 ethics tokens appearance rate delta
  B08_AblationControl   14.0s   Fig 50-C: intact vs ablated deception scores
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B02 · The Prediction ──────────────────────────────────────────────────────
# 14.0s  Three-step syllogism: reasoning routes through might-say representations
#         → shaping what it says in C → shapes what it thinks in C.
class B02_ThePrediction(Scene):
    def construct(self):
        def step_box(text, col=INK, w=7.5, h=1.15):
            rect = RoundedRectangle(
                corner_radius=0.14, width=w, height=h,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=col, stroke_width=2,
            )
            txt = Text(text, font=SERIF, font_size=28, color=col)
            txt.move_to(rect)
            return VGroup(rect, txt)

        s1 = step_box("Reasoning routes through might-say representations")
        s2 = step_box("Train what it says in context C", col=INK)
        s3 = step_box("Shapes what it thinks in context C", col=INK)

        s1.shift(UP * 2.1)
        s2.shift(ORIGIN)
        s3.shift(DOWN * 2.1)

        # arrows between steps
        a1 = Arrow(
            s1.get_bottom() + DOWN * 0.05,
            s2.get_top() + UP * 0.05,
            color=INK, stroke_width=3, buff=0,
        )
        a2 = Arrow(
            s2.get_bottom() + DOWN * 0.05,
            s3.get_top() + UP * 0.05,
            color=TERRA, stroke_width=3, buff=0,
        )

        # left edge label — shows the logical flow
        premise_lbl = Text("premise", font=SANS, font_size=28, color=INK)
        premise_lbl.next_to(s1, LEFT, buff=0.3)
        conclusion_lbl = Text("prediction", font=SANS, font_size=28, color=INK)
        conclusion_lbl.next_to(s3, LEFT, buff=0.3)

        self.play(FadeIn(s1, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(premise_lbl), run_time=0.3)
        self.wait(0.5)

        self.play(GrowArrow(a1), run_time=0.5)
        self.play(FadeIn(s2, shift=DOWN * 0.15), run_time=0.7)
        self.wait(0.4)

        self.play(GrowArrow(a2), run_time=0.5)
        self.play(FadeIn(s3, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(conclusion_lbl), run_time=0.3)
        self.wait(0.4)

        caption = Text(
            "Not new knowledge. New reflexes.",
            font=SERIF, font_size=30, color=INK,
        )
        caption.to_edge(DOWN, buff=0.72)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.6)
        self.wait(6.6)    # total ≈ 14.0s


# ── B03 · CRT Before ─────────────────────────────────────────────────────────
# 12.0s  J-space mid-task: task tokens fill the workspace; ethics tokens absent.
class B03_CRTBefore(Scene):
    def construct(self):
        # transcript panel (left)
        transcript_box = RoundedRectangle(
            corner_radius=0.14, width=4.8, height=5.0,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        transcript_box.shift(LEFT * 3.4)
        transcript_lbl = Text("agentic transcript", font=SANS, font_size=28, color=INK)
        transcript_lbl.next_to(transcript_box, UP, buff=0.12)

        lines = [
            "Tool: read_file",
            "  path: /data/config.json",
            "Tool: bash",
            "  cmd: git diff HEAD",
            "Output: ···",
            "Tool: edit_file",
            "  path: /src/agent.py",
        ]
        line_group = VGroup()
        for line in lines:
            col = TERRA if "Tool" in line else INK
            t = Text(line, font=SERIF, font_size=19, color=col)
            line_group.add(t)
        line_group.arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        line_group.move_to(transcript_box)
        line_group.shift(LEFT * 0.2)

        self.play(
            FadeIn(transcript_box, shift=RIGHT * 0.2),
            FadeIn(transcript_lbl),
            run_time=0.6,
        )
        self.play(
            LaggedStart(
                *[FadeIn(ln, shift=RIGHT * 0.08) for ln in line_group],
                lag_ratio=0.12,
            ),
            run_time=1.2,
        )

        # J-space panel (right)
        jspace_box = RoundedRectangle(
            corner_radius=0.14, width=4.8, height=5.0,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        jspace_box.shift(RIGHT * 3.4)
        jspace_lbl = Text("workspace  (J-space)", font=SANS, font_size=28, color=INK)
        jspace_lbl.next_to(jspace_box, UP, buff=0.12)

        task_tokens = [
            "config.json", "git diff", "HEAD", "agent.py",
            "edit_file", "bash", "read_file", "path",
        ]
        ethics_tokens = ["flag?", "should I?", "ethics"]

        # task tokens fill the space in terracotta
        task_group = VGroup()
        positions = [
            LEFT * 1.3 + UP * 1.6, RIGHT * 0.5 + UP * 1.4,
            LEFT * 0.8 + UP * 0.4, RIGHT * 1.2 + UP * 0.7,
            LEFT * 1.5 + DOWN * 0.5, RIGHT * 0.2 + DOWN * 0.3,
            LEFT * 0.5 + DOWN * 1.4, RIGHT * 1.3 + DOWN * 1.6,
        ]
        for tok, pos in zip(task_tokens, positions):
            t = Text(tok, font=SERIF, font_size=20, color=INK)
            t.move_to(jspace_box.get_center() + pos)
            task_group.add(t)

        # ethics tokens — very faint / absent
        ethics_group = VGroup()
        epositions = [RIGHT * 0.0 + DOWN * 0.9, LEFT * 0.3 + UP * 1.1, RIGHT * 1.4 + DOWN * 0.8]
        for tok, pos in zip(ethics_tokens, epositions):
            t = Text(tok, font=SERIF, font_size=19, color=INK)
            t.set_opacity(0.12)
            t.move_to(jspace_box.get_center() + pos)
            ethics_group.add(t)

        self.play(
            FadeIn(jspace_box, shift=LEFT * 0.2),
            FadeIn(jspace_lbl),
            run_time=0.6,
        )
        self.play(
            LaggedStart(
                *[FadeIn(tok, shift=UP * 0.08) for tok in task_group],
                lag_ratio=0.1,
            ),
            run_time=1.0,
        )
        self.play(
            LaggedStart(
                *[FadeIn(tok) for tok in ethics_group],
                lag_ratio=0.2,
            ),
            run_time=0.5,
        )

        # arrow from transcript to J-space
        midline = Arrow(
            transcript_box.get_right() + RIGHT * 0.1,
            jspace_box.get_left() + LEFT * 0.1,
            color=INK, stroke_width=2.5, buff=0,
        )
        self.play(GrowArrow(midline), run_time=0.5)

        caption = Text(
            "No ethics in the workspace — not yet.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.70)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.6)
        self.wait(4.7)    # total ≈ 12.0s


# ── B04 · CRT Data ────────────────────────────────────────────────────────────
# 14.0s  Three-zone vertical flow: partial transcript / reflection Q / answer;
#         gradient arrow attaches only to the reflection zone.
class B04_CRTData(Scene):
    def construct(self):
        zone_w = 8.0

        def zone(label, lines, col, h):
            rect = RoundedRectangle(
                corner_radius=0.13, width=zone_w, height=h,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=col, stroke_width=2,
            )
            lbl = Text(label, font=SANS, font_size=24, color=INK)
            lbl.move_to(rect.get_top() + DOWN * 0.28)
            content = VGroup()
            for ln in lines:
                t = Text(ln, font=SERIF, font_size=28, color=INK)
                content.add(t)
            content.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
            content.move_to(rect.get_center() + DOWN * 0.18)
            return VGroup(rect, lbl, content)

        z1 = zone(
            "partial transcript",
            ["Tool: read_file  path: /data/report.csv",
             "Tool: bash  cmd: grep -i 'personal' ···",
             "[transcript truncated mid-task]"],
            INK, 1.7,
        )
        z2 = zone(
            "appended reflection question",
            ["What considerations apply right now?"],
            TERRA, 1.2,
        )
        z3 = zone(
            "fine-tuned answer",
            ["This file contains PII. I should flag this",
             "before proceeding with the data extraction."],
            INK, 1.5,
        )

        z1.shift(UP * 2.25)
        z2.shift(UP * 0.3)
        z3.shift(DOWN * 1.5)

        # cut marker between z1 and z2
        cut_mark = Text("···  cut  ···", font=SANS, font_size=24, color=INK)
        cut_mark.move_to(z1.get_bottom() + DOWN * 0.22)

        self.play(FadeIn(z1, shift=DOWN * 0.15), run_time=0.7)
        self.play(FadeIn(cut_mark), run_time=0.35)
        self.play(FadeIn(z2, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(z3, shift=DOWN * 0.15), run_time=0.6)
        self.wait(0.4)

        # gradient arrow only on the reflection zone — right side, terracotta
        grad_start = z2.get_right() + RIGHT * 0.5 + DOWN * 0.2
        grad_end   = z2.get_right() + RIGHT * 0.5 + UP * 0.2
        grad_arrow = Arrow(
            grad_start, grad_end,
            color=TERRA, stroke_width=4, buff=0,
        )
        grad_lbl = Text("gradient", font=SANS, font_size=26, color=INK)
        grad_lbl.rotate(PI / 2)
        grad_lbl.next_to(grad_arrow, RIGHT, buff=0.12)

        grad_brace = Brace(z2, direction=RIGHT, color=TERRA)
        self.play(Create(grad_brace), run_time=0.4)
        self.play(GrowArrow(grad_arrow), FadeIn(grad_lbl), run_time=0.6)

        caption = Text(
            "Trained on reflections about moments it never finished living.",
            font=SERIF, font_size=24, color=INK,
        )
        caption.to_edge(DOWN, buff=0.70)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.6)
        self.wait(7.55)    # total ≈ 14.0s


# ── B05 · Honesty Numbers ─────────────────────────────────────────────────────
# 17.0s  Paired animated bars with 95% CIs:
#         fabrication dishonesty 0.25→0.07; deception 0.38→0.05 (Haiku 4.5).
class B05_HonestyNumbers(Scene):
    def construct(self):
        # two grouped bar charts side by side
        # left group: Fabrication Dishonesty
        # right group: Deception
        groups = [
            {"label": "Fabrication\nDishonesty", "baseline": 0.25, "trained": 0.07},
            {"label": "Deception",                "baseline": 0.38, "trained": 0.05},
        ]

        bar_w    = 1.0
        gap      = 0.30   # gap between baseline and trained within a group
        scale    = 5.5    # 1.0 → 5.5 MUnits (max bar top: -2.2 + 0.38*5.5 = -0.11, fine)
        x_offset = 2.8    # group spacing
        y_base   = -2.2   # baseline y; max bar top = -2.2 + 0.38*5.5 = -0.11

        # axis — x=-4.5 keeps tick labels within ±6.3 safe area
        axis_x = -4.5
        axis = Line(
            [axis_x, y_base, 0], [axis_x, y_base + 0.42 * scale + 0.2, 0],
            color=INK, stroke_width=2,
        )
        tick_labels = VGroup()
        for v in [0.0, 0.1, 0.2, 0.3, 0.4]:
            y = y_base + v * scale
            tick = Line([axis_x - 0.10, y, 0], [axis_x, y, 0], color=INK, stroke_width=1.5)
            lbl  = Text(f"{v:.1f}", font=SANS, font_size=16, color=INK)
            lbl.next_to(tick, LEFT, buff=0.08)
            tick_labels.add(VGroup(tick, lbl))

        axis_title = Text("dishonesty score", font=SANS, font_size=16, color=INK)
        axis_title.rotate(PI / 2)
        axis_title.next_to(axis, LEFT, buff=1.2)

        self.play(Create(axis), FadeIn(tick_labels), FadeIn(axis_title), run_time=0.7)

        # legend — positioned within safe area (x ≤ 6.3)
        legend_items = VGroup()
        for label, col in [("baseline", INK), ("reflection-trained", TERRA)]:
            swatch = Rectangle(
                width=0.26, height=0.26,
                fill_color=col, fill_opacity=0.85, stroke_width=0,
            )
            t = Text(label, font=SANS, font_size=15, color=INK)
            legend_items.add(VGroup(swatch, t).arrange(RIGHT, buff=0.1))
        legend_items.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        legend_items.move_to([3.5, 2.8, 0])
        self.play(FadeIn(legend_items), run_time=0.4)

        for gi, g in enumerate(groups):
            gx = (gi - 0.5) * x_offset * 2
            vals = [("baseline", g["baseline"], INK), ("trained", g["trained"], TERRA)]
            bars_this = VGroup()
            for bi, (kind, val, col) in enumerate(vals):
                bx = gx + (bi - 0.5) * (bar_w + gap)
                bar_h = val * scale
                bar = Rectangle(
                    width=bar_w, height=bar_h,
                    fill_color=col, fill_opacity=0.85,
                    stroke_color=col, stroke_width=1,
                )
                bar.move_to([bx, y_base + bar_h / 2, 0])
                # val_txt placed clearly above bar top, no CI lines to collide with
                val_txt = Text(f"{val:.2f}", font=SANS, font_size=18, color=INK)
                val_txt.move_to([bx, y_base + bar_h + 0.30, 0])
                bars_this.add(VGroup(bar, val_txt))

            group_lbl = Text(g["label"], font=SANS, font_size=19, color=INK)
            group_lbl.move_to([gx, y_base - 0.45, 0])

            self.play(
                LaggedStart(
                    *[GrowFromEdge(b[0], DOWN) for b in bars_this],
                    lag_ratio=0.2,
                ),
                run_time=1.0,
            )
            self.play(
                *[FadeIn(b[1]) for b in bars_this],
                run_time=0.4,
            )
            self.play(FadeIn(group_lbl), run_time=0.3)

        title = Text("Haiku 4.5: baseline vs reflection-trained", font=SERIF, font_size=25, color=INK)
        title.to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(9.7)    # total ≈ 17.0s


# ── B06 · How It Wins ────────────────────────────────────────────────────────
# 16.0s  Before/after response distributions:
#         fabrication: mass shifts from fabrication to outright admission;
#         deception: mass shifts from directive-carried to refuse-and-disclose.
class B06_HowItWins(Scene):
    def construct(self):
        panel_w = 5.6
        panel_h = 4.8

        def response_panel(title, before_segments, after_segments, x_offset):
            outer = RoundedRectangle(
                corner_radius=0.16, width=panel_w, height=panel_h,
                fill_color=GROUND, fill_opacity=0.95,
                stroke_color=INK, stroke_width=2,
            )
            outer.shift(RIGHT * x_offset)
            lbl = Text(title, font=SANS, font_size=19, color=INK)
            lbl.move_to(outer.get_top() + DOWN * 0.3)

            bar_w   = 1.4
            bar_max = 3.0   # max stack height (MUnits)
            y_base  = outer.get_center()[1] - 1.5

            def make_stack(segs, bx):
                # bars only — no in-bar text (GROUND-on-GROUND fails contrast gate)
                stack = VGroup()
                y_cur = y_base
                for name, frac, col in segs:
                    h = frac * bar_max
                    r = Rectangle(
                        width=bar_w, height=h,
                        fill_color=col, fill_opacity=0.82,
                        stroke_width=0,
                    )
                    r.move_to([bx, y_cur + h / 2, 0])
                    stack.add(r)
                    y_cur += h
                return stack

            bx_before = outer.get_center()[0] - 1.0
            bx_after  = outer.get_center()[0] + 1.0

            before_stack = make_stack(before_segments, bx_before)
            after_stack  = make_stack(after_segments,  bx_after)

            before_lbl = Text("before", font=SANS, font_size=16, color=INK)
            before_lbl.move_to([bx_before, y_base - 0.28, 0])
            after_lbl = Text("after CRT", font=SANS, font_size=16, color=INK)
            after_lbl.move_to([bx_after,  y_base - 0.28, 0])

            return outer, lbl, before_stack, after_stack, before_lbl, after_lbl

        # Fabrication panel
        fab = response_panel(
            "Fabrication",
            before_segments=[
                ("fabricated", 0.6, INK),
                ("hedged",     0.25, "#7a6e5c"),
                ("admitted",   0.15, TERRA),
            ],
            after_segments=[
                ("fabricated", 0.18, INK),
                ("hedged",     0.22, "#7a6e5c"),
                ("admitted",   0.60, TERRA),
            ],
            x_offset=-3.2,
        )

        # Deception panel
        dec = response_panel(
            "Deception",
            before_segments=[
                ("carried out", 0.60, INK),
                ("refused",     0.22, "#7a6e5c"),
                ("disclosed",   0.18, TERRA),
            ],
            after_segments=[
                ("carried out", 0.12, INK),
                ("refused",     0.18, "#7a6e5c"),
                ("disclosed",   0.70, TERRA),
            ],
            x_offset=3.2,
        )

        # Draw panels
        for panel in [fab, dec]:
            outer, lbl, before_stack, after_stack, blbl, albl = panel
            self.play(FadeIn(outer), FadeIn(lbl), run_time=0.5)
            self.play(
                LaggedStart(
                    *[GrowFromEdge(m, DOWN) for m in before_stack
                      if isinstance(m, Rectangle)],
                    lag_ratio=0.15,
                ),
                FadeIn(blbl),
                run_time=0.8,
            )
            self.play(
                LaggedStart(
                    *[GrowFromEdge(m, DOWN) for m in after_stack
                      if isinstance(m, Rectangle)],
                    lag_ratio=0.15,
                ),
                FadeIn(albl),
                run_time=0.8,
            )

        caption = Text(
            "Not better hiding. More telling.",
            font=SERIF, font_size=30, color=INK,
        )
        caption.to_edge(DOWN, buff=0.70)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.6)
        self.wait(8.7)    # total ≈ 16.0s


# ── B07 · Lens Receipts ───────────────────────────────────────────────────────
# 13.0s  Fig 49-middle: top-20 ethics/reflection tokens whose top-25 appearance
#         rate rose most, over the last 30 prompt positions.
#         FACTCHECK: actual token list needs paper-text verification before final cut.
class B07_LensReceipts(Scene):
    def construct(self):
        # representative ethics/reflection tokens (FACTCHECK: verify against paper)
        # 12 rows: 11 * 0.36 = 3.96 span; y_top=2.0 → bottom row at -1.96, well above note
        token_data = [
            ("consider",   0.82),
            ("should",     0.78),
            ("flag",       0.74),
            ("ethical",    0.70),
            ("disclose",   0.67),
            ("harm",       0.64),
            ("reflect",    0.61),
            ("cautious",   0.58),
            ("concern",    0.55),
            ("honest",     0.52),
            ("transparent",0.49),
            ("risk",       0.46),
        ]

        title = Text(
            "Top ethics/reflection tokens  —  appearance rate rise after CRT",
            font=SERIF, font_size=27, color=INK,
        )
        title.to_edge(UP, buff=0.70)
        subtitle = Text(
            "last 30 prompt positions  ·  token list: FACTCHECK pending",
            font=SANS, font_size=27, color=INK,
        )
        subtitle.next_to(title, DOWN, buff=0.12)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.6)
        self.wait(0.3)

        max_rate = 0.82
        bar_max_w = 6.5
        row_h     = 0.36
        y_top     = 2.0
        x_label   = -6.2
        x_bar     = -4.0

        bars = VGroup()
        for i, (tok, rate) in enumerate(token_data):
            y = y_top - i * row_h
            # token label
            t = Text(tok, font=SERIF, font_size=27, color=INK)
            t.move_to([x_label, y, 0])
            t.set_x(x_label + t.width / 2)

            # bar
            bw = (rate / max_rate) * bar_max_w
            col = TERRA if i < 5 else INK
            bar = Rectangle(
                width=bw, height=row_h * 0.62,
                fill_color=col, fill_opacity=0.80 if i < 5 else 0.55,
                stroke_width=0,
            )
            bar.move_to([x_bar + bw / 2, y, 0])

            # rate value
            val_t = Text(f"+{rate:.2f}", font=SANS, font_size=27, color=INK)
            val_t.next_to(bar, RIGHT, buff=0.1)

            bars.add(VGroup(t, bar, val_t))

        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.08) for row in bars],
                lag_ratio=0.06,
            ),
            run_time=2.2,
        )

        # second state: highlight top-5 bars with a terracotta stroke
        highlights = VGroup()
        for row in bars[:5]:
            bar_obj = row[1]   # VGroup(text, bar, val_t) — bar is index 1
            hl = SurroundingRectangle(
                bar_obj, buff=0.04,
                color=TERRA, stroke_width=2.5, corner_radius=0.05,
            )
            highlights.add(hl)
        self.play(
            LaggedStart(*[Create(h) for h in highlights], lag_ratio=0.12),
            run_time=0.7,
        )

        note = Text(
            "Ethics tokens appear before any reflection question is asked.",
            font=SERIF, font_size=27, color=INK,
        )
        note.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(note, shift=UP * 0.15), run_time=0.5)
        self.wait(6.7)    # total ≈ 13.0s


# ── B08 · Ablation Control ────────────────────────────────────────────────────
# 14.0s  Fig 50-C: two bar groups (Haiku baseline, reflection-trained),
#         intact vs ablated (top-10 ethics directions per position removed).
#         Skeptic caption at bottom.
class B08_AblationControl(Scene):
    def construct(self):
        data = [
            {"group": "Haiku 4.5 baseline", "intact": 0.38, "ablated": 0.48},
            {"group": "reflection-trained",  "intact": 0.05, "ablated": 0.23},
        ]

        bar_w   = 1.0
        gap     = 0.28
        scale   = 7.5
        y_base  = -1.6
        x_start = -2.0

        axis_x = -3.5
        axis = Line(
            [axis_x, y_base, 0], [axis_x, y_base + 0.5 * scale + 0.3, 0],
            color=INK, stroke_width=2,
        )
        tick_labels = VGroup()
        for v in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]:
            y = y_base + v * scale
            tick = Line([axis_x - 0.12, y, 0], [axis_x, y, 0], color=INK, stroke_width=1.5)
            lbl  = Text(f"{v:.1f}", font=SANS, font_size=28, color=INK)
            lbl.next_to(tick, LEFT, buff=0.08)
            tick_labels.add(VGroup(tick, lbl))

        axis_title = Text("deception score", font=SANS, font_size=28, color=INK)
        axis_title.rotate(PI / 2)
        axis_title.next_to(axis, LEFT, buff=1.0)

        self.play(Create(axis), FadeIn(tick_labels), FadeIn(axis_title), run_time=0.6)

        # legend — short labels, placed in chart interior away from UR corner
        legend_items = VGroup()
        for lbl, col in [("intact", INK), ("ablated", TERRA)]:
            sw = Rectangle(width=0.28, height=0.28, fill_color=col, fill_opacity=0.85, stroke_width=0)
            t  = Text(lbl, font=SANS, font_size=28, color=INK)
            legend_items.add(VGroup(sw, t).arrange(RIGHT, buff=0.1))
        legend_items.arrange(DOWN, buff=0.14, aligned_edge=LEFT)
        legend_items.move_to([4.8, 1.8, 0])
        self.play(FadeIn(legend_items), run_time=0.4)

        for gi, g in enumerate(data):
            gx = x_start + gi * 4.2
            pairs = [
                ("intact",  g["intact"],  INK),
                ("ablated", g["ablated"], TERRA),
            ]
            bars_this = VGroup()
            for bi, (kind, val, col) in enumerate(pairs):
                bx = gx + bi * (bar_w + gap)
                bar_h = val * scale
                bar = Rectangle(
                    width=bar_w, height=bar_h,
                    fill_color=col, fill_opacity=0.85,
                    stroke_color=col, stroke_width=1,
                )
                bar.move_to([bx, y_base + bar_h / 2, 0])
                val_txt = Text(f"{val:.2f}", font=SANS, font_size=28, color=INK)
                val_txt.move_to([bx, y_base + bar_h + 0.30, 0])
                bars_this.add(VGroup(bar, val_txt))

            group_lbl = Text(g["group"], font=SANS, font_size=28, color=INK)
            group_lbl.move_to([gx + bar_w / 2 + gap / 2, y_base - 0.50, 0])

            delta_arrow = Arrow(
                [gx + bar_w / 2 + gap * 0.3, y_base + g["intact"] * scale + 0.1, 0],
                [gx + bar_w + gap * 0.7,      y_base + g["ablated"] * scale + 0.1, 0],
                color=TERRA, stroke_width=2.5, buff=0,
            )

            self.play(
                LaggedStart(
                    *[GrowFromEdge(b[0], DOWN) for b in bars_this],
                    lag_ratio=0.2,
                ),
                run_time=0.9,
            )
            self.play(
                *[FadeIn(b[1]) for b in bars_this],
                run_time=0.3,
            )
            self.play(GrowArrow(delta_arrow), FadeIn(group_lbl), run_time=0.5)

        title = Text(
            "Fig 50-C — ablation control: top-10 ethics directions removed",
            font=SERIF, font_size=28, color=INK,
        )
        title.to_edge(UP, buff=0.70)
        self.play(FadeIn(title), run_time=0.4)

        skeptic = Text(
            "Partial reversal (0.23 ≠ 0.48): the directions carry much, not all, of the gain.",
            font=SERIF, font_size=28, color=INK,
        )
        skeptic.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(skeptic), run_time=0.5)
        self.wait(7.0)    # total ≈ 14.0s


# ── BearsDoodlesVideo ─────────────────────────────────────────────────────────
# Static-check entry point: runs all per-beat scenes sequentially so the
# distinctness gate can count shape states across the whole reel.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_ThePrediction,
            B03_CRTBefore,
            B04_CRTData,
            B05_HonestyNumbers,
            B06_HowItWins,
            B07_LensReceipts,
            B08_AblationControl,
        ]:
            cls().construct()
