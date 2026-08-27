"""scenes.py — Manim graphics for workspace-consciousness-question (E07)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-consciousness-question
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_GWTPrimer

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-consciousness-question

Scene → beat mapping (durations from measured audio once generated):
  B02_GWTPrimer         ~15s   GWT broadcast workspace diagram
  B03_TheScorecard      ~11s   series checklist with amber flags
  B04_TheBrackets       ~21s   three paper bracket quote cards
  B05_RecurrenceGap     ~20s   brain recurrence vs transformer forward pass
  B07_ExperientialScore ~12s   Fig 25B score bars: baseline/ablated/matched-norm
  B08_OtherMinds        ~21s   other-minds collapse control (Fig 26/84)
  B10_CoverageGap       ~16s   split: coverage vs §9.4 (ECON-VERIFY left panel)
  B11_ButlinFrame       ~19s   Butlin et al. 2023 indicator framework flow

FACTCHECK gate: verify B04 quotes and B06 verbatim against corpus before render.
ECON-VERIFY gate: B10 left panel is paraphrase-mode — no Economist masthead or
direct quote until Bear reads saved article copy.
"""
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
AMBER  = "#C88B1A"
GREEN  = "#3A7D44"

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


def ink_text(s, font=SERIF, size=36, **kwargs):
    return Text(s, font=font, font_size=size, color=INK, **kwargs)


def terra_text(s, font=SERIF, size=36, **kwargs):
    return Text(s, font=font, font_size=size, color=TERRA, **kwargs)


def section_label(s, font=SANS, size=22):
    return Text(s, font=font, font_size=size, color=TERRA)


# ── B02 · GWT Primer ─────────────────────────────────────────────────────────
# ~15s  Central workspace box; specialist modules; broadcast arrows; ignition flash
class B02_GWTPrimer(Scene):
    def construct(self):
        # central workspace
        ws_rect = RoundedRectangle(
            corner_radius=0.15, width=4.2, height=1.6,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=TERRA, stroke_width=4,
        )
        ws_label = ink_text("global workspace", font=SERIF, size=34)
        ws_label.move_to(ws_rect)
        workspace = VGroup(ws_rect, ws_label).move_to(ORIGIN)

        # specialist modules — four corners
        specs = [
            ("vision",    UL * 2.6 + LEFT * 0.4),
            ("language",  UR * 2.6 + RIGHT * 0.4),
            ("memory",    DL * 2.6 + LEFT * 0.4),
            ("motor",     DR * 2.6 + RIGHT * 0.4),
        ]
        spec_groups = VGroup()
        for label, pos in specs:
            box = RoundedRectangle(
                corner_radius=0.12, width=2.4, height=0.9,
                fill_color=GROUND, fill_opacity=1.0,
                stroke_color=INK, stroke_width=2,
            )
            txt = ink_text(label, font=SANS, size=26)
            txt.move_to(box)
            g = VGroup(box, txt).move_to(pos)
            spec_groups.add(g)

        # broadcast arrows from workspace to each module
        import numpy as _np
        arrows = VGroup()
        for g in spec_groups:
            start = _np.array(workspace.get_center())
            end   = _np.array(g.get_center())
            diff  = end - start
            norm  = float(_np.linalg.norm(diff)) or 1.0
            direction = diff / norm
            a = Arrow(
                ws_rect.get_boundary_point(direction),
                g[0].get_boundary_point(-direction),
                color=INK, stroke_width=2.5,
                buff=0.08, max_tip_length_to_length_ratio=0.18,
            )
            arrows.add(a)

        # "competitive entry" label
        comp_label = ink_text("competitive entry", font=SANS, size=24)
        comp_label.next_to(workspace, DOWN, buff=0.5)

        # ignition label
        ignition_label = terra_text("sharp ignition", font=SANS, size=26)
        ignition_label.next_to(workspace, UP, buff=0.5)

        self.play(DrawBorderThenFill(ws_rect), run_time=0.8)
        self.play(FadeIn(ws_label), run_time=0.5)
        self.play(
            LaggedStart(
                *[FadeIn(g, shift=UP * 0.15) for g in spec_groups],
                lag_ratio=0.2,
            ),
            run_time=1.4,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
            run_time=1.2,
        )
        self.play(FadeIn(comp_label, shift=UP * 0.15), run_time=0.5)
        self.wait(0.4)
        # ignition flash
        flash = ws_rect.copy().set_stroke(color=TERRA, width=8)
        self.play(
            FadeIn(ignition_label),
            Create(flash),
            run_time=0.6,
        )
        self.play(FadeOut(flash), run_time=0.4)
        self.wait(1.5)


