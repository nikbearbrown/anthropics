"""Manim scenes — claude-liam-the-missing-feedback-loop
Deep-explainer: Anthropic's Model Hardware Standard — what the loop proves.
Palette: claude stage — cream #FAF9F5, ink #3D3929, terracotta #D55E00-free zone:
terracotta #D97757, mute #8B7355.

LAYOUT LAW (Simon's Ant post-mortem):
  - No hardcoded move_to([x, y, 0]); use next_to() / arrange() / to_edge() / shift().
  - Rows/columns: VGroup(...).arrange(DIR, buff=N).
  - Text inside a box: width derived from the box.
  - bbox-overlap assertion (check_overlaps) at end of every construct(),
    including EVERY visible label.

STAGE LAYOUT LAW: subject operating LEFT, ledger/numbers updating RIGHT,
causally synced.
"""
from manim import *
import numpy as np

# ── palette ──────────────────────────────────────────────────────────────────
CREAM = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"
MUTE  = "#8B7355"
GRAY  = "#A89F91"

config.background_color = CREAM
config.frame_rate        = 24
# Render size is the RENDER TARGET, not a constant. Hardcoding 1080 here silently
# overrode manim's -qk flag, so every "4K" master shipped upscaled 1080 Manim
# (caught by post's per-beat 4K audit, 2026-08-31). Stage/final renders set
# ART_MANIM_H=2160 ART_MANIM_W=3840.
import os
config.pixel_height      = int(os.environ.get("ART_MANIM_H", "1080"))
config.pixel_width       = int(os.environ.get("ART_MANIM_W", "1920"))


# ── helpers ──────────────────────────────────────────────────────────────────
def _t(text, size=34, color=INK, **kw):
    # Pango space-collapse fix (this Mac): double every space — doubles render
    # at normal single-space width; singles sometimes render at zero width.
    return Text(text.replace(" ", "  "), color=color, font_size=size,
                font="EB Garamond", **kw)

def _mono(text, size=22, color=MUTE, **kw):
    # Menlo never collapses spaces — do NOT double them (doubling trips the
    # GATE T kerning check with real double-wide gaps).
    return Text(text, color=color, font_size=size, font="Menlo", **kw)

def _box(content, h_pad=0.28, v_pad=0.20, stroke=INK, sw=2.0, fill=CREAM,
         corner=0.12):
    r = RoundedRectangle(
        corner_radius=corner,
        width=content.width + 2 * h_pad,
        height=content.height + 2 * v_pad,
        color=stroke, stroke_width=sw, fill_color=fill, fill_opacity=1
    )
    r.move_to(content)
    return VGroup(r, content)

def _rule_floor(scene):
    r = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
    r.set_stroke(color=INK, width=2.0, opacity=0.30)
    r.to_edge(DOWN, buff=0.53)
    scene.add(r)
    return r

def check_overlaps(*mobs, margin=0.12, label=""):
    def _bb(m):
        return (m.get_left()[0], m.get_bottom()[1], m.get_right()[0], m.get_top()[1])
    bbs = [(m, _bb(m)) for m in mobs]
    viol = []
    for i, (ma, (la, ba, ra, ta)) in enumerate(bbs):
        for j, (mb, (lb, bb_y, rb, tb)) in enumerate(bbs):
            if j <= i:
                continue
            if la < rb + margin and ra > lb - margin and ba < tb + margin and ta > bb_y - margin:
                viol.append(f"  mob[{i}] × mob[{j}]")
    tag = f"[BBOX {label}]" if label else "[BBOX]"
    if viol:
        print(f"{tag} {len(viol)} overlap(s):\n" + "\n".join(viol))
    else:
        print(f"{tag} OK")


def _cycle(labels, center, r=1.55, box_size=24):
    """Four labelled boxes OUTSIDE a circle + the circle path (the dot's track
    stays clear of the labels — GATE T reads dot-over-text as an overlap)."""
    circ = Circle(radius=r, color=INK, stroke_width=2.0, stroke_opacity=0.5)
    circ.move_to(center)
    angles = [PI / 2, 0, -PI / 2, PI]          # top, right, bottom, left
    boxes = VGroup()
    for lbl, a in zip(labels, angles):
        b = _box(_t(lbl, size=box_size), h_pad=0.22, v_pad=0.14)
        direction = np.array([np.cos(a), np.sin(a), 0])
        b.move_to(circ.get_center() + direction * (r + 0.62))
        boxes.add(b)
    return circ, boxes


def _ledger(rows, row_size=24, key_color=MUTE, buff=0.34, key_w=None):
    """rows: list of (key, value_mobject-or-str). Returns VGroup of row VGroups."""
    out = VGroup()
    for k, v in rows:
        key = _t(k, size=row_size, color=key_color)
        val = v if isinstance(v, Mobject) else _t(str(v), size=row_size)
        row = VGroup(key, val).arrange(RIGHT, buff=0.35)
        out.add(row)
    out.arrange(DOWN, buff=buff, aligned_edge=LEFT)
    return out


