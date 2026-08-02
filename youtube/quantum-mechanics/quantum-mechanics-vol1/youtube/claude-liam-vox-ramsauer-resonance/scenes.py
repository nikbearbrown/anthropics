import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json"))); DUR={x["beat_id"]:float(x.get("actual_duration_s") or x.get("estimated_duration_s") or 8) for x in b["beats"]}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def barrier(w=3): return Rectangle(width=w,height=4.3,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.12)
def wav(x0,x1,k,y=0,col=TEAL):
 xs=np.linspace(x0,x1,300); return VMobject(color=col,stroke_width=3).set_points_smoothly([np.array([x,.55*np.sin(k*x)+y,0]) for x in xs])

class B02_Regions(Scene):
 def construct(self):
  d=DUR.get("B02",10); self.add(bg(),ttl("ABOVE THE BARRIER: WAVES PROPAGATE EVERYWHERE")); b=barrier(); w1=wav(-6,-1.5,2,0); wi=wav(-1.5,1.5,3.5,0,CRIMSON); w2=wav(1.5,6,2,0); labs=VGroup(Text("k",font=MONO,font_size=25,color=TEAL).move_to(LEFT*4+DOWN*1.4),Text("q",font=MONO,font_size=25,color=CRIMSON).move_to(DOWN*1.4),Text("k",font=MONO,font_size=25,color=TEAL).move_to(RIGHT*4+DOWN*1.4),Text("E > V0",font=MONO,font_size=26,color=INK).move_to(UP*2)); self.play(FadeIn(b),Create(w1),Create(wi),Create(w2),FadeIn(labs),run_time=1.2); self.wait(max(.1,d-1.2))

class B03_Question(Scene):
 def construct(self):
  d=DUR.get("B03",6); self.add(bg(),Text("THE QUESTION",font=DISPLAY,font_size=23,color=SLATE).move_to(UP*2.3),Text("How can two reflecting boundaries",font=SERIF,font_size=40,color=INK).move_to(UP*.5),Text("produce zero reflection?",font=SERIF,font_size=44,color=CRIMSON).move_to(DOWN*.9)); self.wait(d)

class B04_FirstPaths(Scene):
 def construct(self):
  d=DUR.get("B04",11); self.add(bg(),ttl("TWO FIRST REFLECTED PATHS")); b=barrier(); inc=Arrow(LEFT*5,LEFT*1.7,color=TEAL,buff=0); r0=Arrow(LEFT*1.7,LEFT*4.5,color=CRIMSON,buff=0).shift(UP*1.2); inside=VGroup(Arrow(LEFT*1.3,RIGHT*1.3,color=TEAL,buff=0).shift(DOWN*.3),Arrow(RIGHT*1.3,LEFT*1.3,color=SLATE,buff=0).shift(DOWN*1.2)); labs=VGroup(Text("immediate reflection",font=MONO,font_size=23,color=CRIMSON).next_to(r0,UP),Text("one internal round trip",font=MONO,font_size=23,color=INK).move_to(DOWN*2.7)); self.play(FadeIn(b),GrowArrow(inc),run_time=.6); self.play(GrowArrow(r0),GrowFromCenter(inside),FadeIn(labs),run_time=.9); self.wait(max(.1,d-1.5))

class B05_ManyPaths(Scene):
 def construct(self):
  d=DUR.get("B05",11); self.add(bg(),ttl("THE BARRIER GENERATES A SERIES OF ROUND TRIPS")); b=barrier(5); ys=[1.3,.5,-.3,-1.1]; paths=VGroup(*[VGroup(Arrow(LEFT*2.2,RIGHT*2.2,color=TEAL,buff=0),Arrow(RIGHT*2.2,LEFT*2.2,color=CRIMSON,buff=0)).shift(UP*y) for y in ys]); weights=VGroup(*[Text(s,font=MONO,font_size=22,color=INK).move_to(RIGHT*4+UP*y) for y,s in zip(ys,["path 1","path 2","path 3","..."])]); self.play(FadeIn(b),GrowFromCenter(paths),FadeIn(weights),run_time=1.2); self.wait(max(.1,d-1.2))

