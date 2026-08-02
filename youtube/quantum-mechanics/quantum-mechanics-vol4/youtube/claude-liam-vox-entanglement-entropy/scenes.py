import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/"vox/aspects/explainer/vox-explainer/manim"))
from vox_graphics import *

def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
BS=json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")));D={b["beat_id"]:float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8) for b in BS["beats"]}
def chip(t,c=SLATE,w=2.6):
 r=RoundedRectangle(corner_radius=.12,width=w,height=.85).set_fill(GROUND,1).set_stroke(c,3);x=Text(t,font=MONO,color=c,font_size=24).move_to(r)
 if x.width>w*.84:x.scale_to_fit_width(w*.84)
 return VGroup(r,x)
def title(a,b,c=TEAL):
 x=Text(a,font=DISPLAY,color=INK,font_size=42,weight=BOLD);y=Text(b,font=SERIF,color=c,font_size=28,slant=ITALIC)
 if x.width>11.5:x.scale_to_fit_width(11.5)
 if y.width>11:y.scale_to_fit_width(11)
 return VGroup(x,y).arrange(DOWN,buff=.4)
def entropy_curve():
 ax=Axes(x_range=[0,.8,.2],y_range=[0,1,.25],x_length=8.5,y_length=4.5,axis_config={"color":INK,"include_ticks":False});f=lambda x:0 if x<1e-5 else -(np.cos(x)**2)*np.log2(np.cos(x)**2)-(np.sin(x)**2)*np.log2(np.sin(x)**2);curve=ax.plot(f,x_range=[.001,np.pi/4],color=CRIMSON);return ax,curve
class B02_SchmidtFamily(Scene):
 def construct(self):
  eq=Text("|psi(theta)> = cos(theta)|00> + sin(theta)|11>",font=MONO,color=INK,font_size=38);rng=Text("0 <= theta <= pi/4",font=SERIF,color=TEAL,font_size=31,slant=ITALIC).next_to(eq,DOWN,buff=.7);self.play(FadeIn(eq),FadeIn(rng),run_time=.9);self.wait(max(.5,D["B02"]-.9))
class B03_EntropyCurve(Scene):
 def construct(self):
  ax,curve=entropy_curve();eq=Text("S = -p log2 p - (1-p) log2(1-p)",font=MONO,color=TEAL,font_size=29).to_edge(UP,buff=.45);self.play(Create(ax),Create(curve),FadeIn(eq),run_time=1.3);self.wait(max(.5,D["B03"]-1.3))
class B04_ProductEnd(Scene):
 def construct(self):
  ax,curve=entropy_curve();dot=Dot(ax.c2p(0,0),color=TEAL,radius=.14);lab=title("THETA = 0","product state · S = 0 ebits",TEAL).scale(.75).to_edge(UP,buff=.5);self.play(FadeIn(ax),FadeIn(curve),FadeIn(dot),FadeIn(lab),run_time=1);self.wait(max(.5,D["B04"]-1))
class B05_BellPeak(Scene):
 def construct(self):
  ax,curve=entropy_curve();dot=Dot(ax.c2p(np.pi/4,1),color=CRIMSON,radius=.14);lab=title("THETA = PI/4","Bell pair · S = 1 ebit",CRIMSON).scale(.75).to_edge(UP,buff=.5);self.play(FadeIn(ax),FadeIn(curve),FadeIn(dot),FadeIn(lab),run_time=1);self.wait(max(.5,D["B05"]-1))
class B06_WorkedExample(Scene):
 def construct(self):
  probs=VGroup(chip("p0 = 3/4",TEAL,3),chip("p1 = 1/4",CRIMSON,3)).arrange(RIGHT,buff=.7);eq=Text("H2(3/4) = 0.811 ebits",font=MONO,color=INK,font_size=43).next_to(probs,DOWN,buff=.9);self.play(FadeIn(probs),run_time=.5);self.play(FadeIn(eq),run_time=.6);self.wait(max(.5,D["B06"]-1.1))