# ── B02_TheLoopRuns  (12.63 s) ───────────────────────────────────────────────
class B02_TheLoopRuns(Scene):
    """The software loop spins; the ledger counts its laps at zero cost."""

    def construct(self):
        _rule_floor(self)
        center_l = LEFT * 3.0 + UP * 0.3

        circ, boxes = _cycle(["WRITE", "RUN", "OBSERVE", "REVISE"], center_l,
                             r=1.45)
        self.play(Create(circ), run_time=0.8)
        self.play(LaggedStart(*[FadeIn(b) for b in boxes], lag_ratio=0.2),
                  run_time=1.0)

        # ledger, right
        theta = ValueTracker(PI / 2)
        laps = Integer(0, color=INK, font_size=44)
        laps.add_updater(lambda m: m.set_value(int((theta.get_value() - PI / 2) / TAU)))
        cost = _t("$0", size=28)
        verdict = _t("PASS", size=28)

        def _verdict_upd(m):
            even = int((theta.get_value() - PI / 2) / PI) % 2 == 0
            p = m.get_center()
            m.become(_t("PASS" if even else "FAIL", size=28,
                        color=INK if even else GRAY).move_to(p))
        verdict.add_updater(_verdict_upd)
        led = _ledger([("ITERATIONS", laps), ("COST", cost), ("VERDICT", verdict)],
                      row_size=26, buff=0.5)
        led_box = SurroundingRectangle(led, color=INK, stroke_width=2.0, buff=0.42,
                                       corner_radius=0.12)
        led_grp = VGroup(led_box, led)
        led_grp.move_to(RIGHT * 3.6 + UP * 0.3)
        self.play(FadeIn(led_box), FadeIn(led), run_time=0.8)

        # the dot spins; counter follows
        dot = Dot(color=TERRA, radius=0.11)
        dot.add_updater(lambda m: m.move_to(circ.point_at_angle(theta.get_value())))
        self.add(dot)
        self.play(theta.animate.increment_value(6 * TAU), run_time=7.4,
                  rate_func=linear)
        dot.clear_updaters()
        laps.clear_updaters()
        verdict.clear_updaters()

        # git revert chip
        chip = _box(_mono("git revert", size=22, color=INK), h_pad=0.24, v_pad=0.14,
                    sw=1.5)
        chip.next_to(led_grp, DOWN, buff=0.4)
        self.play(FadeIn(chip, shift=UP * 0.2), run_time=0.6)
        self.wait(0.9)
        check_overlaps(circ, *boxes, led_grp, chip, label="B02")


# ── B03_SameLoopThroughAtoms  (14.10 s) ──────────────────────────────────────
class B03_SameLoopThroughAtoms(Scene):
    """Two loops, one fast one grinding; the paired ledger's rollback cell is empty."""

    def construct(self):
        _rule_floor(self)

        code_c = Circle(radius=0.95, color=INK, stroke_width=2.0, stroke_opacity=0.5)
        atom_c = Circle(radius=0.95, color=INK, stroke_width=2.0, stroke_opacity=0.5)
        pair = VGroup(code_c, atom_c).arrange(RIGHT, buff=1.1)
        pair.move_to(LEFT * 3.7 + UP * 0.9)
        code_lbl = _t("CODE", size=24).next_to(code_c, DOWN, buff=0.28)
        atom_lbl = _t("ATOMS", size=24).next_to(atom_c, DOWN, buff=0.28)
        self.play(Create(code_c), Create(atom_c), FadeIn(code_lbl), FadeIn(atom_lbl),
                  run_time=1.2)

        th_c = ValueTracker(PI / 2)
        th_a = ValueTracker(PI / 2)
        d_c = Dot(color=TERRA, radius=0.09)
        d_a = Dot(color=TERRA, radius=0.09)
        d_c.add_updater(lambda m: m.move_to(code_c.point_at_angle(th_c.get_value())))
        d_a.add_updater(lambda m: m.move_to(atom_c.point_at_angle(th_a.get_value())))
        self.add(d_c, d_a)

        # ledger, right — pairwise rows
        hdr_s = _t("SOFTWARE", size=24, color=MUTE)
        hdr_p = _t("PHYSICAL", size=24, color=MUTE)
        pairs = [
            ("execution", "actuation"),
            ("test output", "sensor reading"),
            ("compiler error", "silent fault"),
        ]
        col_s = VGroup(hdr_s, *[_t(a, size=24) for a, _ in pairs])
        col_p = VGroup(hdr_p, *[_t(b, size=24) for _, b in pairs])
        col_s.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        col_p.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        table = VGroup(col_s, col_p).arrange(RIGHT, buff=0.9, aligned_edge=UP)
        table.move_to(RIGHT * 3.3 + UP * 0.9)

        spin = 10.4  # seconds of concurrent dot motion, spread across plays
        self.play(FadeIn(hdr_s), FadeIn(hdr_p),
                  th_c.animate.increment_value(TAU * 1.2),
                  th_a.animate.increment_value(TAU * 0.3),
                  run_time=1.4, rate_func=linear)
        for i in range(3):
            self.play(FadeIn(col_s[i + 1]), FadeIn(col_p[i + 1]),
                      th_c.animate.increment_value(TAU * 1.4),
                      th_a.animate.increment_value(TAU * 0.35),
                      run_time=1.7, rate_func=linear)

        # rollback row — cells aligned under their columns
        rb_s = _mono("git revert", size=22, color=INK)
        rb_p = _t("— none", size=24, color=TERRA)
        rb_s.next_to(col_s[-1], DOWN, buff=0.5)
        rb_s.align_to(col_s, LEFT)
        rb_p.next_to(col_p[-1], DOWN, buff=0.5)
        rb_p.align_to(col_p, LEFT)
        rb_key = _t("rollback", size=20, color=MUTE)
        rb_key.next_to(rb_s, DOWN, buff=0.22)
        rb_key.align_to(col_s, LEFT)
        rb_row = VGroup(rb_s, rb_p, rb_key)
        self.play(FadeIn(rb_row),
                  th_c.animate.increment_value(TAU * 1.4),
                  th_a.animate.increment_value(TAU * 0.3),
                  run_time=1.7, rate_func=linear)

        # atoms dot stalls mid-arc; code dot keeps going
        self.play(th_c.animate.increment_value(TAU * 1.6),
                  th_a.animate.increment_value(TAU * 0.12),
                  run_time=2.0, rate_func=linear)
        d_a.clear_updaters()
        stall = _t("stalled", size=20, color=TERRA).next_to(d_a, UR, buff=0.1)
        self.play(FadeIn(stall),
                  th_c.animate.increment_value(TAU * 1.2),
                  run_time=1.5, rate_func=linear)
        d_c.clear_updaters()
        self.wait(1.2)
        check_overlaps(code_c, atom_c, code_lbl, atom_lbl, table, rb_row, stall,
                       label="B03")


