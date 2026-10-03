## What
Q3 platform review found that API response times nearly doubled last quarter — not from anything we shipped, but from a third-party configuration service silently throttling our feature-flag system during the daily morning traffic spike. The team diagnosed the cause, chose a small cache-based fix over a multi-quarter migration, and restored performance with about two weeks of build time.

## Why it matters
The regression hit customer-facing latency and went undetected on our own dashboards for three days, because we instrument the code we wrote but not the dependencies it calls. The larger cost was internal: a six-week debate over how to fix it consumed more engineering time than the fix itself, and that pattern will keep recurring across the org unless we change how we resolve stalled architecture calls.

## What's new
Latency is back at pre-regression levels and holding. Two operating principles came out of the postmortem and are being adopted by the platform team: instrument every dependency, not just the code we own; and when a debate stalls between a large option and a small one, run the small experiment before extending the argument. Next quarter engineering will audit every third-party client we depend on for the same class of hidden per-request work.

## What to do
Endorse the dependency audit as a Q4 priority so it is not displaced by feature commitments, and reinforce the "run the small experiment" norm the next time a team escalates a stalled build-versus-buy decision. There is no budget or hiring ask attached — the value is a clear signal from you that this operating change has executive backing.
