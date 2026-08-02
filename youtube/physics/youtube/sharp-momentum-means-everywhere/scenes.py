import json
from pathlib import Path
from manim import *

CREAM, INK, TERRA = "#FAF9F5", "#3D3929", "#D97757"
FONT = "EB Garamond"

HERE = Path(__file__).parent
try:
    _bs = json.loads((HERE / 'beat_sheet.json').read_text())
    DUR = {b['beat_id']: float(b.get('actual_duration_s') or b.get('estimated_duration_s') or 5)
           for b in _bs.get('beats', [])}
    TITLE = _bs['metadata'].get('title', '')
except Exception:
    DUR = {}; TITLE = ''

def d(bid, default=5.0):
    return DUR.get(bid, default)

def bg():
    return Rectangle(width=16, height=9).set_fill(CREAM, 1).set_stroke(width=0)

def ink_txt(t, size=36, color=INK, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)

def terra_txt(t, size=36, color=TERRA, **kw):
    return Text(t, font=FONT, font_size=size, color=color, **kw)


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Sharp Momentum\nMeans Everywhere", size=54)
        title.move_to(ORIGIN)
        sub = terra_txt("p = ħk  →  |ψ|² = constant", size=34)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_SharpMomentum(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        lbl1 = ink_txt("I know exactly", size=56)
        lbl2 = ink_txt("what p is!", size=56)
        lbl1.to_edge(LEFT, buff=1.0).shift(UP * 0.4)
        lbl2.next_to(lbl1, DOWN, buff=0.15).align_to(lbl1, LEFT)
        # Momentum arrow — use Line to avoid small arrowhead blobs
        arrow = Line([-1.0, 0, 0], [4.0, 0, 0], color=INK, stroke_width=6)
        p_lbl = MathTex(r"p = \hbar k", color=INK, font_size=80)
        p_lbl.next_to(arrow, UP, buff=0.3)
        self.play(FadeIn(lbl1), FadeIn(lbl2), run_time=0.5)
        self.play(Create(arrow), FadeIn(p_lbl), run_time=0.7)
        self.wait(max(0.1, dur - 1.2))


class H02_SmearedEverywhere(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("But where IS it?", size=56)
        lbl.to_edge(UP, buff=0.8)
        # Flat probability bar showing "everywhere"
        xs = np.linspace(-6.5, 6.5, 200)
        flat_y = -0.5
        flat = Line([-6.5, flat_y, 0], [6.5, flat_y, 0], color=INK, stroke_width=4)
        everywhere_lbl = ink_txt("everywhere", size=56)
        everywhere_lbl.move_to([0, flat_y - 0.7, 0])
        baffled = ink_txt("?", size=80)
        baffled.move_to([0, 1.5, 0])
        self.play(FadeIn(lbl), run_time=0.4)
        self.play(FadeIn(baffled), run_time=0.4)
        self.play(Create(flat), run_time=0.6)
        self.play(FadeIn(everywhere_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.8))


class A01_PlaneWave(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        title = ink_txt("Plane wave: fixed wavelength", size=56)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 400)
        k = 2.5
        ys = np.cos(k * xs) * 1.2
        pts = [[x, y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        wave.shift(DOWN * 0.3)
        # Amplitude constant line — solid lines to avoid small dash blobs
        amp_top = Line([-6.5, 1.2 - 0.3, 0], [6.5, 1.2 - 0.3, 0], color=INK,
                       stroke_width=1.5, stroke_opacity=0.5)
        amp_bot = Line([-6.5, -1.2 - 0.3, 0], [6.5, -1.2 - 0.3, 0], color=INK,
                       stroke_width=1.5, stroke_opacity=0.5)
        amp_lbl = ink_txt("amplitude = const.", size=56)
        amp_lbl.move_to([3.0, 1.6, 0])
        # One momentum — use Line to avoid small arrowhead blobs
        p_arrow = Line([-1.0, -2.5, 0], [1.0, -2.5, 0], color=INK, stroke_width=5)
        p_lbl = MathTex(r"p = \hbar k", color=INK, font_size=80)
        p_lbl.next_to(p_arrow, RIGHT, buff=0.3)
        self.add(title)
        self.play(Create(wave), run_time=0.7)
        self.play(Create(amp_top), Create(amp_bot), FadeIn(amp_lbl), run_time=0.5)
        self.play(Create(p_arrow), FadeIn(p_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.7))


class A02_FlatProbability(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        title = ink_txt("probability constant: particle everywhere", size=56)
        title.to_edge(UP, buff=0.6)
        # Flat probability density line
        flat_y = 0.0
        flat_rect = Rectangle(width=13, height=1.0, color=INK, stroke_width=2)
        flat_rect.set_fill(INK, opacity=0.10)
        flat_rect.move_to([0, flat_y, 0])
        axis = Line([-6.5, flat_y - 0.7, 0], [6.5, flat_y - 0.7, 0],
                    color=INK, stroke_width=2)
        x_lbl = ink_txt("x", size=56)
        x_lbl.next_to(axis, RIGHT, buff=0.1)
        label = ink_txt("everywhere", size=56)
        label.move_to([0, flat_y + 2.0, 0])
        arrows = VGroup(
            Line([0, flat_y + 1.5, 0], [-5.5, flat_y + 0.6, 0], color=INK, stroke_width=2),
            Line([0, flat_y + 1.5, 0], [5.5, flat_y + 0.6, 0], color=INK, stroke_width=2),
        )
        self.add(title, axis, x_lbl)
        self.play(Create(flat_rect), run_time=0.6)
        self.play(Write(label), run_time=0.5)
        self.play(Create(arrows), run_time=0.4)
        self.wait(max(0.1, dur - 1.5))


class A03_ClearAndPrepare(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        title = ink_txt("What if we add momenta together?", size=56)
        title.to_edge(UP, buff=0.8)
        sub = ink_txt("superpose waves with different k", size=56)
        sub.next_to(title, DOWN, buff=0.5)
        formula = MathTex(r"\psi = \sum_n a_n e^{ikx}", color=INK, font_size=80)
        formula.move_to([0, -0.5, 0])
        self.play(FadeIn(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.4)
        self.play(FadeIn(formula), run_time=0.5)
        self.wait(max(0.1, dur - 1.4))


class A04_ThreeMomenta(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        title = ink_txt("3 momenta summed: beats appear", size=42)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        ks = [2.0, 2.5, 3.0]
        ys = sum(np.cos(k * xs) for k in ks) / 3.0
        pts = [[x, y * 1.5 - 0.5, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        axis = Line([-6.5, -0.5, 0], [6.5, -0.5, 0], color=INK, stroke_width=2)
        # Probability
        prob_ys = ys ** 2
        prob_pts = [[x, prob_y * 1.0 - 2.8, 0] for x, prob_y in zip(xs, prob_ys)]
        prob_curve = VMobject(color=INK, stroke_width=2)
        prob_curve.set_points_smoothly(prob_pts)
        prob_lbl = MathTex(r"|\psi|^2", color=INK, font_size=68)
        prob_lbl.move_to([-5.5, -2.8, 0])
        self.add(title, axis)
        self.play(Create(wave), run_time=0.8)
        self.play(Create(prob_curve), FadeIn(prob_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.3))


class A05_SixMomenta(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        title = ink_txt("6 momenta: a clearer central lump", size=34)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        ks = np.linspace(1.8, 3.2, 6)
        ys = sum(np.cos(k * xs) for k in ks) / 6.0
        pts = [[x, y * 1.8 - 0.5, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        axis = Line([-6.5, -0.5, 0], [6.5, -0.5, 0], color=INK, stroke_width=2)
        prob_ys = ys ** 2
        prob_pts = [[x, prob_y * 1.2 - 2.8, 0] for x, prob_y in zip(xs, prob_ys)]
        prob_curve = VMobject(color=TERRA, stroke_width=2)
        prob_curve.set_points_smoothly(prob_pts)
        lump_lbl = terra_txt("lump forming", size=28)
        lump_lbl.move_to([0, -2.2, 0])
        self.add(title, axis)
        self.play(Create(wave), run_time=0.6)
        self.play(Create(prob_curve), FadeIn(lump_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.0))


class A06_WavePacket(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        title = ink_txt("Many momenta: localized wave packet", size=56)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 600)
        # Gaussian-weighted superposition
        k0 = 2.5; dk = 0.8
        ks = np.linspace(k0 - 2 * dk, k0 + 2 * dk, 50)
        weights = np.exp(-0.5 * ((ks - k0) / dk) ** 2)
        ys = sum(w * np.cos(k * xs) for w, k in zip(weights, ks))
        ys = ys / np.max(np.abs(ys)) * 1.4
        pts = [[x, y - 0.2, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        # Envelope
        env = np.exp(-0.5 * (xs / 1.5) ** 2) * 1.4
        env_pts = [[x, y - 0.2, 0] for x, y in zip(xs, env)]
        env_curve = VMobject(color=INK, stroke_width=2, stroke_opacity=0.5)
        env_curve.set_points_smoothly(env_pts)
        neg_env_pts = [[x, -y - 0.2, 0] for x, y in zip(xs, env)]
        neg_env_curve = VMobject(color=INK, stroke_width=2, stroke_opacity=0.5)
        neg_env_curve.set_points_smoothly(neg_env_pts)
        axis = Line([-6.5, -0.2, 0], [6.5, -0.2, 0], color=INK, stroke_width=2)
        lbl = ink_txt("wave packet (blob)", size=56)
        lbl.move_to([3.0, 1.8, 0])
        self.add(title, axis)
        self.play(Create(wave), run_time=0.7)
        self.play(Create(env_curve), Create(neg_env_curve), run_time=0.4)
        self.play(FadeIn(lbl), run_time=0.3)
        self.wait(max(0.1, dur - 1.4))


class A07_ProbabilityBump(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        xs = np.linspace(-6.5, 6.5, 600)
        k0 = 2.5; dk = 0.8
        ks = np.linspace(k0 - 2 * dk, k0 + 2 * dk, 50)
        weights = np.exp(-0.5 * ((ks - k0) / dk) ** 2)
        ys = sum(w * np.cos(k * xs) for w, k in zip(weights, ks))
        ys = ys / np.max(np.abs(ys)) * 1.2
        wave_pts = [[x, y + 1.0, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=2)
        wave.set_points_smoothly(wave_pts)
        # Probability density
        prob = ys ** 2
        prob_max = np.max(prob)
        prob_pts = [[x, p / prob_max * 1.5 - 2.5, 0] for x, p in zip(xs, prob)]
        prob_curve = VMobject(color=TERRA, stroke_width=4)
        prob_curve.set_points_smoothly(prob_pts)
        prob_fill_pts = [[x, p / prob_max * 1.5 - 2.5, 0] for x, p in zip(xs, prob)]
        ax_wave = Line([-6.5, 1.0, 0], [6.5, 1.0, 0], color=INK, stroke_width=2)
        ax_prob = Line([-6.5, -2.5, 0], [6.5, -2.5, 0], color=INK, stroke_width=2)
        wave_lbl = ink_txt("ψ(x)", size=26)
        wave_lbl.move_to([-5.5, 1.5, 0])
        prob_lbl = terra_txt("|ψ|²(x)", size=26)
        prob_lbl.move_to([-5.5, -2.0, 0])
        sep = DashedLine([-6.5, -0.5, 0], [6.5, -0.5, 0], color=INK, stroke_width=1, dash_length=0.2)
        self.add(ax_wave, ax_prob, sep, wave, wave_lbl)
        self.play(Create(prob_curve), FadeIn(prob_lbl), run_time=0.8)
        self.wait(max(0.1, dur - 0.8))


class A08_OneMomentumEverywhere(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        xs = np.linspace(-6.5, 6.5, 600)
        # Left: plane wave (one momentum)
        plane_pts = [[x, np.cos(2.5 * x) * 1.0 + 1.5, 0] for x in xs]
        plane = VMobject(color=INK, stroke_width=3)
        plane.set_points_smoothly(plane_pts)
        flat = Line([-6.5, 0.2, 0], [6.5, 0.2, 0], color=TERRA, stroke_width=4)
        ax_left = Line([-6.5, 0.2, 0], [6.5, 0.2, 0], color=INK, stroke_width=2)
        one_lbl = ink_txt("one momentum", size=26)
        one_lbl.move_to([0, 3.0, 0])
        every_lbl = terra_txt("everywhere", size=26)
        every_lbl.move_to([0, -0.5, 0])
        vs_lbl = terra_txt("vs.", size=36)
        vs_lbl.move_to([0, -1.5, 0])
        # Right packet
        k0 = 2.5; dk = 0.8
        ks = np.linspace(k0 - 2*dk, k0 + 2*dk, 50)
        weights = np.exp(-0.5 * ((ks - k0)/dk)**2)
        ys2 = sum(w * np.cos(k * xs) for w, k in zip(weights, ks))
        ys2 = ys2 / np.max(np.abs(ys2)) * 1.0
        pack_pts = [[x, y - 2.8, 0] for x, y in zip(xs, ys2)]
        pack = VMobject(color=INK, stroke_width=3)
        pack.set_points_smoothly(pack_pts)
        ax_pack = Line([-6.5, -2.8, 0], [6.5, -2.8, 0], color=INK, stroke_width=2)
        many_lbl = ink_txt("many momenta → a place", size=26)
        many_lbl.move_to([0, -4.2, 0])
        label = terra_txt("one momentum: everywhere\na place needs many", size=36)
        label.move_to([0, 0.0, 0])
        self.play(Write(label), run_time=1.0)
        self.wait(max(0.1, dur - 1.0))
