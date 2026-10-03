"""scenes.py — claude-liam-democracy-math-equation Manim scenes

16 scenes for the MANIM-lane beats:
  B05 B08 B14 B15 B17 B18 B20 B22 B25 B26 B27 B28 B30 B31 B35 B36

Batch render (from the reel folder):
  for cls in B05_ReverseEngineerBox B08_ContributionsNormalized B14_BernoulliOutcome \
             B15_LogitCurve B17_BetaPol B18_Hierarchy B20_SwissTimeline B22_Changepoint \
             B25_Prior B26_Update B27_BayesFactor B28_IllustrativePosteriors \
             B30_EventStudy B31_ZeroSurprise B35_TheNullResult B36_Falsify; do
    bid=${cls%%_*}
    manim -qh --fps 30 -r 1920,1080 scenes.py $cls &&
    mv media/videos/scenes/1080p30/${cls}.mp4 manim/${bid}.mp4
  done

Design: Claude palette; EB Garamond; one terracotta accent per scene.
"""
import json, math, pathlib
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

CREAM, INK, ACCENT, MUTE, WHITE = "#F2F0E9", "#3D3929", "#D97757", "#5D584F", "#FAF9F5"
config.background_color = CREAM

DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass

def dur(bid): return DUR.get(bid, 12.0)

def serif(txt, sz=40, clr=INK, **kw): return Text(txt, font_size=sz, color=clr, **kw)

def caps(txt, sz=24, clr=MUTE, **kw):
    return _Tx(txt.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **kw)

def tag_illustrative():
    t = caps("the essay's illustration", 26, INK)
    t.to_corner(DR).shift(UP * 0.35 + LEFT * 0.7)
    ln = Line(t.get_left() + DOWN * 0.22, t.get_right() + DOWN * 0.22, color=ACCENT, stroke_width=1.5)
    return VGroup(t, ln)

def hold(scene, bid, spent):
    scene.wait(max(1.0, dur(bid) - spent))


class B05_ReverseEngineerBox(Scene):
    def construct(self):
        box = RoundedRectangle(width=5.8, height=4.2, corner_radius=0.15, color=INK, stroke_width=7).shift(LEFT * 3.0)
        q = serif("?", 140, MUTE).move_to(box)
        lbl = caps("the decision process", 28).next_to(box, DOWN, 0.35)
        outs = VGroup(*[Arrow(box.get_right() + UP * y, box.get_right() + RIGHT * 3.6 + UP * y,
                              color=INK, stroke_width=9, max_tip_length_to_length_ratio=0.12)
                        for y in (1.2, 0.0, -1.2)])
        outc = VGroup(*[serif(t, 40, INK).next_to(outs[i], RIGHT, 0.2)
                        for i, t in enumerate(["granted", "denied", "granted"])])
        self.play(Create(box), FadeIn(q), FadeIn(lbl), run_time=1.6)
        self.play(LaggedStart(*[GrowArrow(a) for a in outs], lag_ratio=0.3),
                  LaggedStart(*[FadeIn(t) for t in outc], lag_ratio=0.3), run_time=2.2)
        backs = VGroup(*[Line(outc[i].get_left() + LEFT * 0.15, box.get_right() + UP * y,
                                    color=ACCENT, stroke_width=9)
                         for i, y in enumerate((1.2, 0.0, -1.2))])
        blabel = serif("work backward from outcomes", 40, INK).next_to(box, UP, 0.5).shift(RIGHT * 0.9)
        self.play(LaggedStart(*[Create(b) for b in backs], lag_ratio=0.25), FadeIn(blabel), run_time=2.4)
        hold(self, "B05", 6.2)


