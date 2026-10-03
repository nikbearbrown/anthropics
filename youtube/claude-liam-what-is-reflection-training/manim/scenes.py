"""Manim scenes — claude-liam-what-is-reflection-training
Simple 'What is' explainer. Claude stage. LAYOUT + STAGE LAYOUT laws bind.
4K-safe from authoring: text >= 24, mono uppercase/digits, |x| <= 6.1.
"""
from manim import *
import numpy as np, os

CREAM="#FAF9F5"; INK="#3D3929"; TERRA="#D97757"; MUTE="#8B7355"; GRAY="#A89F91"
config.background_color = CREAM
config.frame_rate = 24
config.pixel_height = int(os.environ.get("ART_MANIM_H","1080"))
config.pixel_width  = int(os.environ.get("ART_MANIM_W","1920"))

def _t(s,size=34,color=INK,**kw):
    return Text(s.replace(" ","  "),color=color,font_size=size,font="EB Garamond",**kw)
def _mono(s,size=24,color=MUTE,**kw):
    return Text(s,color=color,font_size=size,font="Menlo",**kw)
def _box(c,h_pad=0.28,v_pad=0.2,stroke=INK,sw=2.0,fill=CREAM,corner=0.12):
    r=RoundedRectangle(corner_radius=corner,width=c.width+2*h_pad,height=c.height+2*v_pad,
                       color=stroke,stroke_width=sw,fill_color=fill,fill_opacity=1)
    r.move_to(c); return VGroup(r,c)
def _rule(scene):
    r=Line(LEFT*6,RIGHT*6,color=INK,stroke_width=2).set_stroke(opacity=0.3)
    r.to_edge(DOWN,buff=0.53); scene.add(r); return r
def _clamp(m,lim=6.1):
    if m.get_right()[0]>lim: m.shift(LEFT*(m.get_right()[0]-lim))
    if m.get_left()[0]<-lim: m.shift(RIGHT*(-lim-m.get_left()[0]))
    return m
def check_overlaps(*mobs,margin=0.12,label=""):
    bb=lambda m:(m.get_left()[0],m.get_bottom()[1],m.get_right()[0],m.get_top()[1])
    v=[]
    for i,a in enumerate(mobs):
        la,ba,ra,ta=bb(a)
        for j,b in enumerate(mobs):
            if j<=i: continue
            lb,bb_,rb,tb=bb(b)
            if la<rb+margin and ra>lb-margin and ba<tb+margin and ta>bb_-margin:
                v.append(f"  {i}x{j}")
    print(f"[BBOX {label}] "+("OK" if not v else f"{len(v)} overlap(s):\n"+"\n".join(v)))
def _ledger(rows,size=26,buff=0.42):
    out=VGroup()
    for k,v in rows:
        key=_t(k,size=size,color=MUTE)
        val=v if isinstance(v,Mobject) else _t(str(v),size=size)
        out.add(VGroup(key,val).arrange(RIGHT,buff=0.32))
    out.arrange(DOWN,buff=buff,aligned_edge=LEFT); return out


class B02_TheWorkspacePremise(Scene):
    """18.28s — the workspace band holds might-say chips; IF/THEN lands."""
    def construct(self):
        _rule(self)
        col=Rectangle(width=2.0,height=4.6,color=INK,stroke_width=2,
                      fill_color=CREAM,fill_opacity=1)
        col.move_to(LEFT*3.9+UP*0.2)
        band=Rectangle(width=2.0,height=1.9,stroke_width=0,fill_color=TERRA,fill_opacity=0.28)
        band.move_to(col)
        bl=_t("THE WORKSPACE",size=25,color=TERRA).next_to(col,UP,buff=0.25)
        self.play(Create(col),run_time=0.8)
        self.play(FadeIn(band),FadeIn(bl),run_time=0.9)
        chips=VGroup(*[_box(_t(w,size=24),h_pad=0.12,v_pad=0.08,sw=1.2)
                       for w in ["task","file","next step"]])
        chips.arrange(DOWN,buff=0.18).move_to(band)
        for c in chips: c.scale(0.9)
        self.play(LaggedStart(*[FadeIn(c) for c in chips],lag_ratio=0.3),run_time=1.3)
        held=_t("held in might-say currency",size=24,color=MUTE).next_to(col,DOWN,buff=0.3)
        self.play(FadeIn(held),run_time=0.6)
        if_row=VGroup(_t("IF",size=26,color=MUTE),
                      _t("thinking runs through might-say",size=26)).arrange(RIGHT,buff=0.3)
        then_row=VGroup(_t("THEN",size=26,color=MUTE),
                        _t("train the saying, change the thinking",size=26)).arrange(RIGHT,buff=0.3)
        panel=VGroup(if_row,then_row).arrange(DOWN,buff=0.55,aligned_edge=LEFT)
        pbox=SurroundingRectangle(panel,color=INK,stroke_width=2,buff=0.42,corner_radius=0.12)
        grp=VGroup(pbox,panel); grp.move_to(RIGHT*2.6+UP*0.6); _clamp(grp)
        self.play(FadeIn(pbox),FadeIn(if_row),run_time=1.0)
        self.wait(0.8)
        self.play(FadeIn(then_row),run_time=1.0)
        u=Line(then_row.get_left()+DOWN*0.26,then_row.get_right()+DOWN*0.26,
               color=TERRA,stroke_width=3)
        self.play(Create(u),run_time=0.6)
        foot=_t("not new knowledge — new reflexes",size=28)
        foot.next_to(grp,DOWN,buff=0.55); _clamp(foot)
        self.play(FadeIn(foot),run_time=0.8)
        self.wait(8.4)
        check_overlaps(col,bl,held,grp,foot,label="B02")


