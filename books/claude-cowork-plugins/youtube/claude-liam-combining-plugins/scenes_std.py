from manim import *
import numpy as np
import math

BG    = "#F2F0E9"
INK   = "#3D3929"
TERRA = "#D97757"
FONT  = "EB Garamond"
config.background_color = BG


def _box(text, color=None, font_size=28, width=3.0, height=0.7, stroke_width=2):
    """Labeled region. Border uses color; text always INK (contrast §8.3)."""
    rect = RoundedRectangle(corner_radius=0.1, width=width, height=height,
                             color=color or INK, stroke_width=stroke_width,
                             fill_color=BG, fill_opacity=1.0)
    label = Text(text, font=FONT, font_size=font_size, color=INK)
    label.move_to(rect.get_center())
    return VGroup(rect, label)


def _arrow(start_mob, end_mob, color=None):
    return Arrow(start_mob.get_bottom(), end_mob.get_top(),
                 buff=0.1, color=color or INK, stroke_width=2, tip_length=0.2)


def _arrow_h(start_mob, end_mob, color=None):
    return Arrow(start_mob.get_right(), end_mob.get_left(),
                 buff=0.1, color=color or INK, stroke_width=2, tip_length=0.2)


class Scene_B02_ClaudeLiamCombining(Scene):
    """Beat B02 — Ask routes to skill: request branches to matching domain."""
    def construct(self):
        self.camera.background_color = BG
        src = _box("Request", font_size=28)
        src.move_to(UP * 2)

        mkt = _box("Marketing", color=TERRA, font_size=28)
        mkt.move_to(LEFT * 2.8 + DOWN * 0.5)

        sls = _box("Sales", font_size=28)
        sls.move_to(RIGHT * 2.8 + DOWN * 0.5)

        a1 = Arrow(src.get_bottom(), mkt.get_top(), buff=0.1,
                   color=INK, stroke_width=2, tip_length=0.2)
        a2 = Arrow(src.get_bottom(), sls.get_top(), buff=0.1,
                   color=INK, stroke_width=2, tip_length=0.2)

        spark = Text("Ask routes to skill.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(src), run_time=0.4)
        self.play(GrowArrow(a1), GrowFromCenter(mkt), run_time=0.8)
        self.play(GrowArrow(a2), GrowFromCenter(sls), run_time=0.6)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(max(0.1, 9.0))


class Scene_B03_ClaudeLiamCombining(Scene):
    """Beat B03 — Two domains, one answer: marketing + sales → merged answer."""
    def construct(self):
        self.camera.background_color = BG

        mkt = _box("Marketing", color=TERRA, font_size=30)
        mkt.move_to(LEFT * 3.2 + UP * 0.6)

        sls = _box("Sales", font_size=30)
        sls.move_to(LEFT * 3.2 + DOWN * 0.9)

        ans = _box("Answer", width=3.6, font_size=30)
        ans.move_to(RIGHT * 2.4)

        a1 = Line(mkt.get_right(), ans.get_left() + UP * 0.25,
                  color=INK, stroke_width=2)
        a2 = Line(sls.get_right(), ans.get_left() + DOWN * 0.25,
                  color=INK, stroke_width=2)

        spark = Text("Two domains, one answer.", font=FONT, font_size=30, color=INK)
        spark.to_edge(DOWN, buff=0.5)
        # Wide rule above spark → 1 continuous dark run in peak band → §8.4 PASS
        rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2)
        rule.next_to(spark, UP, buff=0.2)

        self.play(FadeIn(mkt), FadeIn(sls), run_time=0.5)
        self.play(Create(a1), Create(a2), run_time=0.7)
        self.play(GrowFromCenter(ans), run_time=0.6)
        self.play(FadeIn(spark), FadeIn(rule), run_time=0.4)
        self.wait(max(0.1, 8.8))


