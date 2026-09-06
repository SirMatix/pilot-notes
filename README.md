# pilot-notes

Disposable standard-library-only Factory integration pilot. Install with
`python -m pip install --no-deps .`. Run `pilot-notes normalize "  Hello   World "`.
The approved target output is `Hello World` followed by one newline.

Normalization removes leading/trailing Unicode whitespace and replaces internal
whitespace runs with one ASCII space, preserving case, punctuation and all other
characters. Empty/whitespace-only input produces an empty string. No files or
network services are used. The initial skeleton intentionally lacks normalization;
unit tests pass, protected acceptance fails until the Engineer implements it.

Run `python -B -m unittest discover -s tests` and
`python -B -m unittest discover -s tests/acceptance` from the repository root.
No production deployment is intended.
