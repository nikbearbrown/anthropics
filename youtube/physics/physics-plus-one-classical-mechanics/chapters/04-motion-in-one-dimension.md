# Chapter 4 — Motion in One Dimension

*Everything moves. The question is: relative to what?*

---

You are sitting on a high-speed train. The rails blur beneath the window. The landscape slides past. And yet the coffee cup on the table in front of you sits perfectly still.

A person standing on the platform watches the train go by. To them, that cup is hurtling past at 280 kilometers per hour.

Who is right?

Both are. Not because physics is vague, or because truth is relative in some philosophical sense, but because motion is not a property of the cup. Motion is a *relationship* — between the cup and whatever you chose to measure it against. Change the measurement point and you change the answer, completely and correctly.

This is the foundation. Before you can say how fast something moves, or in what direction, you have to answer a prior question: moving relative to what? Physicists call the answer to that question a *reference frame*. Everything in this chapter — position, displacement, velocity, the information hidden in a graph — follows from choosing one.

<!-- → IMAGE: photograph or illustration of a passenger looking at a stationary coffee cup inside a moving train car, with a blurred platform visible through the window — caption should name the two reference frames explicitly (passenger's frame, platform observer's frame) and show that both are correct; the image should make the relativity of motion feel concrete before the formalism begins -->

---

## The Reference Frame

Stand in a stadium at sunset. The sun sinks toward the horizon. A friend in Brazil, on the opposite side of Earth, watches the same sun rise. The sun is the same object, emitting the same light. But *setting* or *rising* depends entirely on where you stand. This is not a metaphor for subjectivity. It is a precise physical statement: the description of motion depends on the observer's reference frame.

A reference frame is a coordinate system anchored to something you decide to treat as stationary. Usually you pick the ground, or the walls of a room, and call that your zero — your origin. Then every other object's position is measured as a distance and direction from that origin. The cup is one meter from the window. The window is 30 meters from the platform entrance. Position is always a comparison.

Here is what reference frames actually give you: they turn the vague word *here* into a number. Once you have a number, you can do arithmetic on it. And once you can do arithmetic on position, you can calculate how position changes — which is motion.

The most important thing to notice is this: two observers with different origins will assign different position numbers to the same object. You say the cup is at position 1 meter. I say it is at position 11 meters (because I put my origin 10 meters behind yours). We disagree about where it is. But if the cup moves half a meter to the right, we *both* record the same change: plus half a meter. The change in position does not depend on where you put the origin. Only the absolute position does.

<!-- → DIAGRAM: two number lines placed one above the other, both showing the same cup and the same wall; top line has origin at the cup's left (observer A), bottom line has origin 10 m to the right (observer B) — the cup reads position 1 m on the top line and position 11 m on the bottom; an arrow showing the cup moving 0.5 m right is drawn on both lines; both Δd arrows are identical in length and direction; student should see that absolute position differs but displacement is the same -->

That change in position has a name: *displacement*.

---

## Distance and Displacement

Displacement is defined as

$$\Delta d = d_f - d_0$$

where $d_0$ is the starting position and $d_f$ is the finishing position. The Greek letter $\Delta$ — delta — means *change in*. It appears throughout physics as a shorthand for "final minus initial."

Displacement is not the same as distance, and the difference is not pedantic.

Distance is the length of the actual path. If you walk to school via a winding route, distance is the sum of every step: 1.5 km west, then 0.8 km north, then 0.6 km east. Total distance: 2.9 km. Distance is always positive, because path length cannot be negative.

Displacement is the straight-line net change from start to finish. If school is 1.5 km west of your house, your displacement is 1.5 km west — regardless of the detours. If you then walk home, your displacement is zero. You ended where you began.

The trade-off is this: distance tells you how much ground the object covered. Displacement tells you where it actually ended up relative to where it started. You need both, and they answer different questions.

Now, displacement has a sign — positive or negative — because it has a direction. Before you can assign a sign, you have to make a choice: which direction is positive? The choice is arbitrary. You can call rightward positive, or leftward, or upward. What matters is that you pick one and stay consistent. The math will carry the direction for you after that.