class B08_ContributionsNormalized(Scene):
    def construct(self):
        title = caps("channel one — contributions", 28).to_edge(UP, 0.8)
        big = Rectangle(width=1.1, height=3.2, color=INK, fill_color=INK, fill_opacity=0.75).shift(LEFT * 3 + DOWN * 0.6)
        sm = Rectangle(width=1.1, height=0.5, color=INK, fill_color=INK, fill_opacity=0.75).shift(RIGHT * 1.2 + DOWN * 1.95)
        bl = serif("$1M — a giant", 34).next_to(big, DOWN, 0.3)
        sl = serif("$10k — a shop", 34).next_to(sm, DOWN, 0.3)
        self.play(FadeIn(title), GrowFromEdge(big, DOWN), GrowFromEdge(sm, DOWN), FadeIn(bl), FadeIn(sl), run_time=2.2)
        arrow = serif("÷ firm assets", 32, INK).shift(UP * 1.6 + RIGHT * 3.4)
        big2 = Rectangle(width=1.1, height=1.4, color=ACCENT, fill_color=ACCENT, fill_opacity=0.8).move_to(big, aligned_edge=DOWN)
        sm2 = Rectangle(width=1.1, height=1.4, color=ACCENT, fill_color=ACCENT, fill_opacity=0.8).move_to(sm, aligned_edge=DOWN)
        eq = serif("comparable signals", 36, INK).next_to(arrow, DOWN, 0.4)
        self.play(FadeIn(arrow), Transform(big, big2), Transform(sm, sm2), run_time=2.0)
        self.play(FadeIn(eq), run_time=0.8)
        hold(self, "B08", 5.0)


class B14_BernoulliOutcome(Scene):
    def construct(self):
        c1 = RoundedRectangle(width=5.0, height=3.0, corner_radius=0.12, color=INK, fill_color=WHITE, fill_opacity=1).shift(LEFT * 3.1 + UP * 0.9)
        c0 = RoundedRectangle(width=5.0, height=3.0, corner_radius=0.12, color=INK, fill_color=WHITE, fill_opacity=1).shift(RIGHT * 3.1 + UP * 0.9)
        t1 = VGroup(serif("Y = 1", 64), serif("exemption granted", 34, MUTE)).arrange(DOWN, buff=0.25).move_to(c1)
        t0 = VGroup(serif("Y = 0", 64), serif("denied", 34, MUTE)).arrange(DOWN, buff=0.25).move_to(c0)
        self.play(FadeIn(c1), FadeIn(t1), run_time=1.0)
        self.play(FadeIn(c0), FadeIn(t0), run_time=1.0)
        bern = serif("Y  follows  Bernoulli( π )", 64).shift(DOWN * 1.9)
        self.play(Write(bern), run_time=1.6)
        pi_ring = Line(LEFT * 0.5, RIGHT * 0.5, color=ACCENT, stroke_width=7).next_to(bern, DOWN, 0.1).shift(RIGHT * 1.78)
        plabel = serif("the probability the model explains", 36, INK).next_to(bern, DOWN, 0.5)
        self.play(Create(pi_ring), FadeIn(plabel), run_time=1.4)
        hold(self, "B14", 5.0)


class B15_LogitCurve(Scene):
    def construct(self):
        ax = Axes(x_range=[-4, 4, 2], y_range=[0, 1, 0.5], x_length=8.6, y_length=4.6,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.1)
        xl = serif("political spend", 34, MUTE).next_to(ax.x_axis, DOWN, 0.2)
        yl = serif("P(exemption)", 34, MUTE).rotate(PI / 2).move_to([-5.1, -0.1, 0])
        line = ax.plot(lambda x: 0.5 + 0.125 * x, x_range=[-4, 4], color=INK, stroke_width=8)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), run_time=1.8)
        self.play(Create(line), run_time=1.4)
        sig = ax.plot(lambda x: 1 / (1 + math.exp(-1.4 * x)), x_range=[-4, 4], color=ACCENT, stroke_width=9)
        lab = serif("the logit link — curved, saturating, pinned to 0 and 1", 36, INK).to_edge(UP, 0.8)
        mid = Dot(ax.c2p(0, 0.5), color=ACCENT, radius=0.14)
        self.play(Transform(line, sig), FadeIn(lab), run_time=2.4)
        self.play(GrowFromCenter(mid), run_time=0.4)
        hold(self, "B15", 6.0)


