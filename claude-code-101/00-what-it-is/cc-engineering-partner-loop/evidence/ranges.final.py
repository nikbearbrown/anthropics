def parse_range(s):
    """Parse '1-5' -> (1, 5). '7' -> (7, 7). '', reversed, or extra dashes is an error."""
    parts = s.split('-')
    if len(parts) == 1:
        return (int(parts[0]), int(parts[0]))
    if len(parts) != 2:
        raise ValueError(f"invalid range: {s!r}")
    start, end = int(parts[0]), int(parts[1])
    if start > end:
        raise ValueError(f"reversed range: {s!r}")
    return (start, end)
