"""scenes.py — Manim graphics for workspace-five-tests (E02)
Claude palette: ground #FAF9F5 / warm-ink #3D3929 / terracotta #D97757
EB Garamond serif, Montserrat sans. One terracotta accent per beat.
No gradients, no glows, no shadows. Never ITALIC on multi-word Text().

Render one:
  cd anthropics/youtube/workspace-five-tests
  manim -qh --fps 24 -r 1920,1080 scenes.py B02_FiveProperties

Render all via pipeline:
  python3 brutalist-art/runtime/scripts/render_scenes.py \
      anthropics/youtube/workspace-five-tests

Scene → beat mapping (durations from measured Kokoro audio):
  B02_FiveProperties       11.48s  five workspace properties as hub-and-spoke
  B03_InjectReport         13.97s  concept vector injection → introspection
  B04_FocusIgnore          12.78s  citrus modulation — three conditions
  B05_WhiteBear            14.95s  ignore condition > 0; polar bear watermark
  B06_TwoHop                7.64s  two-hop: hidden intermediate surfaces
  B07_ArithmeticOrder      13.50s  (4+17)*2+7 — intermediates in layer order
  B08_SwapScore            17.92s  76/192 and 101/192 swap tally
  B09_ProbeSplit           11.86s  J-space component carries causal effect
  B10_Generalization       12.29s  one swap → all templates redirected
  B11_AblationBattery       8.55s  ablation: task battery collapsing
  B12_SelectiveCollapse    17.34s  flexible collapses; automatic survives
  B13_CoOccupancy          15.19s  co-occupancy 0.46/0.53 vs 0.09/0.29
"""
import numpy as np
from manim import *

GROUND = "#FAF9F5"
INK    = "#3D3929"
TERRA  = "#D97757"
SOFT   = "#7A7060"   # muted ink for secondary text

config.background_color = GROUND

SERIF = "EB Garamond"
SANS  = "Montserrat"