class B17_BetaPol(Scene):
    def construct(self):
        eq = serif("logit(π) = α + β·econ · X·econ + β·pol · X·pol", 40).to_edge(UP, 1.0)
        self.play(Write(eq), run_time=2.2)
        ring = Line(LEFT * 1.8, RIGHT * 1.8, color=ACCENT, stroke_width=6).next_to(eq, DOWN, 0.12).shift(RIGHT * 3.15)
        lab = serif("β-pol — the allegation, as a coefficient", 36, INK).next_to(eq, DOWN, 0.5)
        self.play(Create(ring), FadeIn(lab), run_time=1.4)
        ax = Axes(x_range=[-1, 3, 1], y_range=[0, 1, 1], x_length=7.5, y_length=2.4,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 1.3)
        zero = Line(ax.c2p(0, 0), ax.c2p(0, 1.05), color=MUTE, stroke_width=6)
        zl = serif("0", 34, MUTE).next_to(zero, DOWN, 0.12).shift(LEFT * 0.35)
        d0 = ax.plot(lambda x: math.exp(-8 * x * x), x_range=[-1, 3], color=INK, stroke_width=7)
        self.play(Create(ax), Create(zero), FadeIn(zl), Create(d0), run_time=1.8)
        d1 = ax.plot(lambda x: math.exp(-8 * (x - 1.4) ** 2), x_range=[-1, 3], color=ACCENT, stroke_width=8)
        note = serif("posterior clearly right of zero = connection buys probability", 32, INK).next_to(ax, DOWN, 0.25)
        pk = Dot(ax.c2p(1.4, 1.0), color=ACCENT, radius=0.13)
        self.play(Transform(d0, d1), FadeIn(note), run_time=2.0)
        self.play(GrowFromCenter(pk), run_time=0.4)
        hold(self, "B17", 8.0)


class B18_Hierarchy(Scene):
    def construct(self):
        model = RoundedRectangle(width=11.5, height=5.6, corner_radius=0.15, color=MUTE, stroke_width=6).shift(DOWN * 0.2)
        mlab = caps("one model", 28).next_to(model.get_top(), DOWN, 0.2)
        inds = VGroup()
        for i, (name, base) in enumerate([("electronics", 0.62), ("steel", 0.35), ("pharma", 0.48)]):
            ib = RoundedRectangle(width=3.3, height=3.9, corner_radius=0.12, color=INK, stroke_width=2.5)
            ib.shift(LEFT * 3.9 + RIGHT * 3.9 * i + DOWN * 0.45)
            il = caps(name, 20, INK).next_to(ib.get_top(), DOWN, 0.18)
            bar = Rectangle(width=0.5, height=2.4 * base, color=MUTE, fill_color=MUTE, fill_opacity=0.6)
            bar.move_to(ib.get_bottom() + UP * (0.8 + 1.2 * base) + LEFT * 0.7)
            bl = serif("baseline", 32, MUTE).next_to(bar, DOWN, 0.1)
            dots = VGroup(*[Dot(ib.get_bottom() + UP * (0.5 + 1.9 * base * (0.7 + 0.25 * j)) + RIGHT * (0.35 + 0.35 * j),
                                radius=0.07, color=INK) for j in range(3)])
            inds.add(VGroup(ib, il, bar, bl, dots))
        self.play(Create(model), FadeIn(mlab), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(g) for g in inds], lag_ratio=0.3), run_time=2.6)
        star = Dot(inds[0][0].get_bottom() + UP * 3.1 + RIGHT * 0.9, radius=0.11, color=ACCENT)
        ring = Circle(radius=0.24, color=ACCENT, stroke_width=7).move_to(star)
        note = serif("did THIS firm beat its own industry's odds?", 36, INK).to_edge(UP, 0.8)
        self.play(FadeIn(star), Create(ring), FadeIn(note), run_time=1.8)
        hold(self, "B18", 7.4)


