def format_price(cents: int) -> str:
    if not isinstance(cents, int) or isinstance(cents, bool):
        raise TypeError("cents must be an int")
    sign = "-" if cents < 0 else ""
    n = abs(cents)
    dollars, remainder = divmod(n, 100)
    return f"{sign}${dollars:,}.{remainder:02d}"
