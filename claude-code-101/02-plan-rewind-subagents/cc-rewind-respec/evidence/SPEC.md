# dedupe.py — spec

`dedupe(items)` returns `items` with duplicates removed.

Two constraints:
1. **Preserve order**: the first occurrence of each item stays in place; later duplicates are dropped.
2. **Handle unhashable items**: elements like lists must be supported. Do not rely on hashing.

Do not modify tests.