class B20_SwissTimeline(Scene):
    def construct(self):
        kicker = caps("us–swiss trade, 2025", 30, MUTE).to_edge(DOWN, 0.75)
        line = Line(LEFT * 5.0, RIGHT * 5.0, color=INK, stroke_width=8).shift(DOWN * 0.7)
        self.play(Create(line), FadeIn(kicker), run_time=1.2)
        events = [(-3.9, "AUG", "talks stall — 39%"), (-0.6, "SEP", "“icy”"), (3.7, "NOV 4", "the gifts")]
        spent = 1.2
        for x, when, what in events:
            tick = Line(UP * 0.3, DOWN * 0.3, color=INK, stroke_width=8).move_to(line.get_center() + RIGHT * x)
            w1 = caps(when, 32, MUTE).next_to(tick, DOWN, 0.3)
            w2 = serif(what, 44, INK).next_to(tick, UP, 0.35)
            self.play(Create(tick), FadeIn(w1), FadeIn(w2), run_time=1.1)
            spent += 1.1
        clock = VGroup(
            Circle(radius=0.55, color=INK, stroke_width=9),
            Line(ORIGIN, UP * 0.34, color=INK, stroke_width=8),
            Line(ORIGIN, RIGHT * 0.24, color=INK, stroke_width=8),
        )
        bar = VGroup(
            Rectangle(width=1.7, height=0.8, color=INK, stroke_width=8),
            Line(LEFT * 0.55, LEFT * 0.55 + UP * 0.5, color=INK, stroke_width=2).shift(DOWN * 0.25),
            Line(ORIGIN, UP * 0.5, color=INK, stroke_width=2).shift(DOWN * 0.25),
            Line(RIGHT * 0.55, RIGHT * 0.55 + UP * 0.5, color=INK, stroke_width=2).shift(DOWN * 0.25),
        )
        gift = VGroup(bar, clock.shift(RIGHT * 1.6)).arrange(RIGHT, buff=0.5)
        gift.move_to(line.get_center() + RIGHT * 3.7 + UP * 2.3)
        gl = serif("a clock and a gold bar", 34, INK).next_to(gift, UP, 0.25)
        accent = Line(LEFT * 0.8, RIGHT * 0.8, color=ACCENT, stroke_width=9).move_to(line.get_center() + RIGHT * 3.7 + DOWN * 1.15)
        self.play(FadeIn(gift), FadeIn(gl), Create(accent), run_time=1.2)
        hold(self, "B20", spent + 1.2)

class B22_Changepoint(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 1], y_range=[0, 50, 25], x_length=9.6, y_length=4.4,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.4)
        yl = serif("tariff rate", 34, MUTE).rotate(PI / 2).next_to(ax.y_axis, LEFT, 0.2)
        hi = ax.plot(lambda x: 39, x_range=[0.5, 7.4], color=INK, stroke_width=8)
        hlab = serif("39%", 36, INK).next_to(ax.c2p(1.2, 39), UP, 0.2)
        self.play(Create(ax), FadeIn(yl), Create(hi), FadeIn(hlab), run_time=1.8)
        flag = Triangle(color=ACCENT, fill_color=ACCENT, fill_opacity=1, stroke_width=0)\
            .scale(0.22).rotate(PI).move_to(ax.c2p(6.2, 44))
        flab = caps("nov 4 — gifts (E=1)", 28).next_to(flag, UP, 0.2)
        self.play(FadeIn(flag), FadeIn(flab), run_time=1.2)
        drop = ax.plot(lambda x: 15, x_range=[7.4, 9.6], color=ACCENT, stroke_width=9)
        fall = Line(ax.c2p(7.4, 39), ax.c2p(7.4, 15), color=ACCENT, stroke_width=9)
        cp = Circle(radius=0.16, color=ACCENT, stroke_width=7).move_to(ax.c2p(7.4, 15))
        dlab = serif("Nov 14 — 15%. The changepoint.", 36, INK).next_to(ax.c2p(7.9, 15), DOWN, 0.45)
        self.play(Create(fall), Create(drop), Create(cp), FadeIn(dlab), run_time=2.0)
        self.play(FadeIn(tag_illustrative()), run_time=0.8)
        hold(self, "B22", 7.8)


