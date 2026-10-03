# Binary search — Mira

Binary search works by cutting the list in half each time. You start with the
whole list, look at the middle element, and compare it to the target. If the
middle is smaller, throw away the left half; if the middle is bigger, throw
away the right half. Keep going until you find it.

The midpoint is `(lo + hi) // 2`. The loop shrinks the range and stops when
the target is found or the range is empty.

Binary search is O(log n) because each step throws away half of what is left.
