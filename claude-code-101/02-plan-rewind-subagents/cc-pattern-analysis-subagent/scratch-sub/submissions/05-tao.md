# Binary search — Tao

Binary search needs the list to be sorted first — that is the precondition.
On each step you compare the middle element to the target and eliminate the
half that cannot contain it. The invariant is that the target (if present)
lives in `[lo, hi)` at every step; the loop terminates when `lo == hi`.

I use `mid = lo + (hi - lo) // 2`. That avoids the overflow that
`(lo + hi) // 2` can hit for very large lists.

Time is O(log n), extra space is O(1).