class B25_Prior(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 10, 2], y_range=[0, 1, 1], x_length=9.4, y_length=4.2,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.25)
        xl = serif("effect  of  contributions  (percentage  points)", 34, MUTE).next_to(ax.x_axis, DOWN, 0.2)
        self.play(Create(ax), FadeIn(xl), run_time=1.4)
        prior = ax.plot(lambda x: math.exp(-0.5 * ((x - 4) / 1.5) ** 2), x_range=[-2, 10], color=INK, stroke_width=8)
        center = Line(ax.c2p(4, 0), ax.c2p(4, 1.02), color=ACCENT, stroke_width=9)
        clab = serif("≈ 4 points", 36, INK).next_to(ax.c2p(4, 1.02), UP, 0.15)
        src = caps("published 2018–2020 research — the prior", 28).to_edge(UP, 0.8)
        self.play(Create(prior), Create(center), FadeIn(clab), FadeIn(src), run_time=2.4)
        hold(self, "B25", 3.8)


class B26_Update(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 10, 2], y_range=[0, 1, 1], x_length=9.4, y_length=4.0,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.25)
        self.play(Create(ax), run_time=1.0)
        prior = ax.plot(lambda x: math.exp(-0.5 * ((x - 4) / 1.5) ** 2), x_range=[-2, 10], color=MUTE, stroke_width=7)
        plab = serif("prior", 34, MUTE).next_to(ax.c2p(4, 1.0), UP, 0.12)
        pk = Dot(ax.c2p(4, 1.0), color=MUTE, radius=0.12)
        self.play(Create(prior), FadeIn(plab), GrowFromCenter(pk), run_time=1.4)
        post_r = ax.plot(lambda x: math.exp(-0.5 * ((x - 6.5) / 1.0) ** 2), x_range=[-2, 10], color=ACCENT, stroke_width=9)
        rlab = serif("stronger evidence — posterior moves right", 34, INK).to_edge(UP, 0.8)
        self.play(Create(post_r), FadeIn(rlab), run_time=1.8)
        post_l = ax.plot(lambda x: math.exp(-0.5 * (x / 0.8) ** 2), x_range=[-2, 10], color=ACCENT, stroke_width=9)
        llab = serif("no effect in the data — dragged back to zero", 34, INK).to_edge(UP, 0.8)
        pk2 = Dot(ax.c2p(0, 1.0), color=ACCENT, radius=0.13)
        self.play(Transform(post_r, post_l), Transform(rlab, llab), GrowFromCenter(pk2), run_time=2.2)
        note = serif("the starting belief is explicit — and the evidence may overrule it", 34, INK).next_to(ax, DOWN, 0.25)
        self.play(FadeIn(note), run_time=0.9)
        hold(self, "B26", 7.3)