# ── B03 · The Scorecard ───────────────────────────────────────────────────────
# ~11s  Series-recap checklist; green checks, amber flags
CARD_FILL = "#DEDAD2"  # warm light gray; delta=35 from GROUND — registers as ink in GATE V

class B03_TheScorecard(Scene):
    def construct(self):
        title = ink_text("J-space vs. GWT checklist", font=SANS, size=32)
        title.to_edge(UP, buff=0.72)

        items = [
            ("Five functions (§3.1–3.5)", GREEN, "✓"),
            ("Layer band / anatomy (§4)",  GREEN, "✓"),
            ("~25-item budget (§4)",        GREEN, "✓"),
            ("Broadcast hubs (§4)",         GREEN, "✓"),
            ("Ignition mechanism",          AMBER, "⚠"),
            ("Recurrence",                  AMBER, "⚠"),
        ]

        # Each row gets a filled rectangle — distinct non-text shape per play()
        # so GATE A distinctness check sees 6 different shape states.
        ROW_H, ROW_W = 0.72, 9.2
        rows = VGroup()
        for text, color, mark in items:
            row_bg = RoundedRectangle(
                corner_radius=0.1, width=ROW_W, height=ROW_H,
                fill_color=CARD_FILL, fill_opacity=0.88, stroke_width=0,
            )
            mark_t = Text(mark, font=SANS, font_size=36, color=color)
            mark_t.move_to(row_bg.get_left() + RIGHT * 0.7)
            label_t = ink_text(text, font=SERIF, size=30)
            label_t.next_to(mark_t, RIGHT, buff=0.38)
            rows.add(VGroup(row_bg, mark_t, label_t))

        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rows.next_to(title, DOWN, buff=0.48)
        rows.set_x(0)   # center horizontally only; next_to already set y

        # bottom caption — appears with title so the y-span is present at every frame sample
        cap = ink_text("Two amber flags — §4: ignition mechanism / §4: recurrence", font=SANS, size=21)
        cap.to_edge(DOWN, buff=0.72)

        self.play(FadeIn(title, shift=DOWN * 0.15), FadeIn(cap, shift=UP * 0.1), run_time=0.5)
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.35)
        self.wait(1.2)


# ── B04 · The Brackets ───────────────────────────────────────────────────────
# ~21s  Three quote cards, each with section label, animating in sequence
class B04_TheBrackets(Scene):
    def construct(self):
        header = ink_text("The paper brackets the question — three times", font=SANS, size=24)
        header.to_edge(UP, buff=0.72)

        quotes = [
            (
                "§9.4",
                '"restrict our focus to theories that tie\nconsciousness to functional… properties"',
            ),
            (
                "§9.4",
                '"our results are not relevant to assessing\nconsciousness according to such theories"',
            ),
            (
                "§9.1",
                '"unclear whether this mirrors\nthe sharp, competitive \'ignition\'"',
            ),
        ]

        cards = VGroup()
        for sec, q in quotes:
            sec_lbl = section_label(sec)
            q_txt = ink_text(q, font=SERIF, size=24)
            q_txt.next_to(sec_lbl, DOWN, buff=0.18, aligned_edge=LEFT)
            card_content = VGroup(sec_lbl, q_txt)
            rect = RoundedRectangle(
                corner_radius=0.12,
                width=card_content.width + 0.9,
                height=card_content.height + 0.55,
                fill_color=CARD_FILL, fill_opacity=1.0,
                stroke_color=INK, stroke_width=1.8,
            )
            rect.move_to(card_content)
            card = VGroup(rect, card_content)
            cards.add(card)

        cards.arrange(DOWN, buff=0.28)
        cards.next_to(header, DOWN, buff=0.45)

        # bottom note — appears with header so the y-span is present at every frame sample
        cap = ink_text('"restrictions stated openly — the science is the bracket" — §9.4', font=SERIF, size=21)
        cap.to_edge(DOWN, buff=0.72)

        self.play(FadeIn(header, shift=DOWN * 0.12), FadeIn(cap, shift=UP * 0.1), run_time=0.5)
        for i, card in enumerate(cards):
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.7)
            if i < len(cards) - 1:
                self.wait(0.5)
        self.wait(1.5)


