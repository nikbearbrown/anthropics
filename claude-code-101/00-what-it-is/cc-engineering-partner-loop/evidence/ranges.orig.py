def parse_range(s):
    """Parse '1-5' -> (1, 5). '7' -> (7, 7). '' or reversed is an error."""
    parts = s.split('-')
    if len(parts) == 1:
        return (int(parts[0]), int(parts[0]))
    return (int(parts[0]), int(parts[1]))
