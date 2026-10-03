# csv-shape — troubleshooting and edge cases

Consult this file when `csv_shape.py` returns output that looks wrong or refuses to run. Each section names a symptom, explains the underlying cause, and gives the workaround.

## No header row

`csv_shape.py` assumes the first row of the file is a header and reports every subsequent row in the `rows:` count. For a headerless CSV, the first data row will be misread as column names and the row count will be short by one.

Workaround: prepend a synthetic header before running the script, or accept that the first row will label the columns.

```bash
{ echo "c1,c2,c3"; cat data.csv; } > /tmp/with-header.csv
python3 csv_shape.py /tmp/with-header.csv
```

## Ragged rows (rows with fewer fields than the header)

The dtype guesser walks the body looking for the first non-empty value in column `i`. Short rows are skipped for that column via the `i < len(r)` guard, so ragged data will not raise an error — but a column that only appears in short rows will report `empty`.

If ragged rows are unexpected, inspect the file with `awk -F, '{print NF}' data.csv | sort -u` to see the distinct field counts.

## Quoted numbers

A value like `"42"` is stripped of quotes by `csv.reader` before `guess_dtype` sees it, so quoted integers and floats still resolve to `int` or `float`. A value like `"42 "` with an embedded space also resolves correctly, since `guess_dtype` calls `.strip()` first.

A value like `"1,234"` (thousands separator inside the number) will resolve to `str`, not `int` — the comma makes `int()` and `float()` both fail. Strip separators upstream if numeric typing matters.

## Tab-separated or pipe-separated files

`csv_shape.py` uses the default `csv.reader`, which splits on commas. A TSV file will parse as a single column whose values contain tab characters, and the `cols:` count will read as `1`.

Workaround: convert to CSV first, e.g. `tr '\t' ',' < data.tsv > /tmp/data.csv`, then run the script. Do not edit `csv_shape.py` to add a `--delimiter` flag; extending the script is out of scope for this skill.

## Encoding errors

The script opens files with the platform default encoding. A file written as UTF-16 or Latin-1 with non-ASCII bytes will raise `UnicodeDecodeError` on read.

Workaround: transcode to UTF-8 first, e.g. `iconv -f UTF-16 -t UTF-8 data.csv > /tmp/data.csv`.

## Dtype disagrees with the rest of the column

`guess_dtype` looks only at the first non-empty value. A column whose first row is `0` and whose remaining rows are `"low"`, `"medium"`, `"high"` will report `int`. This is by design — the script is a fast structural probe, not a full column scan.

For a column-wide dtype consensus, load the file into pandas (`pd.read_csv`) and inspect `df.dtypes`.

## Empty file or header-only file

An empty file prints `empty file` and exits with status `1`. A file with only a header prints `rows: 0`, the column count, and every column labelled `empty` — the script never found a non-empty value to guess from.

## BOM in the first column name

A UTF-8 BOM at the start of the file will appear as a prefix on the first column's name (e.g. `﻿name` instead of `name`). Strip the BOM at the shell before running: `sed -i '' '1s/^\xEF\xBB\xBF//' data.csv` on macOS, or open the file in an editor that normalizes on save.
