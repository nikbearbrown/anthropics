# csv-shape — a tiny CSV inspector

`csv_shape.py` reads any CSV and prints its shape: rows, columns, column
names, and the dtype guessed from the first non-empty value in each column.
It stays under 60 lines and has no dependencies outside the standard library.

We are building a Claude Code skill at `skills/csv-shape/` so future sessions
know when to reach for `csv_shape.py` instead of writing pandas one-liners.