class B06_Phase(Scene):
 def construct(self):
  d=DUR.get("B06",10); self.add(bg(),ttl("INTERNAL PROPAGATION ADDS PHASE")); b=barrier(5); one=Arrow(LEFT*2.1,RIGHT*2.1,color=TEAL,buff=0).shift(UP*.8); two=VGroup(Arrow(LEFT*2.1,RIGHT*2.1,color=CRIMSON,buff=0),Arrow(RIGHT*2.1,LEFT*2.1,color=CRIMSON,buff=0)).shift(DOWN*.8); labs=VGroup(Text("one traversal: q L",font=MONO,font_size=27,color=TEAL).next_to(one,UP),Text("round trip: 2 q L",font=MONO,font_size=27,color=CRIMSON).next_to(two,DOWN)); self.play(FadeIn(b),GrowArrow(one),GrowFromCenter(two),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))

class B07_HalfWaves(Scene):
 def construct(self):
  d=DUR.get("B07",11); self.add(bg(),ttl("RESONANCE: AN INTEGER NUMBER OF HALF-WAVELENGTHS")); b=barrier(6); w=wav(-3,3,PI,0,TEAL); eq=Text("q L = n pi",font=MONO,font_size=40,color=CRIMSON).move_to(UP*2.5); cancel=VGroup(Arrow(LEFT*4.8,LEFT*2.3,color=INK,buff=0).shift(DOWN*2.5),Arrow(LEFT*2.3,LEFT*4.8,color=CRIMSON,buff=0).shift(DOWN*2.5)); lab=Text("reflected amplitudes cancel",font=SERIF,font_size=27,color=INK).move_to(RIGHT*2.5+DOWN*2.5); self.play(FadeIn(b),Create(w),FadeIn(eq),run_time=.9); self.play(GrowFromCenter(cancel),FadeIn(lab),run_time=.8); self.wait(max(.1,d-1.7))

class B08_Perfect(Scene):
 def construct(self):
  d=DUR.get("B08",10); self.add(bg(),ttl("IDEAL RESONANCE")); left=VGroup(Text("REFLECTION",font=DISPLAY,font_size=29,color=CRIMSON),Text("R = 0",font=MONO,font_size=48,color=CRIMSON)).arrange(DOWN,buff=.6).move_to(LEFT*3.5); right=VGroup(Text("TRANSMISSION",font=DISPLAY,font_size=29,color=TEAL),Text("T = 1",font=MONO,font_size=48,color=TEAL)).arrange(DOWN,buff=.6).move_to(RIGHT*3.5); div=Line(UP*2.2,DOWN*2.2,color=SLATE); self.play(FadeIn(left,right),Create(div),run_time=1); self.wait(max(.1,d-1))

class B09_Scan(Scene):
 def construct(self):
  d=DUR.get("B09",10); self.add(bg(),ttl("TRANSMISSION PEAKS AT SUCCESSIVE RESONANCES")); ax=Axes(x_range=[0,10,2],y_range=[0,1.1,.2],x_length=10,y_length=4,tips=False).move_to(DOWN*.2); curve=ax.plot(lambda x:.12+.88/(1+15*np.sin(1.25*x)**2),x_range=[.1,10],color=TEAL); labs=VGroup(Text("energy",font=MONO,font_size=23,color=INK).next_to(ax,DOWN),Text("T",font=MONO,font_size=23,color=INK).next_to(ax,LEFT),Text("T = 1",font=MONO,font_size=23,color=CRIMSON).move_to(UP*2.3)); self.play(Create(ax),Create(curve),FadeIn(labs),run_time=1.1); self.wait(max(.1,d-1.1))