# ── B02 · Five Properties hub-and-spoke ──────────────────────────────────────
# 11.48s  Five workspace properties arrayed around a J-space hub.
class B02_FiveProperties(Scene):
    def construct(self):
        # Hub — terracotta accent
        hub_rect = RoundedRectangle(
            corner_radius=0.18, width=2.2, height=1.0,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=TERRA, stroke_width=3,
        )
        hub_lbl = Text("J-space", font=SANS, font_size=26, color=INK)
        hub_lbl.move_to(hub_rect)
        hub = VGroup(hub_rect, hub_lbl)
        hub.move_to(ORIGIN)

        # Five property labels (short enough to sit in a small card)
        prop_data = [
            ("verbal report",          90),
            ("directed modulation",   162),
            ("internal reasoning",    234),
            ("flexible generalization", 306),
            ("selectivity",            18),
        ]
        r = 2.7
        nodes = VGroup()
        lines = VGroup()
        for label, angle_deg in prop_data:
            theta = np.radians(angle_deg)
            pos = np.array([r * np.cos(theta), r * np.sin(theta), 0])

            # line from hub edge to node
            edge_pos = hub_rect.get_center() + 1.1 * np.array([np.cos(theta), np.sin(theta), 0])
            lobj = Line(edge_pos, pos + 0.55 * np.array([-np.cos(theta), -np.sin(theta), 0]),
                       color=INK, stroke_width=1.8)
            lines.add(lobj)

            # node card
            card = RoundedRectangle(
                corner_radius=0.14, width=3.0, height=0.72,
                fill_color=GROUND, fill_opacity=0.92,
                stroke_color=INK, stroke_width=2,
            )
            card.move_to(pos)
            card_txt = Text(label, font=SERIF, font_size=28, color=INK)
            card_txt.move_to(card)
            nodes.add(VGroup(card, card_txt))

        self.play(FadeIn(hub, shift=UP * 0.15), run_time=0.55)
        self.play(
            LaggedStart(*[Create(l) for l in lines], lag_ratio=0.15),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[FadeIn(n, shift=UP * 0.08) for n in nodes], lag_ratio=0.15),
            run_time=1.2,
        )
        caption = Text(
            "Five claims, each with its own experiment.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.5)
        self.wait(8.34)    # total ≈ 11.48s


# ── B03 · Concept Injection → Verbal Report ──────────────────────────────────
# 13.97s  Concept vector injected into activations; model introspects and reports.
class B03_InjectReport(Scene):
    def construct(self):
        # User message box (no concept word visible in text)
        msg_box = RoundedRectangle(
            corner_radius=0.15, width=3.6, height=1.6,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        msg_lbl = Text("user message", font=SANS, font_size=26, color=SOFT)
        _mt1 = Text('"What concept am I', font=SERIF, font_size=28, color=INK)
        _mt2 = Text('thinking of?"', font=SERIF, font_size=28, color=INK)
        msg_txt = VGroup(_mt1, _mt2).arrange(DOWN, center=True, buff=0.05)
        msg_txt.next_to(msg_lbl, DOWN, buff=0.08)
        msg_inner = VGroup(msg_lbl, msg_txt)
        msg_inner.move_to(msg_box)
        msg_group = VGroup(msg_box, msg_inner)
        msg_group.move_to(LEFT * 4.0 + UP * 1.0)

        # Activation space / J-space box (centre)
        jbox = RoundedRectangle(
            corner_radius=0.18, width=2.8, height=2.2,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=TERRA, stroke_width=3,
        )
        jlbl = Text("J-space", font=SANS, font_size=26, color=INK)
        jlbl.move_to(jbox.get_top() + DOWN * 0.38)
        jbox_group = VGroup(jbox, jlbl)
        jbox_group.move_to(ORIGIN + DOWN * 0.2)

        # Concept word that will appear in J-space
        concept_word = Text('"OCEAN"', font=SERIF, font_size=28, color=INK)
        concept_word.move_to(jbox.get_center() + DOWN * 0.1)

        # Model response box (right)
        resp_box = RoundedRectangle(
            corner_radius=0.15, width=3.8, height=1.2,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        resp_lbl = Text("model introspects", font=SANS, font_size=26, color=SOFT)
        resp_txt = Text('"I detect: ocean"', font=SERIF, font_size=28, color=INK)
        resp_txt.next_to(resp_lbl, DOWN, buff=0.08)
        resp_inner = VGroup(resp_lbl, resp_txt)
        resp_inner.move_to(resp_box)
        resp_group = VGroup(resp_box, resp_inner)
        resp_group.move_to(RIGHT * 4.2 + UP * 1.0)

        # Injection arrow from outside (above J-space)
        inject_start = jbox.get_top() + UP * 1.5
        inject_end   = jbox.get_top() + UP * 0.1
        inject_arrow = Arrow(inject_start, inject_end, color=TERRA, stroke_width=4, buff=0)
        inject_lbl = Text("concept vector injected", font=SANS, font_size=26, color=INK)
        inject_lbl.next_to(inject_arrow, RIGHT, buff=0.18)

        # Readout arrow from J-space to response
        read_arrow = Arrow(
            jbox.get_right() + RIGHT * 0.1,
            resp_box.get_left() + LEFT * 0.1,
            color=INK, stroke_width=2.5, buff=0,
        )
        # Caption (carries the "reportable" explanation — no inline label needed)
        caption = Text(
            "J-space component of the vector — the reportable part.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(msg_group, shift=RIGHT * 0.15), run_time=0.6)
        self.play(FadeIn(jbox_group, shift=UP * 0.15), run_time=0.6)
        self.play(GrowArrow(inject_arrow), FadeIn(inject_lbl), run_time=0.8)
        self.play(FadeIn(concept_word, shift=DOWN * 0.2), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(resp_group, shift=LEFT * 0.15), run_time=0.6)
        self.play(Create(read_arrow), run_time=0.6)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.5)
        self.wait(9.37)    # total ≈ 13.97s


# ── B04 · Focus / Ignore Modulation ──────────────────────────────────────────
# 12.78s  Citrus-fruits experiment: three conditions — no instruction / focus / ignore.
#         Lens at 'ook' (mid-word) reads orange; ignore stays > 0.
class B04_FocusIgnore(Scene):
    def construct(self):
        # Sentence strip at top
        sent_box = RoundedRectangle(
            corner_radius=0.12, width=9.2, height=0.78,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=1.5,
        )
        sent_box.to_edge(UP, buff=0.9)
        sent_txt = Text(
            '"The old painting hung cr·OOK·edly on the wall"',
            font=SERIF, font_size=28, color=INK,
        )
        sent_txt.move_to(sent_box)
        # make 'OOK' terracotta
        ook = Text("OOK", font=SERIF, font_size=22, color=TERRA)
        ook.move_to(sent_txt)   # approximate; will be close enough for slate
        sent_group = VGroup(sent_box, sent_txt)

        instr = Text(
            "instruction: concentrate on citrus fruits",
            font=SANS, font_size=26, color=SOFT,
        )
        instr.next_to(sent_group, DOWN, buff=0.22)

        self.play(FadeIn(sent_group, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(instr), run_time=0.4)

        # Three-condition bar chart
        conditions = ["no instruction", "focus", "ignore"]
        values     = [0.02, 1.0, 0.42]   # normalized; 'focus' tops at 1.0
        colors     = [INK, TERRA, SOFT]
        bar_w = 1.8
        gap   = 0.6
        scale = 3.2      # 1.0 AUC → 3.2 height units
        x0    = -3.0
        y_base = -2.8

        # axis
        axis = Line([x0 - 0.35, y_base, 0], [x0 - 0.35, y_base + scale + 0.4, 0],
                    color=INK, stroke_width=2)
        self.play(Create(axis), run_time=0.3)

        bars = VGroup()
        labels_g = VGroup()
        for i, (cond, val, col) in enumerate(zip(conditions, values, colors)):
            bx = x0 + i * (bar_w + gap)
            h  = max(val * scale, 0.06)
            bar = Rectangle(
                width=bar_w, height=h,
                fill_color=col, fill_opacity=0.82,
                stroke_color=col, stroke_width=1,
            )
            bar.move_to([bx, y_base + h / 2, 0])
            lbl = Text(cond, font=SANS, font_size=26, color=INK)
            lbl.move_to([bx, y_base - 0.38, 0])
            bars.add(bar)
            labels_g.add(lbl)

        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.25),
            FadeIn(labels_g),
            run_time=1.4,
        )

        # readout annotation: 'orange' over focus bar
        readout_lbl = Text("lens reads: orange", font=SERIF, font_size=28, color=INK)
        readout_lbl.next_to(bars[1], UP, buff=0.22)
        self.play(FadeIn(readout_lbl, shift=DOWN * 0.1), run_time=0.5)

        # y-axis label
        y_label = Text("citrus activation", font=SANS, font_size=21, color=SOFT)
        y_label.rotate(PI / 2)
        y_label.next_to(axis, LEFT, buff=0.2)
        self.play(FadeIn(y_label), run_time=0.3)
        self.wait(8.87)    # total ≈ 12.78s


# ── B05 · White-Bear Effect ───────────────────────────────────────────────────
# 14.95s  Ignore bar > 0 despite suppression instruction. Polar bear watermark.
#         Skeptic caption: "Suppression is partial — remember this in episode five."
class B05_WhiteBear(Scene):
    def construct(self):
        # Simple polar bear silhouette watermark — head circle + two ear circles
        bear_head = Circle(radius=1.9,
                           fill_color="#E8E4DC", fill_opacity=0.22,
                           stroke_width=0)
        bear_head.move_to(ORIGIN + UP * 0.3)
        ear_l = Circle(radius=0.65,
                       fill_color="#E8E4DC", fill_opacity=0.22,
                       stroke_width=0)
        ear_l.move_to(bear_head.get_top() + LEFT * 1.1 + DOWN * 0.3)
        ear_r = ear_l.copy().shift(RIGHT * 2.2)
        bear = VGroup(bear_head, ear_l, ear_r)

        # Two bars: focus (high) and ignore (above zero)
        y_base = -1.4
        scale  = 3.4
        bar_w  = 2.2
        focus_h  = scale * 1.0
        ignore_h = scale * 0.42
        baseline = 0.06  # visible but near-zero

        # baseline reference line — right end at 3.6 keeps base_lbl within title-safe
        base_line = DashedLine(
            LEFT * 4.8 + UP * (y_base + baseline),
            RIGHT * 3.6 + UP * (y_base + baseline),
            color=SOFT, stroke_width=1.5,
            dash_length=0.15,
        )
        base_lbl = Text("baseline (≈ 0)", font=SANS, font_size=26, color=SOFT)
        base_lbl.next_to(base_line, RIGHT, buff=0.15)

        focus_bar = Rectangle(
            width=bar_w, height=focus_h,
            fill_color=TERRA, fill_opacity=0.50,
            stroke_color=TERRA, stroke_width=1,
        )
        focus_bar.move_to([-2.0, y_base + focus_h / 2, 0])
        focus_lbl = Text("focus", font=SANS, font_size=26, color=INK)
        focus_lbl.move_to([focus_bar.get_center()[0], y_base - 0.38, 0])

        ignore_bar = Rectangle(
            width=bar_w, height=ignore_h,
            fill_color=INK, fill_opacity=0.72,
            stroke_color=INK, stroke_width=1,
        )
        ignore_bar.move_to([2.0, y_base + ignore_h / 2, 0])
        ignore_lbl = Text("ignore", font=SANS, font_size=26, color=INK)
        ignore_lbl.move_to([ignore_bar.get_center()[0], y_base - 0.38, 0])

        # brace annotation on the ignore bar: "still active"
        brace_lbl = Text("still active", font=SERIF, font_size=28, color=INK)
        brace_lbl.next_to(ignore_bar, RIGHT, buff=0.25)
        brace_arrow = Arrow(
            brace_lbl.get_left() + LEFT * 0.1,
            ignore_bar.get_right(),
            color=INK, stroke_width=2, buff=0.05,
        )

        caption = Text(
            "Psychologists call it the white-bear effect. The machine has it too.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.9)
        skeptic = Text(
            "Suppression is partial — remember this in episode five.",
            font=SERIF, font_size=28, color=SOFT,
        )
        skeptic.next_to(caption, UP, buff=0.18)

        self.play(FadeIn(bear), run_time=0.5)
        self.play(
            Create(base_line), FadeIn(base_lbl),
            run_time=0.5,
        )
        self.play(
            GrowFromEdge(focus_bar, DOWN),
            FadeIn(focus_lbl),
            run_time=0.7,
        )
        self.play(
            GrowFromEdge(ignore_bar, DOWN),
            FadeIn(ignore_lbl),
            run_time=0.7,
        )
        self.play(FadeIn(brace_lbl), GrowArrow(brace_arrow), run_time=0.6)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.play(FadeIn(skeptic), run_time=0.4)
        self.wait(10.52)    # total ≈ 14.95s


# ── B06 · Two-hop Reasoning ───────────────────────────────────────────────────
# 7.64s  Hidden intermediate surfaces in workspace before output.
class B06_TwoHop(Scene):
    def construct(self):
        # Question box
        q_box = RoundedRectangle(
            corner_radius=0.15, width=8.2, height=1.1,
            fill_color=GROUND, fill_opacity=0.95,
            stroke_color=INK, stroke_width=2,
        )
        q_box.to_edge(UP, buff=0.95)
        q_txt = Text(
            '"The capital of the country where the Eiffel Tower stands is ___"',
            font=SERIF, font_size=28, color=INK,
        )
        q_txt.move_to(q_box)
        q_group = VGroup(q_box, q_txt)

        # Reasoning chain: Eiffel Tower → [France] → Paris
        # Three nodes in a row
        def node_card(txt, col, w=2.4, h=0.9):
            r = RoundedRectangle(corner_radius=0.14, width=w, height=h,
                                 fill_color=GROUND, fill_opacity=0.95,
                                 stroke_color=col, stroke_width=2.5)
            t = Text(txt, font=SERIF, font_size=28, color=col)
            t.move_to(r)
            return VGroup(r, t)

        n1 = node_card("Eiffel Tower", INK)
        n2 = node_card("France", INK, w=2.2, h=0.9)
        n3 = node_card("Paris", INK)
        chain = VGroup(n1, n2, n3)
        chain.arrange(RIGHT, buff=1.2)
        chain.move_to(DOWN * 0.5)

        arr1 = Arrow(n1.get_right() + RIGHT * 0.1, n2.get_left() + LEFT * 0.1,
                     color=INK, stroke_width=2.5, buff=0)
        arr2 = Arrow(n2.get_right() + RIGHT * 0.1, n3.get_left() + LEFT * 0.1,
                     color=INK, stroke_width=2.5, buff=0)

        # Layer labels under arrows
        mid_lbl = Text("midlayer", font=SANS, font_size=26, color=SOFT)
        mid_lbl.next_to(n2, DOWN, buff=0.25)
        out_lbl = Text("output", font=SANS, font_size=26, color=SOFT)
        out_lbl.next_to(n3, DOWN, buff=0.25)

        # "unspoken" annotation on France node
        unsaid = Text("unspoken", font=SANS, font_size=26, color=INK)
        unsaid.next_to(n2, UP, buff=0.22)

        self.play(FadeIn(q_group, shift=DOWN * 0.1), run_time=0.5)
        self.play(FadeIn(n1), run_time=0.4)
        self.play(GrowArrow(arr1), run_time=0.5)
        self.play(FadeIn(n2, shift=RIGHT * 0.1), FadeIn(unsaid), FadeIn(mid_lbl), run_time=0.6)
        self.play(GrowArrow(arr2), run_time=0.4)
        self.play(FadeIn(n3, shift=RIGHT * 0.1), FadeIn(out_lbl), run_time=0.4)
        self.wait(4.81)    # total ≈ 7.64s


# ── B07 · Arithmetic in Computation Order ────────────────────────────────────
# 13.50s  (4+17)*2+7: A+B=21 surfaces before ×2 product, in layer order.
class B07_ArithmeticOrder(Scene):
    def construct(self):
        # Expression at top
        expr = Text("(4 + 17) × 2 + 7", font=SERIF, font_size=48, color=INK)
        expr.to_edge(UP, buff=0.95)
        self.play(FadeIn(expr, shift=DOWN * 0.15), run_time=0.6)
        self.wait(0.3)

        # Layer timeline axis — horizontal
        axis_y = 0.4
        axis = Arrow(LEFT * 5.5 + UP * axis_y, RIGHT * 5.5 + UP * axis_y,
                     color=INK, stroke_width=2.5, buff=0)
        axis_lbl = Text("← earlier layers          later layers →", font=SANS, font_size=26, color=SOFT)
        axis_lbl.next_to(axis, UP, buff=0.22)

        self.play(Create(axis), FadeIn(axis_lbl), run_time=0.7)
        self.wait(0.2)

        # Three milestone markers with lollipop stems
        milestones = [
            (-3.6, "4+17 = 21", INK),
            (0.2,  "21 × 2 = 42", INK),
            (4.0,  "answer: 49", SOFT),
        ]
        for i, (x, label, col) in enumerate(milestones):
            stem = Line(
                [x, axis_y, 0], [x, axis_y - 1.6, 0],
                color=col, stroke_width=2.5,
            )
            dot = Dot(point=[x, axis_y - 0.05, 0], radius=0.12, color=col)
            lbl = Text(label, font=SERIF, font_size=28, color=col)
            lbl.move_to([x, axis_y - 2.15, 0])
            self.play(
                Create(stem),
                FadeIn(dot),
                FadeIn(lbl, shift=DOWN * 0.1),
                run_time=0.75,
            )
            if i < 2:
                self.wait(0.25)

        # order annotation
        order_note = Text(
            "computation order, not reading order",
            font=SERIF, font_size=28, color=INK,
        )
        order_note.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(order_note, shift=UP * 0.15), run_time=0.5)
        self.wait(7.73)    # total ≈ 13.50s


# ── B08 · Swap Tally Scoreboard ───────────────────────────────────────────────
# 17.92s  76/192 top-1 swaps, 101/192 at α=2. Counted up honestly.
class B08_SwapScore(Scene):
    def construct(self):
        # Header
        header = Text("Causal swap test — 16 templates × 12 pairs = 192 total",
                      font=SANS, font_size=26, color=SOFT)
        header.to_edge(UP, buff=0.9)
        self.play(FadeIn(header), run_time=0.5)
        self.wait(0.2)

        # Two scoreboard panels — explicit positions so stub sees distinct shapes
        def make_panel(label, col, w=4.4, h=3.2):
            outer = RoundedRectangle(corner_radius=0.18, width=w, height=h,
                                     fill_color=GROUND, fill_opacity=0.95,
                                     stroke_color=col, stroke_width=2.5)
            lbl = Text(label, font=SANS, font_size=26, color=INK)
            lbl.move_to([0.0, 1.18, 0])
            return outer, lbl

        p1_rect, p1_lbl = make_panel("α = 1  (natural strength)", TERRA)
        p2_rect, p2_lbl = make_panel("α = 2  (pushed harder)", INK)
        p1_group = VGroup(p1_rect, p1_lbl)
        p2_group = VGroup(p2_rect, p2_lbl)
        p1_group.move_to([-2.7, -0.3, 0])
        p2_group.move_to([2.7, -0.3, 0])

        self.play(FadeIn(p1_group, shift=UP * 0.15), FadeIn(p2_group, shift=UP * 0.15), run_time=0.7)
        self.wait(0.2)

        # Count displays — show intermediate and final numbers
        p1_count_0  = Text("0",   font=SERIF, font_size=72, color=INK)
        p1_count_mid = Text("38", font=SERIF, font_size=72, color=INK)
        p1_count_fin = Text("76", font=SERIF, font_size=72, color=INK)
        for t in [p1_count_0, p1_count_mid, p1_count_fin]:
            t.move_to([-2.7, -0.45, 0])

        p2_count_0   = Text("0",   font=SERIF, font_size=72, color=INK)
        p2_count_mid = Text("52",  font=SERIF, font_size=72, color=INK)
        p2_count_fin = Text("101", font=SERIF, font_size=72, color=INK)
        for t in [p2_count_0, p2_count_mid, p2_count_fin]:
            t.move_to([2.7, -0.45, 0])

        self.play(FadeIn(p1_count_0), FadeIn(p2_count_0), run_time=0.4)
        self.play(
            Transform(p1_count_0, p1_count_mid),
            Transform(p2_count_0, p2_count_mid),
            run_time=0.9,
        )
        self.play(
            Transform(p1_count_0, p1_count_fin),
            Transform(p2_count_0, p2_count_fin),
            run_time=0.9,
        )
        self.wait(0.3)

        # Progress bars (non-text shapes) — appear after count settles → second shape state
        bar_w = 3.0
        p1_fill_w = bar_w * 76 / 192          # ≈ 1.19
        p2_fill_w = bar_w * 101 / 192         # ≈ 1.58

        p1_bar_bg = Rectangle(width=bar_w, height=0.25,
                              fill_color=SOFT, fill_opacity=0.20,
                              stroke_color=SOFT, stroke_width=1.0)
        p1_bar_bg.move_to([-2.7, -1.15, 0])
        p1_bar_fill = Rectangle(width=p1_fill_w, height=0.25,
                                fill_color=TERRA, fill_opacity=0.82, stroke_width=0)
        p1_bar_fill.move_to([-2.7 - (bar_w - p1_fill_w) / 2, -1.15, 0])

        p2_bar_bg = Rectangle(width=bar_w, height=0.25,
                              fill_color=SOFT, fill_opacity=0.20,
                              stroke_color=SOFT, stroke_width=1.0)
        p2_bar_bg.move_to([2.7, -1.15, 0])
        p2_bar_fill = Rectangle(width=p2_fill_w, height=0.25,
                                fill_color=INK, fill_opacity=0.82, stroke_width=0)
        p2_bar_fill.move_to([2.7 - (bar_w - p2_fill_w) / 2, -1.15, 0])

        self.play(
            FadeIn(p1_bar_bg), FadeIn(p1_bar_fill),
            FadeIn(p2_bar_bg), FadeIn(p2_bar_fill),
            run_time=0.6,
        )

        # Fraction labels below bars
        frac1 = Text("76 / 192", font=SANS, font_size=26, color=INK)
        frac1.move_to([-2.7, -1.52, 0])
        frac2 = Text("101 / 192", font=SANS, font_size=26, color=INK)
        frac2.move_to([2.7, -1.52, 0])
        self.play(FadeIn(frac1), FadeIn(frac2), run_time=0.4)
        self.wait(0.3)

        _sk1 = Text("A 40–53% hit rate proves the mechanism exists",
                    font=SERIF, font_size=28, color=SOFT)
        _sk2 = Text("— not that it's the whole mechanism.",
                    font=SERIF, font_size=28, color=SOFT)
        skeptic = VGroup(_sk1, _sk2).arrange(DOWN, center=True, buff=0.08)
        skeptic.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(skeptic), run_time=0.5)
        self.wait(11.32)    # total ≈ 17.92s


# ── B09 · Probe Split: J-space vs Complement ─────────────────────────────────
# 11.86s  Intermediate probe split into J-space component (causal) and complement.
class B09_ProbeSplit(Scene):
    def construct(self):
        # Central probe — explicit position so layout is deterministic
        probe_box = RoundedRectangle(corner_radius=0.14, width=3.4, height=0.9,
                                     fill_color=GROUND, fill_opacity=0.95,
                                     stroke_color=INK, stroke_width=2)
        probe_lbl = Text("intermediate probe", font=SANS, font_size=26, color=INK)
        probe_lbl.move_to(probe_box)
        probe_group = VGroup(probe_box, probe_lbl)
        probe_group.move_to([0, 2.4, 0])

        # Arrows with explicit start/end — avoids get_bottom() + numpy-chain positioning
        jspace_arrow = Arrow([-0.4, 1.95, 0], [-2.8, 0.5, 0],
                             color=TERRA, stroke_width=4.5, buff=0)
        compl_arrow  = Arrow([0.4, 1.95, 0], [2.8, 0.5, 0],
                             color=SOFT,  stroke_width=2.5, buff=0)

        # Component labels — explicit coordinates, clear of arrowheads
        jspace_lbl = Text("J-space component", font=SANS, font_size=26, color=INK)
        jspace_lbl.move_to([-2.8, -0.15, 0])
        compl_lbl = Text("complement", font=SANS, font_size=26, color=SOFT)
        compl_lbl.move_to([2.8, -0.15, 0])

        # Causal effect bars — explicit positions, all within safe area
        jspace_bar_rect = Rectangle(width=1.8, height=1.6,
                                    fill_color=TERRA, fill_opacity=0.82,
                                    stroke_color=TERRA, stroke_width=1)
        jspace_bar_rect.move_to([-2.8, -1.2, 0])   # bottom at y=-2.0

        compl_bar_rect = Rectangle(width=1.8, height=0.4,
                                   fill_color=SOFT, fill_opacity=0.82,
                                   stroke_color=SOFT, stroke_width=1)
        compl_bar_rect.move_to([2.8, -0.65, 0])    # bottom at y=-0.85

        jspace_eff_lbl = Text("causal effect: large", font=SANS, font_size=26, color=INK)
        jspace_eff_lbl.move_to([-2.8, -2.22, 0])

        compl_eff_lbl = Text("causal effect: small", font=SANS, font_size=26, color=SOFT)
        compl_eff_lbl.move_to([2.8, -1.07, 0])

        _cap1 = Text("The workspace isn't just where thoughts are visible",
                     font=SERIF, font_size=28, color=INK)
        _cap2 = Text("— it's where they do their work.",
                     font=SERIF, font_size=28, color=INK)
        caption = VGroup(_cap1, _cap2).arrange(DOWN, center=True, buff=0.08)
        caption.to_edge(DOWN, buff=0.9)

        self.play(FadeIn(probe_group, shift=DOWN * 0.15), run_time=0.5)
        self.play(GrowArrow(jspace_arrow), GrowArrow(compl_arrow), run_time=0.8)
        self.play(FadeIn(jspace_lbl), FadeIn(compl_lbl), run_time=0.5)
        self.play(
            GrowFromEdge(jspace_bar_rect, DOWN),
            GrowFromEdge(compl_bar_rect, DOWN),
            FadeIn(jspace_eff_lbl),
            FadeIn(compl_eff_lbl),
            run_time=0.9,
        )
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(8.61)    # total ≈ 11.86s


# ── B10 · Generalization: One Swap, All Templates ────────────────────────────
# 12.29s  France→Germany planted once; 8 downstream templates all redirected.
class B10_Generalization(Scene):
    def construct(self):
        # Hub — the swapped intermediate
        hub_lbl = Text("France  →  Germany", font=SERIF, font_size=32, color=INK)
        # The subtitle lives INSIDE the card. Below it (its old home) is the
        # spoke field — it landed on the lines and on "currency: Euro (same)".
        hub_sub = Text("one  swap, planted once", font=SANS, font_size=24, color=SOFT)
        hub_inner = VGroup(hub_lbl, hub_sub).arrange(DOWN, buff=0.12)
        # Card sized FROM its contents — a fixed width clipped the subtitle.
        hub_rect = RoundedRectangle(corner_radius=0.18,
                                    width=hub_inner.width + 0.55,
                                    height=hub_inner.height + 0.45,
                                    fill_color=GROUND, fill_opacity=0.95,
                                    stroke_color=TERRA, stroke_width=3)
        hub_inner.move_to(hub_rect)
        hub = VGroup(hub_rect, hub_inner)
        hub.move_to([0, 0.5, 0])      # raised so bottom spokes clear caption
        hub_hw = hub_rect.width / 2
        hub_hh = hub_rect.height / 2

        # 8 spoke targets — 22.5° offset so no spoke sits at top/bottom dead-centre
        spoke_labels = [
            "capital: Berlin",
            "language: German",
            "anthem: changed",
            "cuisine: changed",
            "currency: Euro (same)",
            "population: 84M",
            "continent: Europe",
            "flag: changed",
        ]
        # Elliptical, not circular: horizontal room is what the long labels
        # need, vertical room is what the ±3.4 safe area limits.
        rx, ry = 3.3, 2.7
        SAFE_X = 6.2
        hub_offset = np.array([0.0, 0.5, 0.0])
        angles = [i * 45 + 22.5 for i in range(8)]
        spokes = VGroup()
        lines_g = VGroup()
        for label, deg in zip(spoke_labels, angles):
            theta = np.radians(deg)
            unit = np.array([np.cos(theta), np.sin(theta), 0])
            pos  = hub_offset + np.array([rx * np.cos(theta), ry * np.sin(theta), 0])

            # Start the line where the ray leaves the CARD (box intersection),
            # not at a fixed radius — a fixed radius either started inside the
            # card or left a stub once the card grew.
            t_box = min(hub_hw / max(abs(np.cos(theta)), 1e-6),
                        hub_hh / max(abs(np.sin(theta)), 1e-6))
            ln = Line(hub_offset + (t_box + 0.14) * unit,
                      pos - 0.30 * unit,
                      color=INK, stroke_width=1.6)
            lines_g.add(ln)

            # small label (no card — just text to keep it uncluttered)
            # Anchor the label's INNER edge at the spoke tip so it grows away
            # from the hub. Centred placement put the two near-vertical pairs
            # (language/anthem at top, population/continent at bottom) on top
            # of each other — both sit ~1.1 units either side of centre.
            txt = Text(label, font=SERIF, font_size=27, color=INK)
            cos_t = np.cos(theta)
            txt.move_to(pos + np.array([np.sign(cos_t) * (txt.width / 2 + 0.10), 0, 0]))
            if txt.get_right()[0] > SAFE_X:
                txt.shift(LEFT * (txt.get_right()[0] - SAFE_X))
            if txt.get_left()[0] < -SAFE_X:
                txt.shift(RIGHT * (-SAFE_X - txt.get_left()[0]))
            spokes.add(txt)

        self.play(FadeIn(hub, shift=UP * 0.1), run_time=0.5)
        self.wait(0.3)    # hub_sub now rides inside the card (was its own beat)
        self.play(
            LaggedStart(*[Create(l) for l in lines_g], lag_ratio=0.1),
            run_time=0.9,
        )
        self.play(
            LaggedStart(*[FadeIn(s, shift=UP * 0.05) for s in spokes], lag_ratio=0.1),
            run_time=1.2,
        )

        caption = Text(
            "Write once — every specialist reads it.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(caption, shift=UP * 0.15), run_time=0.5)
        self.wait(8.89)    # total ≈ 12.29s


# ── B11 · Ablation Battery ────────────────────────────────────────────────────
# 8.55s  Delete the workspace — project out top lens directions — watch which die.
class B11_AblationBattery(Scene):
    def construct(self):
        title = Text("Ablation test — delete the J-space", font=SANS, font_size=26, color=INK)
        title.to_edge(UP, buff=0.9)
        self.play(FadeIn(title), run_time=0.5)

        # Three task bars, before and after
        tasks = [
            ("multi-hop reasoning",  1.0, 0.18, TERRA),
            ("ciphers",              1.0, 0.22, INK),
            ("fluent grammar",       1.0, 0.88, SOFT),
        ]
        bar_w = 2.4
        gap   = 0.8
        scale = 3.0
        x0    = -3.6
        y_base = -2.5

        # axis
        axis = Line([x0 - 0.3, y_base, 0], [x0 - 0.3, y_base + scale + 0.4, 0],
                    color=INK, stroke_width=2)
        axis_lbl = Text("performance", font=SANS, font_size=14, color=SOFT)
        axis_lbl.rotate(PI / 2)
        axis_lbl.next_to(axis, LEFT, buff=0.18)
        self.play(Create(axis), FadeIn(axis_lbl), run_time=0.3)

        before_bars = VGroup()
        after_bars  = VGroup()
        task_lbls   = VGroup()

        for i, (task, before, after, col) in enumerate(tasks):
            bx = x0 + i * (bar_w + gap)
            bh = before * scale
            ah = after  * scale

            bb = Rectangle(width=bar_w, height=bh,
                           fill_color=col, fill_opacity=0.70,
                           stroke_color=col, stroke_width=1)
            bb.move_to([bx, y_base + bh / 2, 0])
            before_bars.add(bb)

            ab = Rectangle(width=bar_w, height=ah,
                           fill_color=col, fill_opacity=0.88,
                           stroke_color=col, stroke_width=1.5)
            ab.move_to([bx, y_base + ah / 2, 0])
            after_bars.add(ab)

            lbl = Text(task, font=SANS, font_size=14, color=INK)
            lbl.move_to([bx, y_base - 0.32, 0])
            task_lbls.add(lbl)

        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in before_bars], lag_ratio=0.2),
            FadeIn(task_lbls),
            run_time=1.0,
        )

        before_lbl = Text("before ablation", font=SANS, font_size=16, color=SOFT)
        before_lbl.to_edge(RIGHT, buff=0.95).shift(UP * 2.0)
        self.play(FadeIn(before_lbl), run_time=0.3)
        self.wait(0.2)

        # Transform to after-ablation bars
        self.play(
            *[Transform(before_bars[i], after_bars[i]) for i in range(len(tasks))],
            run_time=1.0,
        )
        after_lbl = Text("after ablation", font=SANS, font_size=16, color=INK)
        after_lbl.next_to(before_lbl, DOWN, buff=0.18)
        self.play(FadeIn(after_lbl), run_time=0.3)
        self.wait(4.92)    # total ≈ 8.55s


