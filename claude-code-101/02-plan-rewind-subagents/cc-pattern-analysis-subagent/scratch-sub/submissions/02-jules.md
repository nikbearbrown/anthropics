# Binary search — Jules

Take a sorted list. Look at the element in the middle, using
`mid = (lo + hi) // 2`. If it matches the target, return it. Otherwise, pick
the half that could still contain the target, and repeat on that half.

We know the target is inside the current window at every step, and the window
gets smaller, so we cannot loop forever. When the window has one element and
it is not the target, the target is not there.

Complexity: O(log n) time.
