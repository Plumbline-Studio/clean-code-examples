"""The rule, as a check a computer can run: a change that says it is a fix must add or change a test.

    python3 fix_needs_check.py "fix: discount taken twice" invoice.py test_fixes.py   -> ok
    python3 fix_needs_check.py "fix: discount taken twice" invoice.py                 -> refused

The first argument is the change's title (a commit message or pull request title). The rest are
the files it changed. In a real project, CI passes these in on every pull request (see
.github/workflows/check.yml at the root of this repo).
"""

import re
import sys

FIX = re.compile(r"^\s*(fix|bugfix|hotfix)\b|\bfix(es|ed)?\b", re.IGNORECASE)
TEST = re.compile(r"(^|/)(test_[^/]+\.py|[^/]+_test\.py|[^/]+\.(test|spec)\.[jt]sx?)$")


def is_fix(title: str) -> bool:
    return bool(FIX.search(title))


def touches_a_test(files: list[str]) -> bool:
    return any(TEST.search(f) for f in files)


def check(title: str, files: list[str]) -> str | None:
    """None when the change is fine; otherwise one plain sentence saying what is missing."""
    if is_fix(title) and not touches_a_test(files):
        return "This change says it fixes something, but no test was added or changed. Add a test that fails without the fix."
    return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    problem = check(sys.argv[1], sys.argv[2:])
    print(problem or "ok")
    sys.exit(1 if problem else 0)