class B10_Width(Scene):
 def construct(self):
  d=DUR.get("B10",10); self.add(bg(),ttl("WIDTH CHANGES THE PHASE CONDITION")); b1=barrier(2).move_to(LEFT*3.5); b2=barrier(4).move_to(RIGHT*3.5); labs=VGroup(Text("L",font=MONO,font_size=30,color=CRIMSON).next_to(b1,DOWN),Text("2L",font=MONO,font_size=30,color=CRIMSON).next_to(b2,DOWN),Text("qL = n pi",font=MONO,font_size=28,color=INK).move_to(LEFT*3.5+UP*2.6),Text("2qL = n pi",font=MONO,font_size=28,color=INK).move_to(RIGHT*3.5+UP*2.6)); self.play(FadeIn(b1,b2,labs),run_time=1); self.wait(max(.1,d-1))

class B11_Nonideal(Scene):
 def construct(self):
  d=DUR.get("B11",11); self.add(bg(),ttl("WHAT BLURS PERFECT TRANSPARENCY")); items=VGroup(*[Text(s,font=MONO,font_size=28,color=c) for s,c in [("absorption",CRIMSON),("disorder",INK),("dephasing",CRIMSON),("energy spread",INK)]]).arrange(DOWN,buff=.5).move_to(LEFT*3.2); ideal=VGroup(Line(LEFT*1.7,RIGHT*1.7,color=TEAL,stroke_width=5),Text("sharp T=1 peak",font=SERIF,font_size=25,color=TEAL)).arrange(DOWN).move_to(RIGHT*3.4+UP*.8); blurred=VGroup(Line(LEFT*2.2,RIGHT*2.2,color=SLATE,stroke_width=12),Text("lower, broader peak",font=SERIF,font_size=25,color=INK)).arrange(DOWN).move_to(RIGHT*3.4+DOWN*1.2); self.play(FadeIn(items,ideal,blurred),run_time=1); self.wait(max(.1,d-1))

class B12_Recap(Scene):
 def construct(self):
  d=DUR.get("B12",8); self.add(bg(),Text("THE BARRIER REMAINS",font=DISPLAY,font_size=32,color=CRIMSON).move_to(UP*1.7),Text("its reflected paths erase one another",font=SERIF,font_size=40,color=INK),Text("q L = n pi  →  T = 1",font=MONO,font_size=31,color=TEAL).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=10.58
  self.add(bg(),ttl('Assume the particle energy is above the'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Assume the particle energy is above the rectangular bar',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The wave propagates in every region, but its wave numbe',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.13
  self.add(bg(),ttl('Those are only the first two paths.'))
  stmt=Text('Those are only the first two paths',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The wave can make repeated round trips inside the barri',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: derive — sequential step build
 def construct(self):
  d=9.32
  self.add(bg(),ttl('Their relative phases depend on the inte'))
  s0=Text('Their relative phases depend on the internal wav',font=SERIF,font_size=30,color=INK).shift(UP*1.5)
  s0.set_max_width(12)
  self.play(Write(s0),run_time=max(0.01,d*0.23))
  s1=Text('One traversal adds phase q L',font=SERIF,font_size=30,color=INK).shift(UP*0.4)
  s1.set_max_width(12)
  self.play(Write(s1),run_time=max(0.01,d*0.23))
  s2=Text('one round trip adds two q L',font=SERIF,font_size=30,color=CRIMSON).shift(UP*-0.7)
  s2.set_max_width(12)
  self.play(Write(s2),run_time=max(0.01,d*0.23))
  self.wait(max(0.01,d*0.3))
class B08_SDT(Scene):
 # B08 SDT retrofit: generic reveal with underline
 def construct(self):
  d=9.79
  self.add(bg(),ttl('At that resonance, reflected probability'))
  stmt=Text('At that resonance, reflected probability falls to zero ',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
class B10_SDT(Scene):
 # B10 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=8.09
  self.add(bg(),ttl('Changing the width shifts the resonances'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Changing the width shifts the resonances because the pr',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Double L, and the matching energies rearrange',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.15
  self.add(bg(),ttl('This is a coherent above-barrier effect '))
  stmt=Text('This is a coherent above-barrier effect for an ideal re',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Absorption, disorder, dephasing, or a broad energy spre',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