class B03_TheGap(Scene):
    """13.67s — the workspace holds the job; the ethics slot stays hollow."""
    def construct(self):
        _rule(self)
        lines=VGroup(*[Line(LEFT*1.6,RIGHT*1.6,color=GRAY,stroke_width=3)
                       for _ in range(9)])
        lines.arrange(DOWN,buff=0.32).move_to(LEFT*3.9+UP*0.3)
        self.play(LaggedStart(*[Create(l) for l in lines],lag_ratio=0.08),run_time=1.4)
        mark=Line(LEFT*1.8,RIGHT*1.8,color=TERRA,stroke_width=4)
        mark.move_to(lines[5])
        ml=_t("ethically loaded moment",size=28,color=TERRA).next_to(lines,DOWN,buff=0.35)
        self.play(Create(mark),FadeIn(ml),run_time=0.9)
        ws=RoundedRectangle(corner_radius=0.12,width=4.3,height=3.3,color=INK,
                            stroke_width=2.5,fill_color=CREAM,fill_opacity=1)
        ws.move_to(RIGHT*3.3+UP*0.35); _clamp(ws)
        wl=_t("THE WORKSPACE, MID-TASK",size=28,color=MUTE).next_to(ws,UP,buff=0.2); _clamp(wl)
        self.play(Create(ws),FadeIn(wl),run_time=0.8)
        items=VGroup(*[_t(w,size=26) for w in ["file path","command","next move"]])
        items.arrange(DOWN,buff=0.3,aligned_edge=LEFT)
        ghost=DashedVMobject(RoundedRectangle(corner_radius=0.08,width=3.4,height=0.6,
                             color=TERRA,stroke_width=2.5),num_dashes=30)
        gl=_t("should I flag this?",size=28,color=TERRA)
        gl.move_to(ghost)
        gslot=VGroup(ghost,gl)
        inner=VGroup(items,gslot).arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        inner.move_to(ws)
        self.play(LaggedStart(*[FadeIn(i) for i in items],lag_ratio=0.3),run_time=1.4)
        self.wait(1.6)
        self.play(Create(ghost),FadeIn(gl),run_time=1.1)
        self.wait(4.6)
        check_overlaps(lines,ml,ws,wl,label="B03")