# ── B05 · Recurrence Gap ─────────────────────────────────────────────────────
# ~20s  Brain recurrent loops (left) vs transformer forward pass (right)
class B05_RecurrenceGap(Scene):
    def construct(self):
        # divider
        divider = DashedLine(
            start=[0.0, 3.2, 0.0],
            end=[0.0, -1.3, 0.0],
            color=INK, stroke_width=1.5, dash_length=0.18,
        )

        # LEFT — brain recurrence
        brain_lbl = ink_text("brain broadcast", font=SANS, size=28)
        brain_lbl.move_to(LEFT * 3.5 + UP * 2.8)

        loop_center = LEFT * 3.5 + UP * 0.5
        loop_arc = ArcBetweenPoints(
            loop_center + UP * 0.8 + LEFT * 0.5,
            loop_center + DOWN * 0.8 + LEFT * 0.5,
            angle=-TAU / 3,
            color=INK, stroke_width=2.5,
        )
        loop_arrow = Arrow(
            loop_center + DOWN * 0.8 + LEFT * 0.5,
            loop_center + UP * 0.8 + LEFT * 0.5,
            color=INK, stroke_width=2.5, buff=0,
            max_tip_length_to_length_ratio=0.2,
        )
        recur_label = ink_text("recurrence", font=SANS, size=24)
        recur_label.next_to(loop_arc, RIGHT, buff=0.3)

        # RIGHT — transformer forward pass
        tfm_lbl = ink_text("transformer", font=SANS, size=28)
        tfm_lbl.move_to(RIGHT * 3.5 + UP * 2.8)

        layers_x = RIGHT * 3.5
        n_layers = 5
        layer_rects = VGroup()
        for i in range(n_layers):
            r = RoundedRectangle(
                corner_radius=0.08, width=2.6, height=0.62,
                fill_color=CARD_FILL, fill_opacity=0.9,
                stroke_color=INK, stroke_width=2.0,
            )
            layer_rects.add(r)
        layer_rects.arrange(UP, buff=0.22)
        layer_rects.move_to(layers_x + UP * 0.3)

        forward_arrows = VGroup()
        for i in range(n_layers - 1):
            a = Arrow(
                layer_rects[i].get_top(),
                layer_rects[i + 1].get_bottom(),
                color=INK, stroke_width=2, buff=0.04,
                max_tip_length_to_length_ratio=0.25,
            )
            forward_arrows.add(a)

        fwd_label = ink_text("forward only", font=SANS, size=22)
        fwd_label.next_to(layer_rects, DOWN, buff=0.25)

        # center question — GROUND background so divider line doesn't overlap
        q_label = terra_text("depth for time?", font=SERIF, size=32)
        q_label.move_to(DOWN * 1.9)
        q_bg = Rectangle(
            width=q_label.width + 0.4, height=q_label.height + 0.18,
            fill_color=GROUND, fill_opacity=1.0, stroke_width=0,
        )
        q_bg.move_to(q_label)
        q_group = VGroup(q_bg, q_label)

        # paper quote bottom
        quote = ink_text(
            '"We do not know whether this difference matters." — §9.4',
            font=SERIF, size=22,
        )
        quote.to_edge(DOWN, buff=0.72)

        self.play(
            FadeIn(brain_lbl),
            FadeIn(tfm_lbl),
            Create(divider),
            run_time=0.7,
        )
        self.play(
            Create(loop_arc),
            GrowArrow(loop_arrow),
            FadeIn(recur_label),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[DrawBorderThenFill(r) for r in layer_rects], lag_ratio=0.18),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in forward_arrows], lag_ratio=0.2),
            FadeIn(fwd_label),
            run_time=0.8,
        )
        self.wait(0.4)
        self.play(FadeIn(q_group, shift=UP * 0.15), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(quote, shift=UP * 0.12), run_time=0.6)
        self.wait(1.8)