# ── B08_OneLevelDown  (15.23 s) ──────────────────────────────────────────────
class B08_OneLevelDown(Scene):
    """Bespoke glue collapses into one driver bus; the ledger prices N×M → N+M."""

    def construct(self):
        _rule_floor(self)

        agent = _box(_t("AGENT", size=26), h_pad=0.3, v_pad=0.18)
        agent.move_to(LEFT * 2.9 + UP * 2.3)
        devices = VGroup(*[
            _box(_t(n, size=18), h_pad=0.12, v_pad=0.1, sw=1.5)
            for n in ["MICROSCOPE", "LIQUID HANDLER", "ARM", "LASER"]
        ]).arrange(RIGHT, buff=0.18)
        devices.move_to(LEFT * 2.9 + DOWN * 1.8)
        # Title-safe clamp: the row must stay inside the 90% box (|x| <= 6.1).
        # Bigger labels (the 41px floor at 2160) widened it past the edge.
        if devices.width > 11.2:
            devices.scale(11.2 / devices.width)
        devices.move_to(LEFT * 2.9 + DOWN * 1.8)
        if devices.get_left()[0] < -6.1:
            devices.shift(RIGHT * (-6.1 - devices.get_left()[0]))
        self.play(FadeIn(agent), LaggedStart(*[FadeIn(d) for d in devices],
                                             lag_ratio=0.15), run_time=1.3)

        # the tangle: bezier glue lines, deliberately crossing
        tangle = VGroup()
        offs = [1.6, -1.2, 0.9, -1.7]
        for d, off in zip(devices, offs):
            p0 = agent.get_bottom() + DOWN * 0.05
            p3 = d.get_top() + UP * 0.05
            mid = (p0 + p3) / 2 + RIGHT * off
            path = CubicBezier(p0, p0 + DOWN * 0.9 + RIGHT * off, mid, p3,
                               color=GRAY, stroke_width=2.5)
            tangle.add(path)
        glue = _t("custom glue, per pair", size=20, color=MUTE)
        glue.next_to(tangle, RIGHT, buff=0.25)
        self.play(LaggedStart(*[Create(p) for p in tangle], lag_ratio=0.2),
                  FadeIn(glue), run_time=1.9)
        self.wait(0.7)

        # collapse into one bus through a DRIVER band
        band = RoundedRectangle(corner_radius=0.1, width=devices.width + 0.3,
                                height=0.62, color=INK, stroke_width=2.0,
                                fill_color=CREAM, fill_opacity=1)
        band.move_to(VGroup(agent, devices).get_center())
        band_lbl = _t("DRIVER", size=24).move_to(band)
        trunk = Line(agent.get_bottom() + DOWN * 0.05, band.get_top() + UP * 0.02,
                     color=INK, stroke_width=3.0)
        drops = VGroup(*[
            Line(np.array([d.get_top()[0], band.get_bottom()[1], 0]) + DOWN * 0.02,
                 d.get_top() + UP * 0.02, color=INK, stroke_width=2.5)
            for d in devices
        ])
        self.play(FadeOut(tangle), FadeOut(glue), run_time=0.9)
        self.play(FadeIn(band), FadeIn(band_lbl), Create(trunk), run_time=1.1)
        self.play(LaggedStart(*[Create(l) for l in drops], lag_ratio=0.15),
                  run_time=1.0)

        # ledger, right
        hdr = _t("4 devices · 3 agents", size=22, color=MUTE)
        r1 = VGroup(_t("BESPOKE", size=24, color=MUTE),
                    _mono("4 × 3 = 12", size=24, color=INK)).arrange(RIGHT, buff=0.45)
        r2 = VGroup(_t("STANDARD", size=24, color=MUTE),
                    _mono("4 + 3 = 7", size=24, color=INK)).arrange(RIGHT, buff=0.45)
        led = VGroup(hdr, r1, r2).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        led_box = SurroundingRectangle(led, color=INK, stroke_width=2.0, buff=0.4,
                                       corner_radius=0.12)
        grp = VGroup(led_box, led)
        grp.move_to(RIGHT * 3.5 + UP * 0.3)
        self.play(FadeIn(led_box), FadeIn(hdr), run_time=0.7)
        self.play(FadeIn(r1), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(r2), run_time=0.8)

        seven = r2[1][-1]
        ring = Line(seven.get_corner(DL) + DOWN * 0.12 + LEFT * 0.15,
                    seven.get_corner(DR) + DOWN * 0.12 + RIGHT * 0.15,
                    color=TERRA, stroke_width=4.0)
        ring._qc_intentional = True
        self.play(Create(ring), run_time=0.7)
        self.wait(2.2)
        check_overlaps(agent, devices, band, band_lbl, grp, label="B08")


