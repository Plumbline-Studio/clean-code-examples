# Every fix becomes a check

**The idea:** when you fix a mistake, you also write a small test that would have caught it.
Then a computer runs that test on every change, forever. The same mistake can't come back
without someone noticing.

**Why it matters:** fixing a bug once is easy. Keeping it fixed while people (and AI helpers)
keep changing the code is the hard part. A written note ("be careful with discounts") gets
forgotten. A test never forgets.

## What is in this folder

| File | What it is |
|---|---|
| `invoice.py` | A tiny invoice total. It had three bugs, now fixed. Each fix has a comment. |
| `test_invoice.py` | Tests for a normal day. |
| `test_fixes.py` | One test for each bug we fixed, named for the bug. This file only grows. |
| `fix_needs_check.py` | The rule as a check: a change that says it is a fix must add or change a test. |
| `test_fix_needs_check.py` | Tests for the rule itself. |

## Run it

You need Python 3. Nothing to install.

```
cd 01-every-fix-becomes-a-check
python3 -m unittest -v
```

You should see 11 tests pass.

Now try the rule. A fix with a test passes:

```
python3 fix_needs_check.py "fix: discount taken twice" invoice.py test_fixes.py
```

A fix with no test is refused:

```
python3 fix_needs_check.py "fix: discount taken twice" invoice.py
```

## Try breaking it

Open `invoice.py` and put the old bug back: take the discount off each line too. Run the tests.
`test_fix_1_discount_is_taken_once` fails and tells you which mistake came back.

## Use it in your own project

1. Keep a test file just for fixes (like `test_fixes.py`). Name each test for the bug.
2. Run `fix_needs_check.py` in CI on every pull request, with the pull request title and the
   list of changed files. See [`.github/workflows/check.yml`](../.github/workflows/check.yml).
3. When an AI helper fixes something, the same rule applies: no test, no merge.