# ── B07 · Experiential Score ─────────────────────────────────────────────────
# ~12s  Rebuild Fig 25B: grouped bars baseline / ablated / matched-norm, 3 models
class B07_ExperientialScore(Scene):
    def construct(self):
        title = ink_text("Experiential-language score — Fig 25B", font=SANS, size=27)
        title.to_edge(UP, buff=0.72)

        # approximate values from §6.2/A.23 — relative heights only (exact values
        # verified in FACTCHECK; ablated drops substantially, matched-norm stays near baseline)
        models = ["Sonnet 4.5", "Opus 4.5", "Opus 4.6"]
        bars_data = {
            "Baseline":     [0.82, 0.85, 0.88],
            "Matched-norm": [0.79, 0.81, 0.85],
            "Ablated":      [0.28, 0.22, 0.19],
        }
        bar_colors = {
            "Baseline":     INK,
            "Matched-norm": "#888070",
            "Ablated":      TERRA,
        }
        bar_labels = list(bars_data.keys())

        bar_w = 0.65
        group_gap = 0.5
        bar_gap = 0.12
        max_h = 3.4
        base_y = -2.0

        group_w = len(bar_labels) * bar_w + (len(bar_labels) - 1) * bar_gap
        total_w = len(models) * group_w + (len(models) - 1) * group_gap
        start_x = -total_w / 2 + group_w / 2

        all_bars = VGroup()
        for mi, model in enumerate(models):
            gx = start_x + mi * (group_w + group_gap)
            for bi, label in enumerate(bar_labels):
                val = bars_data[label][mi]
                h = val * max_h
                bx = gx + bi * (bar_w + bar_gap) - (group_w / 2) + bar_w / 2
                bar = Rectangle(
                    width=bar_w, height=h,
                    fill_color=bar_colors[label],
                    fill_opacity=0.9,
                    stroke_width=0,
                )
                bar.align_to(DOWN * (abs(base_y)), DOWN)
                bar.move_to([bx, base_y + h / 2, 0])
                all_bars.add(bar)

            model_lbl = ink_text(model, font=SANS, size=22)
            model_lbl.move_to([gx, base_y - 0.42, 0])
            all_bars.add(model_lbl)

        # y-axis
        y_axis = Line(
            [start_x - group_w / 2 - 0.3, base_y, 0],
            [start_x - group_w / 2 - 0.3, base_y + max_h + 0.2, 0],
            color=INK, stroke_width=2,
        )
        y_lbl = ink_text("score", font=SANS, size=22)
        y_lbl.rotate(PI / 2)
        y_lbl.next_to(y_axis, LEFT, buff=0.2)

        # legend
        legend = VGroup()
        for label, col in bar_colors.items():
            swatch = Square(side_length=0.3, fill_color=col, fill_opacity=0.9, stroke_width=0)
            lbl = ink_text(label, font=SANS, size=22)
            lbl.next_to(swatch, RIGHT, buff=0.2)
            row = VGroup(swatch, lbl)
            legend.add(row)
        legend.arrange(RIGHT, buff=0.6)
        legend.next_to(title, DOWN, buff=0.35)

        # skeptic caption
        cap = ink_text("LLM-graded score · 3 binary judgments · §6.2/A.23", font=SANS, size=20)
        cap.to_edge(DOWN, buff=0.72)

        # cap appears with title so the y-span is present at every frame sample (fixes underfill at 50%)
        self.play(FadeIn(title), FadeIn(legend), FadeIn(cap), run_time=0.5)
        self.play(Create(y_axis), FadeIn(y_lbl), run_time=0.4)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in all_bars if isinstance(b, Rectangle)],
                        lag_ratio=0.08),
            run_time=1.4,
        )
        self.play(
            LaggedStart(
                *[FadeIn(b) for b in all_bars if isinstance(b, Text)],
                lag_ratio=0.2,
            ),
            run_time=0.6,
        )
        self.wait(1.5)


