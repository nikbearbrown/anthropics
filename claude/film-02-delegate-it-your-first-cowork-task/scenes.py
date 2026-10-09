"""scenes.py — Delegate It: Your First Cowork Task (Film 2 of the Claude at Work series).
13 Manim scenes, M01–M13. House conventions: 16:9, safe-area coords
(±6.3 x, ±3.4 y), distinct non-text shapes per beat, every on-screen text
is read aloud in its beat. Paper background set in EVERY construct."""
from manim import *
config.pixel_width = 1920
config.pixel_height = 1080
INK = "#111111"
PAPER = "#F7F3EA"
ACCENT = "#B8472F"
BLUE = "#2F6BB8"
GREEN = "#2E8B57"
GREY = "#8A8578"
CARD = "#FFFFFF"
GOLD = "#E8B93C"


def title_card(title, sub=None):
    plate = RoundedRectangle(corner_radius=0.25, width=11.5, height=2.6,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=INK, stroke_width=3)
    t = Text(title, font_size=54, color=INK).move_to(plate.get_center() + UP * 0.35)
    g = VGroup(plate, t)
    if sub is not None:
        s = Text(sub, font_size=34, color=GREY).next_to(t, DOWN, buff=0.3)
        g.add(s)
    return g


def bullet(pos, color=ACCENT, r=0.12):
    return Dot(point=[pos[0], pos[1], 0], radius=r, color=color)