class B27_BayesFactor(Scene):
    def construct(self):
        beam = Line(LEFT * 4.4, RIGHT * 4.4, color=INK, stroke_width=10).shift(UP * 1.7)
        post = Line(beam.get_center(), beam.get_center() + DOWN * 1.5, color=INK, stroke_width=8)
        lpan = VGroup(Line(beam.get_left(), beam.get_left() + DOWN * 1.0, color=INK, stroke_width=2.5),
                      serif("favoritism", 44).move_to(beam.get_left() + DOWN * 1.45))
        rpan = VGroup(Line(beam.get_right(), beam.get_right() + DOWN * 1.0, color=INK, stroke_width=2.5),
                      serif("merit", 44).move_to(beam.get_right() + DOWN * 1.45))
        self.play(Create(beam), Create(post), FadeIn(lpan), FadeIn(rpan), run_time=1.8)
        scale = NumberLine(x_range=[0, 120, 10], length=11.5, color=MUTE, stroke_width=2,
                           include_ticks=True, tick_size=0.22).shift(DOWN * 2.2)
        def sx(v): return (v - 60) / 120 * 11.5
        m10 = Line([sx(10), -2.2 - 0.15, 0], [sx(10), -2.2 + 0.25, 0], color=INK, stroke_width=7)
        m100 = Line([sx(100), -2.2 - 0.15, 0], [sx(100), -2.2 + 0.25, 0], color=ACCENT, stroke_width=7)
        l10 = serif("10 — strong", 36, INK).next_to(m10, DOWN, 0.2)
        l100 = serif("100 — decisive", 36, INK).next_to(m100, DOWN, 0.2)
        blab = caps("bayes factor", 30).to_edge(UP, 0.8)
        self.play(Create(scale), Create(m10), Create(m100), FadeIn(l10), FadeIn(l100), FadeIn(blab), run_time=2.2)
        self.play(Rotate(beam, -0.06, about_point=beam.get_center()),
                  lpan.animate.shift(DOWN * 0.2), rpan.animate.shift(UP * 0.2), run_time=1.4)
        hold(self, "B27", 5.4)


class B28_IllustrativePosteriors(Scene):
    def construct(self):
        ax = Axes(x_range=[-2, 22, 4], y_range=[0, 1, 1], x_length=9.4, y_length=3.6,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(UP * 0.6)
        xl = serif("effect on approval odds (percentage points)", 34, MUTE).next_to(ax.x_axis, DOWN, 0.2)
        self.play(Create(ax), FadeIn(xl), run_time=1.2)
        d1 = ax.plot(lambda x: 0.85 * math.exp(-0.5 * ((x - 6.2) / 1.1) ** 2), x_range=[-2, 22], color=INK, stroke_width=8)
        l1 = serif("contributions ≈ 6", 34, INK).next_to(ax.c2p(6.2, 0.9), UP, 0.1)
        d2 = ax.plot(lambda x: math.exp(-0.5 * ((x - 14.7) / 3.0) ** 2), x_range=[-2, 22], color=ACCENT, stroke_width=9)
        l2 = serif("ballroom donor ≈ 15", 34, INK).next_to(ax.c2p(14.7, 1.0), UP, 0.1)
        self.play(Create(d1), FadeIn(l1), run_time=1.4)
        self.play(Create(d2), FadeIn(l2), run_time=1.4)
        bf = serif("Bayes Factor: 247 — past “decisive”", 34, INK).shift(DOWN * 2.3 + LEFT * 1.5)
        ring = Line(LEFT * (bf.width / 2), RIGHT * (bf.width / 2), color=ACCENT, stroke_width=6).next_to(bf, DOWN, 0.15)
        self.play(Write(bf), Create(ring), run_time=1.6)
        self.play(FadeIn(tag_illustrative()), run_time=0.8)
        hold(self, "B28", 6.4)


class B30_EventStudy(Scene):
    def construct(self):
        eq = serif("abnormal return = actual − expected", 40).to_edge(UP, 0.8)
        self.play(Write(eq), run_time=1.8)
        ax = Axes(x_range=[0, 10, 1], y_range=[-1, 3, 1], x_length=9.4, y_length=3.8,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(DOWN * 0.9)
        pts = [0.2, 0.3, 0.1, 0.25, 0.2, 0.3, 2.1, 2.2, 2.15, 2.3]
        series = VMobject(color=INK, stroke_width=8)
        series.set_points_smoothly([ax.c2p(i, v) for i, v in enumerate(pts)])
        win = Rectangle(width=1.4 / 10 * 9.4, height=3.8, color=ACCENT,
                        fill_color=ACCENT, fill_opacity=0.12, stroke_width=2).move_to(ax.c2p(6.3, 1.0))
        wl = caps("announcement day", 28, ACCENT).next_to(win, UP, 0.15)
        self.play(Create(ax), Create(series), run_time=2.0)
        self.play(FadeIn(win), FadeIn(wl), run_time=1.2)
        hold(self, "B30", 5.0)


class B31_ZeroSurprise(Scene):
    def construct(self):
        base = Line(LEFT * 4.6, RIGHT * 4.6, color=MUTE, stroke_width=6).shift(DOWN * 1.6)
        b1 = Rectangle(width=1.6, height=2.6, color=INK, fill_color=INK, fill_opacity=0.8).move_to(base.get_center() + LEFT * 2.4, aligned_edge=DOWN).shift(DOWN * 0)
        b1.align_to(base, DOWN).shift(UP * 0.0)
        b1.move_to(base.get_center() + LEFT * 2.4 + UP * 1.3)
        l1 = VGroup(serif("+2%", 36, INK), serif("unconnected wins", 34, MUTE)).arrange(DOWN, buff=0.15).next_to(b1, UP, 0.25)
        b2 = Rectangle(width=1.6, height=0.22, color=ACCENT, fill_color=ACCENT, fill_opacity=1).move_to(base.get_center() + RIGHT * 2.4 + UP * 0.06)
        l2 = VGroup(serif("≈ 0", 40, INK), serif("connected wins", 34, MUTE)).arrange(DOWN, buff=0.15).next_to(b2, UP, 1.0)
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), Create(base), run_time=1.6)
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=1.4)
        ring = Ellipse(width=2.4, height=1.0, color=ACCENT, stroke_width=7).move_to(b2.get_center() + UP * 0.1)
        note = serif("zero surprise — the market had priced the favor in", 36, INK).to_edge(UP, 0.8)
        self.play(Create(ring), FadeIn(note), run_time=1.6)
        self.play(FadeIn(tag_illustrative()), run_time=0.7)
        hold(self, "B31", 5.3)