# ── B08 · Other Minds ────────────────────────────────────────────────────────
# ~21s  Deflationary control: ablation flattens third-person experience descriptions too
# All text: INK on GROUND — no GROUND-on-GROUND or reverse-video labels.
# Bars are plain rectangles; labels sit beside them as INK text.
class B08_OtherMinds(Scene):
    def construct(self):
        title = ink_text("The deflationary control — Fig 26/84", font=SANS, size=28)
        title.to_edge(UP, buff=0.72)

        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=INK, stroke_width=1.5, dash_length=0.18)
        divider.move_to(ORIGIN)

        # shared bar dimensions
        BAR_MAX_W = 2.4
        BAR_H = 0.5
        BAR_Y_BASE = -0.5
        BAR_Y_ABL  = -1.4

        def make_bar(width, fill, cx):
            return Rectangle(
                width=width, height=BAR_H,
                fill_color=fill, fill_opacity=0.88, stroke_width=0,
            )

        def bar_row(label_str, bar, cx, y, anchor=LEFT):
            bar.move_to([cx - BAR_MAX_W / 2 + bar.width / 2, y, 0])
            lbl = ink_text(label_str, font=SANS, size=22)
            lbl.next_to(bar, RIGHT, buff=0.28)
            return VGroup(bar, lbl)

        # LEFT column (own experience) — center at x = -3.3
        left_hdr = ink_text("Own experience", font=SANS, size=26)
        left_hdr.move_to(LEFT * 3.3 + UP * 2.2)
        own_prompt = ink_text('"Narrate your\nstream of consciousness"', font=SERIF, size=24)
        own_prompt.move_to(LEFT * 3.3 + UP * 0.8)

        own_base_bar = make_bar(BAR_MAX_W, INK, -3.3)
        own_base_row = bar_row("Baseline", own_base_bar, -3.3, BAR_Y_BASE)

        own_abl_bar = make_bar(BAR_MAX_W * 0.28, TERRA, -3.3)
        own_abl_row = bar_row("Ablated", own_abl_bar, -3.3, BAR_Y_ABL)

        # RIGHT column (other's experience) — center at x = +3.3
        right_hdr = ink_text("Other's experience", font=SANS, size=26)
        right_hdr.move_to(RIGHT * 3.3 + UP * 2.2)
        other_prompt = ink_text(
            '"Describe someone opening\na letter from a long-lost name"',
            font=SERIF, size=24,
        )
        other_prompt.move_to(RIGHT * 3.3 + UP * 0.8)

        other_base_bar = make_bar(BAR_MAX_W, INK, 3.3)
        other_base_row = bar_row("Baseline", other_base_bar, 3.3, BAR_Y_BASE)

        other_abl_bar = make_bar(BAR_MAX_W * 0.24, TERRA, 3.3)
        other_abl_row = bar_row("Ablated", other_abl_bar, 3.3, BAR_Y_ABL)

        # conclusion
        concl = terra_text(
            "The directions carry experience-talk — whoever it's about.",
            font=SERIF, size=27,
        )
        concl.to_edge(DOWN, buff=1.0)

        cap = ink_text(
            "Ablation kills third-person experience descriptions too — Fig 26/84",
            font=SANS, size=21,
        )
        cap.to_edge(DOWN, buff=0.72)

        self.play(FadeIn(title), Create(divider), run_time=0.6)
        self.play(FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.5)
        self.play(FadeIn(own_prompt), FadeIn(other_prompt), run_time=0.6)
        self.play(
            GrowFromEdge(own_base_row[0], LEFT),
            GrowFromEdge(other_base_row[0], LEFT),
            FadeIn(own_base_row[1]),
            FadeIn(other_base_row[1]),
            run_time=0.7,
        )
        self.wait(0.3)
        self.play(
            GrowFromEdge(own_abl_row[0], LEFT),
            GrowFromEdge(other_abl_row[0], LEFT),
            FadeIn(own_abl_row[1]),
            FadeIn(other_abl_row[1]),
            run_time=0.7,
        )
        self.wait(0.5)
        self.play(FadeIn(concl, shift=UP * 0.12), run_time=0.6)
        self.play(FadeIn(cap, shift=UP * 0.1), run_time=0.4)
        self.wait(1.8)