def check_mark(pos, scale=1.0, color=GREEN):
    return VGroup(
        Line(ORIGIN, RIGHT * 0.5 + DOWN * 0.3, color=color, stroke_width=10),
        Line(RIGHT * 0.5 + DOWN * 0.3, RIGHT * 1.3 + UP * 0.4, color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


def x_mark(pos, scale=1.0, color=ACCENT):
    return VGroup(
        Line(LEFT * 0.5 + UP * 0.5, RIGHT * 0.5 + DOWN * 0.5, color=color, stroke_width=10),
        Line(LEFT * 0.5 + DOWN * 0.5, RIGHT * 0.5 + UP * 0.5, color=color, stroke_width=10),
    ).scale(scale).move_to(pos)


def labeled_box(label, pos, w=3.4, h=1.6, box_color=INK, label_size=36):
    box = Rectangle(width=w, height=h, stroke_color=box_color, stroke_width=4,
                    fill_color=CARD, fill_opacity=1).move_to(pos)
    lab = Text(label, font_size=label_size, color=INK).move_to(box.get_center())
    return VGroup(box, lab)


def chip(label, pos, color=GREY, w=2.6, h=0.9, label_size=26):
    c = RoundedRectangle(corner_radius=0.2, width=w, height=h,
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=color, stroke_width=3).move_to(pos)
    t = Text(label, font_size=label_size, color=INK).move_to(c.get_center())
    return VGroup(c, t)


def doc_card(title, pos, w=3.6, h=4.2, bars=3):
    d = RoundedRectangle(corner_radius=0.15, width=w, height=h,
                         fill_color=CARD, fill_opacity=1,
                         stroke_color=INK, stroke_width=3).move_to(pos)
    t = Text(title, font_size=26, color=INK).move_to(
        [pos[0], pos[1] + h / 2 - 0.45, 0])
    g = VGroup(d, t)
    for i in range(bars):
        y = pos[1] + h / 2 - 1.1 - i * 0.55
        bar = Line([pos[0] - w / 2 + 0.5, y, 0],
                   [pos[0] + w / 2 - 0.5, y, 0],
                   color=GREY, stroke_width=5)
        g.add(bar)
    return g


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        plate = RoundedRectangle(corner_radius=0.3, width=12.4, height=6.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        clock = Circle(radius=1.1, color=INK, stroke_width=5).move_to([-3.6, 1.0, 0])
        hand1 = Line([-3.6, 1.0, 0], [-3.6, 1.75, 0], color=INK, stroke_width=8)
        hand2 = Line([-3.6, 1.0, 0], [-3.1, 0.75, 0], color=INK, stroke_width=8)
        self.play(Create(clock), Create(hand1), Create(hand2))
        t = Text("1:00 PM", font_size=44, color=INK).move_to([-3.6, -0.9, 0])
        self.play(Write(t))
        acme = chip("Acme Corp call", [-3.6, -2.0, 0], color=BLUE, w=3.4)
        self.play(FadeIn(acme))
        stamp = chip("prep: none", [0.2, 0.6, 0], color=ACCENT, w=2.8, h=1.0,
                     label_size=30)
        self.play(FadeIn(stamp))
        arrow = Arrow([1.9, 0.6, 0], [2.9, 0.6, 0], color=ACCENT, stroke_width=8)
        self.play(GrowArrow(arrow))
        task = labeled_box("delegate the prep", [4.6, 0.6, 0], w=3.2, h=1.6,
                           box_color=ACCENT, label_size=30)
        self.play(Create(task[0]), Write(task[1]))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        cw = labeled_box("Cowork", [0, 0.6, 0], w=3.6, h=1.8,
                         box_color=ACCENT, label_size=44)
        self.play(Create(cw[0]), Write(cw[1]))
        subs = chip("takes the whole task", [0, -1.15, 0], color=ACCENT, w=3.6,
                    h=0.8, label_size=26)
        self.play(FadeIn(subs))
        names = ["calendar", "Slack", "email"]
        xs = [-4.2, 0.0, 4.2]
        for i, (name, x) in enumerate(zip(names, xs)):
            c = chip(name, [x, 2.4, 0], color=GREY, w=2.6)
            ln = Line([x, 2.0, 0], [x * 0.25, 1.5, 0], color=GREY, stroke_width=4)
            self.play(FadeIn(c), Create(ln))
        cap = Text("you delegate the outcome, not the steps", font_size=34,
                   color=INK).move_to([0, -2.6, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M03_B01(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.25, width=10.5, height=1.7,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to([0, 2.2, 0])
        self.play(FadeIn(card))
        l1 = Text("Prep me for today's call", font_size=38, color=INK)
        l1.move_to([0, 2.55, 0])
        l2 = Text("with Acme Corp at one.", font_size=38, color=INK)
        l2.next_to(l1, DOWN, buff=0.15)
        self.play(Write(l1), Write(l2))
        directives = ["calendar search", "attendee research", "Slack threads",
                      "meeting notes", "match folder format"]
        for i, d in enumerate(directives):
            x = -4.8 + i * 2.4
            c = chip(d, [x, 0.2, 0], color=BLUE, w=2.2, h=0.85, label_size=22)
            self.play(FadeIn(c))
        cap = Text("the delegation, word for word", font_size=30, color=GREY)
        cap.move_to([0, -2.6, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M04_B02(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("the plan", font_size=48, color=INK).to_edge(UP, buff=0.7)
        rule = Line(LEFT * 1.6, RIGHT * 1.6, color=ACCENT, stroke_width=5)
        rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(rule))
        rows = ["calendar search", "attendee research",
                "Slack + notes review", "write the agenda"]
        for i, r in enumerate(rows):
            y = 1.2 - i * 1.05
            box = RoundedRectangle(corner_radius=0.15, width=6.4, height=0.85,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([0, y, 0])
            lab = Text(r, font_size=28, color=INK).move_to([-2.6, y, 0]).shift(RIGHT * 2.6)
            lab.move_to(box.get_center() + LEFT * 0.9)
            self.play(FadeIn(box), Write(lab))
            self.play(FadeIn(check_mark([2.55, y, 0], scale=0.8)))
        cap = Text("it starts working while you do something else", font_size=30,
                   color=GREY).move_to([0, -2.9, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M05_B03(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rows = ["calendar search", "attendee research",
                "Slack + notes review", "write the agenda"]
        row_groups = []
        for i, r in enumerate(rows):
            y = 2.0 - i * 1.0
            box = RoundedRectangle(corner_radius=0.15, width=5.4, height=0.8,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=INK, stroke_width=3).move_to([-3.2, y, 0])
            lab = Text(r, font_size=24, color=INK).move_to(box.get_center() + LEFT * 0.7)
            g = VGroup(box, lab)
            if i < 2:
                g.add(check_mark([-1.15, y, 0], scale=0.7))
            row_groups.append(g)
            self.add(g)
        # new source row slides in; lower rows shift down to make room
        new = RoundedRectangle(corner_radius=0.15, width=5.4, height=0.8,
                               fill_color="#F3E3D8", fill_opacity=1,
                               stroke_color=ACCENT, stroke_width=4).move_to([-3.2, 0.0, 0])
        new_t = Text("check email", font_size=24, color=INK).move_to(new.get_center())
        new_g = VGroup(new, new_t).shift(DOWN * 3.2)
        self.add(new_g)
        self.play(row_groups[2].animate.shift(DOWN * 1.0),
                  row_groups[3].animate.shift(DOWN * 1.0),
                  new_g.animate.shift(UP * 3.2))
        self.play(FadeIn(check_mark([-1.15, 0.0, 0], scale=0.7)))
        chat = RoundedRectangle(corner_radius=0.2, width=4.6, height=1.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=GREY, stroke_width=3).move_to([3.6, 1.4, 0])
        chat_t = Text("stop, wait,\nstart over", font_size=26, color=GREY).move_to(chat.get_center())
        self.play(FadeIn(chat), Write(chat_t))
        self.play(FadeIn(x_mark([3.6, 1.4, 0], scale=1.2)))
        piv = chip("pivot mid-task", [3.6, -1.2, 0], color=ACCENT, w=3.4, h=1.0,
                   label_size=28)
        self.play(FadeIn(piv))
        cap = Text("nothing is thrown away", font_size=28, color=INK).move_to([3.6, -2.6, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M06_B04(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        doc = doc_card("Acme Corp \u2014 agenda", [-3.4, 0.2, 0], w=3.8, h=4.4, bars=4)
        self.play(FadeIn(doc))
        calls = [("push for: decisions", 1.6), ("lead with: biggest win", 0.3),
                 ("watch: watch items", -1.0)]
        for label, y in calls:
            c = chip(label, [2.8, y, 0], color=ACCENT, w=4.6, h=0.95, label_size=26)
            self.play(FadeIn(c))
        cap = Text("prep, plus judgment", font_size=32, color=INK).move_to([0, -2.9, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M07_B05(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        old = doc_card("existing format", [-4.0, 1.2, 0], w=3.2, h=3.4, bars=3)
        new = doc_card("your agenda", [0.6, 1.2, 0], w=3.2, h=3.4, bars=3)
        self.play(FadeIn(old), FadeIn(new))
        arrow = Arrow([-2.2, 1.2, 0], [-1.2, 1.2, 0], color=ACCENT, stroke_width=8)
        self.play(GrowArrow(arrow))
        match = Text("same headings, same bullets", font_size=28, color=INK)
        match.move_to([-1.7, 3.3, 0])
        self.play(Write(match))
        srcs = [("calendar: attendees", BLUE), ("Slack: contacts", GREEN),
                ("email: feedback", ACCENT)]
        for i, (s, col) in enumerate(srcs):
            c = chip(s, [-4.2 + i * 4.2, -1.3, 0], color=col, w=3.6, h=0.85,
                     label_size=22)
            self.play(FadeIn(c))
        blank = RoundedRectangle(corner_radius=0.15, width=6.2, height=0.85,
                                 fill_color=PAPER, fill_opacity=1,
                                 stroke_color=GREY, stroke_width=3).move_to([0.7, -2.5, 0])
        bt = Text("action items (blank)", font_size=26, color=GREY).move_to(blank.get_center())
        self.play(FadeIn(blank), Write(bt))
        self.wait(1.2)


class M08_B06(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        thread = RoundedRectangle(corner_radius=0.2, width=4.6, height=2.0,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=BLUE, stroke_width=4).move_to([-3.6, 0.8, 0])
        self.play(FadeIn(thread))
        t1 = Text("last Tuesday", font_size=30, color=INK).move_to([-3.6, 1.3, 0])
        t2 = Text("pricing thread", font_size=30, color=INK).move_to([-3.6, 0.45, 0])
        self.play(Write(t1), Write(t2))
        doc = doc_card("the brief", [3.4, 0.6, 0], w=3.4, h=3.8, bars=3)
        self.play(FadeIn(doc))
        arrow = Arrow([-1.1, 0.8, 0], [1.5, 0.8, 0], color=ACCENT, stroke_width=10)
        self.play(GrowArrow(arrow))
        fold = Text("folded in", font_size=28, color=ACCENT).move_to([0.2, 1.6, 0])
        self.play(Write(fold))
        stamp = chip("no restart", [0.2, -2.4, 0], color=ACCENT, w=2.8, h=1.0,
                     label_size=30)
        self.play(FadeIn(stamp))
        self.wait(1.2)


class M09_B07(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        doc = doc_card("the agenda", [0, 0.9, 0], w=3.6, h=3.6, bars=3)
        self.play(FadeIn(doc))
        stamp = chip("yours to own", [0, -1.6, 0], color=ACCENT, w=3.2, h=1.0,
                     label_size=30)
        self.play(FadeIn(stamp))
        a1 = Arrow([-2.2, -1.6, 0], [-4.2, -1.6, 0], color=INK, stroke_width=8)
        a2 = Arrow([2.2, -1.6, 0], [4.2, -1.6, 0], color=INK, stroke_width=8)
        self.play(GrowArrow(a1), GrowArrow(a2))
        p1 = Text("via Claude", font_size=28, color=INK).move_to([-4.9, -2.4, 0])
        p2 = Text("yourself", font_size=28, color=INK).move_to([4.9, -2.4, 0])
        self.play(Write(p1), Write(p2))
        cap = Text("it prepares, you decide", font_size=34, color=INK).move_to([0, -2.9, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M10_B08(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        rules = ["delegate the outcome", "connect tools once",
                 "steer mid-flight", "never start over"]
        card = RoundedRectangle(corner_radius=0.25, width=8.6, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to([0, 1.2, 0])
        self.play(FadeIn(card))
        for i, r in enumerate(rules):
            y = 2.3 - i * 0.75
            d = bullet([-3.6, y, 0], color=ACCENT)
            t = Text(r, font_size=30, color=INK).move_to([-1.0, y, 0])
            self.play(FadeIn(d), Write(t))
        chat = chip("chat \u2014 answers", [-2.6, -2.2, 0], color=GREY, w=4.4, h=1.1,
                    label_size=30)
        cw = chip("Cowork \u2014 takes the task", [2.6, -2.2, 0], color=ACCENT, w=4.4,
                  h=1.1, label_size=30)
        self.play(FadeIn(chat), FadeIn(cw))
        self.wait(1.2)


class M11_B09(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.25, width=8.2, height=3.8,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=INK, stroke_width=4).move_to([-1.2, 0.8, 0])
        self.play(FadeIn(card))
        head = Text("good first task", font_size=40, color=INK).move_to([-1.2, 2.2, 0])
        self.play(Write(head))
        crits = ["clear output", "a deadline", "you own the final"]
        for i, c in enumerate(crits):
            y = 1.2 - i * 0.85
            self.play(FadeIn(check_mark([-4.4, y, 0], scale=0.7)))
            t = Text(c, font_size=30, color=INK).move_to([-3.5, y, 0]).shift(RIGHT * 1.9)
            t.move_to([-1.6, y, 0])
            self.play(Write(t))
        pick = chip("meeting prep", [3.9, 0.8, 0], color=ACCENT, w=3.2, h=1.2,
                    label_size=32)
        self.play(FadeIn(pick))
        self.play(FadeIn(check_mark([3.9, 2.0, 0], scale=0.9)))
        self.wait(1.2)


class M12_B10(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        names = ["calendar", "Slack", "email"]
        chips = []
        for i, n in enumerate(names):
            x = -4.0 + i * 2.6
            c = chip(n, [x, 1.8, 0], color=GREY, w=2.4)
            chips.append(c)
            self.play(FadeIn(c))
        once = chip("connected once", [0, 0.0, 0], color=GREEN, w=3.6, h=1.1,
                    label_size=30)
        self.play(FadeIn(once))
        for c in chips:
            ln = Line(c.get_center() + DOWN * 0.45, once.get_center() + UP * 0.55,
                      color=GREY, stroke_width=4)
            self.play(Create(ln))
        arrow = Arrow([2.1, 0.0, 0], [3.1, 0.0, 0], color=ACCENT, stroke_width=8)
        self.play(GrowArrow(arrow))
        sent = labeled_box("one sentence\nto delegate", [4.7, 0.0, 0], w=3.0, h=1.8,
                           box_color=ACCENT, label_size=30)
        self.play(Create(sent[0]), Write(sent[1]))
        cap = Text("do the setup today", font_size=32, color=INK).move_to([0, -2.6, 0])
        self.play(Write(cap))
        self.wait(1.2)


class M13_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # Phase 1: recap
        recap = RoundedRectangle(corner_radius=0.25, width=10.0, height=4.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=ACCENT, stroke_width=4).move_to([0, 0.4, 0])
        self.play(FadeIn(recap))
        head = Text("four lines to keep", font_size=40, color=INK).move_to([0, 2.1, 0])
        self.play(Write(head))
        lines = ["delegate the outcome, not the steps", "connect your tools once",
                 "steer mid-flight \u2014 never start over", "own the final document"]
        grp = VGroup(recap, head)
        for i, ln in enumerate(lines):
            y = 1.1 - i * 0.8
            t = Text(ln, font_size=30, color=INK).move_to([0, y, 0])
            grp.add(t)
            self.play(Write(t))
        self.wait(2.5)
        # Phase 2: your turn
        self.play(FadeOut(grp))
        turn = RoundedRectangle(corner_radius=0.25, width=10.0, height=4.4,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=BLUE, stroke_width=4).move_to([0, 0.2, 0])
        self.play(FadeIn(turn))
        th = Text("your turn", font_size=44, color=BLUE).move_to([0, 1.7, 0])
        self.play(Write(th))
        steps = ["pick one meeting this week", "hand Cowork the prep",
                 "steer it once"]
        tg = VGroup(turn, th)
        for i, s in enumerate(steps):
            y = 0.6 - i * 0.8
            t = Text(s, font_size=30, color=INK).move_to([0, y, 0])
            tg.add(t)
            self.play(Write(t))
        self.wait(2.5)
        # Phase 3: outro
        self.play(FadeOut(tg))
        out = title_card("Delegate It", "Next: While You Were Away")
        self.play(FadeIn(out))
        handle = Text("@NikBearBrown", font_size=30, color=GREY).move_to([0, -2.6, 0])
        self.play(Write(handle))
        self.wait(2.0)
