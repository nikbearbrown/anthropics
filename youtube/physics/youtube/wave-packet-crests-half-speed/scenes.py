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

# Shared wave-packet helper
def packet_y(xs, x_center, k0=3.0, sigma=1.5, amp=1.0):
    envelope = np.exp(-0.5 * ((xs - x_center) / sigma) ** 2)
    ripple = np.cos(k0 * (xs - x_center))
    return amp * envelope * ripple


class INTRO_Title(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("INTRO", 5.0)
        title = ink_txt("Wave-Packet Crests\nRun at Half Speed", size=54)
        title.move_to(ORIGIN)
        sub = terra_txt("v_phase = v/2    v_group = v", size=34)
        sub.next_to(title, DOWN, buff=0.7)
        bear = ink_txt("Bear's Notes · Quantum Mechanics", size=26)
        bear.next_to(sub, DOWN, buff=0.5)
        self.play(FadeIn(title), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.play(FadeIn(bear), run_time=0.4)
        self.wait(max(0.1, dur - 1.6))


class H01_RipplingBlob(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H01", 5.0)
        lbl = ink_txt("A rippling blob\nglides past…", size=40)
        lbl.to_edge(LEFT, buff=0.8)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.3
        # Animate packet moving right
        center_tracker = ValueTracker(-3.0)
        packet = always_redraw(lambda: VMobject(
            color=INK, stroke_width=3
        ).set_points_smoothly(
            [[x, baseline_y + packet_y(xs, center_tracker.get_value())[i], 0]
             for i, x in enumerate(xs)]
        ))
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(axis, packet)
        self.play(FadeIn(lbl), run_time=0.5)
        self.play(center_tracker.animate.set_value(3.0),
                  run_time=min(dur - 0.5, 4.0), rate_func=linear)
        self.wait(max(0.1, dur - 4.5))


class H02_DoubleTake(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("H02", 5.0)
        lbl = ink_txt("Wait — the ripples\nslip backward inside!", size=40)
        lbl.to_edge(LEFT, buff=0.8)
        # Show packet moving right, crests moving at half speed (appear to shift)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.3
        group_tracker = ValueTracker(-2.0)
        phase_tracker = ValueTracker(-2.0)
        def make_packet():
            xc = group_tracker.get_value()
            xp = phase_tracker.get_value()
            env = np.exp(-0.5 * ((xs - xc) / 1.5) ** 2)
            ripple = np.cos(3.0 * (xs - xp))
            ys = env * ripple * 1.0
            pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
            return VMobject(color=INK, stroke_width=3).set_points_smoothly(pts)
        packet = always_redraw(make_packet)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        surprise_lbl = terra_txt("?!", size=60)
        surprise_lbl.to_edge(RIGHT, buff=1.0)
        self.add(axis, packet)
        self.play(FadeIn(lbl), FadeIn(surprise_lbl), run_time=0.5)
        # Group moves right at v, phase at v/2
        self.play(
            group_tracker.animate.set_value(2.0),
            phase_tracker.animate.set_value(0.0),  # half the group displacement
            run_time=min(dur - 0.5, 4.0), rate_func=linear
        )
        self.wait(max(0.1, dur - 4.5))


class A01_StaticPacket(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A01", 5.0)
        title = ink_txt("Gaussian envelope + internal crests", size=34)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.2
        ys = packet_y(xs, 0.0, k0=3.5, sigma=2.0, amp=1.2)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        # Envelope outline
        env = 1.2 * np.exp(-0.5 * (xs / 2.0) ** 2)
        env_pts = [[x, baseline_y + y, 0] for x, y in zip(xs, env)]
        neg_env_pts = [[x, baseline_y - y, 0] for x, y in zip(xs, env)]
        env_curve = VMobject(color=TERRA, stroke_width=2, stroke_opacity=0.7)
        env_curve.set_points_smoothly(env_pts)
        neg_env_curve = VMobject(color=TERRA, stroke_width=2, stroke_opacity=0.7)
        neg_env_curve.set_points_smoothly(neg_env_pts)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        env_lbl = terra_txt("envelope", size=26)
        env_lbl.move_to([3.5, baseline_y + 1.8, 0])
        crest_lbl = ink_txt("crests", size=26)
        crest_lbl.move_to([-3.5, baseline_y - 1.5, 0])
        self.add(title, axis)
        self.play(Create(wave), run_time=0.6)
        self.play(Create(env_curve), Create(neg_env_curve), run_time=0.4)
        self.play(FadeIn(env_lbl), FadeIn(crest_lbl), run_time=0.4)
        self.wait(max(0.1, dur - 1.4))


class A02_PacketMoving(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A02", 5.0)
        title = ink_txt("The packet drifts right (group velocity)", size=32)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.2
        center = ValueTracker(-2.5)
        packet = always_redraw(lambda: VMobject(
            color=INK, stroke_width=3
        ).set_points_smoothly(
            [[x, baseline_y + packet_y(xs, center.get_value())[i], 0]
             for i, x in enumerate(xs)]
        ))
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        arrow = always_redraw(lambda: Arrow(
            [center.get_value() - 0.5, baseline_y - 1.5, 0],
            [center.get_value() + 0.5, baseline_y - 1.5, 0],
            color=INK, buff=0, stroke_width=4
        ))
        vg_lbl = ink_txt("v_g = p/m", size=28)
        vg_lbl.move_to([0, baseline_y - 2.3, 0])
        self.add(title, axis, packet, arrow, vg_lbl)
        self.play(center.animate.set_value(2.5),
                  run_time=min(dur - 0.3, 5.0), rate_func=linear)
        self.wait(max(0.1, dur - 5.3))


class A03_CrestDot(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A03", 5.0)
        title = ink_txt("Red dot tracks one crest", size=32)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.2
        k0 = 3.5
        group_v = 2.0   # arbitrary units
        phase_v = 1.0   # = v_p = v_g / 2
        t = ValueTracker(0.0)
        def get_packet():
            tc = t.get_value()
            xc = -2.0 + group_v * tc  # group center
            xp_shift = phase_v * tc   # phase displacement
            env = np.exp(-0.5 * ((xs - xc) / 2.0) ** 2)
            ripple = np.cos(k0 * (xs - xp_shift))
            ys = 1.2 * env * ripple
            pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
            return VMobject(color=INK, stroke_width=3).set_points_smoothly(pts)
        def get_crest_pos():
            tc = t.get_value()
            return [-2.0 + group_v * tc - 2 * PI / k0 * 0.0
                    + phase_v * tc, baseline_y + 1.2, 0]
        packet = always_redraw(get_packet)
        crest_dot = always_redraw(lambda: Dot(
            [-2.0 + phase_v * t.get_value(), baseline_y + 0.8, 0],
            radius=0.2, color=TERRA
        ))
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(title, axis, packet, crest_dot)
        self.play(t.animate.set_value(1.8),
                  run_time=min(dur - 0.3, 3.5), rate_func=linear)
        self.wait(max(0.1, dur - 3.8))


class A04_SpeedLegend(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A04", 5.0)
        # Static packet
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = 0.8
        ys = packet_y(xs, 0.0, k0=3.5, sigma=1.8, amp=1.0)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(axis, wave)
        # Long envelope arrow = v_group
        env_arrow = Arrow([-1.5, -1.0, 0], [4.5, -1.0, 0],
                          color=INK, buff=0, stroke_width=5)
        env_lbl = ink_txt("v_group = p/m", size=28)
        env_lbl.next_to(env_arrow, DOWN, buff=0.2)
        # Short crest arrow = v_phase (half length)
        crest_arrow = Arrow([-1.5, -2.5, 0], [1.5, -2.5, 0],
                            color=INK, buff=0, stroke_width=5)
        crest_lbl = ink_txt("v_phase = p/2m = v/2", size=28)
        crest_lbl.next_to(crest_arrow, DOWN, buff=0.2)
        self.play(Create(env_arrow), FadeIn(env_lbl), run_time=0.6)
        self.play(Create(crest_arrow), FadeIn(crest_lbl), run_time=0.5)
        self.wait(max(0.1, dur - 1.1))


class A05_CrestFallsBehind(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A05", 5.0)
        title = ink_txt("Crest falls toward the back of envelope", size=32)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.3
        group_v = 2.0; phase_v = 1.0
        t = ValueTracker(0.0)
        def get_packet():
            tc = t.get_value()
            xc = -1.5 + group_v * tc
            xp_shift = phase_v * tc
            env = np.exp(-0.5 * ((xs - xc) / 2.0) ** 2)
            ripple = np.cos(3.5 * (xs - xp_shift))
            ys = 1.0 * env * ripple
            pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
            return VMobject(color=INK, stroke_width=3).set_points_smoothly(pts)
        def get_env_center():
            return [-1.5 + group_v * t.get_value(), baseline_y, 0]
        def get_crest_center():
            return [-1.5 + phase_v * t.get_value(), baseline_y + 0.9, 0]
        packet = always_redraw(get_packet)
        env_dot = always_redraw(lambda: Dot(get_env_center(), radius=0.18, color=INK))
        crest_dot = always_redraw(lambda: Dot(get_crest_center(), radius=0.2, color=TERRA))
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        crest_lbl = ink_txt("crest", size=36)
        crest_lbl.move_to([-1.5, baseline_y + 1.5, 0])
        env_lbl = ink_txt("envelope center", size=36)
        env_lbl.move_to([-1.5, baseline_y - 1.0, 0])
        self.add(title, axis, packet, crest_dot, env_dot)
        self.play(FadeIn(crest_lbl), FadeIn(env_lbl), run_time=0.3)
        self.play(t.animate.set_value(1.8),
                  run_time=min(dur - 0.3, 4.0), rate_func=linear)
        self.wait(max(0.1, dur - 4.3))


class A06_CrestsBornAndFade(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A06", 5.0)
        title = ink_txt("Crests born at front, fade at rear", size=34)
        title.to_edge(UP, buff=0.6)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = -0.3
        group_v = 2.5; phase_v = 1.25
        t = ValueTracker(0.0)
        def get_packet():
            tc = t.get_value()
            xc = -2.0 + group_v * tc
            env = np.exp(-0.5 * ((xs - xc) / 2.0) ** 2)
            ripple = np.cos(3.5 * (xs - phase_v * tc))
            ys = 1.0 * env * ripple
            pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
            return VMobject(color=INK, stroke_width=3).set_points_smoothly(pts)
        packet = always_redraw(get_packet)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        front_arrow = terra_txt("← born", size=22)
        rear_arrow = ink_txt("fade →", size=22)
        front_arrow.move_to([2.5, baseline_y + 1.8, 0])
        rear_arrow.move_to([-2.5, baseline_y - 1.5, 0])
        self.add(title, axis, packet, front_arrow, rear_arrow)
        self.play(t.animate.set_value(1.7),
                  run_time=min(dur - 0.2, 3.9), rate_func=linear)
        self.wait(max(0.1, dur - 4.1))


class A07_VelocityLabels(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A07", 5.0)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = 0.5
        group_v = 2.0; phase_v = 1.0
        t = ValueTracker(0.0)
        def get_packet():
            tc = t.get_value()
            xc = -2.0 + group_v * tc
            env = np.exp(-0.5 * ((xs - xc) / 2.0) ** 2)
            ripple = np.cos(3.5 * (xs - phase_v * tc))
            ys = 1.0 * env * ripple
            pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
            return VMobject(color=INK, stroke_width=3).set_points_smoothly(pts)
        def get_env_tip():
            xc = -2.0 + group_v * t.get_value()
            return [xc, baseline_y + 1.0, 0]
        def get_crest_pos():
            return [-2.0 + phase_v * t.get_value(), baseline_y + 1.0, 0]
        packet = always_redraw(get_packet)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        # Static labels below
        phase_lbl = ink_txt("phase velocity  v_p = p/2m", size=28)
        phase_lbl.move_to([-2.0, -1.5, 0])
        group_lbl = ink_txt("group velocity  v_g = p/m", size=28)
        group_lbl.move_to([2.5, -2.8, 0])
        self.add(axis, packet)
        self.play(FadeIn(phase_lbl), run_time=0.5)
        self.play(FadeIn(group_lbl), run_time=0.5)
        self.play(t.animate.set_value(1.5),
                  run_time=min(dur - 1.0, 4.0), rate_func=linear)
        self.wait(max(0.1, dur - 5.0))


class A08_EnvelopeIsParticle(Scene):
    def construct(self):
        self.camera.background_color = CREAM
        self.add(bg())
        dur = d("A08", 5.0)
        xs = np.linspace(-6.5, 6.5, 500)
        baseline_y = 0.5
        ys = packet_y(xs, 0.5, k0=3.5, sigma=2.0, amp=1.1)
        pts = [[x, baseline_y + y, 0] for x, y in zip(xs, ys)]
        wave = VMobject(color=INK, stroke_width=3)
        wave.set_points_smoothly(pts)
        # Highlight envelope
        env = 1.1 * np.exp(-0.5 * ((xs - 0.5) / 2.0) ** 2)
        env_pts = [[x, baseline_y + y, 0] for x, y in zip(xs, env)]
        neg_env_pts = [[x, baseline_y - y, 0] for x, y in zip(xs, env)]
        env_curve = VMobject(color=TERRA, stroke_width=4)
        env_curve.set_points_smoothly(env_pts)
        neg_env_curve = VMobject(color=TERRA, stroke_width=4)
        neg_env_curve.set_points_smoothly(neg_env_pts)
        axis = Line([-6.5, baseline_y, 0], [6.5, baseline_y, 0], color=INK, stroke_width=2)
        self.add(axis, wave, env_curve, neg_env_curve)
        label = ink_txt("the envelope IS the particle", size=42)
        label.move_to([0, -1.8, 0])
        sub = ink_txt("v_group = p/m = v (particle speed)\nv_phase = p/2m = v/2", size=26)
        sub.move_to([0, -3.3, 0])
        underline = Line(label.get_left() + DOWN * 0.08,
                         label.get_right() + DOWN * 0.08,
                         color=TERRA, stroke_width=3)
        self.play(Write(label), run_time=0.8)
        self.play(Create(underline), run_time=0.3)
        self.play(FadeIn(sub), run_time=0.4)
        self.wait(max(0.1, dur - 1.5))
