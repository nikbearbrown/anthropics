"""scenes.py — Muse the Agent (Film 12). Manim visuals, house template."""
from manim import *
import numpy as np

config.pixel_width = 1920
config.pixel_height = 1080

INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"


def check_mark(pos, scale=0.35, color=GREEN):
    """Two-Line check mark (checker's stub has no Checkmark)."""
    l1 = Line(LEFT * 0.2 * scale, ORIGIN, color=color, stroke_width=int(8 * scale / 0.35))
    l2 = Line(ORIGIN, RIGHT * 0.45 * scale + UP * 0.45 * scale, color=color,
              stroke_width=int(8 * scale / 0.35))
    return VGroup(l1, l2).move_to(pos)


def cross_mark(pos, scale=0.35, color=ACCENT):
    """Two crossing Lines = X mark."""
    w = int(8 * scale / 0.35)
    l1 = Line(LEFT * 0.35 * scale + DOWN * 0.35 * scale,
              RIGHT * 0.35 * scale + UP * 0.35 * scale, color=color, stroke_width=w)
    l2 = Line(LEFT * 0.35 * scale + UP * 0.35 * scale,
              RIGHT * 0.35 * scale + DOWN * 0.35 * scale, color=color, stroke_width=w)
    return VGroup(l1, l2).move_to(pos)


def bullet(pos, color=ACCENT):
    return Dot(pos, radius=0.09, color=color)


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.3, width=9.5, height=3.2,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.4)
    grp = VGroup(plate, t)
    if sub:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.35)
        grp.add(s)
    return grp


