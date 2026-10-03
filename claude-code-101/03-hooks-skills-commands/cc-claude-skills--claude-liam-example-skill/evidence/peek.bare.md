# Peek: sales.csv

- **Path:** `sales.csv`
- **Rows:** 9 data rows (+ 1 header) — 10 lines total
- **Columns (6):** `rep`, `region`, `quarter`, `sold`, `returned`, `net`

## Header
```
rep,region,quarter,sold,returned,net
```

## First rows
| rep | region | quarter | sold | returned | net |
|---|---|---|---|---|---|
| A. Reyes | west | Q1 | 148 | 12 | 136 |
| K. Patel | east | Q1 | 203 | 31 | 172 |
| J. Choi  | west | Q1 | 111 | 4  | 107 |
| A. Reyes | west | Q2 | 166 | 9  | 157 |
| K. Patel | east | Q2 | 197 | 44 | 153 |

## Last rows
| rep | region | quarter | sold | returned | net |
|---|---|---|---|---|---|
| J. Choi  | west | Q2 | 124 | 3  | 121 |
| A. Reyes | west | Q3 | 171 | 7  | 164 |
| K. Patel | east | Q3 | 188 | 52 | 136 |
| J. Choi  | west | Q3 | 138 | 2  | 136 |

## Quick notes
- 3 reps × 3 quarters (Q1–Q3) = 9 rows, fully balanced panel.
- Regions: `west` (A. Reyes, J. Choi), `east` (K. Patel).
- `net` = `sold` − `returned` holds for every row.
- K. Patel has notably higher return counts (31, 44, 52) than the west reps (single digits).
