# Binary search — Omar

Divide the array in half. Look at the middle: `mid = (lo + hi) // 2`. If the
middle is the target, you found it. Otherwise you know which half to search
next, because the array is sorted.

You keep dividing until the halves have length one. Then you know if the
target is present. Big-O is n log n in the worst case, log n in the best
case, from my notes.
