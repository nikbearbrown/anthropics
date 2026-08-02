import sys,json,pathlib,numpy as np
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[3]/'vox/aspects/explainer/vox-explainer/manim'))
from vox_graphics import *
DUR={}
try:
 b=json.load(open(pathlib.Path(__file__).with_name('beat_sheet.json'))); DUR={x['beat_id']:float(x.get('actual_duration_s') or x.get('estimated_duration_s') or 8) for x in b['beats']}
except Exception: pass
def bg(): return Rectangle(width=16,height=9).set_fill(GROUND,1).set_stroke(width=0)
def ttl(s): return Text(s,font=DISPLAY,font_size=28,color=INK).move_to(UP*3.35)
def well(): return FunctionGraph(lambda x:.035*(x*x-9)**2-1.5,x_range=[-5,5],color=INK,stroke_width=4)
def lobes(): return VGroup(FunctionGraph(lambda x:2*np.exp(-3*(x+3)**2)-1.2,x_range=[-5,0],color=CRIMSON,stroke_width=4),FunctionGraph(lambda x:2*np.exp(-3*(x-3)**2)-1.2,x_range=[0,5],color=CRIMSON,stroke_width=4))
class B02_Equations(Scene):
 def construct(self):
  d=DUR.get('B02',15); self.add(bg(),ttl('EXACT THEOREM · APPROXIMATE CLASSICAL CLOSURE')); rows=VGroup(Text('d<x>/dt = <p>/m',font=MONO,font_size=39,color=TEAL),Text('d<p>/dt = <F(x)>',font=MONO,font_size=39,color=CRIMSON),Text('<F(x)> approx F(<x>)  only when justified',font=MONO,font_size=31,color=INK)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B03_Narrow(Scene):
 def construct(self):
  d=DUR.get('B03',12); self.add(bg(),ttl('NARROW PACKET: LOCALLY CLASSICAL')); w=well(); p=FunctionGraph(lambda x:1.3*np.exp(-3*(x+2.3)**2)-.7,x_range=[-4,0],color=CRIMSON,stroke_width=4); mean=DashedLine(DOWN*2,UP*1.8,color=TEAL).shift(LEFT*2.3); lab=Text('short-time approximation',font=SERIF,font_size=31,color=TEAL).move_to(DOWN*2.8); self.play(Create(w),Create(p),Create(mean),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B04_Split(Scene):
 def construct(self):
  d=DUR.get('B04',14); self.add(bg(),ttl('SPLIT STATE: MEAN ON THE BARRIER')); w=well(); p=lobes(); mean=DashedLine(DOWN*2.2,UP*2.1,color=TEAL); lab=Text('<x> = 0',font=MONO,font_size=32,color=TEAL).move_to(UP*2.5); self.play(Create(w),Create(p),Create(mean),FadeIn(lab),run_time=1); self.wait(max(.1,d-1))
class B05_MeanMode(Scene):
 def construct(self):
  d=DUR.get('B05',14); self.add(bg(),ttl('MEAN IS NOT MODE')); ax=NumberLine(x_range=[-4,4,1],length=10,color=SLATE); dots=VGroup(Dot(ax.n2p(-2),radius=.3,color=CRIMSON),Dot(ax.n2p(2),radius=.3,color=CRIMSON),Dot(ax.n2p(0),radius=.18,color=TEAL)); labs=VGroup(Text('modes',font=MONO,font_size=28,color=CRIMSON).move_to(LEFT*3+UP*1.3),Text('mean',font=MONO,font_size=28,color=TEAL).move_to(UP*1.3)); self.play(Create(ax),FadeIn(dots,labs),run_time=1); self.wait(max(.1,d-1))
class B06_NarrowForce(Scene):
 def construct(self):
  d=DUR.get('B06',17); self.add(bg(),ttl('NARROW SUPPORT SAMPLES NEARLY ONE FORCE')); curve=FunctionGraph(lambda x:.18*x*x-.8,x_range=[-3.8,3.8],color=INK); window=Rectangle(width=1.7,height=3.5,color=TEAL,fill_color=TEAL,fill_opacity=.1).shift(LEFT*2); tangent=Line(LEFT*3+DOWN*.3,LEFT*1+UP*.3,color=CRIMSON); eq=Text('<F> approx F(<x>)',font=MONO,font_size=36,color=TEAL).move_to(DOWN*2.5); self.play(Create(curve),FadeIn(window),Create(tangent),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B07_Symmetry(Scene):
 def construct(self):
  d=DUR.get('B07',14); self.add(bg(),ttl('EVEN POTENTIAL · ODD FORCE · CANCELLING AVERAGE')); left=Arrow(LEFT*4,LEFT*1.5,color=CRIMSON,buff=0); right=Arrow(RIGHT*4,RIGHT*1.5,color=CRIMSON,buff=0); center=DashedLine(DOWN*2,UP*2,color=TEAL); eq=Text('<F> = 0 by symmetry',font=MONO,font_size=37,color=INK).move_to(DOWN*2.6); self.play(GrowArrow(left),GrowArrow(right),Create(center),FadeIn(eq),run_time=1); self.wait(max(.1,d-1))
class B08_Ensemble(Scene):
 def construct(self):
  d=DUR.get('B08',16); self.add(bg(),ttl('ONE MEAN · TWO CLUSTERS OF OUTCOMES')); dots=VGroup(*[Dot(np.array([x,0,0]),radius=.12,color=CRIMSON) for x in [-3.4,-3.2,-3,-2.8,-2.6,2.6,2.8,3,3.2,3.4]]); mean=Arrow(DOWN*2,ORIGIN,color=TEAL,buff=0); labs=VGroup(Text('detections',font=MONO,font_size=29,color=CRIMSON).move_to(UP*1.2),Text('ensemble mean',font=MONO,font_size=29,color=TEAL).move_to(DOWN*2.5)); self.play(FadeIn(dots),GrowArrow(mean),FadeIn(labs),run_time=1); self.wait(max(.1,d-1))
class B09_Moments(Scene):
 def construct(self):
  d=DUR.get('B09',16); self.add(bg(),ttl('A SPLIT STATE NEEDS MORE THAN ITS MEAN')); rows=VGroup(Text('<x> : center',font=MONO,font_size=36,color=SLATE),Text('variance : spread',font=MONO,font_size=36,color=TEAL),Text('full P(x) : two lobes',font=MONO,font_size=36,color=CRIMSON)).arrange(DOWN,buff=.75); self.play(FadeIn(rows),run_time=1); self.wait(max(.1,d-1))
class B10_YourTurn(Scene):
 def construct(self):
  d=DUR.get('B10',17); self.add(bg(),ttl('YOUR TURN: HALF AT -2 · HALF AT +2')); eqs=VGroup(Text('<x> = 0',font=MONO,font_size=42,color=TEAL),Text('Var(x) approx 4',font=MONO,font_size=42,color=CRIMSON),Text('variance reveals what the mean hides',font=SERIF,font_size=31,color=INK)).arrange(DOWN,buff=.8); self.play(FadeIn(eqs),run_time=1); self.wait(max(.1,d-1))
class B11_Recap(Scene):
 def construct(self):
  d=DUR.get('B11',18); self.add(bg(),Text('WHY THE AVERAGE STOPS LOOKING CLASSICAL',font=DISPLAY,font_size=34,color=CRIMSON).move_to(UP*2.3),Text('<F(x)> need not equal F(<x>)',font=MONO,font_size=34,color=TEAL).move_to(UP*.8),Text('split distributions defeat one-number summaries',font=MONO,font_size=30,color=INK).move_to(DOWN*.4),Text('expectation value is not a hidden trajectory',font=MONO,font_size=30,color=CRIMSON).move_to(DOWN*1.8)); self.wait(d)
class B02_SDT(Scene):
 # B02 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.72
  self.add(bg(),ttl('Ehrenfest\'s theorem is exact: the positi'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Ehrenfest\'s theorem is exact: the position mean changes',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('For a narrow packet in a smooth potential, average forc',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B03_SDT(Scene):
 # B03 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=14.34
  self.add(bg(),ttl('Place a narrow packet on one side'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Place a narrow packet on one side of a double well: two',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('Over times short enough that spreading and tunneling st',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B07_SDT(Scene):
 # B07 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.42
  self.add(bg(),ttl('For an even double-well potential, the f'))
  stmt=Text('For an even double-well potential, the force is odd',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('In a symmetric two-lobed state, contributions from plus',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
class B08_SDT(Scene):
 # B08 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=15.91
  self.add(bg(),ttl('Expectation value is an ensemble average'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('Expectation value is an ensemble average over the proba',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('For two separated humps, the mean can sit between them ',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B09_SDT(Scene):
 # B09 SDT retrofit: compare — two sides diverge at the spoken contrast
 def construct(self):
  d=17.09
  self.add(bg(),ttl('The implication: Ehrenfest does not assi'))
  left_box=Rectangle(width=5.5,height=3.2,color=TEAL,fill_color=TEAL,fill_opacity=.07,stroke_width=2).shift(LEFT*3.2)
  left_lbl=Text('The implication: Ehrenfest does not assign each quantum',font=SERIF,font_size=28,color=INK).move_to(left_box)
  left_lbl.set_max_width(4.8)
  right_box=Rectangle(width=5.5,height=3.2,color=CRIMSON,fill_color=CRIMSON,fill_opacity=.07,stroke_width=2).shift(RIGHT*3.2)
  right_lbl=Text('It relates expectation values',font=SERIF,font_size=28,color=CRIMSON).move_to(right_box)
  right_lbl.set_max_width(4.8)
  divider=Line(UP*2.2,DOWN*2.2,color=SLATE,stroke_width=1.5)
  self.play(FadeIn(left_box,left_lbl),run_time=max(0.01,d*0.3))
  self.play(Create(divider),run_time=max(0.01,d*0.15))
  self.play(FadeIn(right_box,right_lbl),run_time=max(0.01,d*0.3))
  self.wait(max(0.01,d*0.25))
class B10_SDT(Scene):
 # B10 SDT retrofit: generic reveal with underline
 def construct(self):
  d=15.85
  self.add(bg(),ttl('Your turn. A normalized state has half'))
  stmt=Text('A normalized state has half its probability near x equa',font=SERIF,font_size=38,color=INK).move_to(ORIGIN)
  stmt.set_max_width(12)
  underline=Line(stmt.get_left()+DOWN*.32,stmt.get_right()+DOWN*.32,color=CRIMSON,stroke_width=2.5)
  self.play(Write(stmt),run_time=max(0.01,d*0.4))
  self.play(Create(underline),run_time=max(0.01,d*0.2))
  detail=Text('The mean is zero',font=SERIF,font_size=28,color=SLATE).shift(DOWN*1.4)
  detail.set_max_width(12)
  self.play(FadeIn(detail),run_time=max(0.01,d*0.2))
  self.wait(max(0.01,d*0.2))