**A worked example.** A cyclist rides 3 km west, then turns and rides 2 km east. Set east as positive, west as negative.

She starts at position $d_0 = 0$. After riding 3 km west, she is at $d = -3$ km. After riding 2 km east, she is at $d = -3 + 2 = -1$ km.

Displacement: $\Delta d = -1 - 0 = -1$ km. The negative sign means net movement westward — which is correct.

Distance: 3 + 2 = 5 km. Path length, always positive.

Notice what happened. We did not have to reason about direction separately. We made one choice at the start (east is positive), applied it consistently, and the displacement's sign told us the answer. This is how all vector arithmetic works: encode the direction in the sign, do the algebra, read the direction out at the end.

<!-- → DIAGRAM: overhead map view of a cyclist's round-trip — a dot at origin labeled "start", a curved winding path going left to a point labeled "−3 km", then a straight arrow going right back to "−1 km" labeled "final position"; the full winding path is labeled "distance = 5 km"; a single straight arrow from start to final position is labeled "displacement = −1 km (westward)"; student should see visually that distance follows the path while displacement is the straight net change -->

One misconception to head off. If an object travels out and comes back to exactly where it started, its displacement is zero. The distance is whatever the path length was. Zero displacement does not mean the object did not move. It means the object's net change in position is zero. The distinction will matter enormously when we calculate work, and again when we study momentum.

---

## Speed and Velocity

Speed is how fast an object's position changes. The formula is:

$$v_{\text{avg}} = \frac{\text{distance}}{\text{time}}$$

A car that covers 150 km in 3.2 hours has an average speed of 150 ÷ 3.2 = 47 km/h.

Velocity is the vector version of speed: it includes direction. Average velocity is:

$$\mathbf{v}_{\text{avg}} = \frac{\Delta d}{\Delta t} = \frac{d_f - d_0}{t_f - t_0}$$

The formula looks almost identical. The difference is that displacement appears in the numerator instead of distance — and displacement carries a sign.

Here is where the distinction bites. Suppose you drive 150 km to a city, then drive 150 km back home. Total distance: 300 km. Total displacement: 0 km. Average speed: 300 km divided by total time — some positive number. Average velocity: 0 km divided by total time — zero.

Same trip. Two very different numbers. Speed tells you how much ground you covered per unit of time. Velocity tells you your net progress in a direction per unit of time. If your displacement is zero, your average velocity is zero, regardless of how much you drove.

When would you care about each? Speed is the right quantity when you are thinking about fuel consumption, or how long a trip takes, or how far the tires have worn. Velocity is the right quantity when you are asking where the object ended up, or whether it is making progress toward a goal.

<!-- → TABLE: two-column table contrasting the 150 km round trip — rows: total distance (300 km / 300 km), total displacement (300 km / 0 km), average speed (300 km ÷ total time = some positive value / same), average velocity (300 km ÷ total time / 0 km ÷ total time = 0); left column for outbound leg only, right column for full round trip — student should see exactly where the two quantities diverge and why velocity collapses to zero on return -->

A second distinction, subtler but equally important: the difference between *average* and *instantaneous*.

The speedometer in a car does not show your average speed since you left home. It shows your speed *right now*. But what does "right now" mean for speed? Speed requires a time interval — distance over time. What is the distance in zero time? Zero. What is zero divided by zero?

This is not a trick question. It is the question that led Newton and Leibniz to invent calculus. The instantaneous speed is defined as the limit of average speed as the time interval shrinks toward zero — so small that the speed does not have time to change during the measurement. In practice, it means: what would the average speed be over a very, very short interval centered on this moment?

You do not need the calculus here. You need the concept: average velocity is computed over a finite interval and depends on the start and end points. Instantaneous velocity is the velocity at a single moment, and it is what the slope of a position-time graph gives you.

**A worked example.** Layla jogs 304 m north in 180 seconds.