class B05_CutAskTune(Scene):
    """16.60s — cut the transcript, append the question, tune; the ledger lands."""
    def construct(self):
        _rule(self)
        bar=Rectangle(width=4.6,height=0.55,color=INK,stroke_width=2,
                      fill_color=GRAY,fill_opacity=0.3)
        bar.move_to(LEFT*3.2+UP*1.9)
        tl=_t("a real transcript",size=28,color=MUTE).next_to(bar,UP,buff=0.3)
        tl.align_to(bar,LEFT)
        self.play(FadeIn(bar),FadeIn(tl),run_time=0.9)
        cutx=bar.get_left()[0]+2.9
        cut=DashedLine([cutx,bar.get_top()[1]+0.25,0],[cutx,bar.get_bottom()[1]-0.25,0],
                       color="#A64A24",stroke_width=4)
        keep=Rectangle(width=2.9,height=0.55,color=INK,stroke_width=2,
                       fill_color=CREAM,fill_opacity=1).align_to(bar,LEFT).align_to(bar,DOWN)
        cl=_t("CUT, MID-TASK",size=28,color="#A64A24")  # WCAG-deep terracotta for TEXT
        cl.next_to(cut,UP,buff=0.3); cl.align_to(cut,LEFT); _clamp(cl)
        self.play(Create(cut),FadeIn(keep),FadeIn(cl),run_time=1.1)
        q=_box(_t("what considerations apply right now?",size=28),h_pad=0.24,v_pad=0.16,
               stroke="#A64A24",sw=2.0)
        q.next_to(keep,DOWN,buff=0.7); q.align_to(keep,LEFT); _clamp(q,5.9)
        aq=Arrow(keep.get_bottom(),q.get_top(),color=INK,stroke_width=2.5,tip_length=0.14,buff=0.1)
        self.play(GrowArrow(aq),FadeIn(q),run_time=1.2)
        tune=_box(_t("FINE-TUNE on strong answers",size=28),h_pad=0.26,v_pad=0.18,sw=2.5)
        tune.next_to(q,DOWN,buff=0.7); tune.align_to(q,LEFT); _clamp(tune,5.9)
        at=Arrow(q.get_bottom(),tune.get_top(),color=INK,stroke_width=2.5,tip_length=0.14,buff=0.1)
        self.play(GrowArrow(at),FadeIn(tune),run_time=1.2)
        led=_ledger([("CUT","mid-task"),("ASK","the reflection question"),
                     ("TUNE","on strong answers")],size=28,buff=0.45)
        pbox=SurroundingRectangle(led,color=INK,stroke_width=2,buff=0.4,corner_radius=0.12)
        grp=VGroup(pbox,led); grp.move_to(RIGHT*3.9+UP*1.1); _clamp(grp)
        self.play(FadeIn(grp),run_time=1.0)
        foot=_t("reflections about moments never finished",size=28)
        foot.move_to([2.7,tune.get_center()[1]-1.35,0]); _clamp(foot)
        self.play(FadeIn(foot),run_time=0.8)
        self.wait(7.4)
        check_overlaps(bar,tl,cl,q,tune,grp,foot,label="B05")


class B06_TheNumbers(Scene):
    """14.95s — before/after pairs fall; the only change is the training."""
    def construct(self):
        _rule(self)
        SC=5.2
        def pair(name,b,a):
            bb=Rectangle(width=0.75,height=b*SC,color=GRAY,fill_color=GRAY,
                         fill_opacity=0.5,stroke_width=0)
            ab=Rectangle(width=0.75,height=0.02,color=INK,fill_color=INK,
                         fill_opacity=0.7,stroke_width=0)
            bars=VGroup(bb,ab).arrange(RIGHT,buff=0.25,aligned_edge=DOWN)
            bl=_mono(f"{b:.2f}",size=24,color=MUTE).next_to(bb,UP,buff=0.12)
            al=_mono(f"{a:.2f}",size=24,color=INK)
            nl=_t(name,size=25,color=MUTE).next_to(bars,DOWN,buff=0.25)
            return VGroup(bars,bl,al,nl),ab,al,a
        p1,a1,l1,v1=pair("FABRICATION",0.25,0.07)
        p2,a2,l2,v2=pair("DECEPTION",0.38,0.05)
        both=VGroup(p1,p2).arrange(RIGHT,buff=1.5,aligned_edge=DOWN)
        both.move_to(LEFT*3.1+UP*0.1)
        self.play(FadeIn(p1[0][0]),FadeIn(p1[1]),FadeIn(p1[3]),
                  FadeIn(p2[0][0]),FadeIn(p2[1]),FadeIn(p2[3]),run_time=1.2)
        self.add(a1,a2)
        l1.next_to(a1,UP,buff=0.12); l2.next_to(a2,UP,buff=0.12)
        self.play(a1.animate.stretch_to_fit_height(v1*SC).align_to(p1[0][0],DOWN),
                  a2.animate.stretch_to_fit_height(v2*SC).align_to(p2[0][0],DOWN),
                  run_time=2.2)
        l1.next_to(a1,UP,buff=0.12); l2.next_to(a2,UP,buff=0.12)
        self.play(FadeIn(l1),FadeIn(l2),run_time=0.6)
        led=_ledger([("MODEL","same"),("SIZE","same"),
                     ("CHANGE","reflection training")],size=26,buff=0.5)
        pbox=SurroundingRectangle(led,color=INK,stroke_width=2,buff=0.42,corner_radius=0.12)
        grp=VGroup(pbox,led); grp.move_to(RIGHT*3.6+UP*0.3); _clamp(grp)
        self.play(FadeIn(grp),run_time=1.0)
        u=Line(led[2].get_left()+DOWN*0.26,led[2].get_right()+DOWN*0.26,
               color=TERRA,stroke_width=3)
        self.play(Create(u),run_time=0.6)
        self.wait(6.6)
        check_overlaps(both,l1,l2,grp,label="B06")


