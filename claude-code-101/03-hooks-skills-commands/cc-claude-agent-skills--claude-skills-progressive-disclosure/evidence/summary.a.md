# Summary — Q3 platform review

Support first-response time climbed from 42 to 121 minutes in Q3, driven by 19% free-tier growth and losing two on-call engineers to a hiring freeze. The auto-triage classifier was 94% accurate overall, but its token-count heuristic for "needs a human" misrouted paying customers who wrote short, precise questions into the low-priority queue.

Rotating unassigned tickets to on-call fixed the tail but doubled interruption cost; a second classifier changed the failure mode but not the rate. The fix that worked was a per-plan priority floor — paid tickets never drop below "medium" regardless of classifier output. Backlog is now 63 minutes and falling.

Lesson: 94% classifier accuracy still hid a systematic misroute at the tail, exactly where paying customers were. Both classifier and floor stay.