Average velocity: $304 \text{ m} \div 180 \text{ s} = 1.7 \text{ m/s north}$.

If she had jogged the same 304 m north via a zigzag path, her average velocity would still be 1.7 m/s north. Velocity depends on displacement — start point and end point — not on the path between them.

Now imagine two joggers who cover the same start and end points in the same time: one by a straight path, one by a winding path. Same average velocity. Different average speeds. The one who wound around covered more distance in the same time.

This difference becomes crucial in two dimensions — a curved path and a straight path between the same endpoints have the same displacement and the same average velocity, but very different distances and average speeds.

---

## Reading Motion from a Graph

There is something worth pausing on. We have been talking about motion as numbers: position at this time, velocity over that interval. But there is another way to represent motion — geometrically. A graph turns motion into a shape, and the shape contains the same information as the numbers. Usually more efficiently.

The position-time graph puts time on the horizontal axis and position on the vertical axis. Each point on the graph is a statement: at this moment, the object was at this position. Connect the points and you get a line or a curve — the *trajectory* of the object as a function of time.

The slope of that line is the velocity.

Why? Slope is rise over run. On a position-time graph, rise is $\Delta d$ (change in position) and run is $\Delta t$ (change in time). The ratio $\Delta d / \Delta t$ is — by definition — average velocity. So the slope of a position-time graph is the average velocity over that interval.

If the line is straight, the velocity is constant. Steep slope: fast. Shallow slope: slow. Horizontal line (zero slope): the object is stationary. Negative slope: the object is moving in the negative direction — backward, or downward, or whatever you called negative when you set up the reference frame.

<!-- → CHART: four small position-time graphs arranged in a 2×2 grid — top left: steep positive slope labeled "fast, moving forward"; top right: shallow positive slope labeled "slow, moving forward"; bottom left: horizontal line labeled "stationary"; bottom right: steep negative slope labeled "fast, moving backward"; each graph has the same time axis; student should learn to read velocity magnitude and direction from slope shape alone, before touching numbers -->

If the line is curved, the velocity is changing. To find the instantaneous velocity at a single point on a curve, you draw a *tangent line* — a straight line that just grazes the curve at exactly that point, neither cutting through it nor pulling away. The slope of the tangent is the instantaneous velocity at that moment.

The velocity-time graph tells a different story. Time is still on the horizontal axis, but now velocity is on the vertical axis. The slope of a velocity-time graph is acceleration — the rate at which velocity changes. That is the subject of the next chapter.

But the velocity-time graph has a second secret: the *area* under the curve is displacement.

<!-- → CHART: two side-by-side velocity-time graphs — left: constant velocity (horizontal line at +0.5 km/min), with a shaded rectangle underneath labeled "area = displacement = +5 km"; right: linearly increasing velocity (a diagonal line from 0 to some value), with a shaded triangle underneath labeled "area = displacement = ½ × base × height"; caption should note that for any shape, area = displacement, and that the sign of velocity determines whether the area counts as positive or negative displacement -->

This takes a moment to see. Velocity has units of meters per second. Time has units of seconds. Multiply them: meters per second times seconds gives meters — displacement. If you plot velocity on the vertical axis and time on the horizontal axis, the area of a rectangle with height $v$ and width $t$ is $v \times t$, which is displacement. The area under the curve is the accumulated displacement over that time interval.

For a constant velocity, the shape under the curve is a rectangle. Easy. For a changing velocity, you break the region into rectangles and triangles, approximate, and in the limit you get the exact displacement — which is, again, the calculus, but the geometric intuition requires no calculus at all.

**A worked example.** A car drives toward school at a constant velocity of +0.5 km/min for 10 minutes, then returns at -0.5 km/min for 10 minutes.

On the position-time graph: a straight line with positive slope going up for the first 10 minutes, then a straight line with negative slope going back down. At 20 minutes, the car is back where it started.

On the velocity-time graph: a horizontal line at +0.5 km/min for 10 minutes, then a horizontal line at -0.5 km/min for 10 minutes.

