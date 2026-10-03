# Q3 platform review — the queue backlog

Support tickets to first-response climbed from 42 minutes in July
to 121 minutes by the end of September. Two things happened at
once: the free tier grew nineteen percent, and the on-call rotation
lost two engineers to a hiring freeze. The auto-triage classifier
kept up on volume — it labelled 94% of tickets correctly — but the
label it uses for "needs a human answer" is a heuristic on token
count, and paying customers writing short precise questions
were routed into the low-priority queue by accident.

We tried three fixes. Rotating unassigned tickets to the on-call
pager fixed the tail but doubled interruption cost. Adding a second
classifier changed the failure mode but not the rate. What worked
was smaller: a per-plan priority floor, so a paid ticket never
falls below "medium" no matter what the classifier says.

The floor is now live. Backlog is 63 minutes and falling. The
lesson is that classifier accuracy at 94% still hid a systematic
misroute at the tail, and the tail was where our paying customers
were. We are keeping the classifier and we are keeping the floor.
