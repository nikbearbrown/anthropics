def dedupe(items):
    result = []
    seen = []
    seen_hashable = set()
    for item in items:
        try:
            if item in seen_hashable:
                continue
            seen_hashable.add(item)
        except TypeError:
            if any(item == s for s in seen):
                continue
        seen.append(item)
        result.append(item)
    return result