Displacement from the area:
- Outbound area: $(+0.5)(10) = +5$ km.
- Return area: $(-0.5)(10) = -5$ km.
- Total: $+5 + (-5) = 0$ km.

Distance: the sum of absolute areas: $5 + 5 = 10$ km.

The position-time graph encodes the same information geometrically, in a different form. Both graphs are true; neither is more real than the other. Each reveals something the other obscures: the position graph shows where the car was; the velocity graph shows how its motion was structured.

---

## How It Fits Together

Start with the reference frame. You choose an origin and a positive direction. That choice is yours to make; no physics constrains it. Different choices give different numbers, but the same physical truths.

Once the frame is set, position becomes a number — a precise location measured from your origin. And once position is a number, you can take differences.

Distance is the total path length. Always positive, because it counts steps, not direction. Displacement is the net change in position: $\Delta d = d_f - d_0$. Can be positive, negative, or zero, depending on which way you ended up relative to where you started.

Speed is distance divided by time. Velocity is displacement divided by time. Same structure; different numerators. Speed is always positive. Velocity carries the sign of the displacement — and therefore carries the direction.

Graphs encode all of this as geometry. Slope of a position-time graph is velocity. Area under a velocity-time graph is displacement. These are not separate facts to memorize. They both follow from the definitions: slope is $\Delta d / \Delta t$, which is velocity; area of a velocity-time rectangle is $v \times t$, which is displacement.

The thread running through all of it: *direction matters*. Distance ignores it. Displacement encodes it. Speed ignores it. Velocity encodes it. Graphs display it in the sign of the slope. This insistence on direction is not bookkeeping. It is physics. A car traveling north at 60 km/h is in a genuinely different physical state from a car traveling south at 60 km/h. They have the same speed; they have opposite velocities; if both decelerate at the same rate, they will stop in different places. Direction is information.

**A fuller worked example, putting all of it together.** A student leaves school, which is 1.2 km east of her home. She jogs west — in the negative direction — at a constant 2.4 m/s for 8 minutes, stops for 2 minutes, then jogs west again for 4 minutes at the same speed. Where does she end up?

Set home as origin, east as positive. School is at $d_0 = +1200$ m.

Phase 1 (jog west, 8 min = 480 s):  
Velocity: $-2.4$ m/s.  
Displacement: $(-2.4)(480) = -1152$ m.  
Position after phase 1: $1200 + (-1152) = +48$ m. She is 48 m east of home.

Phase 2 (stop, 2 min):  
Displacement: 0.  
Position unchanged: +48 m.

Phase 3 (jog west, 4 min = 240 s):  
Velocity: $-2.4$ m/s.  
Displacement: $(-2.4)(240) = -576$ m.  
Position after phase 3: $48 + (-576) = -528$ m. She is 528 m *west* of home.

Total displacement: $-528 - 1200 = -1728$ m westward.  
Total distance: $1152 + 576 = 1728$ m. (Equal to the magnitude of displacement here because she never reversed direction — but this coincidence of magnitudes does not hold in general.)  
Average velocity: $-1728 \text{ m} \div 840 \text{ s} = -2.06$ m/s. Notice this is less than the jogging speed of 2.4 m/s in magnitude — because the two-minute stop contributed time without contributing displacement, pulling the average down.

The position-time graph for this motion: a descending line from (0 s, +1200 m) to (480 s, +48 m), then a horizontal line from (480 s, +48 m) to (600 s, +48 m), then another descending line from (600 s, +48 m) to (840 s, −528 m). Three segments, two slopes, one flat. The slopes are both negative and equal in magnitude, confirming the velocity was the same in both jogging phases.

<!-- → CHART: annotated position-time graph of the student's full journey — three labeled segments: "jogging (slope = −2.4 m/s)" from 0 to 480 s, "stopped (slope = 0)" from 480 to 600 s, "jogging (slope = −2.4 m/s)" from 600 to 840 s; a horizontal dashed line at d = 0 labeled "home"; the final point at (840 s, −528 m) labeled "528 m west of home"; student should see how the stop appears as a flat segment and how both jogging phases produce identical slopes confirming equal velocities -->

