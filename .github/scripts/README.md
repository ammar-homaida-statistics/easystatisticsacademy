# Mathematical placeholder inventory

Run the read-only regression check from the repository root:

```sh
python .github/scripts/validate_math_placeholders.py
python .github/scripts/validate_math_placeholders.py --details
python .github/scripts/validate_math_placeholders.py --inventory
python -m unittest discover -s .github/scripts -p 'test_math_placeholders.py' -v
```

Python 3.9+ is sufficient; the new validator and tests use only the standard
library. `--root PATH` inspects a different checkout and `--baseline PATH` selects
an explicit baseline. The script never edits lessons, reconstructs formulas, or
writes a baseline. `--inventory` emits JSON to standard output for auditing and
does **not** apply the CI gate; CI uses the default checking mode.

The observed damaged expressions are literal private-use tokens containing
U+EA01, an ASCII integer, and U+EA02 (for example, `\uea010\uea02`). The validator
also detects unmatched U+EA01/U+EA02 delimiters. It scans Markdown and HTML source,
including templates, and excludes `.github`, Git metadata, generated `_site`
output, and dependency/cache directories. It does not certify formula accuracy
or identify every possible kind of mathematical rendering damage.

The baseline in `.github/math-placeholder-baseline.json` records the original
commit and each token's count on each affected source page. That original source
contains 702 occurrences across 108 pages:

| Section | Affected pages | Occurrences |
| --- | ---: | ---: |
| descriptive | 7 | 27 |
| inference | 51 | 372 |
| modeling | 6 | 6 |
| probability | 44 | 297 |

Existing debt passes. A token on a new page, a new token ID on an affected page,
or an increased count for an existing token fails. Removing placeholders or
changing line numbers passes. Decreases on one page or token cannot offset an
increase elsewhere. Failures include file paths, line numbers, and counts.

Treat the baseline as a reviewed inventory, not a budget for new damage. When
formulas are repaired in a future PR, reduce or remove the corresponding baseline
entries in that same PR; do not increase allowances. Without reducing those
entries, the count-based gate would still permit the original count on that page.
Review changes to the baseline along with changes to lessons. Exit codes are
`0` for no additions, `1` for newly introduced markers, and `2` for a scan or
baseline error.
