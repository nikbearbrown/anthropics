# SPEC — format_price

`format_price(cents: int) -> str`. Handles exactly these cases:

- `1299`  -> `"12.99 EUR"`
- `0`     -> `"0.00 EUR"`
- `10000` -> `"100.00 EUR"`
- `12345` -> `"123.45 EUR"`
- `-50`   -> raises `ValueError`

Rules: no dollar sign. No thousands separator. Always two decimals. Suffix ` EUR` (space then EUR). Negative input raises `ValueError`. Nothing else.