The velocity-time graph: $-2.4$ m/s from $t = 0$ to $t = 480$ s, then 0 from $t = 480$ to $t = 600$ s, then $-2.4$ m/s from $t = 600$ to $t = 840$ s. The area under this graph: $(-2.4)(480) + (0)(120) + (-2.4)(240) = -1152 + 0 + (-576) = -1728$ m. Matches the total displacement exactly.

---

## What the Next Chapter Requires

This chapter has given you the tools to *describe* motion: where something is, how far it traveled, how fast it is going, what direction. That is kinematics — the geometry of motion.

What it has not done is explain why motion changes. Why does the student slow down when she reaches a hill? Why does a ball thrown upward come back down? The answer requires a new concept: force. And the connection between force and change in velocity — not velocity itself, but change in velocity — is acceleration.

Acceleration is what the slope of a velocity-time graph measures. You have already read it off a graph in this chapter. The next chapter asks what causes it, and what happens when we follow that question all the way to Newton's three laws.

One preview worth holding. Notice that everything in this chapter involved *changes* in position and velocity, not the absolute values. Newton's laws will turn out to work the same way: they govern changes in velocity, not velocity itself. An object moving at constant velocity, with no acceleration, requires no force. This is counterintuitive — it feels like you need to keep pushing something to keep it moving. But that feeling comes from friction, which is itself a force opposing the motion. Strip friction away and constant velocity requires nothing. The chapter ahead will make that precise.

---

## What Would Change My Mind

Every experiment ever run confirms that motion is frame-dependent — that there is no absolute rest against which to measure it. If any experiment revealed a genuinely preferred reference frame (some state of absolute rest against which all motion could be defined absolutely), the foundational claim of this chapter would require revision. No such experiment has succeeded. Einstein's special relativity, rather than overturning the frame-dependence of motion, deepened it: not only is there no preferred position, there is no preferred clock either.

## Still Puzzling

We move through space at extraordinary speeds — Earth's surface spins at up to 460 m/s at the equator; Earth orbits the sun at 30 km/s; the solar system moves through the galaxy at roughly 230 km/s. Yet we feel stationary. The brain chooses a reference frame automatically, anchoring perception to the immediate environment. This works well enough for daily life. It becomes actively misleading in physics, where the chosen reference frame must be explicit and the choice must be justified. How the brain settles on its implicit reference frames — and why those frames feel absolute rather than chosen — is a question that sits at the intersection of physics, neuroscience, and the philosophy of perception. Physics can describe the frames. It cannot yet fully explain why one feels more real than another.

---

## Exercises

### Warm-up

**1.** A dog runs 8 m east, then 3 m west. Set east as positive. Calculate: (a) total distance traveled, (b) displacement, (c) magnitude of displacement. Which of your three answers could be zero even if the dog kept running? Which could be negative?

*Tests: distance vs. displacement, sign convention.*

**2.** A car covers 240 km in 4 hours. A second car covers 240 km in 3 hours but drives in the opposite direction. Do the two cars have the same average speed? The same average velocity? Explain without calculating.

*Tests: speed vs. velocity, direction as essential information.*

**3.** A position-time graph shows a straight horizontal line at $d = +5$ m for 10 seconds. What is the object's velocity? What is its displacement over those 10 seconds? What is the distance it travels?

*Tests: reading zero velocity from a graph; displacement and distance when stationary.*

**4.** A velocity-time graph shows a constant velocity of $+3$ m/s for 6 seconds, followed immediately by $-3$ m/s for 6 seconds. Without calculating, what is the total displacement? What is the total distance?

*Tests: area under a velocity-time graph; signed vs. unsigned area.*

---

### Application

**5.** You jog from your house to a coffee shop 600 m north in 5 minutes, buy coffee, then jog back home in 6 minutes. (a) What is your total distance? (b) What is your total displacement? (c) What is your average speed for the whole trip? (d) What is your average velocity for the whole trip? (e) Why does the answer to (d) feel like a cheat?