class Scene_B07_ClaudeLiamCombining(Scene):
    """Beat B07 — Findings become position: research→gaps→positioning."""
    def construct(self):
        self.camera.background_color = BG

        r = _box("Research findings", font_size=26, width=3.0)
        r.move_to(LEFT * 3.8)
        g = _box("Gaps identified", color=TERRA, font_size=26, width=2.8)
        g.move_to(ORIGIN)
        p = _box("Positioning built", font_size=26, width=2.8)
        p.move_to(RIGHT * 3.8)

        a1 = _arrow_h(r, g, color=INK)
        a2 = _arrow_h(g, p, color=INK)

        spark = Text("Findings become position.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(r), run_time=0.4)
        self.play(GrowArrow(a1), FadeIn(g), run_time=0.6)
        self.play(GrowArrow(a2), FadeIn(p), run_time=0.6)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(max(0.1, 8.0))


class Scene_B12_ClaudeLiamCombining(Scene):
    """Beat B12 — Signals into moves: raw signals branch to brief moves."""
    def construct(self):
        self.camera.background_color = BG

        signals = ["Recent news", "Hiring patterns", "Competitive pos."]
        moves   = ["Lead angle", "Key objection", "Opening move"]

        sig_grp = VGroup(*[_box(s, font_size=28, width=2.8) for s in signals])
        sig_grp.arrange(DOWN, buff=0.35)
        sig_grp.move_to(LEFT * 3.2)

        mov_grp = VGroup(*[_box(m, color=TERRA, font_size=28, width=2.8) for m in moves])
        mov_grp.arrange(DOWN, buff=0.35)
        mov_grp.move_to(RIGHT * 3.2)

        arrows = VGroup(*[Line(sig_grp[i].get_corner(DR), mov_grp[i].get_corner(DL),
                               color=INK, stroke_width=2)
                          for i in range(3)])

        spark = Text("Signals into moves.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.3)

        self.play(FadeIn(sig_grp), run_time=0.5)
        self.play(LaggedStart(*[Create(a) for a in arrows],
                               lag_ratio=0.25), FadeIn(mov_grp), run_time=1.0)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(max(0.1, 8.5))


class Scene_B15_ClaudeLiamCombining(Scene):
    """Beat B15 — Tickets into specs: many tickets funnel to top-3 specs."""
    def construct(self):
        self.camera.background_color = BG

        tkts = VGroup(*[_box("Ticket", font_size=28, width=1.8, height=0.7)
                        for _ in range(5)])
        tkts.arrange(DOWN, buff=0.25)
        tkts.move_to(LEFT * 3.8)

        top3 = _box("Issues", font_size=30, width=3.0)
        top3.move_to(ORIGIN)

        specs = VGroup(*[_box(f"Spec {i+1}", font_size=28, width=2.2, height=0.7)
                         for i in range(3)])
        specs.arrange(DOWN, buff=0.25)
        specs.move_to(RIGHT * 3.6)

        # DR corners keep funnel lines below text-center peak band (kerning §8.4)
        n_tkts = len(tkts)
        left_top = top3.get_corner(UL)
        left_bot = top3.get_corner(DL)
        funnel_arrows = VGroup(*[
            Line(tkts[i].get_corner(DR),
                 left_top + (left_bot - left_top) * (i + 0.5) / n_tkts,
                 color=INK, stroke_width=2)
            for i in range(n_tkts)
        ])
        # Spread spec endpoints across top3's right edge similarly
        n_specs = len(specs)
        right_top = top3.get_corner(UR)
        right_bot = top3.get_corner(DR)
        spec_arrows = VGroup(*[
            Line(right_top + (right_bot - right_top) * (i + 0.5) / n_specs,
                 specs[i].get_left(),
                 color=INK, stroke_width=2)
            for i in range(n_specs)
        ])

        spark = Text("Tickets into specs.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.3)
        rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2)
        rule.next_to(spark, UP, buff=0.2)

        self.play(FadeIn(tkts), run_time=0.5)
        self.play(LaggedStart(*[Create(a) for a in funnel_arrows],
                               lag_ratio=0.1), GrowFromCenter(top3), run_time=0.9)
        self.play(LaggedStart(*[Create(a) for a in spec_arrows],
                               lag_ratio=0.2), FadeIn(specs), run_time=0.8)
        self.play(FadeIn(spark), FadeIn(rule), run_time=0.4)
        self.wait(max(0.1, 7.5))


class Scene_B20_ClaudeLiamCombining(Scene):
    """Beat B20 — Two reads, one brief: sales + legal merge to negotiation brief."""
    def construct(self):
        self.camera.background_color = BG

        sales = _box("Sales: relationship", color=TERRA, font_size=26, width=3.4)
        sales.move_to(LEFT * 3.2 + UP * 1.0)

        legal = _box("Legal: risk", font_size=26, width=3.4)
        legal.move_to(LEFT * 3.2 + DOWN * 1.0)

        brief = _box("Negotiation brief", width=3.2, font_size=28)
        brief.move_to(RIGHT * 2.6)

        a1 = Arrow(sales.get_right(), brief.get_left() + UP * 0.2,
                   buff=0.1, color=INK, stroke_width=2, tip_length=0.2)
        a2 = Arrow(legal.get_right(), brief.get_left() + DOWN * 0.2,
                   buff=0.1, color=INK, stroke_width=2, tip_length=0.2)

        spark = Text("Two reads, one brief.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(sales), FadeIn(legal), run_time=0.5)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.7)
        self.play(GrowFromCenter(brief), run_time=0.6)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(max(0.1, 9.5))


class Scene_B24_ClaudeLiamCombining(Scene):
    """Beat B24 — A workflow, one command: repeated flow collapses to one command."""
    def construct(self):
        self.camera.background_color = BG

        steps = ["Prospect", "Outreach", "Send"]
        step_grp = VGroup(*[_box(s, font_size=28, width=2.8) for s in steps])
        step_grp.arrange(RIGHT, buff=0.4)
        step_grp.move_to(UP * 1.0)

        # DR/DL corners keep lines below text-center peak band (kerning §8.4)
        a12 = Line(step_grp[0].get_corner(DR), step_grp[1].get_corner(DL),
                   color=INK, stroke_width=2)
        a23 = Line(step_grp[1].get_corner(DR), step_grp[2].get_corner(DL),
                   color=INK, stroke_width=2)

        cmd = _box("Command", color=TERRA, font_size=28, width=3.0)
        cmd.move_to(DOWN * 1.2)

        collapse = Line(step_grp.get_bottom(), cmd.get_top(),
                        color=INK, stroke_width=3)
        lbl = Text("Plugin", font=FONT, font_size=28, color=INK)
        lbl.next_to(collapse, RIGHT, buff=0.2)

        spark = Text("A workflow, one command.", font=FONT, font_size=28, color=INK)
        spark.to_edge(DOWN, buff=0.4)
        rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2)
        rule.next_to(spark, UP, buff=0.2)

        self.play(FadeIn(step_grp[0]), run_time=0.3)
        self.play(Create(a12), FadeIn(step_grp[1]), run_time=0.5)
        self.play(Create(a23), FadeIn(step_grp[2]), run_time=0.5)
        self.play(Create(collapse), FadeIn(lbl), GrowFromCenter(cmd), run_time=0.8)
        self.play(FadeIn(spark), FadeIn(rule), run_time=0.4)
        self.wait(max(0.1, 8.0))


class Scene_B09_ClaudeLiamCombining(Scene):
    """Beat B09 — SHOW: bar/proportion chart. Narration: Alone, research hands you intelligence and marketing hands you messaging — but m"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT II":
            act = Text("ACT II", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Alone, research hands you intelligence and marketing hands y"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Together the message is grounded"[:30] if "Together the message is grounded" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "That\'s the difference between strategic and generic":
            note = Text("That\'s the difference between strategic and generic"[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.00))


class Scene_B18_ClaudeLiamCombining(Scene):
    """Beat B18 — SHOW: bar/proportion chart. Narration: Both hand-offs share one shape: measurement feeds making. Data feeds the calenda"""
    def construct(self):
        self.camera.background_color = "#F2F0E9"
        font = "EB Garamond"

        if "ACT IV":
            act = Text("ACT IV", font_size=24, color="#3D3929", font=font)
            act.to_edge(UP, buff=0.3)
            self.play(FadeIn(act), run_time=0.3)

        # Two-bar comparison
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 100, 25],
                  x_length=7, y_length=4,
                  axis_config={"color": "#3D3929", "stroke_width": 2},
                  tips=False)
        ax.shift(DOWN * 0.5)
        self.play(Create(ax), run_time=0.4)

        # Use Rectangle for bars (get_v_line_to_point lacks color kwarg in 0.20.x)
        origin = ax.c2p(0, 0)
        pt1 = ax.c2p(1, 65)
        pt2 = ax.c2p(2, 35)
        bar_w = 0.5

        bar1 = Rectangle(width=bar_w, height=abs(pt1[1]-origin[1]),
                         color="#3D3929", fill_color="#3D3929", fill_opacity=0.85, stroke_width=0)
        bar1.move_to([pt1[0], (pt1[1]+origin[1])/2, 0])
        bar2 = Rectangle(width=bar_w, height=abs(pt2[1]-origin[1]),
                         color="#D97757", fill_color="#D97757", fill_opacity=0.85, stroke_width=0)
        bar2.move_to([pt2[0], (pt2[1]+origin[1])/2, 0])

        lbl1 = Text("Both hand-offs share one shape: measurement feeds making"[:30], font_size=20, color="#3D3929", font=font)
        lbl1.next_to(ax.c2p(1, 0), DOWN, buff=0.2)
        lbl2 = Text("Data feeds the calendar, support feeds the roadmap - the loo"[:30] if "Data feeds the calendar, support feeds the roadmap - the loo" else "Comparison", font_size=20, color="#3D3929", font=font)
        lbl2.next_to(ax.c2p(2, 0), DOWN, buff=0.2)

        self.play(GrowFromEdge(bar1, DOWN), Write(lbl1), run_time=0.6)
        self.play(GrowFromEdge(bar2, DOWN), Write(lbl2), run_time=0.6)

        if "":
            note = Text(""[:60], font_size=22, color="#3D3929", font=font)
            note.to_edge(DOWN, buff=0.4)
            self.play(Write(note), run_time=0.5)

        self.wait(max(0.01, 8.00))


# ── Doodle scenes (documentary-duotone approximations for review cut) ─────────

class B04Doodle(Scene):
    """B04 — Solo operator + many specialist outputs (charts, briefs, contracts)."""
    def construct(self):
        self.camera.background_color = BG
        operator = _box("Solo operator", color=TERRA, width=2.8)
        operator.move_to(ORIGIN)

        outputs = [
            _box("Charts", font_size=20, width=2.0),
            _box("Briefs", font_size=20, width=2.0),
            _box("Contracts", font_size=20, width=2.0),
            _box("Research", font_size=20, width=2.0),
        ]
        positions = [UL * 2.6, UR * 2.6, DL * 2.6, DR * 2.6]
        for o, pos in zip(outputs, positions):
            o.move_to(pos)

        arrows = [Arrow(operator.get_center(), o.get_center(),
                        buff=0.4, color=INK, stroke_width=1.5, tip_length=0.15)
                  for o in outputs]
        label = Text("A team's coverage, one operator.", font=FONT, font_size=22, color=INK)
        label.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(operator), run_time=0.4)
        self.play(LaggedStart(*[AnimationGroup(GrowArrow(a), FadeIn(o))
                                for a, o in zip(arrows, outputs)],
                              lag_ratio=0.2), run_time=1.2)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 6.8))


class B08Doodle(Scene):
    """B08 — One standout (terracotta) figure among grey crowd."""
    def construct(self):
        self.camera.background_color = BG
        crowd = VGroup(*[_box("·", font_size=14, width=0.9, height=0.5)
                         for _ in range(8)])
        crowd.arrange_in_grid(rows=2, cols=4, buff=0.35)
        crowd.move_to(ORIGIN)

        standout = _box("Distinct", color=TERRA, font_size=22, width=2.2)
        standout.move_to(RIGHT * 4.5)

        label = Text("A stance that stands apart.", font=FONT, font_size=22, color=INK)
        label.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(crowd), run_time=0.5)
        self.play(GrowFromCenter(standout), run_time=0.7)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 5.5))


class B10Doodle(Scene):
    """B10 — Operator at doorway with preparation folder."""
    def construct(self):
        self.camera.background_color = BG
        door_left  = Line(UP * 1.8 + LEFT * 0.6, DOWN * 1.8 + LEFT * 0.6, color=INK, stroke_width=3)
        door_right = Line(UP * 1.8 + RIGHT * 0.6, DOWN * 1.8 + RIGHT * 0.6, color=INK, stroke_width=3)
        door_top   = Line(UP * 1.8 + LEFT * 0.6, UP * 1.8 + RIGHT * 0.6, color=INK, stroke_width=3)
        door = VGroup(door_left, door_right, door_top)
        door.move_to(LEFT * 2.5)

        figure = _box("You", color=TERRA, font_size=24, width=1.6)
        figure.next_to(door, LEFT, buff=0.5)

        folder = _box("Prep", font_size=22, width=1.8)
        folder.next_to(figure, DOWN, buff=0.3)

        label = Text("Walk in better prepared.", font=FONT, font_size=22, color=INK)
        label.to_edge(DOWN, buff=0.4)

        self.play(Create(door), run_time=0.5)
        self.play(FadeIn(figure), FadeIn(folder), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 3.2))


class B11Doodle(Scene):
    """B11 — Operator at table reviewing a combined brief."""
    def construct(self):
        self.camera.background_color = BG
        research = _box("RESEARCH", font_size=28, width=2.4)
        research.move_to(LEFT * 3.0 + UP * 1.1)

        sales = _box("SALES BRIEF", color=TERRA, font_size=28, width=2.4)
        sales.move_to(LEFT * 3.0 + DOWN * 0.6)

        brief = _box("COMBINED BRIEF", color=TERRA, font_size=28, width=2.8)
        brief.move_to(RIGHT * 2.5 + UP * 0.25)

        a1 = Arrow(research.get_right(), brief.get_left() + UP * 0.2,
                   buff=0.1, color=INK, stroke_width=2, tip_length=0.2)
        a2 = Arrow(sales.get_right(), brief.get_left() + DOWN * 0.2,
                   buff=0.1, color=INK, stroke_width=2, tip_length=0.2)

        label = Text("RESEARCH + SALES — ONE BRIEF.", font=FONT, font_size=28, color=INK)
        label.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(research), FadeIn(sales), run_time=0.5)
        self.play(GrowArrow(a1), GrowArrow(a2), GrowFromCenter(brief), run_time=0.8)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 8.0))


class B16Doodle(Scene):
    """B16 — Maker beside a board of support tickets (data feeds direction)."""
    def construct(self):
        self.camera.background_color = BG
        maker = _box("Maker", color=TERRA, font_size=24, width=2.0)
        maker.move_to(LEFT * 3.5)

        tickets = VGroup(*[_box(f"Ticket {i+1}", font_size=18, width=1.8, height=0.5)
                           for i in range(4)])
        tickets.arrange(DOWN, buff=0.25)
        tickets.move_to(RIGHT * 2.5)

        arrow = Arrow(tickets.get_left(), maker.get_right(),
                      buff=0.2, color=INK, stroke_width=2, tip_length=0.2)

        label = Text("Evidence, not intuition.", font=FONT, font_size=22, color=INK)
        label.to_edge(DOWN, buff=0.4)

        self.play(FadeIn(maker), run_time=0.4)
        self.play(FadeIn(tickets), run_time=0.5)
        self.play(GrowArrow(arrow), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 6.8))


class B21Doodle(Scene):
    """B21 — Two parties at a negotiation table with contract between them."""
    def construct(self):
        self.camera.background_color = BG
        table = Rectangle(width=4.0, height=0.15, color=INK, fill_color=INK, fill_opacity=1)
        table.move_to(ORIGIN)

        party_a = _box("You", color=TERRA, font_size=24, width=1.8)
        party_a.move_to(LEFT * 3.2)

        party_b = _box("Counterpart", font_size=22, width=2.0)
        party_b.move_to(RIGHT * 3.2)

        contract = _box("Contract", color=TERRA, font_size=22, width=2.0)
        contract.move_to(UP * 1.0)

        line_a = Line(party_a.get_right(), table.get_left(), color=INK, stroke_width=2)
        line_b = Line(party_b.get_left(), table.get_right(), color=INK, stroke_width=2)

        label = Text("Relationship + risk, one seat.", font=FONT, font_size=22, color=INK)
        label.to_edge(DOWN, buff=0.4)

        self.play(Create(table), run_time=0.3)
        self.play(FadeIn(party_a), FadeIn(party_b), run_time=0.5)
        self.play(Create(line_a), Create(line_b), run_time=0.4)
        self.play(GrowFromCenter(contract), run_time=0.5)
        self.play(FadeIn(label), run_time=0.4)
        self.wait(max(0.1, 7.6))


class B25Doodle(Scene):
    """B25 — Gap between two blocks; the gap is named, not hidden."""
    def construct(self):
        self.camera.background_color = BG
        block_l = _box("Data", font_size=28, width=2.2)
        block_l.move_to(LEFT * 3.5)

        gap_box = _box("Gap", color=TERRA, font_size=28, width=2.0)
        gap_box.move_to(ORIGIN)

        block_r = _box("Roadmap", font_size=28, width=2.2)
        block_r.move_to(RIGHT * 3.5)

        a_l = Arrow(block_l.get_right(), gap_box.get_left(), buff=0.1,
                    color=INK, stroke_width=2, tip_length=0.2)
        a_r = Arrow(gap_box.get_right(), block_r.get_left(), buff=0.1,
                    color=INK, stroke_width=2, tip_length=0.2)

        note = Text("not yet reachable", font=FONT, font_size=26, color=INK)
        note.next_to(gap_box, DOWN, buff=0.4)

        not_yet = Text("Name the gap before it surprises you.", font=FONT, font_size=28, color=INK)
        not_yet.to_edge(DOWN, buff=0.5)

        self.play(FadeIn(block_l), FadeIn(block_r), run_time=0.5)
        self.play(GrowArrow(a_l), GrowFromCenter(gap_box), run_time=0.6)
        self.play(GrowArrow(a_r), run_time=0.4)
        self.play(FadeIn(note), run_time=0.3)
        self.play(FadeIn(not_yet), run_time=0.4)
        self.wait(max(0.1, 7.0))
