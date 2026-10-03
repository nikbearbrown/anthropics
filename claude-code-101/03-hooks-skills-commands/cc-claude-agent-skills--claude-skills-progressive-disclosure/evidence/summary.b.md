## What
Support first-response time nearly tripled in Q3 (42 to 121 minutes) after free-tier growth and a hiring freeze coincided with a subtle auto-triage misroute that dropped short paid-customer tickets into the low-priority queue.

## Why it matters
A 94% classifier accuracy masked a systematic tail failure that hit paying customers specifically, meaning the metric looked healthy while revenue-critical users waited longest.

## What's new
A per-plan priority floor is live, guaranteeing that paid tickets never fall below "medium" regardless of classifier output; backlog has already dropped to 63 minutes and is still falling.

## What to do
Keep both the classifier and the floor in place, and treat aggregate accuracy as insufficient on its own — segment tail-latency by plan to catch similar misroutes early.