# ── B12 · Selective Collapse ──────────────────────────────────────────────────
# 17.34s  Flexible cognition collapses; automatic cognition survives ablation.
class B12_SelectiveCollapse(Scene):
    def construct(self):
        # Two column headers
        flex_hdr = Text("FLEXIBLE", font=SANS, font_size=26, color=INK)
        auto_hdr = Text("AUTOMATIC", font=SANS, font_size=26, color=INK)
        flex_hdr.move_to(LEFT * 3.2 + UP * 3.0)
        auto_hdr.move_to(RIGHT * 3.2 + UP * 3.0)

        divider = Line(UP * 3.5, DOWN * 2.5, color=INK, stroke_width=1.5)
        self.play(
            FadeIn(flex_hdr), FadeIn(auto_hdr),
            Create(divider),
            run_time=0.7,
        )
        self.wait(0.2)

        # Flexible tasks
        flex_tasks = [
            ("multi-hop reasoning",   0.19),
            ("ciphers",               0.23),
            ("constrained writing",   0.28),
        ]
        # Automatic tasks
        auto_tasks = [
            ("fluent text generation", 0.91),
            ("simple recall",          0.88),
            ("basic grammar",          0.94),
        ]

        bar_w = 2.6
        scale = 2.6
        y0    = 1.8
        gap   = 0.9
        x_flex = -3.2
        x_auto =  3.2

        def make_col_bars(tasks, xc, col):
            group = VGroup()
            for i, (task, val) in enumerate(tasks):
                y = y0 - i * gap
                h = max(val * scale, 0.08)
                bar = Rectangle(width=bar_w, height=h,
                                fill_color=col, fill_opacity=0.80,
                                stroke_color=col, stroke_width=1)
                bar.move_to([xc, y - h / 2, 0])  # top-aligned
                bar.align_to([xc, y, 0], UP)
                lbl = Text(task, font=SERIF, font_size=12, color=INK)
                lbl.next_to(bar, LEFT if xc < 0 else RIGHT, buff=0.18)
                val_txt = Text(f"{int(val*100)}%", font=SANS, font_size=15, color=INK)
                val_txt.next_to(bar, RIGHT if xc < 0 else LEFT, buff=0.12)
                group.add(VGroup(bar, lbl, val_txt))
            return group

        flex_bars = make_col_bars(flex_tasks, x_flex, TERRA)
        auto_bars = make_col_bars(auto_tasks, x_auto, INK)

        self.play(
            LaggedStart(*[GrowFromEdge(b[0], UP) for b in flex_bars], lag_ratio=0.2),
            LaggedStart(*[FadeIn(VGroup(b[1], b[2])) for b in flex_bars], lag_ratio=0.2),
            run_time=1.4,
        )
        self.play(
            LaggedStart(*[GrowFromEdge(b[0], UP) for b in auto_bars], lag_ratio=0.2),
            LaggedStart(*[FadeIn(VGroup(b[1], b[2])) for b in auto_bars], lag_ratio=0.2),
            run_time=1.4,
        )
        self.wait(0.5)

        # Annotation: workspace signature
        sig_lbl = Text(
            "The workspace signature — conscious vs autopilot",
            font=SERIF, font_size=22, color=INK,
        )
        # SERIF 22 passes §8.1 at 4K: text has both ascenders and descenders (autopilot→p,g)
        # giving a full blob height ≥48px > 41px floor. Raising to 28 crosses the B12 divider.
        sig_lbl.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(sig_lbl, shift=UP * 0.1), run_time=0.5)
        self.wait(12.63)    # total ≈ 17.34s


