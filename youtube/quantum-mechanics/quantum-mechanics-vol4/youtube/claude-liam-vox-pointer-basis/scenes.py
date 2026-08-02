import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.6):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=25).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 return VGroup(x,y).arrange(DOWN,buff=.4)
class B02_ZCoupling(Scene):
 def construct(self):
  q=VGroup(chip("|0>",TEAL,2),chip("|1>",CRIMSON,2)).arrange(DOWN,buff=.5);couple=chip("sigma Z coupling",SLATE,3.5);env=chip("ENVIRONMENT",CRIMSON,3.2);g=VGroup(q,couple,env).arrange(RIGHT,buff=.8);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B02"]-1))
class B03_RecordsDiverge(Scene):
 def construct(self):
  rows=VGroup(VGroup(chip("|0>",TEAL,2),chip("|E0>",TEAL,2.5)).arrange(RIGHT,buff=.7),VGroup(chip("|1>",CRIMSON,2),chip("|E1>",CRIMSON,2.5)).arrange(RIGHT,buff=.7)).arrange(DOWN,buff=.8);cap=Text("environmental overlap decreases",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(rows,DOWN,buff=.6);self.play(FadeIn(rows),FadeIn(cap),run_time=1);self.wait(max(.5,D["B03"]-1))
class B04_PointerStable(Scene):
 def construct(self):
  g=VGroup(chip("|0> population stable",TEAL,4),chip("|1> population stable",CRIMSON,4)).arrange(DOWN,buff=.7);head=Text("IDEAL PURE Z DEPHASING",font=DISPLAY,color=INK,font_size=41,weight=BOLD).next_to(g,UP,buff=.8);self.play(FadeIn(head),FadeIn(g),run_time=1);self.wait(max(.5,D["B04"]-1))
class B05_PlusShrinks(Scene):
 def construct(self):
  c=Circle(radius=2,color=SLATE);a=Arrow(ORIGIN,RIGHT*1.8,color=CRIMSON,buff=0);dot=Dot(ORIGIN,color=INK,radius=.14);lab=Text("|+> transverse Bloch vector → 0",font=SERIF,color=TEAL,font_size=31,slant=ITALIC).to_edge(DOWN,buff=.7);self.play(Create(c),GrowArrow(a),run_time=.6);self.play(Transform(a,Arrow(ORIGIN,RIGHT*.15,color=CRIMSON,buff=0)),FadeIn(dot),FadeIn(lab),run_time=.9);self.wait(max(.5,D["B05"]-1.5))
class B06_ZNotXMixture(Scene):
 def construct(self):
  yes=title("Z BASIS","mixture of |0> and |1>",TEAL);no=title("NOT X BASIS","not a mixture selected as |+> and |->",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B06"]-1))
class B07_CouplingChangesBasis(Scene):
 def construct(self):
  z=VGroup(chip("Z coupling",TEAL,3),chip("|0>, |1>",TEAL,3)).arrange(RIGHT,buff=.6);x=VGroup(chip("X coupling",CRIMSON,3),chip("|+>, |->",CRIMSON,3)).arrange(RIGHT,buff=.6);g=VGroup(z,x).arrange(DOWN,buff=.8);cap=Text("pointer basis follows the interaction",font=SERIF,color=INK,font_size=31,slant=ITALIC).next_to(g,DOWN,buff=.6);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_CompetingDynamics(Scene):
 def construct(self):
  a=chip("system Hamiltonian",TEAL,4);b=chip("environment coupling",CRIMSON,4);vs=Text("compete across timescales",font=DISPLAY,color=INK,font_size=40,weight=BOLD);g=VGroup(a,vs,b).arrange(DOWN,buff=.6);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B08"]-1))
class B09_EinselectionScope(Scene):
 def construct(self):
  a=title("EXPLAINS","robust basis + lost interference",TEAL);b=title("DOES NOT CHOOSE","the unique outcome",CRIMSON);g=VGroup(a,b).arrange(DOWN,buff=.8);self.play(FadeIn(g),run_time=1);self.wait(max(.5,D["B09"]-1))
class B11_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Why Decoherence",font=DISPLAY,color=WHITE,font_size=52,weight=BOLD);b=Text("Picks a Direction",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B11"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.41
  self.add(bg(),ttl('Use an idealized interaction proportiona'))
  stmt=Text('Use an idealized interaction proportional to sigma Z co',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The environment responds differently to the Z eigenstat',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B03_SDT(Scene):
 # B03 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.15
  self.add(bg(),ttl('A zero branch becomes correlated with en'))
  stmt=Text('A zero branch becomes correlated with environmental rec',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('a one branch with E one',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.58
  self.add(bg(),ttl('If the qubit starts in zero or'))
  stmt=Text('If the qubit starts in zero or one, pure dephasing leav',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('These basis states are stable under this interaction, a',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=8.83
  self.add(bg(),ttl('The resulting local mixture is diagonal '))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The resulting local mixture is diagonal in the Z basis,',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('The preferred direction came from what the environment ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.14
  self.add(bg(),ttl('But always is too strong. If the'))
  stmt=Text('But always is too strong',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('If the coupling monitored X instead, plus and minus wou',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.31
  self.add(bg(),ttl('The system\'s own Hamiltonian can also co'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The system\'s own Hamiltonian can also compete with envi',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Pointer states are therefore selected by the full dynam',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=12.22
  self.add(bg(),ttl('This is environment-induced superselecti'))
  stmt=Text('This is environment-induced superselection: robust stat',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('It explains basis stability, not which unique outcome o',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=7.79
  self.add(bg(),ttl('Why decoherence picks a direction: the i'))
  stmt=Text('Why decoherence picks a direction: the interaction reco',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