class B35_TheNullResult(Scene):
    def construct(self):
        title = serif("the same method, two tariff programs", 32).to_edge(UP, 0.8)
        base = Line(LEFT * 4.8, RIGHT * 4.8, color=MUTE, stroke_width=6).shift(DOWN * 1.7)
        b1 = Rectangle(width=2.0, height=2.4, color=INK, fill_color=INK, fill_opacity=0.8).move_to(base.get_center() + LEFT * 2.5 + UP * 1.2)
        l1 = VGroup(serif("Section 301", 34), serif("political effect found", 34, MUTE)).arrange(DOWN, buff=0.12).next_to(b1, DOWN, 0.3).shift(DOWN * 0.0)
        l1.next_to(b1, UP, 0.3)
        b2 = Rectangle(width=2.0, height=0.14, color=ACCENT, fill_color=ACCENT, fill_opacity=1).move_to(base.get_center() + RIGHT * 2.5 + UP * 0.07)
        l2 = VGroup(serif("steel & aluminum", 34), serif("no effect", 34, INK)).arrange(DOWN, buff=0.12).next_to(b2, UP, 1.0)
        self.play(FadeIn(title), Create(base), run_time=1.0)
        self.play(GrowFromEdge(b1, DOWN), FadeIn(l1), run_time=1.4)
        self.play(GrowFromEdge(b2, DOWN), FadeIn(l2), run_time=1.4)
        ring = Ellipse(width=3.0, height=1.1, color=ACCENT, stroke_width=7).move_to(b2.get_center() + UP * 0.15)
        note = serif("a method that can exonerate is a method you can trust to accuse", 32, INK).to_edge(DOWN, 0.75)
        self.play(Create(ring), FadeIn(note), run_time=1.6)
        hold(self, "B35", 5.4)