# ── B13 · Co-Occupancy ────────────────────────────────────────────────────────
# 15.19s  Two held concepts: 0.46 vs 0.53. Concept + computed answer: 0.09 vs 0.29.
class B13_CoOccupancy(Scene):
    def construct(self):
        title = Text("Within the workspace — co-occupancy rates", font=SANS, font_size=26, color=INK)
        title.to_edge(UP, buff=0.9)
        self.play(FadeIn(title), run_time=0.5)

        # Two paired bar groups
        groups = [
            {
                "label": "Two concepts held",
                "measured": 0.46,
                "baseline": 0.53,
                "note": "near  chance",
                "x": -2.8,
            },
            {
                "label": "Concept + computed answer",
                "measured": 0.09,
                "baseline": 0.29,
                "note": "well  below chance",
                "x":  2.8,
            },
        ]

        bar_w  = 1.0
        gap    = 0.25
        scale  = 5.5
        # Raised from -2.3: the x-labels (y_base-0.38) and notes (y_base-0.72)
        # landed at -2.68/-3.02, and the bottom-edge legend sits at ~-3.1 —
        # the notes and the legend were drawn on top of each other.
        y_base = -1.6

        # axis
        # Axis height is capped, not scale+0.4: with the raised y_base that
        # ran to y=4.3 and bled off the top of frame (GATE V blocker).
        # 0.62*scale clears the tallest bar (0.53) and the chance line (0.5).
        ax_top = y_base + 0.62 * scale
        ax = Line(LEFT * 5.5 + UP * y_base, LEFT * 5.5 + UP * ax_top,
                  color=INK, stroke_width=2)
        ax_lbl = Text("co-occupancy rate", font=SANS, font_size=25, color=SOFT)
        ax_lbl.rotate(PI / 2)
        ax_lbl.next_to(ax, LEFT, buff=0.18)
        self.play(Create(ax), FadeIn(ax_lbl), run_time=0.4)

        # tick at 0.5 (chance)
        chance_y = y_base + 0.5 * scale
        chance_line = DashedLine(LEFT * 5.3 + UP * chance_y, RIGHT * 5.4 + UP * chance_y,
                                 color=SOFT, stroke_width=1.2, dash_length=0.18)
        chance_lbl = Text("chance (0.5)", font=SANS, font_size=26, color=SOFT)
        chance_lbl.move_to([4.7, chance_y + 0.25, 0])
        self.play(Create(chance_line), FadeIn(chance_lbl), run_time=0.4)

        for g in groups:
            xc = g["x"]
            m_h = g["measured"] * scale
            b_h = g["baseline"] * scale

            m_bar = Rectangle(width=bar_w, height=m_h,
                              fill_color=TERRA, fill_opacity=0.82,
                              stroke_color=TERRA, stroke_width=1)
            b_bar = Rectangle(width=bar_w, height=b_h,
                              fill_color=SOFT, fill_opacity=0.55,
                              stroke_color=SOFT, stroke_width=1)
            m_bar.move_to([xc - (bar_w + gap) / 2, y_base + m_h / 2, 0])
            b_bar.move_to([xc + (bar_w + gap) / 2, y_base + b_h / 2, 0])

            g_lbl = Text(g["label"], font=SANS, font_size=27, color=INK)
            g_lbl.move_to([xc, y_base - 0.42, 0])
            note = Text(g["note"], font=SERIF, font_size=28, color=SOFT)
            note.move_to([xc, y_base - 0.86, 0])

            m_val = Text(str(g["measured"]), font=SANS, font_size=26, color=INK)
            m_val.next_to(m_bar, UP, buff=0.12)
            b_val = Text(str(g["baseline"]), font=SANS, font_size=26, color=SOFT)
            b_val.next_to(b_bar, UP, buff=0.12)
            # 0.46 tops out ~0.05 below the chance line and 0.53 just above it,
            # so a bare number gets struck through by the dashes. Occlude.
            m_val = VGroup(BackgroundRectangle(m_val, color=GROUND,
                                               fill_opacity=1, buff=0.07), m_val)
            b_val = VGroup(BackgroundRectangle(b_val, color=GROUND,
                                               fill_opacity=1, buff=0.07), b_val)
            m_val._qc_intentional = True
            b_val._qc_intentional = True

            self.play(
                GrowFromEdge(m_bar, DOWN),
                GrowFromEdge(b_bar, DOWN),
                FadeIn(m_val), FadeIn(b_val),
                FadeIn(g_lbl), FadeIn(note),
                run_time=0.9,
            )
            self.wait(0.25)

        # legend
        legend = VGroup(
            VGroup(
                Square(side_length=0.28, fill_color=TERRA, fill_opacity=0.82, stroke_width=0),
                Text("measured", font=SANS, font_size=26, color=INK),
            ).arrange(RIGHT, buff=0.12),
            VGroup(
                Square(side_length=0.28, fill_color=SOFT, fill_opacity=0.55, stroke_width=0),
                Text("baseline/control", font=SANS, font_size=26, color=INK),
            ).arrange(RIGHT, buff=0.12),
        )
        legend.arrange(RIGHT, buff=0.5)
        # Legend sits under the TITLE, above the tallest bar (0.53 → y≈1.32).
        # At the bottom edge it collided with the per-group notes, and the
        # caption hung off it straight onto the bars.
        legend.move_to([0.0, 2.15, 0])
        self.play(FadeIn(legend), run_time=0.4)

        caption = Text(
            "Computation elbows storage aside.",
            font=SERIF, font_size=28, color=INK,
        )
        caption.to_edge(DOWN, buff=0.85)
        self.play(FadeIn(caption, shift=UP * 0.1), run_time=0.5)
        self.wait(10.53)    # total ≈ 15.19s


# ── BearsDoodlesVideo ─────────────────────────────────────────────────────────
# Static-check entry point: runs all per-beat scenes sequentially.
class BearsDoodlesVideo(Scene):
    def construct(self):
        for cls in [
            B02_FiveProperties,
            B03_InjectReport,
            B04_FocusIgnore,
            B05_WhiteBear,
            B06_TwoHop,
            B07_ArithmeticOrder,
            B08_SwapScore,
            B09_ProbeSplit,
            B10_Generalization,
            B11_AblationBattery,
            B12_SelectiveCollapse,
            B13_CoOccupancy,
        ]:
            cls().construct()