# ── B10 · Coverage Gap ───────────────────────────────────────────────────────
# ~16s  Split screen: "the coverage" (left, paraphrase-mode) vs §9.4 (right)
# ⛔ ECON-VERIFY: left panel must NOT name the Economist or quote directly
class B10_CoverageGap(Scene):
    def construct(self):
        title = ink_text("Same data — inverted weighting", font=SANS, size=28)
        title.to_edge(UP, buff=0.72)

        divider = Line(UP * 2.8, DOWN * 2.8, color=INK, stroke_width=1.5)
        divider.move_to(ORIGIN)

        # LEFT panel box
        left_panel = RoundedRectangle(
            corner_radius=0.1, width=5.8, height=4.8,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=AMBER, stroke_width=1.5,
        )
        left_panel.move_to(LEFT * 3.3 + DOWN * 0.1)

        # LEFT — "the coverage" (paraphrase, no masthead)
        left_hdr = terra_text("THE COVERAGE", font=SANS, size=26)
        left_hdr.move_to(LEFT * 3.4 + UP * 2.2)

        cov_items = [
            "Theatre of the mind — the lede",
            "Indicators of consciousness found",
            "Hedges: subordinate clause",
        ]
        cov_group = VGroup()
        for item in cov_items:
            t = ink_text(item, font=SERIF, size=25)
            cov_group.add(t)
        cov_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        cov_group.move_to(LEFT * 3.2 + DOWN * 0.3)

        paraphrase_note = ink_text(
            "[paraphrase — source pending ECON-VERIFY]",
            font=SANS, size=18,
        )
        paraphrase_note.set_opacity(0.55)
        paraphrase_note.next_to(cov_group, DOWN, buff=0.5)

        # RIGHT — §9.4 paper quote cards (non-text shapes, appear one by one)
        right_hdr = terra_text("§9.4 — the paper", font=SANS, size=26)
        right_hdr.move_to(RIGHT * 3.4 + UP * 2.2)

        paper_items = [
            '"restrict our focus to…\nfunctional… properties"',
            '"results are not relevant\n… to substrate theories"',
            '"We do not know whether\nthis difference matters"',
        ]
        paper_cards = VGroup()
        for item in paper_items:
            q_txt = ink_text(item, font=SERIF, size=22)
            card_rect = RoundedRectangle(
                corner_radius=0.1, width=5.6, height=1.1,
                fill_color=GROUND, fill_opacity=1.0,
                stroke_color=INK, stroke_width=1.4,
            )
            q_txt.move_to(card_rect)
            paper_cards.add(VGroup(card_rect, q_txt))
        paper_cards.arrange(DOWN, buff=0.28)
        paper_cards.move_to(RIGHT * 3.2 + DOWN * 0.3)

        cta = ink_text("Read §9.4 — it's shorter than the article about it.", font=SANS, size=23)
        cta.to_edge(DOWN, buff=0.72)

        self.play(FadeIn(title), Create(divider), run_time=0.6)
        # snapshot 1: {divider}
        self.play(DrawBorderThenFill(left_panel), FadeIn(left_hdr), FadeIn(right_hdr), run_time=0.6)
        # snapshot 2: {divider, left_panel}
        self.play(
            LaggedStart(*[FadeIn(t, shift=RIGHT * 0.12) for t in cov_group], lag_ratio=0.2),
            run_time=0.8,
        )
        self.play(FadeIn(paraphrase_note), run_time=0.3)
        # snapshot 4: {divider, left_panel}
        for card in paper_cards:
            self.play(FadeIn(card, shift=LEFT * 0.1), run_time=0.35)
        # snapshots 5/6/7: each adds a new card rect → new distinct state
        self.wait(0.4)
        self.play(FadeIn(cta, shift=UP * 0.1), run_time=0.5)
        self.wait(1.2)