class B36_Falsify(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 6, 3], y_range=[0, 1, 1], x_length=8.8, y_length=3.4,
                  axis_config={"color": MUTE, "stroke_width": 2, "include_ticks": False}).shift(UP * 1.0)
        zero = Line(ax.c2p(0, 0), ax.c2p(0, 1.05), color=MUTE, stroke_width=6)
        wide = ax.plot(lambda x: 0.7 * math.exp(-0.5 * ((x - 2.2) / 1.3) ** 2), x_range=[-3, 6], color=INK, stroke_width=8)
        self.play(Create(ax), Create(zero), Create(wide), run_time=1.8)
        spike = ax.plot(lambda x: math.exp(-0.5 * (x / 0.28) ** 2), x_range=[-3, 6], color=ACCENT, stroke_width=9)
        lab = serif("β-pol collapses onto zero — favoritism falsified", 36, INK).to_edge(UP, 0.8)
        self.play(Transform(wide, spike), FadeIn(lab), run_time=2.2)
        c1 = Arc(radius=1.5, start_angle=PI, angle=-PI, color=INK, stroke_width=8).shift(DOWN * 2.2 + LEFT * 0.4)
        c2 = Arc(radius=1.5, start_angle=PI, angle=-PI, color=ACCENT, stroke_width=8).shift(DOWN * 2.2 + RIGHT * 0.4)
        cl = serif("connected and unconnected approval curves — overlapping", 34, MUTE).next_to(VGroup(c1, c2), DOWN, 0.25)
        self.play(Create(c1), Create(c2), FadeIn(cl), run_time=2.0)
        hold(self, "B36", 6.0)


def _twocol(scene, bid, lt, lsub, rt, rsub, l_accent=True):
    div = Line(UP * 3.0, DOWN * 3.0, color=MUTE, stroke_width=8)
    lt_ = serif(lt, 56, INK).move_to(LEFT * 3.5 + UP * 2.0)
    ll = Line(LEFT * 0.9, RIGHT * 0.9, color=ACCENT if l_accent else INK, stroke_width=8).next_to(lt_, DOWN, 0.35)
    ls = VGroup(*[serif(x, 34, MUTE) for x in lsub]).arrange(DOWN, buff=0.3).next_to(ll, DOWN, 0.5)
    rt_ = serif(rt, 56, INK).move_to(RIGHT * 3.5 + UP * 1.1)
    rl = Line(LEFT * 0.9, RIGHT * 0.9, color=INK if l_accent else ACCENT, stroke_width=8).next_to(rt_, DOWN, 0.35)
    rs = VGroup(*[serif(x, 34, MUTE) for x in rsub]).arrange(DOWN, buff=0.3).next_to(rl, DOWN, 0.5)
    for grp in (ls, rs):
        if grp.width > 5.4: grp.scale(5.4 / grp.width)
    scene.play(Create(div), run_time=0.8)
    scene.play(FadeIn(lt_), Create(ll), FadeIn(ls), run_time=1.6)
    scene.play(FadeIn(rt_), Create(rl), FadeIn(rs), run_time=1.6)
    hold(scene, bid, 4.0)


class B07_TwoCol(Scene):
    def construct(self):
        _twocol(self, "B07", "influence", ["Fuzzy.", "Unmeasurable.", "Deniable."],
                "proxies", ["Contributions.", "Lobbying.", "Gifts."], l_accent=True)


class B16_TwoCol(Scene):
    def construct(self):
        _twocol(self, "B16", "X-econ", ["Suppliers. Harm. Strategy.", "The merit case."],
                "X-pol", ["Money. Lobbying. Gifts.", "The allegation."], l_accent=False)


class B23_TwoCol(Scene):
    def construct(self):
        _twocol(self, "B23", "frequentist", ["Could this be chance?"],
                "bayesian", ["How probable is the cause?"], l_accent=False)


class B34_TwoCol(Scene):
    def construct(self):
        _twocol(self, "B34", "detected", ["Connected firms win more,", "merit held constant."],
                "not detected", ["Why.", "Intent never appears in the data."], l_accent=False)