*Tests: all four quantities for a round trip; why average velocity collapses on return.*

**6.** A position-time graph has two straight segments: from (0 s, 0 m) to (5 s, 20 m), then from (5 s, 20 m) to (12 s, 6 m). (a) Calculate the velocity during each segment. (b) Is the object moving in the same direction in both segments? (c) Calculate the average velocity over the full 12 seconds using total displacement and total time.

*Tests: extracting velocity as slope; sign change as direction reversal; average vs. segment velocity.*

**7.** A velocity-time graph shows a straight line increasing from 0 m/s at $t = 0$ to 20 m/s at $t = 10$ s. Estimate the displacement during this interval. (Hint: the shape under the line is a triangle. Area of a triangle = ½ × base × height.)

*Tests: area under a non-rectangular velocity-time curve; geometric reasoning.*

**8.** Two trains leave the same station at the same time. Train A travels north at a constant 80 km/h. Train B travels south at a constant 80 km/h. After 2 hours: (a) Are their speeds the same? (b) Are their velocities the same? (c) What is each train's displacement? (d) How far apart are they?

*Tests: same speed, opposite velocity; displacement as a signed quantity.*

---

### Synthesis

**9.** A ball is thrown straight up. It rises for 2 seconds, reaches its highest point, then falls back to the thrower's hand in another 2 seconds. Take upward as positive. (a) What is the ball's displacement over the full 4 seconds? (b) What is the distance traveled? (c) What is the average velocity over the full trip? (d) At the highest point, the ball's speed is momentarily zero. What does this mean for the slope of the position-time graph at that instant? (e) Sketch what the position-time graph looks like — is it a straight line or a curve? What does the shape tell you about whether velocity is constant?

*Tests: displacement vs. distance on a reversal; instantaneous velocity = zero at turning point; curved graph = changing velocity.*

**10.** Two cyclists start at the same point and both reach a finish line 3 km away in exactly 20 minutes. Cyclist A takes a straight path. Cyclist B takes a winding path through the park that is 4 km long. (a) Do they have the same average velocity? (b) Do they have the same average speed? (c) On a position-time graph (measuring straight-line distance from start to finish), how would their lines compare? (d) If you were tracking their actual paths on a map, how would the graphs differ?

*Tests: velocity depends on displacement; speed depends on distance; same endpoints, different paths.*

---

### Challenge

**11.** A satellite orbits Earth at a constant speed of 7,800 m/s, completing one full orbit every 90 minutes. (a) What is its average speed over one full orbit? (b) What is its average velocity over one full orbit? (c) Over half an orbit? (d) Is it possible for an object to have a constant speed but a continuously changing velocity? Use the satellite to make the case. This distinction will become the foundation of Chapter 6 (circular motion) — write one sentence predicting what concept Chapter 6 will need to introduce to explain it.

*Tests: speed vs. velocity for circular motion; displacement zero after full orbit; preview of centripetal acceleration.*

---

## LLM Exercise — Chapter 4: Motion in One Dimension (Physics Demonstrations Notebook Project)

**Project:** Physics Demonstrations Notebook.
**What you're building this chapter:** the ramp-and-flat-surface position-time demo — visual evidence of constant acceleration vs. constant velocity.
**Tool:** **Claude Project** for the entry. Phone for video. Optional **Claude Code** to digitize and graph.

---

**The Prompt:**

