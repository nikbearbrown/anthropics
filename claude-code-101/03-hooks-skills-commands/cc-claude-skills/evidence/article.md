# Q3 platform review — engineering all-hands notes

Last quarter our API p95 latency drifted from 180 ms to 340 ms. The cause was
not the code we merged — the two features that shipped were both well-tested
and behind flags. It was the flags themselves. The evaluator we chose eighteen
months ago fetches its rules from a config service on every request, and we
had crossed a threshold where that config service began to throttle us during
the daily 09:00 traffic spike.

The team spent six weeks arguing whether to replace the evaluator (a big
migration, no shipping features for a quarter) or to cache its results (small
change, unclear correctness implications when flags update). We picked the
cache. We wrote it in a week, wrote the invalidation contract in another
week, and shipped it behind its own flag. p95 is back to 190 ms and holding.

Two things came out of this that generalize. First: instrument the machinery
you did not write. We had beautiful graphs of our own service and none of
the config service that was actually slow — the outage was invisible for
three days on our dashboards. Second: when a debate stalls, run the small
experiment. The cache took less time to build than the argument about whether
to build it took to have.

Next quarter we will audit every third-party client we depend on for the same
pattern — hidden per-request work behind an API that looks free.