class B07_Balance(Scene):
 def construct(self):
  less=VGroup(chip("3/4",TEAL,2),chip("1/4",CRIMSON,2)).arrange(DOWN,buff=.3);more=VGroup(chip("1/2",TEAL,2),chip("1/2",CRIMSON,2)).arrange(DOWN,buff=.3);g=VGroup(VGroup(less,Text("0.811",font=MONO,color=INK,font_size=34)).arrange(DOWN,buff=.45),VGroup(more,Text("1.000",font=MONO,color=INK,font_size=34)).arrange(DOWN,buff=.45)).arrange(RIGHT,buff=2);cap=Text("more balanced Schmidt weight → more entanglement",font=SERIF,color=INK,font_size=30,slant=ITALIC).next_to(g,DOWN,buff=.6);self.play(FadeIn(g),FadeIn(cap),run_time=1);self.wait(max(.5,D["B07"]-1))
class B08_AsymptoticRate(Scene):
 def construct(self):
  a=chip("many identical pure pairs",TEAL,4);b=chip("ideal LOCC",SLATE,3);c=chip("Bell pairs at asymptotic rate S",CRIMSON,4.8);g=VGroup(a,b,c).arrange(RIGHT,buff=.55);ar=VGroup(Arrow(a.get_right(),b.get_left(),color=INK,buff=.15),Arrow(b.get_right(),c.get_left(),color=INK,buff=.15));cap=Text("not a finite-batch one-shot guarantee",font=SERIF,color=CRIMSON,font_size=30,slant=ITALIC).to_edge(DOWN,buff=.8);self.play(FadeIn(g),run_time=.6);self.play(*[GrowArrow(x) for x in ar],FadeIn(cap),run_time=.8);self.wait(max(.5,D["B08"]-1.4))
class B09_ScopeBoundary(Scene):
 def construct(self):
  yes=title("DIRECT RULE","bipartite pure states",TEAL);no=title("MORE CARE","mixed or multipartite states",CRIMSON);g=VGroup(yes,no).arrange(DOWN,buff=.8);self.play(LaggedStart(*[FadeIn(x) for x in g],lag_ratio=.25),run_time=1.2);self.wait(max(.5,D["B09"]-1.2))
class B11_TitleOutro(Scene):
 def construct(self):
  bg=Rectangle(width=14.3,height=8.1).set_fill("#171717",1).set_stroke(width=0);a=Text("Entanglement Has",font=DISPLAY,color=WHITE,font_size=51,weight=BOLD);b=Text("a Thermometer",font=SERIF,color="#D7C8FF",font_size=42,slant=ITALIC);c=Text("Liam, in for Bear",font=SERIF,color=WHITE,font_size=27,slant=ITALIC);g=VGroup(a,b,c).arrange(DOWN,buff=.35);self.add(bg);self.play(FadeIn(g),run_time=.7);self.wait(max(.5,D["B11"]-.7))
class B02_SDT(Scene):
 # B02 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('Consider cosine theta zero-zero plus sin'))
  stmt=Text('Consider cosine theta zero-zero plus sine theta one-one',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('These are already Schmidt-form amplitudes',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B04_SDT(Scene):
 # B04 SDT retrofit: generic reveal with underline
 def construct(self):
  d=10.0
  self.add(bg(),ttl('At theta zero, all weight sits on'))
  stmt=Text('At theta zero, all weight sits on zero-zero',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The state factors, either subsystem is pure, and the en',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B05_SDT(Scene):
 # B05 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('At theta pi over four, the weights'))
  stmt=Text('At theta pi over four, the weights are equal halves',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The state is a Bell pair and the subsystem entropy reac',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B06_SDT(Scene):
 # B06 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=12.0
  self.add(bg(),ttl('For root three over two times zero-zero'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('For root three over two times zero-zero plus one half t',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Their binary entropy is about zero point eight one one ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=11.0
  self.add(bg(),ttl('The state is entangled because both Schm'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The state is entangled because both Schmidt terms are p',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('More balanced local uncertainty means more pure-state b',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: generic reveal with underline
 def construct(self):
  d=11.0
  self.add(bg(),ttl('And the simple entropy rule has a'))
  stmt=Text('And the simple entropy rule has a boundary: it is the s',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('Mixed and multipartite states require more care and can',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B11_SDT(Scene):
 # B11 SDT retrofit: generic reveal with underline
 def construct(self):
  d=8.0
  self.add(bg(),ttl('Entanglement has a thermometer: the entr'))
  stmt=Text('Entanglement has a thermometer: the entropy of either h',font=SERIF,font_size=28,color=INK).move_to(ORIGIN)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  # no detail
  self.wait(max(0.01,d*0.2))