class B08_MechanismAndAblation(Scene):
    """20.76s — the installed reflex, then its deletion; the meter claws back."""
    def construct(self):
        _rule(self)
        ws=RoundedRectangle(corner_radius=0.12,width=4.2,height=2.9,color=INK,
                            stroke_width=2.5,fill_color=CREAM,fill_opacity=1)
        ws.move_to(LEFT*3.3+UP*0.5)
        wl=_t("THE WORKSPACE, MID-TASK",size=28,color=MUTE).next_to(ws,UP,buff=0.2); _clamp(wl)
        self.play(Create(ws),FadeIn(wl),run_time=0.9)
        base=VGroup(*[_t(w,size=28) for w in ["file path","next move"]])
        eth=_box(_t("ethics",size=28,color=TERRA),h_pad=0.14,v_pad=0.09,stroke=TERRA,sw=1.8)
        ref=_box(_t("reflect",size=28,color=TERRA),h_pad=0.14,v_pad=0.09,stroke=TERRA,sw=1.8)
        inner=VGroup(base[0],base[1],eth,ref).arrange(DOWN,buff=0.28,aligned_edge=LEFT)
        inner.move_to(ws)
        self.play(FadeIn(base[0]),FadeIn(base[1]),run_time=0.8)
        self.play(FadeIn(eth,shift=RIGHT*0.2),FadeIn(ref,shift=RIGHT*0.2),run_time=1.2)
        inst=_t("the installed reflex — before any question",size=28,color=MUTE)
        inst.next_to(ws,DOWN,buff=0.3); _clamp(inst)
        self.play(FadeIn(inst),run_time=0.7)
        # meter
        mv=ValueTracker(0.05)
        num=DecimalNumber(0.05,num_decimal_places=2,color=INK,font_size=52)
        num.add_updater(lambda m: m.set_value(mv.get_value()))
        ml2=_t("DECEPTION SCORE",size=28,color=MUTE)
        frame=Rectangle(width=3.0,height=0.34,color=INK,stroke_width=1.5)
        mfill=always_redraw(lambda: Rectangle(
            width=max(0.02,mv.get_value()/0.4*3.0),height=0.34,
            color=TERRA,fill_color=TERRA,fill_opacity=0.6,stroke_width=0
        ).align_to(frame,LEFT).align_to(frame,DOWN))
        meter=VGroup(ml2,num,frame).arrange(DOWN,buff=0.35,aligned_edge=LEFT)
        meter.move_to(RIGHT*3.8+UP*0.6); _clamp(meter)
        self.add(mfill)
        self.play(FadeIn(meter),run_time=0.8)
        self.wait(2.8)
        # ablation: strike and remove the chips, meter climbs
        x1=Cross(eth,stroke_color=TERRA,stroke_width=5); x1._qc_intentional=True
        x2=Cross(ref,stroke_color=TERRA,stroke_width=5); x2._qc_intentional=True
        self.play(Create(x1),Create(x2),run_time=0.9)
        self.play(VGroup(eth,x1).animate.shift(RIGHT*0.4).set_opacity(0),
                  VGroup(ref,x2).animate.shift(RIGHT*0.4).set_opacity(0),
                  mv.animate.set_value(0.23),run_time=2.4)
        num.clear_updaters()
        foot=_t("the gain lives in those directions",size=28)
        foot.next_to(meter,DOWN,buff=0.85); _clamp(foot)
        u=Line(foot.get_left()+DOWN*0.24,foot.get_right()+DOWN*0.24,color=TERRA,stroke_width=2.5)
        self.play(FadeIn(foot),Create(u),run_time=0.9)
        self.wait(7.8)
        check_overlaps(ws,wl,inst,meter,foot,label="B08")
