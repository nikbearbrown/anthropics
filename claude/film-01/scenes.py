"""scenes.py — Meet Your Three Claudes (Film 1 of the Claude at Work series).
14 Manim scenes, M01–M14. House conventions: 16:9, safe-area coords
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


class M01_Bidea(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        plate = RoundedRectangle(corner_radius=0.3, width=12.4, height=6.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        hook = Text("one name, three places", font_size=52, color=INK)
        hook2 = Text("you meet it?", font_size=52, color=ACCENT)
        hook.move_to([0, 2.2, 0])
        hook2.next_to(hook, DOWN, buff=0.25)
        rule = Line(LEFT * 4.5, RIGHT * 4.5, color=GREY, stroke_width=4).move_to([0, 1.1, 0])
        self.play(Write(hook), Create(rule))
        self.play(Write(hook2))
        b_chat = labeled_box("chat", [-4.0, -1.3, 0], w=3.2, h=1.7, box_color=GREEN)
        b_code = labeled_box("code", [0, -1.3, 0], w=3.2, h=1.7, box_color=BLUE)
        b_mate = labeled_box("teammate", [4.0, -1.3, 0], w=3.2, h=1.7, box_color=ACCENT)
        self.play(Create(b_chat[0]), Write(b_chat[1]))
        self.play(Create(b_code[0]), Write(b_code[1]))
        self.play(Create(b_mate[0]), Write(b_mate[1]))
        self.wait(1.2)


class M02_Bdefs(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("Three terms", font_size=48, color=INK).to_edge(UP, buff=0.7)
        head_rule = Line(LEFT * 2.2, RIGHT * 2.2, color=ACCENT, stroke_width=5)
        head_rule.next_to(head, DOWN, buff=0.25)
        self.play(Write(head), Create(head_rule))
        terms = [
            ("Conversation", "Claude in chat \u2014 you talk, it answers", GREEN),
            ("Claude Code", "the coding agent, living in your terminal", BLUE),
            ("Cowork", "the teammate \u2014 you delegate the outcome", ACCENT),
        ]
        xs = [-4.0, 0.0, 4.0]
        for i, (term, gloss, color) in enumerate(terms):
            x = xs[i]
            card = RoundedRectangle(corner_radius=0.2, width=3.7, height=2.6,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=4).move_to([x, -0.4, 0])
            dot = bullet([x - 1.45, 0.45, 0], color=color)
            t = Text(term, font_size=30, color=INK).move_to([x + 0.1, 0.45, 0])
            g = Text(gloss, font_size=21, color=GREY).move_to([x, -0.85, 0])
            self.play(FadeIn(card), FadeIn(dot), Write(t), Write(g))
        self.wait(1.2)


class M03_B01(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        win = RoundedRectangle(corner_radius=0.25, width=8.6, height=4.6,
                               fill_color=CARD, fill_opacity=1,
                               stroke_color=GREEN, stroke_width=4).move_to([0, 0.2, 0])
        self.play(FadeIn(win))
        q = RoundedRectangle(corner_radius=0.35, width=5.4, height=1.0,
                             fill_color="#E4E1D8", fill_opacity=1,
                             stroke_color=GREY, stroke_width=2).move_to([-1.0, 1.4, 0])
        q_t = Text("a question\u2026", font_size=30, color=INK).move_to(q.get_center())
        self.play(FadeIn(q), Write(q_t))
        a = RoundedRectangle(corner_radius=0.35, width=6.2, height=1.0,
                             fill_color=CARD, fill_opacity=1,
                             stroke_color=GREEN, stroke_width=3).move_to([-0.6, -0.1, 0])
        a_t = Text("an answer, in the same breath", font_size=28, color=INK).move_to(a.get_center())
        self.play(FadeIn(a), Write(a_t))
        lab = Text("chat \u2014 thinks with you", font_size=34, color=GREEN).move_to([0, -2.6, 0])
        ldot = bullet([-3.6, -2.6, 0], color=GREEN)
        self.play(FadeIn(ldot), Write(lab))
        self.wait(1.2)


class M04_B02(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        term = RoundedRectangle(corner_radius=0.2, width=9.2, height=4.4,
                                fill_color="#1E1E1E", fill_opacity=1,
                                stroke_color=BLUE, stroke_width=4).move_to([0, 0.4, 0])
        self.play(FadeIn(term))
        p1 = Text("$ claude  \"ship the feature\"", font_size=32, color=CARD).move_to([-2.2, 1.7, 0])
        self.play(Write(p1))
        lines = ["reads the repo\u2026", "writes the code\u2026", "runs the tests\u2026"]
        for i, ln in enumerate(lines):
            t = Text(ln, font_size=30, color="#B8B8B8").move_to([-2.6, 0.8 - i * 0.8, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Write(t))
        tick = check_mark([3.4, -0.8, 0], scale=1.1)
        self.play(Create(tick[0]), Create(tick[1]))
        quote = Text("bridge the difference between an idea", font_size=26, color=INK).move_to([0, -2.5, 0])
        quote2 = Text("and a shipped product \u2014 Cat Woo", font_size=26, color=BLUE).move_to([0, -3.05, 0])
        self.play(Write(quote), Write(quote2))
        self.wait(1.2)


class M05_B03(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        hand_lab = Text("you hand over the outcome", font_size=34, color=INK).move_to([-3.4, 2.2, 0])
        self.play(Write(hand_lab))
        arrow = Arrow([-3.4, 1.4, 0], [-3.4, 0.4, 0], color=ACCENT, stroke_width=8)
        self.play(GrowArrow(arrow))
        card = RoundedRectangle(corner_radius=0.25, width=7.4, height=3.6,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to([-3.4, -1.6, 0])
        card_lab = Text("teammate", font_size=40, color=ACCENT).move_to([-3.4, -0.5, 0])
        self.play(FadeIn(card), Write(card_lab))
        tasks = ["research the account", "draft the brief", "schedule the follow-up"]
        for i, ln in enumerate(tasks):
            y = -1.3 - i * 0.75
            cm = check_mark([-6.0, y, 0], scale=0.6)
            t = Text(ln, font_size=26, color=INK).move_to([-5.3, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        quote = Text("it doesn't just tell you about the fix", font_size=26, color=INK).move_to([2.2, 0.6, 0])
        quote2 = Text("\u2014 it makes it happen \u00b7 Angela Jang", font_size=26, color=ACCENT).move_to([2.2, -0.05, 0])
        self.play(Write(quote), Write(quote2))
        self.wait(1.2)


class M06_B04(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        bubble = RoundedRectangle(corner_radius=0.5, width=7.6, height=2.8,
                                  fill_color=CARD, fill_opacity=1,
                                  stroke_color=GREEN, stroke_width=4).move_to([0, 1.2, 0])
        self.play(FadeIn(bubble))
        qs = []
        for i, x in enumerate([-2.2, 0.0, 2.2]):
            q = Text("?", font_size=72, color=GREEN).move_to([x, 1.2, 0])
            qs.append(q)
            self.play(Write(q))
        ans = Text("one answer, argued out", font_size=34, color=INK).move_to([0, -0.4, 0])
        self.play(*[FadeOut(q) for q in qs], Write(ans))
        lab = Text("chat wins at thinking", font_size=34, color=GREEN).move_to([0, -2.2, 0])
        ldot = bullet([-2.9, -2.2, 0], color=GREEN)
        self.play(FadeIn(ldot), Write(lab))
        self.wait(1.2)


class M07_B05(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        fcard = RoundedRectangle(corner_radius=0.2, width=6.4, height=3.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=BLUE, stroke_width=4).move_to([-2.6, 0.4, 0])
        fhead = Text("your repo", font_size=34, color=BLUE).move_to([-2.6, 1.5, 0])
        self.play(FadeIn(fcard), Write(fhead))
        for i in range(3):
            y = 0.6 - i * 0.85
            cm = check_mark([-5.0, y, 0], scale=0.65)
            ln = Line([-4.3, y, 0], [-1.2, y, 0], color=GREY, stroke_width=6)
            self.play(Create(cm[0]), Create(cm[1]), Create(ln))
        chip1 = RoundedRectangle(corner_radius=0.35, width=4.6, height=1.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to([3.4, 1.2, 0])
        c1 = Text("1,000+ PRs a month", font_size=30, color=INK).move_to(chip1.get_center())
        self.play(Create(chip1), Write(c1))
        chip2 = RoundedRectangle(corner_radius=0.35, width=4.6, height=1.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to([3.4, -0.4, 0])
        c2 = Text("migration time \u221290%", font_size=30, color=INK).move_to(chip2.get_center())
        self.play(Create(chip2), Write(c2))
        foot = Text("Spotify, on the same kit", font_size=28, color=GREY).move_to([3.4, -1.8, 0])
        self.play(Write(foot))
        self.wait(1.2)


class M08_B06(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        card = RoundedRectangle(corner_radius=0.25, width=8.8, height=4.0,
                                fill_color=CARD, fill_opacity=1,
                                stroke_color=ACCENT, stroke_width=4).move_to([0, 0.6, 0])
        head = Text("owns the outcome", font_size=40, color=ACCENT).move_to([0, 1.9, 0])
        self.play(FadeIn(card), Write(head))
        tasks = ["research the account", "draft the brief", "schedule the follow-up"]
        for i, ln in enumerate(tasks):
            y = 0.9 - i * 0.85
            cm = check_mark([-3.6, y, 0], scale=0.6)
            t = Text(ln, font_size=28, color=INK).move_to([-2.9, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        bar_bg = RoundedRectangle(corner_radius=0.3, width=7.6, height=0.8,
                                  fill_color="#E4E1D8", fill_opacity=1,
                                  stroke_color=INK, stroke_width=3).move_to([0, -1.9, 0])
        self.play(Create(bar_bg))
        bar_fill = RoundedRectangle(corner_radius=0.3, width=5.6, height=0.55,
                                    fill_color=ACCENT, fill_opacity=1,
                                    stroke_color=ACCENT, stroke_width=2).move_to([-0.8, -1.9, 0])
        cap = Text("while you're away", font_size=32, color=INK).move_to([0, -2.9, 0])
        self.play(GrowFromEdge(bar_fill, LEFT), Write(cap))
        self.wait(1.2)


class M09_B07(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        q = Text("who does the doing?", font_size=48, color=INK).to_edge(UP, buff=0.8)
        q_rule = Line(LEFT * 2.6, RIGHT * 2.6, color=ACCENT, stroke_width=5)
        q_rule.next_to(q, DOWN, buff=0.25)
        self.play(Write(q), Create(q_rule))
        rows = [
            ("you do it \u2192 chat", GREEN),
            ("the doing is code \u2192 Claude Code", BLUE),
            ("hand over the outcome \u2192 Cowork", ACCENT),
        ]
        for i, (ln, color) in enumerate(rows):
            y = 0.9 - i * 1.25
            card = RoundedRectangle(corner_radius=0.2, width=9.4, height=1.0,
                                    fill_color=CARD, fill_opacity=1,
                                    stroke_color=color, stroke_width=3).move_to([0, y, 0])
            t = Text(ln, font_size=32, color=INK).move_to(card.get_center())
            d = bullet([-4.3, y, 0], color=color)
            self.play(FadeIn(card), FadeIn(d), Write(t))
        self.wait(1.2)


class M10_B08(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("skip these mistakes", font_size=44, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        rows = [
            ("delegate \u2192 chat: it can't act", "it can advise"),
            ("brainstorm \u2192 Code: it's a builder", "not a sounding board"),
            ("vague wish \u2192 Cowork: needs the outcome", "not the steps"),
        ]
        for i, (ln, _) in enumerate(rows):
            y = 0.9 - i * 1.3
            xm = x_mark([-4.6, y, 0], scale=0.8)
            t = Text(ln, font_size=30, color=INK).move_to([-3.9, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            strike = Line([-4.2, y, 0], [-4.2 + t.width + 0.4, y, 0], color=ACCENT, stroke_width=4)
            self.play(Create(xm[0]), Create(xm[1]), Write(t), Create(strike))
        foot = Text("right surface, right job", font_size=34, color=GREEN).move_to([0, -2.6, 0])
        fdot = bullet([-2.6, -2.6, 0], color=GREEN)
        self.play(FadeIn(fdot), Write(foot))
        self.wait(1.2)


class M11_B09(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        b_chat = labeled_box("chat", [-4.2, 0.4, 0], w=3.0, h=1.7, box_color=GREEN)
        b_code = labeled_box("Code", [0, 0.4, 0], w=3.0, h=1.7, box_color=BLUE)
        b_cow = labeled_box("Cowork", [4.2, 0.4, 0], w=3.0, h=1.7, box_color=ACCENT)
        self.play(Create(b_chat[0]), Write(b_chat[1]))
        a1 = Arrow([-2.4, 0.4, 0], [-1.5, 0.4, 0], color=INK, stroke_width=8)
        self.play(GrowArrow(a1), Create(b_code[0]), Write(b_code[1]))
        a2 = Arrow([1.5, 0.4, 0], [2.4, 0.4, 0], color=INK, stroke_width=8)
        self.play(GrowArrow(a2), Create(b_cow[0]), Write(b_cow[1]))
        token = Dot(point=[-4.2, 2.0, 0], radius=0.22, color=ACCENT)
        path = Line([-4.2, 2.0, 0], [4.2, 2.0, 0], color=GREY, stroke_width=3)
        self.play(Create(path), FadeIn(token))
        self.play(token.animate.move_to([4.2, 2.0, 0]), run_time=1.6)
        lab = Text("one task, three surfaces", font_size=34, color=INK).move_to([0, -2.2, 0])
        ldot = bullet([-2.8, -2.2, 0])
        self.play(FadeIn(ldot), Write(lab))
        self.wait(1.2)


class M12_B10(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        plate = RoundedRectangle(corner_radius=0.3, width=11.8, height=5.4,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        q1 = Text("\u201cthree layers to one story\u201d", font_size=52, color=ACCENT)
        q1.move_to([0, 0.9, 0])
        self.play(Write(q1))
        rule = Line(LEFT * 3.5, RIGHT * 3.5, color=GREY, stroke_width=4).move_to([0, -0.3, 0])
        self.play(Create(rule))
        attr = Text("Cat Woo, Anthropic Tokyo keynote", font_size=32, color=INK).move_to([0, -1.3, 0])
        self.play(Write(attr))
        foot = Text("the models, the platform agents, and Claude Code", font_size=28, color=GREY).move_to([0, -2.1, 0])
        self.play(Write(foot))
        self.wait(1.2)


class M13_B11(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        head = Text("Claude at Work", font_size=48, color=INK).to_edge(UP, buff=0.7)
        self.play(Write(head))
        dots = []
        for i in range(10):
            x = -5.4 + i * 1.2
            color = ACCENT if i == 0 else GREY
            d = Dot(point=[x, 0.6, 0], radius=0.3, color=color)
            dots.append(d)
            self.play(FadeIn(d))
        one = Text("1", font_size=30, color=CARD).move_to(dots[0].get_center())
        self.play(Write(one))
        titles = ["Delegate It", "Scheduled Tasks", "Tag Claude In"]
        for i, t in enumerate(titles):
            lab = Text(t, font_size=26, color=GREY).move_to([-5.4 + (i + 1) * 1.2, -0.5, 0])
            self.play(Write(lab))
        nxt = Text("Next: Delegate It \u2014 Cowork's first real task", font_size=34, color=ACCENT).move_to([0, -1.9, 0])
        ndot = bullet([-4.9, -1.9, 0], color=ACCENT)
        self.play(FadeIn(ndot), Write(nxt))
        self.wait(1.2)


class M14_BvdtHtfOut(Scene):
    def construct(self):
        self.camera.background_color = PAPER
        # --- recap: four lines ---
        plate = RoundedRectangle(corner_radius=0.25, width=12.2, height=6.2,
                                 fill_color=CARD, fill_opacity=1,
                                 stroke_color=INK, stroke_width=3).move_to(ORIGIN)
        self.play(FadeIn(plate))
        recap_lines = [
            "Chat: thinks with you \u2014 you do the doing",
            "Code: builds in your repo \u2014 the doing is code",
            "Cowork: owns outcomes \u2014 you hand over the finish line",
            "One question: who does the doing?",
        ]
        recap_mobs = []
        for i, ln in enumerate(recap_lines):
            y = 1.9 - i * 1.15
            d = bullet([-5.5, y, 0])
            t = Text(ln, font_size=28, color=INK).move_to([-4.9, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            recap_mobs.extend([d, t])
            self.play(FadeIn(d), Write(t))
        # --- your turn ---
        self.play(*[FadeOut(m) for m in recap_mobs], FadeOut(plate))
        yt_card = RoundedRectangle(corner_radius=0.25, width=11.6, height=4.6,
                                   fill_color=CARD, fill_opacity=1,
                                   stroke_color=ACCENT, stroke_width=4).move_to(ORIGIN)
        yt_head = Text("Your turn.", font_size=48, color=ACCENT).move_to([0, 1.5, 0])
        self.play(FadeIn(yt_card), Write(yt_head))
        steps = [
            "Pick one task. Ask: who does the doing?",
            "Which Claude gets it \u2014 and why?",
        ]
        step_mobs = []
        for i, s in enumerate(steps):
            y = 0.3 - i * 1.0
            cm = check_mark([-5.0, y, 0], scale=0.8)
            t = Text(s, font_size=32, color=INK).move_to([-4.2, y, 0])
            t.shift(RIGHT * (t.width / 2 - 0.2))
            step_mobs.extend([cm, t])
            self.play(Create(cm[0]), Create(cm[1]), Write(t))
        # --- outro ---
        self.play(*[FadeOut(m) for m in step_mobs], FadeOut(yt_card), FadeOut(yt_head))
        out = title_card("Meet Your Three Claudes", "@NikBearBrown")
        self.play(FadeIn(out[0]), Write(out[1]), Write(out[2]))
        nxt = Text("Next: Delegate It", font_size=36, color=GREY).move_to([0, -2.6, 0])
        ndot = bullet([-2.4, -2.6, 0], color=ACCENT)
        self.play(FadeIn(ndot), Write(nxt))
        self.wait(1.2)