# ── B10_TheFloorBelowTheModel  (14.63 s) ─────────────────────────────────────
class B10_TheFloorBelowTheModel(Scene):
    """The driver band stops the 7.0 V command; the manifest names its author."""

    def construct(self):
        _rule_floor(self)

        bands = VGroup(*[
            VGroup(
                RoundedRectangle(corner_radius=0.1, width=4.2, height=0.95,
                                 color=INK, stroke_width=sw, fill_color=CREAM,
                                 fill_opacity=1),
                _t(n, size=22)
            ) for n, sw in [("AGENT — proposes", 2.0),
                            ("DRIVER — enforces", 3.5),
                            ("DEVICE — acts", 2.0)]
        ])
        for b in bands:
            b[1].move_to(b[0])
        bands.arrange(DOWN, buff=0.85)
        bands.move_to(LEFT * 2.7 + UP * 0.2)
        self.play(LaggedStart(*[FadeIn(b) for b in bands], lag_ratio=0.25),
                  run_time=1.4)

        agent_b, driver_b, device_b = bands

        # arrow 1: 7.0 V — dies at the driver
        a1_start = agent_b.get_bottom() + LEFT * 1.1 + DOWN * 0.05
        a1_end = np.array([a1_start[0], driver_b.get_top()[1] + 0.06, 0])
        a1 = Arrow(a1_start, a1_end, color=INK, stroke_width=3.0, tip_length=0.16,
                   buff=0)
        a1_lbl = _mono("write 7.0 V", size=18, color=INK).next_to(a1, LEFT, buff=0.12)
        self.play(GrowArrow(a1), FadeIn(a1_lbl), run_time=0.9)
        x1 = Cross(stroke_color=TERRA, stroke_width=5.0, scale_factor=0.16)
        x1.move_to(a1_end + DOWN * 0.05)
        x1._qc_intentional = True
        lim = _mono("[0, 5.0]", size=18, color=TERRA)
        lim.next_to(a1_lbl, DOWN, buff=0.18)
        lim.align_to(a1_lbl, LEFT)
        self.play(Create(x1), FadeIn(lim), run_time=0.8)
        self.wait(0.8)

        # arrow 2: 3.2 V — passes through to the device
        a2_start = agent_b.get_bottom() + RIGHT * 1.7 + DOWN * 0.05
        a2_end = np.array([a2_start[0], device_b.get_top()[1] + 0.06, 0])
        a2 = Arrow(a2_start, a2_end, color=INK, stroke_width=3.0, tip_length=0.16,
                   buff=0)
        a2_lbl = _mono("write 3.2 V", size=18, color=INK)
        a2_lbl.next_to(a2_start + DOWN * 0.28, RIGHT, buff=0.16)
        self.play(GrowArrow(a2), FadeIn(a2_lbl), run_time=1.1)
        self.play(Indicate(device_b, color=INK, scale_factor=1.04), run_time=0.8)

        # manifest table, right
        rows = VGroup(
            _mono("measurable:  [...]", size=21, color=INK),
            _mono("adjustable:  [...]", size=21, color=INK),
            _mono("safety_limits: {…}", size=21, color=INK),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        m_box = SurroundingRectangle(rows, color=INK, stroke_width=2.0, buff=0.38,
                                     corner_radius=0.12)
        m_title = _t("the manifest", size=22, color=MUTE).next_to(m_box, UP, buff=0.2)
        man = VGroup(m_box, rows, m_title)
        man.move_to(RIGHT * 3.9 + UP * 0.9)
        self.play(FadeIn(man), run_time=1.0)

        hl = SurroundingRectangle(rows[2], color=TERRA, stroke_width=3.0, buff=0.1)
        hl._qc_intentional = True
        self.play(Create(hl), run_time=0.7)
        pen = _t("✎", size=34, color=TERRA)
        pen_lbl = _t("written by a person", size=22, color=INK)
        pen_grp = VGroup(pen, pen_lbl).arrange(RIGHT, buff=0.22)
        pen_grp.next_to(m_box, DOWN, buff=0.45)
        self.play(FadeIn(pen_grp, shift=UP * 0.15), run_time=0.9)
        self.wait(2.4)
        check_overlaps(bands, a1_lbl, a2_lbl, lim, man, pen_grp, label="B10")


# ── B14_TheBaseline  (13.82 s) ───────────────────────────────────────────────
class B14_TheBaseline(Scene):
    """The linear script marches its fixed steps; the ledger halts at 58%."""

    def construct(self):
        _rule_floor(self)

        steps = VGroup(*[
            _box(_t(f"STEP {i+1}", size=22), h_pad=0.14, v_pad=0.11, sw=1.5)
            for i in range(4)
        ]).arrange(RIGHT, buff=0.45)
        steps.move_to(LEFT * 3.4 + UP * 2.1)
        arrows = VGroup(*[
            Arrow(steps[i].get_right(), steps[i + 1].get_left(), color=INK,
                  stroke_width=2.0, tip_length=0.13, buff=0.06)
            for i in range(3)
        ])
        chain_lbl = _t("one path, no branches", size=22, color=MUTE)
        chain_lbl.next_to(steps, UP, buff=0.3)
        self.play(FadeIn(steps), Create(arrows), FadeIn(chain_lbl), run_time=1.3)

        dot = Dot(color=TERRA, radius=0.1)
        dot.move_to(steps[0].get_top() + UP * 0.15)
        path = VMobject().set_points_as_corners(
            [s.get_top() + UP * 0.15 for s in steps])
        self.add(dot)

        # ledger right: success bar + rows
        bar_frame = Rectangle(width=0.85, height=2.4, color=INK, stroke_width=2.0)
        bar_h = ValueTracker(0.0)
        bar_fill = always_redraw(lambda: Rectangle(
            width=0.85, height=max(bar_h.get_value(), 0.01) * 2.4,
            color=INK, fill_color=INK, fill_opacity=0.55, stroke_width=0
        ).align_to(bar_frame, DOWN).align_to(bar_frame, LEFT))
        pct = always_redraw(lambda: _t(f"{round(bar_h.get_value()*100)}%", size=26)
                            .next_to(bar_frame, UP, buff=0.16))
        bar_lbl = _t("SUCCESS", size=24, color=MUTE).next_to(bar_frame, DOWN, buff=0.2)
        bar_grp_anchor = VGroup(bar_frame, bar_lbl)
        rows = _ledger([
            ("TIME / ATTEMPT", _mono("150 s", size=26, color=INK)),
            ("TEAM", _t("four engineers", size=28)),
            ("BUILD", _t("several months", size=28)),
        ], row_size=24, buff=0.42)
        right = VGroup(bar_grp_anchor, rows).arrange(RIGHT, buff=0.9,
                                                     aligned_edge=DOWN)
        right.move_to(RIGHT * 3.3 + DOWN * 1.0)
        if right.get_right()[0] > 6.1:
            right.shift(LEFT * (right.get_right()[0] - 6.1))
        self.add(bar_fill, pct)
        self.play(FadeIn(bar_frame), FadeIn(bar_lbl), run_time=0.7)

        # dot marches twice while the ledger fills
        self.play(MoveAlongPath(dot, path), bar_h.animate.set_value(0.30),
                  FadeIn(rows[0]), run_time=2.3, rate_func=linear)
        dot.move_to(steps[0].get_top() + UP * 0.15)
        self.play(MoveAlongPath(dot, path), bar_h.animate.set_value(0.58),
                  FadeIn(rows[1]), FadeIn(rows[2]), run_time=2.3, rate_func=linear)

        # the ceiling
        ceil_y = bar_frame.get_bottom() + UP * 0.58 * 2.4
        ceiling = Line(bar_frame.get_left() + LEFT * 0.35, bar_frame.get_right() +
                       RIGHT * 0.35, color=TERRA, stroke_width=3.0)
        ceiling.move_to(np.array([bar_frame.get_center()[0], ceil_y[1], 0]))
        ceiling._qc_intentional = True
        ceil_lbl = _t("a ceiling", size=24, color=TERRA)
        ceil_lbl.next_to(ceiling, RIGHT, buff=0.2)
        self.play(Create(ceiling), FadeIn(ceil_lbl), run_time=0.9)
        self.wait(2.2)
        check_overlaps(steps, chain_lbl, bar_frame, bar_lbl, rows, ceil_lbl,
                       pct, label="B14")


# ── B15_TheLoopWithPhotons  (14.02 s) ────────────────────────────────────────
class B15_TheLoopWithPhotons(Scene):
    """Act one's loop, relabeled for the rig; attempts climb through the night."""

    def construct(self):
        _rule_floor(self)
        center_l = LEFT * 2.9 + UP * 0.35

        circ, boxes = _cycle(["INDUCE", "RECOVER", "MEASURE", "REVISE"], center_l,
                             r=1.45, box_size=22)
        self.play(Create(circ), LaggedStart(*[FadeIn(b) for b in boxes],
                                            lag_ratio=0.18), run_time=1.4)

        # four role sparks at the diagonals
        roles = ["planner", "operator", "analyst", "critic"]
        diag = [UR, DR, DL, UL]
        sparks = VGroup()
        for r_name, d in zip(roles, diag):
            s = Square(side_length=0.17, color=TERRA, fill_color=TERRA,
                       fill_opacity=1, stroke_width=0).rotate(PI / 4)
            tag = _mono(r_name.upper(), size=22, color=MUTE)
            g = VGroup(s, tag).arrange(DOWN, buff=0.08)
            g.move_to(circ.get_center() + d * 1.95)
            sparks.add(g)
        self.play(LaggedStart(*[FadeIn(s) for s in sparks], lag_ratio=0.2),
                  run_time=1.1)

        # sabotage tags flash at INDUCE (top box)
        induce = boxes[0]
        tags = ["BEAM BLOCKED", "POWER CUT", "FREQ SHOVED"]
        theta = ValueTracker(PI / 2)
        dot = Dot(color=TERRA, radius=0.1)
        dot.add_updater(lambda m: m.move_to(circ.point_at_angle(theta.get_value())))
        self.add(dot)

        # ledger right
        att = Integer(0, color=INK, font_size=42)
        rate_v = ValueTracker(0.0)
        rate = Integer(0, color=INK, font_size=42)
        rate.add_updater(lambda m: m.set_value(int(rate_v.get_value() * 100)))
        night_frame = Rectangle(width=3.0, height=0.32, color=INK, stroke_width=1.5)
        night_w = ValueTracker(0.0)
        night_fill = always_redraw(lambda: Rectangle(
            width=max(night_w.get_value(), 0.003) * 3.0, height=0.32,
            color=INK, fill_color=INK, fill_opacity=0.4, stroke_width=0
        ).align_to(night_frame, LEFT).align_to(night_frame, DOWN))
        led = _ledger([
            ("ATTEMPTS", att),
            ("NIGHT", night_frame),
            ("RECOVERY / 100", rate),
        ], row_size=24, buff=0.5)
        led_box = SurroundingRectangle(led, color=INK, stroke_width=2.0, buff=0.42,
                                       corner_radius=0.12)
        grp = VGroup(led_box, led)
        grp.move_to(RIGHT * 3.8 + UP * 0.35)
        self.add(night_fill)
        self.play(FadeIn(led_box), FadeIn(led), run_time=0.8)

        att.add_updater(lambda m: m.set_value(int((theta.get_value() - PI / 2)
                                                  / TAU * 45)))
        # spin + tags + climbing numbers
        for i, tg in enumerate(tags):
            t_m = _mono(tg, size=20, color=TERRA).next_to(induce, UP, buff=0.16)
            self.play(FadeIn(t_m),
                      theta.animate.increment_value(TAU * 1.6),
                      rate_v.animate.set_value(0.3 + 0.2 * i),
                      night_w.animate.set_value(0.25 + 0.25 * i),
                      run_time=1.55, rate_func=linear)
            self.play(FadeOut(t_m), theta.animate.increment_value(TAU * 0.5),
                      run_time=0.45, rate_func=linear)
        self.play(theta.animate.increment_value(TAU * 2.2),
                  rate_v.animate.set_value(0.9),
                  night_w.animate.set_value(1.0),
                  run_time=2.4, rate_func=linear)
        dot.clear_updaters()
        att.clear_updaters()
        rate.clear_updaters()
        self.wait(1.5)
        check_overlaps(circ, *boxes, sparks, grp, label="B15")


# ── B17_SevenHundredTrials  (14.63 s) ────────────────────────────────────────
class B17_SevenHundredTrials(Scene):
    """700 cells raster full; five stay terracotta; the ledger counts in sync."""

    FAIL_IDX = {61, 217, 340, 512, 663}

    def construct(self):
        _rule_floor(self)

        n_cols, n_rows = 28, 25   # 700
        cell = 0.155
        rows = VGroup()
        idx = 0
        for r in range(n_rows):
            row = VGroup()
            for c in range(n_cols):
                col = TERRA if idx in self.FAIL_IDX else INK
                sq = Square(side_length=cell * 0.82, color=col, fill_color=col,
                            fill_opacity=0.75, stroke_width=0)
                row.add(sq)
                idx += 1
            row.arrange(RIGHT, buff=cell * 0.18)
            rows.add(row)
        rows.arrange(DOWN, buff=cell * 0.18)
        rows.move_to(LEFT * 3.3 + UP * 0.25)
        grid_lbl = _t("700 blind trials", size=22, color=MUTE)
        grid_lbl.next_to(rows, UP, buff=0.3)
        self.play(FadeIn(grid_lbl), run_time=0.5)

        # ledger right
        rec = Integer(695, color=INK, font_size=40)
        rec_row = VGroup(_t("RECOVERED", size=22, color=MUTE), rec,
                         _t("/ 700", size=24, color=MUTE)).arrange(RIGHT, buff=0.28)
        rec.set_value(0)  # arranged at 3-digit width so '/ 700' never collides
        rate_lbl = VGroup(_t("RATE", size=22, color=MUTE),
                          _t("99.3%", size=32)).arrange(RIGHT, buff=0.35)
        rate_lbl[1].set_opacity(0)
        led_top = VGroup(rec_row, rate_lbl).arrange(DOWN, buff=0.45,
                                                    aligned_edge=LEFT)
        led_top.move_to(RIGHT * 3.6 + UP * 2.1)
        self.play(FadeIn(led_top), run_time=0.5)

        # raster fill synced to counter
        counter = ValueTracker(0)
        rec.add_updater(lambda m: m.set_value(
            min(695, int(counter.get_value() / 700 * 695))))
        self.play(
            LaggedStart(*[FadeIn(row) for row in rows], lag_ratio=0.6),
            counter.animate.set_value(700),
            run_time=5.2, rate_func=linear)
        rec.clear_updaters()
        rec.set_value(695)
        self.play(rate_lbl[1].animate.set_opacity(1), run_time=0.5)

        # latency bars — with an explicit axis break on the human bar
        def lat_bar(label, w, color=INK, note=""):
            bar = Rectangle(width=w, height=0.3, color=color, fill_color=color,
                            fill_opacity=0.6, stroke_width=0)
            lbl = _t(label, size=19, color=MUTE)
            val = _t(note, size=19)
            return VGroup(lbl, bar, val).arrange(RIGHT, buff=0.25)

        b1 = lat_bar("SIMPLE", 0.7, note="0.9–5.4 s")
        b2 = lat_bar("HARD", 1.3, note="10–14 s")
        b3 = lat_bar("HUMAN", 2.2, color=MUTE, note="5–10 min")
        bars = VGroup(b1, b2, b3).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        bars.next_to(led_top, DOWN, buff=0.6)
        bars.align_to(led_top, LEFT)
        if bars.get_right()[0] > 6.1:
            bars.shift(LEFT * (bars.get_right()[0] - 6.1))
        # axis break glyph on the human bar — two slanted cream gaps
        brk_pt = b3[1].get_left() + RIGHT * 0.55
        gap = Rectangle(width=0.14, height=0.5, color=CREAM, fill_color=CREAM,
                        fill_opacity=1, stroke_width=0).move_to(brk_pt)
        s1 = Line(brk_pt + DL * 0.16 + LEFT * 0.05, brk_pt + UR * 0.16 + LEFT * 0.05,
                  color=TERRA, stroke_width=3)
        s2 = Line(brk_pt + DL * 0.16 + RIGHT * 0.05, brk_pt + UR * 0.16 + RIGHT * 0.05,
                  color=TERRA, stroke_width=3)
        brk_g = VGroup(gap, s1, s2)
        brk_g._qc_intentional = True
        self.play(FadeIn(b1), run_time=0.6)
        self.play(FadeIn(b2), run_time=0.6)
        self.play(FadeIn(b3), FadeIn(brk_g), run_time=0.8)

        tally = _box(VGroup(_t("failures", size=19, color=MUTE),
                            _t("5", size=26, color=TERRA)).arrange(RIGHT, buff=0.2),
                     h_pad=0.2, v_pad=0.12, sw=1.5)
        tally.next_to(rows, DOWN, buff=0.32)
        self.play(FadeIn(tally, shift=UP * 0.15), run_time=0.6)
        self.wait(2.3)
        check_overlaps(rows, grid_lbl, led_top, bars, tally, label="B17")


# ── B21_OneCompilerManySensors  (16.19 s) ────────────────────────────────────
class B21_OneCompilerManySensors(Scene):
    """All code funnels through one verifier; each physical task bolts on its own."""

    def construct(self):
        _rule_floor(self)

        # LEFT: the universal funnel
        comp = _box(_t("COMPILER / TESTS", size=26), h_pad=0.42, v_pad=0.3, sw=2.5)
        comp.move_to(LEFT * 3.7 + UP * 0.4)
        self.play(FadeIn(comp), run_time=0.7)

        chip_ws = [0.9, 1.3, 0.7, 1.1, 0.8, 1.2]
        verdicts = ["PASS", "PASS", "FAIL", "PASS", "PASS", "FAIL"]
        out_row = VGroup()
        for i, (w, v) in enumerate(zip(chip_ws, verdicts)):
            chip = RoundedRectangle(corner_radius=0.07, width=w, height=0.42,
                                    color=INK, stroke_width=1.5, fill_color=CREAM,
                                    fill_opacity=1)
            chip.next_to(comp, UP, buff=1.15)
            stamp = _t(v, size=19, color=INK if v == "PASS" else GRAY)
            self.play(FadeIn(chip, shift=DOWN * 0.1), run_time=0.25)
            self.play(chip.animate.move_to(comp.get_center()),
                      run_time=0.35, rate_func=rush_into)
            self.remove(chip)
            out = _box(stamp, h_pad=0.12, v_pad=0.08, sw=1.2)
            out_row.add(out)
            out_row.arrange_in_grid(rows=2, buff=0.22)
            out_row.next_to(comp, DOWN, buff=0.7)
            self.play(FadeIn(out, shift=DOWN * 0.15), run_time=0.25)
        one_lbl = _t("one funnel, every shape", size=24, color=MUTE)
        one_lbl.next_to(out_row, DOWN, buff=0.3)
        self.play(FadeIn(one_lbl), run_time=0.5)

        # RIGHT: four tasks, four bespoke sensors + the question-mark slot
        def sensor_glyph(kind):
            if kind == "photo":
                return VGroup(Circle(radius=0.11, color=INK, stroke_width=2),
                              Line(ORIGIN, UR * 0.14, color=INK, stroke_width=2))
            if kind == "camera":
                body = RoundedRectangle(corner_radius=0.04, width=0.34, height=0.22,
                                        color=INK, stroke_width=2)
                lens = Circle(radius=0.06, color=INK, stroke_width=2).move_to(body)
                return VGroup(body, lens)
            if kind == "clock":
                c = Circle(radius=0.13, color=INK, stroke_width=2)
                h = Line(c.get_center(), c.get_center() + UP * 0.09, color=INK,
                         stroke_width=2)
                return VGroup(c, h)
            arc = Arc(radius=0.15, start_angle=PI, angle=-PI, color=INK,
                      stroke_width=2)
            needle = Line(arc.get_arc_center(), arc.get_arc_center() + UR * 0.11,
                          color=INK, stroke_width=2)
            return VGroup(arc, needle)

        tasks = VGroup()
        for name, kind in [("LASER LOCK", "photo"), ("PLATE READ", "camera"),
                           ("REACTION", "clock"), ("WELD", "gauge")]:
            chip = _box(_t(name, size=16), h_pad=0.13, v_pad=0.1, sw=1.5)
            g = sensor_glyph(kind)
            g.next_to(chip, UP, buff=0.14)
            tasks.add(VGroup(chip, g))
        tasks.arrange(RIGHT, buff=0.3)
        tasks.move_to(RIGHT * 3.4 + UP * 1.1)
        if tasks.get_right()[0] > 6.1:
            tasks.shift(LEFT * (tasks.get_right()[0] - 6.1))
        self.play(LaggedStart(*[FadeIn(t) for t in tasks], lag_ratio=0.3),
                  run_time=2.4)

        yours = _box(_t("YOUR TASK", size=17), h_pad=0.16, v_pad=0.12, sw=1.5)
        q = _t("?", size=34, color=TERRA)
        yours_g = VGroup(yours, q)
        q.next_to(yours, UP, buff=0.12)
        yours_g.next_to(tasks, DOWN, buff=0.75)
        self.play(FadeIn(yours_g, shift=LEFT * 0.3), run_time=0.9)

        footer = _t("the verifier is the custom part", size=26)
        footer.next_to(yours_g, DOWN, buff=0.55)
        under = Line(footer.get_left() + DOWN * 0.22, footer.get_right() + DOWN * 0.22,
                     color=TERRA, stroke_width=2.5)
        self.play(FadeIn(footer), Create(under), run_time=0.9)
        self.wait(2.0)
        check_overlaps(comp, out_row, one_lbl, tasks, yours_g, footer, label="B21")


# ── B25_WeighThePreview  (14.95 s) ───────────────────────────────────────────
class B25_WeighThePreview(Scene):
    """Demonstrated vs asserted on a balance; the checklist grades the sources."""

    def construct(self):
        _rule_floor(self)

        # LEFT: the balance — pans are platforms; the tilt is a shift, not a
        # rotation, so chips never collide or skew.
        pivot_pt = LEFT * 3.0 + UP * 0.9
        post = Line(pivot_pt, pivot_pt + DOWN * 1.9, color=INK, stroke_width=3)
        base = Line(pivot_pt + DOWN * 1.9 + LEFT * 0.7,
                    pivot_pt + DOWN * 1.9 + RIGHT * 0.7, color=INK, stroke_width=3)
        lpan = Line(LEFT * 0.65, RIGHT * 0.65, color=INK, stroke_width=3)
        rpan = Line(LEFT * 0.65, RIGHT * 0.65, color=INK, stroke_width=3)
        lpan.move_to(pivot_pt + LEFT * 1.6 + DOWN * 0.2)
        rpan.move_to(pivot_pt + RIGHT * 1.6 + DOWN * 0.2)
        beam = always_redraw(lambda: Line(
            lpan.get_center() + UP * 0.02, rpan.get_center() + UP * 0.02,
            color=INK, stroke_width=3.5))
        self.play(Create(post), Create(base), Create(lpan), Create(rpan),
                  run_time=1.3)
        self.add(beam)
        l_hdr = _t("demonstrated", size=20, color=MUTE)
        r_hdr = _t("asserted", size=20, color=MUTE)
        l_hdr.next_to(lpan, DOWN, buff=1.0)
        r_hdr.next_to(rpan, DOWN, buff=1.0)
        self.play(FadeIn(l_hdr), FadeIn(r_hdr), run_time=0.6)

        def chip(txt, solid=True):
            t = _t(txt, size=17, color=INK if solid else MUTE)
            return _box(t, h_pad=0.14, v_pad=0.09, sw=1.8 if solid else 1.2,
                        fill=CREAM)

        c1 = chip("REAL HARDWARE"); c2 = chip("BLIND TRIALS")
        c3 = chip("GENERALIZES", solid=False); c4 = chip("“SOLVED”", solid=False)
        lstack = VGroup(lpan)
        rstack = VGroup(rpan)
        c1.next_to(lpan, UP, buff=0.06)
        c3.next_to(rpan, UP, buff=0.06)

        # RIGHT: checklist
        def check_row(name, ok, note=""):
            mark = _t("✓" if ok else "✗", size=24, color=INK if ok else TERRA)
            lbl = _t(name, size=22)
            row = VGroup(mark, lbl)
            if note:
                row.add(_t(note, size=18, color=MUTE))
            return row.arrange(RIGHT, buff=0.28)

        checks = VGroup(
            check_row("peer review", False),
            check_row("replication", False),
            check_row("open code", False),
            check_row("real hardware", True),
            check_row("blind trials", True, "(company-run)"),
        ).arrange(DOWN, buff=0.34, aligned_edge=LEFT)
        checks.move_to(RIGHT * 3.6 + UP * 0.8)

        self.play(FadeIn(c1, shift=DOWN * 0.3), FadeIn(checks[3]),
                  lstack.animate.shift(DOWN * 0.14),
                  rstack.animate.shift(UP * 0.14), run_time=1.1)
        lstack.add(c1)
        c1.next_to(lpan, UP, buff=0.06)
        c2.next_to(c1, UP, buff=0.1)
        self.play(FadeIn(c2, shift=DOWN * 0.3), FadeIn(checks[4]),
                  lstack.animate.shift(DOWN * 0.14),
                  rstack.animate.shift(UP * 0.14), run_time=1.1)
        lstack.add(c2)
        c3.next_to(rpan, UP, buff=0.06)
        self.play(FadeIn(c3, shift=DOWN * 0.3), FadeIn(checks[0]),
                  lstack.animate.shift(UP * 0.05),
                  rstack.animate.shift(DOWN * 0.05), run_time=1.1)
        rstack.add(c3)
        c4.next_to(c3, UP, buff=0.1)
        self.play(FadeIn(c4, shift=DOWN * 0.3), FadeIn(checks[1]),
                  lstack.animate.shift(UP * 0.02),
                  rstack.animate.shift(DOWN * 0.02), run_time=1.1)
        rstack.add(c4)
        self.play(FadeIn(checks[2]), run_time=0.7)

        footer = _t("a preview, weighed as one", size=26)
        footer.next_to(checks, DOWN, buff=0.7)
        footer.align_to(checks, LEFT)
        under = Line(footer.get_left() + DOWN * 0.22,
                     footer.get_right() + DOWN * 0.22, color=TERRA,
                     stroke_width=2.5)
        self.play(FadeIn(footer), Create(under), run_time=0.8)
        self.wait(2.2)
        check_overlaps(l_hdr, r_hdr, c1, c2, c3, c4, checks, footer,
                       label="B25")