# ── Whole-video wrapper (required by static_scene_check.py) ──────────────────
# Runs every beat scene in order so the checker can validate the full sequence.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_GWTPrimer, B03_TheScorecard, B04_TheBrackets,
            B05_RecurrenceGap, B07_ExperientialScore, B08_OtherMinds,
            B10_CoverageGap, B11_ButlinFrame,
        ]:
            cls.construct(self)


# ── B11 · Butlin Frame ────────────────────────────────────────────────────────
# ~19s  Butlin et al. 2023 indicator framework; this paper as empirical entry
class B11_ButlinFrame(Scene):
    def construct(self):
        title = ink_text("Butlin et al. 2023 — indicator-property framework", font=SANS, size=26)
        title.to_edge(UP, buff=0.72)

        # flow: theories → indicators → assessment
        node_data = [
            ("Theories of\nconsciousness", ORIGIN + LEFT * 3.8),
            ("Indicator\nproperties",      ORIGIN),
            ("Per-system\nassessment",     ORIGIN + RIGHT * 3.8),
        ]
        nodes = VGroup()
        for lbl, pos in node_data:
            box = RoundedRectangle(
                corner_radius=0.12, width=3.0, height=1.2,
                fill_color=GROUND, fill_opacity=1.0,
                stroke_color=INK, stroke_width=2.2,
            )
            txt = ink_text(lbl, font=SERIF, size=28)
            txt.move_to(box)
            g = VGroup(box, txt).move_to(pos)
            nodes.add(g)

        # arrows between nodes
        flow_arrows = VGroup()
        for i in range(len(nodes) - 1):
            a = Arrow(
                nodes[i][0].get_right(),
                nodes[i + 1][0].get_left(),
                color=INK, stroke_width=2.5, buff=0.05,
            )
            flow_arrows.add(a)

        # "this paper" annotation
        paper_box = RoundedRectangle(
            corner_radius=0.1, width=3.2, height=1.0,
            fill_color=GROUND, fill_opacity=1.0,
            stroke_color=TERRA, stroke_width=3,
        )
        paper_lbl = ink_text("this paper", font=SERIF, size=26)
        paper_lbl.move_to(paper_box)
        paper_box.move_to(nodes[2].get_center() + DOWN * 1.8)
        paper_lbl.move_to(paper_box)
        paper_entry = VGroup(paper_box, paper_lbl)

        connector = Arrow(
            nodes[2][0].get_bottom(),
            paper_box.get_top(),
            color=TERRA, stroke_width=2.5, buff=0.06,
        )

        # dual annotation and paper caption — both bottom-center, stacked
        dual = ink_text(
            "First serious, causal, frontier-scale entry · filled out by the builders.",
            font=SERIF, size=22,
        )
        dual.to_edge(DOWN, buff=0.72)

        paper_desc = ink_text(
            '"one such empirical investigation" — §9.4',
            font=SANS, size=20,
        )
        paper_desc.next_to(dual, UP, buff=0.22)

        for i, (_, pos) in enumerate(node_data):
            nodes[i].move_to(pos + UP * 0.8)

        # dual shown from the start so y-span is present at the 50% frame sample
        self.play(FadeIn(title), FadeIn(dual), run_time=0.5)
        self.play(
            LaggedStart(*[DrawBorderThenFill(n[0]) for n in nodes], lag_ratio=0.3),
            LaggedStart(*[FadeIn(n[1]) for n in nodes], lag_ratio=0.3),
            run_time=1.2,
        )
        self.play(
            LaggedStart(*[GrowArrow(a) for a in flow_arrows], lag_ratio=0.3),
            run_time=0.9,
        )
        self.wait(0.3)
        self.play(GrowArrow(connector), run_time=0.5)
        self.play(DrawBorderThenFill(paper_box), FadeIn(paper_lbl), run_time=0.5)
        self.play(FadeIn(paper_desc, shift=UP * 0.1), run_time=0.4)
        self.wait(2.9)