```
Chapter 4 demo for my Physics Demos Notebook. Notebook Charter is
in this Claude Project. Chapter 4 taught: position and reference
frames; speed vs. velocity (direction matters for velocity);
average vs. instantaneous; reading position-time and velocity-time
graphs (slope of x-t = velocity; slope of v-t = acceleration; area
under v-t = displacement).

**The Demo:** Roll a ball down a ramp onto a flat surface. Measure
position at equal time intervals. Compare ramp segment (constant
acceleration) to flat segment (approximately constant velocity).

**Materials:**
- A ramp: a textbook on a few magazines, or a board on books, or
  a hardcover book propped at one end.
- A ball that rolls smoothly: marble, ping-pong ball, small
  rubber ball.
- A flat surface continuous with the ramp's foot.
- A measuring tape or ruler. Mark the surface at 10 cm intervals
  with painter's tape or chalk.
- A phone with video recording (or a stopwatch and patience).

**Procedure:**

1. Set up: ramp angle ~10–20 degrees. Mark positions at 10 cm
   intervals from the top of the ramp through the flat surface.
   Total length: aim for 60–80 cm.

2. Predict before observing: The ball should accelerate down the
   ramp (gravity component); it should decelerate slightly on the
   flat (friction). Predict the time to traverse each marked
   interval. Will the times be equal? Decreasing? Increasing?

3. Run the experiment: release the ball from a consistent starting
   point. Record video at 30 or 60 fps. Run 5 trials.

4. Analyze: For each trial, identify the frame the ball passes
   each mark. Compute the time to traverse each interval. Tabulate.

5. Compute average velocity for each interval (distance / time).
   Plot velocity vs. time (centered at midpoint of each interval).

**Use Claude as a thinking partner:**
- Before the demo: "Predict what the velocity-time graph should
  look like for ramp + flat surface. Sketch it in words."
- After the demo: "Here are my measured times and velocities.
  Does the data fit constant acceleration on the ramp and
  approximately constant velocity on the flat? Where does the
  data deviate from the prediction, and what physical effect
  could cause the deviation (slipping, spinning, ramp-foot bump)?"

**Notebook entry should include:**
- The materials and setup (with photo).
- The prediction sketched in advance.
- The data table (time per interval, computed velocity).
- The position-time and velocity-time graphs (sketched by hand
  or generated with Claude Code).
- The verdict: constant acceleration on the ramp? Constant
  velocity on the flat? Magnitudes that make sense?
- One thing that didn't work the first time and what you changed.

End with one specific question the demo raised: e.g., "Why does
the ball seem to lose energy at the ramp-foot transition?" These
questions become the threads for later chapters.
```

---

**What this produces:** A complete demo entry with data, graphs, and analysis. The transition from constant acceleration to constant velocity at the ramp foot is one of physics's most teachable moments — the demo makes it tactile.

**How to adapt this prompt:**

- *For your own project:* Smartphone video at 60 fps gives 16.7 ms time resolution — plenty for marble-on-ramp. If you don't have video, use a stopwatch but expect noisier data.
- *For ChatGPT / Gemini:* Works as written.
- *For Claude Code:* If you want to digitize the video frame-by-frame and produce real position-time graphs, Claude Code with OpenCV or video-frame extraction is the right tool. Optional but valuable.
- *For a Claude Project:* The entry goes in the notebook. Photos commit to the project folder.

**Connection to previous chapters:** Ch 2's "model vs. reality" discipline gets exercised — the constant-velocity model will fail on the ramp; the constant-acceleration model will fail on the flat (because of friction).

**Preview of next chapter:** Chapter 5 is acceleration in detail. You'll do a free-fall demo — drop two objects of very different mass and time them. The chapter's claim that g is mass-independent gets tested.

---

## AI Wayback Machine

**Galileo Galilei** worked out the kinematics of falling bodies in the late 16th century.

**Run this:**

```
Who is Galileo Galilei, and how does their work connect to motion
in one dimension we covered in this chapter? Keep it to three
paragraphs. End with the single most surprising thing about their
career or ideas.
```

→ Search **"Galileo Galilei"** on Wikipedia.

**Now make the prompt better.** Try one of these:

- Ask it to walk through one of Galileo Galilei's experiments or arguments in detail.
- Add a constraint: "Answer including criticisms or limits of Galileo Galilei's framework."

What changes? What gets better? What gets worse?

---

*Tags: kinematics; reference-frames; vectors; scalars; displacement; velocity; graphing-motion; one-dimensional-motion*