def term_card(term, gloss, pos):
    plate = RoundedRectangle(corner_radius=0.18, width=5.2, height=1.7,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(term, font_size=36, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = Text(gloss, font_size=24, color=GREY).move_to(plate.get_center() + DOWN * 0.4)
    return VGroup(plate, t, g)


def small_card(label, pos, width=2.6):
    plate = RoundedRectangle(corner_radius=0.14, width=width, height=1.1,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    t = Text(label, font_size=30, color=INK).move_to(plate.get_center())
    return VGroup(plate, t)


def row_card(label, pos, width=6.0):
    plate = RoundedRectangle(corner_radius=0.14, width=width, height=0.85,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=2).move_to(pos)
    d = bullet(plate.get_left() + RIGHT * 0.4)
    t = Text(label, font_size=30, color=INK).next_to(d, RIGHT, buff=0.25)
    return VGroup(plate, d, t)


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = title_card("the other Muse", "the agent that runs errands")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        labels = ["goal", "plan", "errands"]
        x = -2.9
        prev = None
        for lab in labels:
            c = small_card(lab, DOWN * 2.2 + RIGHT * x)
            d = bullet(DOWN * 2.2 + RIGHT * x + UP * 0.95, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
            if prev is not None:
                arrow = Arrow(prev.get_right() + RIGHT * 0.15, c.get_left() - RIGHT * 0.15,
                              color=INK, buff=0.05, stroke_width=6)
                self.play(Create(arrow))
            prev = c
            x += 2.9
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("four terms", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        cards = [
            ("Agent", "acts toward a goal", LEFT * 3.1 + UP * 0.9),
            ("Intent layer", "the want, then money", RIGHT * 3.1 + UP * 0.9),
            ("Blast radius", "how far failure spreads", LEFT * 3.1 + DOWN * 1.1),
            ("Allow-list", "deny unless allowed", RIGHT * 3.1 + DOWN * 1.1),
        ]
        for term, gloss, pos in cards:
            c = term_card(term, gloss, pos)
            d = bullet(pos + DOWN * 1.25, color=BLUE)
            self.play(FadeIn(c, shift=UP * 0.2), FadeIn(d))
        self.wait(1.2)


class M03_B01Loop(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("goal in, plan out", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        goal = small_card("goal", LEFT * 3.6 + UP * 0.3)
        plan = small_card("plan", ORIGIN + UP * 0.3)
        act = small_card("act", RIGHT * 3.6 + UP * 0.3)
        self.play(FadeIn(goal, shift=RIGHT * 0.3))
        a1 = Arrow(goal.get_right(), plan.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a1), FadeIn(plan, shift=RIGHT * 0.3))
        a2 = Arrow(plan.get_right(), act.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a2), FadeIn(act, shift=RIGHT * 0.3))
        gate = Square(side_length=0.95, color=ACCENT, fill_opacity=0.25, stroke_width=4
                      ).rotate(45 * DEGREES).next_to(a2, UP, buff=0.25)
        gt = Text("approval", font_size=24, color=ACCENT).next_to(gate, UP, buff=0.15)
        self.play(Create(gate), Write(gt))
        term = Rectangle(width=3.2, height=1.6, color=INK, stroke_width=4).shift(DOWN * 2.0)
        prompt = Text(">_", font_size=36, color=INK).move_to(term.get_center() + LEFT * 0.9)
        cap = Text("its own cloud computer", font_size=28, color=GREY).next_to(term, DOWN, buff=0.2)
        self.play(FadeIn(term), Write(prompt), Write(cap))
        self.wait(1.2)


class M04_B02Errands(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("consumer errands", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        labels = ["book travel", "shop", "forms", "tickets", "subscriptions"]
        y = 1.8
        for lab in labels:
            row = row_card(lab, LEFT * 1.4 + UP * y, width=5.2)
            self.play(FadeIn(row, shift=LEFT * 0.3))
            y -= 1.15
        dots = VGroup(*[Dot(RIGHT * (2.2 + i * 0.55) + DOWN * 1.6, radius=0.11, color=BLUE)
                        for i in range(6)])
        lab = Text("connectors", font_size=28, color=GREY).next_to(dots, DOWN, buff=0.2)
        self.play(FadeIn(dots), Write(lab))
        self.wait(1.2)


class M05_B03Tiers(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("three tiers", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        tiers = [
            ("Free", "100M / week", LEFT * 4.0),
            ("Power", "$20 / mo \u00b7 500M / week", ORIGIN),
            ("Maximum", "$100 / mo \u00b7 3B / week", RIGHT * 4.0),
        ]
        for name, amt, pos in tiers:
            plate = RoundedRectangle(corner_radius=0.18, width=3.9, height=2.0,
                                     fill_color=CARD, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2).move_to(pos + UP * 0.4)
            t = Text(name, font_size=36, color=INK).move_to(plate.get_center() + UP * 0.45)
            a = Text(amt, font_size=26, color=GREY).move_to(plate.get_center() + DOWN * 0.45)
            d = bullet(pos + DOWN * 1.15, color=BLUE)
            self.play(FadeIn(VGroup(plate, t, a), shift=UP * 0.2), FadeIn(d))
        foot = Text("card required, even free", font_size=28, color=ACCENT).shift(DOWN * 2.6)
        self.play(Write(foot))
        self.wait(1.2)


class M06_B04Endure(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("endurance, not intelligence", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        bar_e = Rectangle(width=5.5, height=0.7, fill_color=GREEN, fill_opacity=0.9,
                          stroke_width=0).shift(LEFT * 0.6 + UP * 0.9)
        lab_e = Text("endurance", font_size=32, color=INK).next_to(bar_e, LEFT, buff=0.4)
        self.play(GrowFromEdge(bar_e, LEFT), Write(lab_e))
        bar_i = Rectangle(width=2.2, height=0.7, fill_color=GREY, fill_opacity=0.9,
                          stroke_width=0).shift(LEFT * 2.25 + DOWN * 0.5)
        lab_i = Text("intelligence", font_size=32, color=INK).next_to(bar_i, LEFT, buff=0.4)
        self.play(GrowFromEdge(bar_i, LEFT), Write(lab_i))
        cap = Text("saves time, not thought", font_size=36, color=ACCENT).shift(DOWN * 2.2)
        d = bullet(DOWN * 2.2 + LEFT * 4.4, color=ACCENT)
        self.play(Write(cap), FadeIn(d))
        self.wait(1.2)


class M07_B05Fees(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("who pays", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        you = small_card("you", LEFT * 4.0 + UP * 0.6)
        muse = small_card("Muse", ORIGIN + UP * 0.6)
        merch = small_card("merchant", RIGHT * 4.0 + UP * 0.6)
        self.play(FadeIn(you, shift=RIGHT * 0.3))
        a1 = Arrow(you.get_right(), muse.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a1), FadeIn(muse, shift=RIGHT * 0.3))
        a2 = Arrow(muse.get_right(), merch.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a2), FadeIn(merch, shift=RIGHT * 0.3))
        fee = CurvedArrow(merch.get_bottom(), muse.get_bottom() + RIGHT * 1.2,
                          angle=-TAU / 4, color=ACCENT, stroke_width=6)
        fee_lab = Text("merchant pays Meta a cut", font_size=28, color=ACCENT).next_to(fee, DOWN, buff=0.2)
        self.play(Create(fee), Write(fee_lab))
        cap = Text("you never see a charge", font_size=32, color=GREY).shift(DOWN * 2.5)
        self.play(Write(cap))
        self.wait(1.2)


class M08_B06Intent(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the intent layer", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        want = small_card("want", LEFT * 3.6 + UP * 0.4)
        choose = small_card("choose", ORIGIN + UP * 0.4)
        buy = small_card("buy", RIGHT * 3.6 + UP * 0.4)
        self.play(FadeIn(want, shift=RIGHT * 0.3))
        a1 = Arrow(want.get_right(), choose.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a1), FadeIn(choose, shift=RIGHT * 0.3))
        a2 = Arrow(choose.get_right(), buy.get_left(), color=INK, buff=0.15, stroke_width=6)
        self.play(Create(a2), FadeIn(buy, shift=RIGHT * 0.3))
        bracket = Brace(want, UP, color=ACCENT, buff=0.15)
        blab = Text("the intent layer", font_size=30, color=ACCENT).next_to(bracket, UP, buff=0.15)
        mdot = Dot(blab.get_right() + RIGHT * 0.4, radius=0.16, color=BLUE)
        mlabel = Text("Meta", font_size=26, color=BLUE).next_to(mdot, RIGHT, buff=0.2)
        self.play(GrowFromCenter(bracket), Write(blab), FadeIn(mdot), Write(mlabel))
        self.wait(1.2)


class M09_B07Queues(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("queues become markets", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        figs = VGroup(*[Circle(radius=0.28, color=INK, stroke_width=5).shift(LEFT * (2.4 - i * 1.2) + UP * 0.4)
                        for i in range(4)])
        self.play(FadeIn(figs, shift=RIGHT * 0.3))
        stall = Rectangle(width=4.4, height=2.2, color=ACCENT, stroke_width=5).shift(DOWN * 0.2)
        tags = VGroup(*[Text("$", font_size=30, color=ACCENT).shift(LEFT * (1.2 - i * 1.2) + DOWN * 0.2)
                        for i in range(3)])
        self.play(FadeOut(figs, shift=UP * 0.3), FadeIn(stall), FadeIn(tags))
        arrow = Arrow(stall.get_bottom(), DOWN * 2.4, color=INK, buff=0.1, stroke_width=6)
        slab = Text("surplus \u2192 subscriptions + resellers", font_size=28, color=GREY).next_to(arrow, DOWN, buff=0.15)
        self.play(Create(arrow), Write(slab))
        self.wait(1.2)


class M10_B08Loyalty(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the drift", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        ff = Text("frequent flyers", font_size=32, color=INK).shift(LEFT * 3.4 + UP * 1.4)
        sp = Text("spending", font_size=32, color=ACCENT).shift(RIGHT * 3.4 + UP * 1.4)
        arrow = Arrow(ff.get_right(), sp.get_left(), color=ACCENT, buff=0.2, stroke_width=6)
        self.play(Write(ff), Write(sp), Create(arrow))
        vis = small_card("visible line", LEFT * 2.8 + DOWN * 1.2, width=3.4)
        figs = VGroup(*[Dot(LEFT * (3.6 - i * 0.5) + DOWN * 0.45, radius=0.09, color=INK)
                        for i in range(4)])
        self.play(FadeIn(vis, shift=UP * 0.2), FadeIn(figs))
        inv = small_card("invisible score", RIGHT * 2.8 + DOWN * 1.2, width=3.4)
        q = Text("?", font_size=44, color=GREY).next_to(inv, UP, buff=0.25)
        self.play(FadeIn(inv, shift=UP * 0.2), FadeIn(q))
        self.wait(1.2)


class M11_B09Access(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("full disk, deny-list", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        big = Circle(radius=1.5, color=ACCENT, stroke_width=6).shift(LEFT * 3.0 + DOWN * 0.2)
        blab = Text("the whole disk", font_size=30, color=INK).move_to(big.get_center())
        self.play(Create(big), Write(blab))
        x = cross_mark(big.get_center() + RIGHT * 1.9 + UP * 0.0, scale=0.5)
        self.play(FadeIn(x, scale=0.6))
        small = Circle(radius=0.85, color=GREEN, stroke_width=6).shift(RIGHT * 3.0 + DOWN * 0.2)
        slab = Text("allow-list", font_size=28, color=INK).move_to(small.get_center())
        self.play(Create(small), Write(slab))
        chk = check_mark(small.get_center() + RIGHT * 1.35, scale=0.5)
        self.play(FadeIn(chk, scale=0.6))
        cap = Text("Saltzer and Schroeder, 1975", font_size=30, color=GREY).shift(DOWN * 2.7)
        self.play(Write(cap))
        self.wait(1.2)


class M12_B10Inject(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("adversarial, not random", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        page = Rectangle(width=2.6, height=3.4, color=INK, stroke_width=4).shift(LEFT * 3.6)
        plines = VGroup(*[Line(LEFT * 0.9, RIGHT * 0.9, color=GREY, stroke_width=4)
                          .shift(LEFT * 3.6 + UP * (1.1 - i * 0.55)) for i in range(5)])
        self.play(FadeIn(page), FadeIn(plines))
        agent = Dot(ORIGIN + DOWN * 0.4, radius=0.28, color=BLUE)
        alab = Text("agent", font_size=26, color=BLUE).next_to(agent, DOWN, buff=0.2)
        self.play(FadeIn(agent), Write(alab))
        steer = DashedLine(page.get_right(), agent.get_center(), color=ACCENT,
                           stroke_width=4, dash_length=0.18)
        self.play(Create(steer))
        button = Circle(radius=0.75, color=ACCENT, fill_opacity=0.85, stroke_width=0).shift(RIGHT * 3.6 + DOWN * 0.4)
        push = Arrow(agent.get_center(), button.get_center(), color=ACCENT, buff=0.35, stroke_width=8)
        self.play(FadeIn(button, scale=0.5), Create(push))
        self.wait(1.2)


class M13_B11Setup(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("impact \u00d7 recoverability", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        vline = Line(UP * 2.2, DOWN * 2.2, color=INK, stroke_width=4).shift(LEFT * 0.6)
        hline = Line(LEFT * 4.6, RIGHT * 4.6, color=INK, stroke_width=4).shift(LEFT * 0.6 + DOWN * 0.2)
        self.play(Create(vline), Create(hline))
        xl = Text("recoverability", font_size=26, color=GREY).next_to(hline, DOWN, buff=0.25)
        yl = Text("impact", font_size=26, color=GREY).rotate(90 * DEGREES).next_to(vline, LEFT, buff=0.35)
        rl = Text("recoverable", font_size=22, color=GREY).move_to(LEFT * 2.6 + DOWN * 0.85)
        ul = Text("unrecoverable", font_size=22, color=GREY).move_to(RIGHT * 1.6 + DOWN * 0.85)
        lo = Text("low", font_size=22, color=GREY).move_to(LEFT * 1.35 + DOWN * 1.5)
        hi = Text("high", font_size=22, color=GREY).move_to(LEFT * 1.35 + UP * 1.1)
        self.play(Write(xl), Write(yl), FadeIn(rl), FadeIn(ul), FadeIn(lo), FadeIn(hi))
        cell = Rectangle(width=3.6, height=1.9, color=ACCENT, fill_opacity=0.2,
                         stroke_width=5).move_to(RIGHT * 1.6 + UP * 1.1)
        clab = Text("the short list", font_size=28, color=ACCENT).move_to(cell.get_center() + UP * 0.5)
        items = Text("email \u00b7 money \u00b7 credentials \u00b7 public voice", font_size=22, color=INK).move_to(cell.get_center() + DOWN * 0.45)
        self.play(FadeIn(cell), Write(clab), Write(items))
        self.wait(1.2)


class M14_B12Rules(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("five rules", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rules = [
            "an agent\u2019s access is the attacker\u2019s access",
            "ask how bad it gets, not how likely",
            "caps belong outside the agent",
            "irreversible actions get a human",
            "protect the short list with real walls",
        ]
        y = 1.75
        for i, r in enumerate(rules, start=1):
            row = row_card(r, ORIGIN + UP * y, width=10.4)
            num = Text(str(i), font_size=30, color=CARD)
            disc = Circle(radius=0.26, color=ACCENT, fill_opacity=1, stroke_width=0)
            disc.move_to(row.get_left() + RIGHT * 0.45)
            num.move_to(disc.get_center())
            self.play(FadeIn(row, shift=LEFT * 0.3), FadeIn(disc), Write(num))
            y -= 1.35
        self.wait(1.2)


class M15_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap
        head = Text("the film in three lines", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        recap = [
            "The agent: goal in, plan out, errands done \u2014 endurance, not intelligence.",
            "Who pays: transaction fees now, the intent layer forever.",
            "Survive it: allow-lists, caps outside the agent, the five rules.",
        ]
        y = 1.3
        rec_g = VGroup()
        for line in recap:
            row = row_card(line, ORIGIN + UP * y, width=10.6)
            self.play(FadeIn(row, shift=LEFT * 0.3))
            rec_g.add(row)
            y -= 1.45
        self.play(FadeOut(head), FadeOut(rec_g))
        # Phase 2: your turn
        card = title_card("audit one agent", "what can it touch? what can it spend? what can it never do?")
        self.play(FadeIn(card, shift=DOWN * 0.3))
        turn_g = VGroup(card)
        self.play(FadeOut(turn_g))
        # Phase 3: outro
        outro = title_card("@NikBearBrown", "Thanks for watching the series")
        ring = Circle(radius=2.6, color=ACCENT, stroke_width=5).move_to(ORIGIN + DOWN * 0.2)
        self.play(FadeIn(outro, shift=DOWN * 0.3))
        self.play(Create(ring))
        self.wait(1.2)
